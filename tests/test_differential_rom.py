"""Independent differential tests: reconstructed component vs ORIGINAL ROM code.

Each test builds randomized but reproducible inputs (fixed seed), runs the real
M68000 routine under Unicorn, runs the pure-Python component, and demands exact
equality. Unicorn is optional: the module is skipped when it is unavailable.

Run:  python3 -m unittest tests.test_differential_rom -v
Seed: 20261022 (identical on every run).
"""
from __future__ import annotations

import collections
import importlib.util
import random
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "tests"))

from components.sor_engine import (  # noqa: E402
    Actor, BoxTables, air_control, clamp_terminal_velocity, directional_gravity,
    integrate, neutral_gravity, project, soft_gravity,
)
from components.sor_engine.boxes import Box, aabb_overlap, build_player_boxes  # noqa: E402
from components.sor_engine.fixed import s16, s32, u32  # noqa: E402

# Counted so the verification tool can report evidence volume, not just "PASS".
COMPARISONS: "collections.Counter[str]" = collections.Counter()

HAS_UNICORN = importlib.util.find_spec("unicorn") is not None

SEED = 20261022
FRAME_SCENARIOS = [
    ("neutral_jump", 40, dict(gravity="neutral", air_control=False, buttons=0, cam_x=0, cam_y=0),
     dict(x=983040, z=524288, y=0, vx=0, vz=0, vy=-491520, sprite_w=4, sprite_h=2)),
    ("directional_jump_left", 40, dict(gravity="directional", air_control=True, buttons=0x04, cam_x=96, cam_y=0),
     dict(x=983040, z=524288, y=0, vx=-196608, vz=0, vy=-557056, sprite_w=4, sprite_h=2)),
    ("launched_descent", 50, dict(gravity="directional", air_control=False, buttons=0, cam_x=0, cam_y=0),
     dict(x=900000, z=460000, y=-1310720, vx=32768, vz=-16384, vy=65536, sprite_w=4, sprite_h=2)),
    ("frozen_hold", 10, dict(gravity="neutral", air_control=True, buttons=0x08, cam_x=0, cam_y=0),
     dict(x=983040, z=524288, y=-65536, vx=12345, vz=-6789, vy=50000,
          state=0x14, flags_59=0x80, sprite_w=4, sprite_h=2)),
]

try:
    from rom_oracle import Oracle
    _IMPORT_ERROR = None
except Exception as exc:  # pragma: no cover - environment dependent
    Oracle = None
    _IMPORT_ERROR = exc


@unittest.skipUnless(HAS_UNICORN and Oracle is not None, "unicorn not installed: ROM oracle unavailable")
class DifferentialROM(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.o = Oracle()
        cls.tables = BoxTables.load()

    # ---- D1 gravity --------------------------------------------------
    def test_D1_gravity(self):
        rng = random.Random(SEED + 1)
        for kind, fn in (("neutral", neutral_gravity), ("soft", soft_gravity),
                         ("directional", directional_gravity)):
            for _ in range(300):
                COMPARISONS["D1_gravity"] += 1
                vy = rng.randrange(-0x40000, 0x140000)
                a = Actor(vy=vy)
                fn(a)
                self.assertEqual(u32(a.vy), self.o.gravity(kind, vy),
                                 f"{kind} vy=0x{vy:08X}")

    # ---- D2 terminal clamp -------------------------------------------
    def test_D2_terminal_clamp(self):
        cases = [0, 1, -1, 0xBFFFF, 0xC0000, 0xC0001, 0xFFFFFF, 0x80000000]
        rng = random.Random(SEED + 2)
        cases += [rng.randrange(-0x100000, 0x200000) for _ in range(200)]
        for vy in cases:
            COMPARISONS["D2_clamp"] += 1
            a = Actor(vy=vy)
            clamp_terminal_velocity(a)
            self.assertEqual(u32(a.vy), self.o.clamp(vy), f"vy=0x{vy:08X}")

    # ---- D3 air control ---------------------------------------------
    def test_D3_air_control(self):
        rng = random.Random(SEED + 3)
        for _ in range(400):
            COMPARISONS["D3_air_control"] += 1
            buttons = rng.randrange(0, 16)          # low nibble: U/D/L/R
            vx = rng.randrange(-0x60000, 0x60000)
            state = rng.randrange(0, 256)
            anim = rng.randrange(0, 0x10000)
            a = Actor(buttons=buttons, vx=vx, state=state, anim_offset=anim)
            taken = air_control(a)
            ovx, ostate, oanim = self.o.air_control(buttons, vx, state, anim)
            self.assertEqual(u32(a.vx), ovx, f"vx buttons={buttons}")
            self.assertEqual(a.state & 0xFF, ostate, f"state buttons={buttons}")
            self.assertEqual(a.anim_offset, oanim, f"anim buttons={buttons}")
            self.assertEqual(taken, bool(buttons & 0x0C), "branch-taken flag")

    # ---- D4 integration / freeze ------------------------------------
    def test_D4_integration(self):
        rng = random.Random(SEED + 4)
        cases = [(0, 0), (0x14, 0x80), (0x14, 0x00), (0x15, 0x80), (0x15, 0x00),
                 (0x16, 0x80), (0x10, 0x80), (0x14, 0xFF), (0x14, 0x7F)]
        cases += [(rng.randrange(0, 0x120), rng.randrange(0, 256)) for _ in range(400)]
        for state, f59 in cases:   # `state` here is +$08 (the freeze predicate's input)
            COMPARISONS["D4_integration"] += 1
            vals = [rng.randrange(-0x2000000, 0x2000000) for _ in range(6)]
            a = Actor(x=vals[0], z=vals[1], y=vals[2], vx=vals[3], vz=vals[4],
                      vy=vals[5], anim_offset=state, flags_59=f59)
            integrated = integrate(a)
            ox, oz, oy = self.o.integrate(*vals, state, f59)
            self.assertEqual(u32(a.x), ox, f"x state={state:#x} f59={f59:#x}")
            self.assertEqual(u32(a.z), oz, f"z state={state:#x} f59={f59:#x}")
            self.assertEqual(u32(a.y), oy, f"y state={state:#x} f59={f59:#x}")
            frozen = ((state & 0xFF00) | (state & 0x00FC)) == 0x14 and bool(f59 & 0x80)
            self.assertEqual(integrated, not frozen)

    # ---- D5 body boxes ----------------------------------------------
    def test_D5_body_boxes(self):
        rng = random.Random(SEED + 5)
        positions = [(0, 0, 0), (1000, 500, -20), (-300, 640, -100), (32767, 32767, 32767),
                     (-32768, -32768, -32768)]
        positions += [(rng.randrange(-2000, 2000), rng.randrange(-200, 3000),
                       rng.randrange(-400, 200)) for _ in range(60)]
        for at_p1 in (False, True):
            for pos in positions:
                for w in range(0, 32):   # valid table range; >31 reads adjacent ROM (documented)
                    COMPARISONS["D5_body_boxes"] += 1
                    for h in (0, 1, 2, 4, 8, 12, 31):
                        a = Actor(sprite_w=w, sprite_h=h, flags_4b=0,
                                  x=pos[0] << 16, z=pos[1] << 16, y=pos[2] << 16)
                        p, s = build_player_boxes(a, self.tables, at_p1_base=at_p1)
                        op, os_ = self.o.boxes(w, h, 0, pos[0], pos[1], pos[2], at_p1)
                        self.assertEqual(p.as_tuple(), op, f"primary w={w} h={h} pos={pos} p1={at_p1}")
                        self.assertEqual(s.as_tuple(), os_, f"secondary w={w} h={h} pos={pos} p1={at_p1}")
        # invulnerable branch
        for at_p1 in (False, True):
            for w in (0, 4):
                a = Actor(sprite_w=w, sprite_h=2, flags_4b=0x02,
                          x=1000 << 16, z=500 << 16, y=-20 << 16)
                p, s = build_player_boxes(a, self.tables, at_p1_base=at_p1)
                op, os_ = self.o.boxes(w, 2, 0x02, 1000, 500, -20, at_p1)
                self.assertEqual((p.as_tuple(), s.as_tuple()), (op, os_))

    # ---- D6 AABB predicate ------------------------------------------
    def test_D6_aabb(self):
        rng = random.Random(SEED + 6)
        cases = [
            ((0, 10, 0, 10, 0, 10), (0, 10, 0, 10, 0, 10)),
            ((0, 10, 0, 10, 0, 10), (10, 20, 0, 10, 0, 10)),   # touching X
            ((0, 10, 0, 10, 0, 10), (11, 20, 0, 10, 0, 10)),   # gap X
            ((0, 10, 0, 10, 0, 10), (0, 10, 10, 20, 0, 10)),   # touching Z
            ((0, 10, 0, 10, 0, 10), (0, 10, 0, 10, 10, 20)),   # touching Y
            ((0, 10, 0, 10, 0, 10), (0, 10, 0, 10, 11, 20)),   # gap Y
            ((-5, 5, -5, 5, -5, 5), (-1, 1, -1, 1, -1, 1)),    # containment
        ]
        for _ in range(500):
            def box():
                x = rng.randrange(-50, 50); y = rng.randrange(-50, 50); z = rng.randrange(-50, 50)
                return (x, x + rng.randrange(0, 30), z, z + rng.randrange(0, 30),
                        y, y + rng.randrange(0, 30))
            cases.append((box(), box()))
        for ba, bb in cases:
            COMPARISONS["D6_aabb"] += 1
            got = aabb_overlap(Box(*ba), Box(*bb))
            self.assertEqual(got, self.o.aabb(ba, bb), f"{ba} vs {bb}")

    # ---- D7 projection + culling ------------------------------------
    def test_D7_projection(self):
        rng = random.Random(SEED + 7)
        cases = [(1, 0x00, 1000, 500, -20, 0, 0), (1, 0x00, 1000, 500, -20, 300, 100),
                 (1, 0x02, 1000, 500, -20, 300, 100), (1, 0x08, 2000, 500, -20, 0, 0),
                 (1, 0x00, 2000, 500, -20, 0, 0), (5, 0x00, -2000, 500, -20, 0, 0),
                 (1, 0x00, 1000, 500, 300, 0, 0), (1, 0x00, 1000, 500, -2000, 0, 0)]
        cases += [(rng.choice([1, 2, 5]), rng.randrange(0, 16), rng.randrange(-3000, 3000),
                   rng.randrange(-300, 2000), rng.randrange(-1200, 400),
                   rng.randrange(-500, 500), rng.randrange(-200, 200)) for _ in range(500)]
        for (t, f, x, z, y, cx, cy) in cases:
            for police in (False, True):
                COMPARISONS["D7_projection"] += 1
                a = Actor(type_id=t, flags_01=f, x=x << 16, z=z << 16, y=y << 16)
                sx, sy, culled = project(a, cx, cy, police)
                osx, osy, oculled = self.o.project(t, f, x, z, y, cx, cy, police)
                self.assertEqual(culled, oculled, f"cull t={t} f={f} pos={(x,z,y)} cam={(cx,cy)} police={police}")
                if not culled:
                    self.assertEqual((sx & 0xFFFF, sy & 0xFFFF), (osx, osy),
                                     f"screen t={t} f={f} pos={(x,z,y)} cam={(cx,cy)}")

    # ---- D8 composed frame trajectories -----------------------------
    def test_D8_frame_composition(self):
        from reconstruction.slice_runner import actor_from_dict, step
        for name, frames, plan, initial in FRAME_SCENARIOS:
            with self.subTest(scenario=name):
                oplan = dict(plan)
                oplan["initial"] = dict(initial)
                otrace = self.o.frame(oplan, frames)
                a = actor_from_dict(initial)
                for f in range(frames):
                    COMPARISONS["D8_frame"] += 1
                    snap = step(a, plan, self.tables)
                    o = otrace[f]
                    for key in ("x", "z", "y", "vx", "vz", "vy"):
                        self.assertEqual(u32(snap[key]), o[key],
                                         f"{name} frame {f} {key}: {snap[key]} vs {o[key]}")
                    self.assertEqual(snap["box_primary"], o["box_primary"], f"{name} f{f} primary box")
                    self.assertEqual(snap["box_secondary"], o["box_secondary"], f"{name} f{f} secondary box")
                    if not o["culled"]:
                        self.assertEqual((snap["sx"] & 0xFFFF, snap["sy"] & 0xFFFF), (o["sx"], o["sy"]),
                                         f"{name} f{f} screen")
                    self.assertEqual(a.state & 0xFF, o["state"], f"{name} f{f} state")
                    self.assertEqual(a.anim_offset, o["anim_offset"], f"{name} f{f} anim")


if __name__ == "__main__":
    unittest.main(verbosity=2)
