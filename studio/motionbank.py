#!/usr/bin/env python3
"""motionbank — a machine-usable bank of camera moves, actions and phrasings.

Why: every bad clip we produced had a prompt problem, not a model problem —
several camera moves stacked in one sentence, "subtle sway" with no number,
emotions written as adjectives. This bank makes the good phrasing the default:
you pick ids, it writes the sentence, and it refuses to emit a prompt that
breaks the rules.

Verbs
  list                     what is in the bank (counts per category)
  show <id>                one entry in full
  search <text>            find by id/fa/en
  compose <spec.json>      spec -> prompt (with rule checks)
  lint "<text>"            check an existing prompt against the rules
  jobs <spec.json>         spec -> gen_jobs.json for studio/mivi_shot.py
  shots <bank ids...>      quick prompt from ids on the command line

A spec is a JSON list of shots; every field is a bank id or free text:
  [{"id": "h1", "still": "…png", "attempts": 1,
    "shot_size": "ws", "camera": "static_locked",
    "subject": "rise_from_bench", "place": "rainy bus stop at night, wet asphalt",
    "micro": ["breath_visible"], "environment": "rain_lamp",
    "end_state": "she is standing, still holding his gaze",
    "look": "wide_night", "negative": "static"}]
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BANK_PATH = Path(__file__).resolve().parent / "motions" / "bank.json"

CAMERA_WORDS = ["push in", "push-in", "pushes in", "push", "dolly", "pan", "tilt",
                "orbit", "crane", "track", "zoom", "handheld", "follow", "re-frame", "reframe"]
VAGUE = ["subtle", "slight", "slightly", "gentle", "gently", "natural", "smooth",
         "slowly", "softly", "a little", "some"]


def load(path: str | Path | None = None) -> dict:
    """Default bank is the live-action one; `--bank` selects another (e.g. anime_bank.json)."""
    return json.loads(Path(path or BANK_PATH).read_text(encoding="utf-8"))


def index(bank: dict) -> dict:
    idx = {}
    for cat, val in bank.items():
        if isinstance(val, list):
            for e in val:
                if isinstance(e, dict) and "id" in e:
                    idx[e["id"]] = {**e, "_cat": cat}
    return idx


def fmt(entry: dict, **kw) -> str:
    """Fill {placeholders} from default values and the caller's overrides."""
    text = entry.get("en", entry.get("body", ""))
    if isinstance(text, list):
        text = ", ".join(text)
    vals = dict(entry.get("default") or {})
    vals.update({k: v for k, v in kw.items() if v is not None})
    for k, v in vals.items():
        text = text.replace("{" + k + "}", str(v))
    return text


# ------------------------------------------------------------------ lint
def _strip_negations(low: str) -> str:
    """"no zoom, no pan, no handheld" is a *promise*, not a move — drop it."""
    low = re.sub(r"\b(no|without|never)\s+(zoom|pan|tilt|orbit|crane|track|handheld|dolly|"
                 r"reframe|reframing|drift|camera movement|movement)\b[^,.;]*", " ", low)
    return re.sub(r"\s+", " ", low)


def lint(text: str) -> dict:
    low = text.lower()
    issues = []
    scan = _strip_negations(low)

    # 1) one move
    moves = sorted({w for w in CAMERA_WORDS if w in scan})
    static = ("static" in low) or ("locked-off" in low) or ("locked off" in low)
    if len(moves) > 2:
        issues.append({"rule": "one_move", "level": "warn",
                       "msg": f"{len(moves)} camera terms at once: {moves}"})
    if not static and not moves:
        issues.append({"rule": "state_static", "level": "warn",
                       "msg": "no camera statement — the model will invent a drift"})
    if static and len(moves) > 1:
        issues.append({"rule": "state_static", "level": "warn",
                       "msg": "says static but also names moves"})

    # 2) vague magnitude
    vague_hits = [w for w in VAGUE if w in scan]
    has_number = bool(re.search(r"\d", text))
    if vague_hits and not has_number:
        issues.append({"rule": "micro_magnitude", "level": "warn",
                       "msg": f"vague motion words with no number: {vague_hits}"})

    # 3) zoom word for a physical move
    if "zoom" in scan:
        issues.append({"rule": "no_zoom_word", "level": "warn",
                       "msg": "uses 'zoom' — name dolly / push in / track instead"})

    # 4) several beats
    beats = len(re.findall(r"\bthen\b", low)) + len(re.findall(r"\bthereafter\b", low))
    if beats >= 2:
        issues.append({"rule": "one_beat", "level": "warn",
                       "msg": f"{beats} 'then' clauses — one beat per 4 s clip"})

    # 5) end state
    if "by the last frame" not in low and "by the end" not in low:
        issues.append({"rule": "end_state", "level": "warn",
                       "msg": "no end-state anchor"})

    # 6) negative
    if "no text" not in low:
        issues.append({"rule": "negative", "level": "warn",
                       "msg": "no negative block (text/subtitle)"})

    errors = [i for i in issues if i["level"] == "error"]
    return {"ok": not issues, "score": max(0, 100 - 12 * len(issues)),
            "issues": issues, "errors": errors}


# ------------------------------------------------------------------ compose
def compose(spec: dict, bank: dict | None = None) -> dict:
    bank = bank or load()
    idx = index(bank)
    def get(key, default=None):
        if not key:
            return default
        if isinstance(key, str) and key in idx:
            return idx[key]
        return {"id": None, "en": key, "_cat": "free"}

    shot = get(spec.get("shot_size"), {"en": "wide shot"})
    cam = get(spec.get("camera"), idx["static_locked"])
    subj = get(spec.get("subject"), {"en": ""})
    micro = spec.get("micro")
    micros = [get(m) for m in ([micro] if isinstance(micro, str) else (micro or []))]
    env = get(spec.get("environment"))
    look = get(spec.get("look"), idx.get("cine_night") or {"en": ""})

    neg_key = spec.get("negative") or ("static" if cam.get("kind") == "static" else "default")
    neg = bank["negative"].get(neg_key, bank["negative"]["default"]) \
        if neg_key in bank["negative"] else (neg_key if isinstance(neg_key, str) else bank["negative"]["default"])

    mag = spec.get("magnitude") or {}
    subj_txt = fmt(subj, **mag) if subj.get("en") else ""
    parts = []
    cam_txt = fmt(cam, **mag)
    parts.append(f"[shot] {fmt(shot)}, {cam_txt}")
    if subj_txt:
        parts.append(f"[subject] {subj_txt}")
    if spec.get("place"):
        parts.append(f"[place] {spec['place']}")
    motion_bits = [fmt(m, **mag) for m in micros if m.get("en")]
    if motion_bits:
        parts.append("[motion] " + "; ".join(motion_bits))
    if env and env.get("en"):
        parts.append(f"[environment] {fmt(env)}")
    if spec.get("end_state"):
        parts.append(f"[end] by the last frame: {spec['end_state']}")
    parts.append(f"[look] {fmt(look)}")
    parts.append(f"[negative] {neg}")

    prompt = "\n".join(parts)
    report = lint(prompt)
    return {"id": spec.get("id"), "prompt": prompt, "lint": report,
            "beats": subj.get("beats", 1),
            "camera_kind": cam.get("kind", "move")}


# ------------------------------------------------------------------ verbs
def cmd_list(a):
    bank = load()
    rows = []
    for cat, val in bank.items():
        if isinstance(val, list):
            rows.append((cat, len(val), [e.get("id") for e in val][:6]))
    print(f"{'category':<12}{'count':>6}  sample")
    for cat, n, sample in rows:
        print(f"{cat:<12}{n:>6}  {', '.join(sample)}")
    print("\nrules:", ", ".join(bank["rules"]))


def cmd_show(a):
    idx = index(load())
    e = idx.get(a.id)
    if not e:
        raise SystemExit(f"no entry '{a.id}'")
    print(json.dumps(e, indent=2, ensure_ascii=False))


def cmd_search(a):
    bank = load()
    q = a.text.lower()
    for cat, val in bank.items():
        if not isinstance(val, list):
            continue
        for e in val:
            blob = json.dumps(e, ensure_ascii=False).lower()
            if q in blob:
                print(f"{cat:<12} {e['id']:<22} {str(e.get('en', e.get('body')))[:80]}")


def cmd_compose(a):
    specs = json.loads(Path(a.spec).read_text(encoding="utf-8"))
    if isinstance(specs, dict):
        specs = [specs]
    out = []
    bad = 0
    for s in specs:
        r = compose(s)
        out.append(r)
        mark = "OK " if r["lint"]["ok"] else "!! "
        print(f"{mark}{r['id']}  ({r['camera_kind']}, {r['beats']} beat)  "
              f"score={r['lint']['score']}")
        for i in r["lint"]["issues"]:
            print(f"     - [{i['rule']}] {i['msg']}")
        if not r["lint"]["ok"]:
            bad += 1
    if a.out:
        Path(a.out).write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8")
    if a.verbose:
        for r in out:
            print("\n" + "-" * 60 + "\n" + r["prompt"])
    return 0 if bad == 0 else 1


def cmd_lint(a):
    r = lint(a.text)
    print(json.dumps(r, indent=2, ensure_ascii=False))
    return 0 if r["ok"] else 1


def cmd_jobs(a):
    """spec -> the file studio/mivi_shot.py consumes."""
    specs = json.loads(Path(a.spec).read_text(encoding="utf-8"))
    bank = load(getattr(a, "bank", None))
    jobs, rows = [], []
    for s in specs:
        r = compose(s, bank)
        jobs.append({"id": s["id"], "still": s.get("still", ""),
                     "still_from": s.get("still_from"),
                     "prompt": r["prompt"], "attempts": int(s.get("attempts", 1)),
                     "model": s.get("model", "mivi-gx-720p"),
                     "quality": int(s.get("quality", 2))})
        rows.append({"id": s["id"], "lint_ok": r["lint"]["ok"], "score": r["lint"]["score"],
                     "issues": r["lint"]["issues"]})
    Path(a.out).write_text(json.dumps({"shots": jobs}, indent=2, ensure_ascii=False),
                           encoding="utf-8")
    print(json.dumps({"jobs": len(jobs), "out": a.out,
                      "clean": sum(1 for r in rows if r["lint_ok"])}, indent=2))
    for r in rows:
        if not r["lint_ok"]:
            print(f"  ! {r['id']}: " + "; ".join(i["msg"] for i in r["issues"]))
    return 0


def cmd_shots(a):
    bank = load(getattr(a, "bank", None))
    spec = {"id": "adhoc", "subject": a.subject, "camera": a.camera,
            "shot_size": a.size, "micro": a.micro, "environment": a.environment,
            "place": a.place, "end_state": a.end, "look": a.look}
    r = compose({k: v for k, v in spec.items() if v}, bank)
    print(r["prompt"])
    print()
    for i in r["lint"]["issues"]:
        print(f"[{i['rule']}] {i['msg']}")
    return 0


def main():
    ap = argparse.ArgumentParser(prog="motionbank")
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("list"); p.set_defaults(fn=cmd_list)

    p = sub.add_parser("show"); p.add_argument("id"); p.set_defaults(fn=cmd_show)

    p = sub.add_parser("search"); p.add_argument("text"); p.set_defaults(fn=cmd_search)

    p = sub.add_parser("compose"); p.add_argument("spec")
    p.add_argument("--out"); p.add_argument("--verbose", action="store_true")
    p.set_defaults(fn=cmd_compose)

    p = sub.add_parser("lint"); p.add_argument("text"); p.set_defaults(fn=cmd_lint)

    p = sub.add_parser("jobs"); p.add_argument("--bank", default=None,
        help="alternative bank JSON, e.g. studio/motions/anime_bank.json"); p.add_argument("spec"); p.add_argument("--out", required=True)
    p.set_defaults(fn=cmd_jobs)

    p = sub.add_parser("shots"); p.add_argument("--bank", default=None)
    p.add_argument("--subject"); p.add_argument("--camera"); p.add_argument("--size")
    p.add_argument("--micro", action="append"); p.add_argument("--environment")
    p.add_argument("--place"); p.add_argument("--end"); p.add_argument("--look")
    p.set_defaults(fn=cmd_shots)

    a = ap.parse_args()
    sys.exit(a.fn(a) or 0)


if __name__ == "__main__":
    main()
