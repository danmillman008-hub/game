#!/usr/bin/env python3
"""bank.py — the repo knowledge bank: one JSON file, verified against the live API.

Everything learned about other people's code lives in `repos.json`. That file is the
source of truth; `BANK.md` is generated from it so the readable table can never drift
from the data. Numbers are never typed from memory: `verify` re-reads stars, licence
and last-commit straight from api.github.com and reports (or applies) the diff.

    python3 studio/knowledge/bank.py check            # is the bank internally valid
    python3 studio/knowledge/bank.py stats            # what we know, by verdict and gap
    python3 studio/knowledge/bank.py list --gap lipsync
    python3 studio/knowledge/bank.py verify           # compare with GitHub, report drift
    python3 studio/knowledge/bank.py verify --update  # write the fresh numbers back
    python3 studio/knowledge/bank.py export           # regenerate BANK.md

Why a bank and not a doc: a hand-written table is wrong the day after it is written
(piper moved org, Wav2Lip still has no licence, LatentSync added a 512px model).
A JSON file can be re-checked by a machine in ten seconds.
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
BANK = HERE / "repos.json"
MD = HERE / "BANK.md"

VERDICTS = {"take": "بگیر — در مسیر تولید استفاده می‌شود",
            "study": "مطالعه — الگوریتم را بخوان، کد را نه",
            "avoid": "نگیر — لایسنس/کیفیت/رها‌شدگی"}

# the gaps are the ones from studio/GAPS.md plus the two sound ones
GAPS = {
    "a-cut": "دستور زبان برش",
    "b-pacing": "ریتم و طول شات",
    "c-murch": "قانون مِرچ در تدوین",
    "d-story": "ساختار روایت",
    "e-subjective": "عینیت در برابر ذهنیت",
    "f-color": "تطبیق رنگ بین شات‌ها",
    "g-sound": "صدا، داکینگ، J/L-cut",
    "h-prompt": "طول پرامپت برای Wan",
    "i-qc": "کیفیت‌سنجی خودکار",
    "j-frame": "تصویر، اینترپولیشن، فرمت",
    "k-continuity": "دادهٔ تداوم",
    "lipsync": "لب‌سینک و TTS",
}

REQUIRED = ("repo", "url", "gap", "verdict", "note")


class BankError(SystemExit):
    pass


# ------------------------------------------------------------------ loading ---
def load(path: Path = BANK) -> dict:
    if not path.exists():
        raise BankError(f"no bank at {path}")
    return json.loads(path.read_text(encoding="utf-8"))


def save(data: dict, path: Path = BANK) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


# ------------------------------------------------------------------ checks ----
def check(data: dict) -> list[str]:
    problems: list[str] = []
    seen: set[str] = set()
    for i, e in enumerate(data.get("repos", [])):
        tag = e.get("repo") or f"#{i}"
        for k in REQUIRED:
            if not e.get(k):
                problems.append(f"{tag}: missing {k}")
        if e.get("repo") in seen:
            problems.append(f"{tag}: duplicate")
        seen.add(e.get("repo"))
        if e.get("gap") not in GAPS:
            problems.append(f"{tag}: unknown gap {e.get('gap')!r}")
        if e.get("verdict") not in VERDICTS:
            problems.append(f"{tag}: unknown verdict {e.get('verdict')!r}")
        if e.get("repo") and e.get("url") and not e["url"].endswith("/" + e["repo"]):
            problems.append(f"{tag}: url does not end with the repo name")
    return problems


# ------------------------------------------------------------------- github ---
def _token() -> str | None:
    if os.environ.get("GITHUB_TOKEN"):
        return os.environ["GITHUB_TOKEN"]
    try:
        return subprocess.run(["gh", "auth", "token"], capture_output=True, text=True,
                              timeout=20).stdout.strip() or None
    except Exception:                              # noqa: BLE001
        return None


def live(repo: str, token: str | None = None) -> dict:
    """One call per repo. Returns the three fields that actually change."""
    req = urllib.request.Request(f"https://api.github.com/repos/{repo}",
                                 headers={"Accept": "application/vnd.github+json",
                                          "User-Agent": "studio-bank"})
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(req, timeout=30) as r:
        d = json.loads(r.read().decode())
    return {"stars": d.get("stargazers_count"),
            "license": (d.get("license") or {}).get("spdx_id") or "none",
            "pushed_at": (d.get("pushed_at") or "")[:10],
            "archived": bool(d.get("archived")),
            "error": None}


def verify(data: dict, update: bool = False, token: str | None = None) -> list[str]:
    token = token or _token()
    drift: list[str] = []
    for e in data["repos"]:
        try:
            got = live(e["repo"], token)
        except urllib.error.HTTPError as ex:
            if ex.code == 404:
                drift.append(f"{e['repo']}: GONE (404) — renamed or deleted")
                if update:
                    e["missing"] = True
            else:
                drift.append(f"{e['repo']}: HTTP {ex.code}")
            time.sleep(1.2)
            continue
        except Exception as ex:                    # noqa: BLE001
            drift.append(f"{e['repo']}: {type(ex).__name__}")
            time.sleep(1.2)
            continue
        e.pop("missing", None)
        for k in ("stars", "license", "pushed_at", "archived"):
            if e.get(k) != got[k]:
                drift.append(f"{e['repo']}: {k} {e.get(k)} -> {got[k]}")
                if update:
                    e[k] = got[k]
        e["verified_on"] = time.strftime("%Y-%m-%d")
        time.sleep(1.2)
    if update:
        data["verified_on"] = time.strftime("%Y-%m-%d")
        save(data)
    return drift


# ------------------------------------------------------------------- output ---
def stats(data: dict) -> str:
    repos = data["repos"]
    lines = [f"{len(repos)} repos · verified {data.get('verified_on', 'never')}", ""]
    for v, label in VERDICTS.items():
        n = sum(1 for e in repos if e["verdict"] == v)
        lines.append(f"  {v:6s} {n:3d}  {label}")
    lines.append("")
    for g, label in GAPS.items():
        rows = [e for e in repos if e["gap"] == g]
        if rows:
            lines.append(f"  {g:12s} {len(rows):2d}  {label}")
    missing = [e["repo"] for e in repos if e.get("missing")]
    if missing:
        lines.append("")
        lines.append("  gone: " + ", ".join(missing))
    return "\n".join(lines)


def export_md(data: dict) -> str:
    out = ["# BANK — ریپوهایی که بررسی کرده‌ایم", "",
           "> این فایل از `repos.json` ساخته می‌شود. دستی ویرایش نکن.",
           f"> آخرین تأیید: **{data.get('verified_on', 'هرگز')}**", ""]
    for g, label in GAPS.items():
        rows = [e for e in data["repos"] if e["gap"] == g]
        if not rows:
            continue
        out += [f"## {g} — {label}", "",
                "| ریپو | ★ | لایسنس | آخرین کامیت | حکم | چرا |",
                "|---|---|---|---|---|---|"]
        rows.sort(key=lambda e: (-(e.get("stars") or 0)))
        for e in rows:
            mark = {"take": "✅ بگیر", "study": "📖 مطالعه", "avoid": "✕ نگیر"}[e["verdict"]]
            lic = e.get("license") or "—"
            pushed = e.get("pushed_at") or "—"
            out.append(f"| [`{e['repo']}`]({e['url']}) | {e.get('stars') or '—'} | {lic} | "
                       f"{pushed} | {mark} | {e['note']} |")
        out.append("")
    return "\n".join(out)


# --------------------------------------------------------------------- cli ----
def main() -> None:
    ap = argparse.ArgumentParser(prog="bank", description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("check"); p.set_defaults(fn=lambda a: None)
    p = sub.add_parser("stats"); p.set_defaults(fn=lambda a: None)
    p = sub.add_parser("list"); p.add_argument("--gap"); p.add_argument("--verdict")
    p.set_defaults(fn=lambda a: None)
    p = sub.add_parser("verify"); p.add_argument("--update", action="store_true")
    p.set_defaults(fn=lambda a: None)
    p = sub.add_parser("export"); p.set_defaults(fn=lambda a: None)
    a = ap.parse_args()

    data = load()
    if a.cmd == "check":
        problems = check(data)
        for pr in problems:
            print(f"  ! {pr}")
        print("BANK OK" if not problems else f"{len(problems)} problem(s)")
        raise SystemExit(1 if problems else 0)
    if a.cmd == "stats":
        print(stats(data)); return
    if a.cmd == "list":
        for e in data["repos"]:
            if a.gap and e["gap"] != a.gap:
                continue
            if a.verdict and e["verdict"] != a.verdict:
                continue
            print(f"{e['verdict']:6s} {e['gap']:12s} {str(e.get('stars') or '—'):>7s} "
                  f"{(e.get('license') or '—'):14s} {e['repo']}")
        return
    if a.cmd == "verify":
        drift = verify(data, a.update)
        for d in drift:
            print(f"  ~ {d}")
        if not drift:
            print("no drift — every entry still matches GitHub")
        elif a.update:
            print(f"\nupdated {BANK.name}; now run: bank.py export")
        else:
            print("\nrun with --update to apply")
        raise SystemExit(0)
    if a.cmd == "export":
        MD.write_text(export_md(data), encoding="utf-8")
        print(f"-> {MD}")


if __name__ == "__main__":
    main()
