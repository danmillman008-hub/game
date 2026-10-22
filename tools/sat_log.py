"""Read the per-frame state log written by tools/md_capture (frames.bin).

Record layout, one per emulated frame:
    u32 frame
    u8[640]  sprite attribute table (80 entries x 8 bytes, VRAM byte order)
    u8[26]   VDP registers 0-23, then the 16-bit status word
    u8[80]   40 vertical-scroll words (big-endian)
    u8[128]  CRAM (64 words, host/little-endian)
"""
from __future__ import annotations

import struct
from pathlib import Path

SAT_BYTES = 640
RECORD = 4 + SAT_BYTES + 26 + 80 + 128


def read_frames(path) -> list[dict]:
    raw = Path(path).read_bytes()
    out = []
    for off in range(0, len(raw) - RECORD + 1, RECORD):
        frame = struct.unpack_from(">I", raw, off)[0]
        sat_raw = raw[off + 4: off + 4 + SAT_BYTES]
        regs = list(raw[off + 4 + SAT_BYTES: off + 4 + SAT_BYTES + 24])
        status = struct.unpack_from(">H", raw, off + 4 + SAT_BYTES + 24)[0]
        vs = [struct.unpack_from(">H", raw, off + 4 + SAT_BYTES + 26 + i * 2)[0]
              for i in range(40)]
        cram = [struct.unpack_from("<H", raw, off + 4 + SAT_BYTES + 26 + 80 + i * 2)[0]
                for i in range(64)]
        out.append({"frame": frame, "sat": sat_raw, "regs": regs, "status": status,
                    "vsram": vs, "cram": cram})
    return out


def entries(sat_raw: bytes) -> list[dict]:
    """Decode all 80 sprite entries of the SAT cache.

    The 640 bytes are Genesis Plus GX's internal SAT cache (`sat[]`), which is a
    host-order (little-endian) copy of VRAM's sprite attribute table, 4 words per
    entry. Field positions are taken from the emulator's own parser in
    core/vdp_render.c (`parse_satb_m5_im2`):

        w0: bits 0-8  = y position
        w1: bits 0-6  = link (index of next sprite), bits 8-11 = size
             (bits 8-9 = height, bits 10-11 = width, both minus 1)
        w2: tile | palette | flips | priority
        w3: bits 0-8  = x position
    """
    words = struct.unpack_from("<320H", sat_raw, 0)
    out = []
    for idx in range(80):
        y, size, attr, x = words[idx * 4: idx * 4 + 4]
        out.append({
            "idx": idx,
            "y": y & 0x1FF,
            "x": x & 0x1FF,
            "h": ((size >> 8) & 3) + 1,
            "w": ((size >> 10) & 3) + 1,
            "link": size & 0x7F,
            "tile": attr & 0x7FF,
            "pal": (attr >> 13) & 3,
            "pri": bool(attr & 0x8000),
            "vflip": bool(attr & 0x1000),
            "hflip": bool(attr & 0x0800),
        })
    return out


def sprites(sat_raw: bytes, blank_y: int = 0x1FF) -> list[dict]:
    """Visible sprites, following the link chain from entry 0.

    A sprite is skipped when its y is off-screen (the usual way the game empties
    an entry), and the chain stops at link 0 or beyond the table.
    """
    all_entries = entries(sat_raw)
    out, idx, seen = [], 0, set()
    while idx < 80 and idx not in seen:
        seen.add(idx)
        e = all_entries[idx]
        if e["y"] != blank_y:
            out.append(e)
        idx = e["link"]
    return out
