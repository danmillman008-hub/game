#!/usr/bin/env python3
"""MISSION-06 — dump Kotlin data-class field lists from decompiled sources.

Field names survive obfuscation for data classes (they are referenced by kotlinx.serialization /
Parcelize / Gson), so a field dump is trustworthy evidence for content models and wire DTOs — unlike
method bodies, which must be read case by case.

Input : a source tree (default /tmp/dad) and a list of fully-qualified class names (or --all-content /
--from-csv). Output: JSON {class: {fields:[{type,name}], source, lines}}.
"""
from __future__ import annotations

import argparse
import csv
import json
import os
import re
import sys

FIELD = re.compile(r"^\s+(?:private|public|protected) (?:final|static final) ([A-Za-z0-9_.$<>\[\], ?]+?) ([A-Za-z0-9_$]+);\s*$")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", default="/tmp/dad")
    ap.add_argument("--classes", nargs="*", default=[])
    ap.add_argument("--from-csv", default="")
    ap.add_argument("--out", required=True)
    a = ap.parse_args()

    names = list(a.classes)
    if a.from_csv:
        for row in csv.DictReader(open(a.from_csv, encoding="utf-8")):
            dto = row.get("class_path") or row.get("class") or ""
            if dto:
                names.append(dto.replace("/", "."))
    seen, out = set(), {}
    for n in names:
        if n in seen:
            continue
        seen.add(n)
        p = os.path.join(a.src, n + ".java")
        if not os.path.exists(p):
            out[n] = {"found": False, "fields": []}
            continue
        fields = []
        for line in open(p, encoding="utf-8", errors="replace"):
            m = FIELD.match(line)
            if m and not m.group(2).startswith("$"):
                fields.append({"type": m.group(1).strip(), "name": m.group(2)})
        out[n] = {"found": True, "fields": fields, "source": p}
    json.dump(out, open(a.out, "w", encoding="utf-8"), indent=1)
    ok = sum(1 for v in out.values() if v["found"])
    withf = sum(1 for v in out.values() if v["fields"])
    print(f"classes={len(out)} found={ok} with_fields={withf}")
    for n, v in list(out.items())[:12]:
        print(f"  {n.split('.')[-1]:34} {'MISSING' if not v['found'] else str(len(v['fields'])) + ' fields'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
