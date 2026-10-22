"""Extract Stage-1 art from frames the original game produced.

Why not from VRAM: the plane-level decode is still unresolved (RESEARCH_LOG
RL-76), and the 8x8 cells of a real Stage-1 frame do not appear anywhere in the
56 assets decoded from table $00A666 (shape matching: 3.8%), so those tiles are
loaded by another path that has not been traced. Rather than invent art, the art
is taken from the original's own output at the pixel level.

Environment: each frame is cut into 8x8 cells, deduplicated into an atlas, and a
cell map is written out. The renderer then composes the scene from the atlas.

Characters: a sprite's pixels are the pixels that change when it moves. Taking a
frame where a character stands in a region, and a later frame where it has moved
away, gives both the art (from the first frame) and an alpha mask (where the two
differ). No background pixels leak into the sprite.
"""
from __future__ import annotations

import collections
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from tools.ppm import read_ppm            # noqa: E402
from tools.sat_log import read_frames, entries   # noqa: E402

OUT = ROOT / "reconstruction" / "stage1" / "assets"

BG_FRAMES = [14349, 14399, 14449, 14499]     # camera static, stage visible
CELL = 8


def build_atlas() -> dict:
    """Unique 8x8 cells across the given frames, with a cell map per frame."""
    cells: dict[bytes, int] = {}
    atlas: list[bytes] = []
    maps = {}
    for fr in BG_FRAMES:
        w, h, px = read_ppm(f"/tmp/det1/f{fr:04d}.ppm")
        grid = []
        for cy in range(h // CELL):
            row = []
            for cx in range(w // CELL):
                raw = bytearray()
                for y in range(CELL):
                    base = ((cy * CELL + y) * w + cx * CELL) * 3
                    raw += px[base:base + CELL * 3]
                key = bytes(raw)
                idx = cells.get(key)
                if idx is None:
                    idx = cells[key] = len(atlas)
                    atlas.append(key)
                row.append(idx)
            grid.append(row)
        maps[fr] = {"w": w // CELL, "h": h // CELL, "cells": grid}
    print(f"atlas: {len(atlas)} unique cells from {len(BG_FRAMES)} frames")
    return {"atlas": atlas, "maps": maps}


def write_atlas(atlas: list[bytes]) -> None:
    from PIL import Image
    per_row = 32
    rows = (len(atlas) + per_row - 1) // per_row
    img = Image.new("RGB", (per_row * CELL, rows * CELL))
    for i, raw in enumerate(atlas):
        ox, oy = (i % per_row) * CELL, (i // per_row) * CELL
        for y in range(CELL):
            for x in range(CELL):
                o = (y * CELL + x) * 3
                img.putpixel((ox + x, oy + y), (raw[o], raw[o + 1], raw[o + 2]))
    img.save(OUT / "atlas.png")


def extract_sprite(frame_a: str, frame_b: str, box, name: str, threshold=40) -> dict | None:
    """Sprite art + alpha from a region that a character vacates between frames."""
    w, h, pa = read_ppm(frame_a)
    _, _, pb = read_ppm(frame_b)
    x0, y0, x1, y1 = box
    x0, y0 = max(0, x0), max(0, y0)
    x1, y1 = min(w, x1), min(h, y1)
    if x1 <= x0 or y1 <= y0:
        return None
    from PIL import Image
    img = Image.new("RGBA", (x1 - x0, y1 - y0))
    mask = 0
    for y in range(y0, y1):
        for x in range(x0, x1):
            i = (y * w + x) * 3
            a = pa[i:i + 3]
            b = pb[i:i + 3]
            d = sum(abs(a[k] - b[k]) for k in range(3))
            if d > threshold:
                img.putpixel((x - x0, y - y0), (a[0], a[1], a[2], 255))
                mask += 1
            else:
                img.putpixel((x - x0, y - y0), (0, 0, 0, 0))
    if mask < 40:
        return None
    bbox = img.getbbox()
    img = img.crop(bbox)
    img.save(OUT / f"{name}.png")
    return {"file": f"{name}.png", "w": img.width, "h": img.height,
            "source_frames": [frame_a, frame_b], "opaque_pixels": mask}


def player_boxes(frames_path: str, frame: int) -> list[tuple]:
    """Bounding boxes of on-screen sprite clusters at a frame (screen coords)."""
    f = {x["frame"]: x for x in read_frames(frames_path)}[frame]
    pts = []
    for e in entries(f["sat"]):
        if not e["tile"]:
            continue
        x, y = e["x"] - 128, e["y"] - 128
        if -8 <= x < 320 and 0 <= y < 224:
            pts.append((x, y, e["w"] * 8, e["h"] * 8, e["idx"]))
    return pts


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    data = build_atlas()
    write_atlas(data["atlas"])
    (OUT / "atlas.json").write_text(json.dumps({
        "cell": CELL,
        "count": len(data["atlas"]),
        "maps": data["maps"],
        "note": "cells are RGB triplets, row major, 8x8; origin = frame's top-left",
    }) + "\n")

    print("\non-screen sprite clusters (frame 14599, screen coords):")
    for x, y, w, h, idx in sorted(player_boxes("/tmp/det1/frames.bin", 14599))[:14]:
        print(f"   #{idx:2d} at ({x},{y}) size {w}x{h}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
