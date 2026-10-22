#!/usr/bin/env python3
"""Stage-2 vertical slice: a frame-stepped reconstruction of the player's
2.5D kinematics + body-box geometry, driven only by the reusable component.

This is NOT a game and does not implement gameplay. It reproduces one bounded
layer of engine behaviour, in the documented per-frame order, so that its output
can be compared frame-by-frame with the original ROM routines.

Per-frame order (evidence: $001C44 player skeleton; $001FDC/$002006 state
handlers; $003886; $00442C; $004140; $00AF46):

    1. state-handler physics   (gravity variant; optional air control)
    2. terminal-velocity clamp
    3. position integration    (with the +$08/+$59 freeze predicate)
    4. body-box rebuild        (two AABBs, +$64 and +$70)
    5. sprite projection       (+$28/+$2C and cull decision)

Usage:
    python3 reconstruction/slice_runner.py scenarios/neutral_jump.json
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from components.sor_engine import (  # noqa: E402
    Actor, BoxTables, air_control, build_player_boxes, clamp_terminal_velocity,
    directional_gravity, integrate, neutral_gravity, project, soft_gravity,
)

GRAVITY = {
    "neutral": neutral_gravity,
    "directional": directional_gravity,
    "soft": soft_gravity,
}

_TABLES: BoxTables | None = None


def tables() -> BoxTables:
    global _TABLES
    if _TABLES is None:
        _TABLES = BoxTables.load()
    return _TABLES


def actor_from_dict(d: dict) -> Actor:
    return Actor(**{k: v for k, v in d.items() if k in Actor.__dataclass_fields__})


def step(a: Actor, plan: dict, t: BoxTables) -> dict:
    """Advance exactly one original-frame worth of the sliced behaviour."""
    a.buttons = plan.get("buttons", a.buttons)   # +$54 held-state byte
    gravity = GRAVITY[plan.get("gravity", "neutral")]
    gravity(a)                                  # 1. state-handler physics
    if plan.get("air_control"):
        air_control(a)
    clamp_terminal_velocity(a)                  # 2. $003886
    integrated = integrate(a)                   # 3. $00442C
    primary, secondary = build_player_boxes(   # 4. $004140
        a, t, at_p1_base=plan.get("at_p1_base", False))
    sx, sy, culled = project(                   # 5. $00AF46
        a, plan.get("cam_x", 0), plan.get("cam_y", 0), plan.get("police", False))
    if not culled:
        a.screen_x, a.screen_y = sx, sy
    return {
        "x": a.x, "z": a.z, "y": a.y,
        "vx": a.vx, "vz": a.vz, "vy": a.vy,
        "sx": a.screen_x, "sy": a.screen_y, "culled": culled,
        "box_primary": primary.as_tuple(),
        "box_secondary": secondary.as_tuple(),
        "state": a.state, "anim_offset": a.anim_offset,
        "integrated": integrated,
    }


def run_scenario(scenario: dict) -> list[dict]:
    a = actor_from_dict(scenario["initial"])
    t = tables()
    trace = []
    for f in range(scenario.get("frames", 60)):
        plan = dict(scenario)
        plan["buttons"] = scenario.get("buttons_by_frame", {}).get(str(f), scenario.get("buttons", 0))
        snap = step(a, plan, t)
        snap["frame"] = f
        trace.append(snap)
    return trace


def main() -> None:
    if len(sys.argv) < 2:
        print(__doc__)
        return
    scenario = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    for snap in run_scenario(scenario):
        print(f"{snap['frame']:3d} x={snap['x']:>11} y={snap['y']:>11} vy={snap['vy']:>11} "
              f"sx={snap['sx']:>5} sy={snap['sy']:>5} box={snap['box_primary']}")


if __name__ == "__main__":
    main()
