"""Record a deterministic input script and print the resulting encounter report.

    python -m prototype.tools.record_encounter [--out prototype/data/scripted_run.json]

The recorder drives the game with the prototype's AutoPilot, writes every
`Command` it emitted to JSON, and then replays that JSON through a *fresh* game
to prove the recording alone reproduces the run.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from prototype.neon_alley import adapter  # noqa: E402
from prototype.neon_alley.autopilot import AutoPilot  # noqa: E402
from prototype.neon_alley.game import Command, Game  # noqa: E402

FIELDS = ("move_x", "move_z", "jump", "punch", "kick")


def record(max_frames: int = 8000) -> tuple[list[dict], dict]:
    game = Game()
    game.start()
    pilot = AutoPilot()
    script: list[dict] = []
    while game.state == Game.PLAY and len(script) < max_frames:
        cmd = pilot.command(game)
        script.append({f: int(getattr(cmd, f)) for f in FIELDS})
        game.update(cmd)
    return script, report(game, script)


def replay(script: list[dict]) -> Game:
    game = Game()
    game.start()
    for entry in script:
        if game.state != Game.PLAY:
            break
        game.update(Command(**{f: entry[f] for f in FIELDS}))
    return game


def report(game: Game, script: list[dict]) -> dict:
    return {
        "state": game.state,
        "frames": len(script),
        "kills": game.kills,
        "total_enemies": game.total_enemies,
        "player_hp": game.player.hp,
        "player_position": [game.player.wx, game.player.wz],
        "component_calls": dict(adapter.STATS),
        "first_frame_without_hp": _first_damage(script),
    }


def _first_damage(script: list[dict]) -> int | None:
    game = Game()
    game.start()
    for i, entry in enumerate(script):
        game.update(Command(**{f: entry[f] for f in FIELDS}))
        if game.player.hp < game.player.max_hp:
            return i
    return None


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=str(ROOT / "prototype" / "data" / "scripted_run.json"))
    args = ap.parse_args(argv)

    script, stats = record()
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps({"version": 1, "frames": len(script), "commands": script},
                              indent=0))
    replay_game = replay(script)
    print(f"recorded {len(script)} command frames -> {out.relative_to(ROOT)}")
    print("recorded run :", json.dumps(stats, sort_keys=True))
    print("replayed run :", json.dumps({
        "state": replay_game.state,
        "frame": replay_game.frame,
        "kills": replay_game.kills,
        "player_hp": replay_game.player.hp,
        "player_position": [replay_game.player.wx, replay_game.player.wz],
    }, sort_keys=True))
    ok = (replay_game.state == stats["state"] and replay_game.kills == stats["kills"]
          and replay_game.player.hp == stats["player_hp"])
    print("replay matches recording:", ok)
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
