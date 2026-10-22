"""Render decoded tile data as PNG (contact sheets) for inspection.

Genesis 4bpp tiles are 32 bytes: 8 rows x 4 bytes, one byte per bit-plane,
MSB = leftmost pixel. Colour index = p0 | p1<<1 | p2<<2 | p3<<3.

Two modes:
  --gray     index -> grayscale (structure check, no palette needed)
  --palette  apply a 16-colour palette (CRAM-derived or explicit)

Usage:
    python tools/gfx_render.py --bank 0 --gray
    python tools/gfx_render.py --bank 0 --palette 1
"""
from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

os.environ.setdefault("SDL_VIDEODRIVER", "dummy")

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

OUT = ROOT / "reconstruction" / "gfx" / "preview"


def tile_pixels(tile: bytes, layout: str = "nibble") -> list[list[int]]:
    """8x8 colour indices from a 32-byte tile.

    `layout="nibble"` is the layout this ROM actually produces: four bytes per
    row, two pixels per byte, high nibble = left pixel. Established empirically
    (mean absolute neighbour difference 1.15 vs 3.18 for the planar reading on
    bank 5) and used for every gallery in this repository.

    `layout="planar"` is the stock Mega Drive bit-plane order, kept so the
    comparison can be reproduced.
    """
    rows = []
    if layout == "nibble":
        for y in range(8):
            base = y * 4
            row = []
            for b in tile[base:base + 4]:
                row.append((b >> 4) & 0x0F)
                row.append(b & 0x0F)
            rows.append(row)
        return rows
    for y in range(8):
        base = y * 4
        b0, b1, b2, b3 = tile[base:base + 4]
        row = []
        for x in range(8):
            shift = 7 - x
            idx = ((b0 >> shift) & 1) | (((b1 >> shift) & 1) << 1) | \
                  (((b2 >> shift) & 1) << 2) | (((b3 >> shift) & 1) << 3)
            row.append(idx)
        rows.append(row)
    return rows


def cram_to_rgb(word: int) -> tuple[int, int, int]:
    """Genesis CRAM word -> 8-bit RGB (3 bits per channel, bits 1-3/5-7/9-11)."""
    r = (word >> 1) & 0x7
    g = (word >> 5) & 0x7
    b = (word >> 9) & 0x7
    return (r * 255 // 7, g * 255 // 7, b * 255 // 7)


GRAY = [(i * 17, i * 17, i * 17) for i in range(16)]


def render_sheet(tiles: bytes, cols: int = 16, scale: int = 3,
                 palette: list[tuple[int, int, int]] | None = None,
                 max_tiles: int | None = None, bg=(24, 18, 40),
                 layout: str = "nibble", start: int = 0):
    import pygame

    n = len(tiles) // 32
    n = max(0, n - start)
    if max_tiles:
        n = min(n, max_tiles)
    rows = max(1, (n + cols - 1) // cols)
    cell = 8 * scale
    surf = pygame.Surface((cols * cell, rows * cell))
    surf.fill(bg)
    pal = palette or GRAY
    for t in range(n):
        px = tile_pixels(tiles[(start + t) * 32:(start + t + 1) * 32], layout)
        ox = (t % cols) * cell
        oy = (t // cols) * cell
        for y in range(8):
            for x in range(8):
                idx = px[y][x]
                if idx == 0:
                    continue                      # index 0 = transparent in sprites
                colour = pal[idx] if idx < len(pal) else (255, 0, 255)
                surf.fill(colour, (ox + x * scale, oy + y * scale, scale, scale))
        # grid
        pygame.draw.rect(surf, (40, 34, 62), (ox, oy, cell, cell), 1)
    return surf


def main(argv=None) -> int:
    import json
    import pygame
    ap = argparse.ArgumentParser()
    ap.add_argument("--bank", type=int, default=0)
    ap.add_argument("--entry", type=int, default=0)
    ap.add_argument("--gray", action="store_true")
    ap.add_argument("--palette", default=None, help="palette hex file or 'cram:0xADDR'")
    ap.add_argument("--scale", type=int, default=3)
    ap.add_argument("--cols", type=int, default=16)
    ap.add_argument("--max", type=int, default=0)
    ap.add_argument("--out", default=None)
    ap.add_argument("--layout", default="nibble", choices=("nibble", "planar"))
    ap.add_argument("--start", type=int, default=0)
    args = ap.parse_args(argv)

    pygame.init()
    pygame.display.set_mode((64, 64))

    sys.path.insert(0, str(ROOT))
    from tools.gfx_banks import load_rom
    from tools.sor_gfx_format import decode

    rom = load_rom()
    import json as _json
    inv = _json.loads((ROOT / "reconstruction" / "gfx" / "banks.json").read_text())
    items = [i for i in inv["items"] if i["bank"] == args.bank and i["entry"] == args.entry]
    if not items:
        raise SystemExit("no such bank/entry")
    src = int(items[0]["src"], 16)
    data, meta = decode(rom, src)

    pal = None
    if args.palette:
        if args.palette.startswith("cram:"):
            addr = int(args.palette.split(":")[1], 16)
            pal = [cram_to_rgb(int.from_bytes(rom[addr + 2 * i:addr + 2 * i + 2], "big"))
                   for i in range(16)]
        else:
            pal = []
            for line in Path(args.palette).read_text().split():
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                pal.append(cram_to_rgb(int(line, 16)))
    surf = render_sheet(data, cols=args.cols, scale=args.scale, palette=pal,
                        max_tiles=args.max or None, layout=args.layout, start=args.start)
    OUT.mkdir(parents=True, exist_ok=True)
    out = Path(args.out).resolve() if args.out else OUT / f"bank{args.bank:02d}_{args.entry}_" \
                                                 f"{'gray' if not pal else 'pal'}.png"
    pygame.image.save(surf, out)
    try:
        shown = out.relative_to(ROOT)
    except ValueError:
        shown = out
    print(f"{shown}  tiles={meta['tiles']} size={surf.get_size()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
