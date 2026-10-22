"""Environment plate, voting only over frames in which each cell is unoccupied.

A cell is "occupied" when a sprite entry from the original game's sprite table
covers it. The plate for that cell is then taken from frames where nothing covers
it, so no character art can leak into the environment. Ties are broken by
whichever candidate occurs first, and the vote strength is recorded.
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

from tools.ppm import read_ppm                        # noqa: E402
from tools.sat_log import read_frames, entries        # noqa: E402
from PIL import Image                                 # noqa: E402

OUT = ROOT / "reconstruction" / "stage1" / "assets"
CELL = 8


def occupied_cells(sat_frame) -> set[tuple[int, int]]:
    occ = set()
    for e in entries(sat_frame["sat"]):
        if not e["tile"]:
            continue
        x, y = e["x"] - 128, e["y"] - 128
        if e["w"] > 8 or e["h"] > 8:      # malformed / off-table entry
            continue
        for by in range(e["h"]):
            for bx in range(e["w"]):
                cx, cy = (x + bx * 8) // CELL, (y + by * 8) // CELL
                if 0 <= cx < 40 and 0 <= cy < 28:
                    occ.add((cx, cy))
    return occ


def frame_cells(path: str):
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
    return out


def main() -> int:
    out = OUT
    out.mkdir(parents=True, exist_ok=True)
    sources = [("fight", "/tmp/fight"), ("walk", "/tmp/walk")]
    data = []
    for name, d in sources:
        fb = Path(d) / "frames.bin"
        if not fb.exists():
            continue
        sats = {f["frame"]: f for f in read_frames(str(fb))}
        for p in glob.glob(f"{d}/f*.ppm"):
            m = re.search(r"f(\d+)\.ppm$", p)
            if not m:
                continue
            fr = int(m.group(1))
            y0 = 14200 if name == "fight" else 14200
            if not (y0 <= fr <= 15800) or fr not in sats:
                continue
            data.append((fr, p, occupied_cells(sats[fr])))
    print(f"{len(data)} frames, each with its occupied-cell set")
    if not data:
        return 1

    grids = [(fr, frame_cells(p), occ) for fr, p, occ in data]
    h = len(grids[0][1])
    w = len(grids[0][1][0])
    plate = Image.new("RGB", (w * CELL, h * CELL))
    px = plate.load()
    weak = 0
    used = 0
    for cy in range(h):
        for cx in range(w):
            votes = collections.Counter()
            for fr, grid, occ in grids:
                if (cx, cy) in occ:
                    continue
                votes[grid[cy][cx]] += 1
            if not votes:
                weak += 1
                continue
            best, n = votes.most_common(1)[0]
            used += 1
            if n * 2 <= sum(votes.values()):
                weak += 1
            for y in range(CELL):
                for x in range(CELL):
                    o = (y * CELL + x) * 3
                    px[cx * CELL + x, cy * CELL + y] = tuple(best[o:o + 3])
    plate.save(out / "plate.png")
    print(f"plate from {used}/{h*w} cells with any uncontested sample; "
          f"{weak} cells lack a clear majority")
    (out / "plate.json").write_text(json.dumps({
        "cells": h * w, "cells_with_samples": used, "cells_weak": weak,
        "frames": len(data),
        "method": "per-cell mode over frames where no sprite covers the cell",
    }, indent=1) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
