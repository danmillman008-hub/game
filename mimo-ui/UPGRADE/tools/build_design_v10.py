#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build_design_v10.py — RESTORE the ORIGINAL curved path-map architecture.

Round 10 (user, 2026-11-04): «من حرفمو پس میگیرم … همون معماری اورجینال
رو به کار ببر … اون خطی که قوس داشت … بیشتر کد رو بکاوی و دقیقاً بازسازی کن».

v9's ONE straight line is REVERTED.  Starts from the clean v9 template
(5 tabs / no routine / no Dictate / no UI annotations / one exam lock /
Mimo exam skin) and restores:

  * 3 lanes x=80 / 196 / 312 (116dp = node 92 + spacing_l 24)
  * vertical pitch 116dp -> REAL 24dp gaps between nodes
  * rounded Q elbows (32dp = spacing_xl), two coloured connector segments
  * alternating elbow shapes A/B/A/B/B from the original path map
  * 26dp node corners / 10dp connector / 48dp icons
  * real practice vectors ic_bolt_charged / ic_bolt_mastered
  * 15 test-tracks.json section ordinals mapped onto the 6 visible nodes
  * 220ms / 400ms checkpoint timings

All geometry comes from DESIGN/NODE_CODE_GEOMETRY.json (v10), both at build
time and at runtime.  Screenshots are VISUAL_CROSSCHECK_ONLY.  No product code.
"""
from __future__ import annotations
import json
import re
import sys
from pathlib import Path

UP = Path(sys.argv[1] if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]).resolve()
GEO = json.loads((UP / "DESIGN" / "CODE_GEOMETRY.json").read_text(encoding="utf-8"))
LRN = json.loads((UP / "DESIGN" / "LEARN_CODE_GEOMETRY.json").read_text(encoding="utf-8"))
NOD = json.loads((UP / "DESIGN" / "NODE_CODE_GEOMETRY.json").read_text(encoding="utf-8"))
NDG = NOD["nodeGeometry"]
BASE = (UP / "tools" / "design_v9_template.html").read_text(encoding="utf-8")
OUT = UP / "DESIGN" / "index.html"
TPL_OUT = UP / "tools" / "design_v10_template.html"

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


def css_color(raw):
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


def build_css():
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


def sub1(text, old, new, label):
    n = text.count(old)
    if n != 1:
        raise SystemExit("anchor %s matched %d times" % (label, n))
    return text.replace(old, new, 1)


def rx1(text, pattern, new, label, flags=re.S):
    r = re.compile(pattern, flags)
    ms = list(r.finditer(text))
    if len(ms) != 1:
        raise SystemExit("regex %s matched %d times" % (label, len(ms)))
    return text[:ms[0].start()] + new + text[ms[0].end():]


def to_payload_vector(v):
    return {"source": v["source"],
            "viewport": [v["viewportWidth"], v["viewportHeight"]],
            "size_dp": [v["widthDp"], v["heightDp"]],
            "paths": [{"d": p["d"], "fill": p["fill"], "alpha": None,
                       "fillType": p["fillType"]} for p in v["paths"]],
            "sha_bytes": None}


merged = dict(GEO["vectors"])
for src in (LRN["vectors"], NOD["vectors"]):
    for name, v in src.items():
        if name not in merged:
            merged[name] = to_payload_vector(v)

payload = {"method": GEO["method"], "apk_sha256": GEO["apk_sha256"],
           "sources": GEO["sources"], "vectors": merged, "colors": GEO["colors"],
           "dimens": GEO["dimens"], "styles": GEO["styles"], "strings": GEO["strings"],
           "layouts": GEO["layouts"], "compose_path_class_count": GEO["compose_path_class_count"]}

learn_payload = {
    "method": LRN["method"], "apk": LRN["apk"], "strings": LRN["strings"],
    "contentModel": LRN["contentModel"],
    "counts": {"vectors": len(LRN["vectors"]), "layouts": len(LRN["layouts"]),
               "nav_graphs": len(LRN["navigation"]),
               "strings": sum(len(v) for v in LRN["strings"].values()),
               "colors": len(LRN["tokens"]["colors"]), "dimens": len(LRN["tokens"]["dimens"]),
               "styles": len(LRN["tokens"]["styleNames"]),
               "catalog_rows": sum(1 for _ in open(UP / "CATALOGS" / "MIMO_LEARN_SUBSCREENS.csv", encoding="utf-8")) - 1,
               "dex_classes": sum(v["count"] for k, v in LRN["dex"].items() if k != "literals")},
    "layoutNames": sorted(LRN["layouts"]), "vectorNames": sorted(LRN["vectors"]),
    "subScreens": ["learn", "select-path", "path-overview", "section-detail", "unfinished-track"],
}

node_payload = {
    "method": NOD["method"], "apk_sha256": NOD["apk_sha256"], "round": NOD["round"],
    "nodeGeometry": NDG, "strings": NOD["strings"], "contentModel": NOD["contentModel"],
    "tokens": {"colors": NOD["tokens"]["colors"], "dimens": NOD["tokens"]["dimens"]},
    "shapeNames": sorted(NOD["shapes"]), "dex": NOD["dex"],
    "isolation": NOD["isolation"], "counts": NOD["counts"],
    "codeFidelity": NOD["code_fidelity"], "codeReview": NDG["codeReview"],
}

t = BASE.replace("l9", "l10")          # internal class/id prefix

# --------------------------------------------------------------------------
# CSS10 — original curved zigzag, positions generated from nodeGeometry
# --------------------------------------------------------------------------
size = NDG["node"]["size_dp"]
radius = int(NDG["node"]["corner_radius_dp"])
icon_dp = NDG["node"]["icon_dp"]
half = size // 2
vbw, vbh = NDG["viewBox"]
pos_css = "\n".join(".%s{left:calc(%d%% - %dpx);top:%dpx}" %
                    (n["id"], round(n["cx"] / vbw * 100), half, n["cy"] - half)
                    for n in NDG["nodes"])
enter = NDG["timing"]["checkpoint_enter_ms"] / 1000.0

CSS10 = r'''
/* ============ v10 · ORIGINAL CURVED ZIGZAG nodes (data-driven from NODE_CODE_GEOMETRY.json) ============ */
.tabs{grid-template-columns:repeat(5,1fr)}
.tabs .tab{font-size:10px;letter-spacing:0}
.pathwrap.l10{height:__H__px;margin-top:8px;background:radial-gradient(circle,var(--line2) 1.6px,transparent 1.7px) 0 0/26px 26px;background-color:var(--bg);position:relative;overflow:hidden}
.pathwrap.l10 .connector{position:absolute;inset:0;width:100%;height:100%;pointer-events:none;z-index:0}
.pathwrap.l10 .node{position:absolute;width:__S__px;height:__S__px;border-radius:__R__px;display:flex;align-items:center;justify-content:center;cursor:pointer;z-index:2;transition:transform .__T__s ease,box-shadow .__T__s ease;-webkit-tap-highlight-color:transparent}
.pathwrap.l10 .node:hover{transform:translateY(-2px)}
.pathwrap.l10 .node .ic{width:__I__px;height:__I__px}
.pathwrap.l10 .node.done{background:linear-gradient(158deg,var(--progress) 0%,var(--primary) 100%);box-shadow:0 8px 0 var(--primary-hi),0 12px 18px rgba(37,39,70,.18)}
.pathwrap.l10 .node.done .ic{color:#fff}
.pathwrap.l10 .node.cur{background:var(--card);border:3px solid var(--progress);box-shadow:0 0 0 7px var(--card),0 0 0 10px var(--progress-weak)}
.pathwrap.l10 .node.cur:before{content:"";position:absolute;inset:6px;border:2px solid var(--line2);border-radius:20px}
.pathwrap.l10 .cur-inner{position:relative;z-index:1;display:flex;align-items:center;justify-content:center;width:100%;height:100%}
.pathwrap.l10 .node.cur .ic{width:46px;height:46px;color:var(--text)}
.pathwrap.l10 .hring{width:60px;height:60px;border-radius:50%;background:conic-gradient(from -90deg,var(--progress) 0 55%,var(--progress-bg) 55% 100%);display:flex;align-items:center;justify-content:center;position:relative}
.pathwrap.l10 .hring:before{content:"";position:absolute;inset:8px;border-radius:50%;background:var(--card)}
.pathwrap.l10 .hring b{position:relative;z-index:1;font:700 13px/1 system-ui,sans-serif;color:var(--text)}
.pathwrap.l10 .node.next{background:var(--disabled);box-shadow:0 8px 0 var(--card-pressed);opacity:.92}
.pathwrap.l10 .node.next .ic{color:#fff}
.pathwrap.l10 .node.bolt.active{background:linear-gradient(158deg,var(--progress),var(--primary));box-shadow:0 8px 0 var(--primary-hi),0 12px 18px rgba(37,39,70,.18)}
.pathwrap.l10 .node.bolt.active .ic{width:__I__px;height:__I__px}
.pathwrap.l10 .node.bolt.optional{background:var(--disabled);box-shadow:0 8px 0 var(--card-pressed);opacity:.92}
.pathwrap.l10 .node.bolt.optional .ic{width:__I__px;height:__I__px}
__POS__
.gloss-fab{position:absolute;z-index:4;right:12px;bottom:8px;width:56px;height:56px;border-radius:50%;background:var(--card);border:1px solid var(--line2);display:flex;align-items:center;justify-content:center;color:var(--text);cursor:pointer;box-shadow:0 3px 8px rgba(37,39,70,.12)}
.gloss-fab .book{width:27px;height:31px;border:2px solid var(--text);border-radius:5px;position:relative;display:flex;align-items:center;justify-content:center}
.gloss-fab .book:before{content:"";position:absolute;left:4px;top:0;bottom:0;width:2px;background:var(--text);opacity:.55}
.gloss-fab .book b{font:700 13px/1 system-ui,sans-serif;margin-left:4px;color:var(--text)}
'''.replace("__H__", str(vbh)).replace("__S__", str(size)).replace("__R__", str(radius)).replace(
    "__I__", str(icon_dp)).replace("__T__", str(enter).replace("0.", "")).replace("__POS__", pos_css)

t = rx1(t, r'/\* ============ v9 · SINGLE VERTICAL LINE nodes.*?/\* ---- v9 · exam surfaces',
        CSS10.lstrip("\n") + "/* ---- v10 · exam surfaces (unchanged): MORE Mimo, skin only ---- */\n", "css10")

# --------------------------------------------------------------------------
# learn section: 2 rounded-Q connector paths + 6 zigzag nodes
# --------------------------------------------------------------------------
COLOR = {"done": "var(--progress)", "next": "var(--progress-bg)"}
paths_html = "\n".join(
    '            <path d="%s" fill="none" stroke="%s" stroke-width="%s" '
    'stroke-linecap="round" stroke-linejoin="round" opacity="%s"/>' %
    (p["d"], COLOR[p["role"]], p["stroke_dp"], ".85" if p["role"] == "done" else "1")
    for p in NDG["connector_paths"])
SVG10 = ('          <svg class="connector" viewBox="0 0 %d %d" preserveAspectRatio="none">\n'
         '%s\n'
         '          </svg>' % (vbw, vbh, paths_html))
t = rx1(t, r'          <svg class="connector".*?</svg>', SVG10, "connector10")

CODE = {
    "done": "ic_check_white · completed chapter (PathMapViewModel$onTutorialClick)",
    "current": "white double ring · ic_play / 1/2 · bg_circular.xml",
    "next": "ic_square_rounded · UNLOCKED next chapter · test-tracks.json section",
    "bolt_active": "ic_bolt_charged · charged practice checkpoint",
    "bolt_optional": "ic_bolt_mastered · optional/mastered practice",
}
node_html = []
for n in NDG["nodes"]:
    cls = {"done": "done", "current": "cur", "next": "next",
           "bolt_active": "bolt active", "bolt_optional": "bolt optional"}[n["state"]]
    attrs = 'class="node %s %s"' % (cls, n["id"])
    if n["state"] == "current":
        node_html.append('          <div %s id="curNode" data-nav="%s" data-code="%s">'
                         '<span class="cur-inner" id="curInner"><span class="hring"><b>1/2</b></span></span></div>'
                         % (attrs, n["click"], CODE[n["state"]]))
        continue
    mono = "" if n["state"].startswith("bolt") else ' data-mono="1"'
    practice = ' data-practice="%d"' % n["practice"] if "practice" in n else ""
    section = ' data-section="%d"' % n["section_ordinal"]
    node_html.append('          <div %s data-icon="%s" data-size="%d"%s data-nav="%s"%s%s data-code="%s"></div>'
                     % (attrs, n["icon"], icon_dp, mono, n["click"], practice, section, CODE[n["state"]]))
t = rx1(t, r'          <div class="node done l10n1.*?data-code="ic_bolt_mastered · optional/mastered practice"></div>\n',
        "\n".join(node_html) + "\n", "nodes10")

# --------------------------------------------------------------------------
# review chrome + wording -> v10
# --------------------------------------------------------------------------
t = sub1(t, "<title>طرح رابط کاربری v9 — گرهها روی یک خط عمودی واحد (Design Review)</title>",
         "<title>طرح رابط کاربری v10 — معماری اورجینال قوسدار مسیر یادگیری (Design Review)</title>", "title")
t = sub1(t, '<h1>طرح رابط کاربری — دور نهم <span class="ver">DESIGN v9 · REVIEW</span></h1>',
         '<h1>طرح رابط کاربری — دور دهم <span class="ver">DESIGN v10 · REVIEW</span></h1>', "h1")
t = rx1(t, r"<p>بازآفرینی ۱۰۰٪ بخشهای اصلی میمو.*?</p>",
        "<p>بازآفرینی ۱۰۰٪ بخشهای اصلی میمو <b>از روی کد/مهندسی معکوس</b> · "
        "<b>دور دهم:</b> درخواست «خط صاف» پس گرفته شد و <b>معماری اورجینال قوسدار</b> "
        "برگشت: سه لاین <code>۸۰/۱۹۶/۳۱۲</code>، فاصلهٔ واقعی <b>۲۴dp</b> بین گرهها، "
        "زانوهای گرد <code>Q</code> به شعاع <b>۳۲dp</b>، و دو قطعهٔ رنگی مسیر (انجامشده بنفش / "
        "آینده یاسی). کاوش عمیقتر کد: ۹۲ کلاس <code>PathMap*</code>، ۱۵ فصل / ۲۲۳ درس "
        "<code>test-tracks.json</code>، <code>ArcProgressView</code>، سه لایهٔ "
        "<code>progress_bar_chapter</code> و وکتورهای واقعی بولت. پنج تب، بدون روتین/دیکته/"
        "یادداشت داخل UI، بدون گرهٔ قفل، تنها یک قفل در هاب آزمونها، چارچوب آزمونها بدون تغییر. "
        "اسکرینشاتها فقط چک بصری.</p>", "header-p")
t = sub1(t, '۱ · یادگیری (خط واحد)', '۱ · یادگیری (مسیر قوسدار)', "switcher1")
t = sub1(t, '🔷 هندسهٔ دقیق گرهها v9', '🔷 هندسهٔ اورجینال گرهها v10', "node-link")

ASIDE_INSERT = '''  <aside class="spec">
    <h3>دور دهم · بازگشت به معماری اورجینال (کاوش عمیقتر کد)</h3>
    <ul>
      <li>درخواست دور نهم («یک خط صاف بدون قوس») <b>پس گرفته شد</b>. همان مسیر اصلی میمو برگشت: لاینهای <code>۸۰ / ۱۹۶ / ۳۱۲</code>، جابهجایی چپ‑راست، <b>فاصلهٔ ۲۴dp</b> بین گرهها و زانوهای گرد <code>Q</code> به شعاع <b>۳۲dp</b>.</li>
      <li>شبکه از کد: فاصلهٔ لاینها و گام عمودی <code>۱۱۶ = ۹۲ + spacing_l(۲۴)</code>؛ شعاع زانو <code>spacing_xl(۳۲)</code>؛ ترتیب زانوها <code>A/B/A/B/B</code> (خروج افقی←ورود عمودی / خروج عمودی←ورود افقی) دقیقاً مثل اسکرینشات.</li>
      <li>اعداد تصحیحشدهٔ v9 برگشتند: شعاع گره <b>۲۶dp</b> (۱۶dp مال دکمهٔ مربعی Glance widget است)، ضخامت مسیر <b>۱۰dp</b> (۶dp مال نوار پیشرفت <b>درس</b> است نه خط مسیر). آیکن ۴۸dp، وکتورهای <code>ic_bolt_charged</code> / <code>ic_bolt_mastered</code>، انیمیشن ۲۲۰/۴۰۰ms و گرهٔ «بعدیِ بدون قفل» حفظ شدند.</li>
      <li>کاوش تازه: <b>۹۲ کلاس DEX</b> مسیر (screen / viewmodel / overlay / interactors / practice)، <code>ArcProgressView.getFinishedStrokeColor()/getUnfinishedStrokeColor()/setStrokeWidth(F)</code>، ۱۵ فصل و ۲۲۳ <code>tutorialId</code> با <code>startIndex/endIndex</code> که به ترتیب گرهها نگاشت شدند، ۱۰ شِیپ AXML و ۱۰ وکتور <code>pathData</code>.</li>
      <li>مسیر دو قطعه است: بنفش <code>progress_chapter_primary</code> تا گرهٔ فعلی، یاسی <code>progress_chapter_background</code> بعد از آن. همچنان <b>هیچ گرهٔ قفلی</b> در یادگیری نیست؛ تنها قفل همان کارت «آزمون نهایی / دو هفتگی» است. ۱۴ اسکرینشات فقط <b>چک بصری</b>.</li>
    </ul>'''
t = rx1(t, r'  <aside class="spec">', ASIDE_INSERT, "aside10-open")

t = sub1(t, "⚠️ این <b>طرح دور نهم v9</b> است، نه محصول.",
         "⚠️ این <b>طرح دور دهم v10</b> است، نه محصول.", "footer10")
t = sub1(t, "در دور نهم گرهها از نو از کد خوانده شدند و روی <b>یک خط عمودی واحد و بدون قوس</b> چیده شدند.",
         "در دور دهم درخواست خط صاف پس گرفته شد و <b>معماری اورجینال قوسدار</b> با کاوش عمیقتر کد بازسازی شد.", "footer10-note")
t = sub1(t, "<b>شواهد دور نهم (خط واحد):</b> ", "<b>شواهد دور دهم (معماری اورجینال):</b> ", "stats10")
t = sub1(t, 'NODE.nodeGeometry.layout.mode+" / محور x="+NODE.nodeGeometry.layout.axis_x;',
         'NODE.nodeGeometry.layout.mode+" / قوسهای Q="+NODE.counts.curves+" / فاصله "+NODE.nodeGeometry.layout.node_gap_dp+"dp";', "stats10-layout")

# --------------------------------------------------------------------------
# inject payloads
# --------------------------------------------------------------------------
TPL_OUT.write_text(t, encoding="utf-8")
css = build_css()
js = "var GEO=" + json.dumps(payload, ensure_ascii=False, separators=(",", ":")) + ";"
ljs = "var LEARN=" + json.dumps(learn_payload, ensure_ascii=False, separators=(",", ":")) + ";"
njs = "var NODE=" + json.dumps(node_payload, ensure_ascii=False, separators=(",", ":")) + ";"
html = (t.replace("/*__CSS__*/", css).replace("/*__GEO__*/", js)
         .replace("/*__LEARN__*/", ljs).replace("/*__NODE__*/", njs))
for ph in ("/*__CSS__*/", "/*__GEO__*/", "/*__LEARN__*/", "/*__NODE__*/", "/*__HAB__*/"):
    if ph in html:
        raise SystemExit("placeholder not replaced: " + ph)
OUT.write_text(html, encoding="utf-8")

lanes = sorted({n["cx"] for n in NDG["nodes"]})
print(json.dumps({
    "output": str(OUT), "bytes": OUT.stat().st_size,
    "template": str(TPL_OUT), "template_bytes": TPL_OUT.stat().st_size,
    "svg_vectors": len(merged), "views": html.count("<button data-go="),
    "tabs": html.count('data-tab="'), "nodes": len(NDG["nodes"]),
    "layout": NDG["layout"]["mode"], "lanes": lanes,
    "viewBox": NDG["viewBox"], "gap_dp": NDG["layout"]["node_gap_dp"],
    "elbow_radius_dp": NDG["layout"]["elbow_radius_dp"],
    "connector_paths": len(NDG["connector_paths"]),
    "curve_commands": sum(p["d"].count("Q") for p in NDG["connector_paths"]),
    "single_straight_line_path": '<path d="M196 0 V620"' in html,
    "locked_nodes": html.count('class="node locked') + html.count("data-locked="),
    "dictate_button": bool(re.search(r'<button[^>]*data-lh="Dictate"', html)),
    "routine": 'data-screen="routine"' in html,
    "method": GEO["method"],
}, ensure_ascii=False, indent=1))
