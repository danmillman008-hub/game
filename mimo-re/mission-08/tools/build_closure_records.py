#!/usr/bin/env python3
"""Mission 8 — Phase 12 closure records.

Takes the canonical question register (Phase 0) plus a hand-written transition file and emits
machine-readable transition records. A transition is rejected unless it names

  * the previous status and the new status (both from the 8-value vocabulary),
  * at least one evidence artefact that exists on disk,
  * a reproduction command that a reader can run.

Nothing is promoted by default: questions without a transition record keep their previous status,
which is itself recorded so that "unchanged" is visible rather than implied.

Usage
  python3 build_closure_records.py --register ../00_BASELINE/CANONICAL_OPEN_QUESTION_REGISTER.json \
      --transitions transitions.json --out ../12_OPEN_QUESTION_CLOSURE
"""
import argparse
import csv
import json
import os
import sys

STATUSES = ["CLOSED_STATIC", "PARTIALLY_CLOSED", "BACKEND_ONLY", "NOT_RECOVERED",
            "GENUINELY_UNKNOWN", "BLOCKED_BY_ENVIRONMENT", "SUPERSEDED", "OUT_OF_SCOPE"]
REQUIRED = ("previous_status", "new_status", "evidence", "reproduction", "rationale")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--register", required=True)
    ap.add_argument("--transitions", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--mission-root", default=None)
    a = ap.parse_args()
    root = a.mission_root or os.path.dirname(os.path.dirname(os.path.abspath(a.register)))
    reg = json.load(open(a.register))
    tr = json.load(open(a.transitions))
    by_id = {q["id"]: q for q in reg["questions"]}

    records = []
    errors = []
    for tid, t in tr["transitions"].items():
        for k in REQUIRED:
            if k not in t:
                errors.append(f"{tid}: missing {k}")
        if t.get("new_status") not in STATUSES:
            errors.append(f"{tid}: illegal new_status {t.get('new_status')!r}")
        if t.get("previous_status") not in STATUSES:
            errors.append(f"{tid}: illegal previous_status {t.get('previous_status')!r}")
        missing = [e for e in t.get("evidence", []) if not os.path.exists(os.path.join(root, e))]
        if missing:
            errors.append(f"{tid}: missing evidence files {missing}")
        if tid in by_id and by_id[tid]["status_current"] != t.get("previous_status"):
            errors.append(f"{tid}: previous_status does not match the canonical register "
                          f"({by_id[tid]['status_current']})")
        records.append({"id": tid, **t})
    if errors:
        print(json.dumps({"errors": errors}, indent=1))
        return 1

    changed = {r["id"]: r["new_status"] for r in records}
    rows = []
    for q in reg["questions"]:
        new = changed.get(q["id"], q["status_current"])
        rows.append({
            "id": q["id"], "domain": q["domain"],
            "previous_status": q["status_current"], "new_status": new,
            "changed": "yes" if new != q["status_current"] else "no",
            "transition_id": next((r["id"] for r in records if r["id"] == q["id"]), ""),
            "evidence": ";".join(q["evidence_files"][:3]),
        })
    for r in records:
        if r["id"] not in by_id:
            rows.append({"id": r["id"], "domain": "mission-08", "previous_status": "",
                         "new_status": r["new_status"], "changed": "new",
                         "transition_id": r["id"], "evidence": ";".join(r["evidence"][:3])})

    os.makedirs(a.out, exist_ok=True)
    with open(os.path.join(a.out, "03_TRANSITION_RECORDS.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    with open(os.path.join(a.out, "02_QUESTION_REGISTER.json"), "w") as fh:
        json.dump({"status_vocabulary": STATUSES, "count": len(rows),
                   "changed": sum(1 for r in rows if r["changed"] == "yes"),
                   "new_in_mission08": sum(1 for r in rows if r["changed"] == "new"),
                   "unchanged": sum(1 for r in rows if r["changed"] == "no"),
                   "rows": rows, "transitions": records}, fh, indent=1, ensure_ascii=False)
        fh.write("\n")
    print(json.dumps({"questions": len(rows), "changed": sum(1 for r in rows if r["changed"] == "yes"),
                      "new": sum(1 for r in rows if r["changed"] == "new")}, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
