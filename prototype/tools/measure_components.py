"""Measure how often the game calls each verified component.

    python -m prototype.tools.measure_components

Three paths are measured separately so the numbers are comparable:
  1. simulation only  — recorded script replayed through Game.update()
  2. simulation+draw  — the same frames, each one also rendered
  3. jump coverage    — a script with jumps, so gravity/air-control are exercised
"""
from __future__ import annotations

import json
import os
import sys
from pathlib import Path

os.environ.setdefault("SDL_VIDEODRIVER", "dummy")
os.environ.setdefault("SDL_AUDIODRIVER", "dummy")

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from prototype.neon_alley import adapter  # noqa: E402
from prototype.neon_alley.game import Command, Game  # noqa: E402

FIELDS = ("move_x", "move_z", "jump", "punch", "kick")
KEYS = ("integrate", "build_boxes", "aabb", "gravity", "clamp", "air_control", "project")


def load_script():
    data = json.loads((ROOT / "prototype" / "data" / "scripted_run.json").read_text())
    return [Command(**{f: e[f] for f in FIELDS}) for e in data["commands"]]


def simulate(commands, renderer=None):
    game = Game()
    game.start()
    adapter.reset_stats()
    for i, cmd in enumerate(commands):
        if game.state != Game.PLAY:
            break
        game.update(cmd)
        if renderer is not None:
            renderer.draw(game, i / 60.0)
    return game, dict(adapter.STATS)


def jump_script():
    """90 frames: jump, hold right in the air, land, punch, jump again."""
    out = []
    for i in range(90):
        out.append(Command(
            move_x=1,
            jump=(i in (2, 46)),
            punch=(i == 70),
        ))
    return out


def main() -> int:
    import pygame
    pygame.init()
    pygame.display.set_mode((384, 240))
    from prototype.neon_alley.render import Renderer

    renderer = Renderer()
    commands = load_script()

    sim_game, sim_stats = simulate(commands)
    draw_game, draw_stats = simulate(commands, renderer)
    _, jump_stats = simulate(jump_script(), renderer)

    n = len(commands)
    rows = [
        (f"simulation only ({n} frames)", sim_stats),
        (f"simulation + rendering ({n} frames)", draw_stats),
        ("jump script + rendering (90 frames)", jump_stats),
    ]
    header = f"{'path':38s} " + " ".join(f"{k:>12s}" for k in KEYS)
    print(header)
    print("-" * len(header))
    for label, stats in rows:
        print(f"{label:38s} " + " ".join(f"{stats[k]:12d}" for k in KEYS))
    print()
    print("outcome (simulation only):", json.dumps({
        "state": sim_game.state, "frames": sim_game.frame, "kills": sim_game.kills,
        "player_hp": sim_game.player.hp}, sort_keys=True))
    print("outcome (with rendering) :", json.dumps({
        "state": draw_game.state, "frames": draw_game.frame, "kills": draw_game.kills,
        "player_hp": draw_game.player.hp}, sort_keys=True))
    zero = [k for k, v in draw_stats.items() if v == 0]
    print("never called on the drawn path:", zero or "none")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
