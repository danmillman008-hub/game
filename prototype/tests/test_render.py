"""Depth ordering, projection-driven placement, and headless smoke drawing."""
from __future__ import annotations

import unittest

from . import support

from prototype.neon_alley import adapter
from prototype.neon_alley.game import Command, Game


class TestRender(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        support.pygame_display()
        from prototype.neon_alley.render import Renderer
        cls.Renderer = Renderer
        cls.renderer = Renderer()

    def test_depth_order_far_to_near(self):
        game = Game()
        game.start()
        support.place(game.player, 300, 120)     # deep lane (far)
        support.place(support.dummy_enemy(game, 0), 260, 40)   # shallow lane (near)
        support.place(support.dummy_enemy(game, 1), 210, 75)
        order = []
        renderer = self.renderer
        original = renderer._draw_fighter

        def spy(surf, f, sx, sy, t):
            order.append(f.wz)

        renderer._draw_fighter = spy
        try:
            cam = game.cam_x
            renderer._draw_actors(None, game, cam, 0.0)
        finally:
            renderer._draw_fighter = original
        self.assertEqual(order, sorted(order), "actors are not drawn far-to-near")
        self.assertEqual(order, [40, 75, 120])

    def test_offscreen_actor_is_culled_by_the_component(self):
        far = adapter.Actor(type_id=1, x=2000 << 16, z=60 << 16, y=0)
        sx, sy, culled = adapter.project(far, 0, 0)
        self.assertTrue(culled)
        self.assertGreaterEqual(sx, 0x500)

    def test_shadow_stays_on_the_ground_during_a_jump(self):
        game = Game()
        game.start()
        p = game.player
        support.place(p, 300, 90)
        ground_sy = self.renderer._ground_sy(p.body, game.cam_x)
        game.update(Command(jump=True))
        for _ in range(8):
            game.update(Command())
        self.assertLess(p.wy, -5, "player is not airborne")
        airborne_sy = self.renderer._ground_sy(p.body, game.cam_x)
        self.assertEqual(airborne_sy, ground_sy, "shadow detached from the ground plane")
        _, body_sy, _ = self.renderer._screen(p.body, game.cam_x)
        self.assertLess(body_sy, ground_sy, "body did not rise off the ground")

    def test_draw_every_state_without_error(self):
        game = Game()
        surf = self.renderer.draw(game, 0.0)          # title
        self.assertEqual(surf.get_size(), (384, 240))
        game.start()
        for i in range(120):
            game.update(Command(move_x=1, jump=(i == 5), punch=(i == 20)))
            self.renderer.draw(game, i / 60.0)
        game.state = Game.VICTORY
        self.renderer.draw(game, 1.0)
        game.state = Game.DEFEAT
        self.renderer.draw(game, 1.0)

    def test_render_path_uses_projection(self):
        game = Game()
        game.start()
        adapter.reset_stats()
        self.renderer.draw(game, 0.0)
        self.assertGreaterEqual(adapter.STATS["project"], 6)


if __name__ == "__main__":
    unittest.main()
