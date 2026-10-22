"""Extract Stage-1 character sprites from the original's own frames.

A pixel belongs to a character when it is *not* part of the environment. Two
independent tests must agree, which is what removes background contamination:

  * it differs from the other frame in the pair (the character moved/posed), and
  * it differs from the environment plate at that position.

Colours are copied straight from the frame; nothing is recoloured or blended.
Regions where the two tests disagree are left transparent, so a sprite can be
slightly clipped but never contains background art.
"""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from tools.ppm import read_ppm   # noqa: E402
from PIL import Image            # noqa: E402

OUT = ROOT / "reconstruction" / "stage1" / "assets"


def extract(frame_a: str, frame_b: str, plate: str, box, name: str,
            thr_diff=45, thr_plate=35) -> dict:
    w, h, pa = read_ppm(frame_a)
    _, _, pb = read_ppm(frame_b)
    pl = Image.open(plate).convert("RGB")
    pld = list(pl.getdata())
    x0, y0, x1, y1 = box
    x0, y0 = max(0, x0), max(0, y0)
    x1, y1 = min(w, x1), min(h, y1)
    img = Image.new("RGBA", (x1 - x0, y1 - y0), (0, 0, 0, 0))
    kept = 0
    for y in range(y0, y1):
        for x in range(x0, x1):
            i = (y * w + x) * 3
            d_other = sum(abs(pa[i + k] - pb[i + k]) for k in range(3))
            pc = pld[y * w + x]
            d_plate = sum(abs(pa[i + k] - pc[k]) for k in range(3))
            if d_other > thr_diff and d_plate > thr_plate:
                img.putpixel((x - x0, y - y0), (pa[i], pa[i + 1], pa[i + 2], 255))
                kept += 1
    img.save(OUT / f"{name}.png")
    print(f"{name}: {img.size} opaque={kept} from {Path(frame_a).name}")
    return {"name": name, "size": img.size, "opaque": kept}


if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("a")
    ap.add_argument("b")
    ap.add_argument("--box", type=int, nargs=4, required=True)
    ap.add_argument("--name", required=True)
    a = ap.parse_args()
    extract(a.a, a.b, str(OUT / "plate.png"), tuple(a.box), a.name)
