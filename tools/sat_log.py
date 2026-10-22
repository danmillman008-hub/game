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


def sprites(sat_raw: bytes) -> list[dict]:
    """Decode the sprite attribute table following the link chain."""
    out, idx, seen = [], 0, set()
    while idx < 80 and idx not in seen:
        seen.add(idx)
        off = idx * 8
        y, size, attr, x = struct.unpack_from(">HHHH", sat_raw, off)
        if y == 0 and size == 0 and attr == 0 and x == 0:
            break
        out.append({
            "idx": idx,
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
