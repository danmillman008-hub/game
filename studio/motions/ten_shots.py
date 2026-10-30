#!/usr/bin/env python3
"""ten_shots.py — turn 80 story beats into ~160 shot specs with studio coverage rules.

A ten-minute film is not one decision repeated 150 times; it is a coverage system.
This module encodes the rules that make a cut feel directed rather than assembled:

  * every beat gets a PAIR — the action, then the reaction. That is how a scene is
    covered, and it is why the shot count roughly doubles against the beat count.
  * shot sizes walk a pattern and never repeat three times in a row (measured rule
    from video-shotcraft: the eye reads three identical sizes as a slideshow).
  * the angle rotates through eye / high / low / dutch, and a Dutch shot is never
    followed by another Dutch shot — two tilted frames in a row read as an error.
  * each scene opens wide and closes on a hold; holds are 6 s, coverage is 4 s.
  * no character appears in a scene they are not listed in.

Output is two files:
    films/anime_ten/shots.json     the shot list (id, scene, beat, size, angle, char)
    studio/motions/ten_all_specs.json   specs the motion bank can compose

    python3 studio/motions/ten_shots.py
    python3 studio/motions/ten_shots.py --check    # verify the coverage rules
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
FILM = ROOT / "films" / "anime_ten"

SIZES = ["ews", "ws", "ms", "mcu", "cu", "ms", "ws"]
ANGLES = ["eye", "high", "low", "dutch", "eye", "low"]
# framing recipe per angle: (scale, anchor, tilt, crop_head, darken)
FRAMING = {
    "eye":   (0.80, [0.50, 0.99], 0, None, 0.18),
    "high":  (0.45, [0.56, 0.90], 2, None, 0.22),
    "low":   (0.95, [0.44, 1.02], -2, None, 0.10),
    "dutch": (0.85, [0.48, 0.98], -14, None, 0.15),
    "mcu":   (1.45, [0.44, 0.99], 0, 0.44, 0.20),
    "cu":    (2.10, [0.46, 0.99], 0, 0.34, 0.20),
}
PLATE = {"storm": "storm", "plain": "storm", "wall": "storm", "gate": "city",
         "gatehouse": "room", "room": "room", "dawn": "storm"}
SUBJECT = {
    "rin": ["stand_wind_he", "slow_head_turn", "shoulders_set"],
    "sera": ["stand_wind", "slow_head_turn", "lift_blade"],
    "mira": ["shoulders_set", "stand_wind", "slow_head_turn"],
    "kae": ["lift_blade", "slow_head_turn", "stand_wind"],
    "yuna": ["shoulders_set", "single_blink", "slow_head_turn"],
}


def plate_for(place: str) -> str:
    for key, plate in PLATE.items():
        if key in place:
            return plate
    return "storm"


def build(story: dict) -> list[dict]:
    shots = []
    n = 0
    for sc in story["scenes"]:
        chars = sc["chars"]
        for b, beat in enumerate(sc["beats"]):
            for part in (0, 1):                    # action, then reaction
                n += 1
                size = SIZES[(b + part) % len(SIZES)]
                angle = ANGLES[(b + part * 2) % len(ANGLES)]
                if part == 0 and b == 0:
                    size, angle = "ews", "eye"          # every scene opens wide
                ch = chars[(b + part) % len(chars)]
                scale, anchor, tilt, crop, dark = FRAMING[
                    "mcu" if size in ("ms", "mcu") and part else
                    "cu" if size == "cu" else angle]
                shots.append({
                    "id": f"s{sc['n']:02d}_{n:03d}",
                    "scene": sc["n"], "beat": b + 1, "part": "action" if part == 0 else "reaction",
                    "size": size, "angle": angle, "char": ch,
                    "beat_text": beat,
                    "hold_s": 6.0 if (b == len(sc["beats"]) - 1 and part == 1) else 4.0,
                    "still_spec": {"char": ch, "plate": plate_for(sc["place"]),
                                   "scale": scale, "anchor": anchor, "tilt": tilt,
                                   "crop_head": crop, "darken": dark},
                    "subject": SUBJECT[ch][(b + part) % 3],
                })
    return shots


def specs(shots: list[dict], story: dict) -> list[dict]:
    place = {s["n"]: s["place"] for s in story["scenes"]}
    out = []
    for s in shots:
        out.append({
            "id": s["id"], "still_spec": s["still_spec"],
            "shot_size": {"ews": "ews", "ws": "ws", "ms": "ms", "mcu": "cu",
                          "cu": "ecu"}[s["size"]],
            "camera": "static_locked", "subject": s["subject"],
            "place": f"{place[s['scene']]} — {s['beat_text']}",
            "environment": "wires_still", "end_state": "the frame holds as it is",
            "look": "cel_closeup" if s["size"] in ("mcu", "cu") else "cel_night",
            "attempts": 2,
        })
    return out


def check(shots: list[dict]) -> list[str]:
    bad = []
    for i in range(len(shots) - 2):
        trio = [shots[i + k]["size"] for k in range(3)]
        if trio[0] == trio[1] == trio[2]:
            bad.append(f"{shots[i]['id']}: same size three times ({trio[0]})")
    for i in range(len(shots) - 1):
        if shots[i]["angle"] == shots[i + 1]["angle"] == "dutch":
            bad.append(f"{shots[i]['id']}: two Dutch shots in a row")
    ids = [s["id"] for s in shots]
    if len(ids) != len(set(ids)):
        bad.append("duplicate shot ids")
    chars = {s["scene"]: set() for s in shots}
    for s in shots:
        chars[s["scene"]].add(s["char"])
    return bad


def main() -> int:
    ap = argparse.ArgumentParser(prog="ten_shots", description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()

    story = json.loads((FILM / "story.json").read_text(encoding="utf-8"))
    shots = build(story)
    total = sum(s["hold_s"] for s in shots)
    problems = check(shots)

    print(f"{len(shots)} shots · {total / 60:.1f} min of picture · {len(story['scenes'])} scenes")
    for sc in story["scenes"]:
        rows = [s for s in shots if s["scene"] == sc["n"]]
        print(f"  scene {sc['n']} {sc['title']:16s} {len(rows):3d} shots "
              f"{sum(r['hold_s'] for r in rows) / 60:.1f} min")
    if problems:
        print("\ncoverage problems:")
        for p in problems:
            print(f"  ! {p}")
    else:
        print("\ncoverage rules: OK (no size 3x in a row, no double Dutch)")

    if not a.check:
        (FILM / "shots.json").write_text(json.dumps(shots, ensure_ascii=False, indent=2),
                                         encoding="utf-8")
        out = ROOT / "studio/motions/ten_all_specs.json"
        out.write_text(json.dumps(specs(shots, story), ensure_ascii=False, indent=2),
                       encoding="utf-8")
        print(f"\n-> films/anime_ten/shots.json\n-> {out.relative_to(ROOT)}")
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main())
