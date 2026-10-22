"""End-to-end smoke test of the real entry point (window, loop, scaling, draw).

Runs the actual `main.run()` with a dummy SDL video driver for a fixed number of
frames, so the event loop, the frame accumulator, the canvas upscale and the
renderer are all exercised — not just the simulation.
"""
from __future__ import annotations

import os
import tempfile
import unittest
from pathlib import Path

from . import support  # noqa: F401


class TestSmoke(unittest.TestCase):
    def test_main_loop_runs_headless_and_saves_a_frame(self):
        from prototype.neon_alley import main as game_main
        with tempfile.TemporaryDirectory() as tmp:
            shot = os.path.join(tmp, "frame.png")
            rc = game_main.run((640, 400), False, True, max_frames=90, shot=shot)
            self.assertEqual(rc, 0)
            self.assertTrue(Path(shot).exists(), "no frame was captured")
            self.assertGreater(Path(shot).stat().st_size, 1000)

    def test_window_scales_without_changing_the_canvas(self):
        import pygame
        from prototype.neon_alley.config import VIRTUAL_H, VIRTUAL_W
        from prototype.neon_alley.game import Game
        from prototype.neon_alley.render import Renderer
        support.pygame_display()
        surf = Renderer().draw(Game(), 0.0)
        self.assertEqual(surf.get_size(), (VIRTUAL_W, VIRTUAL_H))
        for size in ((640, 400), (1280, 720), (1920, 1080)):
            scale = min(size[0] / VIRTUAL_W, size[1] / VIRTUAL_H)
            target = (int(VIRTUAL_W * scale), int(VIRTUAL_H * scale))
            self.assertGreater(target[0], 0)
            out = pygame.transform.smoothscale(surf, target)
            self.assertEqual(out.get_size(), target)


if __name__ == "__main__":
    unittest.main()


class TestKeyboardMapping(unittest.TestCase):
    """The interactive path: key state -> Command (actions are edge-triggered)."""

    def setUp(self):
        from prototype.neon_alley import main as game_main
        self.m = game_main

    @staticmethod
    def keys(**pressed):
        from collections import defaultdict
        from prototype.neon_alley import main as m
        table = defaultdict(lambda: False)
        for name, value in pressed.items():
            table[getattr(m, f"K_{name.upper()}")] = value
        return table

    def test_movement_keys(self):
        cmd = self.m._poll_command(None, self.keys(d=1, s=1), self.keys())
        self.assertEqual((cmd.move_x, cmd.move_z), (1, 1))
        cmd = self.m._poll_command(None, self.keys(a=1, w=1), self.keys())
        self.assertEqual((cmd.move_x, cmd.move_z), (-1, -1))

    def test_actions_fire_once_per_press(self):
        held = self.keys(j=1, k=1, SPACE=1)
        first = self.m._poll_command(None, held, self.keys())
        self.assertTrue(first.punch and first.kick and first.jump)
        second = self.m._poll_command(None, held, held)   # still held
        self.assertFalse(second.punch or second.kick or second.jump)
