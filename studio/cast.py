#!/usr/bin/env python3
"""cast — keep one character looking like one character.

The problem, measured on our own output: every anchor in the anime line is painted
from a *blank canvas*, so each one invents a new face. The left guard in the two-shot
and the left guard in the close-up are two different men — not because the prompt was
vague, but because nothing carried the identity between them.

The technique was already in this repo and was not being used: `mivi_compose` takes
**two reference images plus a prompt** and returns one new image (`stitchImage`). The
old film (`films/before_leaving`) built every close-up that way — `s04_raha_cu` from
`master_wide.png` + a crop of her. This file is that pipeline, with the vocabulary from
`methodology/20-realistic-character-consistency.md` in lanshu-awesome-ai-video-kit:

    character sheet   one master still of the character, then multi-angle views of it
    omni reference    compose(master, pose/scene ref) -> the same face, new framing
    (face swap)       NOT available to us: mivi_swapface only swaps in preset template
                      faces (ids 1000-1010, 1100, 1200, 2001, 2002), not our character

    python3 studio/cast.py sheet  --master FILM.png --out CAST.png
    python3 studio/cast.py still  --master CAST.png --pose POSE.png --prompt "..." --out S.png
    python3 studio/cast.py ab-test                    # the A/B written up in CONSISTENCY_PLAYBOOK

`still` refuses to run without a master: a close-up with no master is exactly the
defect this file exists to prevent.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "bridge"))
import mivi_mcp as M  # noqa: E402


def compose(ref_a: str, ref_b: str, prompt: str, out: str) -> dict:
    for p in (ref_a, ref_b):
        if not (ROOT / p).exists():
            raise SystemExit(f"reference does not exist: {p}")
    return M.t_compose({"images": [str(ROOT / ref_a), str(ROOT / ref_b)],
                        "prompt": prompt, "out": str(ROOT / out)})


SHEET_PROMPT = (
    "Character sheet of the same person as the first image, three by three grid, "
    "clean pale background: front view, left profile, right profile, back of the head, "
    "medium shot, full body, and two expression studies. Identical face, identical "
    "armour and helmet, identical colours on every panel. 2D cel animation, anime key "
    "art, flat colour fields, constant line width."
)


def cmd_sheet(a) -> int:
    out = a.out or "films/short16/clips_gen/cast_sheet.png"
    r = compose(a.master, a.master, a.prompt or SHEET_PROMPT, out)
    print(json.dumps(r, ensure_ascii=False))
    return 0 if r.get("image_url") else 1


def cmd_still(a) -> int:
    """One new framing of an established character."""
    pose_ref = a.pose
    r = compose(a.master, pose_ref, a.prompt, a.out)
    print(json.dumps(r, ensure_ascii=False))
    return 0 if r.get("image_url") else 1


# ------------------------------------------------------------------ A/B test ---
AB = {
    "id": "ab_left_guard",
    # identity comes from the two-shot; the close-up framing comes from the old anchor
    "master": "films/short16/clips_gen/w_two_src.png",
    "pose": "films/short16/clips_gen/c_left_src.png",
    "prompt": ("Close-up of the guard on the left from the first image, the same young man, "
               "the same pale grey lamellar armour and the same plain helmet, standing at "
               "the castle gate at night in falling snow, warm lantern light on one cheek. "
               "2D cel animation, anime key art, flat colour fields, constant line width."),
    "out": "films/short16/clips_gen/ab_left_guard.png",
}


def cmd_ab(a) -> int:
    out = AB["out"]
    print(f"master {AB['master']}\npose   {AB['pose']}", flush=True)
    r = compose(AB["master"], AB["pose"], AB["prompt"], out)
    print(json.dumps(r, ensure_ascii=False), flush=True)
    if not r.get("image_url"):
        return 1
    res = {"compose": r, "master": AB["master"], "pose": AB["pose"], "out": out,
           "baseline": "films/short16/clips_gen/c_left_src.png"}
    Path("films/short16/clips_gen/ab_left_guard.json").write_text(
        json.dumps(res, indent=2, ensure_ascii=False), encoding="utf-8")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(prog="cast", description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("sheet"); p.add_argument("--master", required=True)
    p.add_argument("--prompt"); p.add_argument("--out"); p.set_defaults(fn=cmd_sheet)
    p = sub.add_parser("still"); p.add_argument("--master", required=True)
    p.add_argument("--pose", required=True); p.add_argument("--prompt", required=True)
    p.add_argument("--out", required=True); p.set_defaults(fn=cmd_still)
    sub.add_parser("ab-test").set_defaults(fn=cmd_ab)
    a = ap.parse_args()
    return a.fn(a)


if __name__ == "__main__":
    raise SystemExit(main())
