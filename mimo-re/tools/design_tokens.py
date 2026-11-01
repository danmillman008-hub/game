#!/usr/bin/env python3
"""Stage 10 — extract the design-token layer (colors, dimensions, fonts).

Mimo keeps its visual language in the resource table, not in code, so the arsc
XML views are the authoritative source. Each token can appear several times
(one entry per configuration: default / night / other density buckets); we keep
document order and classify values by luminance so light/night pairs are
detectable — the *values* are VERIFIED STATIC, the light/night labelling is INFERRED.

Usage:
    python tools/design_tokens.py APK OUT_JSON
"""
from __future__ import annotations

import collections
import json
import re
import sys


def luminance(hexv: str) -> float:
    h = hexv.lstrip("#")
    if len(h) == 8:          # AARRGGBB
        h = h[2:]
    if len(h) != 6:
        return 0.0
    try:
        r, g, b = (int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))
    except ValueError:
        return 0.0
    f = lambda c: c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
    return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(b)


def main(apk_path: str, out_json: str) -> None:
    from loguru import logger
    logger.remove()
    from androguard.core.apk import APK

    apk = APK(apk_path)
    arsc = apk.get_android_resources()
    pkg = arsc.get_packages_names()[0]

    def dump(fn) -> str:
        raw = fn(pkg)
        if isinstance(raw, bytes):
            return raw.decode("utf-8", "replace")
        return str(raw)

    colors_xml = dump(arsc.get_color_resources)
    dimens_xml = dump(arsc.get_dimen_resources)

    colors = collections.OrderedDict()
    for name, val in re.findall(r'<color name="([^"]+)">([^<]+)</color>', colors_xml):
        colors.setdefault(name, []).append(val)

    dimens = collections.OrderedDict()
    for name, val in re.findall(r'<dimen name="([^"]+)">([^<]+)</dimen>', dimens_xml):
        dimens.setdefault(name, []).append(val)

    # app-owned tokens: drop obvious library prefixes
    lib_prefix = ("abc_", "m3_", "material_", "androidx_", "com_", "google_", "design_",
                  "cardview_", "preference_", "notification_", "browser_", "mtrl_", "exo_",
                  "media3_", "adjust_", "firebase_", "ucrop_", "cropimage_", "glance_")
    app_colors = {k: v for k, v in colors.items() if not k.startswith(lib_prefix)}
    app_dimens = {k: v for k, v in dimens.items() if not k.startswith(lib_prefix) and len(k) > 2
                  and not re.fullmatch(r"[a-z]{1,2}\d*", k)}

    pairs = {}
    for k, vals in app_colors.items():
        ls = [luminance(v) for v in vals]
        if len(vals) > 1 and (max(ls) - min(ls)) > 0.25:
            pairs[k] = {"values": vals, "reading": "light/dark pair (inferred from luminance delta)"}

    def numeric_kind(vals):
        nums = []
        for v in vals:
            m = re.match(r"(-?\d+(?:\.\d+)?)(dp|dip|sp|px|pt|s)", v)
            if m:
                nums.append((float(m.group(1)), m.group(2)))
        return nums

    spacings = collections.Counter()
    radii = collections.Counter()
    text_sizes = collections.Counter()
    for k, vals in app_dimens.items():
        for n, unit in numeric_kind(vals):
            if unit in ("dp", "dip") and n <= 64 and (k.startswith(("spacing", "space", "padding",
                                                                    "margin", "gap")) or n % 4 == 0):
                if any(t in k for t in ("radius", "corner", "rounded")):
                    radii[f"{n:g}dp"] += 1
                else:
                    spacings[f"{n:g}"] += 1
            if unit == "sp" and any(t in k for t in ("text_size", "font", "type", "_h1", "_h2",
                                                     "_body", "_caption", "_label", "title")):
                text_sizes[f"{n:g}sp"] += 1

    fonts = sorted({p.split("/")[-1] for p in __import__("glob").glob("/tmp/x/meta/res/font/*")})
    out = {
        "colors": {"count_all": len(colors), "count_app": len(app_colors),
                   "app": app_colors, "light_dark_pairs_inferred": pairs},
        "dimens": {"count_all": len(dimens), "count_app": len(app_dimens), "app": app_dimens},
        "scales": {"radius_values": dict(radii.most_common()),
                   "spacing_values": dict(spacings.most_common()),
                   "text_size_values": dict(text_sizes.most_common())},
        "fonts_shipped": [f for f in fonts if f],
    }
    json.dump(out, open(out_json, "w"), indent=1, ensure_ascii=False)
    print(f"colors all/app: {len(colors)}/{len(app_colors)} | dimens all/app: {len(dimens)}/{len(app_dimens)}")
    print("light/dark pairs inferred:", len(pairs), list(pairs)[:8])
    print("radius values:", dict(radii.most_common(12)))
    print("spacing values:", dict(spacings.most_common(14)))
    print("text sizes:", dict(text_sizes.most_common(12)))
    print("fonts:", out["fonts_shipped"])


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
