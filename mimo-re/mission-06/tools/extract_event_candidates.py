#!/usr/bin/env python3
"""MISSION-06 — build an *evidence-graded* candidate register for analytics event names.

Mission-05 correctly established that the app's `Analytics` assembler class is absent from the
recovered DEX, so a definitive event list cannot be produced statically. What CAN be produced is a
call-site register: every snake_case literal with the class/method that carries it, plus
context flags that separate plausible event names from property keys and unrelated strings.

Context flags per literal occurrence:
  analytics_props   the enclosing method references com.getmimo.analytics.properties.*  (payload built)
  analytics_class   the enclosing class is in com.getmimo.analytics.*
  sdk_track         the enclosing method references np.h / oy.t / firebase analytics (dispatch handle)
This is the strongest static signal available and is deliberately reported as INFERRED.

Output: CSV + JSON summary. Deterministic, read-only.
"""
from __future__ import annotations

import argparse
import collections
import csv
import glob
import json
import os
import re
import sys

LIT = re.compile(r'"([a-z][a-z0-9]*(?:_[a-z0-9]+){1,5})"')
METHOD = re.compile(r'^    (?:public|private|protected|final|static|synthetic|\s)+[A-Za-z0-9_.$\[\]<>]+ ([a-zA-Z0-9_]+)\(')


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", default="/tmp/dad")
    ap.add_argument("--csv", required=True)
    ap.add_argument("--json", required=True)
    a = ap.parse_args()
    rows = []
    for path in sorted(glob.glob(os.path.join(a.src, "**", "*.java"), recursive=True)):
        cls = os.path.basename(path)[:-5]
        try:
            lines = open(path, encoding="utf-8", errors="replace").read().splitlines()
        except Exception:
            continue
        method = "<clinit>"
        analytics_class = cls.startswith("com.getmimo.analytics.")
        for i, line in enumerate(lines, 1):
            m = METHOD.match(line)
            if m:
                method = m.group(1)
            for lit in LIT.finditer(line):
                name = lit.group(1)
                if not 6 <= len(name) <= 48:
                    continue
                window = "\n".join(lines[max(0, i - 40):i + 40])
                rows.append({
                    "literal": name,
                    "class": cls,
                    "method": method,
                    "line": i,
                    "analytics_class": analytics_class,
                    "analytics_props": "analytics.properties" in window or "analytics.properties" in line,
                    "sdk_track": any(k in window for k in ("np.h", "oy.t", "FirebaseAnalytics", "com.adjust.sdk")),
                })
    with open(a.csv, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    uniq = collections.Counter(r["literal"] for r in rows)
    graded = collections.Counter(r["literal"] for r in rows if r["analytics_props"] or r["sdk_track"])
    summary = {
        "occurrences": len(rows),
        "unique_literals": len(uniq),
        "unique_with_analytics_context": len(graded),
        "classes": len({r["class"] for r in rows}),
        "top_literals": uniq.most_common(20),
    }
    json.dump(summary, open(a.json, "w", encoding="utf-8"), indent=1)
    print(json.dumps(summary, indent=1)[:900])
    return 0


if __name__ == "__main__":
    sys.exit(main())
