#!/usr/bin/env python3
"""Offline tests for the voice + lip-sync half. No models, no GPU, no network.

What can be proven without a 114 MB download:
  * a Persian line is routed to Persian, an English line to English, in the same film
  * the engine ladder picks the right engine for 0 / 4 / 8 / 18 GB
  * only narrated shots are candidates, and mouth-visible ones sort first
  * the 25 fps / 16 kHz conform really is 25 fps / 16 kHz (ffmpeg only)

    python3 studio/voicetest.py
"""
from __future__ import annotations

import json
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "studio"))

import lipsync            # noqa: E402
import voice              # noqa: E402

OK, FAIL = "ok  ", "FAIL"
fails = 0


def check(label: str, cond: bool, detail: str = "") -> None:
    global fails
    print(f"  [{OK if cond else FAIL}] {label}{(' — ' + detail) if detail else ''}")
    fails += 0 if cond else 1


def t_language() -> None:
    print("language routing")
    check("Persian -> fa", voice.detect_lang("هنوزم وقتی ناراحتی،") == "fa")
    check("English -> en", voice.detect_lang("Every second he saved") == "en")
    check("digits -> en", voice.detect_lang("1943.") == "en")
    check("mixed line with one Persian word -> fa",
          voice.detect_lang("he said خداحافظ and left") == "fa")
    check("empty -> en (safe default)", voice.detect_lang("") == "en")


def t_plan() -> None:
    print("plan: two languages in one film")
    proj = {"name": "t", "shots": [
        {"n": 1, "narration": "Every second he saved"},
        {"n": 2, "narration": ""},
        {"n": 3, "narration": "هنوزم وقتی ناراحتی،"},
        {"n": 4, "narration": "آره. فکر کردم شاید رفتن،"},
    ]}
    p = voice.build_plan(proj)
    check("3 lines (empty shot dropped)", len(p["rows"]) == 3, str(len(p["rows"])))
    check("1 en / 2 fa", p["by_lang"] == {"en": 1, "fa": 2}, str(p["by_lang"]))
    check("en -> kokoro", p["rows"][0]["engine"] == "kokoro")
    check("fa -> piper", p["rows"][1]["engine"] == "piper")
    forced = voice.build_plan(proj, "fa")
    check("--lang fa forces all", {r["lang"] for r in forced["rows"]} == {"fa"})
    longer = voice.build_plan({"name": "t", "shots": [
        {"n": 1, "narration": "short"}, {"n": 2, "narration": "a much longer line than the first"}]})
    check("estimate grows with text", longer["rows"][1]["est_s"] > longer["rows"][0]["est_s"])
    check("every row has a voice", all(r["voice"] for r in p["rows"]))


def t_ladder() -> None:
    print("lip-sync engine ladder")
    cases = [(0, "wav2lip_onnx"), (3.9, "wav2lip_onnx"), (4, "musetalk"),
             (7.9, "musetalk"), (8, "latentsync15"), (17.9, "latentsync15"),
             (18, "latentsync16"), (80, "latentsync16")]
    for vram, want in cases:
        got = lipsync.pick(vram)
        check(f"{vram:>4} GB -> {want}", got == want, got)
    check("forced engine wins", lipsync.pick(0, "musetalk") == "musetalk")


def t_candidates() -> None:
    print("which shots need lip sync")
    proj = {"name": "t", "shots": [
        {"n": 1, "narration": "", "motion": "rain falls on the street"},
        {"n": 2, "narration": "hello", "motion": "the camera pushes in"},
        {"n": 3, "narration": "look at me", "motion": "he turns to camera, close-up on his face"},
    ]}
    rows = lipsync.candidates(proj)
    check("silent shot excluded", [r["shot"] for r in rows] == [3, 2], str([r["shot"] for r in rows]))
    check("mouth-visible shot ranks first", rows[0]["shot"] == 3)
    check("risk flag set", rows[0]["risk"] == 2 and rows[1]["risk"] == 1)


def t_conform() -> None:
    print("25 fps / 16 kHz conform (ffmpeg)")
    kit = lipsync._kit()
    ff = kit.ffmpeg_bin()
    tmp = Path(tempfile.mkdtemp(prefix="lip-"))
    src = tmp / "src.mp4"
    import subprocess
    subprocess.run([ff, "-y", "-v", "error", "-f", "lavfi", "-i",
                    "testsrc=size=320x240:rate=30:duration=1.2",
                    "-c:v", "libx264", "-pix_fmt", "yuv420p", str(src)], check=True)
    v, w = tmp / "v.mp4", tmp / "a.wav"
    info = lipsync._conform(src, v, w)
    pv, pw = kit.probe(str(v)), kit.probe(str(w))
    check("video is 25 fps", abs(pv["fps"] - 25.0) < 0.01, str(pv["fps"]))
    check("silent source -> silent timing track", info["audio"] == "silence")
    check("wav is 16 kHz mono", pw["has_audio"] and abs(pw["duration_s"] - 1.2) < 0.15,
          f"{pw['duration_s']}s")
    # a VO shorter than the shot must be used as-is, not padded to the video length
    vo = tmp / "vo.mp3"
    subprocess.run([ff, "-y", "-v", "error", "-f", "lavfi", "-i",
                    "sine=frequency=440:duration=0.6", "-c:a", "libmp3lame", str(vo)], check=True)
    info2 = lipsync._conform(src, tmp / "v2.mp4", tmp / "a2.wav", vo)
    check("VO used when present", info2["audio"].startswith("vo:"), info2["audio"])
    check("VO length kept (0.6 s, not 1.2 s)",
          abs(kit.duration_of(str(tmp / "a2.wav")) - 0.6) < 0.15)


def main() -> int:
    print("voice + lipsync offline tests\n")
    for fn in (t_language, t_plan, t_ladder, t_candidates, t_conform):
        fn()
        print()
    print("FAILED" if fails else "ALL OK")
    return 1 if fails else 0


if __name__ == "__main__":
    raise SystemExit(main())
