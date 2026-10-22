"""Access per-frame machine state captured by tools/md_capture.

Files written per run:
    ram.bin     - one 64 KB work-RAM image per frame
    vram.bin    - one 64 KB VRAM image per frame
    frames.bin  - per-frame VDP registers / VSRAM / CRAM / GX sprite array
"""
from __future__ import annotations

import struct
from pathlib import Path

RAM = 0x10000
VRAM = 0x10000


def ram_at(path, frame: int) -> bytes:
    with open(path, "rb") as f:
        f.seek(frame * RAM)
        return f.read(RAM)


def vram_at(path, frame: int) -> bytes:
    with open(path, "rb") as f:
        f.seek(frame * VRAM)
        return f.read(VRAM)


def word(ram: bytes, addr: int) -> int:
    return struct.unpack_from(">H", ram, addr & 0xFFFF)[0]


def long(ram: bytes, addr: int) -> int:
    return struct.unpack_from(">I", ram, addr & 0xFFFF)[0]


def sat_from_vram(vram: bytes, regs: list[int]) -> list[dict]:
    """Decode the sprite attribute table from a raw VRAM image."""
    base = (regs[5] & 0x7F) << 9
    out, idx, seen = [], 0, set()
    while idx < 80 and idx not in seen:
        seen.add(idx)
        off = base + idx * 8
        y, size, attr, x = struct.unpack_from(">HHHH", vram, off)
        if y == 0 and size == 0 and attr == 0 and x == 0:
            break
        out.append({
            "idx": idx, "x": (x & 0x1FF) - 0x80, "y": (y & 0x3FF) - 0x80,
            "w": ((size >> 10) & 3) + 1, "h": ((size >> 8) & 3) + 1,
            "tile": attr & 0x7FF, "pal": (attr >> 13) & 3,
            "vflip": bool(attr & 0x1000), "hflip": bool(attr & 0x0800),
            "link": (size >> 12) & 0xF,
        })
        idx = (size >> 12) & 0xF
    return out
