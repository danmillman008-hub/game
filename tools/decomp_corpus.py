"""Read decompression captures produced by the headless emulator harness.

Record layout (little-endian, written by tools/md_capture/raw/vdphook.c):
    u32 frame, u32 source_address, u32 destination_vram, u32 length,
    then `length` output bytes
"""
from __future__ import annotations

import struct
from pathlib import Path


def read_corpus(path) -> list[dict]:
    raw = Path(path).read_bytes()
    out = []
    pos = 0
    while pos + 16 <= len(raw):
        frame, src, dest, ln = struct.unpack_from("<IIII", raw, pos)
        pos += 16
        if pos + ln > len(raw):
            break
        out.append({"frame": frame, "src": src, "dest": dest, "length": ln,
                    "data": raw[pos:pos + ln]})
        pos += ln
    return out
