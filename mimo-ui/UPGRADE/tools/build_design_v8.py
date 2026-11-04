#!/usr/bin/env python3
# ARCHIVED (round 9): superseded by extract_mimo_nodes_v9.py / build_design_v9.py / finalize_v9.py.
# -*- coding: utf-8 -*-
"""build_design_v8.py — DESIGN v8 from code-extracted Mimo 9.35 geometry.

Round 8 (user, 2026-11-04):
  1. «روتین روزانه» and the WHOLE Habitica idea removed (tab, screen, payload, docs).
  2. «دیکته / Dictate» removed from the AI assistant composer.
  3. All design/policy/EPM/timer annotation notes removed from the phone UI
     (also the code annotations that "slipped into" other screens).
     Exam-hub labels/templates and the descriptive answer text are KEPT.
  4. NO locked node/section anywhere except the ONE pre-existing exam-hub
     «آزمون نهایی / دو هفتگی» lock, which is left untouched.
  5. MAIN TASK: Learn path-map NODES reconstructed exactly — data-driven from
     DESIGN/NODE_CODE_GEOMETRY.json (v8): 92dp squares / 26dp corners / 8dp 3D
     lip, done checks, white double-ring current with 1/2 progress ring,
     play variant, rounded-elbow Q connector, dotted grid, bolt practice nodes,
     floating book affordance. Screenshots are VISUAL_CROSSCHECK_ONLY.
  6. Exam surfaces made MORE Mimo-like in APPEARANCE ONLY (real Mimo vectors +
     ARSC colours/radii/typography). NO architecture/timer/policy change.

Pipeline:
  extract_mimo_geometry.py + extract_mimo_learn_v6.py + extract_mimo_nodes_v8.py
  -> build_design_v8.py -> DESIGN/index.html + tools/design_v8_template.html
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
BASE = (UP / "tools" / "design_v7_template.html").read_text(encoding="utf-8")
OUT = UP / "DESIGN" / "index.html"
TPL_OUT = UP / "tools" / "design_v8_template.html"

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


def drop(text, pattern, label):
    return rx1(text, pattern, "", label)


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
}

# --------------------------------------------------------------------------
# CSS8 — generated partly from NODE_GEOMETRY (code-driven positions)
# --------------------------------------------------------------------------
pos_css = []
for i, n in enumerate(NDG["nodes"]):
    pct = round(n["cx"] / NDG["viewBox"][0] * 100)
    pos_css.append(".%s{left:calc(%d%% - %dpx);top:%dpx}" %
                   (n["id"], pct, NDG["node"]["size_dp"] // 2, n["cy"] - NDG["node"]["size_dp"] // 2))
NODE_POS_CSS = "\n".join(pos_css)

CSS8 = r'''
/* ============ v8 · EXACT Mimo path-map nodes (data-driven from NODE_CODE_GEOMETRY.json) ============ */
.tabs{grid-template-columns:repeat(5,1fr)}
.tabs .tab{font-size:10px;letter-spacing:0}
.pathwrap.l8{height:620px;margin-top:8px;background:radial-gradient(circle,var(--line2) 1.6px,transparent 1.7px) 0 0/26px 26px;background-color:var(--bg);position:relative;overflow:hidden}
.pathwrap.l8 .connector{position:absolute;inset:0;width:100%;height:100%;pointer-events:none;z-index:0}
.pathwrap.l8 .node{position:absolute;width:92px;height:92px;border-radius:26px;display:flex;align-items:center;justify-content:center;cursor:pointer;z-index:2;transition:transform .12s ease;-webkit-tap-highlight-color:transparent}
.pathwrap.l8 .node:hover{transform:translateY(-2px)}
.pathwrap.l8 .node .ic{width:44px;height:44px}
.pathwrap.l8 .node.done{background:linear-gradient(158deg,var(--progress) 0%,var(--primary) 100%);box-shadow:0 8px 0 var(--primary-hi),0 12px 18px rgba(37,39,70,.18)}
.pathwrap.l8 .node.done .ic{color:#fff}
.pathwrap.l8 .node.cur{background:var(--card);border:3px solid var(--progress);box-shadow:0 0 0 7px var(--card),0 0 0 10px var(--progress-weak)}
.pathwrap.l8 .node.cur:before{content:"";position:absolute;inset:6px;border:2px solid var(--line2);border-radius:20px}
.pathwrap.l8 .cur-inner{position:relative;z-index:1;display:flex;align-items:center;justify-content:center;width:100%;height:100%}
.pathwrap.l8 .node.cur .ic{width:46px;height:46px;color:var(--text)}
.pathwrap.l8 .hring{width:60px;height:60px;border-radius:50%;background:conic-gradient(from -90deg,var(--progress) 0 55%,var(--progress-bg) 55% 100%);display:flex;align-items:center;justify-content:center;position:relative}
.pathwrap.l8 .hring:before{content:"";position:absolute;inset:8px;border-radius:50%;background:var(--card)}
.pathwrap.l8 .hring b{position:relative;z-index:1;font:700 13px/1 system-ui,sans-serif;color:var(--text)}
.pathwrap.l8 .node.bolt.active{background:linear-gradient(158deg,var(--progress),var(--primary));box-shadow:0 8px 0 var(--primary-hi),0 12px 18px rgba(37,39,70,.18)}
.pathwrap.l8 .node.bolt.active .ic{width:46px;height:46px;color:var(--text)}
.pathwrap.l8 .node.bolt.optional{background:var(--disabled);box-shadow:0 8px 0 var(--card-pressed)}
.pathwrap.l8 .node.bolt.optional .ic{width:46px;height:46px;color:#fff}
''' + NODE_POS_CSS + r'''
.gloss-fab{position:absolute;z-index:4;right:12px;bottom:8px;width:56px;height:56px;border-radius:50%;background:var(--card);border:1px solid var(--line2);display:flex;align-items:center;justify-content:center;color:var(--text);cursor:pointer;box-shadow:0 3px 8px rgba(37,39,70,.12)}
.gloss-fab .book{width:27px;height:31px;border:2px solid var(--text);border-radius:5px;position:relative;display:flex;align-items:center;justify-content:center}
.gloss-fab .book:before{content:"";position:absolute;left:4px;top:0;bottom:0;width:2px;background:var(--text);opacity:.55}
.gloss-fab .book b{font:700 13px/1 system-ui,sans-serif;margin-left:4px;color:var(--text)}
/* ---- v8 · exam surfaces: MORE Mimo (icons/colours/radii/type ONLY) ---- */
.konkur .appbar{background:var(--card);border-bottom:1px solid var(--line2);padding:0 16px;height:var(--toolbar);min-height:56px;margin-bottom:10px}
.konkur .appbar b{font:700 18px/1.2 system-ui,sans-serif;color:var(--text)}
.konkur .chips .chip{background:var(--card-pressed);border:0;border-radius:999px;padding:6px 13px;font:700 11px/1 system-ui,sans-serif;color:var(--text-weak)}
.konkur .chips .chip.on{background:var(--primary);color:#fff;box-shadow:0 3px 0 var(--primary-hi)}
.konkur .sec{font:700 13px/1.2 system-ui,sans-serif;color:var(--primary);letter-spacing:.3px;margin:16px 14px 8px}
.konkur .cat-meta{background:var(--card);border:1px solid var(--line2);border-radius:12px;padding:8px 11px;font:400 10px/1.8 system-ui,sans-serif;color:var(--text-weak);margin:0 14px 10px}
.konkur .cat-meta b{color:var(--text)}
.konkur .grid3{gap:12px}
.konkur .nodek{background:var(--card-pressed);border:2px solid var(--line2);border-radius:20px;height:88px;box-shadow:0 4px 0 var(--card-pressed);color:var(--primary)}
.konkur .nodek:hover{border-color:var(--primary)}
.konkur .nodek .ic{width:30px;height:30px}
.konkur .nodek .mini{background:var(--card);border:1px solid var(--line2);border-radius:999px;padding:2px 7px;font:700 9px/1.2 system-ui,sans-serif;color:var(--primary)}
.konkur .label{font:700 12px/1.35 system-ui,sans-serif;color:var(--text)}
.konkur .card{background:var(--card);border:1px solid var(--line2);border-radius:16px;box-shadow:0 3px 0 var(--card-pressed)}
.konkur .card b{color:var(--text);font:700 15px/1.3 system-ui,sans-serif}
.konkur .timerchip{border:1px solid var(--primary);background:var(--card-pressed);color:var(--primary);border-radius:999px;font:700 12px/1 system-ui,sans-serif;gap:5px}
.konkur .opt{background:var(--card);border:2px solid var(--line2);border-radius:16px;padding:11px 13px}
.konkur .opt span{background:var(--card-pressed);color:var(--primary);font-weight:700}
.konkur .opt.on{border-color:var(--primary);background:var(--card-pressed)}
.konkur .qtext{font:700 15px/1.9 system-ui,sans-serif;color:var(--text)}
.konkur .qnav .btn,.konkur .qfoot .btn{border:1px solid var(--line2);background:var(--card);border-radius:999px;color:var(--text-weak)}
.konkur .qnav .btn{font:700 12px/1 system-ui,sans-serif;color:var(--text)}
.konkur .tag{background:var(--card-pressed);border:1px solid var(--primary);color:var(--primary);border-radius:999px}
.konkur .wrong{background:var(--card-pressed);border:1px solid var(--line2);border-radius:12px}
.konkur .palette div{border-radius:12px;border:1px solid var(--line2)}
.konkur .palette div.done{background:var(--card-pressed);border-color:var(--primary)}
.konkur .iconbtn{background:var(--card-pressed);border:1px solid var(--line2);color:var(--primary)}
.konkur .keytabs button,.konkur .mini-btn,.konkur .field input{border-radius:12px}
/* ---- v8 · no visible code/design annotations in the phone UI ---- */
.screen .hint[data-hidden],.screen [hidden]{display:none!important}
'''

# --------------------------------------------------------------------------
# LEARN8 — nodes generated from NODE_GEOMETRY (not hand-placed)
# --------------------------------------------------------------------------
def build_learn_nodes():
    parts = []
    for i, n in enumerate(NDG["nodes"]):
        st, nid = n["state"], n["id"]
        alias = ' l6n1' if i == 0 else ''
        if st == "done":
            parts.append('          <div class="node done %s%s" data-icon="%s" data-size="44" data-mono="1" data-nav="chapter" data-code="%s"></div>'
                         % (nid, alias, n["icon"], "PathMapScreenKt · completed chapter"))
        elif st == "current":
            ring = n.get("ring", "1/2")
            parts.append('          <div class="node cur %s" id="curNode" data-nav="chapter" data-code="white double ring · %s · %s"><span class="cur-inner" id="curInner"><span class="hring"><b>%s</b></span></span></div>'
                         % (nid, n["icon"], NDG["current"]["ring_source"], ring))
        elif st == "bolt_active":
            parts.append('          <div class="node bolt active %s" data-icon="%s" data-size="46" data-mono="1" data-nav="section-practice" data-practice="%d" data-code="ic_flash · active practice checkpoint"></div>'
                         % (nid, n["icon"], int(n["practice"])))
        elif st == "bolt_optional":
            parts.append('          <div class="node bolt optional %s" data-icon="%s" data-size="46" data-mono="1" data-nav="section-practice" data-practice="%d" data-code="ic_bolt · optional practice"></div>'
                         % (nid, n["icon"], int(n["practice"])))
    return "\n".join(parts)


conn = []
for cp in NDG["connector_paths"]:
    color = "var(--progress)" if cp["role"] == "done" else "var(--progress-bg)"
    op = ".85" if cp["role"] == "done" else "1"
    conn.append('            <path d="%s" fill="none" stroke="%s" stroke-width="10" stroke-linecap="round" stroke-linejoin="round" opacity="%s"/>' % (cp["d"], color, op))
CONN_HTML = "\n".join(conn)

LEARN8 = r'''      <!-- ============ 1. LEARN / PATH MAP = v8 EXACT nodes, data-driven from code ============ -->
      <section class="screen mimo on" data-screen="learn">
        <div class="mimo-hdr l6">
          <div class="pill"><span data-icon="ic_coin" data-size="26"></span><b>1,272</b></div>
          <div class="pill"><span data-icon="ic_key" data-size="24"></span><span class="inf" data-icon="ic_infinity" data-size="20" data-mono="1"></span></div>
          <div class="pill"><span data-icon="ic_streak_active" data-size="26"></span><b>0</b></div>
        </div>
        <div class="coursebar l6">
          <button class="lst" id="pathSwitchBtn" data-nav="select-path" data-code="ic_list_bulleted → select_path"><span data-icon="ic_list_bulleted" data-size="24" data-mono="1"></span></button>
          <b data-fa="کنکور تجربی">Back-End Developer</b>
        </div>
        <button class="overview-card" id="overviewEntry" data-nav="path-overview" data-code="ViewsKt$OverviewEntryPointHeader → path_see_course_overview">
          <span class="oc-kicker" data-fa="مسیر شغلی">Career path</span>
          <span class="oc-title" data-fa="۳. سلول و بافت">3. Arrays &amp; Functions</span>
          <span class="oc-bar"><i style="width:43%"></i></span>
        </button>
        <div class="pathwrap l6 l8">
          <svg class="connector" viewBox="0 0 __VBW__ __VBH__" preserveAspectRatio="none">
__CONN__
          </svg>
__NODES__
          <div class="gloss-fab" data-glossary="1" data-code="floating book / dictionary affordance"><span class="book"><b>A</b></span></div>
        </div>
      </section>'''
LEARN8 = (LEARN8.replace('__VBW__', str(NDG['viewBox'][0]))
          .replace('__VBH__', str(NDG['viewBox'][1]))
          .replace('__CONN__', CONN_HTML)
          .replace('__NODES__', build_learn_nodes()))

# --------------------------------------------------------------------------
# Template transformations
# --------------------------------------------------------------------------
t = BASE

t = sub1(t, "<title>طرح رابط کاربری v7 — بازآفرینی ۱۰۰٪ میمو از روی کد (Design Review)</title>",
         "<title>طرح رابط کاربری v8 — بازآفرینی ۱۰۰٪ میمو از روی کد (Design Review)</title>", "title")
t = sub1(t, '<h1>طرح رابط کاربری — دور هفتم <span class="ver">DESIGN v7 · REVIEW</span></h1>',
         '<h1>طرح رابط کاربری — دور هشتم <span class="ver">DESIGN v8 · REVIEW</span></h1>', "h1")
t = rx1(t, r"<p>بازآفرینی ۱۰۰٪ بخشهای اصلی میمو.*?</p>",
        "<p>بازآفرینی ۱۰۰٪ بخشهای اصلی میمو <b>از روی کد/مهندسی معکوس</b> · "
        "<b>دور هشتم:</b> گرههای مسیر یادگیری <b>واقعاً از کد</b> بازسازی شدند (مربع ۹۲dp، لبهٔ سهبعدی، تیک بنفش، "
        "حلقهٔ دوتایی سفید + حلقهٔ ½، اتور گردگوشهٔ Q، نقطهچین، گرههای رعدوبرق و کتاب شناور) و <b>هیچ گرهٔ قفلی</b> ندارند. "
        "«روتین روزانه» و کل ایدهٔ امتیازدهی حذف شد؛ «دیکته» حذف شد؛ یادداشتهای توضیحی داخل UI پاک شدند؛ "
        "ظاهر بخش آزمونها فقط در آیکون/رنگ/شعاع به میمو نزدیکتر شد، <b>بدون هیچ تغییر معماری</b>. "
        "اسکرینشاتها فقط چک بصری.</p>", "header-p")

t = sub1(t, '    <a class="btn" href="HABITICA_SCORING.json">⚖️ قواعد امتیازدهی روتین</a>\n', '', "hab-link")
t = sub1(t, '<a class="btn" href="NODE_CODE_GEOMETRY.json">🔷 هندسهٔ گرهها v7</a>',
         '<a class="btn" href="NODE_CODE_GEOMETRY.json">🔷 هندسهٔ دقیق گرهها v8</a>', "node-link")

SWITCHER8 = '''<div class="switcher" id="switcher">
      <button data-go="learn" class="on">۱ · یادگیری (گرههای دقیق)</button>
      <button data-go="select-path">۲ · انتخاب مسیر / درسها</button>
      <button data-go="path-overview">۳ · نمای مسیر + گواهی</button>
      <button data-go="section-detail">۴ · داخل مبحث (فصلها)</button>
      <button data-go="chapter">۵ · کارت شروع فصل</button>
      <button data-go="lesson">۶ · صفحهٔ درس</button>
      <button data-go="section-practice">۷ · تمرین مبحث (رعدوبرق)</button>
      <button data-go="leaderboard">۸ · لیدربورد + اطلاعات من</button>
      <button data-go="user-profile">۹ · پروفایل کاربر</button>
      <button data-go="profile">۱۰ · پروفایل</button>
      <button data-go="exam-hub">۱۱ · هاب آزمونها</button>
      <button data-go="exam-run">۱۲ · اجرای آزمون</button>
      <button data-go="exam-result">۱۳ · صفحهٔ آخر آزمون</button>
      <button data-go="ai">۱۴ · چت AI</button>
    </div>'''
t = rx1(t, r'<div class="switcher" id="switcher">.*?\n    </div>', SWITCHER8, "switcher")

t = sub1(t, "\n</style>", CSS8 + "\n</style>", "css8")
t = re.sub(r'\.node-start(?:\{|:after\{)[^\n]*\}\n', '', t)  # dead v7 START-bubble CSS
t = rx1(t, r'      <!-- ============ 1\. LEARN.*?</section>', LEARN8, "learn8")

# ---- routine screen + HAB payload removed entirely ----
t = rx1(t, r'      <!-- ============ v7 · DAILY ROUTINE.*?</section>\n\n', '', "routine-screen")
t = sub1(t, "<script>/*__HAB__*/</script>\n", "", "hab-script")

# ---- Dictate removed ----
t = drop(t, r'            <button class="fchip ai-foot-chip" data-lh="Dictate">.*?</button>\n', "dictate")

# ---- visible .lh debug labels removed (data-lh audit attributes stay) ----
t = re.sub(r'<span class="lh">[^<]*</span>', '', t)
# ---- title tooltips -> invisible data-code audit attributes ----
t = re.sub(r'\btitle="([^"]*)"', lambda m: 'data-code="' + m.group(1) + '"', t)

# ---- annotation notes removed from the phone UI ----
t = drop(t, r'          <p class="note" style="margin-top:18px">.*?</p>\n', "note-selectpath")
t = drop(t, r'        <p class="note" style="margin:0 18px 22px">.*?</p>\n', "note-pathoverview")
t = drop(t, r'        <p class="sd-note" id="sdNote">.*?</p>\n', "note-sd")
t = drop(t, r'      q\("#sdNote"\)\.innerHTML=[^\n]*\n', "js-sdNote")
t = drop(t, r'        <div class="hint">📜 .*?</div>\n', "note-hub-first")
t = drop(t, r'        <p class="note">⬇️ .*?</p>\n', "note-hub-last")
# policyHint must stay EMPTY: the user explicitly removed that explanation from UI
t = rx1(t, r'    q\("#policyHint"\)\.innerHTML=p\.during\s*\? ".*?"\s*: ".*?";\n',
        '    /* v8: no policy explanation inside the UI */\n', "js-policy-text")
t = sub1(t, "NS.path_nodes.lesson_feedback_keep_going", "NS.chapter_start.lesson_feedback_keep_going", "js-ns-group")
t = sub1(t,
         '        <div class="hint" id="policyHint">سیاست: <b>عادی / زماندار / تحلیلی</b> ← «پاسخبرگ» (گزینههای زدهشده) و «پاسخنامه» (جواب تشریحی + توضیحات) حین آزمون؛ <b>جامع / جمع بندی / نهایی</b> ← زمان خالص آزمون، و در پایان آزمون صفحهٔ پاسخنامه باز میشود.</div>',
         '        <div class="hint" id="policyHint" hidden></div>', "policy-hint")
t = drop(t, r'        <div class="hint">💡 .*?</div>\n', "note-epm")
t = drop(t, r'        <div class="hint">تایمر معکوس .*?</div>\n', "note-timer")
t = drop(t, r'        <p class="note">همان تکدکمهٔ .*?</p>\n', "note-result")
t = sub1(t, '<div class="note" style="margin:0">ai_tutor_chat_header · پوستهٔ میمو</div>', '', "note-ai-head")
t = drop(t, r'          <div class="composer-note">.*?</div>\n', "note-composer")
t = drop(t, r'        <p class="note">✅ چت ساده .*?</p>\n', "note-ai-last")
t = drop(t, r'        <div class="hint">شمارش معکوس؛ .*?</div>\n', "note-timer-sheet")
t = drop(t, r'          <div class="note">قابلیتها:.*?</div>\n', "note-keydesc")
t = drop(t, r'        <p class="sd-note" data-fa="تمرینهای .*?</p>\n', "note-practice")

# ---- exam surfaces: MORE Mimo (vectors + tokens only) ----
def mimo_exam_icons(text):
    def repl(m):
        attrs, glyph = m.group(1), m.group(2)
        km = re.search(r'data-kind="([^"]+)"', attrs)
        k = km.group(1) if km else "normal"
        if glyph == "✓":
            v = "ic_task_completed"
        elif glyph == "🔒":
            v = "ic_lock_alt_02"
        elif glyph == "⏱":
            v = "ic_clock_black_24dp"
        else:
            v = {"comprehensive": "ic_trophy", "timed": "ic_clock_black_24dp",
                 "normal": "ic_file", "analytical": "ic_target",
                 "review": "ic_sparks_alt"}.get(k, "ic_file")
        return ('<div class="nodek"' + attrs + '><span data-icon="' + v +
                '" data-size="28" data-mono="1"></span><span class="mini">')
    return re.sub(r'<div class="nodek"([^>]*)>([◇⏱✓🔒])<span class="mini">', repl, text)

t = mimo_exam_icons(t)
t = re.sub(r'>→</button>', '><span data-icon="ic_arrow_back_24" data-size="20" data-mono="1"></span></button>', t)
t = sub1(t, '<button class="iconbtn" data-help="هاب آزمون">؟</button>',
         '<button class="iconbtn" data-help="هاب آزمون"><span data-icon="ic_help" data-size="18" data-mono="1"></span></button>', "help-icon")
t = sub1(t, '<button class="timerchip" id="timerChip">⏱ <span id="timerLabel">تنظیم زمان</span></button>',
         '<button class="timerchip" id="timerChip"><span data-icon="ic_clock_black_24dp" data-size="16" data-mono="1"></span><span id="timerLabel">تنظیم زمان</span></button>', "timer-icon")
t = sub1(t, '<button class="iconbtn" data-sheet="historySheet">🕘</button>',
         '<button class="iconbtn" data-sheet="historySheet"><span data-icon="ic_clock_black_24dp" data-size="18" data-mono="1"></span></button>', "hist-icon")
t = sub1(t, '<button class="send" id="aiSend">↩</button>',
         '<button class="send" id="aiSend"><span data-icon="ic_arrow_right" data-size="16" data-mono="1"></span></button>', "send-icon")

t = sub1(t, '<button class="on" data-mode="TEACH"', '<button class="on" data-mode="TEACH" data-lh="TEACH mode"', "lh-teach")
t = sub1(t, '<button data-mode="PRACTICE"', '<button data-mode="PRACTICE" data-lh="PRACTICE mode"', "lh-practice")

# ---- bottom nav back to 5 tabs ----
t = drop(t, r'        <div class="tab" data-tab="Routine">.*?</div>\n', "routine-tab")
t = sub1(t, '      <!-- ============ BOTTOM NAV = 6 tabs (v7 explicit override; MAX forbidden) ============ -->',
         '      <!-- ============ BOTTOM NAV = 5 tabs (v8: روتین روزانه removed; MAX forbidden) ============ -->', "nav-comment")

# ---- JS: navigation, locked rows, routine block ----
t = sub1(t,
         '  var tabMap={learn:"Learn",chapter:"Learn",lesson:"Learn","select-path":"Learn","path-overview":"Learn","section-detail":"Learn","section-practice":"Learn",leaderboard:"Leaderboard","user-profile":"Leaderboard",profile:"Profile","exam-hub":"Practice","exam-run":"Practice","exam-result":"Practice",ai:"AI",routine:"Routine"};',
         '  var tabMap={learn:"Learn",chapter:"Learn",lesson:"Learn","select-path":"Learn","path-overview":"Learn","section-detail":"Learn","section-practice":"Learn",leaderboard:"Leaderboard","user-profile":"Leaderboard",profile:"Profile","exam-hub":"Practice","exam-run":"Practice","exam-result":"Practice",ai:"AI"};', "tabmap")
t = sub1(t,
         '  var tabScreen={Learn:"learn",Practice:"exam-hub",AI:"ai",Leaderboard:"leaderboard",Profile:"profile",Routine:"routine"};',
         '  var tabScreen={Learn:"learn",Practice:"exam-hub",AI:"ai",Leaderboard:"leaderboard",Profile:"profile"};', "tabscreen")
t = sub1(t,
         '  qa("#tabs .tab").forEach(function(t){t.addEventListener("click",function(){go(tabScreen[t.dataset.tab]);toast("تب "+t.dataset.tab+" · ناوبری ۶ تب (۵ تب میمو + روتین روزانه)")})});',
         '  qa("#tabs .tab").forEach(function(t){t.addEventListener("click",function(){go(tabScreen[t.dataset.tab]);toast("تب "+t.dataset.tab+" · ناوبری ۵ تب میمو")})});', "tabtoast")

# section detail: NO locked rows
t = sub1(t, '    b.className="sd-row "+(i<2?"done":i===2?"cur":"locked");',
         '    b.className="sd-row "+(i<2?"done":i===2?"cur":"");', "sd-no-lock-class")
t = sub1(t, "+(i<2?\"ic_check_white\":i===2?\"ic_play\":\"ic_lock_alt_02\")+",
         "+(i<2?\"ic_check_white\":i===2?\"ic_play\":\"ic_arrow_right\")+", "sd-no-lock-icon")
t = rx1(t, r'  var soon=document\.createElement\("button"\);soon\.className="sd-row locked";.*?LR\.appendChild\(soon\);\n',
        '', "sd-no-coming-soon-row")

# replace the whole routine JS + delegated handler + stats tail with v8 JS
START = '  /* ============ v7 · daily routine: Habitica SCORING RULES only, Mimo skin ============ */'
END = '\n  histRender();render();'
V8_JS = r'''  /* ============ v8 · «روتین روزانه» و کل ایدهٔ Habitica حذف شد ============ */
  renderPractice(4);

  /* ============ v8 · current-node state (review chrome only, NOT app UI) ============ */
  function setCurState(mode){
    var box=q("#curInner");if(!box)return;
    if(mode==="play")box.innerHTML='<span data-icon="ic_play" data-size="46" data-mono="1"></span>';
    else box.innerHTML='<span class="hring"><b>1/2</b></span>';
    paintIcons(box);
  }
  var nh=q("#nodeHalfBtn"),nplay=q("#nodePlayBtn");
  if(nh)nh.addEventListener("click",function(){setCurState("half");toast("گرهٔ فعلی: حلقهٔ ½")});
  if(nplay)nplay.addEventListener("click",function(){setCurState("play");toast("گرهٔ فعلی: پلی")});

  /* ============ v8 · delegated interactions: bolt nodes / glossary / practice ============ */
  document.addEventListener("click",function(e){
    var b=e.target.closest("[data-practice]");
    if(b){
      var n=+b.dataset.practice;
      if(!n)return;
      renderPractice(n);
      toast("تمرین مبحث: تا فصل "+fa(n)+" (جدا از آزمون کنکور)");
      return;
    }
    var gl=e.target.closest("[data-glossary]");
    if(gl){toast("واژهنامهٔ مبحث");return}
    var o=e.target.closest(".sp-opt");
    if(o){qa(".sp-opt",o.parentNode).forEach(function(x){x.classList.remove("on")});o.classList.add("on");return}
  });

  var n8=q("#nodeStats");
  if(n8)n8.innerHTML="<b>شواهد دور هشتم:</b> "+NODE.counts.vectors+" وکتور pathData · "+NODE.counts.strings+" رشتهٔ ARSC · "+NODE.counts.shapes+" شِیپ AXML · "+NODE.counts.pathmap_classes+" کلاس PathMap DEX · "+NODE.counts.sections+" فصل / "+NODE.counts.tutorial_ids+" شناسهٔ درس · "+NODE.counts.catalog_rows+" ردیف کاتالوگ گره";
  /* v8 · node positions re-applied at runtime from the injected code geometry */
  (function(){
    var G=NODE.nodeGeometry, vb=G.viewBox, sz=G.node.size_dp;
    G.nodes.forEach(function(n){
      var el=q("."+n.id);
      if(el){el.style.left=(n.cx/vb[0]*100)+"%";el.style.top=(n.cy-sz/2)+"px";}
    });
    var c=q(".pathwrap.l8 .connector");
    if(c)c.setAttribute("viewBox","0 0 "+vb[0]+" "+vb[1]);
  })();
  paintIcons();
'''
a = t.find(START)
b = t.find(END, a)
if a < 0 or b < 0:
    raise SystemExit("routine JS anchors not found")
t = t[:a] + V8_JS + t[b:]

# ---- aside spec ----
ASIDE8 = r'''  <aside class="spec">
    <h3>دور هشتم: گرهها، اولین و اصلیترین کار</h3>
    <ul>
      <li><b>ابزار تازه:</b> <code>tools/extract_mimo_nodes_v8.py</code> → <code>DESIGN/NODE_CODE_GEOMETRY.json</code> + <code>CATALOGS/MIMO_PATH_NODES.csv</code> (<span id="nodeStats">شمارش…</span>).</li>
      <li><b>هندسه دقیق از کد:</b> مربع <code>92dp</code> / شعاع <code>26dp</code> / لبهٔ سهبعدی <code>8dp</code> (<code>button_primary_highlight #FF6E3EC8</code>) · گرادیان <code>progress_chapter_primary #FF8D60E2 → button_primary #FF7E4BDE</code> · شبکهٔ نقطهای <code>26dp</code> · اتور <code>stroke 10dp</code> با <b>گوشههای گرد Q به شعاع ۳۲dp</b> (راست/پایین/چپ/پایین)، نه منحنی بزیه.</li>
      <li><b>حالتها:</b> انجامشده = <code>ic_check_white</code> سفید · فعلی = کارت سفید + حلقهٔ دوتایی بنفش (۳dp border + ۷dp فاصله + ۳dp حلقه) + <b>حلقهٔ پیشرفت ½</b> (<code>glance_circular_progress_indicator.xml</code>) · نسخهٔ پلی = <code>ic_play #FF252746</code> · رعدوبرق فعال = <code>ic_flash</code> سرمهای روی بنفش · رعدوبرق اختیاری = <code>ic_bolt</code> سفید روی <code>card_disabled</code>.</li>
      <li><b>شناور:</b> دایرهٔ کتاب/واژهنامه با A (<code>ic_file.xml</code> + <code>bookmark_no_fill.xml</code>) · سربرگ ۳ چیپ <code>PathToolbarKt$RowWithKeys</code> · کارت <code>ViewsKt$OverviewEntryPointHeader</code>.</li>
      <li><b>چک بصری فقط:</b> <code>mimo-01</code> (تیک/پلی/دو بولت/کتاب)، <code>mimo-02</code> (حلقهٔ دوتایی + ½)، <code>mimo-10</code> (چهار تیک + بولت فعال + اتور گردگوشه). کد ملاک است؛ ۰ رنگ/فونت/شعاع/آیکون تازه.</li>
      <li><b>شواهد DEX:</b> <code>PathMapScreenKt</code>، <code>PathMapViewModel$onTutorialClick</code>، <code>GetPathMapState/Dialogs</code>، <code>PathToolbarButtonType</code>، <code>PracticeOptionalIntroKt</code>، <code>TutorialSpotlightKt</code>، <code>ModalData$SmartPractice*</code> — ۹۲ کلاس PathMap. شِیپها: <code>rounded_background_primary</code>، <code>progress_bar_chapter</code>، <code>ic_square_rounded</code>، <code>bg_circular</code>، <code>shadow_bottom</code>.</li>
    </ul>
    <h3>نمایش حالت گرهٔ فعلی (فقط پنل بازبینی)</h3>
    <ul>
      <li><button class="btn" id="nodeHalfBtn">حلقهٔ ½ (mimo-02)</button> <button class="btn" id="nodePlayBtn">پلی (mimo-01)</button> — دکمهها بیرون از گوشیاند، داخل UI محصول نیستند.</li>
      <li><b>هیچ گرهٔ قفلی</b> در یادگیری / داخل مبحث / تمرین مبحث وجود ندارد؛ تنها قفل مجاز، همان <b>«آزمون نهایی / دو هفتگی»</b> موجود در بخش ۶ هاب آزمونهاست و دستنخورده ماند.</li>
    </ul>
    <h3>حذفشدهها (دستور صریح دور هشتم)</h3>
    <ul>
      <li><b>روتین روزانه</b> و <b>کل ایدهٔ امتیازدهی Habitica</b>: تب، صفحه، JSON، کاتالوگها و سندش بهطور کامل حذف شد. پنج تب میمو برگشت؛ <code>MAX</code> ممنوع.</li>
      <li><b>دیکته / Dictate</b> از خط پایین دستیار هوشمند حذف شد؛ «آموزش / TEACH» و «تمرین / PRACTICE» همان یک خط با <code>gemini-flash-lite-latest</code> و <code>medium</code> ماندند.</li>
      <li>همهٔ یادداشتهای توضیحی داخل UI (سیاست، ایدهٔ جزیی <b>EPM</b>، توضیح تایمر، چیپهای کد، برچسبهای <code>.lh</code>، <code>codechip</code> و تولتیپها) پاک شدند؛ شواهد بهصورت <code>data-code</code> / <code>data-lh</code> نامرئی و در کاتالوگها نگهداری میشوند.</li>
      <li>توضیحات <b>قالب فیلد / لیبل ۷ بخش</b> هاب آزمونها و <b>پاسخنامهٔ تشریحی</b> بنا به دستور شما <b>نگه داشته شدند</b>.</li>
    </ul>
    <h3>ظاهر آزمونها: میموتر، بدون تغییر معماری</h3>
    <ul>
      <li>جای ◇ / ⏱ / ✓ / 🔒 / → رفتند <b>وکتورهای واقعی میمو</b>: <code>ic_trophy</code>، <code>ic_clock_black_24dp</code>، <code>ic_task_completed</code>، <code>ic_lock_alt_02</code>، <code>ic_file</code>، <code>ic_target</code>، <code>ic_sparks_alt</code>، <code>ic_arrow_back_24</code>، <code>ic_help</code>.</li>
      <li>رنگها/شعاعها/تایپوگرافی از ARSC: <code>card</code>، <code>card-pressed</code>، <code>primary</code>، <code>line_secondary</code>، شعاع <code>12/16/20dp</code>، <code>toolbar 56dp</code>، <code>TextH2/TextLabel1</code>. چیپها، کارتهای <code>nodek</code>، <code>cat-meta</code>، گزینهها و نوارها فقط <b>پوسته</b> عوض کردند.</li>
      <li><b>تغییری در چارچوب</b> ایجاد نشد: ۷ بخش لیبلدار، تایمر فقط داخل آزمون (کلیک ← عدد ← شروع ← معکوس، توقف/ادامه، ثبت خودکار صفر)، جامع ۲۷۰ دقیقهٔ ثابت، «پاسخبرگ» ≠ «پاسخنامه»، بازشدن خودکار کلید در زمان خالص، دو دکمهٔ تمیز قبل/بعد و تکدکمهٔ «توضیح با هوش مصنوعی».</li>
    </ul>
    <h3>حفظشده</h3>
    <ul>
      <li>گره رعدوبرق ← <code>data-screen=section-practice</code> (تمرین مبحث تا همان فصل، <b>جدا از هاب آزمون</b>) · لیدربورد بدون Promotion Zone · چت مینیمال + تاریخچه + «اضافه کردن فایل» / «زنجیره گفت و گو» · مشاوره <code>PARKED</code> · بدون Pro/پرداخت/MAX · حالت شب + RTL/فارسی · ۱۴ اسکرینشات فقط چک بصری.</li>
    </ul>
    <h3>توکنهای کد</h3>
    <ul>
      <li><b>bg</b> <code>#F6F7FB</code> / شب <code>#252746</code> · <b>button</b> <code>#7E4BDE</code> · <b>progress</b> <code>#8D60E2</code></li>
      <li><b>TextH1</b> 24sp · <b>TextP2</b> 16sp · <b>toolbar</b> 56dp · <b>card radius</b> 12dp</li>
    </ul>
    <h3>وضعیت</h3>
    <ul><li><b>DESIGN v8 · REVIEW</b> — منتظر تأیید نهایی</li><li>بعد از تأیید ← مرحلهٔ پیادهمسازی</li><li>هیچ کد محصولی نوشته نشده</li></ul>
  </aside>'''
t = rx1(t, r'  <aside class="spec">.*?</aside>', ASIDE8, "aside8")

t = rx1(t, r'<footer class="foot-note">.*?</footer>',
        r'''<footer class="foot-note">
⚠️ این <b>طرح دور هشتم v8</b> است، نه محصول. گرههای مسیر یادگیری مستقیماً از <code>NODE_CODE_GEOMETRY.json</code> (جداول ARSC، <code>pathData</code>، شِیپها، <code>test-tracks.json</code> و ۹۲ کلاس PathMap DEX) رندر شدند؛ ۱۴ اسکرینشات فقط <b>چک بصری</b>اند. روتین روزانه و ایدهٔ امتیازدهیاش بهکل حذف شد، دیکته حذف شد، یادداشتهای توضیحی داخل UI پاک شدند و ظاهر آزمونها فقط با آیکون/رنگ میمو نزدیکتر شد. نسخههای <b>DESIGN v6</b> و <b>DESIGN v7</b> بایگانی حسابرسیاند. «وارد کردن کلید API» فقط یک یادداشت است و هیچ صفحۀ تنظیماتی طراحی نشده. هیچ کد محصولی نوشته نشده است.
</footer>''', "footer8")

# ---- inject payloads ----
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
print(json.dumps({
    "output": str(OUT), "bytes": OUT.stat().st_size,
    "template": str(TPL_OUT), "template_bytes": TPL_OUT.stat().st_size,
    "svg_vectors": len(merged), "views": html.count("<button data-go="),
    "tabs": html.count('data-tab="'), "nodes": len(NDG["nodes"]),
    "locked_nodes": html.count('class="node locked') + html.count('data-locked='),
    "dictate": "Dictate" in html, "routine": 'data-screen="routine"' in html,
    "method": GEO["method"],
}, ensure_ascii=False, indent=1))
