"""Extract Stage 1 environment data (tiles, nametables, palettes) from a capture.

Everything comes from the machine state the original game produced, not from
screenshots: tile patterns and nametables out of VRAM, colours out of CRAM.

Outputs (reconstruction/stage1/assets/):
    stage.json   plane A/B world map, palettes, tile atlas reference
    tiles.png    tile atlas, 16 tiles per row, 8x8 px, decoded to RGB

The world map is assembled by sampling several frames: the game streams columns
into a 64x32 nametable and scrolls it, so no single frame contains the whole
stage. Each sample contributes the columns that are visible at that moment,
placed using the horizontal scroll value the VDP is actually using.
"""
from __future__ import annotations

import argparse
import base64
import json
import struct
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from tools.sat_log import read_frames            # noqa: E402
from tools.frame_state import vram_at            # noqa: E402

PLANE_SIZES = {0: (32, 32), 1: (64, 32), 2: (32, 64), 3: (64, 64)}


def cram_rgb(words: list[int]) -> list[tuple[int, int, int]]:
    return [((w >> 1) & 7, (w >> 5) & 7, (w >> 9) & 7) for w in words]


def tile_pixels(vram: bytes, index: int) -> list[list[int]]:
    """8x8 colour indices for one 4bpp tile (Mega Drive planar layout)."""
    base = index * 32
    rows = []
    for y in range(8):
        o = base + y * 4
        p0, p1, p2, p3 = vram[o], vram[o + 1], vram[o + 2], vram[o + 3]
        rows.append([(((p0 >> (7 - x)) & 1) | (((p1 >> (7 - x)) & 1) << 1) |
                      (((p2 >> (7 - x)) & 1) << 2) | (((p3 >> (7 - x)) & 1) << 3))
                     for x in range(8)])
    return rows


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("capture")
    ap.add_argument("--dump-from", type=int, default=14000)
    ap.add_argument("--out", default=str(ROOT / "reconstruction" / "stage1" / "assets"))
    args = ap.parse_args()

    cap = Path(args.capture)
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    frames = {f["frame"]: f for f in read_frames(str(cap / "frames.bin"))}
    sample_frames = sorted(frames)[::10]

    # --- world map assembly -------------------------------------------------
    plane_a: dict[tuple[int, int], int] = {}
    plane_b: dict[tuple[int, int], int] = {}
    plane_a_pri: dict[tuple[int, int], int] = {}
    seen_scroll = []
    for fr in sample_frames:
        f = frames[fr]
        regs = f["regs"]
        vram = vram_at(str(cap / "vram.bin"), fr - args.dump_from)
        pw, ph = PLANE_SIZES[(regs[16] >> 0) & 3]
        base_a = (regs[2] & 0x38) << 10
        base_b = (regs[4] & 0x07) << 13
        hs_a = f["vsram"][0] & 0x3FF if False else None
        # horizontal scroll: from the hscroll table unless in per-column mode
        hs_base = (regs[13] & 0x3F) << 10
        hsa = struct.unpack_from(">H", vram, hs_base)[0] & 0x3FF
        hsb = struct.unpack_from(">H", vram, hs_base + 2)[0] & 0x3FF
        seen_scroll.append((fr, hsa, hsb))
        for col in range(40):
            wx = (hsa // 8 + col)
            for row in range(28):
                wy = row
                ca = base_a + (((wy % ph) * pw + (wx % pw)) * 2)
                cb = base_b + (((wy % ph) * pw + (wx % pw)) * 2)
                wa = struct.unpack_from(">H", vram, ca)[0]
                wb = struct.unpack_from(">H", vram, cb)[0]
                key = (wx % pw, wy)
                plane_a.setdefault(key, wa)
                plane_b.setdefault(key, wb)
                plane_a_pri.setdefault(key, 1 if wa & 0x8000 else 0)

    w = max(k[0] for k in plane_a) + 1
    h = max(k[1] for k in plane_a) + 1
    print(f"world map: {w} x {h} cells ({w*8} x {h*8} px)")
    print("scroll samples (frame, planeA, planeB):", seen_scroll[:6], "...")

    a_cells = [plane_a.get((x, y), 0) for y in range(h) for x in range(w)]
    b_cells = [plane_b.get((x, y), 0) for y in range(h) for x in range(w)]

    # --- palettes and tiles -------------------------------------------------
    last = max(frames)
    cram = frames[last]["cram"]
    flat = [tuple(c) for c in cram_rgb(cram)]
    pal = [flat[i * 16:(i + 1) * 16] for i in range(4)]

    used = set()
    for c in a_cells + b_cells:
        used.add(c & 0x7FF)
    tiles = sorted(used)
    tile_index = {t: i for i, t in enumerate(tiles)}
    atlas = bytearray()
    for t in tiles:
        for row in tile_pixels(vram, t):
            atlas.extend(row)

    (out / "stage.json").write_text(json.dumps({
        "width_cells": w, "height_cells": h,
        "plane_a": a_cells, "plane_b": b_cells,
        "palette": pal,
        "tiles": {"count": len(tiles), "rom_indices": tiles,
                  "data": base64.b64encode(bytes(atlas)).decode()},
        "note": "cell = bit15 priority, bits14-13 palette, bit12 vflip, bit11 hflip, bits10-0 tile",
        "source": {"capture": str(cap), "frames": [min(sample_frames), max(sample_frames)]},
    }, indent=None) + "\n")

    # --- tile atlas PNG (my own decode of the ROM's tile data) --------------
    from PIL import Image
    cols_per_row = 16
    rows_n = (len(tiles) + cols_per_row - 1) // cols_per_row
    img = Image.new("RGB", (cols_per_row * 8, rows_n * 8))
    p = img.load()
    for i, t in enumerate(tiles):
        ox = (i % cols_per_row) * 8
        oy = (i // cols_per_row) * 8
        for y in range(8):
            for x in range(8):
                idx = tile_pixels(vram, t)[y][x]
                r, g, b = pal[0][idx]
                p[ox + x, oy + y] = (r * 255 // 7, g * 255 // 7, b * 255 // 7)
    img.save(out / "tiles.png")
    print(f"tiles: {len(tiles)} -> {out/'tiles.png'}")
    print(f"stage -> {out/'stage.json'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
