#!/usr/bin/env python3
"""Mission 8 — Phase 2 call-relationship extractor.

Produces typed, evidenced edges. An edge exists only if an instruction in the
caller's body names the callee; nothing is inferred from naming conventions.

Edge kinds (from the invoke opcode / call site, never guessed):
  direct     invoke-direct / invoke-direct/range        (constructors, private)
  virtual    invoke-virtual[/range]
  interface  invoke-interface[/range]
  static     invoke-static[/range]
  super      invoke-super[/range]
  callback   an invoke that registers a listener/observer/callback object
             (method name matches set*Listener/add*Listener/addObserver/
              addCallback/subscribe/register*/addOn*Listener)
  framework  a callee that is an Android lifecycle entry point
             (onCreate/onStart/onResume/onStartCommand/doWork/onMessageReceived/
              onNewToken/onAvailable/onLost/onReceive/onBind/onDestroy)
  reflection Class.forName / getDeclaredMethod / getMethod / Method.invoke /
             Proxy.newProxyInstance occurrences (recorded as a *signal* on the
             caller method, with no fabricated target)
  dynamic    callee class not present in the dex set (dynamic feature or
             liveness artefact) — recorded with target name as written

Confidence model (see 03_EDGE_CONFIDENCE_MODEL.md):
  HIGH    direct/static/interface edge to a class whose body exists in the dex
  MEDIUM  virtual edge, or edge to a class that exists but whose method could not
          be matched by descriptor
  LOW     callback/framework edges (the runtime wiring is not observable here),
          and every reflection signal (no target)

Outputs
  02_METHOD_RELATIONSHIPS/02_TYPED_GRAPH_EDGES.csv
  02_METHOD_RELATIONSHIPS/evidence/CALLGRAPH_SUMMARY.json
  02_METHOD_RELATIONSHIPS/evidence/REFLECTION_SITES.json

Usage
  python3 build_call_graph.py --dex-dir /tmp/x --out ../mission-08/02_METHOD_RELATIONSHIPS \
      [--scope app]   # app = callers/callees touching app code (default)
"""
import argparse
import csv
import glob
import json
import os
import re
from collections import Counter, defaultdict

from androguard.core.dex import DEX

KIND = {
    "invoke-direct": "direct", "invoke-direct/range": "direct",
    "invoke-virtual": "virtual", "invoke-virtual/range": "virtual",
    "invoke-interface": "interface", "invoke-interface/range": "interface",
    "invoke-static": "static", "invoke-static/range": "static",
    "invoke-super": "super", "invoke-super/range": "super",
    "invoke-custom": "dynamic", "invoke-custom/range": "dynamic",
}
CALLBACK_RX = re.compile(r"^(set\w*Listener|add\w*Listener|remove\w*Listener|addObserver|"
                         r"removeObserver|addCallback|removeCallback|subscribe\w*|register\w*|"
                         r"addOn\w*Listener|setCallback|observe\w*|collect\w*)$")
FRAMEWORK_RX = re.compile(r"^(onCreate|onStart|onStartCommand|onResume|onPause|onStop|onDestroy|"
                          r"onReceive|onBind|onNewIntent|doWork|onMessageReceived|onNewToken|"
                          r"onAvailable|onLost|onComplete|invokeSuspend|run)$")
REFLECT_RX = re.compile(r"(Class;->forName|Class;->getDeclaredMethod|Class;->getMethod\b|"
                        r"Method;->invoke|Proxy;->newProxyInstance|Constructor;->newInstance|"
                        r"Lkotlin/reflect/)")
PLATFORM_PREFIXES = ("java.", "javax.", "android.", "androidx.", "kotlin.", "dalvik.", "sun.",
                     "org.jetbrains.", "org.w3c.", "org.xmlpull.", "org.json.")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dex-dir", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--scope", default="app", choices=["app", "all"])
    a = ap.parse_args()
    os.makedirs(os.path.join(a.out, "evidence"), exist_ok=True)

    pool = {}
    for path in sorted(glob.glob(os.path.join(a.dex_dir, "*.dex"))):
        with open(path, "rb") as fh:
            dx = DEX(fh.read())
        for c in dx.get_classes():
            pool[c.get_name()[1:-1].replace("/", ".")] = (os.path.basename(path), c)

    # which classes are app-related? app-named, or short-named but referencing app types
    app_named = {n for n in pool if n.startswith("com.getmimo")}
    renamed_app = set()
    for n, (_, cd) in pool.items():
        if n.startswith("com.getmimo") or len(n.rsplit(".", 1)[-1]) > 2:
            continue
        hit = False
        for m in cd.get_methods():
            code = m.get_code()
            if not code:
                continue
            for ins in code.get_bc().get_instructions():
                if "Lcom/getmimo/" in ins.get_output():
                    hit = True
                    break
            if hit:
                break
        if hit:
            renamed_app.add(n)
    app_related = app_named | renamed_app

    edges = Counter()
    edge_meta = {}
    reflection = []
    method_signatures = defaultdict(set)
    for n, (_, cd) in pool.items():
        for m in cd.get_methods():
            method_signatures[n].add((m.get_name(), m.get_descriptor()))

    for cname, (dexfile, cd) in pool.items():
        for m in cd.get_methods():
            code = m.get_code()
            if not code:
                continue
            for ins in code.get_bc().get_instructions():
                op = ins.get_name()
                out = ins.get_output()
                if REFLECT_RX.search(out):
                    reflection.append({"caller": cname, "caller_method": m.get_name(),
                                       "op": op, "snippet": out[:200]})
                if not op.startswith("invoke"):
                    continue
                mm = re.search(r"L([\w/$]+);->([\w<>$]+)(\([^)]*\)[\w/\[\$;]+)", out)
                if not mm:
                    mm = re.search(r"L([\w/$]+);->([\w<>$]+)", out)
                if not mm:
                    continue
                tgt_cls = mm.group(1).replace("/", ".")
                tgt_m = mm.group(2)
                tgt_desc = mm.group(3) if mm.lastindex and mm.lastindex >= 3 else ""
                if a.scope == "app" and not (cname in app_related or tgt_cls in app_related):
                    continue
                kind = KIND.get(op, op)
                conf = "HIGH"
                if kind == "virtual":
                    conf = "MEDIUM"
                if kind == "super":
                    conf = "MEDIUM"
                if kind == "dynamic":
                    conf = "LOW"
                if CALLBACK_RX.match(tgt_m):
                    kind = "callback"
                    conf = "LOW"
                elif FRAMEWORK_RX.match(tgt_m):
                    conf = "LOW" if kind != "direct" else conf
                    if m.get_name() in ("<init>", "<clinit>"):
                        pass
                if tgt_cls not in pool:
                    if tgt_cls.startswith(PLATFORM_PREFIXES):
                        kind = "platform"
                        conf = "MEDIUM"
                    else:
                        kind = "dynamic"
                        conf = "LOW"
                key = (cname, m.get_name(), tgt_cls, tgt_m, kind)
                edges[key] += 1
                sigs = method_signatures.get(tgt_cls, set())
                if tgt_desc:
                    matched = (tgt_m, tgt_desc) in sigs
                else:
                    matched = any(n == tgt_m for n, _ in sigs)
                edge_meta.setdefault(key, {"confidence": conf, "dex_caller": dexfile,
                                           "target_present": tgt_cls in pool,
                                           "target_method_matched": matched})
    rows = []
    for (caller, cm, tcallee, tm, kind), count in edges.items():
        meta = edge_meta[(caller, cm, tcallee, tm, kind)]
        conf = meta["confidence"]
        if kind in ("direct", "static", "interface") and not meta["target_present"]:
            conf = "LOW"
        if kind == "virtual" and meta["target_present"] and meta["target_method_matched"]:
            conf = "MEDIUM"
        rows.append({
            "caller_class": caller, "caller_method": cm,
            "callee_class": tcallee, "callee_method": tm,
            "kind": kind, "confidence": conf, "call_sites": count,
            "caller_is_app_named": caller in app_named,
            "caller_is_renamed_app": caller in renamed_app,
            "callee_present_in_dex": meta["target_present"],
            "callee_method_matched": meta["target_method_matched"],
            "evidence": "dex instruction (invoke-* site in %s.%s)" % (caller, cm),
        })
    rows.sort(key=lambda r: (-r["call_sites"], r["caller_class"], r["callee_class"]))
    with open(os.path.join(a.out, "02_TYPED_GRAPH_EDGES.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()) if rows else ["caller_class"])
        w.writeheader()
        w.writerows(rows)

    fan_out = Counter(r["caller_class"] for r in rows)
    fan_in = Counter(r["callee_class"] for r in rows)
    summary = {
        "generated": "2026-11-01",
        "scope": a.scope,
        "app_named_classes": len(app_named),
        "renamed_app_classes": len(renamed_app),
        "edges": len(rows),
        "call_sites": sum(r["call_sites"] for r in rows),
        "kind_distribution": dict(Counter(r["kind"] for r in rows)),
        "confidence_distribution": dict(Counter(r["confidence"] for r in rows)),
        "edges_to_classes_absent_from_dex": sum(1 for r in rows if not r["callee_present_in_dex"]),
        "edges_to_app_classes_absent_from_dex": sum(
            1 for r in rows if not r["callee_present_in_dex"]
            and (r["callee_class"].startswith("com.getmimo") or r["kind"] == "dynamic")),
        "reflection_sites": len(reflection),
        "top_fan_in": fan_in.most_common(15),
        "top_fan_out": fan_out.most_common(15),
    }
    with open(os.path.join(a.out, "evidence", "CALLGRAPH_SUMMARY.json"), "w") as fh:
        json.dump(summary, fh, indent=1, ensure_ascii=False)
        fh.write("\n")
    with open(os.path.join(a.out, "evidence", "REFLECTION_SITES.json"), "w") as fh:
        json.dump({"count": len(reflection), "sites": reflection[:500]}, fh, indent=1)
        fh.write("\n")
    print(json.dumps({k: summary[k] for k in ("edges", "call_sites", "kind_distribution",
                                              "confidence_distribution",
                                              "edges_to_classes_absent_from_dex",
                                              "reflection_sites")}, indent=1))


if __name__ == "__main__":
    main()
