#!/usr/bin/env python3
"""
ROM-execution probe: runs individual Streets of Rage (REV 00) M68000 subroutines
under Unicorn with a synthetic actor record, returning exact register/memory state.

This is a *reference oracle* for differential testing of the reconstructed
components. It executes the original ROM bytes; it does not emulate the VDP/Z80,
so only self-contained CPU routines can be probed (documented in REPRODUCE.md).

Usage (library):
    vm = RomProbe()
    vm.write_u32(ACTOR+0x24, 0xFFF90000)
    vm.call(0x389A)
    vm.read_u32(ACTOR+0x24)
"""
from __future__ import annotations

import struct
import zipfile
from pathlib import Path

ROM_NAME = "Streets of Rage (JUE) (REV 00) [!].bin"
ZIP_PATH = Path(__file__).resolve().parent.parent / "Streets-of-Rage_Genesis_EN.zip"

SENTINEL = 0x00FFFD00
STACK = 0x00FFFE00
ACTOR = 0x00FFB900          # general-actor slot 1 (RAM alias used by the game)
ACTOR2 = 0x00FFB980         # slot 2, used for player-vs-player box probes


class RomProbe:
    def __init__(self, rom_name: str = ROM_NAME):
        from unicorn import Uc, UC_ARCH_M68K, UC_MODE_BIG_ENDIAN
        from unicorn.m68k_const import UC_CPU_M68K_M68000

        self._u = Uc(UC_ARCH_M68K, UC_MODE_BIG_ENDIAN)
        self._u.ctl_set_cpu_model(UC_CPU_M68K_M68000)
        with zipfile.ZipFile(ZIP_PATH) as zf:
            self.rom = zf.read(rom_name)
        self._u.mem_map(0x000000, 0x080000)
        self._u.mem_write(0x000000, self.rom)
        # The M68000 sign-extends 16-bit absolute addresses ($B800 -> $FFFFB800)
        # while 32-bit absolute operands use $00FFxxxx. Unicorn has no address
        # aliasing, so both windows are mapped onto ONE host buffer.
        import ctypes
        self._ram = ctypes.create_string_buffer(0x10000)
        self._ram_base = ctypes.addressof(self._ram)
        self._u.mem_map_ptr(0xFFFF0000, 0x10000, 3, self._ram_base)
        self._u.mem_map_ptr(0x00FF0000, 0x10000, 3, self._ram_base)
        self.reset()

    # ---- basic state -------------------------------------------------
    def reset(self) -> None:
        from unicorn.m68k_const import UC_M68K_REG_SR, UC_M68K_REG_A7
        self._u.reg_write(UC_M68K_REG_SR, 0x2700)      # supervisor, IRQ masked
        self._u.reg_write(UC_M68K_REG_A7, STACK)
        self._u.mem_write(STACK, struct.pack(">I", SENTINEL))
        self._u.mem_write(0xFFFF0000, b"\x00" * 0x10000)

    def reg(self, name: str) -> int:
        import unicorn.m68k_const as mc
        return self._u.reg_read(getattr(mc, f"UC_M68K_REG_{name.upper()}"))

    def set_reg(self, name: str, value: int) -> None:
        import unicorn.m68k_const as mc
        self._u.reg_write(getattr(mc, f"UC_M68K_REG_{name.upper()}"), value)

    # ---- memory ------------------------------------------------------
    def read(self, addr: int, n: int) -> bytes:
        return bytes(self._u.mem_read(addr, n))

    def write(self, addr: int, data: bytes) -> None:
        self._u.mem_write(addr, data)

    def read_u8(self, a):  return self.read(a, 1)[0]
    def read_u16(self, a): return struct.unpack(">H", self.read(a, 2))[0]
    def read_u32(self, a): return struct.unpack(">I", self.read(a, 4))[0]
    def write_u8(self, a, v):  self.write(a, struct.pack(">B", v & 0xFF))
    def write_u16(self, a, v): self.write(a, struct.pack(">H", v & 0xFFFF))
    def write_u32(self, a, v): self.write(a, struct.pack(">I", v & 0xFFFFFFFF))

    def clear_actor(self, addr: int = ACTOR) -> None:
        self.write(addr, b"\x00" * 128)

    # ---- execution ---------------------------------------------------
    def call(self, entry: int, stop: int | list[int] | None = None,
             max_instr: int = 4000, trace: list | None = None) -> int:
        """Run from `entry` until rts (sentinel) or any address in `stop`.
        Returns the stopping PC. Fills `trace` with every executed PC if given."""
        from unicorn import UC_HOOK_CODE

        stops = set()
        if stop is not None:
            stops = {stop} if isinstance(stop, int) else set(stop)

        def hook(uc, addr, size, _):
            if trace is not None:
                trace.append(addr)
            if addr in stops:
                uc.emu_stop()

        h = self._u.hook_add(UC_HOOK_CODE, hook)
        # re-arm the return sentinel
        self.write_u32(STACK, SENTINEL)
        self.set_reg("a7", STACK)
        self._u.emu_start(entry, SENTINEL, count=max_instr)
        self._u.hook_del(h)
        return self.reg("pc")


if __name__ == "__main__":
    vm = RomProbe()
    vm.clear_actor()
    vm.write_u32(ACTOR + 0x24, 0xFFF90000)
    vm.call(0x389A)
    print(f"after $00389A: vy = 0x{vm.read_u32(ACTOR+0x24):08X}")
