#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
extract_ui.py — Mimo 9.35 (com.getmimo) :: COMPLETE static UI extraction.

Method: REA-style (morluto/rea) evidence discipline — the APK is opened
read-only, every entry is hashed, every UI-relevant byte is emitted either
verbatim or as a lossless decode, and every conclusion is labelled by the
evidence class of the bytes it came from.

Stages
  1. Baseline       : ZIP census, SHA-256 of every member, APK identity.
  2. resources.arsc : full 12,915-id resource table -> JSON/CSV + values XML.
  3. Binary XML     : every res/*.xml (2,858) -> symbolic, human-readable XML.
  4. Binary media   : every PNG/WebP/JPG/OTF/TTF/RIV/MP3 copied verbatim.
  5. Manifest       : decoded symbolic AndroidManifest.xml.
  6. WebView assets : every non-content asset copied verbatim (JS/CSS/HTML/
                      SVG/OTF/JSON fixtures/snippets/prettier/beautify).
  7. DEX            : complete UI class inventory, methods, annotations,
                      string literals, resource-id xrefs, @Composable markers.
  8. Catalogues     : entry census, resource index, layout index, tokens CSS.

Usage:
  python3 tools/extract_ui.py --apk "/abs/path/Mimo_9.35 (1).apk" \
                              --out /abs/path/mimo-ui
Requires: androguard==4.1.4 (pip install androguard==4.1.4)
"""
from __future__ import annotations

import argparse
import collections
import csv
import html
import json
import os
import re
import sys
import time
import zipfile
from pathlib import Path

# androguard is extremely chatty by default
from loguru import logger
logger.remove()

from androguard.core.apk import APK
from androguard.core.axml import AXMLPrinter, format_value
from androguard.core.axml.types import (
    TYPE_REFERENCE, TYPE_ATTRIBUTE, TYPE_INT_DEC, TYPE_INT_HEX,
)
from androguard.core.resources import public
from androguard.core.dex import DEX

import hashlib

APP_PKG = "com.getmimo"
HEXREF = re.compile(r"([@?])([0-9A-Fa-f]{8})")
AXML_MAGIC = b"\x03\x00\x08\x00"

# ---------------------------------------------------------------------------
# small helpers
# ---------------------------------------------------------------------------

def sha256(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def ensure(p: Path) -> Path:
    p.mkdir(parents=True, exist_ok=True)
    return p


def jdump(obj, path: Path, *, pretty=True):
    ensure(path.parent)
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2 if pretty else None,
                               default=str), encoding="utf-8")


def csv_dump(rows, path: Path, fields):
    ensure(path.parent)
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        for r in rows:
            w.writerow({k: (json.dumps(v, ensure_ascii=False) if isinstance(v, (list, dict)) else v)
                        for k, v in r.items()})


def xesc(s) -> str:
    return html.escape(str(s), quote=True)


# ---------------------------------------------------------------------------
# resource-id resolution
# ---------------------------------------------------------------------------

class Resolver:
    def __init__(self, arsc):
        self.arsc = arsc
        self.cache = {}
        self.attr_inverse = public.SYSTEM_RESOURCES["attributes"]["inverse"]

    def name(self, rid: int) -> str:
        """@com.getmimo:layout/foo -> @layout/foo ; framework -> @android:..."""
        if rid in self.cache:
            return self.cache[rid]
        try:
            n = self.arsc.get_resource_xml_name(rid)
        except Exception:
            n = None
        if not n or n.startswith("@null"):
            out = "@null" if rid == 0 else "@0x%08X" % rid
        else:
            out = n
            if out.startswith("@" + APP_PKG + ":"):
                out = "@" + out.split(":", 1)[1]
            elif out.startswith("@android:"):
                pass
            elif rid >> 24 == 1:
                out = "@android:" + out.lstrip("@")
        self.cache[rid] = out
        return out

    def bare(self, rid: int) -> str:
        """name without leading @/? and without package"""
        n = self.name(rid).lstrip("@?")
        if ":" in n:
            n = n.split(":", 1)[1]
        return n

    def attr(self, rid: int) -> str:
        if rid >> 24 == 1:
            return "android:" + self.attr_inverse.get(rid, "attr_0x%08X" % rid)
        n = self.name(rid).lstrip("@?")
        if ":" in n:
            n = n.split(":", 1)[1]
        return n.replace("/", ".")

    def symbolize(self, v):
        """Replace every @7F.... / ?7F.... / @0101.... in a value."""
        if not isinstance(v, str):
            return v
        def sub(m):
            sig, hx = m.group(1), int(m.group(2), 16)
            n = self.name(hx).lstrip("@")
            return sig + n
        return HEXREF.sub(sub, v)


# Common Android enum/flag decoding. Missing maps keep the raw numeric value,
# which is also preserved verbatim in SOURCE/_raw_axml/ALL_RAW_DECODED.json.gz.
GRAVITY = [(0x01, "center_horizontal"), (0x02, "center_vertical"),
           (0x03, "center"), (0x10, "left"), (0x20, "right"), (0x30, "center_horizontal"),
           (0x50, "top"), (0x30, "bottom"), (0x11, "center_vertical"),
           (0x05, "fill_vertical"), (0x07, "fill"), (0x70, "fill_horizontal"),
           (0x77, "fill"), (0x800000, "clip_horizontal"), (0x080000, "clip_vertical"),
           (0x88, "clip_horizontal"), (0x80000000, "start"), (0x00800000, "end")]
SIMPLE_ENUMS = {
    "orientation": {"0": "horizontal", "1": "vertical"},
    "visibility": {"0": "visible", "1": "invisible", "2": "gone"},
    "layoutDirection": {"0": "ltr", "1": "rtl", "2": "inherit", "3": "locale"},
    "textDirection": {"0": "inherit", "1": "firstStrong", "2": "anyRtl", "3": "ltr",
                      "4": "rtl", "5": "locale", "6": "firstStrongLtr", "7": "firstStrongRtl"},
    "textAlignment": {"0": "inherit", "1": "gravity", "2": "textStart", "3": "textEnd",
                      "4": "center", "5": "viewStart", "6": "viewEnd"},
    "importantForAccessibility": {"0": "auto", "1": "yes", "2": "no", "3": "noHideDescendants"},
    "scaleType": {str(i): n for i, n in enumerate(
        ["matrix", "fitXY", "fitStart", "fitCenter", "fitEnd", "center", "centerCrop", "centerInside"])},
    "ellipsize": {str(i): n for i, n in enumerate(["none", "start", "middle", "end", "marquee"])},
    "layerType": {"0": "none", "1": "software", "2": "hardware"},
    "choiceMode": {"0": "none", "1": "singleChoice", "2": "multipleChoice"},
    "cacheColorHint": {},
}


def decode_enum(aname: str, raw: str) -> str:
    # Compiled AXML often stores attribute names as "layout:width" rather
    # than "layout_width"; normalise both spellings.
    local = aname.replace(":", "_")
    if local in ("layout_width", "layout_height"):
        return {"-1": "match_parent", "-2": "wrap_content", "-3": "match_parent"}.get(raw, raw)
    if local in SIMPLE_ENUMS and raw in SIMPLE_ENUMS[local]:
        return SIMPLE_ENUMS[local][raw]
    if local in ("gravity", "layout_gravity", "foregroundGravity") and re.fullmatch(r"-?\d+", raw):
        v = int(raw)
        if v in (0x11, 0x01, 0x10, 0x50, 0x30, 0x05, 0x70, 0x03, 0x07, 0x77, 0x800000, 0x00800000):
            names = [n for bit, n in GRAVITY if v & bit == bit and bit != 0]
            if names:
                return "|".join(dict.fromkeys(names))
    return raw


class SymbolicAXMLPrinter(AXMLPrinter):
    """AXMLPrinter that resolves resource IDs to symbolic names and decodes
    the most common enums, while keeping the raw AXML bytes for audit."""
    def __init__(self, raw, resolver: Resolver):
        self.res = resolver
        self.attr_log = []
        super().__init__(raw)

    def _get_attribute_value(self, index):
        ax = self.axml
        t = ax.getAttributeValueType(index)
        d = ax.getAttributeValueData(index)
        raw = format_value(t, d, lambda _: ax.getAttributeValue(index))
        try:
            aname = ax.getAttributeName(index)
        except Exception:
            aname = ""
        if t == TYPE_REFERENCE:
            val = self.res.name(d)
        elif t == TYPE_ATTRIBUTE:
            val = "?" + self.res.name(d).lstrip("@")
        else:
            val = self.res.symbolize(raw)
            if (t == TYPE_INT_DEC or t == TYPE_INT_HEX) and aname:
                val = decode_enum(aname, val)
        self.attr_log.append({"attr": aname, "raw": raw, "symbolic": val,
                              "value_type": t, "value_data": d})
        return val


# ---------------------------------------------------------------------------
# classification
# ---------------------------------------------------------------------------

def classify(n: str):
    """Return (ui_class, deliverable_kind, reason)."""
    if n == "AndroidManifest.xml":
        return "UI_MANIFEST", "decoded", "declares every activity/alias/theme/deep link"
    if n == "resources.arsc":
        return "UI_RESOURCE_TABLE", "decoded", "complete compiled resource table (values/tokens/strings)"
    if n.startswith("res/"):
        d = n.split("/")[1].split("-")[0]
        if d == "layout":       return "UI_LAYOUT", "decoded", "screen/component XML"
        if d in ("drawable", "mipmap"): return "UI_DRAWABLE", "decoded_or_binary", "vector/shape/image asset"
        if d == "color":        return "UI_COLOR_STATE", "decoded", "color state list / token"
        if d in ("anim", "animator", "interpolator"): return "UI_MOTION", "decoded", "motion spec"
        if d == "menu":         return "UI_MENU", "decoded", "menu definition"
        if d == "navigation":   return "UI_NAVIGATION", "decoded", "navigation graph"
        if d == "font":         return "UI_FONT", "binary", "font file"
        if d == "raw":          return "UI_RAW_ASSET", "binary", "Rive/audio/raw UI asset"
        if d == "xml":          return "UI_XML_CONFIG", "decoded", "UI-related XML config"
        return "UI_RESOURCE", "decoded_or_binary", "compiled resource"
    if n.startswith("assets/"):
        if "/tracks/" in n and n.endswith(".json"):
            return "CONTENT_DATA", "catalogued", "lesson content JSON (data rendered by the UI, not UI code)"
        if n.endswith((".prof", ".profm")):
            return "NON_UI", "catalogued", "ART baseline profile"
        return "UI_WEBVIEW_ASSET", "binary", "WebView/editor/lesson-rendering asset"
    if re.fullmatch(r"classes\d*\.dex", n):
        return "DEX_CODE", "inventoried", "bytecode: UI classes/methods/xrefs"
    if n.startswith("lib/"):
        return "NATIVE", "catalogued", "native library (Rive renderer etc.)"
    return "NON_UI", "catalogued", "metadata/signature/kotlin/other"


# ---------------------------------------------------------------------------
# Stage 2: resources.arsc
# ---------------------------------------------------------------------------

def complex_items(ate, res: Resolver):
    """Decode ResTable_map_entry items into (attribute, symbolic value) pairs."""
    out = []
    parent = ""
    try:
        parent = res.name(ate.item.id_parent).lstrip("@")
        for aid, ref in ate.item.items:
            out.append({"attr": res.attr(aid),
                        "attr_id": "0x%08X" % aid,
                        "value": res.symbolize(ref.format_value()),
                        "value_type": ref.get_data_type_string()})
    except Exception as e:
        out.append({"error": repr(e)})
    return {"parent": parent, "items": out}


def extract_arsc(apk: APK, z, res: Resolver, out: Path, stats):
    arsc = apk.get_android_resources()
    arsc._analyse()
    rows = []
    full = []
    by_qual = collections.defaultdict(lambda: collections.defaultdict(list))
    types = collections.Counter()
    qualifiers = collections.Counter()

    for rid, cfg_map in arsc.resource_values.items():
        nm = res.name(rid).lstrip("@")
        typ, _, key = nm.partition("/")
        if ":" in typ:
            typ = typ.split(":", 1)[1]
        entry = {"id": "0x%08X" % rid, "type": typ, "name": key, "configs": []}
        for cfg, ate in cfg_map.items():
            qual = cfg.get_qualifier() or "default"
            qualifiers[qual] += 1
            if ate.is_complex():
                ci = complex_items(ate, res)
                val = json.dumps(ci["items"], ensure_ascii=False)
                kind = "complex"
            elif ate.is_compact():
                val = res.symbolize(format_value(ate.datatype, ate.data,
                                                 arsc.stringpool_main.getString))
                kind = "simple"
                ci = None
            else:
                val = res.symbolize(ate.key.format_value())
                kind = "simple"
                ci = None
            rec = {"qualifier": qual, "value": val, "kind": kind}
            if ci:
                rec["parent"] = ci["parent"]
                rec["items"] = ci["items"]
            entry["configs"].append(rec)
            rows.append({"res_id": "0x%08X" % rid, "type": typ, "name": key,
                         "qualifier": qual, "value": val, "value_kind": kind,
                         "parent": (ci or {}).get("parent", ""),
                         "complex_items": (ci or {}).get("items", [])})
            by_qual[qual][typ].append((key, val, (ci or {}).get("parent", ""),
                                       (ci or {}).get("items", []), kind))
            types[typ] += 1
        full.append(entry)

    jdump(full, out / "SOURCE/arsc/RESOURCE_TABLE.json", pretty=False)
    csv_dump(rows, out / "CATALOGS/RESOURCE_INDEX.csv",
             ["res_id", "type", "name", "qualifier", "value", "value_kind",
              "parent", "complex_items"])

    # values/<qualifier>/<type>.xml — a source-like rendering of the entire table
    for qual, tmap in by_qual.items():
        qdir = "values" if qual == "default" else "values-" + qual
        for typ, items in tmap.items():
            lines = ['<?xml version="1.0" encoding="utf-8"?>', "<resources>"]
            for key, val, parent, citems, kind in items:
                if kind == "complex":
                    tag = {"style": "style", "plurals": "plurals", "array": "array",
                           "attr": "attr"}.get(typ, typ)
                    pattr = (' parent="%s"' % xesc(parent)) if parent and parent != "@null" else ""
                    lines.append('  <%s name="%s"%s>' % (tag, xesc(key), pattr))
                    for it in citems:
                        if "error" in it:
                            lines.append("    <!-- %s -->" % xesc(it["error"]))
                        else:
                            lines.append('    <item name="%s">%s</item>' %
                                         (xesc(it["attr"]), xesc(it["value"])))
                    lines.append("  </%s>" % tag)
                else:
                    lines.append('  <%s name="%s">%s</%s>' %
                                 (typ, xesc(key), xesc(val), typ))
            lines.append("</resources>")
            p = out / "SOURCE/values" / qdir / (typ + ".xml")
            ensure(p.parent)
            p.write_text("\n".join(lines) + "\n", encoding="utf-8")

    stats["arsc"] = {"resource_ids": len(arsc.resource_values),
                     "config_rows": len(rows),
                     "qualifiers": len(qualifiers),
                     "types": dict(types),
                     "top_qualifiers": qualifiers.most_common(15),
                     "locales": sorted({q for q in qualifiers if re.fullmatch(r"[a-z]{2}(-[A-Za-z0-9]+)*", q)})}
    return arsc


# ---------------------------------------------------------------------------
# Stage 3/4/5/6: res + manifest + assets
# ---------------------------------------------------------------------------

def extract_files(z, res: Resolver, out: Path, stats, census):
    raw_axml = {}
    layout_rows = []
    errors = []
    n_dec, n_bin = 0, 0
    for name in census:
        ui_class, kind, reason = classify(name)
        dest = None
        data = None
        try:
            if ui_class == "UI_MANIFEST":
                data = z.read(name)
                doc = SymbolicAXMLPrinter(data, res).get_xml(pretty=True).decode("utf-8", "replace")
                dest = out / "SOURCE/manifest/AndroidManifest.xml"
                ensure(dest.parent)
                dest.write_text('<?xml version="1.0" encoding="utf-8"?>\n' + doc + "\n", encoding="utf-8")
                n_dec += 1
            elif name.startswith("res/"):
                data = z.read(name)
                target = out / "SOURCE/res" / name[4:]
                ensure(target.parent)
                if data[:4] == AXML_MAGIC:
                    try:
                        pr = SymbolicAXMLPrinter(data, res)
                        raw_axml[name] = AXMLPrinter(data).get_xml(pretty=True).decode("utf-8", "replace")
                        doc = pr.get_xml(pretty=True).decode("utf-8", "replace")
                        target.write_text('<?xml version="1.0" encoding="utf-8"?>\n' + doc + "\n",
                                          encoding="utf-8")
                        n_dec += 1
                        dest = target
                        if ui_class == "UI_LAYOUT":
                            layout_rows.append(layout_facts(name, doc, pr, res, out))
                    except Exception as e:
                        errors.append({"file": name, "stage": "axml", "error": repr(e)})
                        target.write_bytes(data)
                        n_bin += 1
                        dest = target
                else:
                    target.write_bytes(data)
                    n_bin += 1
                    dest = target
            elif ui_class == "UI_WEBVIEW_ASSET":
                data = z.read(name)
                target = out / "SOURCE/assets/ui" / name[7:]
                ensure(target.parent)
                target.write_bytes(data)
                dest = target
                n_bin += 1
        except Exception as e:
            errors.append({"file": name, "stage": "copy", "error": repr(e)})
        if dest:
            census[name]["deliverable"] = str(dest.relative_to(out)).replace(os.sep, "/")
        else:
            census[name]["deliverable"] = {
                "UI_RESOURCE_TABLE": "SOURCE/arsc/RESOURCE_TABLE.json",
                "CONTENT_DATA": "CATALOGS/APK_ENTRY_CENSUS.csv (verbatim hash + path; data, not UI code)",
                "DEX_CODE": "SOURCE/dex/UI_CLASSES.json + UI_CLASS_INDEX.csv",
                "NATIVE": "CATALOGS/APK_ENTRY_CENSUS.csv",
                "NON_UI": "CATALOGS/APK_ENTRY_CENSUS.csv",
            }.get(ui_class, "CATALOGS/APK_ENTRY_CENSUS.csv")

    import gzip
    p = out / "SOURCE/_raw_axml/ALL_RAW_DECODED.json.gz"
    ensure(p.parent)
    with gzip.open(p, "wt", encoding="utf-8") as f:
        json.dump(raw_axml, f, ensure_ascii=False)

    csv_dump(layout_rows, out / "CATALOGS/LAYOUT_INDEX.csv",
             ["layout_path", "decoded_path", "dossier_path", "root_tag", "nodes",
              "ids", "tags", "custom_views", "includes", "references",
              "compose_views", "webviews", "raw_sha256", "decode_status"])
    jdump(layout_rows, out / "CATALOGS/LAYOUT_INDEX.json", pretty=False)
    jdump(errors, out / "CATALOGS/DECODE_ERRORS.json", pretty=False)
    stats["files"] = {"axml_decoded": n_dec, "binary_copied": n_bin,
                      "raw_axml_saved": len(raw_axml),
                      "decode_errors": len(errors),
                      "layouts": len(layout_rows)}
    return layout_rows


def layout_facts(path, doc, pr, res: Resolver, out: Path):
    import xml.etree.ElementTree as ET
    status = "ok"
    tags, ids, custom, includes, refs, compose, webviews = [], [], [], [], [], [], []
    root_tag = ""
    nodes = 0
    try:
        root = ET.fromstring(doc)
        root_tag = root.tag
        for el in root.iter():
            nodes += 1
            tags.append(el.tag)
            if el.tag.startswith("com.") or (el.tag and el.tag[0].islower() and "." in el.tag):
                custom.append(el.tag)
            if "ComposeView" in el.tag:
                compose.append(el.tag)
            if "WebView" in el.tag:
                webviews.append(el.tag)
            if el.tag in ("include", "ViewStub", "merge"):
                for k, v in el.attrib.items():
                    if "layout" in k:
                        includes.append(v)
            for k, v in el.attrib.items():
                if k.endswith("}id") or k == "id":
                    ids.append(v)
                if isinstance(v, str) and v.startswith(("@", "?")):
                    refs.append(v)
    except Exception:
        status = "unparseable_after_decode"
    rel = path[4:]                      # e.g. layout-v31/foo.xml
    stem = re.sub(r"[^A-Za-z0-9_.-]", "_", rel[:-4])
    dossier = "SCREENS/LAYOUTS/%s.md" % stem
    return {"layout_path": path,
            "decoded_path": "SOURCE/res/" + path[4:],
            "dossier_path": dossier,
            "root_tag": root_tag, "nodes": nodes,
            "ids": sorted(set(ids)), "tags": sorted(set(tags)),
            "custom_views": sorted(set(custom)), "includes": sorted(set(includes)),
            "references": sorted(set(refs)),
            "compose_views": sorted(set(compose)), "webviews": sorted(set(webviews)),
            "raw_sha256": sha256(pr.get_xml(pretty=False)),
            "decode_status": status}


# ---------------------------------------------------------------------------
# Stage 7: DEX
# ---------------------------------------------------------------------------

def dex_inventory(z, res: Resolver, out: Path, stats):
    dex_names = sorted(n for n in z.namelist() if re.fullmatch(r"classes\d*\.dex", n))
    classes = []
    layout_xrefs = collections.defaultdict(set)
    compose_funcs = []
    ui_strings = collections.Counter()
    all_strings = collections.Counter()
    mod_markers = []
    dex_stats = []

    for dn in dex_names:
        t0 = time.time()
        d = DEX(z.read(dn))
        strs = [s for s in d.get_strings()]
        for s in strs:
            all_strings[s] += 1
            if "Smob" in s or "Kirlif" in s or "mod obfuscation" in s.lower():
                mod_markers.append({"dex": dn, "string": s[:200]})
        cls = list(d.get_classes())
        dex_stats.append({"dex": dn, "bytes": z.getinfo(dn).file_size,
                          "classes": len(cls), "strings": len(strs),
                          "seconds": round(time.time() - t0, 2)})
        for c in cls:
            cn = c.get_name()
            is_app = cn.startswith("L" + APP_PKG.replace(".", "/") + "/")
            is_ui = cn.startswith("L" + APP_PKG.replace(".", "/") + "/ui/")
            binding = "Binding;" in cn
            kt = cn.endswith("Kt;")
            anns = [str(a) for a in (c.get_annotations() or [])]
            is_compose = any("Compose" in a or "Composable" in a for a in anns) or "Compose" in cn
            if not (is_app or binding or is_compose or kt):
                continue
            methods, fields, literals, rids, calls = [], [], [], set(), set()
            try:
                for f in c.get_fields():
                    fields.append({"name": f.get_name(), "type": f.get_descriptor() if hasattr(f, "get_descriptor") else str(f)})
            except Exception:
                pass
            for m in c.get_methods():
                mname = m.get_name()
                desc = m.get_descriptor()
                methods.append(mname + desc)
                try:
                    for ins in m.get_instructions():
                        op = ins.get_name()
                        for o in ins.get_operands():
                            if len(o) >= 2 and isinstance(o[1], int):
                                v = o[1]
                                if 0x7F000000 <= v <= 0x7FFFFFFF:
                                    rids.add(v)
                            if isinstance(o, (tuple, list)) and len(o) >= 3 and isinstance(o[2], str):
                                s = o[2]
                                if op == "const-string" or op.startswith("const-string"):
                                    literals.append(s)
                                if any(k in s for k in ("setContentView", "inflate", "findViewById",
                                                        "setContent", "setImageResource", "setText",
                                                        "ComposeView", "setLifecycleOwner")):
                                    calls.add(s)
                except Exception:
                    pass
            resolved = {}
            for rid in rids:
                nm = res.name(rid)
                resolved["0x%08X" % rid] = nm
                rtype = nm.lstrip("@?").split("/")[0].split(":")[-1]
                if rtype == "layout":
                    layout_xrefs[cn].add(nm.lstrip("@?").split("/")[-1])
            lit = sorted(set(x for x in literals if isinstance(x, str)))
            for s in lit:
                ui_strings[s] += 1
            rec = {"dex": dn, "class": cn, "superclass": c.get_superclassname(),
                   "interfaces": [str(i) for i in (c.get_interfaces() or [])],
                   "access": c.get_access_flags_string(),
                   "annotations": anns, "is_ui_package": is_ui, "is_binding": binding,
                   "is_compose": is_compose, "is_top_level_compose_file": kt,
                   "n_methods": len(methods), "methods": methods,
                   "n_fields": len(fields), "fields": fields,
                   "string_literals": lit, "resource_ids": resolved,
                   "ui_calls": sorted(calls), "layout_xrefs": sorted(layout_xrefs.get(cn, ()))}
            classes.append(rec)
            if is_compose or kt:
                compose_funcs.append({"class": cn, "dex": dn,
                                     "methods": [m for m in methods if not m.startswith("<init")],
                                     "annotations": anns})

    jdump(classes, out / "SOURCE/dex/UI_CLASSES.json", pretty=False)
    flat = [{k: v for k, v in c.items() if k not in ("methods", "fields", "string_literals",
                                                    "resource_ids", "annotations", "ui_calls")}
            for c in classes]
    csv_dump(flat, out / "CATALOGS/UI_CLASS_INDEX.csv",
             ["dex", "class", "superclass", "interfaces", "access", "is_ui_package",
              "is_binding", "is_compose", "is_top_level_compose_file", "n_methods",
              "n_fields", "layout_xrefs"])
    csv_dump(compose_funcs, out / "SOURCE/dex/COMPOSE_INVENTORY.csv",
             ["class", "dex", "methods", "annotations"])
    csv_dump([{"class": k, "layouts": sorted(v)} for k, v in layout_xrefs.items()],
             out / "SOURCE/dex/LAYOUT_XREFS.csv", ["class", "layouts"])
    p = out / "SOURCE/dex/UI_STRING_LITERALS.txt"
    ensure(p.parent)
    p.write_text("\n".join(sorted(ui_strings)) + "\n", encoding="utf-8")
    jdump({"dex_stats": dex_stats, "mod_markers": mod_markers,
           "total_strings": len(all_strings), "ui_string_literals": len(ui_strings)},
          out / "CATALOGS/DEX_CENSUS.json")
    stats["dex"] = {"files": len(dex_names), "classes_total": sum(d["classes"] for d in dex_stats),
                    "app_classes": len(classes), "ui_package_classes": sum(1 for c in classes if c["is_ui_package"]),
                    "compose_classes": len(compose_funcs),
                    "classes_with_layout_xrefs": len(layout_xrefs),
                    "mod_markers": mod_markers,
                    "dex_stats": dex_stats}
    return classes, layout_xrefs


# ---------------------------------------------------------------------------
# tokens CSS + entry census
# ---------------------------------------------------------------------------

def build_tokens(out: Path, stats):
    import json as _json
    rows = list(csv.DictReader((out / "CATALOGS/RESOURCE_INDEX.csv").open(encoding="utf-8")))
    colors = collections.defaultdict(dict)
    dimens = collections.defaultdict(dict)
    strings = collections.defaultdict(dict)
    styles = collections.defaultdict(dict)
    for r in rows:
        q, t, n, v = r["qualifier"], r["type"], r["name"], r["value"]
        if t == "color":   colors[n][q] = v
        elif t == "dimen": dimens[n][q] = v
        elif t == "string": strings[n][q] = v
        elif t == "style": styles[n][q] = _json.loads(r["complex_items"]) if r["complex_items"] else []
    tok = {"colors": colors, "dimens": dimens, "strings": strings, "styles": styles}
    jdump({"colors": dict(colors), "dimens": dict(dimens), "strings": dict(strings),
           "styles": dict(styles)}, out / "CATALOGS/DESIGN_TOKENS.json", pretty=False)
    jdump({"colors": dict(colors), "dimens": dict(dimens)},
          out / "ATLAS/tokens.json", pretty=False)
    lines = ["/* Mimo 9.35 — complete compiled color/dimen token set (generated) */", ":root {"]
    for n in sorted(colors):
        for q in sorted(colors[n]):
            qv = "default" if q == "default" else q
            lines.append("  --%s__%s: %s;" % (re.sub(r"[^A-Za-z0-9_-]", "-", n),
                                             re.sub(r"[^A-Za-z0-9_-]", "-", qv), colors[n][q]))
    for n in sorted(dimens):
        for q in sorted(dimens[n]):
            qv = "default" if q == "default" else q
            lines.append("  --dim-%s__%s: %s;" % (re.sub(r"[^A-Za-z0-9_-]", "-", n),
                                                 re.sub(r"[^A-Za-z0-9_-]", "-", qv), dimens[n][q]))
    lines.append("}")
    ensure(out / "ATLAS")
    (out / "ATLAS/tokens.css").write_text("\n".join(lines) + "\n", encoding="utf-8")
    stats["tokens"] = {"color_names": len(colors), "dimen_names": len(dimens),
                       "string_names": len(strings), "style_names": len(styles),
                       "color_values": sum(len(v) for v in colors.values()),
                       "dimen_values": sum(len(v) for v in dimens.values()),
                       "string_values": sum(len(v) for v in strings.values())}


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apk", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    apk_path, out = Path(a.apk), Path(a.out)
    ensure(out)
    t0 = time.time()
    z = zipfile.ZipFile(apk_path)
    apk = APK(str(apk_path))
    arsc = apk.get_android_resources()
    res = Resolver(arsc)

    print("[1/8] ZIP census …", flush=True)
    census = {}
    for i in z.infolist():
        n = i.filename
        ui_class, kind, reason = classify(n)
        raw = z.read(n) if not n.endswith("/") else b""
        census[n] = {"path": n, "size": i.file_size, "compressed_size": i.compress_size,
                     "crc32": "%08X" % i.CRC, "sha256": sha256(raw),
                     "ui_class": ui_class, "kind": kind, "reason": reason,
                     "deliverable": ""}
    stats = {"apk": {"path": str(apk_path), "sha256": sha256(apk_path.read_bytes()),
                     "package": apk.get_package(), "version_name": apk.get_androidversion_name(),
                     "version_code": apk.get_androidversion_code(),
                     "min_sdk": apk.get_min_sdk_version(),
                     "target_sdk": apk.get_target_sdk_version(),
                     "entries": len(census)},
             "generated_at_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
             "method": "REA evidence discipline (morluto/rea) + androguard 4.1.4 static decode"}
    print("      entries:", len(census), flush=True)

    print("[2/8] resources.arsc …", flush=True)
    extract_arsc(apk, z, res, out, stats)
    print("      ids:", stats["arsc"]["resource_ids"], "config rows:", stats["arsc"]["config_rows"], flush=True)

    print("[3/8] manifest + res + assets …", flush=True)
    extract_files(z, res, out, stats, census)
    print("      decoded:", stats["files"]["axml_decoded"], "layouts:", stats["files"]["layouts"], flush=True)

    print("[4/8] DEX UI inventory …", flush=True)
    dex_inventory(z, res, out, stats)
    print("      app classes:", stats["dex"]["app_classes"], flush=True)

    print("[5/8] design tokens …", flush=True)
    build_tokens(out, stats)

    print("[6/8] APK entry census …", flush=True)
    csv_dump(list(census.values()), out / "CATALOGS/APK_ENTRY_CENSUS.csv",
             ["path", "size", "compressed_size", "crc32", "sha256", "ui_class",
              "kind", "reason", "deliverable"])
    counts = collections.Counter(v["ui_class"] for v in census.values())
    stats["entry_classes"] = dict(counts)
    stats["elapsed_seconds"] = round(time.time() - t0, 1)

    print("[7/8] SHA-256 of every emitted file …", flush=True)
    sums = []
    for p in sorted(out.rglob("*")):
        if p.is_file() and p.name not in ("SHA256SUMS.txt", "MANIFEST.json"):
            sums.append("%s  %s" % (sha256(p.read_bytes()), p.relative_to(out).as_posix()))
    (out / "CATALOGS/SHA256SUMS.txt").write_text("\n".join(sums) + "\n", encoding="utf-8")
    stats["emitted_files"] = len(sums)

    print("[8/8] MANIFEST.json …", flush=True)
    jdump(stats, out / "MANIFEST.json")
    print("DONE in %.1fs | emitted %d files" % (stats["elapsed_seconds"], len(sums)), flush=True)


if __name__ == "__main__":
    main()
