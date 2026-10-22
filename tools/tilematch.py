"""Identify which ROM-decoded tiles make up a reference frame.

Given a reference frame and a tile atlas decoded from the ROM, recover an actual
tilemap: for every 8x8 cell of the picture, find the (tile, palette) whose pixels
equal the cell. Cells that no known tile explains are reported, never invented.

This is how the reconstruction gets a real tilemap without depending on a
from-scratch VDP plane renderer: the evidence is the original's own output plus
the ROM's own tile data.
"""
from __future__ import annotations

import collections
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from tools.ppm import read_ppm                 # noqa: E402
from tools.vdp_planes import cram_palettes_rgb  # noqa: E402


def tile_patterns(tiles: list[bytes], pal: list[tuple[int, int, int]]):
    """64-length RGB patterns for one palette, plus their signatures."""
    out = {}
    for t, data in enumerate(tiles):
        if len(data) < 32:
            continue
        rgb = []
        for y in range(8):
            o = y * 4
            p0, p1, p2, p3 = data[o], data[o + 1], data[o + 2], data[o + 3]
            for x in range(8):
                b = 7 - x
                c = ((p0 >> b) & 1) | (((p1 >> b) & 1) << 1) | \
                    (((p2 >> b) & 1) << 2) | (((p3 >> b) & 1) << 3)
                rgb.append(pal[c])
        out[tuple(rgb)] = t
    return out


def main() -> int:
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("frame")
    ap.add_argument("cram")
    ap.add_argument("--assets", default=str(ROOT / "reconstruction" / "gfx" / "assets"))
    ap.add_argument("--out", default="/tmp/tilemap.json")
    args = ap.parse_args()

    w, h, px = read_ppm(args.frame)
    pal_list = cram_palettes_rgb(Path(args.cram).read_bytes())

    assets = Path(args.assets)
    tiles = []
    for p in sorted(assets.glob("*.bin")):
        tiles.append(p.read_bytes())

    per_pal = [tile_patterns(tiles, pal) for pal in pal_list]

    cw, ch = w // 8, h // 8
    cells = []
    matched = 0
    colour_hist = collections.Counter()
    for cy in range(ch):
        row = []
        for cx in range(cw):
            sig = []
            for y in range(8):
                base = ((cy * 8 + y) * w + cx * 8) * 3
                for x in range(8):
                    i = base + x * 3
                    sig.append((px[i], px[i + 1], px[i + 2]))
            sig = tuple(sig)
            found = None
            for pi, table in enumerate(per_pal):
                t = table.get(sig)
                if t is not None:
                    found = {"tile": t, "pal": pi}
                    break
            if found:
                matched += 1
                row.append(found)
            else:
                row.append(None)
                colour_hist[sig[0]] += 1
        cells.append(row)

    total = cw * ch
    print(f"cells: {total}, matched to a ROM tile: {matched} ({100*matched/total:.1f}%)")
    if colour_hist:
        print("most common unexplained cell colours:", colour_hist.most_common(4))
    Path(args.out).write_text(json.dumps({"width": cw, "height": ch, "cells": cells}) + "\n")
    print(f"-> {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
