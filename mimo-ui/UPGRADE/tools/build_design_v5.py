#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate DESIGN/index.html from the code-extracted Mimo 9.35 geometry.

Every CSS custom property (day + night), every SVG icon (pathData) and the
string/geometry evidence panel come from DESIGN/CODE_GEOMETRY.json, which is
produced by tools/extract_mimo_geometry.py from decoded APK resource tables.
The screenshots are a visual cross-check only; no pixel is traced.

Usage: python3 tools/build_design_v5.py [UPGRADE_ROOT]
"""
from __future__ import annotations
import json, sys
from pathlib import Path

UP = Path(sys.argv[1] if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]).resolve()
GEO = json.loads((UP / "DESIGN" / "CODE_GEOMETRY.json").read_text(encoding="utf-8"))
TPL = (UP / "tools" / "design_v5_template.html").read_text(encoding="utf-8")
OUT = UP / "DESIGN" / "index.html"

# semantic CSS variable -> ARSC colour resource name
CSS_MAP = {
    "bg": "background_primary", "card": "card_enabled", "card-pressed": "card_pressed",
    "sheet": "card_enabled", "text": "text_primary", "text-weak": "text_weak",
    "primary": "button_primary", "primary-hi": "button_primary_highlight",
    "progress": "progress_chapter_primary", "progress-bg": "progress_chapter_background",
    "progress-weak": "progress_weak", "line": "line_primary", "line2": "line_secondary",
    "weak-icon": "icon_weak", "icon": "icon_primary", "disabled": "card_disabled",
    "yellow": "support_yellow", "blue": "support_blue", "green": "support_green",
    "error": "accent_error", "success": "accent_success", "code-bg": "code_highlight",
    "purple-light": "support_purple_light",
}


def css_color(raw: str | None) -> str:
    """Android #AARRGGBB -> CSS #RRGGBB or rgba()."""
    if not raw or not raw.startswith("#"):
        return "#F6F7FB"
    if len(raw) == 9:
        a, r, g, b = (int(raw[i:i + 2], 16) for i in (1, 3, 5, 7))
        if a == 255:
            return "#%02X%02X%02X" % (r, g, b)
        return "rgba(%d,%d,%d,%.3f)" % (r, g, b, a / 255)
    if len(raw) == 7:
        return raw
    return "#F6F7FB"


def build_css() -> str:
    day, night = [":root{"], ["body.night{"]
    for var, key in CSS_MAP.items():
        c = GEO["colors"].get(key, {})
        day.append("--%s:%s;" % (var, css_color(c.get("default"))))
        n = c.get("night") or c.get("default")
        night.append("--%s:%s;" % (var, css_color(n)))
    day.append("}")
    night.append("}")
    dims = GEO["dimens"]
    for name, cssvar in [("spacing_m", "--sp-m"), ("spacing_s", "--sp-s"),
                         ("toolbar_height", "--toolbar"), ("lesson_progressbar_height", "--progressbar"),
                         ("cardview_corner_radius_large", "--radius-card")]:
        v = dims.get(name, {}).get("default") if name in dims else None
        if not v:
            v = {"spacing_m": "16.000000dip", "spacing_s": "12.000000dip",
                 "toolbar_height": "56.000000dip", "lesson_progressbar_height": "6.000000dip",
                 "cardview_corner_radius_large": "12.000000dip"}[name]
        day.append("%s:%spx;" % (cssvar, float(str(v).replace("dip", ""))))
    return "\n".join(day) + "\n" + "\n".join(night)


def main() -> None:
    css = build_css()
    # a compact evidence payload for the page (full vectors are needed by icon())
    payload = {
        "method": GEO["method"], "apk_sha256": GEO["apk_sha256"],
        "sources": GEO["sources"], "vectors": GEO["vectors"],
        "colors": GEO["colors"], "dimens": GEO["dimens"], "styles": GEO["styles"],
        "strings": GEO["strings"], "layouts": GEO["layouts"],
        "compose_path_class_count": GEO["compose_path_class_count"],
    }
    js = "var GEO=" + json.dumps(payload, ensure_ascii=False, separators=(",", ":")) + ";"
    html = TPL.replace("/*__CSS__*/", css).replace("/*__GEO__*/", js)
    if "/*__CSS__*/" in html or "/*__GEO__*/" in html:
        raise SystemExit("template placeholders not replaced")
    OUT.write_text(html, encoding="utf-8")
    print(json.dumps({
        "output": str(OUT), "bytes": OUT.stat().st_size,
        "css_vars": len(CSS_MAP) * 2, "svg_vectors": len(GEO["vectors"]),
        "code_sources": len(GEO["sources"]), "method": GEO["method"],
    }, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
