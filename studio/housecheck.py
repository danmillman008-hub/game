#!/usr/bin/env python3
"""housecheck — refuse a shot before it is paid for.

The house style is not taste, it is the set of shot shapes this model has actually
held for four seconds. It was measured in twelve takes (2026-10-30), and every rule
below points at the take that produced it. `studio/knowledge/method/HOUSE_STYLE.md`
carries the table; this file is the gate.

    python3 studio/housecheck.py films/short16/gen_jobs_silent20.json
    python3 studio/housecheck.py jobs/*.json --json
    python3 studio/housecheck.py --style          # where the rules are written down

Exit 1 if any shot breaks a rule, 0 if it is clean (warnings alone do not fail).
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STYLE = ROOT / "studio" / "knowledge" / "method" / "HOUSE_STYLE.md"

# --------------------------------------------------------------- the evidence --
# Anchors that lost takes. Nothing is banned for looking wrong: each one is here
# because it produced a specific artefact, named.
BLOCKED = {
    "films/short16/clips_gen/a7_ots_src.png":
        "a hand alone: take 1 redrew it as a fist, take 2 opened the fingers and let go",
    "films/short16/clips_gen/a8_arrival_wide_src.png":
        "figure sliced by the doorway: the model invented a new person, a lantern and rebuilt the arch",
    "films/short16/clips_gen/a2_cobbles_high_last.png":
        "legs cut off at the frame edge: it completed them into a walking woman",
    "films/short16/clips_gen/a5_knight_mcu_src.png":
        "labelled MCU but it is a wide: the stone wall crept upward between frames",
}

# Anchors that held their shape, with the take count they held for.
APPROVED = {
    "films/anime_ten/art/art_knight_a1_fN.png": "her, medium, centred — 1/1 clean",
    "films/anime_ten/art/art_plain2_fN.png": "road, walker small and centred — 1/1 clean",
    "films/anime_ten/art/art_plain_a1_fN.png": "road, walker far — 1/1 clean",
    "films/short16/clips_gen/a6_gauntlet_src.png": "her, medium close-up — 1/1 clean",
}

# A pose change is the single most reliable way to make the model repaint the frame.
POSE_VERBS = re.compile(
    r"\b(arrives?|arriving|stops?|stopping|turns?|turning|raises?|lowers?|lifts?|"
    r"opens?|closes?|tightens?|grips?|grabs?|releases?|enters?|leaves?|"
    r"sits?|stands? up|reaches?|picks? up|draws?|appears?|vanishes|starts? to|"
    r"begins? to (?:walk|move))\b", re.I)

# A gait that does not change the pose ("one step after another") is fine; a walk
# that ends somewhere ("walks across, walks to") is the thing that rebuilds the frame.
WALK_TO = re.compile(r"\bwalks?\b[^.]{0,25}?\b(to|toward|towards|across|into|out of|up to)\b", re.I)

# Naming a prop gives the model permission to animate, duplicate or re-invent it.
PROP_NOUNS = re.compile(r"\b(spear|spears|shaft|sword|blade|weapon|gate|gates|door|doors)\b", re.I)

CAMERA_MOVE = re.compile(
    r"\b(push(?:es)? in|pans?|tracks?|doll(?:y|ies)|zoom(?:s)?|cranes?|orbits?|"
    r"tilts?|moves? in|follows?|handheld|shakes?)\b", re.I)

NEGATIVE_BLOCK = re.compile(r"\bno\s+(text|cgi|watermark|photorealism|blur|subtitle)", re.I)

LOCKED = re.compile(r"^\s*the camera holds still\b", re.I)

# Walking away from a static camera survived twice — but only when the walker is
# small in the frame, which is what these two anchors are.
WALK_OK = {"films/anime_ten/art/art_plain2_fN.png", "films/anime_ten/art/art_plain_a1_fN.png"}

WORD_BAND = (12, 30)


def sentences(text: str) -> list[str]:
    return [s for s in re.split(r"(?<=[.!?])\s+", text.strip()) if s]


def check_shot(shot: dict) -> tuple[list[str], list[str]]:
    """Return (errors, warnings) for one shot."""
    err: list[str] = []
    warn: list[str] = []
    path = shot.get("still") or ""

    if shot.get("still_from_clip"):
        err.append("S1 chained from a clip — identity dies after the first link; start "
                   "every shot from a still")
    if not path:
        err.append("S2 no `still`: a shot with no anchor has no first frame")
    elif not (ROOT / path).exists():
        err.append(f"S2 anchor does not exist: {path}")
    elif path in BLOCKED:
        err.append(f"S3 blocked anchor — {BLOCKED[path]}")
    elif path not in APPROVED:
        warn.append("S3 unproven anchor: tolerated, but nothing here has held for 4 s yet")

    text = shot.get("prompt", "")
    words = len(text.split())
    lo, hi = WORD_BAND
    if words < lo or words > hi:
        err.append(f"S7 {words} words — house band is {lo}–{hi}")

    if "[" in text or "]" in text:
        err.append("S9 bracket tags are T2V syntax, not I2V")

    if text and not LOCKED.match(text):
        err.append("S4 the prompt must open with 'The camera holds still.' — every move "
                   "we asked for was either ignored or rebuilt the frame")
    if CAMERA_MOVE.search(text):
        err.append(f"S4 camera move: '{CAMERA_MOVE.search(text).group(0)}'")

    # "does not turn" is a stillness, not a pose change
    poses = sorted({m.group(0).lower() for m in POSE_VERBS.finditer(text)
                    if not re.search(r"\b(not|never)\s+$", text[max(0, m.start() - 8):m.start()])})
    if poses:
        err.append("S5 pose change: " + ", ".join(poses) + " — the frame gets repainted")
    if "walk" in text.lower() and path not in WALK_OK:
        err.append("S5 walking only survives on the two road anchors (walker small and "
                   "centred); elsewhere the body is rebuilt")
    if WALK_TO.search(text):
        err.append("S5 a walk that ends somewhere — that is an arrival, and arrivals "
                   "come back as a different person")

    props = sorted({m.group(0).lower() for m in PROP_NOUNS.finditer(text)})
    if props:
        err.append("S6 names a prop: " + ", ".join(props) + " — a prop that is named moves")

    if NEGATIVE_BLOCK.search(text):
        err.append("S8 negative block: this endpoint has no negativePrompt field")

    body = sentences(text)
    if len(body) > 3:
        err.append(f"S5 {len(body)} sentences — one camera clause plus at most two motions")

    return err, warn


def main() -> int:
    ap = argparse.ArgumentParser(prog="housecheck", description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("jobs", nargs="*", help="job files to check")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--style", action="store_true", help="print the style document path")
    a = ap.parse_args()

    if a.style:
        print(STYLE.relative_to(ROOT))
        return 0
    if not a.jobs:
        ap.error("give at least one job file (or --style)")

    bad = 0
    results = []
    for f in a.jobs:
        data = json.loads(Path(f).read_text(encoding="utf-8"))
        shots = data["shots"]
        file_errors = 0
        if a.json:
            results.append({"file": f, "shots": []})
        else:
            print(f"\n{f} — {len(shots)} shot(s)")
        for s in shots:
            err, warn = check_shot(s)
            file_errors += len(err)
            if a.json:
                results[-1]["shots"].append({"id": s.get("id"), "errors": err, "warnings": warn})
            else:
                mark = "FAIL" if err else ("warn" if warn else "ok  ")
                print(f"  {mark} {s.get('id','?'):20s} {len(s.get('prompt','').split()):2d} words")
                for e in err:
                    print(f"        - {e}")
                for w in warn:
                    print(f"        ~ {w}")
        bad += file_errors
        if not a.json and not file_errors:
            print("        every shot is a shape this model has held")

    if a.json:
        print(json.dumps({"files": results, "errors": bad}, indent=2))
    else:
        print(f"\n{bad} rule break(s) across {len(a.jobs)} file(s)")
        if bad:
            print(f"rules and the takes behind them: {STYLE.relative_to(ROOT)}")
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())
