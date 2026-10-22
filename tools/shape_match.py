"""Recover a tilemap from a reference frame by palette-independent shape matching.

For each 8x8 cell of a frame the colour indices are unknown, but the *shape* (the
pattern of distinct colour regions) is not. Both the frame cell and every tile
decoded from the ROM are reduced to a canonical index pattern by renaming
colours in order of first appearance, with the cell's most common colour renamed
to 0 (the background/transparent index). An exact pattern match means the ROM
tile is that cell, whatever palette the game used.
"""
from __future__ import annotations

import collections
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from tools.ppm import read_ppm   # noqa: E402


def canonical(values, background_first: bool) -> tuple[int, ...]:
    """Rename colours by first appearance, optionally forcing the mode to 0."""
    order = []
    if background_first:
        mode = collections.Counter(values).most_common(1)[0][0]
        order.append(mode)
    for v in values:
        if v not in order:
            order.append(v)
    ren = {v: i for i, v in enumerate(order)}
    return tuple(ren[v] for v in values)


def tile_patterns(tiles: list[bytes]) -> dict[tuple[int, ...], list[int]]:
    out = collections.defaultdict(list)
    for i, data in enumerate(tiles):
        if len(data) < 32:
            continue
        vals = []
        for y in range(8):
            o = y * 4
            p0, p1, p2, p3 = data[o], data[o + 1], data[o + 2], data[o + 3]
            for x in range(8):
                b = 7 - x
                vals.append(((p0 >> b) & 1) | (((p1 >> b) & 1) << 1) |
                            (((p2 >> b) & 1) << 2) | (((p3 >> b) & 1) << 3))
        out[canonical(vals, background_first=False)].append(i)
    return out


def main() -> int:
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("frame")
    ap.add_argument("--assets", default=str(ROOT / "reconstruction" / "gfx" / "assets"))
    ap.add_argument("--out", default="/tmp/shapemap.json")
    args = ap.parse_args()

    w, h, px = read_ppm(args.frame)
    tiles = []
    names = []
    for p in sorted(Path(args.assets).glob("*.bin")):
        d = p.read_bytes()
        for i in range(0, len(d) - 31, 32):
            tiles.append(d[i:i + 32])
            names.append((p.name, i // 32))

    pats = tile_patterns(tiles)
    print(f"{len(tiles)} tiles, {len(pats)} distinct shapes")

    cw, ch = w // 8, h // 8
    cells, matched = [], 0
    unknown = collections.Counter()
    for cy in range(ch):
        row = []
        for cx in range(cw):
            vals = []
            for y in range(8):
                base = ((cy * 8 + y) * w + cx * 8) * 3
                for x in range(8):
                    i = base + x * 3
                    vals.append(px[i:i + 3])
            key = canonical(vals, background_first=True)
            cand = pats.get(key)
            if cand:
                matched += 1
                row.append({"tile": cand[0], "asset": names[cand[0]][0],
                            "offset": names[cand[0]][1], "colours": len(set(vals))})
            else:
                row.append(None)
                unknown[len(set(vals))] += 1
        cells.append(row)

    total = cw * ch
    print(f"cells {total}, shape-matched {matched} ({100*matched/total:.1f}%)")
    if unknown:
        print("unmatched by colour count:", dict(unknown))
    Path(args.out).write_text(json.dumps({"w": cw, "h": ch, "cells": cells}) + "\n")
    print(f"-> {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
