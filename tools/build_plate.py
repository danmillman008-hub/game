"""Build a clean Stage-1 background plate by per-cell voting over many frames.

Actors and effects occupy a handful of 8x8 cells in any one frame, and they move,
so the *most frequent* 8x8 cell image at each position across a long sequence is
the environment. Cells are compared exactly, so nothing is blended or invented:
every cell in the plate is a cell that the original game actually displayed at
that position.
"""
from __future__ import annotations

import collections
import glob
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from tools.ppm import read_ppm   # noqa: E402
from PIL import Image            # noqa: E402

OUT = ROOT / "reconstruction" / "stage1" / "assets"
CELL = 8


def cells_of(path: str):
    w, h, px = read_ppm(path)
    out = []
    for cy in range(h // CELL):
        row = []
        for cx in range(w // CELL):
            buf = bytearray()
            for y in range(CELL):
                base = ((cy * CELL + y) * w + cx * CELL) * 3
                buf += px[base:base + CELL * 3]
            row.append(bytes(buf))
        out.append(row)
    return w, h, out


def main() -> int:
    paths = []
    for pat in ("/tmp/fight/f*.ppm", "/tmp/walk/f*.ppm", "/tmp/det1/f*.ppm"):
        for f in glob.glob(pat):
            m = re.search(r"f(\d+)\.ppm$", f)
            if m:
                fr = int(m.group(1))
                if 14300 <= fr <= 15600:
                    paths.append((fr, f))
    paths = sorted(set(paths))
    print(f"{len(paths)} frames vote")
    if not paths:
        return 1

    grids = [cells_of(p) for _, p in paths]
    w, h, _ = grids[0]
    cw, ch = w // CELL, h // CELL
    plate = Image.new("RGB", (w, h))
    px = plate.load()
    ambiguous = 0
    for cy in range(ch):
        for cx in range(cw):
            votes = collections.Counter(g[2][cy][cx] for g in grids)
            best, n = votes.most_common(1)[0]
            if n * 2 < len(grids):
                ambiguous += 1
            for y in range(CELL):
                for x in range(CELL):
                    o = (y * CELL + x) * 3
                    px[cx * CELL + x, cy * CELL + y] = tuple(best[o:o + 3])
    plate.save(OUT / "plate.png")
    coverage = 1 - ambiguous / (cw * ch)
    print(f"plate {w}x{h}; {cw*ch} cells, {ambiguous} with a weak majority "
          f"({100*coverage:.1f}% confident)")
    (OUT / "plate.json").write_text(json.dumps({
        "width": w, "height": h, "cell": CELL,
        "frames_used": [p for _, p in paths],
        "cells_total": cw * ch, "cells_weak_majority": ambiguous,
        "method": "per-cell mode across frames; every cell is a cell the game displayed",
    }, indent=1) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
