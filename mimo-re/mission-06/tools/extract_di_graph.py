#!/usr/bin/env python3
"""MISSION-06 — recover the dependency-injection graph from the obfuscated Dagger/Hilt factory.

`Lae/m;` implements the app's component factory: one `switch` whose every `case N:` provides exactly
one object. Reading it yields the *actual* dependency graph (who constructs whom) plus concrete
configuration that is otherwise invisible (OkHttp timeouts, interceptor chains, base URL selection,
Gson adapters).

Input : a decompiled source tree (default /tmp/dad) and the class name (default ae.m).
Output: JSON with one record per case: provided type, constructor args, string literals, singleton
        provider calls (`this.a.X.get()`), and the raw case body for audit.
Deterministic; no network; read-only.
"""
from __future__ import annotations

import argparse
import json
import re
import sys

CASE = re.compile(r"^\s{8,}case (\d+):\s*$")
RETURN_NEW = re.compile(r"return new ([A-Za-z0-9_.$]+)")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", default="/tmp/dad/ae.m.java")
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    lines = open(a.src, encoding="utf-8", errors="replace").read().splitlines()

    starts = [(i, int(m.group(1))) for i, l in enumerate(lines) if (m := CASE.match(l))]
    cases = []
    for idx, (i, num) in enumerate(starts):
        end = starts[idx + 1][0] if idx + 1 < len(starts) else len(lines)
        body = "\n".join(lines[i:end])
        provided = RETURN_NEW.findall(body)
        # constructor argument types: `new T(a, b, c)` is not reliable in DAD output, so record
        # every type mentioned and every provider lookup instead.
        mentions = sorted(set(re.findall(r"\b(?:com\.getmimo|androidx|okhttp3|retrofit2|com\.google|io\.)\.[A-Za-z0-9_.$]+", body)))
        providers = sorted(set(re.findall(r"this\.a\.(\w+)\.get\(\)", body)))
        literals = sorted(set(re.findall(r'"([^"]{2,160})"', body)))
        cases.append({
            "case": num,
            "lines": [i + 1, end],
            "provides": provided,
            "providers_used": providers,
            "types_mentioned": mentions,
            "string_literals": literals,
            "body": body,
        })
    out = {"source": a.src, "cases": len(cases), "providers": cases,
           "note": "DAD pseudo-Java: 'provides' is the type after `return new`; providers_used are "
                   "call sites on the component's lazy provider map (this.a.X.get()), i.e. real edges."}
    json.dump(out, open(a.out, "w", encoding="utf-8"), indent=1)
    named = sum(1 for c in cases if c["provides"])
    print(f"cases={len(cases)} with_construct={named} with_literals={sum(1 for c in cases if c['string_literals'])}")
    for c in cases:
        p = ",".join(x.split(".")[-1] for x in c["provides"]) or "(not a constructor)"
        lit = f"  «{c['string_literals'][0][:44]}»" if c["string_literals"] else ""
        print(f"  case {c['case']:>3}: {p[:64]:64}{lit}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
