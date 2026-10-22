"""Stage-2 reconstruction components: verified Streets of Rage engine rules.

Nothing here is a game: these are small, independently testable behavioural
units recovered from the original ROM and validated against it by executing the
original routines on an MC68000 core.

The ``frame`` module composes them in the order the original player loop uses.
"""

from .actor import Actor, BTN_A, BTN_B, BTN_C, BTN_DOWN, BTN_LEFT, BTN_RIGHT, BTN_START, BTN_UP
from .boxes import Box, BoxTables, aabb_overlap, build_player_boxes
from .fixed import hi16, lo16, s16, s32, u32
from .kinematics import (
    GRAVITY_DESCENT_DIRECTIONAL, GRAVITY_NEUTRAL, GRAVITY_SOFT, VY_TERMINAL_PLAYER,
    air_control, clamp_terminal_velocity, directional_gravity, integrate, is_frozen,
    neutral_gravity, soft_gravity,
)
from .projection import project

__all__ = [n for n in dir() if not n.startswith("_")]
__version__ = "0.1.0"
