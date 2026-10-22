"""16.16 fixed-point helpers matching M68000 32-bit two's-complement semantics.

The original engine integrates positions and velocities as signed 32-bit 16.16
values (add.l / sub.l). Every operation here therefore wraps at 32 bits, exactly
like the hardware. Consumers read whole pixels with :func:`hi16`, which mirrors
the ROM's pervasive ``move.w $10(a0),d0`` idiom (high word only).
"""

from __future__ import annotations

MASK32 = 0xFFFFFFFF
ONE = 0x10000


def s32(value: int) -> int:
    """Wrap to signed 32-bit, as ``add.l``/``sub.l`` do."""
    value &= MASK32
    return value - 0x100000000 if value & 0x80000000 else value


def u32(value: int) -> int:
    return value & MASK32


def hi16(value: int) -> int:
    """Signed high word of a 16.16 value (the engine's 'whole pixels' read)."""
    word = (value >> 16) & 0xFFFF
    return word - 0x10000 if word & 0x8000 else word


def lo16(value: int) -> int:
    return value & 0xFFFF


def s16(value: int) -> int:
    word = value & 0xFFFF
    return word - 0x10000 if word & 0x8000 else word


def px(value: float) -> int:
    """Convenience for building 16.16 constants in tests/scenarios."""
    return s32(int(round(value * ONE)))
