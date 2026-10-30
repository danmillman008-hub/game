#!/usr/bin/env python3
"""filmkit — the instrument an agent plays to turn a screenplay into a film.

Every Mivi/ffmpeg capability I have is behind one verb here, so a whole film is
a short, resumable, inspectable command sequence instead of ad-hoc probing.

    filmkit new       myfilm                 # scaffold a project
    filmkit status    myfilm                 # what exists, what is missing
    filmkit still     myfilm --shot 1 --from file:assets/s01.png
    filmkit still     myfilm --shot 2 --from last:1          # chain shot 1
    filmkit shot      myfilm --shot 1 --takes 2 --quality 1
    filmkit chain     myfilm --from 1 --to 2
    filmkit assemble  myfilm
    filmkit mix       myfilm --vo audio/vo.mp3 --music audio/bed.mp3
    filmkit qc        myfilm
    filmkit frames    out/final.mp4 --at 1,4,7
    filmkit deliver   myfilm --github --tag v1

State lives in <project>/project.json, which is the source of truth and makes
every step safe to re-run. Nothing is mocked: generation goes to Mivi, editing
goes to ffmpeg.
"""
from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "bridge"))
import mivi_mcp as M  # noqa: E402  (the signed API layer, single source of truth)


# --------------------------------------------------------------------- helpers
def ffmpeg_bin() -> str:
    for cand in (os.environ.get("FFMPEG"), shutil.which("ffmpeg")):
        if cand and Path(cand).exists():
            return cand
    try:
        import imageio_ffmpeg
        return imageio_ffmpeg.get_ffmpeg_exe()
    except Exception:
        raise SystemExit("ffmpeg not found: install ffmpeg or set FFMPEG=/path/to/ffmpeg")


def ffprobe_bin():
    """ffprobe if present, else None (filmkit then parses `ffmpeg -i` output)."""
    if os.environ.get("FFPROBE"):
        return os.environ["FFPROBE"]
    if shutil.which("ffprobe"):
        return shutil.which("ffprobe")
    probe = Path(ffmpeg_bin()).parent / "ffprobe"
    return str(probe) if probe.exists() else None


FF, FP = None, None
SHOT_LEN = 4.03          # what the engine actually returns; measured, not configurable


def run(args, timeout=1800) -> str:
    p = subprocess.run(args, capture_output=True, text=True, timeout=timeout)
    if p.returncode != 0:
        raise RuntimeError((p.stderr or p.stdout or "ffmpeg failed")[-1200:])
    return p.stdout


def _probe_without_ffprobe(path) -> dict:
    p = subprocess.run([FF, "-i", str(path)], capture_output=True, text=True)
    txt = (p.stderr or "") + (p.stdout or "")
    import re as _re
    w = h = fps = 0
    m = _re.search(r"Video:.*?(\d{2,5})x(\d{2,5})", txt)
    if m:
        w, h = int(m.group(1)), int(m.group(2))
    f = _re.search(r"(\d+(?:\.\d+)?) fps", txt)
    if f:
        fps = float(f.group(1))
    dur = 0.0
    d = _re.search(r"Duration: (\d+):(\d+):(\d+(?:\.\d+)?)", txt)
    if d:
        dur = int(d.group(1)) * 3600 + int(d.group(2)) * 60 + float(d.group(3))
    has_a = "Audio:" in txt
    size = os.path.getsize(path) if os.path.exists(path) else 0
    return {"path": str(path), "width": w, "height": h, "fps": round(fps, 2),
            "has_audio": has_a, "duration_s": round(dur, 3), "bytes": size,
            "probe": "ffmpeg-fallback"}


def probe(path) -> dict:
    if FP is None:
        return _probe_without_ffprobe(path)
    out = run([FP, "-v", "error", "-print_format", "json", "-show_format",
               "-show_streams", str(path)])
    j = json.loads(out)
    v = next((s for s in j.get("streams", []) if s.get("codec_type") == "video"), {})
    a = next((s for s in j.get("streams", []) if s.get("codec_type") == "audio"), None)
    num, _, den = (v.get("r_frame_rate") or "0/1").partition("/")
    fps = float(num) / float(den or 1) if den else 0.0
    return {"path": str(path), "width": v.get("width"), "height": v.get("height"),
            "fps": round(fps, 2), "has_audio": a is not None,
            "duration_s": round(float(j.get("format", {}).get("duration") or 0), 3),
            "bytes": int(j.get("format", {}).get("size") or 0)}


def duration_of(path) -> float:
    return probe(path)["duration_s"]

# --------------------------------------------------------------------- project
def pdir(name: str) -> Path:
    p = Path(name)
    if p.is_absolute() or p.exists():
        return p
    return ROOT / "films" / name


def load(name: str) -> tuple[Path, dict]:
    d = pdir(name)
    f = d / "project.json"
    if not f.exists():
        raise SystemExit(f"no project at {f} — run: filmkit new {name}")
    return d, json.loads(f.read_text(encoding="utf-8"))


def save(d: Path, proj: dict) -> None:
    proj["updated"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    (d / "project.json").write_text(json.dumps(proj, indent=2, ensure_ascii=False),
                                    encoding="utf-8")


def shot(d: Path, proj: dict, n) -> dict:
    n = int(n)
    for s in proj["shots"]:
        if int(s["n"]) == n:
            return s
    raise SystemExit(f"shot {n} not in project (has {[s['n'] for s in proj['shots']]})")


def resolve(d: Path, value: str) -> str:
    p = Path(value)
    return str(p if p.is_absolute() else (d / p))


# --------------------------------------------------------------------- commands
def cmd_new(a):
    d = pdir(a.name)
    if (d / "project.json").exists() and not a.force:
        raise SystemExit(f"{d}/project.json exists (use --force)")
    for sub in ("stills", "clips", "assets", "audio", "subs", "out", "qc"):
        (d / sub).mkdir(parents=True, exist_ok=True)
    proj = {
        "name": d.name,
        "created": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "aspect": "3:4", "model": "mivi-gx-720p", "quality": 2,
        "crossfade_s": 0.4, "note": "shot duration is fixed at 4.03 s by the engine",
        "shots": [],
    }
    save(d, proj)
    print(f"created {d}")
    print("next: add shots to project.json, then `filmkit status`")


def cmd_plan(a):
    """Add/replace the shot list from a small markdown-ish script file."""
    d, proj = load(a.name)
    text = Path(a.script).read_text(encoding="utf-8")
    shots, cur = [], None
    for line in text.splitlines():
        s = line.strip()
        if s.upper().startswith("SHOT") or s.upper().startswith("پلان"):
            head, _, body = s.partition(":")
            cur = {"n": len(shots) + 1, "motion": body.strip(), "narration": "",
                   "still": None, "state": "planned", "clip": None, "takes": []}
            shots.append(cur)
        elif cur is not None and s and not s.startswith("#"):
            if s.upper().startswith("VO:") or s.upper().startswith("نریشن:"):
                cur["narration"] = s.split(":", 1)[1].strip()
            elif not cur["motion"]:
                cur["motion"] = s
    if not shots:
        raise SystemExit("no 'SHOT:' lines found in the script")
    proj["shots"] = shots
    save(d, proj)
    print(f"{len(shots)} shots planned, ~{len(shots) * 4.03:.1f}s of screen time")


def cmd_status(a):
    d, proj = load(a.name)
    print(f"{proj['name']}  ({proj.get('aspect')}, {proj.get('model')}, 720P={proj.get('quality')})")
    print(f"{'#':>2}  {'state':<10} {'still':<22} {'clip':<22} motion")
    for s in proj["shots"]:
        still = Path(resolve(d, s["still"])).name if s.get("still") else "-"
        clip = Path(resolve(d, s["clip"])).name if s.get("clip") else "-"
        print(f"{s['n']:>2}  {s.get('state','planned'):<10} {still:<22} {clip:<22} "
              f"{(s.get('motion') or '')[:48]}")
    clips = [s for s in proj["shots"] if s.get("clip")]
    est = max(0.0, len(clips) * 4.03 - max(0, len(clips) - 1) * float(proj.get("crossfade_s") or 0))
    print(f"\nclips ready: {len(clips)}/{len(proj['shots'])}   estimated runtime: {est:.1f}s")
    fin = d / "out" / "final.mp4"
    if fin.exists():
        print("final:", json.dumps(probe(fin)))


def _make_still(d: Path, proj: dict, s: dict, spec: str, extra: dict) -> Path:
    """spec: file:<path> | url:<url> | last:<n> | compose:<a>,<b> | upscale:<path>
             | swapface:<path> | masks:<path>"""
    kind, _, val = spec.partition(":")
    outdir = d / "stills"
    outdir.mkdir(exist_ok=True)
    target = outdir / f"s{int(s['n']):02d}.png"

    if kind == "file":
        src = Path(resolve(d, val))
        if not src.exists():
            raise SystemExit(f"missing still file {src}")
        if src.suffix.lower() in (".png", ".jpg", ".jpeg"):
            shutil.copyfile(src, target.with_suffix(src.suffix))
            s["still"] = str(target.with_suffix(src.suffix).relative_to(d))
            return target.with_suffix(src.suffix)
        raise SystemExit("stills must be png/jpg")
    if kind == "url":
        M.download(val, str(target.with_suffix(".jpg")))
        s["still"] = str(target.with_suffix(".jpg").relative_to(d))
        return target.with_suffix(".jpg")
    if kind == "last":
        prev = shot(d, proj, int(val))
        if not prev.get("clip"):
            raise SystemExit(f"shot {val} has no clip to take a last frame from")
        r = M.t_last_frame({"video": resolve(d, prev["clip"]), "out": str(target)})
        s["still"] = str(target.relative_to(d))
        s["chained_from"] = int(val)
        return Path(r["saved"])
    if kind == "compose":
        a_, b_ = [x.strip() for x in val.split(",")]
        r = M.t_compose({"images": [resolve(d, a_), resolve(d, b_)],
                         "prompt": extra.get("prompt") or "", "out": str(target)})
        if not r.get("image_url"):
            raise SystemExit(f"compose failed: {r}")
        s["still"] = str(target.relative_to(d))
        return Path(r["saved"])
    if kind == "upscale":
        r = M.t_upscale({"image": resolve(d, val)})
        url = r.get("result") if isinstance(r.get("result"), str) else None
        if isinstance(r.get("result"), list):
            url = r["result"][0]
        if not url:
            raise SystemExit(f"upscale returned {r}")
        M.download(url, str(target))
        s["still"] = str(target.relative_to(d))
        return target
    if kind == "swapface":
        r = M.t_swapface({"image": resolve(d, val),
                          "template_id": int(extra.get("template") or 1001)})
        res = r.get("result") or {}
        urls = res.get("urlList") if isinstance(res, dict) else None
        if not urls:
            raise SystemExit(f"swapface returned {r}")
        M.download(urls[0], str(target))
        s["still"] = str(target.relative_to(d))
        return target
    if kind == "masks":
        r = M.t_masks({"image": resolve(d, val)})
        (d / "stills" / f"s{int(s['n']):02d}_masks.json").write_text(json.dumps(r, indent=2))
        print(f"masks for shot {s['n']}: {len(r.get('masks') or [])} -> see stills/…_masks.json")
        return Path(resolve(d, s["still"])) if s.get("still") else Path(val)
    raise SystemExit(f"unknown --from kind '{kind}'")


def cmd_still(a):
    d, proj = load(a.name)
    targets = proj["shots"] if a.all else [shot(d, proj, a.shot)]
    for s in targets:
        spec = a.frm or (s.get("still_source") or "")
        if not spec:
            raise SystemExit(f"shot {s['n']}: pass --from or set still_source in project.json")
        s["still_source"] = spec
        path = _make_still(d, proj, s, spec, {"prompt": a.prompt, "template": a.template})
        s["state"] = "still_ready"
        save(d, proj)
        print(f"shot {s['n']}: still -> {path}")


def cmd_shot(a):
    d, proj = load(a.name)
    s = shot(d, proj, a.shot)
    if not s.get("still"):
        raise SystemExit(f"shot {s['n']} has no still — run `filmkit still` first")
    still = resolve(d, s["still"])
    prompt = a.prompt or s.get("motion") or ""
    quality = int(a.quality or proj.get("quality") or 2)
    clips = d / "clips"
    ok = None
    for t in range(1, int(a.takes) + 1):
        created = M.t_video({"image": still, "prompt": prompt,
                             "model": proj.get("model") or "mivi-gx-720p",
                             "quality": quality})
        print(f"shot {s['n']} take {t}: task {created['task_id']}")
        out = clips / f"s{int(s['n']):02d}_t{t}.mp4"
        res = M.t_video_wait({"task_id": created["task_id"], "out": str(out),
                              "timeout_s": a.timeout})
        if not res.get("video_url"):
            print(f"  take {t} failed: {res.get('reason') or res}")
            s.setdefault("takes", []).append({"take": t, "task": created["task_id"],
                                              "ok": False, "reason": res.get("reason")})
            save(d, proj)
            continue
        meta = probe(out)
        print(f"  take {t} ok {meta['width']}x{meta['height']} {meta['duration_s']}s "
              f"{meta['bytes']}B")
        s.setdefault("takes", []).append({"take": t, "task": created["task_id"], "ok": True,
                                          "file": str(out.relative_to(d)), **meta})
        ok = ok or out
        if not a.all_takes:
            break
        save(d, proj)
    if not ok:
        raise SystemExit(f"shot {s['n']}: every take failed")
    s["clip"] = str(ok.relative_to(d))
    s["state"] = "rendered"
    save(d, proj)
    print(f"shot {s['n']}: clip -> {ok}")


def cmd_chain(a):
    d, proj = load(a.name)
    src = shot(d, proj, a.frm)
    dst = shot(d, proj, a.to if a.to else int(a.frm) + 1)
    if not src.get("clip"):
        raise SystemExit(f"shot {src['n']} has no clip yet")
    target = d / "stills" / f"s{int(dst['n']):02d}.jpg"
    r = M.t_last_frame({"video": resolve(d, src["clip"]), "out": str(target)})
    dst["still"] = str(target.relative_to(d))
    dst["still_source"] = f"last:{src['n']}"
    dst["chained_from"] = int(src["n"])
    dst["state"] = "still_ready"
    save(d, proj)
    print(f"chained shot {src['n']} -> shot {dst['n']} ({Path(r['saved']).name})")


def cmd_assemble(a):
    d, proj = load(a.name)
    (d / "out").mkdir(parents=True, exist_ok=True)
    clips = [(s["n"], resolve(d, s["clip"])) for s in proj["shots"] if s.get("clip")]
    if len(clips) < 1:
        raise SystemExit("no clips to assemble")
    out = d / "out" / "final.mp4"
    xf = float(a.crossfade if a.crossfade is not None else (proj.get("crossfade_s") or 0))
    args = [FF, "-y", "-v", "error"]
    for _, c in clips:
        args += ["-i", c]
    if xf > 0 and len(clips) > 1:
        durs = [duration_of(c) for _, c in clips]
        fc, prev, acc = [], "[0:v]", durs[0]
        for i in range(1, len(clips)):
            off = max(acc - xf, 0)
            fc.append(f"{prev}[{i}:v]xfade=transition=fade:duration={xf}:offset={off:.3f}[v{i}]")
            prev, acc = f"[v{i}]", acc + durs[i] - xf
        args += ["-filter_complex", ";".join(fc), "-map", prev, "-c:v", "libx264",
                 "-crf", "18", "-pix_fmt", "yuv420p", "-movflags", "+faststart", str(out)]
    elif len(clips) > 1:
        (d / "out" / "concat.txt").write_text(
            "".join(f"file '{c}'\n" for _, c in clips), encoding="utf-8")
        args = [FF, "-y", "-v", "error", "-f", "concat", "-safe", "0",
                "-i", str(d / "out" / "concat.txt"), "-c", "copy", str(out)]
    else:
        shutil.copyfile(clips[0][1], out)
    run(args)
    print(f"assembled {len(clips)} clips -> {out}")
    print(json.dumps(probe(out)))

    if a.subs:
        _burn(d, out, Path(a.subs))
    elif (d / "subs" / "final.srt").exists():
        _burn(d, out, d / "subs" / "final.srt")

    vo = Path(a.vo) if a.vo else next((p for p in (d / "audio" / "vo_timeline.mp3",
                                                   d / "audio" / "vo.mp3") if p.exists()), None)
    music = Path(a.music) if a.music else (d / "audio" / "bed.mp3" if (d / "audio" / "bed.mp3").exists() else None)
    if vo or music:
        cmd_mix(argparse.Namespace(name=a.name, vo=str(vo) if vo else None,
                                   music=str(music) if music else None,
                                   duck=a.duck, out=None))


FONT = ROOT / "studio" / "fonts" / "Vazirmatn-Bold.ttf"


def _srt_cues(path: Path):
    import re
    txt = path.read_text(encoding="utf-8")
    out = []
    for block in re.split(r"\n\s*\n", txt.strip()):
        lines = [l for l in block.splitlines() if l.strip()]
        if len(lines) < 2 or "-->" not in block:
            continue
        m = re.search(r"(\d+):(\d+):([\d.,]+)\s*-->\s*(\d+):(\d+):([\d.,]+)", block)
        if not m:
            continue
        def sec(h, mi, se):
            return int(h) * 3600 + int(mi) * 60 + float(se.replace(",", "."))
        start, end = sec(*m.group(1, 2, 3)), sec(*m.group(4, 5, 6))
        text = " ".join(lines[lines.index([l for l in lines if "-->" in l][0]) + 1:])
        out.append((start, end, text.strip()))
    return out


def _render_cue_png(text: str, path: Path, w: int, size: int = 44):
    """Shaped Persian (or any RTL/LTR) text as a transparent PNG strip."""
    from PIL import Image, ImageDraw, ImageFont
    txt = text
    try:
        import arabic_reshaper
        from bidi.algorithm import get_display
        txt = get_display(arabic_reshaper.reshape(text))
    except Exception:
        pass
    font = None
    for cand in (FONT, Path("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf")):
        if Path(cand).exists():
            font = ImageFont.truetype(str(cand), size)
            break
    if font is None:
        font = ImageFont.load_default()
    # wrap to the safe width
    max_w = int(w * 0.86)
    words, lines, cur = txt.split(" "), [], ""
    for word in words:
        trial = (cur + " " + word).strip()
        if font.getbbox(trial)[2] <= max_w or not cur:
            cur = trial
        else:
            lines.append(cur); cur = word
    if cur:
        lines.append(cur)
    lh = int(size * 1.45)
    img = Image.new("RGBA", (w, lh * len(lines) + 24), (0, 0, 0, 0))
    dr = ImageDraw.Draw(img)
    for i, line in enumerate(lines):
        tw = font.getbbox(line)[2]
        x = (w - tw) // 2
        y = 12 + i * lh
        for dx, dy in ((-2, 0), (2, 0), (0, -2), (0, 2), (-2, -2), (2, 2)):
            dr.text((x + dx, y + dy), line, font=font, fill=(0, 0, 0, 190))
        dr.text((x, y), line, font=font, fill=(255, 255, 255, 255))
    path.parent.mkdir(parents=True, exist_ok=True)
    img.save(path)


def _burn(d: Path, video: Path, srt: Path):
    """Subtitle burn-in that survives Persian/Arabic shaping."""
    try:
        cues = _srt_cues(srt)
        if not cues:
            raise RuntimeError("no cues parsed")
        info = probe(video)
        w, h = int(info["width"]), int(info["height"])
        args = [FF, "-y", "-v", "error", "-i", str(video)]
        filters, last = [], "0:v"
        for i, (start, end, text) in enumerate(cues, 1):
            png = d / "subs" / f"cue{i:02d}.png"
            _render_cue_png(text, png, w)
            args += ["-i", str(png)]
            y = h - int(h * 0.19)
            filters.append(f"[{last}][{i}:v]overlay=0:{y}:"
                           f"enable='between(t,{start:.3f},{end:.3f})'[o{i}]")
            last = f"o{i}"
        tmp = d / "out" / "_sub.mp4"
        args += ["-filter_complex", ";".join(filters), "-map", f"[{last}]",
                 "-map", "0:a?", "-c:v", "libx264", "-crf", "19", "-pix_fmt", "yuv420p",
                 "-c:a", "copy", "-movflags", "+faststart", str(tmp)]
        run(args)
        shutil.move(str(tmp), str(video))
        print(f"subtitles burned from {srt.name} ({len(cues)} cues, Pillow/Persian-shaped)")
    except Exception as exc:
        print(f"subtitle burn failed ({exc}); falling back to ffmpeg's subtitles filter")
        tmp = d / "out" / "_sub.mp4"
        run([FF, "-y", "-v", "error", "-i", str(video), "-vf",
             f"subtitles={srt}:force_style='Fontsize=20,PrimaryColour=&H00FFFFFF'",
             "-c:a", "copy", str(tmp)])
        shutil.move(str(tmp), str(video))


def cmd_mix(a):
    d, proj = load(a.name)
    (d / "out").mkdir(parents=True, exist_ok=True)
    src = Path(a.out) if a.out else d / "out" / "final.mp4"
    dst = src.with_name("final_audio.mp4")
    args = [FF, "-y", "-v", "error", "-i", str(src)]
    inputs, fc, idx = [], [], 1
    vo = Path(a.vo) if a.vo else None
    music = Path(a.music) if a.music else None
    if vo:
        args += ["-i", str(vo)]
        inputs.append((idx, "vo", 1.0)); idx += 1
    if music:
        args += ["-i", str(music)]
        inputs.append((idx, "bed", 0.18)); idx += 1
    labels = []
    for i, (file_idx, kind, vol) in enumerate(inputs):
        fc.append(f"[{file_idx}:a]volume={vol},aformat=sample_fmts=fltp:"
                  f"sample_rates=48000:channel_layouts=stereo[a{i}]")
        labels.append(f"[a{i}]")
    if a.duck and music and vo:
        # sidechain: the bed ducks itself under the voice; the voice is split so the
        # same stream can both key the compressor and be mixed afterwards
        fc = ["[2:a]aformat=sample_fmts=fltp:sample_rates=48000:channel_layouts=stereo,"
              "volume=0.18[bed]",
              "[1:a]aformat=sample_fmts=fltp:sample_rates=48000:channel_layouts=stereo,"
              "volume=1.0[v0]",
              "[v0]asplit=2[v1][v2]",
              "[bed][v1]sidechaincompress=threshold=0.05:ratio=8:attack=20:release=400[bedd]",
              "[v2][bedd]amix=inputs=2:duration=longest:normalize=0[a]"]
        labels = ["[a]"]
    elif len(labels) > 1:
        fc.append("".join(labels) + f"amix=inputs={len(labels)}:duration=longest:normalize=0[a]")
        labels = ["[a]"]
    # pad the mix so a short VO never truncates the picture
    vid_dur = duration_of(src) or 0.0
    fc.append(f"{labels[0]}apad=whole_dur={vid_dur:.3f}[af]")
    labels = ["[af]"]
    args += ["-filter_complex", ";".join(fc), "-map", "0:v", "-map", labels[0],
             "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", str(dst)]
    run(args)
    shutil.move(str(dst), str(src))
    print(f"audio mixed into {src}")
    print(json.dumps(probe(src)))


def _ts(t: float) -> str:
    t = max(0.0, t)
    h = int(t // 3600); m = int((t % 3600) // 60); sec = t % 60
    return f"{h:02d}:{m:02d}:{sec:06.3f}".replace(".", ",")


def cmd_srt(a):
    """Generate subs/final.srt from each shot's `narration`, on the real cut timeline."""
    d, proj = load(a.name)
    (d / "subs").mkdir(parents=True, exist_ok=True)
    xf = float(a.crossfade if a.crossfade is not None else (proj.get("crossfade_s") or 0))
    step = SHOT_LEN - xf
    cps = float(a.cps or 14.0)          # Persian subtitle reading speed, chars/second
    blocks, t, n = [], 0.0, 0
    for s_ in proj["shots"]:
        if not s_.get("clip"):
            t += step
            continue
        line = (s_.get("narration") or "").strip()
        if line:
            n += 1
            start = t + 0.30
            dur = min(SHOT_LEN - 0.45, max(1.2, len(line) / cps))
            blocks.append(f"{n}\n{_ts(start)} --> {_ts(start + dur)}\n{line}\n")
        t += step
    out = d / "subs" / "final.srt"
    out.write_text("\n".join(blocks), encoding="utf-8")
    print(f"{n} subtitle cues -> {out}  (timeline step {step:.2f}s, xfade {xf}s)")


def cmd_vo(a):
    """Assemble one VO track on the cut timeline from per-shot clips.

    Expects audio/vo/s<shot><any>.mp3 (e.g. s18_part1.mp3, s18_part2.mp3) — every file
    for a shot is laid at that shot's start, in filename order, with a small gap.
    """
    d, proj = load(a.name)
    (d / "audio").mkdir(parents=True, exist_ok=True)
    vo_dir = d / "audio" / "vo"
    if not vo_dir.exists():
        raise SystemExit(f"no {vo_dir}")
    xf = float(a.crossfade if a.crossfade is not None else (proj.get("crossfade_s") or 0))
    step = SHOT_LEN - xf
    args = [FF, "-y", "-v", "error"]
    parts = []          # (input_index, delay_seconds)
    idx = 0
    for s_ in proj["shots"]:
        n = int(s_["n"])
        files = sorted(vo_dir.glob(f"s{n:02d}*.mp3")) + sorted(vo_dir.glob(f"s{n}_*.mp3"))
        files = sorted({p for p in files})
        if not files:
            continue
        base = (n - 1) * step + 0.35
        off = 0.0
        for f in files:
            args += ["-i", str(f)]
            parts.append((idx, base + off))
            idx += 1
            off += duration_of(f) + 0.18
    if not parts:
        raise SystemExit("no VO clips found")
    fc, labels = [], []
    for k, (i, delay) in enumerate(parts):
        ms = int(delay * 1000)
        fc.append(f"[{i}:a]aformat=sample_fmts=fltp:sample_rates=48000:channel_layouts=stereo,"
                  f"adelay={ms}|{ms}[v{k}]")
        labels.append(f"[v{k}]")
    fc.append("".join(labels) + f"amix=inputs={len(labels)}:duration=longest:normalize=0,"
              f"apad=whole_dur={(len(proj['shots']) * step + 1):.2f}[vomix]")
    out = d / "audio" / "vo_timeline.mp3"
    args += ["-filter_complex", ";".join(fc), "-map", "[vomix]", "-c:a", "libmp3lame",
             "-b:a", "192k", str(out)]
    run(args)
    print(f"{len(parts)} VO clips -> {out} ({duration_of(out):.1f}s)")
    print("next: filmkit assemble <project>  (it picks up audio/vo.mp3 or --vo)")


def cmd_loud(a):
    """Normalise the finished mix to broadcast-ish loudness (-16 LUFS, -1.5 dBTP)."""
    d, proj = load(a.name)
    src = Path(a.out) if a.out else d / "out" / "final.mp4"
    if not src.exists():
        raise SystemExit(f"no {src}")
    tmp = src.with_name("_loud.mp4")
    run([FF, "-y", "-v", "error", "-i", str(src), "-c:v", "copy",
         "-af", f"loudnorm=I={a.i}:TP={a.tp}:LRA=11", "-c:a", "aac", "-b:a", "192k",
         "-movflags", "+faststart", str(tmp)])
    shutil.move(str(tmp), str(src))
    info = probe(src)
    print(f"normalised {src.name}: {info['duration_s']}s, audio={info['has_audio']}, "
          f"{info['bytes']//1024} KB")


def cmd_qc(a):
    d, proj = load(a.name)
    (d / "qc").mkdir(parents=True, exist_ok=True)
    report = {"project": proj["name"], "shots": [], "issues": []}
    for s in proj["shots"]:
        if not s.get("clip"):
            report["issues"].append(f"shot {s['n']}: no clip")
            continue
        clip = resolve(d, s["clip"])
        meta = probe(clip)
        report["shots"].append({"n": s["n"], **meta})
        ok_geo = (meta["width"], meta["height"]) in ((960, 1280), (448, 576))
        if not ok_geo:
            report["issues"].append(
                f"shot {s['n']}: {meta['width']}x{meta['height']} is neither 960x1280 (720P) "
                f"nor 448x576 (360P draft)")
        if not (3.5 <= meta["duration_s"] <= 4.6):
            report["issues"].append(f"shot {s['n']}: duration {meta['duration_s']}s")
    fin = d / "out" / "final.mp4"
    if fin.exists():
        report["final"] = probe(fin)
        frames = d / "qc" / "frames"
        frames.mkdir(parents=True, exist_ok=True)
        dur = report["final"]["duration_s"]
        # sample pairs 0.5 s apart INSIDE each shot: a cut is not a defect, a melt is
        pts = []
        for s_ in proj["shots"]:
            if not s_.get("clip"):
                continue
            start = (int(s_["n"]) - 1) * (SHOT_LEN - float(proj.get("crossfade_s") or 0))
            for off in (0.8, 2.2):
                pts.append(round(min(start + off, dur - 0.2), 2))
        pts = sorted({p for p in pts if p > 0})[:12]
        for t in pts:
            out = frames / f"t{t:05.2f}.jpg"
            run([FF, "-y", "-v", "error", "-ss", f"{t}", "-i", str(fin),
                 "-frames:v", "1", str(out)])
        report["frames"] = [str(p.relative_to(d)) for p in sorted(frames.glob("*.jpg"))]
        # crude melt detector: consecutive sampled frames should not be wildly different
        try:
            from PIL import Image, ImageChops, ImageStat
            imgs = [Image.open(p).convert("L").resize((64, 64)) for p in sorted(frames.glob("*.jpg"))]
            diffs = []
            for x, y in zip(imgs, imgs[1:]):
                diffs.append(round(ImageStat.Stat(ImageChops.difference(x, y)).mean[0], 1))
            report["frame_delta"] = diffs
            if any(v > 70 for v in diffs):
                report["issues"].append("two frames 1.4 s apart inside one shot differ >70/255 "
                                        "— possible melt")
        except Exception:
            report["frame_delta"] = None
    else:
        report["issues"].append("no out/final.mp4")
    (d / "qc" / "report.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(json.dumps(report, indent=2)[:1600])
    print(f"\nreport: {d / 'qc' / 'report.json'}")
    if report["issues"]:
        print("ISSUES:\n  " + "\n  ".join(report["issues"]))


def cmd_frames(a):
    outdir = Path(a.out) if a.out else Path("qc/frames")
    outdir.mkdir(parents=True, exist_ok=True)
    made = []
    for t in [x.strip() for x in a.at.split(",") if x.strip()]:
        out = outdir / f"f{t.replace('.', '_')}.jpg"
        run([FF, "-y", "-v", "error", "-ss", t, "-i", a.video, "-frames:v", "1", str(out)])
        made.append(str(out))
    print("\n".join(made))


def cmd_deliver(a):
    d, proj = load(a.name)
    finals = [p for p in (d / "out" / "final.mp4",) if p.exists()]
    if not finals:
        raise SystemExit("nothing to deliver: run `filmkit assemble` first")
    final = finals[0]
    size = final.stat().st_size
    if a.github:
        tag = a.tag or f"{proj['name']}-{time.strftime('%Y%m%d-%H%M')}"
        run(["gh", "release", "create", tag, str(final), "--repo", a.repo,
             "--title", f"{proj['name']} {tag}",
             "--notes", f"film assembled by filmkit: {len(proj['shots'])} shots"])
        print(f"https://github.com/{a.repo}/releases/tag/{tag}")
    if a.drive:
        man = d / "out" / "drive_manifest.json"
        man.write_text(json.dumps({"file": str(final), "bytes": size,
                                   "name": f"{proj['name']}.mp4",
                                   "how": "agent uploads this path with the Drive connector"},
                                  indent=2))
        print(f"drive manifest: {man}\n  file: {final}  ({size/1e6:.1f} MB)")
    if not (a.github or a.drive):
        print(f"{final}  {size/1e6:.1f} MB")


# --------------------------------------------------------------------- main
def main():
    global FF, FP
    ap = argparse.ArgumentParser(prog="filmkit", description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("new"); p.add_argument("name"); p.add_argument("--force", action="store_true")
    p.set_defaults(fn=cmd_new)

    p = sub.add_parser("plan"); p.add_argument("name"); p.add_argument("--script", required=True)
    p.set_defaults(fn=cmd_plan)

    p = sub.add_parser("status"); p.add_argument("name"); p.set_defaults(fn=cmd_status)

    p = sub.add_parser("still"); p.add_argument("name")
    p.add_argument("--shot", type=int); p.add_argument("--all", action="store_true")
    p.add_argument("--from", dest="frm")
    p.add_argument("--prompt"); p.add_argument("--template", type=int)
    p.set_defaults(fn=cmd_still)

    p = sub.add_parser("shot"); p.add_argument("name"); p.add_argument("--shot", type=int, required=True)
    p.add_argument("--takes", type=int, default=1); p.add_argument("--all-takes", action="store_true")
    p.add_argument("--quality", type=int, choices=[1, 2]); p.add_argument("--prompt")
    p.add_argument("--timeout", type=float, default=420)
    p.set_defaults(fn=cmd_shot)

    p = sub.add_parser("chain"); p.add_argument("name"); p.add_argument("--from", dest="frm", required=True)
    p.add_argument("--to", type=int); p.set_defaults(fn=cmd_chain)

    p = sub.add_parser("assemble"); p.add_argument("name")
    p.add_argument("--crossfade", type=float); p.add_argument("--subs")
    p.add_argument("--vo"); p.add_argument("--music"); p.add_argument("--duck", action="store_true")
    p.set_defaults(fn=cmd_assemble)

    p = sub.add_parser("mix"); p.add_argument("name"); p.add_argument("--vo"); p.add_argument("--music")
    p.add_argument("--duck", action="store_true"); p.add_argument("--out")
    p.set_defaults(fn=cmd_mix)

    p = sub.add_parser("srt"); p.add_argument("name")
    p.add_argument("--crossfade", type=float); p.add_argument("--cps", type=float)
    p.set_defaults(fn=cmd_srt)

    p = sub.add_parser("vo"); p.add_argument("name"); p.add_argument("--crossfade", type=float)
    p.set_defaults(fn=cmd_vo)

    p = sub.add_parser("loud"); p.add_argument("name"); p.add_argument("--out")
    p.add_argument("--i", type=float, default=-16.0); p.add_argument("--tp", type=float, default=-1.5)
    p.set_defaults(fn=cmd_loud)

    p = sub.add_parser("qc"); p.add_argument("name"); p.set_defaults(fn=cmd_qc)

    p = sub.add_parser("frames"); p.add_argument("video"); p.add_argument("--at", default="1,4,7")
    p.add_argument("--out"); p.set_defaults(fn=cmd_frames)

    p = sub.add_parser("deliver"); p.add_argument("name")
    p.add_argument("--github", action="store_true"); p.add_argument("--drive", action="store_true")
    p.add_argument("--tag"); p.add_argument("--repo", default="danmillman008-hub/game")
    p.set_defaults(fn=cmd_deliver)

    a = ap.parse_args()
    FF, FP = ffmpeg_bin(), ffprobe_bin()
    M.FFMPEG = FF                    # the API layer shares the same binaries
    M.FFPROBE = FP or "ffprobe"
    a.fn(a)


if __name__ == "__main__":
    main()
