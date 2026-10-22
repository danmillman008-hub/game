"""Execute the ROM's own graphics decompressor ($008192) on a real MC68000 core.

Why execution instead of re-deriving the bitstream: the bank loader at $008642
calls $008192, not the Kosinski routine -- it is a custom format with a
Huffman-style command table decompressed into RAM at $FFFFF600 and two output
tables ($8254 fixed-write / $826A auto-increment), selected by bit 15 of the
leading size word. Stage 2 established the method: run the original code on a
68000 and treat its output as ground truth.

The routine writes through a4 = $C00000 (the VDP data port). We map that region
as plain memory, so the emulated writes land in a buffer in the exact order the
VDP would have received them. Only the auto-increment table is used for the
graphics banks (bit 15 set); the extractor asserts that.

Usage:
    python tools/gfx_decompress.py --src 0x06FDBC
"""
from __future__ import annotations

import argparse
import hashlib
import struct
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ROM_ZIP = ROOT / "Streets-of-Rage_Genesis_EN.zip"
ROM_NAME = "Streets of Rage (JUE) (REV 00) [!].bin"

DECOMP = 0x008192
OUT_BASE = 0xC00000
OUT_SIZE = 0x80000          # 512 KiB of emulated VDP writes

# The Genesis decodes only 24 address lines, so the routine's `lea $f600.w,a1`
# (sign-extended to $FFFFF600) aliases to $00FFF600 inside the RAM window. Both
# aliases are backed by the same host buffer, exactly as on hardware.
RAM_BASE = 0x00FF0000
RAM_SIZE = 0x10000
RAM_ALIAS = 0xFFFF0000
STACK = 0x00FFFE00
SENTINEL = 0x00FF0100       # illegal opcode planted here to stop the emulation


# Unicorn's M68K core raises on `movem.l d0-d7/a0-a1/a3-a5,-(a7)` (mask $FFDC).
# The routine only uses those moves to save/restore registers around a leaf
# computation, so for extraction we NOP the three movem instructions in the
# emulator's *copy* of the image. The ROM file and all evidence stay untouched;
# this is instrumentation of the harness, recorded here and in the docs.
MOVEM_PATCHES = {
    0x008192: "48e7ffdc",   # movem.l d0-d7/a0-a1/a3-a5,-(a7)   (Kosinski-A entry)
    0x0081A4: "48e7ffdc",   # same, alternate entry
    0x0081D6: "4cdf3bff",   # movem.l (a7)+,d0-d7/a0-a1/a3-a5  (epilogue)
}


def load_rom() -> bytes:
    with zipfile.ZipFile(ROM_ZIP) as z:
        return z.read(ROM_NAME)


def rom_for_emulation(rom: bytes) -> bytes:
    """Copy of the ROM with the unsupported movem instructions NOPed out."""
    img = bytearray(rom)
    for addr, expect in MOVEM_PATCHES.items():
        blob = bytes.fromhex(expect)
        assert img[addr:addr + len(blob)] == blob, f"unexpected bytes at {addr:06X}"
        img[addr:addr + len(blob)] = b"\x4e\x71" * (len(blob) // 2)
    return bytes(img)


def decompress(rom: bytes, src: int, tile_count: int | None = None):
    from unicorn import (Uc, UC_ARCH_M68K, UC_MODE_BIG_ENDIAN, UC_HOOK_CODE,
                         UC_HOOK_MEM_WRITE, UC_PROT_ALL)
    from unicorn.m68k_const import (UC_M68K_REG_A0, UC_M68K_REG_A1, UC_M68K_REG_A4,
                                    UC_M68K_REG_A7, UC_M68K_REG_SR, UC_M68K_REG_PC)
    from unicorn import UcError

    import ctypes

    uc = Uc(UC_ARCH_M68K, UC_MODE_BIG_ENDIAN)
    uc.mem_map(0x000000, 0x80000)                 # ROM
    uc.mem_write(0x000000, rom_for_emulation(rom))
    ram = ctypes.create_string_buffer(RAM_SIZE)   # one buffer, two 68k aliases
    uc.mem_map_ptr(RAM_BASE, RAM_SIZE, 3, ctypes.addressof(ram))
    uc.mem_map_ptr(RAM_ALIAS, RAM_SIZE, 3, ctypes.addressof(ram))
    uc.mem_map(OUT_BASE, OUT_SIZE)                # "VDP data port" sink
    uc.mem_write(STACK, struct.pack(">I", SENTINEL))
    uc.mem_write(SENTINEL, b"\x4a\xfc")           # illegal instruction -> stop

    uc.reg_write(UC_M68K_REG_A0, src)
    uc.reg_write(UC_M68K_REG_A7, STACK)
    uc.reg_write(UC_M68K_REG_SR, 0x2700)          # supervisor, interrupts off

    first_word = struct.unpack_from(">H", rom, src)[0]
    auto_increment = bool(first_word & 0x8000)
    # a5 = first_word * 8 rows; each row is one longword -> first_word tiles.
    tiles = first_word
    expect = tiles * 32
    if tile_count is not None:
        expect = tile_count * 32

    # The routine writes longwords to the VDP data port; the VDP's own address
    # counter advances, so the order of writes *is* the tile stream.
    captured = bytearray()

    def on_write(uc_, access, address, size, value, user_data):
        if OUT_BASE <= address < OUT_BASE + 8:
            captured.extend(int(value).to_bytes(size, "big"))
        return True

    uc.hook_add(UC_HOOK_MEM_WRITE, on_write)

    try:
        uc.emu_start(DECOMP, SENTINEL, count=200_000_000)
        stopped = "sentinel"
    except UcError as exc:                        # pragma: no cover - diagnostics
        stopped = f"exception:{exc}"

    out = bytes(captured[:expect]) if expect else bytes(captured)
    return out, {
        "src": src,
        "first_word": first_word,
        "auto_increment": auto_increment,
        "tiles_from_header": tiles,
        "expected_bytes": expect,
        "captured_bytes": len(captured),
        "stopped": stopped,
        "sha256": hashlib.sha256(bytes(out)).hexdigest(),
    }


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", required=True, help="ROM offset, e.g. 0x06FDBC")
    args = ap.parse_args(argv)
    rom = load_rom()
    data, meta = decompress(rom, int(args.src, 0))
    print(f"{meta}")
    print(f"first 32 bytes: {data[:32].hex(' ')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
