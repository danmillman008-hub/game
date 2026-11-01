#!/usr/bin/env python3
"""MISSION-05 — DEX pickaxe: find all code references to a descriptor or string literal.

Answers questions the decompiled view cannot once code is obfuscated: "which classes
actually use <enum/class/method/string>?"  Read-only; no APK modification.

Usage:
  find_refs.py --dex-dir /tmp/x --target 'Lcom/getmimo/data/content/lessonparser/interactive/model/Tag;'
  find_refs.py --dex-dir /tmp/x --string 'fillTheGap'    # substring of const-string
  find_refs.py --dex-dir /tmp/x --target '...Tag;' --json out.json --csv out.csv
"""
from __future__ import annotations
import argparse, csv, glob, json, os, sys, time

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dex-dir", required=True)
    ap.add_argument("--target", action="append", default=[], help="descriptor substring (repeatable)")
    ap.add_argument("--string", action="append", default=[], help="literal substring (repeatable)")
    ap.add_argument("--json", default=None)
    ap.add_argument("--csv", default=None)
    ap.add_argument("--max-hits-per-class", type=int, default=40)
    args = ap.parse_args()
    if not args.target and not args.string:
        print("need --target or --string", file=sys.stderr); return 2

    from loguru import logger as lg
    lg.remove()
    import androguard
    from androguard.core.dex import DEX

    t0 = time.time()
    hits = []
    classes_scanned = methods_scanned = 0
    for p in sorted(glob.glob(os.path.join(args.dex_dir, "classes*.dex"))):
        with open(p, "rb") as fh:
            dex = DEX(fh.read())
        for cls in dex.get_classes():
            classes_scanned += 1
            cname = cls.get_name()
            for m in cls.get_methods():
                code = m.get_code()
                if code is None:
                    continue
                methods_scanned += 1
                n = 0
                for ins in code.get_bc().get_instructions():
                    out = ins.get_output()
                    low = None
                    matched = []
                    for t in args.target:
                        if t in out:
                            matched.append(("descriptor", t))
                    if args.string:
                        if low is None:
                            low = ins.get_name()
                        if low in ("const-string", "const-string/jumbo"):
                            for s in args.string:
                                if s in out:
                                    matched.append(("string", s))
                    if matched:
                        n += 1
                        if n <= args.max_hits_per_class:
                            hits.append({
                                "kind": matched[0][0],
                                "needle": matched[0][1],
                                "class": cname,
                                "method": m.get_name(),
                                "descriptor": m.get_descriptor(),
                                "offset": getattr(ins, "get_addr", lambda: getattr(ins, "addr", -1))(),
                                "instruction": low,
                                "operand": out[:240],
                                "dex": os.path.basename(p),
                            })
        print(f"  scanned {classes_scanned} classes, {methods_scanned} methods, {len(hits)} hits "
              f"({time.time()-t0:.1f}s)", flush=True)

    hits.sort(key=lambda h: (h["class"], h["method"], h["offset"]))
    summary = {"targets": args.target, "strings": args.string,
               "classes_scanned": classes_scanned, "methods_scanned": methods_scanned,
               "hits": len(hits), "referencing_classes": len({h["class"] for h in hits}),
               "androguard_version": androguard.__version__, "seconds": round(time.time() - t0, 1)}
    if args.json:
        json.dump({"summary": summary, "hits": hits}, open(args.json, "w", encoding="utf-8"), indent=1)
    if args.csv:
        with open(args.csv, "w", newline="", encoding="utf-8") as fh:
            w = csv.DictWriter(fh, fieldnames=list(hits[0]) if hits else ["kind"])
            w.writeheader(); w.writerows(hits)
    print(json.dumps(summary, indent=1))
    for h in hits[:25]:
        print(f"  {h['class']} -> {h['method']}{h['descriptor'][:40]} | {h['instruction']} {h['operand'][:90]}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
