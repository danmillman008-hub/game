#!/usr/bin/env python3
"""Extract every DEX annotation (class / field / method / parameter) with resolved values.

Why this tool exists
--------------------
The HTTP endpoints of Mimo live in *annotation space*: no `const-string` instruction in
any of the 12 DEX files references an endpoint path (independently verified by
`mimo-re/tools/literal_reverse_index.py`, which found 0 of 71 endpoint literals as code
strings). androguard 4.1.4 returns annotation elements as `EncodedValue` objects whose
resolved content is `EncodedValue.value`; a naive `isinstance(value, str)` filter therefore
misses every string-valued annotation. This tool dereferences them.

Usage
-----
    python tools/extract_annotations.py EXTRACTED_DIR OUT_JSON [--endpoints-only]

EXTRACTED_DIR must contain classes*.dex. Output is a JSON array of
{scope, owner, dex, type, elements}. Deterministic; read-only w.r.t. the APK.
"""
from __future__ import annotations

import argparse
import collections
import glob
import io
import json
import os

MAX_DEPTH = 4


def flatten(val, depth: int = 0):
    """Turn an EncodedValue.value tree into JSON-safe primitives."""
    if depth > MAX_DEPTH:
        return str(val)[:80]
    if val is None or isinstance(val, (str, int, float, bool)):
        return val
    # EncodedAnnotation
    if hasattr(val, "elements"):
        out = {}
        for el in getattr(val, "elements", []) or []:
            name = getattr(el, "name", None)
            if name is None:
                name = getattr(el, "name_idx", "")
            out[str(name)] = flatten(getattr(el, "value", None), depth + 1)
        return {"__annotation__": out}
    # EncodedArray
    if hasattr(val, "value"):
        return flatten(val.value, depth + 1)
    if isinstance(val, (list, tuple)):
        return [flatten(v, depth + 1) for v in val]
    return str(val)[:80]


def walk_strings(node):
    """Yield every string leaf of a flattened value tree."""
    if isinstance(node, str):
        yield node
    elif isinstance(node, dict):
        for v in node.values():
            yield from walk_strings(v)
    elif isinstance(node, (list, tuple)):
        for v in node:
            yield from walk_strings(v)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("extracted_dir")
    ap.add_argument("out_json")
    ap.add_argument("--endpoints-only", action="store_true")
    args = ap.parse_args()

    from loguru import logger
    logger.remove()
    import androguard.core.dex as DX

    rows: list[dict] = []
    census: collections.Counter = collections.Counter()
    classes_scanned = 0

    for path in sorted(glob.glob(os.path.join(args.extracted_dir, "*.dex"))):
        data = open(path, "rb").read()
        if len(data) < 0x70:
            continue
        dex = DX.DEX(data)
        for cls in dex.get_classes():
            adi = getattr(cls, "annotations_directory_item", None)
            if adi is None:
                continue
            classes_scanned += 1
            cm = cls.CM

            def read_set(off: int):
                buff = io.BytesIO(data)
                buff.seek(off)
                return DX.AnnotationSetItem(buff, cm)

            def parse_anns(asi) -> list[dict]:
                out = []
                for oi in asi.get_annotation_off_item():
                    buff = io.BytesIO(data)
                    buff.seek(oi.get_annotation_off())
                    enc = DX.AnnotationItem(buff, cm).get_annotation()
                    els = {}
                    for el in enc.get_elements():
                        name = str(cm.get_string(el.get_name_idx()))
                        els[name] = flatten(el.get_value())
                    out.append({"type": str(cm.get_type(enc.get_type_idx())), "elements": els})
                return out

            targets: list[tuple[str, str, int]] = []
            ca = adi.get_class_annotations_off()
            if ca:
                targets.append(("class", cls.get_name(), ca))
            for scope, getter in (("field", adi.get_field_annotations),
                                  ("method", adi.get_method_annotations),
                                  ("parameter", adi.get_parameter_annotations)):
                try:
                    items = getter() or []
                except Exception:
                    continue
                for it in items:
                    off = getattr(it, "annotations_off", None)
                    if off is None and hasattr(it, "get_annotations_off"):
                        off = it.get_annotations_off()
                    if not off:
                        continue
                    owner = cls.get_name()
                    try:
                        if scope in ("method", "parameter"):
                            info = cm.get_method(it.method_idx)
                            owner = f"{info[0]}->{info[1]}{info[2][0] if info[2] else ''}"
                            if scope == "parameter":
                                owner += "#param"
                        elif scope == "field":
                            info = cm.get_field(it.field_idx)
                            owner = f"{info[0]}->{info[1]} {info[2]}"
                    except Exception:
                        pass
                    targets.append((scope, owner, off))

            for scope, owner, off in targets:
                try:
                    parsed = parse_anns(read_set(off))
                except Exception:
                    continue
                for a in parsed:
                    census[a["type"]] += 1
                    rows.append({"scope": scope, "owner": owner, "dex": os.path.basename(path), **a})

    endpoint_like = [r for r in rows
                     if any(s.startswith("/") or "{" in s for s in walk_strings(r["elements"]))]
    out = endpoint_like if args.endpoints_only else rows
    os.makedirs(os.path.dirname(args.out_json) or ".", exist_ok=True)
    json.dump(out, open(args.out_json, "w"), indent=1, ensure_ascii=False)

    print(f"classes with annotation directory: {classes_scanned}")
    print(f"annotation instances: {len(rows)} | distinct types: {len(census)}")
    print(f"endpoint-like annotations: {len(endpoint_like)}")
    print("top types:", census.most_common(8))
    for r in endpoint_like[:15]:
        print(f"  {r['type']:34s} {json.dumps(r['elements'], ensure_ascii=False)[:110]} <- {r['owner']}")


if __name__ == "__main__":
    main()
