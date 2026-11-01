#!/usr/bin/env python3
"""Stage 11 — generate final/20_EVIDENCE_INDEX.md from the evidence artefacts.

Reads every JSON/CSV in evidence/ plus data/ summaries, prints a table of artefact ->
what it proves -> key counts, and writes the markdown file with stable evidence IDs.

Usage:
    python tools/build_evidence_index.py EVIDENCE_DIR FINAL_DIR [DATA_DIR]
"""
from __future__ import annotations

import csv
import gzip
import hashlib
import json
import os
import sys


def sha(path: str, limit: int = 0) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        while True:
            chunk = fh.read(1 << 20)
            if not chunk:
                break
            h.update(chunk)
    return h.hexdigest()[:16]


def count_rows(path: str) -> int:
    if path.endswith(".csv"):
        with open(path, newline="", encoding="utf-8") as fh:
            return max(sum(1 for _ in fh) - 1, 0)
    return 0


def main(ev: str, final: str, data: str | None = None) -> None:
    data = data or os.path.join(os.path.dirname(ev), "data")
    rows: list[tuple[str, str, str, str]] = []

    def add(fname: str, proves: str, numbers: str, ev_id: str) -> None:
        p = os.path.join(ev, fname)
        if not os.path.exists(p):
            return
        rows.append((ev_id, f"`evidence/{fname}`", proves, numbers))

    comp = json.load(open(os.path.join(ev, "components.json")))
    add("components.json", "manifest component inventory, exports, deep links",
        f"{len(comp['activities'])} activities, {len(comp['services'])} services, "
        f"{len(comp['providers'])} providers", "EV-MAN-001")
    add("manifest-decoded.xml", "raw decoded AndroidManifest", "full AXML", "EV-MAN-002")

    res = json.load(open(os.path.join(ev, "resources.json")))
    add("resources.json", "locale list, resource types, string catalogue",
        f"{res.get('strings_count','?')} strings, {len(res.get('locales',[]))} locales (incl. sentinel)", "EV-RES-001")
    add("resources-strings.xml", "verbatim app strings (state/behaviour vocabulary)", "1,721 strings", "EV-RES-002")

    dt = json.load(open(os.path.join(ev, "design-tokens.json")))
    add("design-tokens.json", "colours, dimensions, fonts, derived scales",
        f"{dt['colors']['count_app']} app colours, {dt['dimens']['count_app']} app dimens, "
        f"{len(dt['colors']['light_dark_pairs_inferred'])} inferred pairs", "EV-RES-003")

    scr = json.load(open(os.path.join(ev, "screens.json")))
    add("screens.json", "screen/modal/fragment/sheet inventory",
        f"{len(scr['activities'])} activities, {len(scr['modals'])} modals, "
        f"{len(scr['bottom_sheets'])} sheets, {scr['layout_files_count']} layouts", "EV-UI-001")

    inv = json.load(open(os.path.join(ev, "dex-inventory.json")))
    add("dex-inventory.json", "DEX file sizes and class counts",
        f"{len(inv)} dex files, {sum(i['classes'] for i in inv)} classes", "EV-DEX-001")

    with gzip.open(os.path.join(ev, "class-strings.json.gz"), "rt", encoding="utf-8") as fh:
        cs = json.load(fh)
    add("class-strings.json.gz", "per-class string literals (responsibility evidence)",
        f"{len(cs)} app classes", "EV-DEX-002")

    dc = json.load(open(os.path.join(ev, "data-contracts.json")))
    add("data-contracts.json", "recovered data-class field lists (API/progress contracts)",
        f"{len(dc)} contracts", "EV-DEX-003")

    fe = json.load(open(os.path.join(ev, "feature-evidence.json")))
    add("feature-evidence.json", "feature → class index",
        f"{len(fe)} features", "EV-DEX-004")

    li = json.load(open(os.path.join(ev, "literal-index.json")))
    add("literal-index.json", "literal → declaring classes (incl. obfuscated)",
        f"{len(li)} literals, {sum(len(v) for v in li.values())} pairs", "EV-DEX-005")

    ml = json.load(open(os.path.join(ev, "method-literals.json")))
    add("method-literals.json", "method-level literals for parser/lesson classes",
        f"{len(ml)} classes", "EV-DEX-006")

    cd = json.load(open(os.path.join(ev, "content-deep.json")))
    add("content-deep.json", "corpus conformance: DSL, offsets, integrity",
        f"{cd['en']['lessons']} lessons, {cd['dsl']['rangeChecks']['inBounds']} offsets in bounds, "
        f"{sum(cd['issueCounts'].values())} issues", "EV-CNT-001")
    for f, evid in (("tracks.csv", "EV-CNT-002"), ("tutorials.csv", "EV-CNT-003"),
                    ("lessons.csv", "EV-CNT-004"), ("languages.csv", "EV-CNT-005")):
        add(f, "per-entity inventory", f"{count_rows(os.path.join(ev, f))} rows", evid)

    add("retrofit-endpoints.json", "attempted annotation extraction (incomplete)",
        "0 rows — parser abandoned, see §21", "EV-API-009")

    print(f"indexed {len(rows)} artefacts")

    lines = ["# 20 — Evidence index", "",
             "Every claim in `final/00`…`final/21` is traceable to one of the artefacts below.",
             "IDs are stable and are referenced from the section text where precision matters.", "",
             "| Evidence ID | Artefact | What it proves | Measured content | SHA-256 (16) |",
             "|---|---|---|---|---|"]
    for evid, path, proves, numbers in rows:
        fname = path.strip("`").split("/", 1)[1]
        p = os.path.join(ev, fname)
        lines.append(f"| `{evid}` | {path} | {proves} | {numbers} | `{sha(p)}` |")
    lines += ["", "## Reproduce everything", "", "```bash",
              "python3 -m venv .venv && .venv/bin/pip install androguard==4.1.4",
              "# 1) split-archive reassembly (see README.md) → Mimo_9.35.apk",
              ".venv/bin/python tools/export_manifest_resources.py APK evidence",
              ".venv/bin/python tools/design_tokens.py APK evidence/design-tokens.json",
              ".venv/bin/python tools/screen_inventory.py ASSETS evidence",
              ".venv/bin/python tools/dex_evidence.py EXTRACTED evidence",
              ".venv/bin/python tools/literal_reverse_index.py EXTRACTED evidence/literal-index.json",
              ".venv/bin/python tools/content_deep.py ASSETS evidence",
              ".venv/bin/python tools/build_evidence_index.py evidence final",
              ".venv/bin/python tools/build_final_report.py final report.html",
              "```", "",
              "## Evidence classes used in this report", "",
              "| Class | Meaning | Where it dominates |",
              "|---|---|---|",
              "| **VERIFIED STATIC** | read directly from the APK (manifest, resources, DEX literals, "
              "bundled content) with a reproducible command | §01, §04, §05, §06, §13, §14 |",
              "| **VERIFIED RUNTIME** | not used — no instrumented session was performed | — |",
              "| **INFERRED** | reasoned from verified artefacts, labelled `(I)` at the point of use | §02 states, "
              "§07 server grading, §08 prompt assembly, §09 thresholds |",
              "| **UNKNOWN** | stated as unknown, collected in §21 | §15 precedence, §21 (12 questions) |", ""]
    open(os.path.join(final, "20_EVIDENCE_INDEX.md"), "w").write("\n".join(lines))
    print("wrote", os.path.join(final, "20_EVIDENCE_INDEX.md"))


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else None)
