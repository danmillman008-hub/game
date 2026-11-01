#!/usr/bin/env python3
"""Deterministic DEX inspector for Mimo (Mission 8).

Purpose: recover *behavioural* facts for classes the DAD decompiler cannot emit
(the ``ri.*`` / ``np.*`` / ``be.*`` / ``oy.*`` / ``AuthenticationFragment`` family),
and cross-check decompiled bodies against the actual instruction stream.

It never guesses: every value printed is read straight from the DEX file.

Usage
  python3 dex_inspect.py --dex-dir /tmp/x --class ri.a --class ri.c
  python3 dex_inspect.py --dex-dir /tmp/x --classes-file list.txt --out out.json
  python3 dex_inspect.py --dex-dir /tmp/x --class ri.a --instructions
  python3 dex_inspect.py --dex-dir /tmp/x --queue-csv q.csv --coverage

Output schema (--out)
  {"classes": {name: {"super", "interfaces", "fields", "methods": [
      {"name", "desc", "access", "insn_count", "strings", "calls",
       "fields_rw", "invoke_kinds"}]}},
   "coverage": {"total", "present", "missing", "missing_list"}}

Requires: androguard 4.x (only the DEX parser; no decompiler).
"""
import argparse
import glob
import json
import os
import sys

from androguard.core.dex import DEX

ACCESS = [(0x0001, "public"), (0x0002, "private"), (0x0004, "protected"),
          (0x0008, "static"), (0x0010, "final"), (0x0400, "abstract"),
          (0x1000, "synthetic"), (0x00010000, "constructor")]


def flags(v):
    return [n for bit, n in ACCESS if v & bit]


def load(dex_dir):
    pool = {}
    for path in sorted(glob.glob(os.path.join(dex_dir, "*.dex"))):
        with open(path, "rb") as fh:
            dx = DEX(fh.read())
        # index: class name -> (DEX, class_def)
        for c in dx.get_classes():
            pool.setdefault(c.get_name(), (dx, c))
    return pool


def _src_name(dx, cd):
    try:
        idx = cd.get_source_file_idx()
        if not idx:
            return None
        return dx.get_strings()[idx]
    except Exception:  # pragma: no cover - defensive only
        return None


def describe(dx, cd, want_insns=False):
    out = {
        "super": cd.get_superclassname(),
        "interfaces": list(cd.get_interfaces()),
        "access": flags(cd.get_access_flags()),
        "source_file": _src_name(dx, cd),
        "fields": [],
        "methods": [],
    }
    for f in cd.get_fields():
        out["fields"].append({"name": f.get_name(), "type": f.get_descriptor(),
                              "access": flags(f.get_access_flags())})
    for m in cd.get_methods():
        code = m.get_code()
        insns = list(code.get_bc().get_instructions()) if code else []
        rec = {"name": m.get_name(), "desc": m.get_descriptor(),
               "access": flags(m.get_access_flags()),
               "insn_count": len(insns),
               "strings": [], "calls": [], "fields_rw": [],
               "invoke_kinds": [], "registers": None}
        if code:
            rec["registers"] = code.get_registers_size()
            if want_insns:
                rec["instructions"] = []
            for ins in insns:
                op = ins.get_name()
                if op.startswith("invoke"):
                    tgt = ins.get_output()
                    if not tgt or tgt == "?":  # pragma: no cover
                        tgt = "%s %s" % (op, getattr(ins, "get_ref_kind", lambda: "")())
                    rec["calls"].append({"op": op, "target": tgt,
                                         "off": getattr(ins, "offset", None)})
                if op.startswith(("sget", "sput", "iget", "iput")):
                    rec["fields_rw"].append({"op": op, "target": ins.get_output()})
                if "const-string" in op:
                    txt = ins.get_output()
                    if '"' in txt:
                        rec["strings"].append(txt[txt.find('"') + 1:txt.rfind('"')][:400])
                if want_insns:
                    rec["instructions"].append([getattr(ins, "offset", None), op,
                                                ins.get_output()])
            rec["invoke_kinds"] = sorted({c["op"] for c in rec["calls"]})
        out["methods"].append(rec)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dex-dir", required=True)
    ap.add_argument("--class", dest="classes", action="append", default=[])
    ap.add_argument("--classes-file")
    ap.add_argument("--queue-csv", help="CSV with a 'class' column (mission-07 queue)")
    ap.add_argument("--coverage", action="store_true",
                    help="report which requested classes exist in the DEX pool")
    ap.add_argument("--src-dir", help="decompiled tree, for coverage of .java output")
    ap.add_argument("--instructions", action="store_true")
    ap.add_argument("--scan", help="regex over const-string literals; report matching classes")
    ap.add_argument("--scan-methods", help="regex over method names/descriptors; report signatures")
    ap.add_argument("--scan-out")
    ap.add_argument("--out")
    a = ap.parse_args()

    if a.scan_methods:
        import re
        rx = re.compile(a.scan_methods, re.I)
        pool1 = load(a.dex_dir)
        hits = {}
        for cname, (dx, cd) in pool1.items():
            dn = cname[1:-1].replace("/", ".")
            for m in cd.get_methods():
                sig = "%s%s" % (m.get_name(), m.get_descriptor())
                if rx.search(sig):
                    hits.setdefault(dn, []).append(sig[:220])
        out = {"pattern": a.scan_methods, "classes": len(hits),
               "hits": {k: sorted(set(v))[:24] for k, v in sorted(hits.items())}}
        text = json.dumps(out, indent=1, default=str)
        if a.scan_out:
            os.makedirs(os.path.dirname(os.path.abspath(a.scan_out)) or ".", exist_ok=True)
            open(a.scan_out, "w").write(text + "\n")
        print(json.dumps(out, indent=1)[:4000])
        return

    if a.scan:
        import re
        rx = re.compile(a.scan, re.I)
        hits = {}
        pool0 = load(a.dex_dir)
        for cname, (dx, cd) in pool0.items():
            for m in cd.get_methods():
                code = m.get_code()
                if not code:
                    continue
                for ins in code.get_bc().get_instructions():
                    if "const-string" in ins.get_name():
                        txt = ins.get_output()
                        if '"' in txt:
                            lit = txt[txt.find('"') + 1:txt.rfind('"')]
                            if rx.search(lit):
                                hits.setdefault(cname[1:-1].replace("/", "."), []).append(
                                    {"method": m.get_name(), "literal": lit[:300]})
        out = {"pattern": a.scan, "classes": len(hits),
               "hits": {k: v[:20] for k, v in sorted(hits.items())}}
        text = json.dumps(out, indent=1, default=str)
        if a.scan_out:
            os.makedirs(os.path.dirname(os.path.abspath(a.scan_out)) or ".", exist_ok=True)
            open(a.scan_out, "w").write(text + "\n")
        print(json.dumps({"pattern": a.scan, "classes": len(hits),
                          "sample": list(sorted(hits))[:25]}, indent=1))
        return

    want = list(a.classes)
    if a.classes_file:
        with open(a.classes_file) as fh:
            want += [ln.strip() for ln in fh if ln.strip()]
    if a.queue_csv:
        import csv
        with open(a.queue_csv, newline="") as fh:
            rd = csv.DictReader(fh)
            key = "class" if "class" in (rd.fieldnames or []) else (rd.fieldnames or ["class"])[0]
            want += [r[key].strip() for r in rd if r.get(key)]
    want = sorted(set(want))
    if not want:
        sys.exit("nothing requested")

    pool = load(a.dex_dir)
    dotted = {k[1:-1].replace("/", "."): v for k, v in pool.items()}
    result = {"classes": {}, "coverage": {}}

    buf = {k: v for k, v in dotted.items() if k in want}
    missing = [n for n in want if n not in buf]
    result["coverage"] = {"total": len(want), "present": len(buf),
                          "missing": len(missing), "missing_list": missing}
    if a.src_dir:
        have = {n for n in want if a.src_dir and os.path.exists(
            os.path.join(a.src_dir, n + ".java"))}
        result["coverage"]["dad_java_present"] = len(have)
        result["coverage"]["dad_java_missing"] = len(want) - len(have)
    detail = bool(a.classes or a.classes_file)
    for name in sorted(buf):
        if not detail:
            result["classes"][name] = {"present": True}
            continue
        dx, cd = buf[name]
        result["classes"][name] = describe(dx, cd, a.instructions)

    text = json.dumps(result, indent=1, sort_keys=True, default=str)
    if a.out:
        os.makedirs(os.path.dirname(os.path.abspath(a.out)) or ".", exist_ok=True)
        with open(a.out, "w") as fh:
            fh.write(text + "\n")
    cov = result["coverage"]
    print(json.dumps({"coverage": {k: v for k, v in cov.items() if k != "missing_list"},
                      "missing_head": cov["missing_list"][:10]}, indent=1))
    if not a.out:
        print(text)


if __name__ == "__main__":
    main()
