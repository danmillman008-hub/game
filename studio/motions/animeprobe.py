#!/usr/bin/env python3
"""animeprobe.py — did the model keep the 2D style, or did it drift to photoreal?

Eyeballing eight clips is not a measurement. Three numbers are enough:

    palette   unique colours after 5-bit quantisation. A cel plate has 5-15.
              A photoreal frame has thousands. Ratio out/in is the drift factor.
    edges     share of pixels with a strong gradient. Line art: thin, high contrast.
              Photoreal: dense mid-strength texture. Reported with the plate's own value.
    motion    mean absolute difference between the first and last frame. 0.00 means
              the clip is dead (nothing moved); a very high value means the frame
              warped rather than the subject moving.

Verdict per clip:
    held     palette <= 3x the plate and motion > 0.5      (style kept, something moved)
    softened palette <= 10x                                (still 2D, less crisp)
    drifted  palette > 10x                                 (photoreal came back)
    dead     motion <= 0.5                                 (nothing happened)

    python3 studio/motions/animeprobe.py <clip dir or files> --plate films/anime_test/stills/a1_wide.png
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
import tempfile
from pathlib import Path

from PIL import Image, ImageChops, ImageFilter, ImageOps, ImageStat

ROOT = Path(__file__).resolve().parent.parent.parent


def ffmpeg() -> str:
    sys.path.insert(0, str(ROOT / "studio"))
    import filmkit
    return filmkit.ffmpeg_bin()


def frames(clip: Path, n: int = 3) -> list[Image.Image]:
    dur = 4.0
    tmp = Path(tempfile.mkdtemp(prefix="anime-"))
    out = []
    for i in range(n):
        t = 0.2 + (dur - 0.6) * i / max(1, n - 1)
        p = tmp / f"f{i}.png"
        subprocess.run([ffmpeg(), "-y", "-v", "error", "-ss", f"{t:.2f}", "-i", str(clip),
                        "-frames:v", "1", str(p)], check=True)
        out.append(Image.open(p).convert("RGB"))
    return out


def palette(im: Image.Image) -> int:
    q = ImageOps.posterize(im.resize((240, 320)), 5)
    return len(q.getcolors(maxcolors=1 << 20) or [])


def edge_share(im: Image.Image, thr: int = 40) -> float:
    g = im.convert("L").resize((240, 320)).filter(ImageFilter.FIND_EDGES)
    hist = g.histogram()
    strong = sum(hist[thr:])
    return round(strong / (240 * 320), 4)


def plate_diff(a: Image.Image, plate: Image.Image) -> float:
    """0-255 average distance to the input frame. This is the metric that catches the
    failure the palette cannot see: a clip that stays flat but rebuilds the world."""
    d = ImageChops.difference(a.convert("L").resize((96, 128)),
                              plate.convert("L").resize((96, 128)))
    return round(ImageStat.Stat(d).mean[0], 2)


def motion(a: Image.Image, b: Image.Image) -> float:
    d = ImageChops.difference(a.resize((240, 320)), b.resize((240, 320))).convert("L")
    return round(ImageStat.Stat(d).mean[0], 2)


def judge(clip: Path, plate: Image.Image) -> dict:
    fr = frames(clip)
    pal = [palette(f) for f in fr]
    p0 = palette(plate)
    ratio = round((sum(pal) / len(pal)) / max(p0, 1), 2)
    mot = motion(fr[0], fr[-1])
    pd = [plate_diff(f, plate) for f in fr]
    if mot <= 0.5:
        verdict = "dead"
    elif ratio > 10:
        verdict = "drifted"
    elif pd[-1] > 25:
        verdict = "rebuilt"        # flat, but no longer the same place
    elif ratio > 3:
        verdict = "softened"
    else:
        verdict = "held"
    return {"clip": clip.name, "palette": pal, "plate_palette": p0, "drift_x": ratio,
            "edge": [edge_share(f) for f in fr], "motion": mot, "plate_diff": pd,
            "verdict": verdict}


def main() -> int:
    ap = argparse.ArgumentParser(prog="animeprobe", description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("paths", nargs="+")
    ap.add_argument("--plate", default=str(ROOT / "films/anime_test/stills/a1_wide.png"),
                    help="default plate; a clip whose name starts with a2_ uses a2_eye.png")
    ap.add_argument("--json", default=None)
    a = ap.parse_args()

    plate = Image.open(a.plate).convert("RGB")
    alt = Path(a.plate).with_name("a2_eye.png")

    def plate_for(clip: Path) -> Image.Image:
        """Each probe shot has its own key frame — compare against the right one."""
        if clip.name.startswith("a2_") and alt.exists():
            return Image.open(alt).convert("RGB")
        return plate
    clips: list[Path] = []
    for p in map(Path, a.paths):
        clips += sorted(p.glob("*.mp4")) if p.is_dir() else [p]
    if not clips:
        raise SystemExit("no clips found")

    rows = [judge(c, plate_for(c)) for c in clips]
    print(f"plate: {Path(a.plate).name}  palette {rows[0]['plate_palette']}  "
          f"edge {edge_share(plate)}")
    print(f"\n{'clip':28s} {'verdict':9s} {'drift':>6s} {'motion':>7s} "
          f"{'plate0':>7s} {'plateN':>7s}")
    for r in rows:
        print(f"{r['clip']:28s} {r['verdict']:9s} {r['drift_x']:>6.2f} {r['motion']:>7.2f} "
              f"{r['plate_diff'][0]:>7.2f} {r['plate_diff'][-1]:>7.2f}")
    good = sum(1 for r in rows if r["verdict"] in ("held", "softened"))
    built = sum(1 for r in rows if r["verdict"] == "rebuilt")
    print(f"\n{built} rebuilt the world while staying flat")
    print(f"{good}/{len(rows)} kept a 2D look · "
          f"{sum(1 for r in rows if r['verdict'] == 'dead')} dead · "
          f"{sum(1 for r in rows if r['verdict'] == 'drifted')} drifted to photoreal")
    if a.json:
        Path(a.json).write_text(json.dumps(rows, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"-> {a.json}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
