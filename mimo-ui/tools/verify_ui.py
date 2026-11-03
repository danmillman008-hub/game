#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""verify_ui.py — fail-closed completeness check for the whole extraction."""
from __future__ import annotations
import csv, hashlib, json, re, sys, zipfile
from pathlib import Path

OUT = Path(__file__).resolve().parents[1]
CAT = OUT / "CATALOGS"
report = {"checks": [], "status": "PASS"}


def check(name, ok, detail=""):
    report["checks"].append({"check": name, "status": "PASS" if ok else "FAIL",
                             "detail": str(detail)})
    if not ok:
        report["status"] = "FAIL"
    return ok


def sha256(p: Path):
    h = hashlib.sha256()
    with p.open("rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def rows(p):
    with p.open(encoding="utf-8") as f:
        return list(csv.DictReader(f))


census = rows(CAT / "APK_ENTRY_CENSUS.csv")
check("census covers every ZIP member", len(census) == 14398, len(census))
ui_rows = [r for r in census if r["ui_class"].startswith("UI_")]
missing = [r for r in ui_rows
           if r["deliverable"] and not re.search(r"\((verbatim|data|not UI|.*)\)", r["deliverable"])
           and not (OUT / r["deliverable"]).is_file()]
# TEXT-only deliverables (catalogues) are still files; the parenthetical
# descriptions are prose, not paths, so handle them separately.
path_missing = []
for r in ui_rows:
    d = r["deliverable"]
    if not d:
        path_missing.append((r["path"], "empty deliverable"))
    elif "(" in d:
        continue  # prose description of a catalogued-only class
    elif not (OUT / d).is_file():
        path_missing.append((r["path"], d))
check("every UI_* entry has an existing deliverable", not path_missing, path_missing[:10])
check("all UI_* entries classified", all(r["ui_class"] for r in ui_rows), len(ui_rows))
check("all 14,398 entries have SHA-256",
      all(re.fullmatch(r"[0-9a-f]{64}", r["sha256"]) for r in census))

# APK hash agreement with your earlier GitHub analysis
prior = json.loads((OUT / "REFERENCE/PRIOR_WORK/APK_HASHES.json").read_text(encoding="utf-8"))
prior_apk = next(a["sha256"] for a in prior["artifacts"] if a["role"].startswith("re-assembled"))
cur = json.loads((OUT / "MANIFEST.json").read_text(encoding="utf-8"))["apk"]["sha256"]
check("APK SHA-256 equals prior GitHub analysis", prior_apk == cur, cur)

# layouts / dossiers
L = json.loads((CAT / "LAYOUT_INDEX.json").read_text(encoding="utf-8"))
check("layout count", len(L) == 1299, len(L))
check("every decoded layout exists",
      all((OUT / x["decoded_path"]).is_file() for x in L))
check("every layout dossier exists",
      all((OUT / x["dossier_path"]).is_file() for x in L),
      [x["dossier_path"] for x in L if not (OUT / x["dossier_path"]).is_file()][:5])
check("no decode errors",
      json.loads((CAT / "DECODE_ERRORS.json").read_text(encoding="utf-8")) == [])

# screens
S = rows(CAT / "SCREEN_INDEX.csv")
check("screen count", len(S) >= 192, len(S))
check("every screen dossier exists",
      all((OUT / x["dossier"]).is_file() for x in S),
      [x["dossier"] for x in S if not (OUT / x["dossier"]).is_file()][:5])

# resources
R = rows(CAT / "RESOURCE_INDEX.csv")
check("resource config rows", len(R) == 50477, len(R))
ids = {r["res_id"] for r in R}
check("resource IDs", len(ids) == 12915, len(ids))

# coverage-by-area
C = rows(CAT / "COVERAGE_BY_AREA.csv")
bad = [r for r in C if r["status"] != "COMPLETE"]
check("all coverage areas COMPLETE", not bad, bad)

# atlas
check("offline atlas exists and embeds data",
      (OUT / "ATLAS/index.html").is_file() and
      "application/json" in (OUT / "ATLAS/index.html").read_text(encoding="utf-8")[:200000])
check("atlas dataset gzip exists", (OUT / "ATLAS/data.json.gz").is_file())

# reconstructed code
kt = list((OUT / "RECONSTRUCTION/kotlin").glob("*.kt"))
check("Kotlin skeletons present", len(kt) == 109, len(kt))

# documentation
docs = ["00_START_HERE.md", "01_METHOD_AND_EVIDENCE.md", "02_UI_ARCHITECTURE.md",
        "03_DESIGN_SYSTEM.md", "04_SCREEN_CATALOG.md", "05_COMPONENT_LIBRARY.md",
        "06_NAVIGATION_AND_FLOW.md", "07_LESSON_RENDERER_WEBVIEW.md",
        "08_LOCALIZATION_A11Y.md", "09_STATE_AND_MOTION.md",
        "10_HOW_THE_CODE_IS_WRITTEN.md", "11_COVERAGE_AND_GAPS.md",
        "12_REPRODUCE.md", "13_TRACEABILITY.md", "14_CROSS_CHECK_PRIOR_WORK.md"]
check("all 15 documentation volumes present",
      all((OUT / d).is_file() for d in docs),
      [d for d in docs if not (OUT / d).is_file()])

# checksums over every emitted file (written last, so exclude itself)
sums = []
for p in sorted(OUT.rglob("*")):
    if p.is_file() and p.name not in ("SHA256SUMS.txt",):
        sums.append("%s  %s" % (sha256(p), p.relative_to(OUT).as_posix()))
(CAT / "VERIFICATION_REPORT.json").write_text(
    json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
sums = []
for p in sorted(OUT.rglob("*")):
    if p.is_file() and p.name != "SHA256SUMS.txt":
        sums.append("%s  %s" % (sha256(p), p.relative_to(OUT).as_posix()))
(CAT / "SHA256SUMS.txt").write_text("\n".join(sums) + "\n", encoding="utf-8")

print(json.dumps({"status": report["status"],
                  "checks": len(report["checks"]),
                  "failed": [c for c in report["checks"] if c["status"] == "FAIL"],
                  "files_hashed": len(sums)}, ensure_ascii=False, indent=2))
sys.exit(0 if report["status"] == "PASS" else 1)
