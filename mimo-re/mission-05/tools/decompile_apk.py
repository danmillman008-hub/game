#!/usr/bin/env python3
"""MISSION-05 — reproducible batch Java decompiler for the Mimo APK.

Uses androguard's built-in DAD decompiler (no JADX needed). Produces:
  * one .java file per class (pseudo-Java; NOT source-equivalent — see LIMITATIONS)
  * an inventory CSV with per-class method counts and decompile status
  * a manifest JSON with input hashes, tool versions, timings

The decompiled text is written OUTSIDE the repository by design (RULE 6:
do not redistribute proprietary code). Only derived inventory/metadata is committed.

Usage:
  decompile_apk.py --dex-dir /tmp/x --out /tmp/dad --filter 'getmimo'
  decompile_apk.py --dex-dir /tmp/x --out /tmp/dad --classes-file wanted.txt
"""
from __future__ import annotations
import argparse, csv, glob, hashlib, json, os, platform, re, resource, sys, time

def sha256(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dex-dir", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--filter", default=None, help="substring match on class descriptor")
    ap.add_argument("--regex", default=None, help="regex match on class descriptor")
    ap.add_argument("--classes-file", default=None, help="newline-separated descriptors to decompile")
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--inventory", default=None, help="CSV inventory output path")
    ap.add_argument("--manifest", default=None, help="JSON manifest output path")
    args = ap.parse_args()

    from loguru import logger as lg
    lg.remove()
    import androguard
    from androguard.core.dex import DEX
    from androguard.core.analysis.analysis import Analysis
    from androguard.decompiler.decompile import DvClass

    t_start = time.time()
    dex_paths = sorted(glob.glob(os.path.join(args.dex_dir, "classes*.dex")))
    if not dex_paths:
        print("no dex found", file=sys.stderr); return 2
    dexes = []
    for p in dex_paths:
        with open(p, "rb") as fh:
            dexes.append((os.path.basename(p), DEX(fh.read())))
    t_load = time.time() - t_start
    a = Analysis()
    for _, d in dexes:
        a.add(d)
    a.create_xref()
    t_xref = time.time() - t_start

    by_name = {}
    for base, d in dexes:
        for c in d.get_classes():
            by_name[c.get_name()] = (base, c)

    wanted = list(by_name)
    if args.classes_file:
        with open(args.classes_file, encoding="utf-8") as fh:
            sel = {ln.strip() for ln in fh if ln.strip() and not ln.startswith("#")}
        wanted = [n for n in wanted if n in sel]
    elif args.regex:
        rx = re.compile(args.regex)
        wanted = [n for n in wanted if rx.search(n)]
    elif args.filter:
        wanted = [n for n in wanted if args.filter in n]
    wanted.sort()
    if args.limit:
        wanted = wanted[: args.limit]

    os.makedirs(args.out, exist_ok=True)
    rows, ok, failed, total_methods, src_bytes = [], 0, 0, 0, 0
    t_dec = time.time()
    for i, name in enumerate(wanted, 1):
        base, cls = by_name[name]
        rel = name.strip("L;").replace("/", ".") + ".java"
        path = os.path.join(args.out, rel)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        try:
            dv = DvClass(cls, a)
            dv.process()
            src = dv.get_source() or ""
            status = "OK" if src.strip() else "EMPTY"
        except Exception as e:  # noqa: BLE001 - decompiler is fragile by nature
            src = ""
            status = f"ERROR:{type(e).__name__}"
        if src:
            ok += 1
        else:
            failed += 1
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(src)
        n_methods = len(list(cls.get_methods()))
        total_methods += n_methods
        src_bytes += len(src)
        rows.append({
            "class": name,
            "dex": base,
            "methods": n_methods,
            "fields": len(list(cls.get_fields())),
            "superclass": cls.get_superclassname() if hasattr(cls, "get_superclassname") else "",
            "decompile_status": status,
            "source_bytes": len(src),
            "source_lines": src.count("\n") + (1 if src else 0),
        })
        if i % 250 == 0:
            print(f"  {i}/{len(wanted)} classes, {time.time()-t_dec:.1f}s", flush=True)

    t_dec_end = time.time() - t_dec
    if args.inventory:
        os.makedirs(os.path.dirname(os.path.abspath(args.inventory)), exist_ok=True)
        with open(args.inventory, "w", newline="", encoding="utf-8") as fh:
            w = csv.DictWriter(fh, fieldnames=list(rows[0]) if rows else ["class"])
            w.writeheader(); w.writerows(rows)
    manifest = {
        "mission": "mission-05",
        "tool": "tools/decompile_apk.py",
        "engine": "androguard DAD (DecompilerDAD / DvClass)",
        "androguard_version": androguard.__version__,
        "python_version": platform.python_version(),
        "dex_inputs": [{"file": b, "sha256": sha256(os.path.join(args.dex_dir, b)),
                        "bytes": os.path.getsize(os.path.join(args.dex_dir, b))} for b, _ in dexes],
        "selection": {"filter": args.filter, "regex": args.regex,
                      "classes_file": args.classes_file, "limit": args.limit},
        "classes_decompiled": len(wanted),
        "classes_with_source": ok,
        "classes_without_source": failed,
        "methods_total": total_methods,
        "source_bytes_total": src_bytes,
        "timings_s": {"load": round(t_load, 1), "xref_ready": round(t_xref, 1),
                      "decompile": round(t_dec_end, 1), "total": round(time.time() - t_start, 1)},
        "peak_rss_mb": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss // 1024,
        "output_dir": args.out,
        "note": "Pseudo-Java. DAD mis-renders some constructs (e.g. 'v0_1 = ;'). "
                "Cross-check critical logic against smali/instruction dumps.",
        "generated_at_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
    }
    if args.manifest:
        os.makedirs(os.path.dirname(os.path.abspath(args.manifest)), exist_ok=True)
        json.dump(manifest, open(args.manifest, "w", encoding="utf-8"), indent=1)
    print(json.dumps({k: manifest[k] for k in
                      ("classes_decompiled", "classes_with_source", "classes_without_source",
                       "methods_total", "source_bytes_total", "timings_s", "peak_rss_mb")}, indent=1))
    return 0

if __name__ == "__main__":
    sys.exit(main())
