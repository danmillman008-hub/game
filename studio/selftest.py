#!/usr/bin/env python3
"""Offline self-test for filmkit's editing half.

No Mivi call, no credits: builds two synthetic 4 s clips with ffmpeg, then runs the
real verbs (assemble -> mix -> qc) exactly as a project would. If this passes, the
cut/grade/mix/qc path is sound and only generation is left to verify with a render.

    python3 studio/selftest.py
"""
from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
KIT = ROOT / "studio" / "filmkit.py"


def kit(*args) -> str:
    p = subprocess.run([sys.executable, str(KIT), *args], capture_output=True, text=True,
                       timeout=600)
    if p.returncode != 0:
        raise SystemExit(f"filmkit {' '.join(args)} failed:\n{p.stdout}\n{p.stderr}")
    return p.stdout


def ffmpeg() -> str:
    sys.path.insert(0, str(ROOT / "studio"))
    import filmkit
    return filmkit.ffmpeg_bin()


def main() -> int:
    ff = ffmpeg()
    tmp = Path(tempfile.mkdtemp(prefix="filmkit-"))
    proj = tmp / "selftest"
    kit("new", str(proj))

    (proj / "clips").mkdir(exist_ok=True)
    for i, colour in enumerate(("navy", "darkgreen"), start=1):
        out = proj / "clips" / f"s{i:02d}_t1.mp4"
        subprocess.run([ff, "-y", "-v", "error",
                        "-f", "lavfi", "-i", f"color=c={colour}:s=960x1280:r=32:d=4.03",
                        "-c:v", "libx264", "-pix_fmt", "yuv420p", str(out)], check=True)

    data = json.loads((proj / "project.json").read_text())
    data["shots"] = [{"n": 1, "motion": "test a", "still": None,
                      "clip": "clips/s01_t1.mp4", "state": "rendered", "takes": []},
                     {"n": 2, "motion": "test b", "still": None,
                      "clip": "clips/s02_t1.mp4", "state": "rendered", "takes": []}]
    (proj / "project.json").write_text(json.dumps(data, indent=2))

    out = kit("assemble", str(proj), "--crossfade", "0.4")
    assert "assembled 2 clips" in out, out

    audio = tmp / "vo.mp3"
    subprocess.run([ff, "-y", "-v", "error", "-f", "lavfi", "-i", "sine=frequency=300:duration=3",
                    str(audio)], check=True)
    kit("mix", str(proj), "--vo", str(audio))

    qc_raw = kit("qc", str(proj))
    report = json.loads((proj / "qc" / "report.json").read_text())

    final = report.get("final") or {}
    checks = {
        "resolution 960x1280": (final.get("width"), final.get("height")) == (960, 1280),
        "duration ~7.7s (2x4.03-0.4)": 7.0 <= float(final.get("duration_s") or 0) <= 8.5,
        "audio present": bool(final.get("has_audio")),
        "no qc issues": not report.get("issues"),
        "frames sampled": bool(report.get("frames")),
    }
    print(json.dumps(checks, indent=2))
    if not all(checks.values()):
        print(qc_raw[:1200])
        shutil.rmtree(tmp, ignore_errors=True)
        return 1
    print("SELFTEST OK")
    shutil.rmtree(tmp, ignore_errors=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
