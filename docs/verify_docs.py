#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fail-closed integrity check for the canonical handoff (no dependencies).

Usage: python3 docs/verify_docs.py
Checks: index parses, every referenced path exists, every relative markdown
link resolves, no CJK leaked into the Persian docs, honesty flags intact,
commit log matches git, stale verdicts are not repeated in the new docs.
"""
from __future__ import annotations
import json, re, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CHECKS, FAILED = [], []

def ck(name, ok, detail=""):
    CHECKS.append((name, bool(ok), detail))
    if not ok:
        FAILED.append(name + (": " + detail if detail else ""))

index_path = ROOT / "REPO_INDEX.json"
ck("REPO_INDEX.json exists", index_path.is_file())
if not index_path.is_file():
    print("FATAL: REPO_INDEX.json missing"); sys.exit(1)
index = json.loads(index_path.read_text(encoding="utf-8"))
ck("REPO_INDEX.json parses", isinstance(index, dict))
ck("schemaVersion present", index.get("schemaVersion") == "1.0")

# 1. every path in the index resolves
missing = [p for p in index.get("paths", []) if not (ROOT / p).exists()]
ck("all index paths exist", not missing, ", ".join(missing[:6]))

# 2. readOrder and documents exist
ro_missing = [p for p in index.get("readOrder", []) if not (ROOT / p).is_file()]
ck("readOrder files exist", not ro_missing, ", ".join(ro_missing))
doc_missing = [d["path"] for d in index.get("documents", []) if not (ROOT / d["path"]).is_file()]
ck("documented files exist", not doc_missing, ", ".join(doc_missing))

# 3. every relative markdown link in the handoff resolves
md_files = [ROOT / "README.md", ROOT / "AGENTS.md", ROOT / "app/README.md",
             ROOT / "app/content/README.md", ROOT / "CLAUDE.md", ROOT / "GEMINI.md",
             ROOT / ".github/copilot-instructions.md"] + sorted((ROOT / "docs").glob("*.md"))
link_re = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
broken = []
for f in md_files:
    text = f.read_text(encoding="utf-8")
    for target in link_re.findall(text):
        if target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        path = target.split("#", 1)[0].strip()
        if not path:
            continue
        if not (f.parent / path).resolve().exists():
            broken.append("%s -> %s" % (f.relative_to(ROOT), target))
ck("markdown links resolve", not broken, "; ".join(broken[:8]))

# 4. no CJK contamination in the new Persian handoff
cjk = re.compile(r"[\u3400-\u4dbf\u4e00-\u9fff\u3040-\u30ff\uac00-\ud7af]")
cjk_hits = []
for f in md_files:
    for i, line in enumerate(f.read_text(encoding="utf-8").splitlines(), 1):
        if cjk.search(line):
            cjk_hits.append("%s:%d" % (f.relative_to(ROOT), i))
ck("no CJK leaked into handoff docs", not cjk_hits, ", ".join(cjk_hits[:8]))

# 5. honesty invariants survive in docs
readme = (ROOT / "README.md").read_text(encoding="utf-8")
agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
state = (ROOT / "docs/04_CURRENT_STATE.md").read_text(encoding="utf-8")
for label, text, needle in [
    ("README mentions SERVER CONFIRMED=0", readme, "SERVER CONFIRMED=0"),
    ("README mentions unreviewed content", readme, "unreviewed"),
    ("AGENTS mentions no-network rule", agents, "بدون شبکه"),
    ("AGENTS mentions only allowed branch", agents, "arena/aebb90b7-game"),
    ("AGENTS mentions v12.5-fa rules", agents, "v12.5-fa"),
    ("state doc lists 45/45", state, "۴۵/۴۵"),
    ("state doc lists 54/54", state, "۵۴/۵۴"),
    ("state doc lists 51/51", state, "۵۱/۵۱"),
    ("state doc lists 2/2", state, "۲/۲"),
]:
    ck(label, needle in text)

# 6. honesty flags in the machine index
h = index.get("honest", {})
ck("index serverConfirmed == 0", h.get("serverConfirmed") == 0)
ck("index llm/network/generatedText false",
   h.get("llm") is False and h.get("network") is False and h.get("generatedText") is False)
ck("index externalProvider not-configured", h.get("externalProvider") == "not-configured")
ck("index content unreviewed",
   index.get("content", {}).get("reviewStatus") == "unreviewed")

# 7. commit log matches git
commits = subprocess.check_output(
    ["git", "log", "--pretty=format:%h"], cwd=ROOT, text=True).strip().split("\n")
baseline = index["repository"]["baselineHead"]
ancestor = subprocess.run(["git", "merge-base", "--is-ancestor", baseline, "HEAD"],
                          cwd=ROOT).returncode == 0
ck("baseline head is an ancestor of HEAD", ancestor, baseline)
ck("index described head == baseline",
   index["repository"]["head"] == index["repository"]["baselineHead"])
ck("index commitCount >= baseline", index["repository"]["commitCount"] >=
   index["repository"]["baselineCommitCount"],
   "%s vs %s" % (index["repository"]["commitCount"], index["repository"]["baselineCommitCount"]))
ck("git history contains at least the baseline commits",
   len(commits) >= index["repository"]["baselineCommitCount"],
   "%d vs %s" % (len(commits), index["repository"]["baselineCommitCount"]))
log = (ROOT / "docs/09_COMMIT_LOG.md").read_text(encoding="utf-8")
rows = re.findall(r"^\| \d+ \| `[0-9a-f]{7,}` \|", log, flags=re.M)
ck("commit log covers the baseline history",
   len(rows) >= index["repository"]["baselineCommitCount"] and baseline in log,
   "%d rows, baseline=%s" % (len(rows), baseline))

# 8. stale verdicts must not be repeated as current in the new docs
stale_phrases = ["حکم فعلی = DESIGN v4", "DESIGN v5 (حکم فعلی)"]
warning_words = ("بایگانی", "superseded", "⚠️", "قدیمی", "گمراه", "ادعا", "بنر", "stale")
for f in md_files:
    t = f.read_text(encoding="utf-8")
    bad = []
    for line in t.splitlines():
        for phrase in stale_phrases:
            if phrase in line and not any(w in line for w in warning_words):
                bad.append(phrase)
    ck("no stale verdict asserted in %s" % f.relative_to(ROOT), not bad, ", ".join(sorted(set(bad))))

# 9. README document table covers the index documents
for d in index.get("documents", []):
    if d["path"].startswith("docs/") or d["path"] in ("README.md", "AGENTS.md", "REPO_INDEX.json"):
        continue
    ck("README covers " + d["path"], d["path"] in readme)

passed = sum(1 for _, ok, _ in CHECKS if ok)
print("handoff docs: checks=%d passed=%d failed=%s" %
      (len(CHECKS), passed, FAILED if FAILED else "[]"))
sys.exit(1 if FAILED else 0)
