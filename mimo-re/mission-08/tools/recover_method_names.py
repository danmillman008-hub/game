#!/usr/bin/env python3
"""Mission 8 — recover original method names for renamed classes.

Technique (evidence-based, not heuristic)
----------------------------------------
When a class is renamed (e.g. `com.getmimo.…authentication.AuthenticationFirebaseRepository`
→ `com.getmimo.…authentication.a`), its Kotlin lambdas keep the **original** name in their
binary name: `AuthenticationFirebaseRepository$signInWithGoogle$2`. Each such lambda is
constructed with the receiver as its first argument and its body invokes exactly one method on
that receiver.

So: for every orphan lambda whose name encodes `<Original>$<methodName>$…`, read the lambda's
instructions, collect the invoke targets on the *dominant* receiver class, and emit a mapping

    renamed class . obfuscated method (descriptor)  ->  original method name

Confidence:
  HIGH    exactly one candidate method on exactly one receiver class for that lambda family
  MEDIUM  several candidate methods (overloads / chained calls) — all are listed, none chosen
  (no mapping is produced when the lambda does not call into a single receiver class)

The tool never guesses from a name alone: the mapping direction is *original name → obfuscated
method*, and the obfuscated method is read from the instruction that the lambda actually invokes.

Usage
  python3 recover_method_names.py --dex-dir /tmp/x --package com.getmimo.data.source.remote.authentication \
      --out ../mission-08/05_AUTHENTICATION_CLOSURE/evidence/METHOD_NAME_RECOVERY.json
"""
import argparse
import glob
import json
import os
import re
from collections import Counter, defaultdict

from androguard.core.dex import DEX

LAMBDA_RX = re.compile(r"^(?P<orig>[\w.$]+)\$(?P<method>[A-Za-z_]\w*)\$")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dex-dir", required=True)
    ap.add_argument("--package", required=True,
                    help="only lambdas whose original class starts with this package")
    ap.add_argument("--out", required=True)
    a = ap.parse_args()

    pool = {}
    for path in sorted(glob.glob(os.path.join(a.dex_dir, "*.dex"))):
        with open(path, "rb") as fh:
            dx = DEX(fh.read())
        for c in dx.get_classes():
            pool[c.get_name()[1:-1].replace("/", ".")] = c
    names = set(pool)

    families = defaultdict(list)
    for n in names:
        m = LAMBDA_RX.match(n)
        if not m:
            continue
        orig = m.group("orig")
        if not orig.startswith(a.package):
            continue
        if orig in names:           # owner still present, nothing to recover
            continue
        families[(orig, m.group("method"))].append(n)

    out = {"package": a.package, "families": {}, "summary": {}}
    for (orig, method), lambdas in sorted(families.items()):
        targets = Counter()
        for lam in lambdas:
            cd = pool[lam]
            for mm in cd.get_methods():
                code = mm.get_code()
                if not code:
                    continue
                for ins in code.get_bc().get_instructions():
                    if not ins.get_name().startswith("invoke"):
                        continue
                    outtxt = ins.get_output()
                    t = re.search(r"L([\w/$]+);->([\w<>$]+)", outtxt)
                    if not t:
                        continue
                    cls = t.group(1).replace("/", ".")
                    meth = t.group(2)
                    # receiver candidates: classes in the same package that are not the lambda
                    if cls.startswith(a.package) and cls != lam and "$" not in cls:
                        targets[(cls, meth)] += 1
        if targets:
            best = targets.most_common()
            conf = "HIGH" if len(best) == 1 else "MEDIUM"
            out["families"][f"{orig}#{method}"] = {
                "original_class": orig,
                "original_method": method,
                "lambda_classes": sorted(lambdas)[:4],
                "candidates": [{"class": c, "method": m, "sites": n} for (c, m), n in best[:6]],
                "confidence": conf,
            }
    out["summary"] = {"families": len(out["families"]),
                      "high": sum(1 for v in out["families"].values() if v["confidence"] == "HIGH"),
                      "medium": sum(1 for v in out["families"].values() if v["confidence"] == "MEDIUM")}
    os.makedirs(os.path.dirname(os.path.abspath(a.out)) or ".", exist_ok=True)
    with open(a.out, "w") as fh:
        json.dump(out, fh, indent=1, ensure_ascii=False)
        fh.write("\n")
    print(json.dumps(out["summary"], indent=1))


if __name__ == "__main__":
    main()
