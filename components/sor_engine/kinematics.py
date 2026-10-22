"""Vertical/horizontal kinematics of the original engine (Stage-2 slice).

Every rule below was read out of the ROM and then *executed* on a real MC68000
core for differential validation (see tests/test_differential_rom.py and
DIFFERENTIAL_VALIDATION.md).

Evidence anchors (REV 00):
  $00389A  add.l #$E800 to +$24               neutral gravity
  $0038A6  add.l #$3800 to +$24               soft gravity (throw/arc path)
  $0038AE  sign test: vy<0 -> $389A, else add #$8800
  $003886  if +$24 >= $C0000 then +$24 = $C0000
  $0038C0  air control: +-$6000, clamp |vx| <= $38000, facing side effects
  $00442C  integration X+=vx, Z+=vz, Y+=vy with a state-driven freeze
"""

from __future__ import annotations

from .actor import Actor, BTN_LEFT, BTN_RIGHT
from .fixed import s32

GRAVITY_NEUTRAL = 0x0000E800        # +0.90625 px/tick^2
GRAVITY_DESCENT_DIRECTIONAL = 0x00008800  # +1.0625 px/tick^2
GRAVITY_SOFT = 0x00003800           # +0.21875 px/tick^2
VY_TERMINAL_PLAYER = 0x000C0000     # +12.0 px/tick

AIR_ACCEL = 0x00006000              # 0.375 px/tick^2
AIR_VX_LIMIT = 0x00038000           # 3.5 px/tick

# $00442C freeze predicate: (state & $FC) == $14 && bit7 of +$59
FREEZE_STATE_MASK = 0xFC
FREEZE_STATE_VALUE = 0x14
FREEZE_FLAG_BIT = 0x80


def neutral_gravity(a: Actor) -> Actor:
    """$00389A: always add $E800 (ascent gravity for both jump styles)."""
    a.vy = s32(a.vy + GRAVITY_NEUTRAL)
    return a


def soft_gravity(a: Actor) -> Actor:
    """$0038A6: add $3800 (slower arc used by throw/knockdown paths)."""
    a.vy = s32(a.vy + GRAVITY_SOFT)
    return a


def directional_gravity(a: Actor) -> Actor:
    """$0038AE: vy < 0 keeps ascent gravity, vy >= 0 switches to $8800.

    Note the sign test happens *before* the addition, so the exact tick on which
    vy crosses zero still gets the neutral value.
    """
    if a.vy < 0:
        return neutral_gravity(a)
    a.vy = s32(a.vy + GRAVITY_DESCENT_DIRECTIONAL)
    return a


def clamp_terminal_velocity(a: Actor) -> Actor:
    """$003886: only an upper bound; vy is never clamped downward."""
    if a.vy >= VY_TERMINAL_PLAYER:
        a.vy = VY_TERMINAL_PLAYER
    return a


def air_control(a: Actor) -> bool:
    """$0038C0. Returns True if a direction was held (i.e. the ROM took the branch).

    Order inside the ROM: bit3 (right) is tested first and *skips* the left test,
    so a pad reporting both bits moves right. The facing/anim side effects happen
    before the velocity update, and the clamp only runs on the branch that was
    taken (no input => vx is left completely untouched).
    """
    if a.buttons & BTN_RIGHT:
        a.state &= ~0x01                 # bclr.b #0,+$30  (face right)
        a.anim_offset &= ~0x0002         # bclr.b #1,+$09 (low byte of +$08)
        delta = AIR_ACCEL
    elif a.buttons & BTN_LEFT:
        a.state |= 0x01                  # bset.b #0,+$30  (face left)
        a.anim_offset |= 0x0002          # bset.b #1,+$09
        delta = -AIR_ACCEL
    else:
        return False
    a.vx = s32(a.vx + delta)
    if a.vx < -AIR_VX_LIMIT:
        a.vx = -AIR_VX_LIMIT
    elif a.vx > AIR_VX_LIMIT:
        a.vx = AIR_VX_LIMIT
    return True


def is_frozen(a: Actor) -> bool:
    """NOTE: the predicate reads +$08 (animation-block offset), not the state byte.

    $00442C: ``move.w $8(a0),d0 / andi.b #$fc,d0 / cmpi.w #$14,d0``.
    """
    # ``move.w / andi.b #$fc`` masks the LOW byte only, then ``cmpi.w #$14``
    # compares the whole word -> the high byte must be zero as well.
    return (a.anim_offset & 0xFF00 | a.anim_offset & 0x00FC) == FREEZE_STATE_VALUE and \
        bool(a.flags_59 & FREEZE_FLAG_BIT)


def integrate(a: Actor) -> bool:
    """$00442C. Returns False when the freeze predicate suppressed integration.

    The ROM also executes ``andi.b #$FF,$59`` on the integrating path, which
    changes no bits; it is reproduced as a no-op for documentation purposes.
    """
    if is_frozen(a):
        return False
    a.x = s32(a.x + a.vx)
    a.z = s32(a.z + a.vz)
    a.y = s32(a.y + a.vy)
    return True
