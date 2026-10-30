#!/usr/bin/env python3
"""wanprompt.py — write prompts the way Wan 2 expects them, and prove it.

Source of truth (read from the official repos, 2026-10-30):

  Wan-Video/Wan2.2  wan/utils/system_prompt.py :: I2V_A14B_EN_SYS_PROMPT
  Wan-Video/Wan2.1  wan/utils/prompt_extend.py  (LM_EN_SYS_PROMPT)

The I2V system prompt says, verbatim:

    "Focus on dynamic content in the video description and avoid adding static
     scene descriptions. If the user's input already describes elements visible in
     the image, remove those static descriptions."
    "Limit the rewritten prompt to 100 words or less."
    "Retain and emphasize descriptions of camera movements, such as 'the camera
     pans up', 'the camera moves from left to right'."
    "Your rewritten video description should retain the dynamic parts ... focusing
     on the main subject's actions."

Our prompts did the opposite: 90-110 words of place, costume, lighting and style
tags — every one of them already inside the input frame. The model therefore had
nothing left to animate and re-painted the picture instead. That is the "jumbled"
output: it was not a camera problem, it was a prompt-shape problem.

    python3 studio/wanprompt.py check "..."        # score one prompt
    python3 studio/wanprompt.py fix   "..."        # coerce to Wan shape
    python3 studio/wanprompt.py audit films/short16/gen_jobs_min1.json
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

MAX_WORDS = 100
SWEET = (12, 60)

# Words that describe what is already in the still. Each one is a wasted token and,
# worse, a second description of the frame the model has to reconcile.
STATIC = {
    "cel", "animation", "anime", "flat", "colour", "color", "fields", "field",
    "shading", "shaded", "line", "lineart", "art", "background", "painting",
    "photographic", "photorealism", "cgi", "3d", "render", "texture", "textured",
    "gradient", "brush", "style", "look", "palette", "detail", "detailed",
    "quality", "8k", "4k", "watermark", "subtitle", "bokeh", "depth",
}
CAMERA = {
    "pushes", "push", "pulls", "pull", "pans", "pan", "tilts", "tilt", "tracks",
    "track", "dollies", "dolly", "cranes", "crane", "orbits", "orbit", "rises",
    "holds", "static", "steady", "follows", "follow", "zooms", "zoom", "moves",
    "rotates", "shakes", "camera",
}
ACTIONS = {
    "walks", "walk", "steps", "runs", "turns", "turning", "blinks", "looks",
    "raises", "lowers", "lifts", "opens", "closes", "swings", "swaying", "sways",
    "breathes", "speaks", "smiles", "nods", "reaches", "grips", "tightens",
    "falls", "drips", "flickers", "drifts", "settles", "enters", "leaves",
    "relax", "tighten", "swing", "splash", "lift", "stop", "blink", "shift",
}


def _hit(w: list[str], vocab: set[str]) -> list[str]:
    """Match on a 4-character stem so 'tightens/tightened/tightening' all count."""
    out = set()
    for x in w:
        for v in vocab:
            if x == v or (len(x) > 4 and x.startswith(v[:4]) and v[:4] == x[:4]):
                out.add(v)
                break
    return sorted(out)


def words(p: str) -> list[str]:
    return re.findall(r"[a-z']+", p.lower())


def check(prompt: str) -> dict:
    """Score a prompt against the Wan I2V contract."""
    p = prompt.strip()
    w = words(p)
    n = len(w)
    static_hits = _hit(w, STATIC)
    cam_hits = _hit(w, CAMERA)
    act_hits = _hit(w, ACTIONS)
    brackets = len(re.findall(r"\[[^\]]+\]", p))
    # static leak = share of the prompt spent re-describing the frame
    leak = round(100 * sum(w.count(x) for x in STATIC) / max(n, 1))
    problems, advice = [], []
    if n > MAX_WORDS:
        problems.append(f"{n} words > {MAX_WORDS} (Wan truncates at 100)")
    if leak > 12:
        problems.append(f"{leak}% static words — those things are already in the still")
    if not cam_hits:
        problems.append("no camera clause (Wan wants 'the camera pushes in')")
    if not act_hits:
        problems.append("no subject action — the model has nothing to move")
    if brackets:
        problems.append(f"{brackets} bracketed labels — Wan wants prose, not a form")
    if n > 0 and n < SWEET[0]:
        # advice, not a breach: Wan's own examples include ten-word prompts
        advice.append(f"only {n} words — thin, one more action beat would help")
    return {
        "words": n, "static_pct": leak, "static": static_hits, "camera": cam_hits,
        "actions": act_hits, "brackets": brackets,
        "ok": not problems, "problems": problems, "advice": advice,
    }


def fix(prompt: str, camera: str | None = None, action: str | None = None) -> str:
    """Coerce a prompt into Wan shape: drop the tag scaffolding, drop sentences that
    describe the still, keep whatever motion remains, and put the camera first."""
    text = prompt
    text = re.sub(r"\[(shot|look|place|subject|end|negative|style|camera)\]\s*", "", text, flags=re.I)
    text = re.sub(r"\bno (text|subtitle|watermark|photorealism|cgi|3d render|warping|morphing|camera shake)[^,\n]*", "", text, flags=re.I)
    sents = [s.strip(" .") for s in re.split(r"[.\n]", text) if s.strip(" .")]
    keep = []
    for s in sents:
        ws = words(s)
        if not ws:
            continue
        leak = sum(1 for x in ws if x in STATIC) / len(ws)
        if leak > 0.25:                      # this sentence is a style/static block
            continue
        keep.append(s)
    body = ". ".join(keep).strip(" .")
    parts = []
    if camera:
        parts.append(camera.rstrip("."))
    if body:
        parts.append(body)
    if action and action.lower() not in body.lower():
        parts.append(action.rstrip("."))
    out = ". ".join(parts)
    out = re.sub(r"\s+", " ", out).strip(" .") + "."
    if len(words(out)) > MAX_WORDS:          # keep the tail, it usually holds the motion
        out = " ".join(out.split()[-MAX_WORDS:]).capitalize() + "."
    return out


def cmd_check(a) -> int:
    for p in (a.prompt or [sys.stdin.read()]):
        r = check(p)
        print(f"{'OK ' if r['ok'] else 'BAD'} {r['words']:>3}w  static {r['static_pct']:>2}%  "
              f"cam {','.join(r['camera']) or '-'}  act {','.join(r['actions']) or '-'}")
        for x in r["problems"]:
            print(f"    - {x}")
    return 0


def cmd_fix(a) -> int:
    out = fix(a.prompt, a.camera, a.action)
    print(out)
    r = check(out)
    print(f"\n{'OK' if r['ok'] else 'still bad'}: {r['words']}w static {r['static_pct']}%",
          file=sys.stderr)
    return 0


def cmd_audit(a) -> int:
    """Score every prompt in a job file. Used before any batch: a prompt that fails
    here is a prompt that will repaint the frame instead of animating it."""
    jobs = json.loads(Path(a.file).read_text(encoding="utf-8"))
    shots = jobs.get("shots", jobs)
    bad = 0
    print(f"{'id':18s} {'words':>5s} {'static':>7s} {'cam':>4s} {'act':>4s}  verdict")
    for s in shots:
        r = check(s.get("prompt", ""))
        if not r["ok"]:
            bad += 1
        print(f"{s['id']:18s} {r['words']:>5d} {r['static_pct']:>6d}% "
              f"{len(r['camera']):>4d} {len(r['actions']):>4d}  "
              f"{'ok' if r['ok'] else '; '.join(r['problems'])[:60]}")
    print(f"\n{bad}/{len(shots)} prompts break the Wan I2V contract")
    return 1 if bad else 0


def main() -> int:
    ap = argparse.ArgumentParser(prog="wanprompt", description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("check"); p.add_argument("prompt", nargs="?"); p.set_defaults(fn=cmd_check)
    p = sub.add_parser("fix"); p.add_argument("prompt")
    p.add_argument("--camera"); p.add_argument("--action"); p.set_defaults(fn=cmd_fix)
    p = sub.add_parser("audit"); p.add_argument("file"); p.set_defaults(fn=cmd_audit)
    a = ap.parse_args()
    return a.fn(a)


if __name__ == "__main__":
    raise SystemExit(main())
