#!/usr/bin/env python3
"""MISSION-06 — recover the lesson-XML grammar mechanically from the parser classes.

For every class in the parser package (`te/*` by default) extract, per method:
  * `require(depth, ns, "tag")` calls  -> structural expectations (START=2 / END=3)
  * `getName()` comparisons           -> which child tags are accepted
  * `getAttributeValue(ns, "x")`      -> attribute reads
  * `new <Model>(...)` returns        -> AST node produced
This turns 700 lines of pseudo-Java into a checkable grammar table without trusting class names.

Output: JSON (per class/method records) + stdout summary. Deterministic, read-only.
"""
from __future__ import annotations

import argparse
import glob
import json
import os
import re
import sys

RE_REQUIRE = re.compile(r'require\(\s*(\d+)\s*,\s*([^,]+),\s*"([^"]+)"\s*\)')
RE_ATTR = re.compile(r'getAttributeValue\([^,]+,\s*"([^"]+)"\)')
RE_TAGNAME = re.compile(r'\.c\(p\d+\.getName\(\),\s*"([^"]+)"\)|getName\(\),\s*"([^"]+)"')
RE_NEW = re.compile(r'return new (com\.getmimo\.data\.content\.lessonparser\.interactive\.model\.[A-Za-z0-9_.$]+)')
RE_METHOD = re.compile(r'^    public (?:final |static |synthetic )*([A-Za-z0-9_.$\[\]]+) ([a-zA-Z0-9_]+)\((.*)\)$')
RE_COMPARE_TAG = re.compile(r'new com\.getmimo\.data\.content\.lessonparser\.interactive\.model\.Tag\("([A-Z_]+)"')


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", default="/tmp/dad")
    ap.add_argument("--prefix", default="te.")
    ap.add_argument("--json", required=True)
    a = ap.parse_args()
    out = []
    for path in sorted(glob.glob(os.path.join(a.src, a.prefix + "*.java"))):
        cls = os.path.basename(path)[:-5]
        text = open(path, encoding="utf-8", errors="replace").read()
        cur = {"class": cls, "file": path, "methods": []}
        for line in text.splitlines():
            m = RE_METHOD.match(line)
            if m:
                cur["methods"].append({"returns": m.group(1), "name": m.group(2),
                                       "params": m.group(3), "requires": [], "attributes": [],
                                       "child_tags": [], "produces": [], "lines": 0})
            if not cur["methods"]:
                continue
            mm = cur["methods"][-1]
            mm["lines"] += 1
            for d, ns, tag in RE_REQUIRE.findall(line):
                mm["requires"].append({"event": int(d), "tag": tag})
            for at in RE_ATTR.findall(line):
                if at not in mm["attributes"]:
                    mm["attributes"].append(at)
            for g in RE_TAGNAME.findall(line):
                tag = g[0] or g[1]
                if tag and tag not in mm["child_tags"]:
                    mm["child_tags"].append(tag)
            for pr in RE_NEW.findall(line):
                mm["produces"].append(pr)
        out.append(cur)
    json.dump({"prefix": a.prefix, "classes": out}, open(a.json, "w", encoding="utf-8"), indent=1)
    print(f"parser classes: {len(out)}")
    for c in out:
        for m in c["methods"]:
            req = ",".join(f'{r["tag"]}@{r["event"]}' for r in m["requires"])
            prod = ",".join(p.split(".")[-1] for p in m["produces"])
            print(f'  {c["class"]:8} {m["name"]:22} produces={prod[:40]:40} require=[{req}] '
                  f'children={m["child_tags"]} attrs={m["attributes"]}')
    return 0


if __name__ == "__main__":
    sys.exit(main())
