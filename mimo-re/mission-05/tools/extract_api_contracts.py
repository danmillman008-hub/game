#!/usr/bin/env python3
"""MISSION-05 — reconstruct API contracts from obfuscated Retrofit interfaces.

For every method carrying an obfuscated HTTP annotation (value starts with '/'),
emit: interface, method, annotation type, path, declared return type, resolved response
type (unwrapping kotlin.coroutines.Continuation), parameter list with per-parameter
binding annotations (@Path/@Query/@Body/@Header candidates), and body presence.

Key discriminator added in mission-05: HTTP verbs are cross-checked against body presence
(Retrofit forbids @Body on GET/DELETE), which resolves the LOW-confidence verbs of mission-04.

Outputs CSV + JSON. Read-only.
"""
from __future__ import annotations
import argparse, csv, glob, json, os, sys
from collections import defaultdict

def ev_text(ev):
    """Dereference androguard EncodedValue to python value."""
    v = getattr(ev, "value", ev)
    if isinstance(v, list):
        return "|".join(str(getattr(x, "value", x)) for x in v)
    return str(v)

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dex-dir", required=True)
    ap.add_argument("--csv", required=True)
    ap.add_argument("--json", required=True)
    args = ap.parse_args()
    from loguru import logger as lg
    lg.remove()
    from androguard.core.dex import DEX

    rows = []
    for p in sorted(glob.glob(os.path.join(args.dex_dir, "classes*.dex"))):
        with open(p, "rb") as fh:
            dex = DEX(fh.read())
        for cls in dex.get_classes():
            cname = cls.get_name()
            for m in cls.get_methods():
                anns = m.get_annotations()
                if not anns:
                    continue
                http_ann, path, param_anns = [], [], {}
                for a in anns:
                    atype = a.get_type_descriptor()
                    for el in a.get_elements():
                        name = el.get_name()
                        val = ev_text(el.get_value())
                        if val.startswith("/"):
                            http_ann.append(atype)
                            path = val
                # parameter annotations
                for pa in m.get_parameter_annotations() or []:
                    idx = getattr(pa, "get_idx", lambda: None)()
                    for a in pa.get_annotations():
                        atype = a.get_type_descriptor()
                        vals = [ev_text(el.get_value()) for el in a.get_elements()]
                        param_anns.setdefault(idx, []).append({"type": atype, "values": vals})
                if not http_ann:
                    continue
                desc = m.get_descriptor()
                ret = desc.split(")")[-1]
                params = desc[1:desc.index(")")].split() if ")" in desc else []
                params = [x for x in params if x]
                # suspend: trailing Continuation<T> -> T is the response type
                response = ret
                is_suspend = bool(params) and "Lkotlin/coroutines/Continuation;" in params[-1]
                if is_suspend:
                    last = params[-1]
                    inner = last[last.find("<") + 1:-1] if "<" in last else ""
                    response = inner.split(";")[0] + ";" if inner else "UNIT"
                body_params = [i for i, t in enumerate(params)
                               if not t.startswith(("I", "J", "S", "B", "Z", "D", "F", "Lkotlin/coroutines/",
                                                    "Ld70/b;", "La7/i;", "Lkotlin/jvm/functions/"))
                               and not t.startswith("Ljava/lang/String;")]
                rows.append({
                    "interface": cname,
                    "method": m.get_name(),
                    "http_annotation": http_ann[0],
                    "path": path,
                    "declared_return": ret,
                    "response_type": response,
                    "is_suspend": is_suspend,
                    "param_count": len(params),
                    "params": " ".join(params),
                    "body_param_indices": ",".join(map(str, body_params)),
                    "has_body": bool(body_params),
                    "param_bindings": json.dumps(param_anns, ensure_ascii=False) if param_anns else "",
                    "dex": os.path.basename(p),
                })
    rows.sort(key=lambda r: (r["path"], r["interface"], r["method"]))
    with open(args.csv, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0]))
        w.writeheader(); w.writerows(rows)
    by_ann = defaultdict(lambda: {"total": 0, "with_body": 0})
    for r in rows:
        by_ann[r["http_annotation"]]["total"] += 1
        by_ann[r["http_annotation"]]["with_body"] += int(r["has_body"])
    summary = {"endpoints": len(rows),
               "interfaces": len({r["interface"] for r in rows}),
               "by_annotation": {k: dict(v) for k, v in by_ann.items()},
               "with_param_bindings": sum(1 for r in rows if r["param_bindings"]),
               "suspend": sum(1 for r in rows if r["is_suspend"])}
    json.dump({"summary": summary, "endpoints": rows}, open(args.json, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    print(json.dumps(summary, indent=1, ensure_ascii=False))
    return 0

if __name__ == "__main__":
    sys.exit(main())
