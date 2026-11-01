#!/usr/bin/env python3
"""Measure Persian coverage of the runtime overlay against the engines' source trees.

    python3 tools/i18n_coverage.py                    # summary table
    python3 tools/i18n_coverage.py --missing          # untranslated strings, most frequent first
    python3 tools/i18n_coverage.py --engine epm       # only one engine

Engine sources are read from mimo/engines/src/<engine> when present, otherwise from the paths given with --epm/--lh.
"""
from __future__ import annotations

import argparse
import collections
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
MIMO = HERE.parent
CJK = re.compile(r"[\u4e00-\u9fff]")


def collect_epm(root: pathlib.Path) -> collections.Counter:
    counter: collections.Counter = collections.Counter()
    if not root.is_dir():
        return counter
    for path in root.rglob("*"):
        if path.suffix not in (".vue", ".ts") or not path.is_file():
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        for pattern in (r">([^<>{}]{1,60})<", r"['\"`]([^'\"`\n]{1,60})['\"`]"):
            for match in re.finditer(pattern, text):
                value = match.group(1).strip()
                if CJK.search(value):
                    counter[value] += 1
    return counter


def collect_lh(root: pathlib.Path) -> collections.Counter:
    counter: collections.Counter = collections.Counter()
    if not root.is_dir():
        return counter
    for sub in ("app", "components"):
        for path in (root / sub).rglob("*.tsx"):
            text = path.read_text(encoding="utf-8", errors="ignore")
            for match in re.finditer(r">([A-Za-z][^<>{}]{2,45})<", text):
                counter[" ".join(match.group(1).split())] += 1
            for match in re.finditer(r'(?:placeholder|title|aria-label|label)="([A-Za-z][^"]{2,45})"', text):
                counter[" ".join(match.group(1).split())] += 1
    return counter


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--engine", choices=["epm", "lh", "all"], default="all")
    ap.add_argument("--missing", action="store_true")
    ap.add_argument("--epm", type=pathlib.Path, default=MIMO / "engines/src/epm/frontend/src")
    ap.add_argument("--lh", type=pathlib.Path, default=MIMO / "engines/src/learnharness")
    args = ap.parse_args()

    engines = []
    if args.engine in ("epm", "all"):
        engines.append(("epm", collect_epm(args.epm), "dict-epm.json"))
    if args.engine in ("lh", "all"):
        engines.append(("lh", collect_lh(args.lh), "dict-max.json"))

    any_source = False
    for name, strings, dict_name in engines:
        if not strings:
            print(f"[{name}] منبع موتور پیدا نشد ({args.epm if name == 'epm' else args.lh}) — "
                  f"ابتدا tools/bootstrap_engines.sh را اجرا کنید.")
            continue
        any_source = True
        dictionary = json.loads((MIMO / "host/overlay" / dict_name).read_text(encoding="utf-8"))["strings"]
        covered = [s for s in strings if s in dictionary]
        occurrences = sum(strings.values())
        covered_occurrences = sum(strings[s] for s in covered)
        print(f"[{name}] رشتهٔ یکتا {len(strings)} · ترجمه‌شده {len(covered)} "
              f"({len(covered)/len(strings)*100:.1f}%) · پوشش وزنی {covered_occurrences/occurrences*100:.1f}%")
        if args.missing:
            for text, count in strings.most_common():
                if text not in dictionary:
                    print(f"   {count:>4}  {text}")
    if not any_source:
        return 3
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
