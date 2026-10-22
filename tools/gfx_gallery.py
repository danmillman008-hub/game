"""Render contact sheets of the extracted graphics assets using the game's own palettes.

Palettes come from a CRAM dump captured from the running ROM (Mega Drive CRAM:
16 palettes x 16 entries, 9-bit RGB). Each sheet shows one asset, once per
palette row selected, so the artist can see where the data belongs.
"""
from __future__ import annotations

import json
import os
import struct
import sys
from pathlib import Path

os.environ.setdefault("SDL_VIDEODRIVER", "dummy")
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import pygame  # noqa: E402

from tools.gfx_render import render_sheet, cram_to_rgb  # noqa: E402


def load_cram(path) -> list[list[tuple[int, int, int]]]:
    raw = Path(path).read_bytes()
    # GX keeps 0x80 words: the first 64 are the four normal palettes
    # (the rest are the shadow/highlight copies of the same entries).
    words = [struct.unpack_from(">H", raw, i)[0] for i in range(0, min(0x140, len(raw)), 2)]
    if max(words[:64]) > 0x0EEE:                     # tolerate byte-swapped dumps
        words = [((w >> 8) | (w << 8)) & 0xFFFF for w in words]
    return [[cram_to_rgb(words[p * 16 + i]) for i in range(16)] for p in range(4)]


def main(argv=None) -> int:
    argv = argv or sys.argv[1:]
    cram_path = argv[0]
    only = [int(x) for x in argv[1:]] if len(argv) > 1 else None
    palettes = load_cram(cram_path)
    pygame.init()
    pygame.display.set_mode((64, 64))

    adir = ROOT / "reconstruction" / "gfx" / "assets"
    outdir = ROOT / "reconstruction" / "gfx" / "gallery"
    outdir.mkdir(parents=True, exist_ok=True)
    index = json.loads((adir / "index.json").read_text())
    made = 0
    for e in index["entries"]:
        if "file" not in e:
            continue
        if only and e["index"] not in only:
            continue
        data = (adir / e["file"]).read_bytes()
        n = len(data) // 32
        cols = 16 if n > 64 else 8
        scale = 3 if n > 128 else 4
        sheets = []
        for p in range(len(palettes)):
            sheets.append(render_sheet(data, cols=cols, scale=scale,
                                       palette=palettes[p], bg=(12, 8, 20)))
        w = max(s.get_width() for s in sheets)
        h = sum(s.get_height() + 6 for s in sheets)
        page = pygame.Surface((w, h))
        page.fill((0, 0, 0))
        y = 0
        for s in sheets:
            page.blit(s, (0, y))
            y += s.get_height() + 6
        name = f"asset{e['index']:02d}_{e['src']}.png"
        pygame.image.save(page, outdir / name)
        made += 1
    print(f"gallery sheets: {made} -> {outdir.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
