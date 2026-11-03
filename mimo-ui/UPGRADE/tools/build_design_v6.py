#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate DESIGN/index.html (v6) from code-extracted Mimo 9.35 geometry.

Pipeline (all code-first, no screenshot tracing):
  tools/extract_mimo_geometry.py      -> DESIGN/CODE_GEOMETRY.json
  tools/extract_mimo_learn_v6.py      -> DESIGN/LEARN_CODE_GEOMETRY.json
  tools/build_design_v6.py            -> DESIGN/index.html + tools/design_v6_template.html

v6 changes (user design review, 2026-11-03):
  * Learn / Path Map rebuilt cleanly: 3 toolbar pills (coins/keys/streak),
    a real overview-entry header card, dotted zigzag node path, no annotation
    chips, no stray progress ring. PathToolbarKt$RowWithKeys + ViewsKt$OverviewEntryPointHeader.
  * NEW Select Path screen (the "three lines" icon next to the path name):
    Career Paths cards + Courses rows, from track_switcher_* strings,
    ic_badge_* / ic_code_lang_* vectors, profile_certificate_view.xml ring.
  * NEW Path Overview screen (career path header + Professional Certificate
    card + numbered sections from test-tracks.json sections[]).
  * NEW Section detail screen (chapters from sections[].tutorialIds,
    section_details_* / lesson_* / path_section_coming_soon strings).
  * NEW Unfinished track modal (certificates_unfinished_track_dialog_* strings,
    ic_mimo_mascot vector).
  * Onboarding screen removed from the design (page 7 no longer needed).
  * 5-tab navigation, exam hub, timer, answer sheets, AI chat unchanged.
"""
from __future__ import annotations
import json, re, sys
from pathlib import Path

UP = Path(sys.argv[1] if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]).resolve()
GEO = json.loads((UP / "DESIGN" / "CODE_GEOMETRY.json").read_text(encoding="utf-8"))
LRN = json.loads((UP / "DESIGN" / "LEARN_CODE_GEOMETRY.json").read_text(encoding="utf-8"))
BASE = (UP / "tools" / "design_v5_template.html").read_text(encoding="utf-8")
OUT = UP / "DESIGN" / "index.html"
TPL_OUT = UP / "tools" / "design_v6_template.html"

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
    """Assert exactly one replacement."""
    n = text.count(old)
    if n != 1:
        raise SystemExit("template anchor %s matched %d times" % (label, n))
    return text.replace(old, new, 1)


def rx1(text, pattern, new, label, flags=re.S):
    r = re.compile(pattern, flags)
    ms = list(r.finditer(text))
    if len(ms) != 1:
        raise SystemExit("template regex %s matched %d times" % (label, len(ms)))
    return text[:ms[0].start()] + new + text[ms[0].end():]


# --------------------------------------------------------------------------
# 1. Merge the newly extracted Learn vectors into GEO so icon() can draw them
#    with the exact android:pathData from res/drawable/*.xml.
# --------------------------------------------------------------------------
merged = dict(GEO["vectors"])
for name, v in LRN["vectors"].items():
    if name in merged:
        continue
    merged[name] = {
        "source": v["source"],
        "viewport": [v["viewportWidth"], v["viewportHeight"]],
        "size_dp": [v["widthDp"], v["heightDp"]],
        "paths": [{"d": p["d"], "fill": p["fill"], "alpha": None,
                   "fillType": p["fillType"]} for p in v["paths"]],
        "sha_bytes": None,
    }

payload = {
    "method": GEO["method"], "apk_sha256": GEO["apk_sha256"],
    "sources": GEO["sources"], "vectors": merged,
    "colors": GEO["colors"], "dimens": GEO["dimens"], "styles": GEO["styles"],
    "strings": GEO["strings"], "layouts": GEO["layouts"],
    "compose_path_class_count": GEO["compose_path_class_count"],
}

learn_payload = {
    "method": LRN["method"],
    "apk": LRN["apk"],
    "strings": LRN["strings"],
    "contentModel": LRN["contentModel"],
    "counts": {
        "vectors": len(LRN["vectors"]),
        "layouts": len(LRN["layouts"]),
        "nav_graphs": len(LRN["navigation"]),
        "strings": sum(len(v) for v in LRN["strings"].values()),
        "colors": len(LRN["tokens"]["colors"]),
        "dimens": len(LRN["tokens"]["dimens"]),
        "styles": len(LRN["tokens"]["styleNames"]),
        "catalog_rows": sum(1 for _ in open(UP / "CATALOGS" / "MIMO_LEARN_SUBSCREENS.csv", encoding="utf-8")) - 1,
        "dex_classes": sum(v["count"] for k, v in LRN["dex"].items() if k != "literals"),
    },
    "layoutNames": sorted(LRN["layouts"]),
    "vectorNames": sorted(LRN["vectors"]),
    "subScreens": ["learn", "select-path", "path-overview", "section-detail", "unfinished-track"],
}

# --------------------------------------------------------------------------
# 2. Template transformations
# --------------------------------------------------------------------------
t = BASE

t = sub1(t, "<title>طرح رابط کاربری v5 — بازآفرینی ۱۰۰٪ میمو از روی کد (Design Review)</title>",
         "<title>طرح رابط کاربری v6 — بازآفرینی ۱۰۰٪ میمو از روی کد (Design Review)</title>", "title")

t = sub1(t, "<h1>طرح رابط کاربری — نسخهٔ نهایی <span class=\"ver\">DESIGN v5 · FINAL</span></h1>",
         "<h1>طرح رابط کاربری — دور ششم <span class=\"ver\">DESIGN v6 · REVIEW</span></h1>", "h1")

t = rx1(t, r"<p>بازآفرینی ۱۰۰٪ بخشهای اصلی میمو.*?</p>",
        "<p>بازآفرینی ۱۰۰٪ بخشهای اصلی میمو <b>از روی کد/مهندسی معکوس</b> · "
        "<b>دور ششم:</b> صفحهٔ یادگیری تمیز بازسازی شد (۳ چیپ سکه/کلید/استریک + کارت نمای مسیر + مسیر مارپیچ)، "
        "<b>سهخط کنار نام مسیر → «انتخاب مسیر»</b> (مسیرهای شغلی + تکدرسها)، "
        "<b>کارت مسیر → «نمای مسیر»</b> (گواهی حرفهای + فصلهای شمارهدار)، "
        "<b>کلیک روی مبحث → «داخل مبحث»</b> (فصلها و درسها از <code>test-tracks.json</code>) و دیالوگ «مسیر ناتمام». "
        "همه از <code>ARSC</code>، <code>res/drawable/*.xml</code>، <code>res/layout/*.xml</code>، DEX و مدل محتوای داخل APK. "
        "صفحهٔ ورود فعلاً حذف شد. اسکرینشاتها فقط چک بصری.</p>", "header-p")

t = sub1(t, '<a class="btn" href="CODE_GEOMETRY.json">🧬 هندسهٔ استخراجشده از کد</a>',
         '<a class="btn" href="CODE_GEOMETRY.json">🧬 هندسهٔ کد</a>\n'
         '    <a class="btn" href="LEARN_CODE_GEOMETRY.json">📚 شواهد زیرصفحات یادگیری</a>', "header-links")

# ---- switcher: remove onboarding, add 3 new Learn sub-screens (13 views) ----
switcher_old = re.search(r'<div class="switcher" id="switcher">.*?</div>', t, re.S).group(0)
switcher_new = '''<div class="switcher" id="switcher">
      <button data-go="learn" class="on">۱ · یادگیری (بازسازی تمیز)</button>
      <button data-go="select-path">۲ · انتخاب مسیر / درسها</button>
      <button data-go="path-overview">۳ · نمای مسیر + گواهی</button>
      <button data-go="section-detail">۴ · داخل مبحث (فصلها)</button>
      <button data-go="chapter">۵ · کارت شروع فصل</button>
      <button data-go="lesson">۶ · صفحهٔ درس</button>
      <button data-go="leaderboard">۷ · لیدربورد + اطلاعات من</button>
      <button data-go="user-profile">۸ · پروفایل کاربر</button>
      <button data-go="profile">۹ · پروفایل</button>
      <button data-go="exam-hub">۱۰ · هاب آزمونها</button>
      <button data-go="exam-run">۱۱ · اجرای آزمون</button>
      <button data-go="exam-result">۱۲ · صفحهٔ آخر آزمون</button>
      <button data-go="ai">۱۳ · چت AI</button>
    </div>'''
t = sub1(t, switcher_old, switcher_new, "switcher")

# ---- CSS for the new Learn sub-screens (appended last -> wins over v5 rules) ----
CSS6 = r'''
/* ============ v6 · Learn sub-screens, tokens from ARSC ============ */
.l6 .pill{flex:1;background:var(--card-pressed);border-radius:16px;height:42px;display:flex;align-items:center;justify-content:center;gap:8px;font:700 17px/1 system-ui,sans-serif;color:var(--text)}
.l6 .pill b{font-weight:700}
.l6 .pill .inf{margin-left:-5px;color:var(--text)}
.coursebar.l6{height:50px;margin:2px 16px 0;display:flex;align-items:center;justify-content:center;position:relative;border-bottom:0}
.coursebar.l6 b{font:700 18px/1.2 system-ui,sans-serif;letter-spacing:.2px}
.coursebar.l6 .lst{position:absolute;left:2px;top:8px;width:36px;height:36px;border:1px solid var(--line2);background:var(--card);border-radius:13px;display:flex;align-items:center;justify-content:center;color:var(--icon);cursor:pointer}
.coursebar.l6 .lst:hover{border-color:var(--primary)}
.overview-card{display:block;width:calc(100% - 32px);margin:6px 16px 0;padding:14px 18px 16px;text-align:left;background:var(--card);border:2px solid var(--line2);border-radius:20px;cursor:pointer}
.overview-card:hover{border-color:var(--primary)}
.overview-card .oc-kicker{display:block;font:600 14px/1.3 system-ui,sans-serif;color:var(--text-weak)}
.overview-card .oc-title{display:block;margin:5px 0 12px;font:700 21px/1.2 system-ui,sans-serif;color:var(--text);letter-spacing:.2px}
.overview-card .oc-bar{display:block;height:8px;border-radius:999px;background:var(--progress-bg);overflow:hidden}
.overview-card .oc-bar i{display:block;height:100%;background:var(--progress);border-radius:999px}
.pathwrap.l6{height:452px;margin-top:8px;background:radial-gradient(circle,var(--line2) 1.6px,transparent 1.7px) 0 0/26px 26px;background-color:var(--bg)}
.pathwrap.l6 .node{width:92px;height:92px;border-radius:26px}
.pathwrap.l6 .node.done{background:linear-gradient(160deg,var(--purple-light),var(--primary));box-shadow:0 8px 0 var(--primary-hi),0 11px 16px rgba(37,39,70,.18)}
.pathwrap.l6 .node.flash{background:var(--purple-light);opacity:1;box-shadow:0 8px 0 var(--primary-hi),0 11px 16px rgba(37,39,70,.18)}
.pathwrap.l6 .node.flash .ic{color:var(--primary)}
.l6n1{left:calc(50% - 46px);top:22px}
.l6n2{left:calc(80% - 46px);top:128px}
.l6n3{left:calc(50% - 46px);top:234px}
.l6n4{left:calc(20% - 46px);top:340px}
.l6n5{left:calc(50% - 46px);top:340px}
/* ---- Select Path ---- */
.sp-top,.po-top,.sd-top{height:56px;flex-shrink:0;display:flex;align-items:center;justify-content:center;position:relative;border-bottom:1px solid var(--line)}
.sp-top b,.sd-top b{font:700 16px/1 system-ui,sans-serif;color:var(--text-weak)}
.sp-top .x,.po-top .x,.sd-top .x{position:absolute;left:14px;top:14px;width:30px;height:30px;display:flex;align-items:center;justify-content:center;color:var(--icon);cursor:pointer;background:transparent;border:0}
.sp-body{padding:18px 16px 24px}
.sp-body h3{margin:0 0 14px;font:700 24px/1.2 system-ui,sans-serif;letter-spacing:.2px}
.sp-body h3.sub{margin-top:26px}
.career-card{display:block;width:100%;text-align:left;margin:0 0 16px;padding:16px 18px 18px;background:var(--card);border:2px solid var(--line2);border-radius:22px;cursor:pointer;box-shadow:0 4px 0 var(--card-pressed)}
.career-card.sel{border:3px solid var(--primary);box-shadow:0 0 0 6px var(--progress-weak),0 4px 0 var(--card-pressed)}
.career-card .badges{display:flex;gap:5px;align-items:center;height:26px;margin-bottom:10px}
.career-card .badges span{width:24px;height:24px;display:flex;align-items:center;justify-content:center}
.career-card h4{margin:0 0 14px;font:700 22px/1.2 system-ui,sans-serif}
.career-card .cr{display:flex;justify-content:space-between;font:700 12px/1 system-ui,sans-serif;letter-spacing:1.2px;color:var(--text-weak);text-transform:uppercase}
.career-card .cbar{height:8px;border-radius:999px;background:var(--progress-bg);margin-top:9px;overflow:hidden}
.career-card .cbar i{display:block;height:100%;background:var(--progress);border-radius:999px}
.course-row{display:flex;align-items:center;gap:14px;width:100%;text-align:left;margin:0 0 12px;padding:12px 14px;background:var(--card);border:2px solid var(--line2);border-radius:20px;cursor:pointer}
.course-row .cbadge{width:38px;height:38px;flex-shrink:0;display:flex;align-items:center;justify-content:center}
.course-row .ctxt{flex:1;min-width:0}
.course-row .ctxt b{display:block;font:700 21px/1.2 system-ui,sans-serif}
.course-row .ctxt small{display:block;color:var(--text-weak);font:400 14px/1.4 system-ui,sans-serif;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.cring{width:56px;height:56px;flex-shrink:0;border-radius:50%;position:relative;display:flex;align-items:center;justify-content:center;font:700 13px/1 system-ui,sans-serif;color:var(--text);background:var(--progress-bg)}
.cring:before{content:"";position:absolute;inset:9px;border-radius:50%;background:var(--card)}
.cring b{position:relative;z-index:1}
.cring.part{background:conic-gradient(var(--progress) 0 43%,var(--progress-bg) 43% 100%)}
/* ---- Path Overview ---- */
.po-head{padding:18px 18px 8px;position:relative}
.po-head .kick{display:block;font:400 16px/1.3 system-ui,sans-serif;color:var(--text-weak)}
.po-head h1{margin:4px 0 0;font:700 26px/1.2 system-ui,sans-serif;letter-spacing:.2px;max-width:72%}
.po-head .sw{position:absolute;right:18px;top:30px;width:48px;height:48px;border:1px solid var(--line2);border-radius:14px;background:var(--card);display:flex;align-items:center;justify-content:center;color:var(--primary);cursor:pointer}
.cert-card{margin:12px 18px 4px;padding:14px 16px;background:var(--card);border:1px solid var(--line2);border-radius:16px;display:flex;gap:14px;align-items:center;cursor:pointer}
.cert-card .cb{width:48px;height:60px;flex-shrink:0;display:flex;align-items:center;justify-content:center}
.cert-card .cc{flex:1;min-width:0}
.cert-card .cc b{display:block;font:700 19px/1.25 system-ui,sans-serif}
.cert-card .cc .cbar{height:8px;border-radius:999px;background:var(--progress-bg);margin:10px 0 7px;overflow:hidden}
.cert-card .cc .cbar i{display:block;height:100%;width:22%;background:var(--progress);border-radius:999px}
.cert-card .cc .cm{display:flex;justify-content:space-between;font:400 14px/1.3 system-ui,sans-serif;color:var(--text-weak)}
.po-secs{position:relative;padding:10px 18px 26px}
.po-secs:before{content:"";position:absolute;left:46px;top:0;bottom:46px;width:6px;border-radius:999px;background:var(--progress);opacity:.85}
.po-sec{position:relative;display:flex;gap:16px;align-items:flex-start;width:100%;text-align:left;padding:14px 0;background:transparent;border:0;cursor:pointer;z-index:1}
.po-sec .ring{width:56px;height:56px;flex-shrink:0;border-radius:50%;background:var(--card);border:4px solid var(--progress-bg);display:flex;align-items:center;justify-content:center;font:700 13px/1 system-ui,sans-serif}
.po-sec.done .ring{background:var(--primary);border-color:var(--primary);color:#fff}
.po-sec .ring.part{border-color:var(--progress-bg);background:conic-gradient(var(--progress) 0 43%,var(--card) 43% 100%)}
.po-sec .ring.part:before{content:"";position:absolute;inset:5px;border-radius:50%;background:var(--card)}
.po-sec .ring.part b{position:relative;z-index:1}
.po-sec .st{flex:1;padding-top:3px}
.po-sec .st b{display:block;font:700 20px/1.25 system-ui,sans-serif}
.po-sec .st p{margin:4px 0 0;font:400 15px/1.45 system-ui,sans-serif;color:var(--text-weak)}
.po-sec.active{background:var(--card);border:1px solid var(--line2);border-radius:18px;padding:14px 12px;margin:6px -10px;box-shadow:0 2px 8px rgba(37,39,70,.06)}
.po-sec .proj{display:inline-block;margin-top:6px;font:700 11px/1 system-ui,sans-serif;letter-spacing:1px;text-transform:uppercase;color:var(--primary)}
.po-sec .soon{display:inline-block;margin-top:6px;font:700 11px/1 system-ui,sans-serif;letter-spacing:1px;text-transform:uppercase;color:var(--text-weak)}
/* ---- Section detail ---- */
.sd-hero{padding:18px 18px 12px}
.sd-hero .kick{display:block;font:400 15px/1.3 system-ui,sans-serif;color:var(--text-weak)}
.sd-hero h2{margin:5px 0 6px;font:700 24px/1.2 system-ui,sans-serif}
.sd-hero p{margin:0 0 14px;font:400 15px/1.5 system-ui,sans-serif;color:var(--text-weak)}
.sd-hero .cbar{height:8px;border-radius:999px;background:var(--progress-bg);overflow:hidden}
.sd-hero .cbar i{display:block;height:100%;width:43%;background:var(--progress);border-radius:999px}
.sd-list{padding:0 18px 18px}
.sd-row{display:flex;align-items:center;gap:12px;width:100%;text-align:left;margin:0 0 10px;padding:11px 13px;background:var(--card);border:1px solid var(--line2);border-radius:16px;cursor:pointer}
.sd-row .sr{width:34px;height:34px;flex-shrink:0;border-radius:50%;background:var(--card-pressed);display:flex;align-items:center;justify-content:center;font:700 13px/1 system-ui,sans-serif;color:var(--text-weak)}
.sd-row.done .sr{background:var(--primary);color:#fff}
.sd-row.cur .sr{background:var(--progress-weak);color:var(--primary)}
.sd-row .stx{flex:1}
.sd-row .stx b{display:block;font:700 16px/1.3 system-ui,sans-serif}
.sd-row .stx small{display:block;color:var(--text-weak);font:400 12px/1.4 system-ui,sans-serif}
.sd-row .si{color:var(--text-weak);display:flex}
.sd-row.locked{opacity:.55}
.sd-cta{display:block;width:calc(100% - 36px);margin:0 18px 12px;height:50px;border:0;border-radius:999px;background:var(--primary);color:#fff;font:700 14px/1 system-ui,sans-serif;letter-spacing:.6px;text-transform:uppercase;cursor:pointer}
.sd-link{display:block;width:calc(100% - 36px);margin:0 18px 18px;padding:9px;border:1px solid var(--line2);border-radius:999px;background:var(--card);color:var(--primary);font:700 12px/1 system-ui,sans-serif;cursor:pointer}
.sd-note{margin:0 18px 22px;font:400 12px/1.6 system-ui,sans-serif;color:var(--text-weak)}
/* ---- Unfinished track modal ---- */
.ut-card{text-align:center;padding:22px 22px 24px}
.ut-card .utx{position:absolute;right:18px;top:18px;width:26px;height:26px;display:flex;align-items:center;justify-content:center;color:var(--text-weak);cursor:pointer}
.ut-card .ut-art{height:112px;display:flex;align-items:center;justify-content:center;color:var(--primary)}
.ut-card h2{margin:6px 0 12px;font:700 25px/1.25 system-ui,sans-serif}
.ut-card p{margin:0 0 20px;font:400 17px/1.5 system-ui,sans-serif;color:var(--text)}
.ut-card .utok{width:100%;height:54px;border:0;border-radius:16px;background:var(--primary);color:#fff;font:700 17px/1 system-ui,sans-serif;cursor:pointer}
.codechip2{display:inline-block;background:var(--code-bg);border-radius:6px;padding:2px 7px;font:400 11px/1.5 ui-monospace,"Courier New",monospace;direction:ltr;color:var(--text-weak)}
'''
t = sub1(t, "</style>", CSS6 + "\n</style>", "css6")

# ---- Learn screen rebuilt cleanly ----
learn_old = re.search(r'      <!-- ============ 1\. LEARN.*?</section>', t, re.S).group(0)
S = LRN["strings"]
cm = LRN["contentModel"]
sec3 = cm["sections"][2]
learn_new = '''      <!-- ============ 1. LEARN / PATH MAP = rebuilt cleanly from code ============ -->
      <section class="screen mimo on" data-screen="learn">
        <div class="mimo-hdr l6">
          <div class="pill"><span data-icon="ic_coin" data-size="26"></span><b>1,272</b></div>
          <div class="pill"><span data-icon="ic_key" data-size="24"></span><span class="inf" data-icon="ic_infinity" data-size="20" data-mono="1"></span></div>
          <div class="pill"><span data-icon="ic_streak_active" data-size="26"></span><b>0</b></div>
        </div>
        <div class="coursebar l6">
          <button class="lst" id="pathSwitchBtn" data-nav="select-path" title="ic_list_bulleted → select_path / track_switcher_title"><span data-icon="ic_list_bulleted" data-size="24" data-mono="1"></span></button>
          <b data-fa="کنکور تجربی">Back-End Developer</b>
        </div>
        <button class="overview-card" id="overviewEntry" data-nav="path-overview" title="ViewsKt$OverviewEntryPointHeader → path_see_course_overview">
          <span class="oc-kicker" data-fa="مسیر شغلی">Career path</span>
          <span class="oc-title" data-fa="۳. سلول و بافت">3. Arrays &amp; Functions</span>
          <span class="oc-bar"><i style="width:43%"></i></span>
        </button>
        <div class="pathwrap l6">
          <svg class="connector" viewBox="0 0 392 452" preserveAspectRatio="none">
            <path d="M196 68 C196 104 314 100 314 174 C314 226 196 222 196 280 C196 322 78 320 78 386 C78 404 130 386 196 386" fill="none" stroke="var(--progress)" stroke-width="10" stroke-linecap="round" stroke-linejoin="round" opacity=".55"/>
          </svg>
          <div class="node done l6n1" data-icon="ic_check_white" data-size="44" data-mono="1" data-nav="section-detail" title="completed chapter"></div>
          <div class="node done l6n2" data-icon="ic_check_white" data-size="44" data-mono="1" data-nav="section-detail"></div>
          <div class="node done l6n3" data-icon="ic_check_white" data-size="44" data-mono="1" data-nav="section-detail"></div>
          <div class="node done l6n4" data-icon="ic_check_white" data-size="44" data-mono="1" data-nav="section-detail"></div>
          <div class="node flash l6n5" id="curNode" data-icon="ic_flash" data-size="42" data-mono="1" title="current chapter — tap to open Section detail"></div>
        </div>
      </section>

      <!-- ============ 2. SELECT PATH = the three-lines icon ============ -->
      <section class="screen mimo" data-screen="select-path">
        <div class="sp-top"><button class="x" data-nav="learn"><span data-icon="ic_close" data-size="24" data-mono="1"></span></button><b data-fa="انتخاب مسیر">Select Path</b></div>
        <div class="sp-body">
          <h3 id="careerHeading" data-fa="مسیرهای شغلی">Career Paths</h3>
          <div id="careerCards"></div>
          <h3 class="sub" id="courseHeading" data-fa="درسها">Courses</h3>
          <div id="courseRows"></div>
          <p class="note" style="margin-top:18px">همهٔ لیبلها از <span class="codechip2">track_switcher_*</span> / <span class="codechip2">courses</span> / <span class="codechip2">section</span> و وکتورها از <span class="codechip2">ic_badge_*</span>. حلقهها از <span class="codechip2">profile_certificate_view.xml</span> (اندازهٔ ۵۶dp، رنگ <span class="codechip2">progress_primary</span>). <span class="codechip2">track_switcher_title = Coding Path</span> · <span class="codechip2">track_switcher_early_access_label = Early access</span></p>
        </div>
      </section>

      <!-- ============ 3. PATH OVERVIEW = certificate + numbered sections ============ -->
      <section class="screen mimo" data-screen="path-overview">
        <div class="po-top"><button class="x" data-nav="learn"><span data-icon="ic_close" data-size="24" data-mono="1"></span></button></div>
        <div class="po-head">
          <span class="kick" data-fa="مسیر شغلی">Career path</span>
          <h1 data-fa="کنکور تجربی">Back-End Developer</h1>
          <button class="sw" id="overviewSwitch" data-nav="select-path" title="ic_switch → select_path"><span data-icon="ic_switch" data-size="28"></span></button>
        </div>
        <div class="cert-card" id="certCard" data-modal="unfinishedModal" title="certificates_unfinished_track_dialog_*">
          <span class="cb" data-icon="ic_badge_backend_professional" data-size="48"></span>
          <div class="cc">
            <b data-fa="گواهی حرفهای">Professional Certificate</b>
            <div class="cbar"><i></i></div>
            <div class="cm"><span data-fa="۲۲٪ تکمیل">22% Complete</span><span>2/9</span></div>
          </div>
        </div>
        <div class="po-secs" id="sectionRows"></div>
        <p class="note" style="margin:0 18px 22px">عنوان فصلها با <span class="codechip2">path_overview_section_ordinal = %d. %s</span> و نام/توضیح/تعداد درسها از <span class="codechip2">test-tracks.json :: tracks[].sections[]</span>. <span class="codechip2">path_overview_section_project_label = Section Project</span> · <span class="codechip2">path_section_coming_soon = Coming soon</span> · <span class="codechip2">alert_msg_section_setion_locked</span></p>
      </section>

      <!-- ============ 4. SECTION DETAIL = inside a topic ============ -->
      <section class="screen mimo" data-screen="section-detail">
        <div class="sd-top"><button class="x" data-nav="path-overview"><span data-icon="ic_arrow_back_24" data-size="24" data-mono="1"></span></button><b data-fa="مبحث">Section</b></div>
        <div class="sd-hero">
          <span class="kick" data-fa="فصل سوم">Section 3</span>
          <h2 id="sdTitle" data-fa="سلول و بافت">Arrays &amp; Functions</h2>
          <p id="sdDesc">Use arrays &amp; functions to build sophisticated programs</p>
          <div class="cbar"><i></i></div>
        </div>
        <div class="sd-list" id="lessonRows"></div>
        <button class="sd-cta" id="sdContinue" data-nav="chapter" data-fa="ادامه">Continue</button>
        <button class="sd-link" id="sdOverview" data-nav="path-overview" data-fa="نمای دوره">See course overview</button>
        <p class="sd-note" id="sdNote">فهرست درسها از <span class="codechip2">sections[2].tutorialIds</span> (۱۶ شناسهٔ واقعی داخل APK). لیبلها: <span class="codechip2">lesson_continue</span> · <span class="codechip2">lesson_skip</span> · <span class="codechip2">lesson_submit</span> · <span class="codechip2">path_overview_section_project_label</span> · <span class="codechip2">path_section_coming_soon_title</span> · <span class="codechip2">section_details_smart_practice_*</span></p>
      </section>'''
t = sub1(t, learn_old, learn_new, "learn-rebuild")

# ---- remove onboarding screen entirely (page 7 no longer needed) ----
t = rx1(t, r'      <!-- ============ 7\. ONBOARDING ============ -->\s*<section class="screen mimo" data-screen="onboarding">.*?</section>\s*',
        "", "onboarding-remove")

# ---- add Unfinished track modal after chapter modal ----
t = sub1(t, '<div class="modal" id="chapterModal">',
         '''<div class="modal" id="unfinishedModal"><div class="modal-card ut-card">
        <span class="utx" data-modal-close="unfinishedModal"><span data-icon="ic_close" data-size="22" data-mono="1"></span></span>
        <div class="ut-art"><span data-icon="ic_mimo_mascot" data-size="104"></span></div>
        <h2 data-fa="مسیر ناتمام">Unfinished track</h2>
        <p data-fa="مسیر را تمام کنید تا گواهی شخصیشدهاقتان را بگیرید">Finish the track and receive your personalised certificate</p>
        <button class="utok" data-modal-close="unfinishedModal" data-fa="باشه">Ok</button>
      </div></div>
      <div class="modal" id="chapterModal">''', "unfinished-modal")

# ---- navigation map: new screens belong to Learn tab, onboarding removed ----
t = sub1(t,
         'var tabMap={learn:"Learn",chapter:"Learn",lesson:"Learn",leaderboard:"Leaderboard","user-profile":"Leaderboard",profile:"Profile",onboarding:"Learn","exam-hub":"Practice","exam-run":"Practice","exam-result":"Practice",ai:"AI"};',
         'var tabMap={learn:"Learn",chapter:"Learn",lesson:"Learn","select-path":"Learn","path-overview":"Learn","section-detail":"Learn",leaderboard:"Leaderboard","user-profile":"Leaderboard",profile:"Profile","exam-hub":"Practice","exam-run":"Practice","exam-result":"Practice",ai:"AI"};',
         "tabmap")

t = sub1(t, 'if(name!=="chapter")q("#chapterModal").classList.remove("on");',
         'if(name!=="chapter"){qa(".modal").forEach(function(m){m.classList.remove("on")})}', "go-modals")

t = sub1(t, "  function go(name){\n", "  function go(name){\n    var prev=q(\".screen.on\");var prevName=prev?prev.dataset.screen:\"learn\";\n", "go-prev")

t = sub1(t, 'if(name==="chapter"){go("learn");q("#chapterModal").classList.add("on");qa("#switcher button").forEach(function(b){b.classList.toggle("on",b.dataset.go==="chapter")});return}',
         'if(name==="chapter"){go(prevName);q("#chapterModal").classList.add("on");qa("#switcher button").forEach(function(b){b.classList.toggle("on",b.dataset.go==="chapter")});return}', "go-chapter")

# ---- remove the v5 half-chip debug toggle (element no longer exists) ----
t = rx1(t, r'\n  q\("#halfChip"\)\.addEventListener\("click",function\(\)\{.*?\n  \}\);\n', "\n", "halfchip-js")

# ---- new click handlers + data-driven rendering from LEARN payload ----
NEW_JS = r'''
  /* ============ v6 · Learn sub-screens rendered from extracted code data ============ */
  function esc(s){return String(s).replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;")}
  var LS=LEARN.strings, CM=LEARN.contentModel;
  var FA={
    "Full-Stack Developer":"همهٔ دروس کنکور","Python Developer":"کنکور ریاضی",
    "Back-End Developer":"کنکور تجربی","Front-End Developer":"کنکور انسانی",
    "TypeScript":"زیستشناسی","React":"شیمی","HTML":"فیزیک","SQL":"ریاضی",
    "CSS":"ادبیات","Python":"عربی",
    "JS required":"پیشنیاز: زیست پایه","HTML, CSS and JS requi…":"پیشنیاز: زیست و شیمی و فیزیک…",
    "Career Paths":"مسیرهای شغلی","Courses":"درسها","SECTION":"فصل",
    "Section Project":"پروژهٔ مبحث","Coming soon":"بهزودی"
  };
  function fabtn(en){return FA[en]?' data-fa="'+esc(FA[en])+'"':""}
  /* Career Paths cards — badge vectors are the exact ic_badge_* / ic_code_lang_* drawables */
  var CAREERS=[
    {name:"Full-Stack Developer",sec:"1/20",pct:5,icons:["ic_code_lang_html","ic_badge_js","ic_code_lang_css","ic_badge_react","ic_badge_backend","ic_badge_sql"],sel:false},
    {name:"Python Developer",sec:"2/9",pct:22,icons:["ic_badge_python_dev"],sel:false},
    {name:"Back-End Developer",sec:"2/9",pct:22,icons:["ic_badge_js","ic_badge_backend","ic_badge_sql"],sel:true},
    {name:"Front-End Developer",sec:"1/20",pct:5,icons:["ic_code_lang_html","ic_badge_js","ic_code_lang_css","ic_badge_react"],sel:false}
  ];
  var CC=q("#careerCards");
  CAREERS.forEach(function(c){
    var b=document.createElement("button");
    b.className="career-card"+(c.sel?" sel":"");
    if(!c.sel)b.dataset.modal="unfinishedModal";else b.dataset.nav="path-overview";
    var badges=c.icons.map(function(i){return '<span data-icon="'+i+'" data-size="24"></span>'}).join("");
    b.innerHTML='<span class="badges">'+badges+'</span>'
      +'<h4'+fabtn(c.name)+'>'+esc(c.name)+'</h4>'
      +'<span class="cr"><span data-fa="فصل">SECTION</span><span>'+c.sec+'</span></span>'
      +'<span class="cbar"><i style="width:'+c.pct+'%"></i></span>';
    CC.appendChild(b);
  });
  /* Courses rows — labels from track_switcher_typescript_label / react_label */
  var COURSES=[
    {n:"TypeScript",v:"ic_badge_ts",d:LS.track_switcher.track_switcher_typescript_label,ring:"0/4",part:false},
    {n:"React",v:"ic_badge_react",d:"HTML, CSS and JS requi…",ring:"0/3",part:false},
    {n:"HTML",v:"ic_badge_html",d:"",ring:"0/5",part:false},
    {n:"SQL",v:"ic_badge_sql",d:"",ring:"0/6",part:false},
    {n:"CSS",v:"ic_badge_css",d:"",ring:"0/4",part:false},
    {n:"Python",v:"ic_badge_python",d:"",ring:"6/14",part:true}
  ];
  var CR=q("#courseRows");
  COURSES.forEach(function(c){
    var b=document.createElement("button");b.className="course-row";b.dataset.nav="section-detail";
    b.innerHTML='<span class="cbadge" data-icon="'+c.v+'" data-size="38"></span>'
      +'<span class="ctxt"><b'+fabtn(c.n)+'>'+esc(c.n)+'</b>'+(c.d?'<small'+fabtn(c.d)+'>'+esc(c.d)+'</small>':'')+'</span>'
      +'<span class="cring'+(c.part?" part":"")+'"><b>'+c.ring+'</b></span>';
    CR.appendChild(b);
  });
  /* Path Overview sections — ordinal/name/description from test-tracks.json */
  var SR=q("#sectionRows");
  CM.sections.slice(2,7).forEach(function(s,i){
    var ord=i+3, pct=i===0?43:0;
    var b=document.createElement("button");
    b.className="po-sec"+(i===0?" active":"");
    b.dataset.section=String(ord);b.dataset.nav="section-detail";
    var faName=FA[s.name]||{"JavaScript Basics":"سلول و بافت","HTML Intermediate":"بافتهای گیاهی","Semantic HTML":"بافتهای جانوری","CSS Intermediate":"دستگاه گردش خون","Types and Comparisons":"دستگاه تنفس"}[s.name]||s.name;
    b.innerHTML='<span class="ring'+(pct?" part":"")+'"><b>'+pct+'%</b></span>'
      +'<span class="st"><b data-fa="'+ord+'. '+esc(faName)+'">'+ord+'. '+esc(s.name)+'</b>'
      +'<p data-fa="'+esc(faName)+' — '+s.tutorialCount+' درس">'+esc(s.description)+'</p>'
      +(i===1?'<span class="proj" data-fa="پروژهٔ مبحث">Section Project</span>':'')
      +(i===4?'<span class="soon" data-fa="بهزودی">Coming soon</span>':'')+'</span>';
    SR.appendChild(b);
  });
  /* Section detail — chapters from sections[2].tutorialIds */
  var LR=q("#lessonRows"), ids=CM.sections[2].tutorialIds.slice(0,7);
  ids.forEach(function(id,i){
    var b=document.createElement("button");
    b.className="sd-row "+(i<2?"done":i===2?"cur":"locked");
    b.dataset.nav="chapter";
    b.innerHTML='<span class="sr" data-icon="'+(i<2?"ic_check_white":i===2?"ic_play":"ic_lock_alt_02")+'" data-size="18" data-mono="1"></span>'
      +'<span class="stx"><b data-fa="درس '+fa(i+1)+'">Lesson '+(i+1)+'</b><small>tutorialId '+id+' · '+esc(CM.source.split("/").pop())+'</small></span>'
      +'<span class="si" data-icon="ic_arrow_right" data-size="18" data-mono="1"></span>';
    LR.appendChild(b);
  });
  var proj=document.createElement("button");proj.className="sd-row";proj.dataset.nav="chapter";
  proj.innerHTML='<span class="sr" data-icon="ic_badge_backend" data-size="20"></span><span class="stx"><b data-fa="پروژهٔ مبحث">Section Project</b><small data-fa="پروژهٔ پایانی مبحث">path_overview_section_project_label</small></span><span class="si" data-icon="ic_arrow_right" data-size="18" data-mono="1"></span>';
  LR.appendChild(proj);
  var soon=document.createElement("button");soon.className="sd-row locked";soon.dataset.modal="unfinishedModal";
  soon.innerHTML='<span class="sr" data-icon="ic_lock_outline" data-size="18" data-mono="1"></span><span class="stx"><b data-fa="بهزودی">Coming soon</b><small data-fa="برای باز شدن، مبحث قبل را تمام کنید">Unlock this section by finishing the previous one</small></span><span class="si" data-icon="ic_arrow_right" data-size="18" data-mono="1"></span>';
  LR.appendChild(soon);
  /* clicking a section row opens Section detail with that section's own data */
  qa("#sectionRows .po-sec").forEach(function(b){
    b.addEventListener("click",function(){
      var s=CM.sections[+b.dataset.section-1];
      if(!s)return;
      q("#sdTitle").textContent=s.name;
      q("#sdDesc").textContent=s.description;
      q("#sdNote").innerHTML='فهرست درسها از <span class="codechip2">sections['+(+b.dataset.section-1)+'].tutorialIds</span> ('+s.tutorialCount+' شناسهٔ واقعی داخل APK). لیبلها: <span class="codechip2">lesson_continue</span> · <span class="codechip2">lesson_skip</span> · <span class="codechip2">path_overview_section_project_label</span> · <span class="codechip2">alert_msg_section_setion_locked</span>';
    });
  });
  /* generic modal open/close (Unfinished track) */
  document.addEventListener("click",function(e){
    var m=e.target.closest("[data-modal]");if(m){var t=q("#"+m.dataset.modal);if(t)t.classList.add("on");return}
    var c=e.target.closest("[data-modal-close]");if(c){var t2=q("#"+c.dataset.modalClose);if(t2)t2.classList.remove("on");return}
  });
  paintIcons();
  var l6=q("#learnStats");
  if(l6)l6.innerHTML="<b>شواهد دور ششم:</b> "+LEARN.counts.strings+" رشتهٔ ARSC · "+LEARN.counts.vectors+" وکتور pathData · "+LEARN.counts.layouts+" لایهٔ AXML · "+CM.sections.length+" فصل واقعی · "+LEARN.counts.dex_classes+" کلاس DEX · "+LEARN.counts.catalog_rows+" ردیف کاتالوگ";
'''
t = sub1(t, "  histRender();render();\n})();", NEW_JS + "\n  histRender();render();\n})();", "new-js")

# ---- aside spec: replace method/fidelity/edit sections ----
t = rx1(t, r'    <h3>روش این دور: کد اول، عکس فقط چک نهایی</h3>.*?(?=    <h3>توکنهای کد \(نمونه\)</h3>)', '''    <h3>دور ششم: کندوکاو عمیقتر در کدِ زیرصفحات یادگیری</h3>
    <ul>
      <li><b>ابزار تازه:</b> <code>tools/extract_mimo_learn_v6.py</code> → <code>DESIGN/LEARN_CODE_GEOMETRY.json</code> + <code>CATALOGS/MIMO_LEARN_SUBSCREENS.csv</code> (<span id="learnStats">شمارش…</span>).</li>
      <li><b>منابع خواندهشده:</b> <code>DESIGN_TOKENS.json</code> (ARSC)، <code>res/drawable/*.xml</code> (<code>android:pathData</code>)، <code>res/layout/*.xml</code> (AXML دیکدشده)، <code>res/navigation/nav_onboarding_graph.xml</code>، <code>assets/ui/testdata/test-tracks.json</code>، <code>dex/UI_CLASSES.json</code> و <code>UI_STRING_LITERALS.txt</code>.</li>
      <li><b>مسیرساز:</b> <code>ObservePathSwitcherState</code> (۵۱ کلاس) + <code>ic_list_bulleted</code> + <code>select_path</code> + <code>track_switcher_career_paths</code> + <code>track_switcher_title = Coding Path</code>. سهخط کنار نام مسیر ← <b>Select Path</b>.</li>
      <li><b>نمای مسیر:</b> <code>PathOverviewScreenKt</code> (۲۱ کلاس) + <code>ViewsKt$OverviewEntryPointHeader</code> + <code>certificates_professional_title</code> + <code>path_overview_certificate_percent_complete = %1$d%% Complete</code> + <code>path_overview_section_ordinal = %d. %s</code> + <code>ic_switch</code>.</li>
      <li><b>مدل محتوا:</b> <code>test-tracks.json</code> نسخهٔ ۵۲ · ۲۵ مسیر · ۱۵ فصل با <code>name/description/startIndex/endIndex/tutorialIds</code> · ۹ درس؛ فصلها و شناسهٔ درسها مستقیم از این فایل رندر میشوند.</li>
      <li><b>دیالوگ:</b> <code>certificates_unfinished_track_dialog_title/text/action</code> = «Unfinished track / Finish the track and receive your personalised certificate / Ok» + <code>ic_mimo_mascot</code> (۲۹ مسیر وکتور) + شعاع ۲۸dp.</li>
      <li><b>چیدمان یادگیری:</b> <code>PathToolbarKt$RowWithKeys</code> → ۳ چیپ (سکه ۱٬۲۷۲ / کلید ∞ / استریک ۰)؛ <code>progress_bar_mimo.xml</code> → نوار ۸px با شعاع ۱۰۰dp؛ <code>PathMapScreenKt</code> → گرههای مارپیچ. نوشتهها و چیپهای توضیحی v5 حذف شدند.</li>
    </ul>
    <h3>جریان کلیک (همه از کد)</h3>
    <ul>
      <li>سهخط <code>ic_list_bulleted</code> ← <b>Select Path</b>: مسیرهای شغلی (۴ کارت با badgeهای <code>ic_badge_*</code>) + تکدرسها (۶ ردیف، حلقهٔ ۵۶dp، «JS required» / «HTML, CSS and JS requi…»).</li>
      <li>کارت سربرگ مسیر ← <b>Path Overview</b>: گواهی حرفهای ۲۲٪ / ۲ از ۹ + فصلهای شمارهدار ۳…۷ با درصد ۴۳٪/۰٪ و توضیحات.</li>
      <li>دو فلش <code>ic_switch</code> در نمای مسیر ← دوباره <b>Select Path</b>؛ کلیک روی مسیر ناتمام یا روی کارت گواهی ← <b>Unfinished track</b>.</li>
      <li>کلیک روی فصل یا روی گرهٔ مسیر ← <b>داخل مبحث</b> (فهرست درسها با <code>tutorialId</code> واقعی) ← کارت شروع فصل ← صفحهٔ درس.</li>
      <li><b>صفحهٔ ورود فعلاً حذف شد</b> (صفحهٔ ۷ دور قبل)؛ شواهدش در <code>mimo-09-onboarding.webp</code> بایگانی است.</li>
    </ul>
    <h3>تفاوت کد / اسکرینشات (کد ملاک است)</h3>
    <ul>
      <li><b>تب MAX:</b> اسکرینشات <code>mimo-10</code> نسخهای با تب MAX نشان میدهد؛ حکم صریح محصول <b>۵ تب Learn/Practice/AI/Leaderboard/Profile</b> است و MAX راه نیافت. منوی AXML چهارتبه و اسکرینشاتها صرفاً بایگانی شاهداندر.</li>
      <li><b>عنوان فصلها:</b> <code>test-tracks.json</code> نام «Make a Website / HTML Basics…» میدهد، اسکرینشاتها «Back-End Developer / Arrays & Functions…». ساختار، شمارهگذاری، حلقهها و رشتهها از <b>کد</b> آمدند و فقط <b>نام درس/مبحث</b> کنکوری شد.</li>
      <li><b>RTL:</b> APK هیچ کوالیفایر RTL ندارد؛ نمای پیشفرض LTRِ ۱۰۰٪ میمو + دکمهٔ «فارسی / RTL».</li>
    </ul>
    <h3>حفظشده از دور قبل</h3>
    <ul>
      <li>۵ تب · ۷ بخش لیبلدار هاب · تایمر فقط داخل آزمون · ۲۷۰ دقیقهٔ ثابت · «پاسخبرگ» ≠ «پاسخنامه» · دکمهٔ «توضیح با هوش مصنوعی» در صفحهٔ سؤالات و نتیجه · لیدربورد با اطلاعات خود فرد · ۸ دکمهٔ LH · مشاوره PARKED · بدون Pro/پرداخت.</li>
    </ul>
''', "aside-replace")

t = sub1(t, "<li><b>DESIGN v5 · FINAL DRAFT</b> — منتظر تأیید نهایی</li>",
         "<li><b>DESIGN v6 · REVIEW</b> — منتظر تأیید نهایی</li>", "aside-status")

t = sub1(t,
         "⚠️ این <b>طرح نهایی v5</b> است، نه محصول.",
         "⚠️ این <b>طرح دور ششم v6</b> است، نه محصول.", "footer")
t = sub1(t,
         "بخشهای اصلی مستقیماً از جداول منبع Mimo 9.35 (وکتورها، رنگها، دایمنشنها، استایلها، رشتهها، لایههای AXML و فهرست کلاسهای Composeی DEX) بازتولید شدند؛ ۹ اسکرینشات پیوستشده فقط <b>چک بصری</b>اند.",
         "زیرصفحات یادگیری مستقیماً از جداول منبع Mimo 9.35 (رشتههای ARSC، <code>pathData</code> وکتورها، لایههای AXML، گراف ناوبری، <code>test-tracks.json</code> و کلاسهای DEX) بازتولید شدند؛ ۱۴ اسکرینشات پیوستشده فقط <b>چک بصری</b>اند.", "footer2")

# ---- inject GEO + LEARN script payloads ----
t = sub1(t, "<script>/*__GEO__*/</script>",
         "<script>/*__GEO__*/</script>\n<script>/*__LEARN__*/</script>", "geo-script")

TPL_OUT.write_text(t, encoding="utf-8")

css = build_css()
js = "var GEO=" + json.dumps(payload, ensure_ascii=False, separators=(",", ":")) + ";"
ljs = "var LEARN=" + json.dumps(learn_payload, ensure_ascii=False, separators=(",", ":")) + ";"
html = t.replace("/*__CSS__*/", css).replace("/*__GEO__*/", js).replace("/*__LEARN__*/", ljs)
for ph in ("/*__CSS__*/", "/*__GEO__*/", "/*__LEARN__*/"):
    if ph in html:
        raise SystemExit("placeholder not replaced: " + ph)
OUT.write_text(html, encoding="utf-8")
print(json.dumps({
    "output": str(OUT), "bytes": OUT.stat().st_size,
    "template": str(TPL_OUT), "template_bytes": TPL_OUT.stat().st_size,
    "css_vars": len(CSS_MAP) * 2, "svg_vectors": len(merged),
    "learn_vectors_added": len(merged) - len(GEO["vectors"]),
    "learn_strings": learn_payload["counts"]["strings"],
    "sections": len(cm["sections"]), "tutorial_ids": len(cm["sections"][2]["tutorialIds"]),
    "views": html.count("<button data-go="),
    "method": GEO["method"],
}, ensure_ascii=False, indent=1))
