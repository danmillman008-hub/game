#!/usr/bin/env python3
"""MISSION-05 — corrected DEX annotation extractor (class / field / method / PARAMETER).

Mission-04's extractor fed the *parameter* annotation offset (an `annotation_set_ref_list`)
into the `annotation_set_item` parser, producing garbage rows (seen in
`01_STATIC_CODE/annotations.json.gz`: keys like "\\x00\\x00\\x04\\n\\x02..."). This tool
parses the reference list properly and keeps the owning method identity, which is what
Retrofit parameter bindings (@Path/@Query/@Body/@Header) require.

Outputs: CSV (scope, owner, method, param_index, annotation type, elements JSON) + JSON summary.
Read-only; no APK mutation.
"""
from __future__ import annotations
import argparse, collections, csv, glob, io, json, os, sys

MAX_DEPTH = 6


def flatten(val, depth: int = 0):
    if depth > MAX_DEPTH:
        return str(val)[:80]
    if val is None or isinstance(val, (str, int, float, bool)):
        return val
    if hasattr(val, "get_values"):  # androguard EncodedArray
        try:
            return [flatten(v, depth + 1) for v in (val.get_values() or [])]
        except Exception:  # pragma: no cover
            return str(val)[:80]
    if hasattr(val, "elements"):
        out = {}
        for el in getattr(val, "elements", []) or []:
            name = getattr(el, "name", None) or getattr(el, "name_idx", "")
            out[str(name)] = flatten(getattr(el, "value", None), depth + 1)
        return {"__annotation__": out}
    if hasattr(val, "value"):
        return flatten(val.value, depth + 1)
    if isinstance(val, (list, tuple)):
        return [flatten(v, depth + 1) for v in val]
    return str(val)[:80]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dex-dir", required=True)
    ap.add_argument("--csv", required=True)
    ap.add_argument("--json", required=True)
    args = ap.parse_args()
    from loguru import logger
    logger.remove()
    import androguard.core.dex as DX

    rows = []
    for path in sorted(glob.glob(os.path.join(args.dex_dir, "classes*.dex"))):
        data = open(path, "rb").read()
        dex = DX.DEX(data)
        dexname = os.path.basename(path)
        for cls in dex.get_classes():
            adi = getattr(cls, "annotations_directory_item", None)
            if adi is None:
                continue
            cm = cls.CM

            def parse_annset(off):
                if not off:
                    return []
                buff = io.BytesIO(data)
                buff.seek(off)
                out = []
                for oi in DX.AnnotationSetItem(buff, cm).get_annotation_off_item():
                    b2 = io.BytesIO(data)
                    b2.seek(oi.get_annotation_off())
                    enc = DX.AnnotationItem(b2, cm).get_annotation()
                    els = {}
                    for el in enc.get_elements():
                        els[str(cm.get_string(el.get_name_idx()))] = flatten(el.get_value())
                    out.append({"type": str(cm.get_type(enc.get_type_idx())), "elements": els})
                return out

            mtab = dex.get_methods()

            def mkey(midx):
                # cm.get_method(midx) returns [class, name, [params, ret]], not an object;
                # the DEX method table gives a proper MethodIdItem with a descriptor.
                try:
                    m = mtab[midx]
                    return f"{m.get_class_name()}->{m.get_name()}{m.get_descriptor()}"
                except Exception:
                    return f"?method_idx={midx}"

            # class scope
            for a in parse_annset(adi.get_class_annotations_off()):
                rows.append({"scope": "class", "owner": cls.get_name(), "method": "",
                             "param_index": "", "type": a["type"],
                             "elements": json.dumps(a["elements"], ensure_ascii=False),
                             "dex": dexname})
            # field scope
            try:
                for it in adi.get_field_annotations() or []:
                    try:
                        fidx = it.get_field_idx(); f = cm.get_field(fidx)
                        owner = f"{f.get_class_name()}->{f.get_name()}"
                    except Exception:
                        owner = f"?field_idx={getattr(it, 'get_field_idx', lambda: '')()}"
                    for a in parse_annset(it.get_annotations_off()):
                        rows.append({"scope": "field", "owner": owner, "method": "",
                                     "param_index": "", "type": a["type"],
                                     "elements": json.dumps(a["elements"], ensure_ascii=False),
                                     "dex": dexname})
            except Exception:
                pass
            # method scope
            try:
                for it in adi.get_method_annotations() or []:
                    mk = mkey(it.get_method_idx())
                    for a in parse_annset(it.get_annotations_off()):
                        rows.append({"scope": "method", "owner": mk.split("->")[0], "method": mk,
                                     "param_index": "", "type": a["type"],
                                     "elements": json.dumps(a["elements"], ensure_ascii=False),
                                     "dex": dexname})
            except Exception:
                pass
            # parameter scope (corrected)
            try:
                for it in adi.get_parameter_annotations() or []:
                    mk = mkey(it.get_method_idx())
                    off = it.get_annotations_off()
                    if not off:
                        continue
                    buff = io.BytesIO(data)
                    buff.seek(off)
                    refs = DX.AnnotationSetRefList(buff, cm)
                    items = refs.get_list()
                    for pidx, ref in enumerate(items):
                        setoff = getattr(ref, "get_annotations_off", lambda: None)()
                        if not setoff:
                            continue
                        for a in parse_annset(setoff):
                            rows.append({"scope": "parameter", "owner": mk.split("->")[0],
                                         "method": mk, "param_index": pidx, "type": a["type"],
                                         "elements": json.dumps(a["elements"], ensure_ascii=False),
                                         "dex": dexname})
            except Exception as exc:  # keep the run alive, record the failure
                rows.append({"scope": "error", "owner": cls.get_name(), "method": "",
                             "param_index": "", "type": type(exc).__name__,
                             "elements": str(exc)[:200], "dex": dexname})

    rows.sort(key=lambda r: (r["scope"], r["method"], str(r["param_index"])))
    with open(args.csv, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=["scope", "owner", "method", "param_index", "type", "elements", "dex"])
        w.writeheader()
        w.writerows(rows)
    census = collections.Counter(r["scope"] for r in rows)
    types = collections.Counter(r["type"] for r in rows if r["scope"] == "parameter")
    summary = {"total": len(rows), "by_scope": dict(census),
               "param_annotation_types": dict(types.most_common(40))}
    json.dump(summary, open(args.json, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    print(json.dumps(summary, indent=1, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
