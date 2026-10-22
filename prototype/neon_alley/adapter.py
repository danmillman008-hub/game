"""Thin adapter between the game and the validated reconstruction components.

Every function here is a pass-through (plus bookkeeping). No physics is
re-implemented: the game calls these wrappers, and these wrappers call
`components.sor_engine`. `STATS` counts the calls so tests can prove that the
game's real update path exercises the verified code.

The modules are imported as modules (not individual names) so tests can
monkey-patch them and prove the call path is live.
"""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from components.sor_engine import (  # noqa: E402
    Actor, BTN_LEFT, BTN_RIGHT, Box, BoxTables,
    kinematics as _kin, boxes as _boxes, projection as _proj, fixed as _fixed,
)

STATS = {
    "gravity": 0, "clamp": 0, "air_control": 0, "integrate": 0,
    "build_boxes": 0, "aabb": 0, "project": 0,
}

_TABLES: BoxTables | None = None


def tables() -> BoxTables:
    global _TABLES
    if _TABLES is None:
        _TABLES = BoxTables.load(ROOT / "components" / "data" / "body_boxes.json")
    return _TABLES


def reset_stats() -> None:
    for k in STATS:
        STATS[k] = 0


# ---------------------------------------------------------------- kinematics
def gravity(actor: Actor, mode: str = "directional") -> None:
    """[ROM] $00389A / $0038AE. `mode` selects the measured jump chain."""
    STATS["gravity"] += 1
    if mode == "neutral":
        _kin.neutral_gravity(actor)
    elif mode == "soft":
        _kin.soft_gravity(actor)
    else:
        _kin.directional_gravity(actor)


def clamp_terminal(actor: Actor) -> None:
    """[ROM] $003886 — one-sided terminal velocity."""
    STATS["clamp"] += 1
    _kin.clamp_terminal_velocity(actor)


def air_control(actor: Actor) -> bool:
    """[ROM] $0038C0 — acceleration, clamp, facing side effects."""
    STATS["air_control"] += 1
    return _kin.air_control(actor)


def integrate(actor: Actor) -> bool:
    """[ROM] $00442C — three-axis integration with the freeze predicate."""
    STATS["integrate"] += 1
    return _kin.integrate(actor)


def is_frozen(actor: Actor) -> bool:
    return _kin.is_frozen(actor)


# ---------------------------------------------------------------- geometry
def body_boxes(actor: Actor, at_p1_base: bool = False):
    """[ROM] $004140 — two ROM-table AABBs (primary +$64, secondary +$70)."""
    STATS["build_boxes"] += 1
    return _boxes.build_player_boxes(actor, tables(), at_p1_base=at_p1_base)


def overlap(a: Box, b: Box) -> bool:
    """[ROM] $00450C predicate (inclusive, Z/X/Y)."""
    STATS["aabb"] += 1
    return _boxes.aabb_overlap(a, b)


def project(actor: Actor, cam_x: int, cam_y: int, police_active: bool = False):
    """[ROM] $00AF46 — world→screen + engine cull window."""
    STATS["project"] += 1
    return _proj.project(actor, cam_x, cam_y, police_active)


# ---------------------------------------------------------------- fixed point
def hi16(v: int) -> int:
    return _fixed.hi16(v)


def s32(v: int) -> int:
    return _fixed.s32(v)


def px(v: float) -> int:
    return _fixed.px(v)


def facing_from_state(actor: Actor) -> int:
    """[ROM] air control writes facing into bit0 of +$30 (1 = left)."""
    return -1 if (actor.state & 0x01) else 1


__all__ = [
    "Actor", "BTN_LEFT", "BTN_RIGHT", "Box",
    "STATS", "reset_stats", "tables",
    "gravity", "clamp_terminal", "air_control", "integrate", "is_frozen",
    "body_boxes", "overlap", "project", "hi16", "s32", "px", "facing_from_state",
]
