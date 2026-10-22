"""Minimal actor view needed by the Stage-2 slice.

Only the fields the verified slice actually touches are modelled, with the
original record offsets kept in the field names so evidence stays traceable.
The full 128-byte record is documented in DOSSIER.md §7.1; this is a *slice*
of it, not a replacement for it.

Offset map (all confirmed in Stage 2 unless marked):
  +$00 type id              +$01 flags (bit1 = screen-fixed, bit3 = skip cull)
  +$02 sprite tile width    +$03 sprite tile height
  +$08 animation offset     +$10 X  +$14 Z  +$18 Y   (16.16)
  +$1C vX  +$20 vZ  +$24 vY (16.16)
  +$28 screen X  +$2C screen Y (derived, integer)
  +$30 state (bit0 = facing left)
  +$4B flags (bit1 = invulnerable)   +$54 held buttons   +$59 status flags
"""

from __future__ import annotations

from dataclasses import dataclass, replace

from .fixed import s32, s16


@dataclass
class Actor:
    # --- identity / rendering input
    type_id: int = 0x01          # +$00 (1 = player)
    flags_01: int = 0x00         # +$01
    sprite_w: int = 0            # +$02 (index into the body-box table)
    sprite_h: int = 0            # +$03 (index into the body-box table)
    anim_offset: int = 0         # +$08 (word; low byte is +$09)

    # --- 2.5D world state (16.16)
    x: int = 0                   # +$10
    z: int = 0                   # +$14
    y: int = 0                   # +$18
    vx: int = 0                  # +$1C
    vz: int = 0                  # +$20
    vy: int = 0                  # +$24

    # --- derived screen space (integer pixels)
    screen_x: int = 0            # +$28
    screen_y: int = 0            # +$2C

    # --- control / status
    state: int = 0               # +$30
    flags_4b: int = 0            # +$4B
    buttons: int = 0             # +$54 (held, active-high Genesis pad bits)
    flags_59: int = 0            # +$59

    def __post_init__(self) -> None:
        # Positions/velocities live in 32-bit memory lanes; wrap on construction.
        for name in ("x", "z", "y", "vx", "vz", "vy"):
            setattr(self, name, s32(getattr(self, name)))

    def copy(self, **changes) -> "Actor":
        return replace(self, **changes)

# Genesis pad bit positions (active high), as consumed at +$54 by $0038C0.
BTN_UP, BTN_DOWN, BTN_LEFT, BTN_RIGHT = 0x01, 0x02, 0x04, 0x08
BTN_B, BTN_C, BTN_A, BTN_START = 0x10, 0x20, 0x40, 0x80
