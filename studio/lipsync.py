#!/usr/bin/env python3
"""lipsync.py — make the mouth match the voice, or decide not to.

The problem it solves: a shot is generated silent from a still, then a VO line is
laid over it. The mouth moves on its own schedule. This module does the three
things that actually fix that, in cost order:

  1. `plan`     — tells you which shots even need it (mouth in frame) and what the
                  pass will cost. Most films need 3-6 shots, not 40.
  2. `prepare`  — conforms the chosen clips to exactly what every engine wants:
                  25 fps, 16 kHz mono wav, face-croppable. This is the step people
                  get wrong; MuseTalk and LatentSync are both trained at 25 fps.
  3. `run`      — shells out to the best engine the machine can hold, and records
                  the LSE-C / LSE-D acceptance numbers for each output.

Engine choice is a VRAM ladder, all numbers from the repos' own READMEs:

    18 GB  bytedance/LatentSync 1.6   512x512, sharpest          Apache-2.0
     8 GB  bytedance/LatentSync 1.5                              Apache-2.0
     4 GB  TMElyralab/MuseTalk        256x256 face region        no licence file
     0 GB  wav2lip-onnx-HQ            CPU, 96x96 mouth, soft     no licence file

Both are trained on English audiovisual data (LRS2 / VoxCeleb2 / HDTF), which is
why English is the easier case and Persian accent is the harder one.

    python3 studio/lipsync.py check
    python3 studio/lipsync.py plan    <project>
    python3 studio/lipsync.py prepare <project> --shots 3,7,12
    python3 studio/lipsync.py run     <project> --shots 3,7 --repo ~/MuseTalk
"""
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

ENGINES = {
    "latentsync16": {
        "repo": "bytedance/LatentSync", "tag": "1.6", "vram_gb": 18, "license": "Apache-2.0",
        "face": "512x512", "sec_per_8s": None, "run":
            "./inference.sh    # set video/audio/output in the config first",
        "quality": "best detail, fixes the 1.5 blurriness",
    },
    "latentsync15": {
        "repo": "bytedance/LatentSync", "tag": "1.5", "vram_gb": 8, "license": "Apache-2.0",
        "face": "256x256", "sec_per_8s": None, "run":
            "./inference.sh    # set video/audio/output in the config first",
        "quality": "good, softer output",
    },
    "musetalk": {
        "repo": "TMElyralab/MuseTalk", "tag": "v1.5", "vram_gb": 4, "license": "none stated",
        "face": "256x256", "sec_per_8s": 300,
        "run": ("python -m scripts.inference --inference_config {cfg} --result_dir {out} "
                "--unet_model_path {repo}/models/musetalkV15/unet.pth "
                "--unet_config {repo}/models/musetalkV15/musetalk.json --version v15"),
        "quality": "best value: 4 GB card, ~5 min per 8 s, fp16",
    },
    "wav2lip_onnx": {
        "repo": "instant-high/wav2lip-onnx-HQ", "tag": "2025-06", "vram_gb": 0,
        "license": "none stated", "face": "96x96", "sec_per_8s": None,
        "run": "python inference_onnxModel_V2.py --video {video} --audio {wav} --output {out}",
        "quality": "only CPU option; soft mouth, fine for wide shots",
    },
}

GPU_USD_PER_H = 0.35          # a 12-16 GB card, on-demand, 2026 pricing order of magnitude

MOUTH_RISK = re.compile(r"\b(face|faces|close[- ]?up|portrait|eyes|lips|mouth|smile|"
                        r"turns? to camera|looks? at (?:the )?camera|chin|jaw)\b", re.I)


# ---------------------------------------------------------------- probing ----
def _kit():
    """filmkit's probe helpers use module-level FF/FP, which only `main()` sets.
    Importing it means we have to wire the binaries ourselves or probe() gets None."""
    sys.path.insert(0, str(ROOT / "studio"))
    import filmkit
    filmkit.FF = filmkit.ffmpeg_bin()
    filmkit.FP = filmkit.ffprobe_bin()
    return filmkit


def gpu_vram_gb() -> float:
    exe = shutil.which("nvidia-smi")
    if not exe:
        return 0.0
    try:
        p = subprocess.run([exe, "--query-gpu=memory.total", "--format=csv,noheader,nounits"],
                           capture_output=True, text=True, timeout=20)
        vals = [int(x) for x in re.findall(r"\d+", p.stdout)]
        return max(vals) / 1024 if vals else 0.0
    except Exception:                              # noqa: BLE001
        return 0.0


def pick(vram_gb: float, prefer: str | None = None) -> str:
    if prefer:
        if prefer not in ENGINES:
            raise SystemExit(f"unknown engine {prefer}; {list(ENGINES)}")
        return prefer
    if vram_gb >= 18:
        return "latentsync16"
    if vram_gb >= 8:
        return "latentsync15"
    if vram_gb >= 4:
        return "musetalk"
    return "wav2lip_onnx"


# ---------------------------------------------------------------- project ----
def load_project(name: str) -> tuple[Path, dict]:
    d = (ROOT / "films" / name).resolve()
    pj = d / "project.json"
    if not pj.exists():
        raise SystemExit(f"no project.json in {d}")
    return d, json.loads(pj.read_text(encoding="utf-8"))


def candidates(proj: dict) -> list[dict]:
    """A shot needs lip sync when it has speech AND a reason to think the mouth shows."""
    out = []
    for s in proj.get("shots", []):
        text = (s.get("narration") or "").strip()
        if not text:
            continue
        blob = " ".join(str(s.get(k) or "") for k in ("motion", "still_key", "note"))
        risk = 2 if MOUTH_RISK.search(blob) else 1
        out.append({"shot": int(s["n"]), "risk": risk, "clip": s.get("clip"),
                    "chars": len(text), "text": text})
    out.sort(key=lambda r: (-r["risk"], r["shot"]))
    return out


# ---------------------------------------------------------------- commands ----
def cmd_check(a) -> None:
    v = gpu_vram_gb()
    print(f"GPU VRAM: {v:.1f} GB" if v else "GPU: none (nvidia-smi not found)")
    try:
        print(f"ffmpeg:   {_kit().ffmpeg_bin()}")
    except SystemExit:
        print("ffmpeg:   MISSING — install it or set FFMPEG=")
    for k, e in ENGINES.items():
        mark = "<= fits" if v >= e["vram_gb"] else ""
        print(f"  {k:13s} needs {e['vram_gb']:>2} GB  {e['license']:12s} {e['face']:8s} {mark}")
    print(f"\nchoice on this machine: {pick(v)}")
    if v < 4:
        print("no GPU -> only wav2lip_onnx runs here. Expect it to be slow and soft;")
        print("the cheaper fix is editorial: put the line over the listener (L-cut).")


def cmd_plan(a) -> None:
    d, proj = load_project(a.name)
    rows = candidates(proj)
    if not rows:
        print("no narrated shots — nothing to lip-sync")
        return
    eng = pick(gpu_vram_gb(), a.engine)
    e = ENGINES[eng]
    # measure real clip lengths where we can
    filmkit = _kit()
    total_s = 0.0
    for r in rows:
        clip = d / (r["clip"] or "")
        r["dur_s"] = 0.0
        if clip.exists():
            try:
                r["dur_s"] = round(filmkit.duration_of(str(clip)), 2)
            except Exception:                      # noqa: BLE001
                r["dur_s"] = 0.0
        if not r["dur_s"]:
            takes = next((s for s in proj["shots"] if int(s["n"]) == r["shot"]), {}).get("takes") or []
            r["dur_s"] = round(float(takes[0].get("duration_s") or 0), 2) if takes else 0.0
        total_s += r["dur_s"] or 4.0
    est_min = (total_s / 8.0) * (e["sec_per_8s"] or 0) / 60 if e["sec_per_8s"] else None
    plan = {"project": proj.get("name"), "engine": eng, "rows": rows,
            "total_video_s": round(total_s, 1),
            "est_gpu_min": round(est_min, 2) if est_min else None,
            "est_usd": round((est_min or 0) / 60 * GPU_USD_PER_H, 3)}
    out = d / "qc" / "lipsync_plan.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(plan, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"engine: {eng}  ({e['license']}, needs {e['vram_gb']} GB)\n")
    print(f"{'shot':>4} {'risk':>4} {'dur':>6}  text")
    for r in rows:
        print(f"{r['shot']:>4} {'high' if r['risk'] > 1 else 'low':>4} {r['dur_s']:>5.1f}s  "
              f"{r['text'][:56]}")
    print(f"\n{len(rows)} shots, {total_s:.1f}s of video", end="")
    if est_min:
        print(f"  ~{est_min:.1f} min on GPU  ~${plan['est_usd']}")
    else:
        print("  (this engine does not publish a speed; measure it once and fill it in)")
    print(f"plan -> {out.relative_to(ROOT)}")
    print("\ntip: take only the 'high' rows. A line over the listener needs none of this.")


def _conform(src: Path, dst_video: Path, dst_wav: Path, vo: Path | None = None) -> dict:
    """25 fps video + 16 kHz mono wav, which is what every engine was trained on.

    The clips we generate are silent, so there is nothing to extract from them: the
    wav this produces is the *timing* track (silence of the same length). The real
    voice comes from voice.py and is passed to the engine separately."""
    kit = _kit()
    ff = kit.ffmpeg_bin()
    subprocess.run([ff, "-y", "-v", "error", "-i", str(src), "-r", "25",
                    "-c:v", "libx264", "-crf", "16", "-pix_fmt", "yuv420p", str(dst_video)],
                   check=True, timeout=1800)
    dur = kit.duration_of(str(src)) or 1.0
    if vo is not None and vo.exists():
        subprocess.run([ff, "-y", "-v", "error", "-i", str(vo), "-ac", "1",
                        "-ar", "16000", "-c:a", "pcm_s16le", str(dst_wav)],
                       check=True, timeout=600)
        source = f"vo:{vo.name}"
    elif kit.probe(str(src)).get("has_audio"):
        subprocess.run([ff, "-y", "-v", "error", "-i", str(src), "-vn", "-ac", "1",
                        "-ar", "16000", "-c:a", "pcm_s16le", str(dst_wav)],
                       check=True, timeout=600)
        source = "extracted"
    else:
        subprocess.run([ff, "-y", "-v", "error", "-f", "lavfi", "-i",
                        "anullsrc=r=16000:cl=mono", "-t", f"{dur:.3f}",
                        "-c:a", "pcm_s16le", str(dst_wav)], check=True, timeout=600)
        source = "silence"
    return {"dur_s": round(dur, 3), "audio": source}


def cmd_prepare(a) -> None:
    """Conform the chosen clips to 25 fps + 16 kHz mono, and write the engine config."""
    d, proj = load_project(a.name)
    want = {int(x) for x in a.shots.split(",")} if a.shots else None
    rows = [r for r in candidates(proj) if (want is None or r["shot"] in want)]
    if not rows:
        raise SystemExit("nothing selected")
    out_dir = d / "work" / "lip"
    (out_dir / "in").mkdir(parents=True, exist_ok=True)
    (out_dir / "out").mkdir(parents=True, exist_ok=True)
    made = []
    for r in rows:
        clip = d / (r["clip"] or "")
        if not clip.exists():
            print(f"  s{r['shot']:02d} no clip yet, skipped")
            continue
        v = out_dir / "in" / f"s{r['shot']:02d}.mp4"
        w = out_dir / "in" / f"s{r['shot']:02d}.wav"
        vo = d / "audio" / "vo" / f"s{r['shot']:02d}.mp3"
        info = _conform(clip, v, w, vo if vo.exists() else None)
        if vo.exists():
            vlen = _kit().duration_of(str(w))
            if vlen > info["dur_s"] + 0.1:
                print(f"    ! VO is {vlen:.2f}s but the shot is {info['dur_s']:.2f}s — "
                      f"hold the shot or trim the line")
        made.append((r["shot"], v, w))
        print(f"  s{r['shot']:02d} -> {v.relative_to(d)} + {w.name}  "
              f"({info['dur_s']:.2f}s, audio {info['audio']})")
    if not made:
        raise SystemExit("no clips to prepare")

    cfg = out_dir / "in" / "musetalk.yaml"
    cfg.write_text("task_0:\n" + "".join(
        f"  - video_path: {v}\n    audio_path: {w}\n    bbox_shift: 0\n"
        for _, v, w in made), encoding="utf-8")
    print(f"\n{len(made)} prepared at 25 fps / 16 kHz mono")
    print(f"config -> {cfg.relative_to(d)}")
    print(f"run: python3 studio/lipsync.py run {a.name} --shots "
          f"{','.join(str(s) for s, _, _ in made)} --repo ~/MuseTalk")


def cmd_run(a) -> None:
    d, proj = load_project(a.name)
    eng = pick(gpu_vram_gb(), a.engine)
    e = ENGINES[eng]
    if not a.repo:
        raise SystemExit(f"--repo is required: clone {e['repo']} and pass its path")
    repo = Path(a.repo).expanduser().resolve()
    if not repo.exists():
        raise SystemExit(f"{repo} does not exist")
    want = {int(x) for x in a.shots.split(",")} if a.shots else None
    rows = [r for r in candidates(proj) if (want is None or r["shot"] in want)]
    lip = d / "work" / "lip"
    done = []
    for r in rows:
        v = lip / "in" / f"s{r['shot']:02d}.mp4"
        w = lip / "in" / f"s{r['shot']:02d}.wav"
        if not v.exists():
            print(f"  s{r['shot']:02d} not prepared, skipped (run `prepare` first)")
            continue
        out = lip / "out" / f"s{r['shot']:02d}.mp4"
        cmd = e["run"].format(cfg=lip / "in" / "musetalk.yaml", out=lip / "out",
                              repo=str(repo), video=v, wav=w)
        print(f"  s{r['shot']:02d}: {cmd}")
        if a.dry_run:
            continue
        p = subprocess.run(cmd, shell=True, cwd=str(repo), capture_output=True, text=True,
                           timeout=7200)
        if p.returncode != 0:
            print(f"    FAILED: {(p.stderr or p.stdout)[-400:]}")
            continue
        done.append((r["shot"], out))
        print(f"    ok -> {out.relative_to(d)}" if out.exists() else "    ok (check output path)")
    if a.dry_run:
        print("\ndry run: nothing executed. The commands above are exactly what will run.")
    else:
        print(f"\n{len(done)} clips lip-synced. Replace clips/sNN_t1.mp4 with them and re-assemble.")
        print("Next: score them — LSE-C > 6 accept, > 8 good; LSE-D < 8.")


def main() -> None:
    ap = argparse.ArgumentParser(prog="lipsync", description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("check"); p.set_defaults(fn=cmd_check)
    for name, fn in (("plan", cmd_plan), ("prepare", cmd_prepare), ("run", cmd_run)):
        p = sub.add_parser(name); p.add_argument("name")
        p.add_argument("--engine", default=None, choices=list(ENGINES))
        if name == "plan":
            p.add_argument("--all", action="store_true")
        else:
            p.add_argument("--shots", default=None)
        if name == "run":
            p.add_argument("--repo", default=os.environ.get("LIPSYNC_REPO"))
            p.add_argument("--dry-run", action="store_true")
        p.set_defaults(fn=fn)
    a = ap.parse_args()
    a.fn(a)


if __name__ == "__main__":
    main()
