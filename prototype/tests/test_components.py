"""Proof that the game's real update path calls the validated reconstruction.

These tests fail if the game ever substitutes its own arithmetic for the
components: the component module is monkey-patched, and the game must follow.
"""
from __future__ import annotations

import unittest

from . import support

from components.sor_engine import boxes as rom_boxes
from components.sor_engine import kinematics as rom_kin
from components.sor_engine import projection as rom_proj
from prototype.neon_alley import adapter
from prototype.neon_alley.game import Command, Game


class TestComponentInvocation(unittest.TestCase):
    def setUp(self):
        self.game = Game()
        self.game.start()

    def test_import_identity(self):
        """adapter points at components.sor_engine, not at a copy."""
        self.assertIs(adapter._kin.integrate, rom_kin.integrate)
        self.assertIs(adapter._boxes.aabb_overlap, rom_boxes.aabb_overlap)
        self.assertIs(adapter._proj.project, rom_proj.project)
        tables = adapter.tables()
        self.assertEqual(len(tables.records), 32)  # ROM-derived tables loaded
        self.assertTrue(tables.records)

    def test_update_path_calls_every_component(self):
        adapter.reset_stats()
        for i in range(180):
            cmd = Command(move_x=1, jump=(i == 10), punch=(i == 40), kick=(i == 80))
            self.game.update(cmd)
        for key in ("integrate", "build_boxes", "aabb", "gravity", "clamp", "air_control"):
            self.assertGreater(adapter.STATS[key], 0, f"{key} was never called")

    def test_patching_integrate_breaks_the_game(self):
        """If the game had its own integration, patching the ROM routine would not matter."""
        calls = []
        original = rom_kin.integrate

        def spy(actor):
            calls.append(actor)
            return original(actor)

        rom_kin.integrate = spy
        try:
            for _ in range(30):
                self.game.update(Command(move_x=1))
        finally:
            rom_kin.integrate = original
        # player + 2 enemies, for 30 frames: integration happens once per actor/frame
        self.assertGreaterEqual(len(calls), 30)

    def test_patching_projection_breaks_rendering(self):
        import pygame
        support.pygame_display()
        from prototype.neon_alley.render import Renderer

        renderer = Renderer()
        original = rom_proj.project
        seen = []

        def spy(actor, cam_x, cam_y, police_active=False):
            seen.append(actor)
            return original(actor, cam_x, cam_y, police_active)

        rom_proj.project = spy
        try:
            renderer.draw(self.game, 0.0)
        finally:
            rom_proj.project = original
        # player + 2 enemies, each drawn and each shadowed
        self.assertGreaterEqual(len(seen), 6)

    def test_projection_is_the_only_screen_mapping(self):
        import pygame
        support.pygame_display()
        from prototype.neon_alley.render import Renderer

        adapter.reset_stats()
        Renderer().draw(self.game, 0.0)
        self.assertGreater(adapter.STATS["project"], 0)


class TestBoxesStaySeparate(unittest.TestCase):
    def test_attack_box_differs_from_body_boxes(self):
        game = Game()
        game.start()
        p = game.player
        support.place(p, 300, 84)
        p.start_attack("punch")
        atk = p.attack_box()
        bodies = [b for b in p.boxes()]
        for body in bodies:
            self.assertNotEqual((atk.x1, atk.x2, atk.z1, atk.z2, atk.y1, atk.y2),
                                (body.x1, body.x2, body.z1, body.z2, body.y1, body.y2))

    def test_body_box_values_are_rom_table_outputs(self):
        game = Game()
        game.start()
        support.place(game.player, 100, 60)
        support.place(support.dummy_enemy(game), 200, 60)
        self.assertEqual(game.player.body_box().as_tuple(), (97, 111, 52, 68, -42, 0))
        self.assertEqual(support.dummy_enemy(game).body_box().as_tuple(),
                         (197, 207, 52, 68, -50, 0))

    def test_hit_requires_attack_box_overlap_not_body_overlap(self):
        game = Game()
        game.start()
        p = game.player
        enemy = support.dummy_enemy(game)
        support.place(p, 300, 84)
        support.place(enemy, 330, 84)
        p.start_attack("punch")
        self.assertFalse(adapter.overlap(p.body_box(), enemy.body_box()))
        self.assertTrue(adapter.overlap(p.attack_box(), enemy.body_box()))


if __name__ == "__main__":
    unittest.main()


class TestFreezePredicate(unittest.TestCase):
    """`$00442C` refuses to integrate a frozen actor, and the game honours that."""

    def test_frozen_actor_is_not_integrated_and_does_not_land(self):
        game = Game()
        game.start()
        p = game.player
        support.place(p, 300, 90)
        game.update(Command(jump=True))
        for _ in range(3):
            game.update(Command())
        self.assertFalse(p.grounded)
        y_before, x_before = p.body.y, p.body.x

        # the engine's freeze state: (state & $FC) == $14 with bit7 of +$59 set
        p.body.anim_offset = 0x14
        p.body.flags_59 |= 0x80
        self.assertTrue(adapter.is_frozen(p.body))
        for _ in range(20):
            game.update(Command(move_x=1))
        self.assertEqual(p.body.y, y_before, "frozen actor was integrated vertically")
        self.assertFalse(p.grounded, "a suppressed integration was read as a landing")

        p.body.flags_59 &= ~0x80
        self.assertFalse(adapter.is_frozen(p.body))
        for _ in range(60):
            game.update(Command())
        self.assertTrue(p.grounded)
        self.assertEqual(p.body.y, 0)
