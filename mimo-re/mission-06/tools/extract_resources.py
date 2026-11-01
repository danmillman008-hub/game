#!/usr/bin/env python3
"""MISSION-06 — decode Android resources without aapt2.

androguard ships an AXML (binary XML) reader and an ARSC (resource table) parser; that is enough to
recover the navigation graph, XML configs (network security, locales, backup rules) and the design
token table (colors/dimens/styles), none of which are visible from DEX alone.

Inputs : an extracted resource tree (AndroidManifest.xml, resources.arsc, res/**) — read-only.
Outputs: JSON with manifest summary, xml config files (decoded), navigation destinations, token tables.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import warnings
import xml.etree.ElementTree as ET

warnings.filterwarnings("ignore")


def decode_axml(path: str) -> str | None:
    from androguard.core.axml import AXMLPrinter
    try:
        return AXMLPrinter(open(path, "rb").read()).get_xml().decode("utf-8", "replace")
    except Exception:
        return None


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--res", default="/tmp/res")
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    from loguru import logger as lg
    lg.remove()

    out = {"res_root": a.res, "xml_configs": {}, "navigation": [], "strings_sample": [], "tokens": {}}

    # 1) XML configs: everything under res/xml (network security, locales, backup, shortcuts, ...)
    xmldir = os.path.join(a.res, "res", "xml")
    if os.path.isdir(xmldir):
        for fn in sorted(os.listdir(xmldir)):
            text = decode_axml(os.path.join(xmldir, fn))
            if text:
                out["xml_configs"][fn] = text

    # 2) Navigation graphs
    navdir = os.path.join(a.res, "res", "navigation")
    if os.path.isdir(navdir):
        for fn in sorted(os.listdir(navdir)):
            text = decode_axml(os.path.join(navdir, fn))
            if not text:
                continue
            try:
                root = ET.fromstring(text)
            except Exception:
                continue
            dests = []
            A = "{http://schemas.android.com/apk/res/android}"
            for d in root.iter():
                tag = d.tag.split("}")[-1]
                if tag in ("fragment", "activity", "dialog"):
                    dests.append({"type": tag, "id": d.get(A + "id", ""),
                                  "name": d.get(A + "name", ""),
                                  "label": d.get(A + "label", "")})
            out["navigation"].append({"file": fn, "root_start": root.get(A + "startDestination", ""),
                                      "destinations": dests})

    # 3) Design tokens from the resource table
    from androguard.core.axml import ARSCParser
    arsc = ARSCParser(open(os.path.join(a.res, "resources.arsc"), "rb").read())
    pkg = arsc.get_packages_names()[0]
    def tokens(kind: str, n: int) -> dict:
        try:
            res = getattr(arsc, f"get_{kind}_resources")()
        except Exception:
            return {}
        out_: dict[str, str] = {}
        if isinstance(res, dict):
            it = res.items()
        else:
            it = res
        for k, v in list(it)[:n]:
            out_[str(k)] = str(v)[:80]
        return out_
    out["tokens"] = {
        "colors": tokens("color", 400),
        "dimens": tokens("dimen", 400),
        "bools": tokens("bool", 100),
        "integers": tokens("integer", 100),
    }

    # 4) string pool size + a small, non-content sample (UI chrome only)
    sp = arsc.stringpool_main
    raw = []
    for i in range(sp.stringCount):
        try:
            v = sp.getString(i)
        except Exception:
            continue
        if isinstance(v, str):
            raw.append(v)
    out["string_count"] = len(raw)
    out["strings_has_event_stream"] = any("text/event-stream" in s for s in raw)
    json.dump(out, open(a.out, "w", encoding="utf-8"), indent=1)
    print(f"xml configs: {len(out['xml_configs'])}  nav files: {len(out['navigation'])} "
          f"destinations: {sum(len(n['destinations']) for n in out['navigation'])}")
    print(f"colors: {len(out['tokens']['colors'])} dimens: {len(out['tokens']['dimens'])} "
          f"bools: {len(out['tokens']['bools'])} strings: {out['string_count']}")
    print("xml files:", sorted(out["xml_configs"])[:14])
    return 0


if __name__ == "__main__":
    sys.exit(main())
