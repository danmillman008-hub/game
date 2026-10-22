"""Prove the browser port computes the same thing as the Python reference.

    python -m prototype.tools.web_conformance [--json]

Three input sets are replayed through both engines:

  1. the recorded 875-frame encounter (prototype/data/scripted_run.json)
  2. a passive run (no input at all until the game ends)
  3. a synthetic 2,000-frame run from a fixed xorshift sequence

Every frame is compared field by field — position, velocity, health, stun,
attack frame, timers, camera, wave, kills, state — with **no tolerance**.
Exit code is 0 only if all three runs match exactly.
"""
from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from prototype.neon_alley import adapter  # noqa: E402
from prototype.neon_alley.game import Command, Game  # noqa: E402

NODE = shutil.which("node")
HARNESS = ROOT / "prototype" / "web" / "conformance.js"
FIELDS = ("move_x", "move_z", "jump", "punch", "kick")


# --------------------------------------------------------------- input sets
def recorded_commands():
    doc = json.loads((ROOT / "prototype" / "data" / "scripted_run.json").read_text())
    return [{f: int(e[f]) for f in FIELDS} for e in doc["commands"]]


def passive_commands():
    return [{f: 0 for f in FIELDS} for _ in range(4000)]


def synthetic_commands(n=2000, seed=0x2026_1022):
    """Deterministic pseudo-random play: movement, attacks and jumps."""
    out, state = [], seed
    for i in range(n):
        state ^= (state << 13) & 0xFFFFFFFF
        state ^= state >> 17
        state ^= (state << 5) & 0xFFFFFFFF
        state &= 0xFFFFFFFF
        r = state
        out.append({
            "move_x": (1 if r & 1 else -1) if (r >> 1) % 5 else 0,
            "move_z": (1 if r & 2 else -1) if (r >> 3) % 4 else 0,
            "jump": int((r >> 5) % 47 == 0),
            "punch": int((r >> 7) % 9 == 0),
            "kick": int((r >> 9) % 17 == 0),
        })
    return out


# --------------------------------------------------------------- python side
def python_frames(rows):
    game = Game()
    game.start()
    frames = []
    for row in rows:
        if game.state != Game.PLAY:
            break
        game.update(Command(**{f: row[f] for f in FIELDS}))
        frames.append(_dump(game))
    return frames


def _fighter(f):
    return {
        "id": f.id, "hp": f.hp, "x": f.wx, "y": f.wy, "z": f.wz,
        "vx": f.body.vx, "vy": f.body.vy, "vz": f.body.vz,
        "grounded": f.grounded, "facing": f.facing, "hitstun": f.hitstun,
        "iframes": f.iframes, "dead": f.dead, "death_timer": f.death_timer,
        "attack": f"{f.attack.name}:{f.attack.frame}" if f.attack else None,
        "cooldown": f.attack_cooldown,
    }


def _dump(game):
    return {
        "frame": game.frame, "state": game.state, "kills": game.kills,
        "wave": game.wave_index, "cam_x": game.cam_x, "hitstop": game.hitstop,
        "shake": game.shake, "outcome_timer": game.outcome_timer,
        "effects": len(game.effects),
        "player": _fighter(game.player),
        "enemies": [_fighter(e) for e in game.enemies],
    }


# --------------------------------------------------------------- node side
def js_frames(rows):
    if NODE is None:
        raise RuntimeError("node is not installed")
    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as fh:
        json.dump({"commands": rows}, fh)
        path = fh.name
    try:
        proc = subprocess.run([NODE, str(HARNESS), path], capture_output=True, text=True,
                              timeout=300)
        if proc.returncode != 0:
            raise RuntimeError(f"node harness failed: {proc.stderr[-2000:]}")
        return json.loads(proc.stdout)
    finally:
        Path(path).unlink(missing_ok=True)


# --------------------------------------------------------------- comparison
def compare(label, rows):
    py = python_frames(rows)
    js = js_frames(rows)
    if len(py) != len(js):
        return {"label": label, "frames_py": len(py), "frames_js": len(js),
                "ok": False, "first_mismatch": {"reason": "frame count differs"}}
    for i, (a, b) in enumerate(zip(py, js)):
        if a != b:
            diff = {k: (a.get(k), b.get(k)) for k in a if a.get(k) != b.get(k)}
            return {"label": label, "frames_py": len(py), "frames_js": len(js),
                    "ok": False, "first_mismatch": {"frame_index": i,
                                                    "python": a, "js": b, "diff": diff}}
    final = py[-1] if py else {}
    return {"label": label, "frames_py": len(py), "frames_js": len(js), "ok": True,
            "final_state": final.get("state"), "final_frame": final.get("frame"),
            "kills": final.get("kills"),
            "player_hp": final.get("player", {}).get("hp")}


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true", help="print the report as JSON")
    args = ap.parse_args(argv)

    if NODE is None:
        print("node is not installed: cannot run the browser port for comparison")
        return 3

    runs = [
        ("recorded 875-frame encounter", recorded_commands()),
        ("passive run (no input)", passive_commands()),
        ("synthetic 2,000-frame run", synthetic_commands()),
    ]
    reports = [compare(label, rows) for label, rows in runs]

    if args.json:
        print(json.dumps(reports, indent=2))
    else:
        for r in reports:
            status = "MATCH" if r["ok"] else "MISMATCH"
            print(f"{r['label']:32s} {status}  frames={r['frames_py']:5d}"
                  + (f"  -> {r['final_state']}@{r['final_frame']} "
                     f"hp={r['player_hp']} kills={r['kills']}" if r["ok"] else ""))
        if not all(r["ok"] for r in reports):
            for r in reports:
                if not r["ok"]:
                    print("\nfirst mismatch:", json.dumps(r["first_mismatch"], indent=2)[:4000])

    return 0 if all(r["ok"] for r in reports) else 1


if __name__ == "__main__":
    raise SystemExit(main())
