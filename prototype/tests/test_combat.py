"""Hit detection, hit tracking, armour, damage and defeat paths."""
from __future__ import annotations

import unittest

from . import support

from prototype.neon_alley.config import PLAYER_HP
from prototype.neon_alley.game import Command, Game


def fresh():
    game = Game()
    game.start()
    p = game.player
    support.place(p, 300, 90)
    enemy = support.dummy_enemy(game)
    support.place(enemy, 330, 90)
    return game, p, enemy


class TestHitDetection(unittest.TestCase):
    def test_valid_punch_lands(self):
        game, p, e = fresh()
        hp0 = e.hp
        for _ in range(20):
            game.update(Command(punch=True) if game.frame == 0 else Command())
        self.assertEqual(hp0 - e.hp, 7)
        self.assertGreater(len(game.effects), 0, "no on-hit visual spawned")

    def test_kick_lands_and_hits_harder(self):
        game, p, e = fresh()
        hp0 = e.hp
        for _ in range(40):
            game.update(Command(kick=True) if game.frame == 0 else Command())
        self.assertEqual(hp0 - e.hp, 13)

    def test_out_of_range_punch_misses(self):
        game, p, e = fresh()
        support.place(e, 400, 90)          # 100 px away, punch reach is 34
        hp0 = e.hp
        for _ in range(20):
            game.update(Command(punch=True) if game.frame == 0 else Command())
        self.assertEqual(e.hp, hp0)

    def test_wrong_depth_punch_misses(self):
        game, p, e = fresh()
        support.place(e, 330, 130)         # 40 px of depth, punch depth is 22
        hp0 = e.hp
        for _ in range(20):
            game.update(Command(punch=True) if game.frame == 0 else Command())
        self.assertEqual(e.hp, hp0)

    def test_punching_away_from_the_enemy_misses(self):
        game, p, e = fresh()
        support.place(p, 330, 90)          # player is right of the enemy...
        for _ in range(6):
            game.update(Command(move_x=1))  # ...and faces right
        hp0 = e.hp
        for _ in range(20):
            game.update(Command(punch=True) if game.frame % 10 == 0 else Command())
        self.assertEqual(e.hp, hp0)

    def test_one_attack_deals_damage_once(self):
        game, p, e = fresh()
        hp0 = e.hp
        seen = []
        game.update(Command(punch=True))
        for _ in range(14):
            game.update(Command())
            seen.append(e.hp)
        self.assertEqual(hp0 - e.hp, 7, "damage applied more than once")
        self.assertEqual(sum(1 for a, b in zip([hp0] + seen, seen) if b < a), 1)

    def test_hitstun_and_iframes(self):
        game, p, e = fresh()
        game.update(Command(punch=True))
        for _ in range(4):
            game.update(Command())
        self.assertGreater(e.hitstun + e.iframes, 0)

    def test_player_attack_cooldown_blocks_spam(self):
        game, p, e = fresh()
        game.update(Command(punch=True))
        # run to the end of the swing (13 frames, plus hit-stop when it connects)
        for _ in range(40):
            if p.attack is None:
                break
            game.update(Command())
        self.assertIsNone(p.attack)
        self.assertGreater(p.attack_cooldown, 0, "recovery should set a cooldown")
        game.update(Command(punch=True))
        self.assertIsNone(p.attack, "cooldown should reject a new attack")


class TestEnemyAttack(unittest.TestCase):
    def test_enemy_attack_lands_on_idle_player(self):
        game = Game()
        game.start()
        p = game.player
        support.place(p, 300, 90)
        e = support.dummy_enemy(game)
        support.place(e, 328, 90)
        e.cooldown = 0
        hp0 = p.hp
        for _ in range(90):
            game.update(Command())
        self.assertLess(p.hp, hp0)

    def test_enemy_swing_is_armoured_through_startup(self):
        game = Game()
        game.start()
        p = game.player
        support.place(p, 300, 90)
        e = support.dummy_enemy(game)
        support.place(e, 328, 90)
        e.cooldown = 0
        e.start_attack("enemy")
        hp0 = e.hp
        # interrupt attempt during enemy startup: damage lands, swing survives
        game.update(Command(punch=True))
        for _ in range(5):                 # punch needs 3 startup frames
            game.update(Command())
        self.assertLess(e.hp, hp0, "armoured enemy should still take damage")
        self.assertIsNotNone(e.attack, "armoured swing was cancelled by a hit")

    def test_player_can_be_defeated(self):
        game = Game()
        game.start()
        frames = 0
        while game.state == Game.PLAY and frames < 5000:
            game.update(Command())
            frames += 1
        self.assertEqual(game.state, Game.DEFEAT)
        self.assertEqual(game.player.hp, 0)
        self.assertLessEqual(game.player.hp, PLAYER_HP)


class TestDefeatOfEnemies(unittest.TestCase):
    def test_enemy_dies_and_is_counted(self):
        game, p, e = fresh()
        for _ in range(400):
            if e.dead:
                break
            game.update(Command(punch=True) if game.frame % 12 == 0 else Command())
        self.assertTrue(e.dead)
        self.assertEqual(e.hp, 0)
        self.assertEqual(game.kills, 1)

    def test_dead_enemy_is_removed_after_the_death_animation(self):
        game, p, e = fresh()
        e.hp = 1
        for _ in range(200):
            game.update(Command(punch=True) if game.frame % 12 == 0 else Command())
            if e.dead and e.death_timer > 60:
                break
        self.assertNotIn(e, game.enemies)

    def test_dead_enemy_cannot_be_hit_again(self):
        game, p, e = fresh()
        e.hp = 1
        for _ in range(20):
            game.update(Command(punch=True) if game.frame % 12 == 0 else Command())
        self.assertTrue(e.dead)
        kills = game.kills
        for _ in range(60):
            game.update(Command())
        self.assertEqual(game.kills, kills)


if __name__ == "__main__":
    unittest.main()
