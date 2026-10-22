"""Deterministic scripted encounter, replayed from a recorded input file.

`prototype/data/scripted_run.json` holds one `Command` per frame, recorded by
`prototype/tools/record_encounter.py`. Replaying it through a fresh `Game` must
reproduce the same outcome exactly — the simulation has no randomness.
"""
from __future__ import annotations

import json
import unittest
from pathlib import Path

from . import support  # noqa: F401

from prototype.neon_alley import adapter
from prototype.neon_alley.game import Command, Game

SCRIPT = Path(__file__).resolve().parents[1] / "data" / "scripted_run.json"
FIELDS = ("move_x", "move_z", "jump", "punch", "kick")


def load_script(path=SCRIPT):
    data = json.loads(Path(path).read_text())
    return [Command(**{f: entry[f] for f in FIELDS}) for entry in data["commands"]]


def replay(commands):
    game = Game()
    game.start()
    for cmd in commands:
        if game.state != Game.PLAY:
            break
        game.update(cmd)
    return game


class TestScriptedEncounter(unittest.TestCase):
    def test_replay_is_deterministic(self):
        commands = load_script()
        a = replay(commands)
        b = replay(commands)
        self.assertEqual(a.snapshot(), b.snapshot())
        self.assertEqual(a.frame, b.frame)

    def test_recorded_encounter_result(self):
        commands = load_script()
        game = replay(commands)
        print("\n[scripted encounter] " + json.dumps({
            "commands": len(commands),
            "state": game.state,
            "frames": game.frame,
            "kills": game.kills,
            "total_enemies": game.total_enemies,
            "player_hp": game.player.hp,
            "player_position": [game.player.wx, game.player.wz],
        }, sort_keys=True))
        self.assertEqual(game.state, Game.VICTORY)
        self.assertEqual(game.kills, 3)
        self.assertLess(game.player.hp, game.player.max_hp, "script took no damage at all")

    def test_recorded_encounter_exercises_the_components(self):
        commands = load_script()
        adapter.reset_stats()
        replay(commands)
        for key in ("integrate", "build_boxes", "aabb", "gravity", "clamp"):
            self.assertGreater(adapter.STATS[key], 0, key)

    def test_empty_input_script_ends_in_defeat(self):
        """The same simulation, with no player input, must reach the other ending."""
        game = Game()
        game.start()
        for _ in range(4000):
            if game.state != Game.PLAY:
                break
            game.update(Command())
        print(f"\n[passive encounter] state={game.state} frames={game.frame} hp={game.player.hp}")
        self.assertEqual(game.state, Game.DEFEAT)


if __name__ == "__main__":
    unittest.main()
