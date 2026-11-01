#!/usr/bin/env python3
"""Verify that the HANDOFF package is internally consistent.

Layer A of HANDOFF/11_ACCEPTANCE_TESTS.md. Deterministic, no network, stdlib only.

    python3 HANDOFF/tools/verify_handoff.py                 # run all checks
    python3 HANDOFF/tools/verify_handoff.py --update-manifest  # re-hash data/ into MANIFEST.json
    python3 HANDOFF/tools/verify_handoff.py --quiet         # only failures + summary

Exit code 0 when every check passes, 1 otherwise.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

HANDOFF = Path(__file__).resolve().parent.parent
REPO = HANDOFF.parent
DATA = HANDOFF / "data"
MISSION08 = REPO / "mimo-re" / "mission-08"

# data/ files whose copies are pinned in MANIFEST.json (documentation-only edits do not affect these)
PINNED = [
    "content_schema.json", "dsl_grammar.ebnf", "dsl_ast_schema.json", "grading_vectors.json",
    "progress_vectors.json", "room_schema.json", "endpoint_catalog.json", "client_inventory.json",
    "interaction_variants.json", "questions_closure.json", "coverage_matrix.csv",
    "dsl_tags.json", "learner_model.json", "spec_deltas.json",
]

REQUIRED_DOCS = [f"{n:02d}" for n in ()]  # filled below
DOC_NAMES = [
    "START_HERE.md", "AGENT_BRIEF.md", "01_WHAT_MIMO_IS.md", "02_SPEC_CONTENT_MODEL.md",
    "03_SPEC_LESSON_DSL.md", "04_SPEC_INTERACTION_AND_GRADING.md", "05_SPEC_LEARNER_MODEL.md",
    "06_SPEC_STORAGE.md", "07_SPEC_API_AND_AUTH.md", "08_SPEC_STREAMING_AND_TUTOR.md",
    "09_SPEC_ANALYTICS_CONFIG_ENTITLEMENTS.md", "10_BUILD_THE_MIMO_PROJECT.md",
    "11_ACCEPTANCE_TESTS.md", "12_DELTA_REGISTER.md", "13_KNOWN_UNKNOWNS.md", "14_TRACEABILITY.md",
    "15_GLOSSARY.md",
]

SECRET_PATTERNS = [
    re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
    re.compile(r"\bAIza[0-9A-Za-z_\-]{35}\b"),
    re.compile(r"\bghp_[0-9A-Za-z]{36}\b"),
    re.compile(r"\bgithub_pat_[0-9A-Za-z_]{20,}\b"),
    re.compile(r"\bsk-[A-Za-z0-9]{32,}\b"),
    re.compile(r"\bxox[baprs]-[0-9A-Za-z-]{10,}\b"),
    re.compile(r"eyJ[A-Za-z0-9_\-]{10,}\.[A-Za-z0-9_\-]{10,}\.[A-Za-z0-9_\-]{10,}"),  # JWT literal
    re.compile(r"(?i)\b(password|passwd|secret|api[_-]?key|access[_-]?token)\s*[:=]\s*['\"]?[A-Za-z0-9/+_\-]{16,}"),
]

RESULTS: list[tuple[str, bool, str]] = []


def check(cid: str, ok: bool, detail: str = "") -> None:
    RESULTS.append((cid, ok, detail))


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def load(name: str):
    with open(DATA / name, encoding="utf-8") as fh:
        return json.load(fh)


def resolvable(ref: str) -> bool:
    """A mission evidence reference may be repo-root-relative or mission-08-relative."""
    ref = ref.strip().strip("`")
    if not ref or ref in ("—", "-"):
        return True  # no anchor cited; not a broken link
    ref = ref.split(" §")[0].split(" ")[0].rstrip(",")
    for base in (REPO, MISSION08, REPO / "mimo-re"):
        if (base / ref).exists():
            return True
    # allow directory prefixes with trailing slash and wildcard-ish anchors
    part = ref.rstrip("/*")
    for base in (REPO, MISSION08, REPO / "mimo-re"):
        if (base / part).exists():
            return True
    # allow an anchor that names a file by prefix (e.g. "12_UI_RESOURCES/75" -> 75_*.md)
    parent, _, stem = part.rpartition("/")
    for base in (REPO, MISSION08, REPO / "mimo-re"):
        d = base / parent
        if d.is_dir() and stem and any(p.name.startswith(stem) for p in d.iterdir()):
            return True
    return False


def update_manifest() -> None:
    entries = []
    for name in PINNED:
        path = DATA / name
        if not path.exists():
            print(f"! missing pinned file: {name}")
            continue
        entries.append({"file": name, "sha256": sha256(path), "bytes": path.stat().st_size})
    manifest = {
        "generated": "2026-11-01",
        "purpose": "hash-pinned machine-readable artifacts for the HANDOFF package",
        "repo": "danmillman008-hub/game",
        "branch": "arena/ecb8af07-game",
        "apk_sha256": "48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a",
        "count": len(entries),
        "artifacts": entries,
    }
    with open(DATA / "MANIFEST.json", "w", encoding="utf-8") as fh:
        json.dump(manifest, fh, indent=2)
        fh.write("\n")
    print(f"manifest updated: {len(entries)} artifacts")


def run() -> int:
    # A-01 manifest integrity
    manifest = load("MANIFEST.json")
    bad = []
    for item in manifest["artifacts"]:
        path = DATA / item["file"]
        if not path.exists():
            bad.append(f"{item['file']}: missing")
        elif sha256(path) != item["sha256"]:
            bad.append(f"{item['file']}: sha256 mismatch")
    pinned = {p for p in PINNED if (DATA / p).exists()}
    listed = {i["file"] for i in manifest["artifacts"]}
    for name in sorted(pinned - listed):
        bad.append(f"{name}: not pinned in MANIFEST.json")
    check("A-01", not bad, "; ".join(bad) or f"{len(manifest['artifacts'])} artifacts verified")

    # A-02 source paths resolve
    missing_src = [i["file"] for i in manifest["artifacts"]
                   if i.get("source_path") and not resolvable(i["source_path"])
                   and not (REPO / i["source_path"]).exists()]
    check("A-02", not missing_src, f"{len(manifest['artifacts'])} source paths" if not missing_src
          else "; ".join(missing_src))

    # A-03 parseability
    errs = []
    for path in sorted(DATA.iterdir()):
        if path.suffix == ".json":
            try:
                json.loads(path.read_text(encoding="utf-8"))
            except Exception as exc:  # noqa: BLE001
                errs.append(f"{path.name}: {exc}")
        elif path.suffix in (".ebnf", ".csv") and path.stat().st_size == 0:
            errs.append(f"{path.name}: empty")
    check("A-03", not errs, "; ".join(errs) or "all data files parse / are non-empty")

    # A-04 delta register
    d = load("spec_deltas.json")
    rows = d["domain_decisions"]
    vocab = set(d["decision_vocabulary"])
    ids = [r["domain_id"] for r in rows]
    problems = []
    if len(rows) != 45:
        problems.append(f"{len(rows)} domain decisions (expected 45)")
    if sorted(ids) != [f"D-{i:02d}" for i in range(1, 46)]:
        problems.append("domain ids are not D-01..D-45")
    bad_vocab = [r["domain_id"] for r in rows if r["decision"] not in vocab]
    if bad_vocab:
        problems.append("bad decision in " + ",".join(bad_vocab))
    counts = {}
    for r in rows:
        counts[r["decision"]] = counts.get(r["decision"], 0) + 1
    declared = {k: d["counts"][k] for k in counts}
    if counts != declared:
        problems.append(f"counts {counts} != declared {d['counts']}")
    check("A-04", not problems, "; ".join(problems) or
          f"45 decisions, {d['counts']}")

    # A-05 additions
    adds = d["additions"]
    add_ids = [a["id"] for a in adds]
    ok5 = add_ids == [f"ADD-{i:02d}" for i in range(1, 9)]
    check("A-05", ok5, f"{len(adds)} additions {add_ids[0]}..{add_ids[-1]}" if ok5 else str(add_ids))

    # A-06 vector internal consistency
    problems = []
    g = load("grading_vectors.json")
    expectations = {
        "normaliser": "expected", "validated_input_verdict": "verdict", "selection_verdict": "verdict",
        "fill_the_gap_verdict": "verdict", "spell_verdict": "verdict", "module_visibility": "rendered",
        "progress_completion": "solved", "output_parsing": "parsed",
    }
    for section, key in expectations.items():
        vs = g[section]["vectors"]
        if not vs:
            problems.append(f"grading/{section}: empty")
        for i, v in enumerate(vs):
            if key not in v:
                problems.append(f"grading/{section}[{i}]: no {key}")
    p = load("progress_vectors.json")
    for section in ("identity", "new_progress", "ordering_guard", "counter_update", "completion_flag",
                    "queue", "retrieval", "answers_in_chapter", "first_try_count", "version_change"):
        if not p[section]["vectors"]:
            problems.append(f"progress/{section}: empty")
    check("A-06", not problems, "; ".join(problems) or "vectors carry expectations")

    # A-07 evidence anchors resolve
    bad = []
    for r in rows:
        anchor = r.get("evidence_anchor", "")
        if not resolvable(anchor) and not (REPO / anchor).exists():
            bad.append(f"{r['domain_id']}:{anchor}")
    for a in adds:
        src = a.get("source", "")
        if src and src != "same" and not resolvable(src) and not (REPO / src).exists():
            bad.append(f"{a['id']}:{src}")
    check("A-07", not bad, "; ".join(bad) or f"{len(rows) + len(adds)} anchors resolve")

    # A-08 required docs
    missing = [n for n in DOC_NAMES if not (HANDOFF / n).exists()]
    check("A-08", not missing, "; ".join(missing) or f"{len(DOC_NAMES)} documents present")

    # A-09 no secret-shaped material
    hits = []
    for path in sorted(HANDOFF.rglob("*")):
        if not path.is_file() or path.suffix in (".pyc",):
            continue
        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
        except Exception:  # noqa: BLE001
            continue
        for pat in SECRET_PATTERNS:
            for m in pat.finditer(text):
                hits.append(f"{path.relative_to(HANDOFF)}: {m.group(0)[:24]}")
    check("A-09", not hits, "; ".join(hits) or "no secret-shaped strings")

    # A-10 tag counts reconcile
    tags = load("dsl_tags.json")
    total = sum(tags["corpus"]["tag_counts"].values())
    declared_total = tags["corpus"]["tag_occurrences"]
    ok10 = total == declared_total and tags["enum_count"] == len(tags["enum_constants"])
    check("A-10", ok10, f"{total} occurrences over {tags['corpus']['distinct_tags']} tags, "
                         f"{tags['enum_count']} enum constants" if ok10
          else f"sum {total} != {declared_total}")

    return report()


def report() -> int:
    failed = [r for r in RESULTS if not r[1]]
    width = max(len(c) for c, _, _ in RESULTS)
    for cid, ok, detail in RESULTS:
        print(f"[{'PASS' if ok else 'FAIL'}] {cid.ljust(width)}  {detail}")
    print(f"\n{len(RESULTS) - len(failed)}/{len(RESULTS)} checks passed")
    return 1 if failed else 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--update-manifest", action="store_true", help="re-hash data/ into MANIFEST.json")
    ap.add_argument("--quiet", action="store_true", help="print only failures")
    args = ap.parse_args()
    if args.update_manifest:
        update_manifest()
        return 0
    if args.quiet:
        code = run()
        for cid, ok, detail in RESULTS:
            if not ok:
                print(f"[FAIL] {cid} {detail}")
        return code
    return run()


if __name__ == "__main__":
    sys.exit(main())
