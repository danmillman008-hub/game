"""Software re-implementation of the Mega Drive VDP tile renderer.

Purpose: turn a captured machine state (VRAM + CRAM + VDP registers) back into
the exact picture the console produced, so a reconstruction can be compared with
the original at the pixel level, and so extracted tiles/nametables can be
verified against a real frame.

Coordinate conventions follow the hardware:
  * 4bpp tiles are 32 bytes, 8 rows x 4 bit-planes, MSB = leftmost pixel,
    colour index = p0 | p1<<1 | p2<<2 | p3<<3
  * plane A/B nametable entry: bit15 priority, bits 14-13 palette, bit12 vflip,
    bit11 hflip, bits 10-0 tile index
  * sprite entry (8 bytes): Y-128, size/link, palette|vflip|hflip|tile, X-128
  * screen position of a plane pixel = plane coordinate - scroll value
"""
from __future__ import annotations

import struct
from pathlib import Path

SCREEN_W = 320
SCREEN_H = 224

PLANE_SIZES = {  # reg 0x10 bits: (A low nibble / B high nibble)
    0: (32, 32), 1: (64, 32), 2: (32, 64), 3: (64, 64),
}


def load_state(prefix) -> dict:
    """Load a `.vram/.cram/.vdp` triple written by tools/md_capture."""
    p = Path(prefix)
    base = p.parent / p.name if p.suffix == "" else p
    regs_raw = (base.parent / (base.name + ".vdp")).read_bytes()
    raw_vram = (base.parent / (base.name + ".vram")).read_bytes()
    # GX stores VRAM as host (little-endian) words inside a byte array, so the
    # dump is byte-swapped relative to the address order the VDP uses.
    vram = bytearray(len(raw_vram))
    vram[0::2] = raw_vram[1::2]
    vram[1::2] = raw_vram[0::2]
    return {
        "vram": bytes(vram),
        "cram": (base.parent / (base.name + ".cram")).read_bytes(),
        "regs": list(regs_raw[:24]),
        "status": (regs_raw[24] << 8) | regs_raw[25],
    }


def cram_colour(word: int) -> tuple[int, int, int]:
    r, g, b = (word >> 1) & 7, (word >> 5) & 7, (word >> 9) & 7
    return (r * 255 // 7, g * 255 // 7, b * 255 // 7)


def palettes(state) -> list[list[tuple[int, int, int]]]:
    # GX keeps CRAM as host (little-endian) words inside a byte array
    words = [struct.unpack_from("<H", state["cram"], i * 2)[0] for i in range(0x40)]
    return [[cram_colour(words[p * 16 + i]) for i in range(16)] for p in range(4)]


def tile_rows(vram: bytes, index: int) -> list[list[int]]:
    """8x8 colour indices of one 4bpp tile."""
    base = (index & 0x7FF) * 32
    out = []
    for y in range(8):
        b0, b1, b2, b3 = vram[base + y * 4: base + y * 4 + 4]
        out.append([((b0 >> s) & 1) | (((b1 >> s) & 1) << 1) |
                    (((b2 >> s) & 1) << 2) | (((b3 >> s) & 1) << 3)
                    for s in (7, 6, 5, 4, 3, 2, 1, 0)])
    return out


def plane_geometry(regs, plane: str):
    base = ((regs[2] & 0x38) << 10) if plane == "a" else ((regs[4] & 0x07) << 13)
    nib = regs[16] & 0x0F if plane == "a" else (regs[16] >> 4) & 0x0F
    w, h = PLANE_SIZES[nib & 3]
    return base, w, h


def scroll_values(state) -> tuple[list[int], list[int]]:
    """(horizontal scroll per line, vertical scroll per column)."""
    vram, regs = state["vram"], state["regs"]
    hscroll = [0] * SCREEN_H
    hbase = (regs[13] & 0x3F) << 10
    if regs[11] & 0x04:                       # per-line horizontal scroll
        for line in range(SCREEN_H):
            w = struct.unpack_from(">H", vram, hbase + line * 4)[0]
            hscroll[line] = (w & 0x3FF) - (0x400 if w & 0x200 else 0)
    else:
        w = struct.unpack_from(">H", vram, hbase)[0]
        val = (w & 0x3FF) - (0x400 if w & 0x200 else 0)
        hscroll = [val] * SCREEN_H

    vscroll = [0] * 40                        # one per tile column
    mode = regs[11] & 0x03
    if mode in (1, 3) or True:                # VSRAM is always meaningful
        for col in range(40):
            try:
                w = struct.unpack_from(">H", vram, 0)  # placeholder, see caller
                _ = w
            except Exception:
                pass
    return hscroll, vscroll


def vsram_values(state) -> list[int]:
    """Vertical scroll values live in VSRAM, which is captured by the harness
    in the `.vdp` dump as an appendix when available; default is zero."""
    return state.get("vsram") or [0] * 40


def render_plane(state, plane: str, hscroll: list[int], vsram: list[int]):
    """Return an SCREEN_H x SCREEN_W array of (colour, priority) or None."""
    vram, regs = state["vram"], state["regs"]
    pal = palettes(state)
    base, pw, ph = plane_geometry(regs, plane)
    img = [[None] * SCREEN_W for _ in range(SCREEN_H)]
    cache: dict[int, list[list[int]]] = {}
    for sy in range(SCREEN_H):
        hs = hscroll[sy] if sy < len(hscroll) else 0
        for sx in range(SCREEN_W):
            vcol = sx // 8
            vs = vsram[vcol] if vcol < len(vsram) else 0
            wx = (sx + hs) & (pw * 8 - 1)
            wy = (sy + vs) & (ph * 8 - 1)
            entry_addr = base + (((wy // 8) * pw + (wx // 8)) * 2)
            if entry_addr + 1 >= len(vram):
                continue
            w = struct.unpack_from(">H", vram, entry_addr)[0]
            ti = w & 0x7FF
            if ti == 0:
                continue
            rows = cache.get(ti)
            if rows is None:
                rows = cache[ti] = tile_rows(vram, ti)
            py = wy % 8
            px = wx % 8
            if w & 0x1000:
                py = 7 - py
            if w & 0x0800:
                px = 7 - px
            idx = rows[py][px]
            if idx:
                img[sy][sx] = (pal[(w >> 13) & 3][idx], bool(w & 0x8000))
    return img


def sat_entries(vram: bytes, addr: int) -> list[dict]:
    """Decode the sprite attribute table by following the link chain."""
    out = []
    idx = 0
    seen = set()
    while idx < 80 and idx not in seen:
        seen.add(idx)
        off = addr + idx * 8
        if off + 7 >= len(vram):
            break
        y, size, attr, x = struct.unpack_from(">HHHH", vram, off)
        if y == 0 and attr == 0 and x == 0 and size == 0:
            break
        out.append({
            "index": idx,
            "x": (x & 0x1FF) - 0x80,
            "y": (y & 0x3FF) - 0x80,
            "w": ((size >> 10) & 3) + 1,
            "h": ((size >> 8) & 3) + 1,
            "tile": attr & 0x7FF,
            "pal": (attr >> 13) & 3,
            "pri": bool(attr & 0x8000),
            "vflip": bool(attr & 0x1000),
            "hflip": bool(attr & 0x0800),
            "link": (size >> 12) & 0xF,
        })
        idx = (size >> 12) & 0xF
    return out


def render_sprites(state) -> list[tuple[int, int, tuple, bool]]:
    """Return a list of (x, y, colour, priority) sprite pixels, back to front."""
    vram, regs = state["vram"], state["regs"]
    pal = palettes(state)
    sat = (regs[5] & 0x7F) << 9
    pixels = []
    for s in sat_entries(vram, sat):
        for ty in range(s["h"]):
            for tx in range(s["w"]):
                ti = (s["tile"] + ty * s["w"] + tx) if not (s["vflip"] or s["hflip"]) else (s["tile"] + ty * s["w"] + tx)
                rows = tile_rows(vram, ti)
                for py in range(8):
                    for px in range(8):
                        yy = 7 - py if s["vflip"] else py
                        xx = 7 - px if s["hflip"] else px
                        idx = rows[yy][xx]
                        if not idx:
                            continue
                        x = s["x"] + tx * 8 + px
                        y = s["y"] + ty * 8 + py
                        if 0 <= x < SCREEN_W and 0 <= y < SCREEN_H:
                            pixels.append((x, y, pal[s["pal"]][idx], s["pri"]))
    return pixels


def compose(state, hscroll=None, vsram=None) -> list[list[tuple[int, int, int]]]:
    """Full frame: background colour, plane B, plane A, sprites, by priority."""
    if hscroll is None:
        hscroll, _ = scroll_values(state)
    if vsram is None:
        vsram = vsram_values(state)
    regs = state["regs"]
    back = palettes(state)[(regs[7] >> 4) & 3][regs[7] & 0x0F]
    b = render_plane(state, "b", hscroll, vsram)
    a = render_plane(state, "a", hscroll, vsram)
    out = [[back] * SCREEN_W for _ in range(SCREEN_H)]
    for y in range(SCREEN_H):
        for x in range(SCREEN_W):
            if b[y][x] and not b[y][x][1]:
                out[y][x] = b[y][x][0]
            if a[y][x] and not a[y][x][1]:
                out[y][x] = a[y][x][0]
    sprites = render_sprites(state)
    for x, y, colour, pri in sprites:
        if not pri:
            out[y][x] = colour
    for y in range(SCREEN_H):
        for x in range(SCREEN_W):
            if b[y][x] and b[y][x][1]:
                out[y][x] = b[y][x][0]
            if a[y][x] and a[y][x][1]:
                out[y][x] = a[y][x][0]
    for x, y, colour, pri in sprites:
        if pri:
            out[y][x] = colour
    return out


def save_png(pixels, path) -> None:
    import pygame
    pygame.init()
    surf = pygame.Surface((SCREEN_W, SCREEN_H))
    for y in range(SCREEN_H):
        for x in range(SCREEN_W):
            surf.set_at((x, y), pixels[y][x])
    pygame.image.save(surf, str(path))


def diff_pixels(render, ppm_path) -> tuple[int, int]:
    """Count differing pixels between a render and an emulator .ppm capture."""
    from PIL import Image
    im = Image.open(ppm_path).convert("RGB")
    w, h = im.size
    px = im.load()
    differ = 0
    for y in range(min(h, SCREEN_H)):
        for x in range(min(w, SCREEN_W)):
            if tuple(px[x, y]) != tuple(render[y][x]):
                differ += 1
    return differ, w * h
