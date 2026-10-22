"""Specification tests: expectations written from the behavioural spec, with no
emulator involved. If these fail, either the component or the specification is
wrong; neither can hide behind the other.

Run: python3 -m unittest tests.test_component_spec -v
"""
from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from components.sor_engine import (  # noqa: E402
    Actor, BoxTables, aabb_overlap, air_control, build_player_boxes,
    clamp_terminal_velocity, directional_gravity, integrate, is_frozen,
    neutral_gravity, project, soft_gravity,
)
from components.sor_engine.boxes import Box, BoxTables as _BT  # noqa: E402
from components.sor_engine.fixed import hi16, s16, s32  # noqa: E402


class FixedPoint(unittest.TestCase):
    def test_hi16_matches_move_w(self):
        self.assertEqual(hi16(0x0F0000), 15)
        self.assertEqual(hi16(-0x10000), -1)
        self.assertEqual(hi16(-0x08000), -1)      # arithmetic-ish: high word of -0.5 is -1
        self.assertEqual(hi16(0x7FFF8000), 0x7FFF)

    def test_s32_wrap(self):
        self.assertEqual(s32(0x7FFFFFFF + 1), -0x80000000)
        self.assertEqual(s32(-1), -1)
        self.assertEqual(s32(0xFFFFFFFF), -1)


class Gravity(unittest.TestCase):
    def test_neutral_constant(self):
        a = Actor(vy=0)
        neutral_gravity(a)
        self.assertEqual(a.vy, 0xE800)            # +0.90625 px/tick^2

    def test_directional_uses_sign_before_add(self):
        # ascending: neutral value even when the add crosses zero
        a = Actor(vy=-1)
        directional_gravity(a)
        self.assertEqual(a.vy, -1 + 0xE800)
        b = Actor(vy=0)
        directional_gravity(b)
        self.assertEqual(b.vy, 0x8800)            # descending: +1.0625

    def test_soft_gravity(self):
        a = Actor(vy=0)
        soft_gravity(a)
        self.assertEqual(a.vy, 0x3800)            # +0.21875

    def test_terminal_clamp_is_one_sided(self):
        hi = Actor(vy=0xC0001)
        clamp_terminal_velocity(hi)
        self.assertEqual(hi.vy, 0xC0000)
        lo = Actor(vy=-0x900000)
        clamp_terminal_velocity(lo)
        self.assertEqual(lo.vy, -0x900000)        # no downward clamp


class AirControl(unittest.TestCase):
    def test_right_accelerates_and_faces_right(self):
        a = Actor(buttons=0x08, vx=0, state=0x01, anim_offset=0x0002)
        self.assertTrue(air_control(a))
        self.assertEqual(a.vx, 0x6000)
        self.assertEqual(a.state & 0x01, 0)       # facing bit cleared
        self.assertEqual(a.anim_offset & 0x0002, 0)

    def test_left_accelerates_and_faces_left(self):
        a = Actor(buttons=0x04, vx=0, state=0, anim_offset=0)
        self.assertTrue(air_control(a))
        self.assertEqual(a.vx, -0x6000)
        self.assertEqual(a.state & 0x01, 1)
        self.assertEqual(a.anim_offset & 0x0002, 2)

    def test_right_wins_when_both_held(self):
        a = Actor(buttons=0x0C, vx=0)
        air_control(a)
        self.assertEqual(a.vx, 0x6000)

    def test_no_input_leaves_velocity_untouched(self):
        a = Actor(buttons=0x00, vx=0x90000)
        self.assertFalse(air_control(a))
        self.assertEqual(a.vx, 0x90000)           # clamp is inside the branch

    def test_clamp_is_symmetric(self):
        a = Actor(buttons=0x08, vx=0)
        for _ in range(20):
            air_control(a)
        self.assertEqual(a.vx, 0x38000)
        b = Actor(buttons=0x04, vx=0)
        for _ in range(20):
            air_control(b)
        self.assertEqual(b.vx, -0x38000)


class Integration(unittest.TestCase):
    def test_adds_three_axes(self):
        a = Actor(x=0x10000, z=0x20000, y=-0x30000, vx=0x1000, vz=-0x2000, vy=0x3000)
        self.assertTrue(integrate(a))
        self.assertEqual((a.x, a.z, a.y), (0x11000, 0x1E000, -0x2D000))

    def test_freeze_predicate_needs_exact_word(self):
        a = Actor(anim_offset=0x14, flags_59=0x80, x=1, vx=1)
        self.assertTrue(is_frozen(a))
        self.assertFalse(integrate(a))
        self.assertEqual(a.x, 1)
        # high byte must be zero: $0114 is NOT the freeze block
        b = Actor(anim_offset=0x114, flags_59=0x80, x=1, vx=1)
        self.assertFalse(is_frozen(b))
        # low two bits are masked away by andi.b #$FC
        c = Actor(anim_offset=0x17, flags_59=0x80, x=1, vx=1)
        self.assertTrue(is_frozen(c))


class Boxes(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.t = BoxTables.load()

    def test_table_provenance(self):
        self.assertEqual(self.t.z_pairs[0], (-8, 16))
        self.assertEqual(self.t.records[1], (0, 13, 0, -51, 51))
        self.assertEqual(len(self.t.records), 32)

    def test_extents_are_cumulative(self):
        # record 2 = (-3, 10, 0, -50, 50) => x spans X-3 .. X+7
        a = Actor(sprite_w=2, x=1000 << 16, z=500 << 16, y=-20 << 16)
        p, _ = build_player_boxes(a, self.t)
        self.assertEqual(p.as_tuple(), (997, 1007, 492, 508, -70, -20))

    def test_secondary_box_uses_sprite_height(self):
        a = Actor(sprite_w=4, sprite_h=1, x=1000 << 16, z=500 << 16, y=-20 << 16)
        p, s = build_player_boxes(a, self.t)
        self.assertEqual(p.as_tuple(), (987, 1000, 492, 508, -71, -20))
        self.assertEqual(s.as_tuple(), (1000, 1013, 492, 508, -71, -20))

    def test_degenerate_boxes(self):
        a = Actor(sprite_w=0, sprite_h=0)
        p, s = build_player_boxes(a, self.t)
        self.assertEqual(p.as_tuple(), (16, 16, 16, 16, 16, 16))
        self.assertEqual(s.as_tuple(), (0, 0, 0, 0, 0, 0))
        p1, s1 = build_player_boxes(a, self.t, at_p1_base=True)
        self.assertEqual(p1.as_tuple(), (0, 0, 0, 0, 0, 0))

    def test_invulnerable_overrides_secondary(self):
        a = Actor(sprite_w=4, sprite_h=2, flags_4b=0x02)
        _, s = build_player_boxes(a, self.t)
        self.assertEqual(s.as_tuple(), (16, 16, 16, 16, 16, 16))


class AABB(unittest.TestCase):
    def test_inclusive_edges(self):
        base = Box(0, 10, 0, 10, 0, 10)
        self.assertTrue(aabb_overlap(base, Box(10, 20, 0, 10, 0, 10)))
        self.assertFalse(aabb_overlap(base, Box(11, 20, 0, 10, 0, 10)))

    def test_depth_and_height_must_overlap(self):
        base = Box(0, 10, 0, 10, 0, 10)
        self.assertFalse(aabb_overlap(base, Box(0, 10, 11, 20, 0, 10)))
        self.assertFalse(aabb_overlap(base, Box(0, 10, 0, 10, 11, 20)))


class Projection(unittest.TestCase):
    def test_projection_formula(self):
        a = Actor(type_id=1, x=1000 << 16, z=500 << 16, y=-20 << 16)
        sx, sy, culled = project(a, 0, 0)
        self.assertEqual((sx, sy), (1128, 358))   # 1000+128, 250-20+128

    def test_camera_subtraction_and_fixed_actors(self):
        a = Actor(type_id=1, x=1000 << 16, z=500 << 16, y=-20 << 16)
        self.assertEqual(project(a, 300, 100)[:2], (828, 258))
        fixed = a.copy(flags_01=0x02)
        self.assertEqual(project(fixed, 300, 100)[:2], (1128, 358))

    def test_narrow_left_margin(self):
        a = Actor(type_id=1, x=-200 << 16, z=500 << 16, y=-20 << 16)
        self.assertFalse(project(a, 0, 0)[2])     # sx = -72 >= -896 (narrow margin)
        b = Actor(type_id=1, x=-1200 << 16, z=500 << 16, y=-20 << 16)
        self.assertTrue(project(b, 0, 0)[2])      # sx = -1072 < -896

    def test_type5_always_culls_with_wide_margin(self):
        # sx = -272: inside the narrow margin (-896) but outside the wide one (-128)
        a = Actor(type_id=5, flags_01=0x08, x=-400 << 16, z=500 << 16, y=-20 << 16)
        self.assertTrue(project(a, 0, 0, police_active=True)[2])
        plain = Actor(type_id=1, flags_01=0x08, x=-400 << 16, z=500 << 16, y=-20 << 16)
        self.assertFalse(project(plain, 0, 0)[2])   # bit3 skips culling entirely


if __name__ == "__main__":
    unittest.main(verbosity=2)
