#!/usr/bin/env python3
"""MISSION-05 — DTO catalogue: every response/request type referenced by the API catalogue,
with its field list taken from the decompiled class (field names are author-visible because
Kotlin data classes keep field names in the DEX string pool).

Input : evidence/API_CATALOG_V2.csv, a decompiled source tree (default /tmp/dad)
Output: evidence/DTO_CATALOG.csv (+ stdout summary)
"""
from __future__ import annotations
import argparse, csv, os, re, sys, collections

DECL = re.compile(r"^\s*private final ([A-Za-z0-9_.$\[\]]+) (\w+);\s*$")


def descriptor_to_path(desc: str, root: str) -> str | None:
    if not desc.startswith("L"):
        return None
    name = desc[1:].rstrip(";")
    if "<" in name:
        name = name[:name.index("<")]
    return os.path.join(root, name.replace("/", ".") + ".java")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--catalog", default="evidence/API_CATALOG_V2.csv")
    ap.add_argument("--src", default="/tmp/dad")
    ap.add_argument("--csv", default="evidence/DTO_CATALOG.csv")
    args = ap.parse_args()

    rows = list(csv.DictReader(open(args.catalog, encoding="utf-8")))
    uses = collections.defaultdict(lambda: {"as_response": [], "as_request": []})
    for r in rows:
        if r["response_type"]:
            uses[r["response_type"]]["as_response"].append(f'{r["verb"]} {r["path"]}')
        if r["request_body_type"]:
            uses[r["request_body_type"]]["as_request"].append(f'{r["verb"]} {r["path"]}')
    out = []
    for desc, u in sorted(uses.items()):
        path = descriptor_to_path(desc, args.src)
        fields, found = [], False
        if path and os.path.exists(path):
            found = True
            for line in open(path, encoding="utf-8", errors="replace"):
                m = DECL.match(line)
                if m:
                    fields.append(f"{m.group(2)}:{m.group(1)}")
        out.append({"dto": desc,
                    "class_path": desc[1:].rstrip(";") if desc.startswith("L") else desc,
                    "source_found": found,
                    "n_fields": len(fields),
                    "fields": ";".join(fields),
                    "used_as_response": len(u["as_response"]),
                    "used_as_request": len(u["as_request"]),
                    "endpoints": " | ".join(sorted(set(u["as_response"] + u["as_request"]))[:4])})
    with open(args.csv, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(out[0]))
        w.writeheader(); w.writerows(out)
    print(f"DTO types referenced: {len(out)} | with source+fields: {sum(1 for o in out if o['n_fields'])}"
          f" | source missing: {sum(1 for o in out if not o['source_found'])}")
    for o in out[:12]:
        print(f"  {o['class_path'][:58]:58} fields={o['n_fields']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
