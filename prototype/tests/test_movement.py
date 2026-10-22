"""Ground/depth movement, jumping, air control and arena collision."""
from __future__ import annotations

import unittest

from . import support

from prototype.neon_alley.config import (ARENA_X_MAX, ARENA_X_MIN, ARENA_Z_MAX,
                                         ARENA_Z_MIN, PLAYER_DEPTH_VZ)
from prototype.neon_alley.game import Command, Game


class TestGroundMovement(unittest.TestCase):
    def setUp(self):
        self.game = Game()
        self.game.start()

    def test_walks_right_and_left(self):
        p = self.game.player
        x0 = p.wx
        for _ in range(30):
            self.game.update(Command(move_x=1))
        moved = p.wx - x0
        self.assertGreater(moved, 40)        # accelerates to 2.25 px/frame
        self.assertLess(moved, 30 * 3)
        self.assertEqual(p.facing, 1)

        x1 = p.wx
        for _ in range(30):
            self.game.update(Command(move_x=-1))
        self.assertLess(p.wx, x1)
        self.assertEqual(p.facing, -1)

    def test_depth_movement_is_smaller_than_horizontal(self):
        p = self.game.player
        z0 = p.wz
        for _ in range(60):
            self.game.update(Command(move_z=1))
        self.assertGreater(p.wz, z0)
        frames = p.wz - z0
        self.assertAlmostEqual(frames / 60, PLAYER_DEPTH_VZ / 65536, delta=0.2)

    def test_arena_bounds_hold(self):
        p = self.game.player
        for _ in range(900):
            self.game.update(Command(move_x=1, move_z=1))
        self.assertLessEqual(p.wx, ARENA_X_MAX)
        self.assertLessEqual(p.wz, ARENA_Z_MAX)
        for _ in range(1200):
            self.game.update(Command(move_x=-1, move_z=-1))
        self.assertGreaterEqual(p.wx, ARENA_X_MIN)
        self.assertGreaterEqual(p.wz, ARENA_Z_MIN)

    def test_enemies_never_stick_to_bounds(self):
        """Enemies must reach the player even with the player at a corner."""
        game = Game()
        game.start()
        support.place(game.player, ARENA_X_MIN + 2, ARENA_Z_MAX - 2)
        for e in game.enemies:
            e.spawn_delay = 0
        for _ in range(1200):
            game.update(Command())
            for e in game.enemies:
                self.assertGreaterEqual(e.wx, ARENA_X_MIN)
                self.assertLessEqual(e.wx, ARENA_X_MAX)
                self.assertGreaterEqual(e.wz, ARENA_Z_MIN)
                self.assertLessEqual(e.wz, ARENA_Z_MAX)
        # A cornered, passive player takes hits — and can be defeated outright.
        self.assertLess(game.player.hp, 80, "cornered player should have been hit")
        self.assertIn(game.state, (Game.PLAY, Game.DEFEAT))


class TestJumpAndAirControl(unittest.TestCase):
    def setUp(self):
        self.game = Game()
        self.game.start()

    def test_jump_leaves_ground_and_lands(self):
        p = self.game.player
        self.assertTrue(p.grounded)
        apex = 0
        frames = 0
        self.game.update(Command(jump=True))
        self.assertFalse(p.grounded)
        self.assertLess(p.wy, 0)
        while not p.grounded and frames < 240:
            self.game.update(Command())
            apex = min(apex, p.wy)
            frames += 1
        self.assertTrue(p.grounded, "player never landed")
        self.assertLessEqual(apex, -25, "jump did not rise")
        self.assertGreater(frames, 10)
        self.assertEqual(p.body.vy, 0)
        self.assertEqual(p.wy, 0)

    def test_air_control_changes_horizontal_speed(self):
        game = Game()
        game.start()
        p = game.player
        game.update(Command(jump=True))
        # no input in the air for 12 frames
        for _ in range(12):
            game.update(Command())
        vx_neutral = p.body.vx

        game2 = Game()
        game2.start()
        p2 = game2.player
        game2.update(Command(jump=True))
        for _ in range(12):
            game2.update(Command(move_x=1))
        self.assertGreater(p2.body.vx, vx_neutral + 0x1000)
        self.assertGreater(p2.wx, p.wx + 5)

    def test_air_gravity_and_terminal_clamp_are_component_calls(self):
        from prototype.neon_alley import adapter
        adapter.reset_stats()
        for _ in range(40):
            self.game.update(Command(jump=True))
        self.assertGreater(adapter.STATS["gravity"], 0)
        self.assertGreater(adapter.STATS["air_control"], 0)
        self.assertGreater(adapter.STATS["clamp"], 0)

    def test_no_double_jump(self):
        p = self.game.player
        self.game.update(Command(jump=True))
        for _ in range(6):
            self.game.update(Command(jump=True))
        self.assertLess(p.body.vy, 0)  # still rising on the first jump's arc


if __name__ == "__main__":
    unittest.main()
