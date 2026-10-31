#!/usr/bin/env python3
"""lumatch — stop shots from pumping in brightness.

Found on 2026-10-31, on the winter batch: every clip generated from a night still
*loses* light across its four seconds (one went 81 -> 39 mean luminance, a 52 % drop).
Cut four of those together and the film pulses dark-light-dark-light on every cut. The
model does it; the editor has to undo it.

    python3 studio/lumatch.py measure CLIP [CLIP ...]
    python3 studio/lumatch.py match   CLIP [CLIP ...] --out DIR --target 62 --trim 3.0

`measure` reports the head, tail and drift of every clip so the drift is visible before
anyone cuts. `match` writes trimmed, gamma-corrected copies that all land on one mean,
using a gamma curve rather than a brightness offset (an offset lifts the blacks into
fog; the night shots are already mostly shadow).

Gamma per clip:  out = 255 * (in/255) ** (1/g),  g = ln(t/255) / ln(m/255)
which is exactly the curve that maps this clip's mean m onto the target t.
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "studio"))


def ffmpeg() -> str:
    import filmkit
    return filmkit.ffmpeg_bin()


def mean_at(clip: Path, t: float) -> float:
    """Mean luminance of one frame, read through ffmpeg so no PIL dependency."""
    from io import BytesIO
    from PIL import Image, ImageStat
    p = subprocess.run([ffmpeg(), "-v", "error", "-ss", f"{t}", "-i", str(clip),
                        "-frames:v", "1", "-f", "image2pipe", "-vcodec", "png", "-"],
                       capture_output=True, check=True)
    im = Image.open(BytesIO(p.stdout)).convert("L")
    return round(ImageStat.Stat(im).mean[0], 1)


def duration(clip: Path) -> float:
    out = subprocess.run([ffmpeg(), "-i", str(clip)], capture_output=True, text=True).stderr
    for line in out.splitlines():
        if "Duration:" in line:
            h, m, s = line.split("Duration:")[1].split(",")[0].strip().split(":")
            return round(int(h) * 3600 + int(m) * 60 + float(s), 2)
    return 0.0


def probe(clip: Path) -> dict:
    d = duration(clip)
    head = mean_at(clip, 0.05)
    tail = mean_at(clip, max(0.1, d - 0.1))
    return {"clip": clip.name, "duration_s": d, "head": head, "tail": tail,
            "drift_pct": round((tail - head) / head * 100, 1) if head else 0.0}


def gamma_for(mean: float, target: float) -> float:
    import math
    m = min(254.0, max(1.0, mean))
    return round(math.log(target / 255.0) / math.log(m / 255.0), 3)


def cmd_measure(a) -> int:
    rows = [probe(Path(c)) for c in a.clips]
    print(f"{'clip':28s} {'dur':>5s} {'head':>6s} {'tail':>6s} {'drift':>7s}")
    for r in rows:
        flag = "  <-- pumping" if abs(r["drift_pct"]) > 25 else ""
        print(f"{r['clip']:28s} {r['duration_s']:5.2f} {r['head']:6.1f} "
              f"{r['tail']:6.1f} {r['drift_pct']:+6.1f}%{flag}")
    if rows:
        lo, hi = min(r["head"] for r in rows), max(r["head"] for r in rows)
        print(f"\nhead range {lo:.1f}-{hi:.1f} · a cut between the brightest and the "
              f"darkest is a {hi / max(lo, 1e-6):.2f}x jump")
    if a.json:
        Path(a.json).write_text(json.dumps(rows, indent=2), encoding="utf-8")
    return 0


def cmd_match(a) -> int:
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    rows = []
    for c in a.clips:
        clip = Path(c)
        m = mean_at(clip, min(a.trim / 2, duration(clip) / 2))
        g = gamma_for(m, a.target)
        dst = out / f"{clip.stem}_norm.mp4"
        subprocess.run([
            ffmpeg(), "-y", "-v", "error", "-ss", "0", "-t", f"{a.trim}", "-i", str(clip),
            # ffmpeg's eq computes out = (in/255) ** (1/gamma), so it wants 1/g: passing
            # g itself brightened a dark shot by 43 % instead of darkening it by 40 %.
            "-vf", f"eq=gamma={round(1 / g, 3)},fps=24,setsar=1,scale=960:1280",
            "-c:v", "libx264", "-crf", "18", "-pix_fmt", "yuv420p", "-an", str(dst)],
            check=True)
        rows.append({"clip": clip.name, "mean_in": m, "gamma": g, "out": str(dst)})
        print(f"{clip.name:28s} mean {m:5.1f} -> {a.target}  gamma {g}")
    # verify, because a filter that silently does nothing is the whole point of this repo
    print("\nverifying:")
    bad = 0
    for r in rows:
        after = mean_at(Path(r["out"]), min(a.trim / 2, duration(Path(r["out"])) / 2))
        ok = abs(after - a.target) <= a.tolerance
        bad += not ok
        print(f"  {'ok  ' if ok else 'FAIL'} {Path(r['out']).name:28s} {after:5.1f}")
    if a.json:
        Path(a.json).write_text(json.dumps(rows, indent=2), encoding="utf-8")
    return 1 if bad else 0


def main() -> int:
    ap = argparse.ArgumentParser(prog="lumatch", description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("measure"); p.add_argument("clips", nargs="+")
    p.add_argument("--json"); p.set_defaults(fn=cmd_measure)
    p = sub.add_parser("match"); p.add_argument("clips", nargs="+")
    p.add_argument("--out", required=True)
    p.add_argument("--target", type=float, default=62.0)
    p.add_argument("--trim", type=float, default=3.0, help="seconds kept from each clip")
    p.add_argument("--tolerance", type=float, default=6.0)
    p.add_argument("--json"); p.set_defaults(fn=cmd_match)
    a = ap.parse_args()
    return a.fn(a)


if __name__ == "__main__":
    raise SystemExit(main())
