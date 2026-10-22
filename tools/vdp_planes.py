"""Render Mega Drive background planes from a captured machine state.

Deliberately small and explicit: this is the reference for the JavaScript
renderer in reconstruction/stage1/, and both are checked against frames the
original game produced.

Layout facts used (all observable in a capture, none assumed from the game):
  * VRAM in a `.vram`/`vram.bin` dump is stored as host little-endian words, so
    it must be byte-swapped per word to get address order.
  * nametable cell: bit15 priority, bits14-13 palette, bit12 vflip, bit11 hflip,
    bits10-0 tile index.
  * a plane pixel at world (wx, wy) shows cell (wx>>3, wy>>3).
"""
from __future__ import annotations

import struct

PLANE_SIZES = {0: (32, 32), 1: (64, 32), 2: (32, 64), 3: (64, 64)}


def byteswapped(vram: bytes) -> bytes:
    out = bytearray(len(vram))
    out[0::2] = vram[1::2]
    out[1::2] = vram[0::2]
    return bytes(out)


def cram_to_rgb(words_le: bytes) -> list[tuple[int, int, int]]:
    out = []
    for i in range(0x40):
        w = struct.unpack_from("<H", words_le, i * 2)[0]
        out.append((((w >> 1) & 7) * 255 // 7, ((w >> 5) & 7) * 255 // 7,
                    ((w >> 9) & 7) * 255 // 7))
    return out


def palettes(cram_le: bytes) -> list[list[tuple[int, int, int]]]:
    """Four 16-colour palettes, as the VDP presents them."""
    flat = cram_to_rgb(cram_le)
    return [flat[i * 16:(i + 1) * 16] for i in range(4)]


def tile_rgba(vram: bytes, pal, index: int, transparent: bool = False):
    """8x8 RGB rows for a 4bpp tile, or None rows where colour 0 is transparent."""
    rows = []
    base = index * 32
    for y in range(8):
        o = base + y * 4
        p0, p1, p2, p3 = vram[o], vram[o + 1], vram[o + 2], vram[o + 3]
        row = []
        for x in range(8):
            b = 7 - x
            c = ((p0 >> b) & 1) | (((p1 >> b) & 1) << 1) | \
                (((p2 >> b) & 1) << 2) | (((p3 >> b) & 1) << 3)
            if transparent and c == 0:
                row.append(None)
            else:
                row.append(pal[c])
        rows.append(row)
    return rows


def render_plane(vram: bytes, pals, base: int, plane: int, hscroll: int,
                 vscroll: int = 0, width: int = 320, height: int = 224,
                 transparent: bool = True):
    pw, ph = PLANE_SIZES[plane]
    img = [[None] * width for _ in range(height)]
    cache = {}
    for sy in range(height):
        wy = (sy + vscroll) & (ph * 8 - 1)
        cy = wy >> 3
        ty = wy & 7
        for sx in range(width):
            wx = (sx + hscroll) & (pw * 8 - 1)
            cx = wx >> 3
            wr = cy * pw + cx
            if wr >= (len(vram) - base) // 2:
                continue                      # runs off the end of VRAM: leave blank
            cell = struct.unpack_from(">H", vram, base + wr * 2)[0]
            tile = cell & 0x7FF
            key = (tile, (cell >> 13) & 3, bool(cell & 0x1000), bool(cell & 0x0800))
            rows = cache.get(key)
            if rows is None:
                px = cell & 0x800
                cx0 = wx & 7
                vy = 7 - ty if cell & 0x1000 else ty
                trows = tile_rgba(vram, pals[(cell >> 13) & 3], tile, transparent)
                rows = cache[key] = trows
            tx = wx & 7
            if cell & 0x0800:
                tx = 7 - tx
            r = rows[7 - ty if cell & 0x1000 else ty]
            img[sy][sx] = (r[tx], cell, (wx, wy))
    return img


def overlay(dst, src, priority_filter=None):
    """Merge src over dst where src has a pixel (plane composition)."""
    h = len(dst)
    w = len(dst[0])
    for y in range(h):
        row, srow = dst[y], src[y]
        for x in range(w):
            s = srow[x]
            if s is None:
                continue
            if s[0] is None:
                continue
            row[x] = s
    return dst


def gx_pixel_565(r3: int, g3: int, b3: int) -> int:
    """Genesis Plus GX's 16-bit output value for a 3-bit-per-channel colour.

    From core/vdp_render.c: pixel_lut[0][i] = MAKE_PIXEL(r,g,b) with the
    USE_16BPP_RENDERING form, i.e. 5:6:5.
    """
    def mp(r, g, b):
        return ((r << 12) | ((r >> 3) << 11) | (g << 7) | ((g >> 2) << 5) |
                (b << 1) | (b >> 3))
    return mp(r3, g3, b3) & 0xFFFF


def gx_rgb(r3: int, g3: int, b3: int) -> tuple[int, int, int]:
    """The 8-bit RGB a reference capture shows for a 3-bit CRAM colour.

    This mirrors tools/md_capture/frontend.c, which expands the emulator's 5:6:5
    framebuffer with r*255/31, g*255/63, b*255/31. Comparing CRAM colours to a
    capture without this step is an apples-to-oranges test.
    """
    c = gx_pixel_565(r3, g3, b3)
    r = (c >> 11) & 0x1F
    g = (c >> 5) & 0x3F
    b = c & 0x1F
    return (r * 255 // 31, g * 255 // 63, b * 255 // 31)


def cram_words(cram_bytes: bytes) -> list[int]:
    """CRAM as the VDP holds it: 9-bit BBBGGGRRR, from a little-endian dump."""
    return [struct.unpack_from("<H", cram_bytes, i * 2)[0] & 0x1FF for i in range(0x40)]


def cram_palettes_rgb(cram_bytes: bytes) -> list[list[tuple[int, int, int]]]:
    """Four 16-colour palettes in the exact 8-bit RGB a capture would contain."""
    words = cram_words(cram_bytes)
    return [[gx_rgb(w & 7, (w >> 3) & 7, (w >> 6) & 7) for w in words[p * 16:(p + 1) * 16]]
            for p in range(4)]
