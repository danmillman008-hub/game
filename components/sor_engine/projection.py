"""World -> screen projection and sprite culling ($00AF46-$00AFC2).

    sx = X_hi + $80 - cam_x
    sy = (Z_hi >> 1) + Y_hi + $80 - cam_y

`>>1` is an arithmetic shift on the 16-bit depth word: one pixel of depth is
half a pixel of screen rise, and negative depths round downward.

Two documented exceptions, both in the original code:
  * bit1 of +$01 set -> actor is not camera-relative (screen-fixed), so the
    camera offsets are not subtracted (culling still applies);
  * culling is skipped entirely when bit3 of +$01 is set or when the
    police-special latch $FA1A is non-zero. Type $05 keeps the *wide* left
    margin while still being culled.
"""

from __future__ import annotations

from .actor import Actor
from .fixed import hi16, s16

SCREEN_BIAS = 0x80
CULL_LEFT_WIDE = 0xFF80      # -128
CULL_LEFT_NARROW = 0xFC80    # -896
CULL_RIGHT = 0x500           # 1280: sx >= this culls
CULL_TOP = 0x10              # sy < 16 culls   (unsigned)
CULL_BOTTOM = 0x200          # sy >= 512 culls (unsigned)


def project(a: Actor, cam_x: int, cam_y: int, police_active: bool = False) -> tuple[int, int, bool]:
    """Return (screen_x, screen_y, culled); both coordinates are 16-bit words."""
    sx = s16(hi16(a.x) + SCREEN_BIAS)
    sy = s16((hi16(a.z) >> 1) + hi16(a.y) + SCREEN_BIAS)
    if not (a.flags_01 & 0x02):
        sx = s16(sx - cam_x)
        sy = s16(sy - cam_y)

    if a.type_id == 0x05:
        # $00AF8A jumps straight to the bounds test: type $05 is ALWAYS culled,
        # with the wide left margin, regardless of bit3 / $FA1A.
        margin = CULL_LEFT_WIDE
    elif (a.flags_01 & 0x08) or police_active:
        return sx, sy, False
    else:
        margin = CULL_LEFT_NARROW
    culled = (
        sx >= CULL_RIGHT
        or sx < s16(margin)
        or (sy & 0xFFFF) >= CULL_BOTTOM
        or (sy & 0xFFFF) < CULL_TOP
    )
    return sx, sy, culled
