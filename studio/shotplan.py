#!/usr/bin/env python3
"""shotplan.py — plan a scene the way the model actually behaves.

Two rules came out of the measurements (studio/motions/CONSISTENCY_AND_SPEED.md):

  1. **Anchor, don't chain.** Every extra link in a chain is a lossy re-encode of a
     character's face. Identity survives 2-3 links, not 15. So a scene is planned as
     a set of shots that start from a small number of approved stills ("anchors"),
     and a chain is only used when the camera has to travel continuously.

  2. **One camera sentence and one action sentence.** Wan I2V wants motion, not a
     description of the frame it was given.

A scene file:

    {
      "name": "gate",
      "anchors": {"gate": "films/anime_ten/art/art_k2_fN.png",
                  "face": "films/short16/clips_gen/art_knight_last.png"},
      "shots": [
        {"id": "s01", "anchor": "gate", "size": "wide",
         "camera": "The camera pushes in slowly toward the door.",
         "action": "Rain falls through the lantern light."},
        {"id": "s02", "chain_from": "s01",
         "camera": "The camera keeps moving.",
         "action": "She lowers her spear until it touches the stones."}
      ]
    }

    python3 studio/shotplan.py plan studio/motions/scenes/gate.json \
            --out films/short16/gen_jobs_gate.json
    python3 studio/shotplan.py plan ... --out ... --parallel 4
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import wanprompt  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
MAX_CHAIN = 2


def build(scene: dict) -> tuple[list[dict], list[str]]:
    anchors = scene.get("anchors", {})
    shots = scene["shots"]
    notes: list[str] = []
    out: list[dict] = []
    for s in shots:
        parts = [s.get("camera", "").strip(), s.get("action", "").strip()]
        prompt = " ".join(p for p in parts if p)
        if s.get("size") and s["size"] not in prompt.lower():
            prompt = f"{s['size'].capitalize()} shot. {prompt}"
        job = {"id": s["id"], "prompt": prompt, "attempts": int(s.get("attempts", 1)),
               "model": s.get("model", "mivi-gx-720p"), "quality": int(s.get("quality", 2))}
        if s.get("chain_from"):
            job["still_from_clip"] = f"films/short16/clips_gen/{s['chain_from']}_a1.mp4"
        else:
            a = anchors.get(s.get("anchor", ""))
            if not a:
                notes.append(f"{s['id']}: no anchor '{s.get('anchor')}' — shot cannot start")
                a = ""
            job["still"] = a
        out.append(job)
    return out, notes


def chain_depths(shots: list[dict]) -> dict[str, int]:
    by_id = {s["id"]: s for s in shots}
    memo: dict[str, int] = {}

    def d(i: str, seen=()) -> int:
        if i in memo:
            return memo[i]
        src = by_id[i].get("chain_from")
        memo[i] = 0 if not src or src not in by_id or src in seen else 1 + d(src, seen + (i,))
        return memo[i]

    for s in shots:
        d(s["id"])
    return memo


def cmd_plan(a) -> int:
    scene = json.loads(Path(a.scene).read_text(encoding="utf-8"))
    jobs, notes = build(scene)
    depths = chain_depths(scene["shots"])
    deepest = max(depths.values()) if depths else 0

    print(f"scene {scene.get('name', '?')}: {len(jobs)} shots, "
          f"{sum(1 for j in jobs if 'still' in j)} anchored, "
          f"{sum(1 for j in jobs if 'still_from_clip' in j)} chained, "
          f"longest chain {deepest}")
    for n in notes:
        print(f"  ! {n}")
    bad = 0
    for j in jobs:
        r = wanprompt.check(j["prompt"])
        if not r["ok"]:
            bad += 1
            print(f"  ! {j['id']}: {'; '.join(r['problems'])}")
    if deepest > MAX_CHAIN:
        print(f"  ! longest chain is {deepest} — re-anchor: identity drifts past "
              f"{MAX_CHAIN} links")

    waves: dict[int, list[str]] = {}
    for j in jobs:
        waves.setdefault(depths[j["id"]], []).append(j["id"])
    est = sum(180.0 * max(1, -(-len(w) // max(a.parallel, 1))) for w in waves.values())
    print(f"  waves: " + " | ".join(f"{d}:{len(v)}" for d, v in sorted(waves.items())))
    print(f"  est. wall clock ~{est/60:.0f} min at parallel={a.parallel} "
          f"(serial ~{180*len(jobs)/60:.0f} min)")

    if a.out:
        Path(a.out).write_text(json.dumps({"shots": jobs}, indent=2, ensure_ascii=False),
                               encoding="utf-8")
        print(f"  -> {a.out}")
    return 0 if bad == 0 and deepest <= MAX_CHAIN and not notes else 1


def main() -> int:
    ap = argparse.ArgumentParser(prog="shotplan", description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("plan")
    p.add_argument("scene")
    p.add_argument("--out")
    p.add_argument("--parallel", type=int, default=4)
    p.set_defaults(fn=cmd_plan)
    a = ap.parse_args()
    return a.fn(a)


if __name__ == "__main__":
    raise SystemExit(main())
