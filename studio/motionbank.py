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
SHOT_NAMES = {"ews": "Extreme wide shot", "ws": "Wide shot", "ms": "Medium shot",
              "mcu": "Medium close-up", "cu": "Close-up", "ecu": "Extreme close-up",
              "ots": "Over-the-shoulder shot", "insert": "Insert shot"}


def _strip_negations(text: str) -> str:
    """`no zoom, no pan, no handheld` is a promise, not a move — and Wan has no
    negative-prompt field to put it in. Drop every `no/never/without X` clause and
    tidy the punctuation it leaves behind."""
    out = re.sub(r"\b(no|never|without)\s+[^,.;\u2014\u2013]+", " ", text, flags=re.I)
    out = re.sub(r"\s*,\s*(?=,|;|\.|$)", "", out)      # dangling / doubled commas
    out = re.sub(r"^[\s,;\u2014\u2013]+", "", out)
    out = re.sub(r"[\s,;\u2014\u2013]+(the\s+)?camera\s*$", "", out, flags=re.I)
    out = re.sub(r"\s+", " ", out).strip(" ,;\u2014\u2013")
    return out


def lint(text: str) -> dict:
    """The prompt contract is Wan's, not ours.

    Until 2026-10-30 this function demanded a negative block, an end-state sentence
    and a stated static camera. All three are wrong for I2V: Alibaba's own
    `I2V_A14B_EN_SYS_PROMPT` says to drop static descriptions, our API has no
    negative-prompt field, and a "static" clause is already implied by a frame that
    does not move. The old rules scored a *correct* Wan prompt 64/100 and a wrong one
    higher — so it is now a thin wrapper over studio/wanprompt.py.

    Returns the same shape as before: {"ok", "score", "issues", "errors"}.
    """
    import sys
    from pathlib import Path
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    import wanprompt

    r = wanprompt.check(text)
    issues = []
    rules = {
        "word": "length_100",
        "static": "no_static_descriptions",
        "camera": "camera_clause",
        "subject action": "subject_action",
        "bracketed": "prose_not_form",
        "words": "too_thin",
    }
    for problem in r["problems"]:
        rule = next((v for k, v in rules.items() if problem.startswith(k)), "wan_contract")
        issues.append({"rule": rule, "level": "warn", "msg": problem})
    for note in r.get("advice", []):
        issues.append({"rule": "thin", "level": "info", "msg": note})
    return {"ok": r["ok"], "score": max(0, 100 - 20 * len(r["problems"]) - 5 * len(r.get("advice", []))),
            "issues": issues, "errors": []}


# ------------------------------------------------------------------ compose
def compose(spec: dict, bank: dict | None = None) -> dict:
    bank = bank or load()
    idx = index(bank)
    unknown: list[str] = []

    def get(key, default=None):
        if not key:
            return default if default is not None else {"id": None, "en": "", "_cat": "free"}
        if isinstance(key, str) and key in idx:
            return idx[key]
        # previously this pasted the raw id into the prompt ("Fingers_tighten.") —
        # a misspelt bank id used to become a nonsense instruction instead of an error
        unknown.append(key)
        return {"id": None, "en": "", "_cat": "free"}

    # ---- Wan-shaped prose, not a labelled form -------------------------------
    # Sent by the official I2V contract: under 100 words, motion only, no description
    # of what is already in the input frame, no negative block (the API has no field
    # for one). `compose` used to emit `[shot]/[place]/[subject]` tags: 109 words that
    # failed our own linter, which is exactly the prompt shape that made the model
    # repaint instead of animate. See knowledge/prompting/WAN_PROMPTS.md.
    shot = get(spec.get("shot_size"), {"en": ""})
    shot_txt = SHOT_NAMES.get((spec.get("shot_size") or "").lower(), shot.get("en", ""))
    cam = get(spec.get("camera"), idx["static_locked"])
    subj = get(spec.get("subject"), {"en": ""})
    micro = spec.get("micro")
    micros = [get(m) for m in ([micro] if isinstance(micro, str) else (micro or []))]
    have_seed = bool(spec.get("still") or spec.get("still_from") or spec.get("still_from_clip"))
    look = get(spec.get("look"), {}) if (spec.get("look") and not have_seed) else {}

    mag = spec.get("magnitude") or {}
    cam_txt = _strip_negations(fmt(cam, **mag)).strip(" ,")
    if cam_txt and not cam_txt.endswith("."):
        cam_txt += "."
    subj_txt = _strip_negations(fmt(subj, **mag)) if subj.get("en") else ""
    micro_bits = [_strip_negations(fmt(m, **mag)) for m in micros if m.get("en")]
    # a micro that repeats the subject ("one blink" twice) is noise, not a second beat
    def _overlap(x: str, y: str) -> float:
        stop = {"the", "a", "and", "of", "over", "in"}
        stem = lambda t: t[:5] if len(t) >= 5 else t          # blink/blinks/blinking
        a = {stem(t) for t in re.findall(r"[a-z']+", x.lower())} - stop
        b = {stem(t) for t in re.findall(r"[a-z']+", y.lower())} - stop
        return len(a & b) / max(1, len(a | b))

    micro_bits = [b for b in micro_bits if b and (not subj_txt or _overlap(b, subj_txt) < 0.22)]

    lines, dropped = [], []
    if cam_txt:
        lines.append(cam_txt[0].upper() + cam_txt[1:])
    if subj_txt:
        lines.append(subj_txt[0].upper() + subj_txt[1:] + ".")
    if micro_bits:
        lines.append(" ".join(b[0].upper() + b[1:] + "." for b in micro_bits))
    if spec.get("place") and not have_seed:
        lines.append(spec["place"].strip(" .") + ".")
    elif spec.get("place"):
        dropped.append("place (already in the input frame)")
    if spec.get("end_state"):
        lines.append("By the last frame " + spec["end_state"].strip(" .") + ".")
    if look.get("en"):
        lines.insert(0, _strip_negations(fmt(look)) + ".")
    elif spec.get("look"):
        dropped.append("look (the input frame already carries the style)")
    if spec.get("environment"):
        dropped.append("environment (static — Wan DROPS static scene description)")
    if shot_txt and shot_txt.split()[0].lower() not in " ".join(lines).lower():
        lines.insert(0, shot_txt + ".")
    if unknown:
        dropped.append("unknown bank ids (not in anime_bank.json): " + ", ".join(map(str, unknown)))
    dropped.append("negative block (no negativePrompt field on this endpoint)")

    prompt = " ".join(lines).strip()

    # trim to the contract, cheapest sentence first
    def words(t):
        return len(re.findall(r"[A-Za-z']+", t))

    for victim in ("place", "end"):
        if words(prompt) <= 100:
            break
        keep = [l for l in lines if not (victim == "place" and l == (spec.get("place", "").strip() + "."))
                and not (victim == "end" and l.lower().startswith("by the last frame"))]
        if len(keep) != len(lines):
            dropped.append(f"{victim} sentence (trimmed to stay under 100 words)")
            lines = keep
            prompt = " ".join(lines).strip()
    if words(prompt) > 100:
        prompt = " ".join(prompt.split()[:100]).rstrip(",;") + "."

    report = lint(prompt)
    return {"id": spec.get("id"), "prompt": prompt, "lint": report,
            "beats": subj.get("beats", 1),
            "camera_kind": cam.get("kind", "move"),
            "words": words(prompt), "dropped": dropped}


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
    bank = load(getattr(a, "bank", None))
    for s in specs:
        r = compose(s, bank)
        out.append(r)
        mark = "OK " if r["lint"]["ok"] else "!! "
        print(f"{mark}{r['id']}  ({r['camera_kind']}, {r['beats']} beat)  "
              f"score={r['lint']['score']}")
        for i in r["lint"]["issues"]:
            print(f"     - [{i['rule']}] {i['msg']}")
        for d in r.get("dropped", []):
            if d.startswith("unknown bank ids"):
                print(f"     ! {d}")
        if not r["lint"]["ok"] or any(d.startswith("unknown bank ids") for d in r.get("dropped", [])):
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


BANKS = {"live": BANK_PATH, "anime": Path(__file__).resolve().parent / "motions" / "anime_bank.json"}


def pick_bank(specs: list[dict], forced: str | None) -> tuple[dict, str]:
    """Choose the bank the spec actually speaks. The two banks share nine ids with
    different text, so the wrong pick yields a fluent prompt with the wrong
    vocabulary and no motion. Reported, never silent."""
    if forced:
        return load(forced), str(forced)
    best, best_hits, best_name = None, -1, ""
    for name, path in BANKS.items():
        try:
            b = load(path)
        except Exception:  # noqa: BLE001
            continue
        idx = index(b)
        # motion words carry more signal than a shot size the two banks share
        weighted: dict[str, int] = {}
        for s in specs:
            for field, w in (("shot_size", 1), ("camera", 1), ("subject", 3), ("look", 2)):
                k = s.get(field)
                if isinstance(k, str):
                    weighted[k] = max(weighted.get(k, 0), w)
            m = s.get("micro")
            for k in ([m] if isinstance(m, str) else (m or [])):
                weighted[k] = max(weighted.get(k, 0), 2)
        hits = sum(w for k, w in weighted.items() if k in idx)
        if hits > best_hits:          # strict: a tie keeps the live-action default
            best, best_hits, best_name = b, hits, f"{name} ({path.name})"
    return best, best_name


def cmd_jobs(a):
    """spec -> the file studio/mivi_shot.py consumes."""
    specs = json.loads(Path(a.spec).read_text(encoding="utf-8"))
    bank, bank_name = pick_bank(specs, getattr(a, "bank", None))
    jobs, rows, unknown = [], [], []
    missing = [s["id"] for s in specs
               if not s.get("still") and not s.get("still_from") and not s.get("still_from_clip")]
    if missing:
        raise SystemExit(f"no still for {missing} — an i2v job without an image fails on "
                         f"the runner (IsADirectoryError). Set `still` or chain it.")
    for s in specs:
        r = compose(s, bank)
        jobs.append({"id": s["id"], "still": s.get("still", ""),
                     "still_from": s.get("still_from"),
                     "still_from_clip": s.get("still_from_clip"),
                     "prompt": r["prompt"], "attempts": int(s.get("attempts", 1)),
                     "model": s.get("model", "mivi-gx-720p"),
                     "quality": int(s.get("quality", 2))})
        miss = [d for d in r.get("dropped", []) if d.startswith("unknown bank ids")]
        if miss:
            unknown.append((s["id"], miss[0]))
        rows.append({"id": s["id"], "lint_ok": r["lint"]["ok"], "score": r["lint"]["score"],
                     "issues": r["lint"]["issues"], "words": r.get("words")})
    Path(a.out).write_text(json.dumps({"shots": jobs}, indent=2, ensure_ascii=False),
                           encoding="utf-8")
    print(json.dumps({"jobs": len(jobs), "out": a.out,
                      "bank": bank_name,
                      "clean": sum(1 for r in rows if r["lint_ok"])}, indent=2))
    for r in rows:
        if not r["lint_ok"]:
            print(f"  ! {r['id']}: " + "; ".join(i["msg"] for i in r["issues"]))
    for jid, msg in unknown:
        print(f"  ! {jid}: {msg}")
    if unknown:
        # The two banks share nine ids with different text (static_locked, micro_push,
        # slow_dolly_in ...). Composing an anime spec against the live-action bank
        # yields a fluent prompt with the wrong vocabulary and no motion — silent.
        print(f"\nFAILED: {len(unknown)} job(s) reference ids that are not in "
              f"{Path(str(getattr(a, 'bank', None) or BANK_PATH)).name}. "
              f"Pass --bank studio/motions/anime_bank.json for the cel bank.")
        return 1
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
