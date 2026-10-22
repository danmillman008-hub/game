"""Title -> play -> waves -> victory/defeat, restart, and numeric sanity."""
from __future__ import annotations

import unittest

from . import support  # noqa: F401  (sets SDL driver + import path)

from prototype.neon_alley.autopilot import AutoPilot
from prototype.neon_alley.config import WAVES
from prototype.neon_alley.game import Command, Game


class TestFlow(unittest.TestCase):
    def test_title_does_not_simulate(self):
        game = Game()
        for _ in range(30):
            game.update(Command(move_x=1, punch=True))
        self.assertEqual(game.state, Game.TITLE)
        self.assertEqual(game.enemies, [])

    def test_start_spawns_first_wave(self):
        game = Game()
        game.start()
        self.assertEqual(game.state, Game.PLAY)
        self.assertEqual(len(game.enemies), len(WAVES[0]))
        self.assertTrue(all(e.spawn_delay >= 0 for e in game.enemies))

    def test_second_wave_spawns_after_first_is_cleared(self):
        game = Game()
        game.start()
        for e in game.enemies:
            e.hp = 1
            e.dead = True
            e.death_timer = 999
        for _ in range(200):
            game.update(Command())
        self.assertEqual(game.wave_index, 1)
        self.assertEqual(len(game.enemies), len(WAVES[1]))
        self.assertTrue(all(not e.dead for e in game.enemies))
        self.assertEqual(game.enemies[0].kind, WAVES[1][0]["kind"])

    def test_autopilot_reaches_victory(self):
        game = Game()
        game.start()
        pilot = AutoPilot()
        frames = 0
        while game.state == Game.PLAY and frames < 8000:
            game.update(pilot.command(game))
            frames += 1
        self.assertEqual(game.state, Game.VICTORY, f"no victory in {frames} frames")
        self.assertEqual(game.kills, game.total_enemies)

    def test_restart_returns_to_a_clean_run(self):
        game = Game()
        game.start()
        pilot = AutoPilot()
        for _ in range(400):
            if game.state != Game.PLAY:
                break
            game.update(pilot.command(game))
        game.reset()
        self.assertEqual(game.state, Game.TITLE)
        self.assertEqual(game.frame, 0)
        self.assertEqual(game.kills, 0)
        self.assertEqual(game.enemies, [])
        self.assertEqual(game.player.hp, game.player.max_hp)
        game.start()
        self.assertEqual(game.wave_index, 0)
        self.assertEqual(len(game.enemies), len(WAVES[0]))

    def test_two_runs_are_bit_identical(self):
        runs = []
        for _ in range(2):
            game = Game()
            game.start()
            pilot = AutoPilot()
            trace = []
            for _ in range(900):
                if game.state != Game.PLAY:
                    break
                game.update(pilot.command(game))
                trace.append((game.player.wx, game.player.wz, game.player.hp,
                              tuple((e.wx, e.wz, e.hp) for e in game.enemies)))
            runs.append((game.state, game.frame, game.kills, trace))
        self.assertEqual(runs[0], runs[1])


class TestNumericSanity(unittest.TestCase):
    def test_long_run_has_no_invalid_state(self):
        game = Game()
        game.start()
        pilot = AutoPilot()
        for frame in range(3000):
            if game.state != Game.PLAY:
                break
            cmd = pilot.command(game)
            if frame % 97 == 0:
                cmd = Command(move_x=1, move_z=-1, jump=True)
            game.update(cmd)
            for f in [game.player, *game.enemies]:
                for value in (f.body.x, f.body.y, f.body.z, f.body.vx, f.body.vz, f.body.vy):
                    self.assertIsInstance(value, int)
                    self.assertLess(abs(value), 1 << 31)
                box = f.body_box()
                self.assertLessEqual(box.x1, box.x2)
                self.assertLessEqual(box.z1, box.z2)
                self.assertLessEqual(box.y1, box.y2)
                self.assertLessEqual(f.hp, f.max_hp)
                self.assertGreaterEqual(f.hp, 0)

    def test_frame_counter_advances_once_per_update(self):
        game = Game()
        game.start()
        for expected in range(1, 61):
            game.update(Command())
            self.assertEqual(game.frame, expected)


if __name__ == "__main__":
    unittest.main()
