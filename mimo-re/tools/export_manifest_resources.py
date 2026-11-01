#!/usr/bin/env python3
"""Stage 4 — export decoded manifest + resource metadata as evidence.

    python tools/export_manifest_resources.py APK out_dir

Writes:
    manifest-decoded.xml   full AXML manifest (utf-8, for diffable evidence)
    components.json        activities/services/receivers/providers + exported/launchMode/
                           intent-filters (deep links), meta-data
    resources.json         colors / dimens / style counts / string count / fonts / drawables
"""
from __future__ import annotations

import json
import os
import sys
import xml.etree.ElementTree as ET

ANDROID = "{http://schemas.android.com/apk/res/android}"


def main(apk_path: str, out_dir: str) -> None:
    os.makedirs(out_dir, exist_ok=True)
    from loguru import logger
    logger.remove()
    from androguard.core.apk import APK
    from androguard.core.axml import ARSCParser

    apk = APK(apk_path, testzip=False)

    # ---- decoded manifest ----
    raw = apk.get_android_manifest_axml().get_xml().decode("utf-8", "replace")
    open(os.path.join(out_dir, "manifest-decoded.xml"), "w", encoding="utf-8").write(raw)
    root = ET.fromstring(raw)

    def attrs(el):
        return {k.replace(ANDROID, "android:"): v for k, v in el.attrib.items()}

    components = {"package": root.get("package"), "activities": [], "services": [],
                  "receivers": [], "providers": []}
    app = root.find("application")
    for tag, key in (("activity", "activities"), ("service", "services"),
                     ("receiver", "receivers"), ("provider", "providers")):
        for el in app.findall(tag):
            a = attrs(el)
            filters = []
            for f in el.findall("intent-filter"):
                filters.append({
                    "actions": [x.get(ANDROID + "name") for x in f.findall("action")],
                    "categories": [x.get(ANDROID + "name") for x in f.findall("category")],
                    "data": [{k.replace(ANDROID, "android:"): v for k, v in d.attrib.items()}
                             for d in f.findall("data")],
                    "priority": f.get(ANDROID + "priority"),
                })
            components[key].append({
                "name": a.get("android:name"),
                "exported": a.get("android:exported"),
                "enabled": a.get("android:enabled"),
                "launchMode": a.get("android:launchMode"),
                "screenOrientation": a.get("android:screenOrientation"),
                "theme": a.get("android:theme"),
                "permission": a.get("android:permission"),
                "authorities": a.get("android:authorities"),
                "intentFilters": filters,
            })
    components["application_attrs"] = attrs(app)
    json.dump(components, open(os.path.join(out_dir, "components.json"), "w"), indent=1, ensure_ascii=False)

    # ---- resources ----
    arsc = ARSCParser(apk.get_file("resources.arsc"))
    pkg = arsc.get_packages_names()[0]
    colors = arsc.get_color_resources(pkg)
    dimens = arsc.get_dimen_resources(pkg)
    strings_xml = arsc.get_string_resources(pkg).decode("utf-8", "replace")
    open(os.path.join(out_dir, "resources-strings.xml"), "w", encoding="utf-8").write(strings_xml)
    res = {
        "locales": arsc.get_locales(pkg),
        "colors": {k: v for k, v in list(colors.items())[:400]} if isinstance(colors, dict) else colors,
        "dimens": {k: v for k, v in list(dimens.items())[:200]} if isinstance(dimens, dict) else dimens,
        "strings_count": strings_xml.count("<string "),
        "types": list(arsc.get_types(pkg)),
    }
    json.dump(res, open(os.path.join(out_dir, "resources.json"), "w"), indent=1, ensure_ascii=False, default=str)
    print("activities:", len(components["activities"]),
          "| services:", len(components["services"]),
          "| providers:", len(components["providers"]),
          "| colors:", len(res["colors"]) if isinstance(res["colors"], dict) else "?",
          "| strings:", res["strings_count"])


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else "evidence")
