#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build_design_v9.py — DESIGN v9: ONE straight vertical line of nodes.

Round 9 (user, 2026-11-04): «معماری گرهها همچنان نیاز به توجه داره … قوس
نده و گرهها رو در یک خط عمودی قرار بده … بازم بازبینی کن کدش رو و بهتر
شبیهسازی کن».

Starts from the already-cleaned v8 template (5 tabs, no routine, no Dictate,
no UI annotations, one exam lock, Mimo exam skin) and replaces ONLY the
path-map geometry with a code-reviewed single-line layout:

  * all 6 nodes at axis x = 196 (no zigzag / alternating offsets)
  * ONE continuous straight connector path, no Q / C / S curve commands
  * hard linearGradient stop exactly at the current node
  * corner radius 16dp from glance_component_btn_square.xml + dimen.xml
  * connector stroke 6dp from lesson_progressbar_height
  * node gap 12dp from spacing_s
  * real practice vectors ic_bolt_charged / ic_bolt_mastered
  * linear state sequence done / done / current / next / bolt / bolt
  * 220ms enter / 400ms exit from rc_checkpoint_window_*.xml

Screenshots are VISUAL_CROSSCHECK_ONLY. No product code.
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
BASE = (UP / "tools" / "design_v8_template.html").read_text(encoding="utf-8")
OUT = UP / "DESIGN" / "index.html"
TPL_OUT = UP / "tools" / "design_v9_template.html"

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
    "codeFidelity": NOD["code_fidelity"],
}

t = BASE
# internal class/id prefix l8 -> l9 (32 occurrences, all class/id names)
t = t.replace("l8", "l9")

# --------------------------------------------------------------------------
# CSS9 — single-line node rules generated from nodeGeometry
# --------------------------------------------------------------------------
size = NDG["node"]["size_dp"]
radius = int(NDG["node"]["corner_radius_dp"])
icon_dp = NDG["node"]["icon_dp"]
stroke = NDG["connector"]["stroke_dp"]
half = size // 2
pos_css = "\n".join(".%s{left:calc(%d%% - %dpx);top:%dpx}" %
                    (n["id"], round(n["cx"] / NDG["viewBox"][0] * 100), half, n["cy"] - half)
                    for n in NDG["nodes"])
enter = NOD["code_fidelity"]["animations"]["enter_ms"] / 1000.0

CSS9 = r'''
/* ============ v9 · SINGLE VERTICAL LINE nodes (data-driven from NODE_CODE_GEOMETRY.json) ============ */
.tabs{grid-template-columns:repeat(5,1fr)}
.tabs .tab{font-size:10px;letter-spacing:0}
.pathwrap.l9{height:620px;margin-top:8px;background:radial-gradient(circle,var(--line2) 1.4px,transparent 1.5px) 0 0/26px 26px;background-color:var(--bg);position:relative;overflow:hidden}
.pathwrap.l9 .connector{position:absolute;inset:0;width:100%;height:100%;pointer-events:none;z-index:0}
.pathwrap.l9 .node{position:absolute;width:__S__px;height:__S__px;border-radius:__R__px;display:flex;align-items:center;justify-content:center;cursor:pointer;z-index:2;transition:transform .__T__s ease,box-shadow .__T__s ease;-webkit-tap-highlight-color:transparent}
.pathwrap.l9 .node:hover{transform:translateY(-2px)}
.pathwrap.l9 .node .ic{width:__I__px;height:__I__px}
.pathwrap.l9 .node.done{background:linear-gradient(158deg,var(--progress) 0%,var(--primary) 100%);box-shadow:0 8px 0 var(--primary-hi),0 12px 18px rgba(37,39,70,.18)}
.pathwrap.l9 .node.done .ic{color:#fff}
.pathwrap.l9 .node.cur{background:var(--card);border:3px solid var(--progress);box-shadow:0 0 0 7px var(--card),0 0 0 10px var(--progress-weak)}
.pathwrap.l9 .node.cur:before{content:"";position:absolute;inset:6px;border:2px solid var(--line2);border-radius:12px}
.pathwrap.l9 .cur-inner{position:relative;z-index:1;display:flex;align-items:center;justify-content:center;width:100%;height:100%}
.pathwrap.l9 .node.cur .ic{width:46px;height:46px;color:var(--text)}
.pathwrap.l9 .hring{width:60px;height:60px;border-radius:50%;background:conic-gradient(from -90deg,var(--progress) 0 55%,var(--progress-bg) 55% 100%);display:flex;align-items:center;justify-content:center;position:relative}
.pathwrap.l9 .hring:before{content:"";position:absolute;inset:8px;border-radius:50%;background:var(--card)}
.pathwrap.l9 .hring b{position:relative;z-index:1;font:700 13px/1 system-ui,sans-serif;color:var(--text)}
.pathwrap.l9 .node.next{background:var(--card);border:2px solid var(--line2);box-shadow:0 8px 0 var(--card-pressed)}
.pathwrap.l9 .node.next .ic{color:var(--progress-bg)}
.pathwrap.l9 .node.bolt.active{background:linear-gradient(158deg,var(--progress),var(--primary));box-shadow:0 8px 0 var(--primary-hi),0 12px 18px rgba(37,39,70,.18)}
.pathwrap.l9 .node.bolt.active .ic{width:__I__px;height:__I__px}
.pathwrap.l9 .node.bolt.optional{background:var(--disabled);box-shadow:0 8px 0 var(--card-pressed)}
.pathwrap.l9 .node.bolt.optional .ic{width:__I__px;height:__I__px}
__POS__
.gloss-fab{position:absolute;z-index:4;right:12px;bottom:8px;width:56px;height:56px;border-radius:50%;background:var(--card);border:1px solid var(--line2);display:flex;align-items:center;justify-content:center;color:var(--text);cursor:pointer;box-shadow:0 3px 8px rgba(37,39,70,.12)}
.gloss-fab .book{width:27px;height:31px;border:2px solid var(--text);border-radius:5px;position:relative;display:flex;align-items:center;justify-content:center}
.gloss-fab .book:before{content:"";position:absolute;left:4px;top:0;bottom:0;width:2px;background:var(--text);opacity:.55}
.gloss-fab .book b{font:700 13px/1 system-ui,sans-serif;margin-left:4px;color:var(--text)}
'''.replace("__S__", str(size)).replace("__R__", str(radius)).replace(
    "__I__", str(icon_dp)).replace("__T__", str(enter).replace("0.", "")).replace("__POS__", pos_css)

t = rx1(t, r'/\* ============ v8 · EXACT Mimo path-map nodes.*?/\* ---- v8 · exam surfaces:',
        CSS9.lstrip("\n") + "/* ---- v9 · exam surfaces (unchanged from v8): MORE Mimo, skin only ---- */\n", "css9")

# --------------------------------------------------------------------------
# learn section: ONE straight connector + 6 nodes on a single axis
# --------------------------------------------------------------------------
cp = NDG["connector_paths"][0]
stops = cp["gradient_stops"]
stop_html = "\n".join(
    '              <stop offset="%s%%" style="stop-color:var(%s)"/>' %
    (round(s["offset"] * 100, 4), {"progress_chapter_primary": "--progress",
                                   "progress_chapter_background": "--progress-bg"}[s["token"]])
    for s in stops)
SVG9 = ('          <svg class="connector" viewBox="0 0 %d %d" preserveAspectRatio="none">\n'
        '            <defs><linearGradient id="pathLineGrad" x1="0" y1="0" x2="0" y2="1">\n'
        '%s\n'
        '            </linearGradient></defs>\n'
        '            <path d="%s" fill="none" stroke="url(#pathLineGrad)" stroke-width="%s" '
        'stroke-linecap="round"/>\n'
        '          </svg>' % (NDG["viewBox"][0], NDG["viewBox"][1], stop_html, cp["d"], stroke))
t = rx1(t, r'          <svg class="connector".*?</svg>', SVG9, "connector9")

CODE = {
    "done": "ic_check_white · completed chapter (PathMapScreenKt)",
    "current": "white double ring · ic_play · 1/2 · bg_circular.xml",
    "next": "ic_square_rounded · unlocked next chapter (NO lock glyph)",
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
    mono = ' data-mono="1"' if n["state"] != "bolt_active" and n["state"] != "bolt_optional" else ""
    practice = ' data-practice="%d"' % n["practice"] if "practice" in n else ""
    node_html.append('          <div %s data-icon="%s" data-size="%d"%s data-nav="%s"%s data-code="%s"></div>'
                     % (attrs, n["icon"], icon_dp, mono, n["click"], practice, CODE[n["state"]]))
t = rx1(t, r'          <div class="node done l9n1.*?data-code="ic_bolt · optional practice"></div>\n',
        "\n".join(node_html) + "\n", "nodes9")

# --------------------------------------------------------------------------
# review chrome + wording -> v9
# --------------------------------------------------------------------------
t = sub1(t, "<title>طرح رابط کاربری v8 — بازآفرینی ۱۰۰٪ میمو از روی کد (Design Review)</title>",
         "<title>طرح رابط کاربری v9 — گرهها روی یک خط عمودی واحد (Design Review)</title>", "title")
t = sub1(t, '<h1>طرح رابط کاربری — دور هشتم <span class="ver">DESIGN v8 · REVIEW</span></h1>',
         '<h1>طرح رابط کاربری — دور نهم <span class="ver">DESIGN v9 · REVIEW</span></h1>', "h1")
t = rx1(t, r"<p>بازآفرینی ۱۰۰٪ بخشهای اصلی میمو.*?</p>",
        "<p>بازآفرینی ۱۰۰٪ بخشهای اصلی میمو <b>از روی کد/مهندسی معکوس</b> · "
        "<b>دور نهم:</b> معماری گرهها دوباره از کد بازبینی شد و همهٔ گرهها "
        "<b>روی یک محور عمودی واحد</b> (x=۱۹۶) قرار گرفتند؛ <b>هیچ قوس / زیگزاگ / زانوی Q</b> "
        "وجود ندارد و مسیر <b>یک خط صاف پیوسته</b> با گرادیان تکهایست. شعاع گره ۱۶dp، "
        "ضخامت خط ۶dp و فاصلهٔ گرهها ۱۲dp مستقیماً از <code>dimen.xml</code> خوانده شدند؛ "
        "بولتها از وکتورهای واقعی <code>ic_bolt_charged</code> / <code>ic_bolt_mastered</code>اند. "
        "پنج تب، بدون روتین/دیکته/یادداشت داخل UI، <b>فقط یک قفل</b> در هاب آزمونها، "
        "چارچوب آزمونها بدون تغییر. اسکرینشاتها فقط چک بصری.</p>", "header-p")
t = sub1(t, '<button data-go="learn" class="on">۱ · یادگیری (گرههای دقیق)</button>',
         '<button data-go="learn" class="on">۱ · یادگیری (خط واحد)</button>', "switcher1")
t = sub1(t, '🔷 هندسهٔ دقیق گرهها v8', '🔷 هندسهٔ دقیق گرهها v9', "node-link")

ASIDE_INSERT = '''  <aside class="spec">
    <h3>دور نهم · یک خط عمودی واحد (بازبینی مجدد کد)</h3>
    <ul>
      <li>همهٔ <b>۶ گره</b> روی محور <code>x=196</code>؛ بدون قوس، بدون زانوی <code>Q</code>، بدون جابهجایی چپ/راست. مسیر <b>یک <code>&lt;path&gt;</code> صاف پیوسته</b> با گرادیان سخت در محل گرهٔ فعلی.</li>
      <li><b>شعاع گره ۱۶dp</b> از <code>glance_component_btn_square.xml → @dimen/glance_component_square_icon_button_corners</code> (جایگزین ۲۶dp حدسی v8) · <b>ضخامت خط ۶dp</b> از <code>lesson_progressbar_height</code> (جای ۱۰dp) · <b>فاصلهٔ ۱۲dp</b> از <code>spacing_s</code>.</li>
      <li>لایههای <code>progress_bar_chapter.xml</code> (پسزمینه / کممرنگ / اصلی، شعاع ۱۰۰dp) مبنای گرادیان خط؛ <code>ic_square_rounded.xml</code> مبنای شکل گرهٔ بعدی؛ انیمیشن ۲۲۰/۴۰۰ms از <code>rc_checkpoint_window_*.xml</code>.</li>
      <li>حالتها خطی شدند: انجامشده / انجامشده / فعلی (½) / <b>بعدیِ بدون قفل</b> / <code>ic_bolt_charged</code> / <code>ic_bolt_mastered</code>. همچنان <b>هیچ گرهٔ قفلی</b> در یادگیری نیست؛ تنها قفل همان کارت «آزمون نهایی / دو هفتگی» است.</li>
      <li>تغییری در ۵ تب، حذف روتین/دیکته/توضیحات داخل UI، ۷ بخش آزمونها، تایمر، ۲۷۰ دقیقه، «پاسخبرگ» ≠ «پاسخنامه» و تفکیک تمرین مبحث ایجاد نشد. ۱۴ اسکرینشات فقط <b>چک بصری</b>.</li>
    </ul>'''
t = rx1(t, r'  <aside class="spec">', ASIDE_INSERT, "aside9-open")

t = sub1(t, "⚠️ این <b>طرح دور هشتم v8</b> است، نه محصول.",
         "⚠️ این <b>طرح دور نهم v9</b> است، نه محصول.", "footer9")
t = sub1(t, "و ظاهر آزمونها فقط با آیکون/رنگ میمو نزدیکتر شد.",
         "و ظاهر آزمونها فقط با آیکون/رنگ میمو نزدیکتر شد. در دور نهم گرهها از نو از کد خوانده شدند و روی <b>یک خط عمودی واحد و بدون قوس</b> چیده شدند.", "footer9-note")
t = sub1(t, "<b>شواهد دور هشتم:</b> ", "<b>شواهد دور نهم (خط واحد):</b> ", "stats9")
t = sub1(t, 'NODE.counts.catalog_rows+" ردیف کاتالوگ گره";',
         'NODE.counts.catalog_rows+" ردیف کاتالوگ گره · چیدمان "+NODE.nodeGeometry.layout.mode+" / محور x="+NODE.nodeGeometry.layout.axis_x;', "stats9-layout")

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

geo = NDG
curves = sum(len(re.findall(r"[QqCcSsTtAa]", p["d"])) for p in geo["connector_paths"])
print(json.dumps({
    "output": str(OUT), "bytes": OUT.stat().st_size,
    "template": str(TPL_OUT), "template_bytes": TPL_OUT.stat().st_size,
    "svg_vectors": len(merged), "views": html.count("<button data-go="),
    "tabs": html.count('data-tab="'), "nodes": len(geo["nodes"]),
    "layout": geo["layout"]["mode"], "axis_x": geo["layout"]["axis_x"],
    "all_nodes_on_axis": all(n["cx"] == geo["layout"]["axis_x"] for n in geo["nodes"]),
    "connector_paths": len(geo["connector_paths"]), "curve_commands": curves,
    "connector_d": geo["connector_paths"][0]["d"],
    "corner_radius_dp": geo["node"]["corner_radius_dp"],
    "stroke_dp": geo["connector"]["stroke_dp"], "gap_dp": geo["layout"]["gap_dp"],
    "locked_nodes": html.count('class="node locked') + html.count("data-locked="),
    "dictate_button": bool(re.search(r'<button[^>]*data-lh="Dictate"', html)),
    "routine": 'data-screen="routine"' in html,
    "method": GEO["method"],
}, ensure_ascii=False, indent=1))
