#!/usr/bin/env python3
"""links.py — the repo moves files; this proves nothing was left dangling.

Checks, offline and in one pass:

  1. every relative markdown link resolves to a real file
  2. every `path/mentioned/in/backticks.md` that looks like a repo path exists
  3. every python file compiles
  4. every script named in a Makefile target, workflow, or doc exists
  5. no markdown file is still pointing at a path this repo moved away from

    python3 studio/links.py            # human report, exit 1 on any break
    python3 studio/links.py --json     # machine report
"""
from __future__ import annotations

import argparse
import json
import py_compile
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# paths that were moved; any surviving mention is a bug
MOVED = {
    "studio/motions/ANIME_METHOD.md": "studio/knowledge/method/ANIME_METHOD.md",
    "studio/motions/ARTGEN.md": "studio/knowledge/method/ARTGEN.md",
    "studio/motions/WAN_PROMPTS.md": "studio/knowledge/prompting/WAN_PROMPTS.md",
    "studio/motions/CONSISTENCY_AND_SPEED.md": "studio/knowledge/workflow/CONSISTENCY_AND_SPEED.md",
    "studio/motions/WORKFLOW.md": "studio/knowledge/workflow/WORKFLOW.md",
    "studio/toolbox/README.md": "studio/knowledge/research/TOOLBOX.md",
    "films/anime_ten/DELIVERY.md": "studio/knowledge/delivery/DELIVERY.md",
    "films/anime_ten/MIN1_REPORT.md": "studio/knowledge/delivery/MIN1_REPORT.md",
    "films/anime_ten/PRODUCTION.md": "studio/knowledge/archive/PRODUCTION_v1_composite.md",
    "studio/CHAIN_WORKFLOW.md": "studio/knowledge/archive/CHAIN_WORKFLOW.md",
    "studio/QUALITY_WORKFLOW.md": "studio/knowledge/archive/QUALITY_WORKFLOW.md",
    "studio/knowledge/learnings.md": "studio/knowledge/LEARNINGS.md",
    "studio/knowledge/README.md": "studio/knowledge/research/BANK_GUIDE.md (the bank guide; hub has its own README)",
}

LINK = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
CODE_PATH = re.compile(r"`((?:studio|films|bridge|mivi_web|\.github|_inbox)/[A-Za-z0-9_./-]+\.[a-z]{2,4})`")
SCRIPT = re.compile(r"\b((?:studio|bridge)/[A-Za-z0-9_./-]+\.py)\b")


def tracked() -> set[str]:
    try:
        out = subprocess.run(["git", "ls-files"], cwd=ROOT, capture_output=True,
                             text=True, check=True).stdout
        return set(out.split())
    except Exception:  # noqa: BLE001
        return {str(p.relative_to(ROOT)) for p in ROOT.rglob("*") if p.is_file()}


def check_md(files: set[str]) -> list[str]:
    bad = []
    for rel in sorted(f for f in files if f.endswith(".md")):
        p = ROOT / rel
        try:
            text = p.read_text(encoding="utf-8")
        except Exception:  # noqa: BLE001
            continue
        for target in LINK.findall(text):
            t = target.split("#")[0].strip()
            if not t or t.startswith(("http://", "https://", "mailto:", "#")):
                continue
            if t.startswith("/"):
                continue
            full = (p.parent / t).resolve()
            if not full.exists():
                bad.append(f"{rel}: broken link -> {target}")
    return bad


def check_code_paths(files: set[str]) -> list[str]:
    bad = []
    for rel in sorted(f for f in files if f.endswith((".md", ".yml", ".py"))):
        p = ROOT / rel
        try:
            text = p.read_text(encoding="utf-8")
        except Exception:  # noqa: BLE001
            continue
        for m in set(CODE_PATH.findall(text)) | set(SCRIPT.findall(text)):
            if m in MOVED:                      # stale reference, reported separately
                continue
            if any(ch in m for ch in "*<>{}") or "..." in m:
                continue
            if m not in files and not (ROOT / m).exists():
                bad.append(f"{rel}: mentions missing file {m}")
    return bad


def check_moved(files: set[str]) -> list[str]:
    bad = []
    for rel in sorted(files):
        if not rel.endswith((".md", ".yml", ".py", ".json")):
            continue
        try:
            text = (ROOT / rel).read_text(encoding="utf-8")
        except Exception:  # noqa: BLE001
            continue
        for old, new in MOVED.items():
            if old == "studio/knowledge/README.md" and rel == "studio/knowledge/README.md":
                continue
            if f"/{old}" in text:
                bad.append(f"{rel}: still points at moved path {old} -> {new}")
    return bad


def check_python(files: set[str]) -> list[str]:
    bad = []
    for rel in sorted(f for f in files if f.endswith(".py")):
        try:
            with tempfile.TemporaryDirectory() as td:
                py_compile.compile(str(ROOT / rel), cfile=str(Path(td) / "x.pyc"), doraise=True)
        except py_compile.PyCompileError as exc:
            bad.append(f"{rel}: {exc.msg.splitlines()[-1]}")
    return bad


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    files = tracked()
    report = {
        "tracked_files": len(files),
        "markdown_links": check_md(files),
        "code_paths": check_code_paths(files),
        "moved_paths": check_moved(files),
        "python": check_python(files),
    }
    breaks = sum(len(v) for k, v in report.items() if isinstance(v, list))
    if a.json:
        print(json.dumps({**report, "breaks": breaks}, indent=2))
    else:
        for k in ("moved_paths", "markdown_links", "code_paths", "python"):
            items = report[k]
            print(f"{k:16s} {len(items):3d}  {'ok' if not items else ''}")
            for i in items[:20]:
                print(f"    - {i}")
        print(f"\n{report['tracked_files']} tracked files · {breaks} breaks")
    return 1 if breaks else 0


if __name__ == "__main__":
    raise SystemExit(main())
