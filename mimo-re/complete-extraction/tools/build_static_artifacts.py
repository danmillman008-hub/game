#!/usr/bin/env python3
"""Build static-code artifacts: class index, class-level call graph, obfuscation map.

Limitation this tool works around
---------------------------------
No JADX / dex2jar / baksmali is installable in this environment (GitHub release assets are
blocked; PyPI has no JADX; the `smali` PyPI package is an assembler, not a disassembler).
Therefore no Java source can be produced. What *can* be produced deterministically from the
DEX bytecode is:
  * a complete class/method/field inventory with inheritance,
  * a class-level call graph derived from `invoke-*` instructions,
  * a semantic-role proposal for obfuscated classes with the evidence attached.

Usage:
    python tools/build_static_artifacts.py EXTRACTED_DIR OUT_DIR [--app-prefix Lcom/getmimo/]

Outputs (OUT_DIR):
    CLASS_INDEX.json          every class with metadata
    CLASS_INDEX.csv           same, flat, for spreadsheets
    CALL_GRAPH/edges.csv      source class -> target class, invoke count
    CALL_GRAPH/nodes.csv      degree statistics
    CALL_GRAPH/graph.dot      Graphviz source (top edges only)
    OBFUSCATION_MAP.csv       obfuscated class -> proposed role + evidence + confidence
"""
from __future__ import annotations

import argparse
import collections
import csv
import glob
import gzip
import json
import os
import re

ROLE_RULES = [
    ("Activity", "android.app.Activity"),
    ("Service", "android.app.Service"),
    ("BroadcastReceiver", "android.content.BroadcastReceiver"),
    ("ContentProvider", "android.content.ContentProvider"),
    ("Application", "android.app.Application"),
    ("Fragment", "androidx.fragment.app.Fragment"),
    ("View", "android.view.View"),
    ("ViewModel", "androidx.lifecycle.ViewModel"),
    ("Worker", "androidx.work.ListenableWorker"),
    ("SQLiteOpenHelper", "android.database.sqlite.SQLiteOpenHelper"),
]

INVOKE_RE = re.compile(r"(L[^;,\s]+;)->([^(\s]+)(\([^)]*\)\S+)")


def role_of(name: str, supers: list[str], ifaces: list[str], strs: set[str]) -> tuple[str, str]:
    chain = supers + ifaces
    for role, marker in ROLE_RULES:
        if any(marker in c for c in chain):
            return role, f"superclass/interface chain contains {marker}"
    low = name.lower()
    if ".developermenu." in low:
        return "DeveloperTooling", "package name ui.developermenu"
    if ".aiTutor" in name or "aitutor" in low:
        return "AiTutor", "package name contains aitutor"
    if "lessonparser" in low:
        return "LessonParser", "package name contains lessonparser"
    if ".interactors." in low:
        return "UseCase", "package name interactors"
    if re.search(r"\.(Repository|Api|ApiService)$", name) or "source.remote" in low:
        return "DataAccess", "name/package indicates repository or API"
    if "source.local" in low:
        return "LocalDataSource", "package name source.local"
    if "analytics" in low:
        return "Analytics", "package name analytics"
    if "$serializer" in name or "$$serializer" in name:
        return "Serializer", "kotlinx.serialization generated serializer"
    if "$" in name and "WhenMappings" in name:
        return "WhenMappings", "kotlin when-mapping table"
    if re.search(r"(ViewModel|Reducer|State)$", name):
        return "Mvi", "name suffix indicates MVI component"
    if any(s.startswith("Insert INTO ") or s.startswith("SELECT ") or "CREATE TABLE" in s for s in strs):
        return "Dao", "SQL string literals present"
    if any(s.startswith("/v1/") or s.startswith("/v2/") for s in strs):
        return "ApiSurface", "endpoint literal present"
    if not re.search(r"[a-z]{3}", name.rsplit("/", 1)[-1].rstrip(";")):
        return "ObfuscatedUnresolved", "no semantic evidence recovered"
    return "Unknown", "classified but no specific evidence"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("extracted_dir")
    ap.add_argument("out_dir")
    ap.add_argument("--app-prefix", default="Lcom/getmimo/")
    args = ap.parse_args()

    from loguru import logger
    logger.remove()
    import androguard.core.dex as DX

    os.makedirs(os.path.join(args.out_dir, "CALL_GRAPH"), exist_ok=True)
    index, edges = [], collections.Counter()
    obf_map = []

    for path in sorted(glob.glob(os.path.join(args.extracted_dir, "*.dex"))):
        data = open(path, "rb").read()
        if len(data) < 0x70:
            continue
        dex = DX.DEX(data)
        dexname = os.path.basename(path)
        for cls in dex.get_classes():
            name = cls.get_name()
            supers, ifaces = [], []
            try:
                s = cls.get_superclassname()
                if s:
                    supers.append(s)
                ifaces = list(cls.get_interfaces() or [])
            except Exception:
                pass
            methods = cls.get_methods()
            lits = set()
            n_methods = 0
            for m in methods:
                n_methods += 1
                code = m.get_code()
                if not code:
                    continue
                for ins in code.get_bc().get_instructions():
                    op = ins.get_name()
                    if op.startswith("const-string"):
                        try:
                            lits.add(ins.get_raw_string())
                        except Exception:
                            pass
                    elif op.startswith("invoke"):
                        out = ins.get_output()
                        mm = INVOKE_RE.search(out)
                        if mm:
                            edges[(name, mm.group(1))] += 1
            role, why = role_of(name, supers, ifaces, lits)
            index.append({
                "class": name,
                "dex": dexname,
                "superclass": supers[0] if supers else None,
                "interfaces": ifaces,
                "methods": n_methods,
                "fields": len(cls.get_fields()) if hasattr(cls, "get_fields") else None,
                "strings": len(lits),
                "role": role,
                "role_evidence": why,
                "app_class": name.startswith(args.app_prefix),
            })
            if not re.search(r"[a-z]{3}", name.rsplit("/", 1)[-1].rstrip(";")):
                obf_map.append({
                    "obfuscated_id": name,
                    "proposed_role": role,
                    "evidence": why,
                    "superclass": supers[0] if supers else "",
                    "n_interfaces": len(ifaces),
                    "n_methods": n_methods,
                    "n_strings": len(lits),
                    "sample_strings": " | ".join(sorted(lits)[:6])[:300],
                    "confidence": "MEDIUM" if role not in ("ObfuscatedUnresolved", "Unknown") else "LOW",
                })

    with gzip.open(os.path.join(args.out_dir, "CLASS_INDEX.json.gz"), "wt", encoding="utf-8") as fh:
        json.dump(index, fh, ensure_ascii=False)
    with gzip.open(os.path.join(args.out_dir, "CLASS_INDEX.csv.gz"), "wt", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=["class", "dex", "superclass", "methods", "fields", "strings",
                                           "role", "role_evidence", "app_class", "interfaces"])
        w.writeheader()
        for r in index:
            row = dict(r)
            row["interfaces"] = ";".join(r["interfaces"])
            w.writerow(row)

    deg_out = collections.Counter()
    deg_in = collections.Counter()
    for (a, b), n in edges.items():
        deg_out[a] += n
        deg_in[b] += n
    with gzip.open(os.path.join(args.out_dir, "CALL_GRAPH", "edges.csv.gz"), "wt", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["source_class", "target_class", "invokes"])
        for (a, b), n in edges.most_common():
            w.writerow([a, b, n])
    with gzip.open(os.path.join(args.out_dir, "CALL_GRAPH", "nodes.csv.gz"), "wt", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["class", "out_invokes", "in_invokes"])
        for c in sorted(set(deg_out) | set(deg_in)):
            w.writerow([c, deg_out[c], deg_in[c]])
    with open(os.path.join(args.out_dir, "CALL_GRAPH", "graph.dot"), "w", encoding="utf-8") as fh:
        fh.write("digraph mimo_call_graph {\n  rankdir=LR; node [shape=box, fontsize=9];\n")
        for (a, b), n in edges.most_common(400):
            fa, fb = a.strip("L;").replace("/", "."), b.strip("L;").replace("/", ".")
            fh.write(f'  "{fa}" -> "{fb}" [label="{n}"];\n')
        fh.write("}\n")
    with gzip.open(os.path.join(args.out_dir, "OBFUSCATION_MAP.csv.gz"), "wt", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(obf_map[0].keys()) if obf_map else ["obfuscated_id"])
        w.writeheader()
        w.writerows(obf_map)

    app_edges = {k: v for k, v in edges.items() if k[0].startswith(args.app_prefix) and k[1].startswith(args.app_prefix)}
    summary = {
        "classes": len(index),
        "app_classes": sum(1 for r in index if r["app_class"]),
        "call_graph_edges_all": len(edges),
        "call_graph_edges_app_to_app": len(app_edges),
        "obfuscated_classes": len(obf_map),
        "roles": dict(collections.Counter(r["role"] for r in index).most_common()),
        "top_app_edges": [{"from": a, "to": b, "invokes": n}
                          for (a, b), n in sorted(app_edges.items(), key=lambda kv: -kv[1])[:40]],
    }
    with open(os.path.join(args.out_dir, "STATIC_SUMMARY.json"), "w") as fh:
        json.dump(summary, fh, indent=1)
    roles = collections.Counter(r["role"] for r in index)
    print(f"classes: {len(index)} | app classes: {sum(1 for r in index if r['app_class'])}")
    print(f"call-graph edges: {len(edges)} | obfuscated classes mapped: {len(obf_map)}")
    print("roles:", roles.most_common(12))


if __name__ == "__main__":
    main()
