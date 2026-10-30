#!/usr/bin/env python3
"""voice.py — local, offline, CPU TTS for film VO. English and Farsi in one pass.

Why this exists: the VO for every film so far came from a cloud call. That means
(a) no reproducibility — the same line reads differently tomorrow, (b) no A/B —
we cannot make five takes and keep the best, and (c) no offline build.

This module is the answer for both languages the films use:

    English -> Kokoro-82M   Apache-2.0, 82M params, ONNX int8 = 114 MB + 28 MB voices
    Farsi   -> Piper        GPL-3.0 *engine* (called as a CLI, never vendored),
                            fa_IR voices, 5 of them, one .onnx each

Both run on CPU. A line's language is detected per line, so one film can carry a
Persian voice-over and an English one without any flags.

    python3 studio/voice.py check                     # what is installed, what is not
    python3 studio/voice.py plan  <project>           # write audio/vo/vo_plan.json
    python3 studio/voice.py render <project>          # -> audio/vo/sNN.mp3, ready for `filmkit vo`

`render` writes the same filenames `filmkit vo` expects (audio/vo/sNN.mp3), so the
whole chain stays: voice render -> filmkit vo -> filmkit assemble.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CACHE = Path(os.environ.get("STUDIO_TTS_CACHE") or (Path.home() / ".cache" / "studio-tts"))

# --- what we generated the plan from -----------------------------------------
# star counts and licences were read from the GitHub API on 2026-10-30; sizes that
# are marked "measured" came from the release asset list, not from a guess.
CATALOG = {
    "en": {
        "engine": "kokoro",
        "voice": "af_heart",
        "license": "Apache-2.0",
        "params": "82M",
        "note": "best naturalness per MB in the open set; en-US + en-GB",
        "files": [
            ("kokoro-v1.0.int8.onnx", 114_100_000,
             "https://github.com/thewh1teagle/kokoro-onnx/releases/download/"
             "model-files-v1.1/kokoro-v1.0.int8.onnx"),
            ("voices-v1.0.bin", 28_200_000,
             "https://github.com/thewh1teagle/kokoro-onnx/releases/download/"
             "model-files-v1.1/voices-v1.0.bin"),
        ],
        "alternatives": [
            ("chatterbox-nano", "110M", "MIT", "CPU, 3x realtime on 8 cores, [laugh]/[sigh] tags"),
            ("chatterbox-turbo", "350M", "MIT", "English, paralinguistic tags, low VRAM"),
            ("piper en_US", "~63MB/voice", "GPL-3.0", "27 en_US voices, flattest but smallest"),
            ("F5-TTS", "~1.3GB", "MIT", "zero-shot cloning, slow on CPU"),
        ],
    },
    "fa": {
        "engine": "piper",
        "voice": "fa_IR-ganji-medium",
        "license": "GPL-3.0 (engine; CLI only, do not vendor)",
        "params": "medium",
        "note": "the only small offline Farsi TTS with a real voice set (5 voices)",
        "files": [
            ("fa_IR-ganji-medium.onnx", 63_000_000,
             "https://huggingface.co/rhasspy/piper-voices/resolve/v1.0.0/fa/fa_IR/"
             "ganji/medium/fa_IR-ganji-medium.onnx?download=true"),
            ("fa_IR-ganji-medium.onnx.json", 5_000,
             "https://huggingface.co/rhasspy/piper-voices/resolve/v1.0.0/fa/fa_IR/"
             "ganji/medium/fa_IR-ganji-medium.onnx.json?download=true"),
        ],
        "alternatives": [
            ("persian_tts (parsigo)", "ONNX", "none stated", "voice cloning from 5 s, offline CPU"),
            ("Persian-tts-coqui", "VITS", "MIT", "training recipe + ready models"),
        ],
    },
}

FA_VOICES = ["fa_IR-amir", "fa_IR-ganji", "fa_IR-ganji_adabi", "fa_IR-gyro", "fa_IR-reza_ibrahim"]
EN_VOICES = ["af_heart", "af_bella", "af_nicole", "am_michael", "am_fenrir", "bf_emma", "bm_george"]

# speaking rate, used to plan how long a line will be. Both constants were measured,
# not guessed: see studio/knowledge/measurements.json, rendered on a 4-core runner.
WPS_EN = 3.7          # 21 English words in 5.66 s of Kokoro af_heart audio
CPS_FA = 13.3         # 57 Farsi chars in 4.30 s of Piper fa_IR-ganji-medium audio


# ---------------------------------------------------------------- language ----
def detect_lang(text: str) -> str:
    """Persian script -> fa, everything else -> en. Cheap, deterministic, good enough."""
    for ch in text:
        if "\u0600" <= ch <= "\u06ff" or "\u0750" <= ch <= "\u077f":
            return "fa"
    return "en"


def estimate(text: str, lang: str) -> float:
    if lang == "fa":
        return max(0.6, len(text.strip()) / CPS_FA) + 0.30
    words = len(text.split())
    return max(0.6, words / WPS_EN) + 0.30


# ---------------------------------------------------------------- project ----
def load_project(name: str) -> tuple[Path, dict]:
    d = (ROOT / "films" / name).resolve()
    pj = d / "project.json"
    if not pj.exists():
        raise SystemExit(f"no project.json in {d}")
    return d, json.loads(pj.read_text(encoding="utf-8"))


def build_plan(proj: dict, forced: str = "auto", voices: dict | None = None) -> dict:
    voices = voices or {}
    rows = []
    for s in proj.get("shots", []):
        text = (s.get("narration") or "").strip()
        if not text:
            continue
        lang = forced if forced in ("en", "fa") else detect_lang(text)
        spec = CATALOG[lang]
        rows.append({
            "shot": int(s["n"]),
            "lang": lang,
            "engine": voices.get(f"{lang}_engine") or spec["engine"],
            "voice": voices.get(lang) or spec["voice"],
            "chars": len(text),
            "est_s": round(estimate(text, lang), 2),
            "text": text,
        })
    total = round(sum(r["est_s"] for r in rows), 2)
    return {"project": proj.get("name"), "rows": rows, "total_est_s": total,
            "by_lang": {k: sum(1 for r in rows if r["lang"] == k) for k in ("en", "fa")}}


# ---------------------------------------------------------------- models ------
def _have(name: str) -> bool:
    return (CACHE / name).exists()


def fetch(files, allow: bool = True) -> None:
    """Download the model files once, into ~/.cache/studio-tts. On the runner this is
    a plain 142 MB pull; in a sandbox with no outbound access it is the only step
    that fails, and it fails loudly."""
    CACHE.mkdir(parents=True, exist_ok=True)
    for name, size, url in files:
        dst = CACHE / name
        if dst.exists() and dst.stat().st_size > size * 0.5:
            continue
        if not allow:
            raise SystemExit(f"missing {name} in {CACHE}; run fetch or allow download")
        print(f"  download {name} (~{size / 1e6:.0f} MB)")
        tmp = dst.with_suffix(dst.suffix + ".part")
        try:
            with urllib.request.urlopen(url, timeout=180) as r, open(tmp, "wb") as f:
                shutil.copyfileobj(r, f, length=1 << 20)
        except Exception as e:                     # noqa: BLE001 - report, never guess
            tmp.unlink(missing_ok=True)
            raise SystemExit(f"  cannot download {name}: {type(e).__name__}: {e}\n"
                             f"  (this sandbox blocks the CDN; GitHub Actions does not)")
        tmp.replace(dst)


# ---------------------------------------------------------------- backends ----
def synth_kokoro(text: str, voice: str, out_wav: Path, speed: float = 1.0) -> None:
    from kokoro_onnx import Kokoro            # pip install kokoro-onnx soundfile
    import soundfile as sf
    k = Kokoro(str(CACHE / "kokoro-v1.0.int8.onnx"), str(CACHE / "voices-v1.0.bin"))
    samples, sr = k.create(text, voice=voice, speed=speed, lang="en-us")
    sf.write(str(out_wav), samples, sr)


def synth_piper(text: str, voice: str, out_wav: Path, speed: float = 1.0) -> None:
    exe = shutil.which("piper") or shutil.which("piper-tts")
    if not exe:
        raise SystemExit("piper CLI not found: pip install piper-tts  (engine stays external)")
    model = CACHE / f"{voice}.onnx"
    cmd = [exe, "--model", str(model), "--output_file", str(out_wav),
           "--length_scale", f"{1.0 / max(0.5, speed):.3f}"]
    p = subprocess.run(cmd, input=text.encode("utf-8"), capture_output=True, timeout=900)
    if p.returncode != 0 or not out_wav.exists():
        raise SystemExit(f"piper failed: {p.stderr.decode(errors='replace')[-400:]}")


def finish(wav: Path, mp3: Path) -> float:
    """One line, one file: trim dead air, normalise to -16 LUFS mono 48k mp3."""
    sys.path.insert(0, str(ROOT / "studio"))
    import filmkit
    filmkit.FF = filmkit.ffmpeg_bin()
    filmkit.FP = filmkit.ffprobe_bin()
    ff = filmkit.FF
    af = ("silenceremove=start_periods=1:start_threshold=-45dB:start_silence=0.05,"
          "areverse,silenceremove=start_periods=1:start_threshold=-45dB:start_silence=0.05,areverse,"
          "loudnorm=I=-16:TP=-1.5:LRA=11,aresample=48000")
    subprocess.run([ff, "-y", "-v", "error", "-i", str(wav), "-af", af,
                    "-ac", "1", "-c:a", "libmp3lame", "-b:a", "128k", str(mp3)],
                   check=True, timeout=600)
    return filmkit.duration_of(str(mp3))


# ---------------------------------------------------------------- commands ----
def cmd_check(a) -> None:
    print(f"cache: {CACHE}")
    for lang, spec in CATALOG.items():
        print(f"\n{lang}  engine={spec['engine']}  voice={spec['voice']}  {spec['license']}")
        for name, size, _ in spec["files"]:
            state = "ok" if _have(name) else "missing"
            got = f"{CACHE.joinpath(name).stat().st_size / 1e6:.0f} MB" if _have(name) else "-"
            print(f"   {name:34s} {size / 1e6:7.0f} MB  {state:8s} {got}")
    print("\nbinaries:")
    for b in ("ffmpeg", "piper", "piper-tts"):
        print(f"   {b:10s} {shutil.which(b) or 'not found'}")
    try:
        import kokoro_onnx  # noqa: F401
        print("   kokoro_onnx importable")
    except Exception as e:                        # noqa: BLE001
        print(f"   kokoro_onnx NOT importable ({type(e).__name__}) -> pip install kokoro-onnx")


def cmd_plan(a) -> None:
    d, proj = load_project(a.name)
    plan = build_plan(proj, a.lang, {"en": a.voice_en, "fa": a.voice_fa})
    out = d / "audio" / "vo" / "vo_plan.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(plan, ensure_ascii=False, indent=2), encoding="utf-8")
    if not plan["rows"]:
        print("no narration lines in this project — nothing to voice")
        return
    print(f"{len(plan['rows'])} lines  (en {plan['by_lang']['en']} / fa {plan['by_lang']['fa']})"
          f"  ~{plan['total_est_s']:.1f}s of speech\n")
    print(f"{'shot':>4} {'lang':>4} {'engine':>7} {'voice':>22} {'est':>6}  text")
    for r in plan["rows"]:
        print(f"{r['shot']:>4} {r['lang']:>4} {r['engine']:>7} {r['voice']:>22} "
              f"{r['est_s']:>5.1f}s  {r['text'][:52]}")
    print(f"\nplan -> {out.relative_to(ROOT)}")


def cmd_render(a) -> None:
    d, proj = load_project(a.name)
    plan = build_plan(proj, a.lang, {"en": a.voice_en, "fa": a.voice_fa})
    if not plan["rows"]:
        raise SystemExit("no narration lines")
    want = set(int(x) for x in a.only.split(",")) if a.only else None
    vo = d / "audio" / "vo"
    vo.mkdir(parents=True, exist_ok=True)
    work = d / "audio" / "vo" / "_wav"
    work.mkdir(exist_ok=True)

    need = {"en": [], "fa": []}
    for r in plan["rows"]:
        if want and r["shot"] not in want:
            continue
        need[r["lang"]].append(r)
    for lang, rows in need.items():
        if rows:
            fetch(CATALOG[lang]["files"], allow=not a.no_download)

    rendered = []
    for r in plan["rows"]:
        if want and r["shot"] not in want:
            continue
        mp3 = vo / f"s{r['shot']:02d}.mp3"
        if mp3.exists() and not a.force:
            print(f"  s{r['shot']:02d} exists, skip (--force to redo)")
            rendered.append(mp3)
            continue
        wav = work / f"s{r['shot']:02d}.wav"
        # time the model and the ffmpeg post-process separately: folding them into one
        # "rtf" hides which half you are paying for, and ffmpeg on a shared runner is
        # exactly the half that moves.
        import time as _t
        t0 = _t.time()
        if r["engine"] == "kokoro":
            synth_kokoro(r["text"], r["voice"], wav, a.speed)
        elif r["engine"] == "piper":
            synth_piper(r["text"], r["voice"], wav, a.speed)
        else:
            raise SystemExit(f"unknown engine {r['engine']}")
        t1 = _t.time()
        secs = finish(wav, mp3)
        t2 = _t.time()
        r["real_s"] = round(secs, 2)
        r["synth_s"] = round(t1 - t0, 2)
        r["post_s"] = round(t2 - t1, 2)
        r["rtf"] = round((t1 - t0) / max(secs, 1e-6), 2)      # model only
        rendered.append(mp3)
        print(f"  s{r['shot']:02d} {r['lang']} {r['voice']:>22} {secs:5.1f}s  "
              f"rtf {r['rtf']:.2f} (synth {r['synth_s']}s + post {r['post_s']}s)  {mp3.name}")

    (vo / "vo_plan.json").write_text(json.dumps(plan, ensure_ascii=False, indent=2),
                                     encoding="utf-8")
    print(f"\n{len(rendered)} clips -> {vo.relative_to(ROOT)}/")
    print("next: python3 studio/filmkit.py vo <project>   then   ... assemble")


def main() -> None:
    ap = argparse.ArgumentParser(prog="voice", description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("check"); p.set_defaults(fn=cmd_check)

    for name, fn in (("plan", cmd_plan), ("render", cmd_render)):
        p = sub.add_parser(name)
        p.add_argument("name")
        p.add_argument("--lang", default="auto", choices=["auto", "en", "fa"])
        p.add_argument("--voice-en", default=None, help=f"one of {EN_VOICES}")
        p.add_argument("--voice-fa", default=None, help=f"one of {FA_VOICES}")
        if name == "render":
            p.add_argument("--only", default=None, help="shot numbers, e.g. 3,7")
            p.add_argument("--force", action="store_true")
            p.add_argument("--speed", type=float, default=1.0)
            p.add_argument("--no-download", action="store_true")
        p.set_defaults(fn=fn)

    a = ap.parse_args()
    a.fn(a)


if __name__ == "__main__":
    main()
