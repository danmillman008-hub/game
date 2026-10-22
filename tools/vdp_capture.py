"""Reconstruct VRAM / CRAM state from VDP write logs produced by the emulator.

The capture is a per-frame diff log written by `tools/md_capture/` (a headless
Genesis Plus GX frontend). Record layout: u32 (frame<<16 | word_address), u16 value.

This is ground truth: it is what the real game actually put in VRAM on a real
Mega Drive, so it can be used to validate or correct the static decompressor.
"""
from __future__ import annotations

import struct
from collections import defaultdict
from pathlib import Path


def read_log(path: str | Path, frames_hint: int = 100000) -> list[tuple[int, int, int]]:
    """Read a capture log. The frontend writes native-endian; auto-detect it."""
    raw = Path(path).read_bytes()
    for endian in ("<", ">"):
        recs = []
        ok = True
        for i in range(0, len(raw) - 5, 6):
            n, v = struct.unpack_from(endian + "IH", raw, i)
            fr, addr = n >> 16, n & 0xFFFF
            if fr >= frames_hint:
                ok = False
                break
            recs.append((fr, addr, v))
        if ok and recs and all(recs[i][0] <= recs[i + 1][0] for i in range(len(recs) - 1)):
            return recs
    raise ValueError(f"{path}: unreadable capture log")


def state_at(records, frame: int, size_words: int = 0x8000, base: int = 0) -> list[int]:
    """Word-addressed memory image as of `frame` (inclusive)."""
    mem = [0] * size_words
    for fr, addr, val in records:
        if fr > frame:
            break
        if 0 <= addr - base < size_words:
            mem[addr - base] = val
    return mem


def uploads(records, min_run: int = 64) -> list[dict]:
    """Group per-frame writes into contiguous address runs = one upload event."""
    per_frame: dict[int, list[tuple[int, int]]] = defaultdict(list)
    for fr, addr, val in records:
        per_frame[fr].append((addr, val))
    events = []
    for fr in sorted(per_frame):
        writes = sorted(per_frame[fr])
        run: list[tuple[int, int]] = []
        for addr, val in writes:
            if run and addr != run[-1][0] + 1:
                if len(run) >= min_run:
                    events.append({"frame": fr, "start": run[0][0], "words": len(run),
                                   "data": [v for _, v in run]})
                run = []
            run.append((addr, val))
        if len(run) >= min_run:
            events.append({"frame": fr, "start": run[0][0], "words": len(run),
                           "data": [v for _, v in run]})
    return events


def to_bytes(words) -> bytes:
    return b"".join(struct.pack(">H", w & 0xFFFF) for w in words)
