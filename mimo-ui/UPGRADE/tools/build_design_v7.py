#!/usr/bin/env python3
# ARCHIVED / REVOKED (round 8): the routine tab and the Habitica scoring idea were removed entirely.
# Kept only as a v7 audit-trail builder. Use tools/build_design_v8.py + tools/finalize_v8.py instead.
# -*- coding: utf-8 -*-
"""Generate DESIGN/index.html (v7) from code-extracted Mimo 9.35 geometry.

Pipeline (all code-first, no screenshot tracing):
  tools/extract_mimo_geometry.py      -> DESIGN/CODE_GEOMETRY.json
  tools/extract_mimo_learn_v6.py      -> DESIGN/LEARN_CODE_GEOMETRY.json
  tools/extract_mimo_nodes_v7.py      -> DESIGN/NODE_CODE_GEOMETRY.json
                                         CATALOGS/MIMO_PATH_NODES.csv
  tools/write_habitica_spec.py        -> DESIGN/HABITICA_SCORING.json
                                         CATALOGS/HABITICA_SOURCES.csv
                                         CATALOGS/HABITICA_SCORING.csv
                                         CATALOGS/PRACTICE_VS_EXAM.csv
  tools/build_design_v7.py            -> DESIGN/index.html + tools/design_v7_template.html

v7 changes (user design review, 2026-11-04):
  1. Learn path-map NODE structure rebuilt exactly from code + visual cross-check:
     purple done squares with 3D lip, current white double-ring + play,
     1/2 progress ring, locked square, elbow connector, dotted grid,
     bolt/practice nodes, floating glossary/book affordance, START bubble.
  2. Bolt nodes open a SEPARATE section-practice checkpoint quiz (from the topic
     up to that section), NOT the Konkur exam hub. 3-way isolation documented.
  3. AI top bar: chain/import emoji replaced by real Mimo attachment/file icons
     with short clear Persian labels «اضافه کردن فایل» + «زنجیره گفت و گو».
  4. AI composer: TEACH/PRACTICE made tiny and kept on the SAME bottom line as
     Dictate (mic icon, voice), gemini-flash-lite-latest and medium.
  5. Exam question page: two clean buttons «سؤال قبل» / «سؤال بعد»; below them
     ONE subtle bottom line with پاسخبرگ + the rest, not bold/bulky.
  6. Leaderboard: Promotion Zone removed.
  7. Bottom nav: 6th low-key Mimo-skinned tab «روتین روزانه» whose scoring is
     ONLY Habitica's scoring system (no Habitica UI/assets/content/code).
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
HAB = json.loads((UP / "DESIGN" / "HABITICA_SCORING.json").read_text(encoding="utf-8"))
BASE = (UP / "tools" / "design_v6_template.html").read_text(encoding="utf-8")
OUT = UP / "DESIGN" / "index.html"
TPL_OUT = UP / "tools" / "design_v7_template.html"

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
        raise SystemExit("template anchor %s matched %d times" % (label, n))
    return text.replace(old, new, 1)


def rx1(text, pattern, new, label, flags=re.S):
    r = re.compile(pattern, flags)
    ms = list(r.finditer(text))
    if len(ms) != 1:
        raise SystemExit("template regex %s matched %d times" % (label, len(ms)))
    return text[:ms[0].start()] + new + text[ms[0].end():]


# --------------------------------------------------------------------------
# 1. Merge all extracted vectors (v5 + v6 Learn + v7 nodes) into one GEO payload
# --------------------------------------------------------------------------
def to_payload_vector(v):
    return {
        "source": v["source"],
        "viewport": [v["viewportWidth"], v["viewportHeight"]],
        "size_dp": [v["widthDp"], v["heightDp"]],
        "paths": [{"d": p["d"], "fill": p["fill"], "alpha": None,
                   "fillType": p["fillType"]} for p in v["paths"]],
        "sha_bytes": None,
    }


merged = dict(GEO["vectors"])
for src in (LRN["vectors"], NOD["vectors"]):
    for name, v in src.items():
        if name not in merged:
            merged[name] = to_payload_vector(v)

payload = {
    "method": GEO["method"], "apk_sha256": GEO["apk_sha256"],
    "sources": GEO["sources"], "vectors": merged,
    "colors": GEO["colors"], "dimens": GEO["dimens"], "styles": GEO["styles"],
    "strings": GEO["strings"], "layouts": GEO["layouts"],
    "compose_path_class_count": GEO["compose_path_class_count"],
}

learn_payload = {
    "method": LRN["method"], "apk": LRN["apk"], "strings": LRN["strings"],
    "contentModel": LRN["contentModel"],
    "counts": {
        "vectors": len(LRN["vectors"]), "layouts": len(LRN["layouts"]),
        "nav_graphs": len(LRN["navigation"]),
        "strings": sum(len(v) for v in LRN["strings"].values()),
        "colors": len(LRN["tokens"]["colors"]), "dimens": len(LRN["tokens"]["dimens"]),
        "styles": len(LRN["tokens"]["styleNames"]),
        "catalog_rows": sum(1 for _ in open(UP / "CATALOGS" / "MIMO_LEARN_SUBSCREENS.csv", encoding="utf-8")) - 1,
        "dex_classes": sum(v["count"] for k, v in LRN["dex"].items() if k != "literals"),
    },
    "layoutNames": sorted(LRN["layouts"]), "vectorNames": sorted(LRN["vectors"]),
    "subScreens": ["learn", "select-path", "path-overview", "section-detail", "unfinished-track"],
}

node_payload = {
    "method": NOD["method"], "apk_sha256": NOD["apk_sha256"], "round": NOD["round"],
    "strings": NOD["strings"], "contentModel": NOD["contentModel"],
    "layoutNames": sorted(NOD["layouts"]), "animations": NOD["animations"],
    "rawAssets": NOD["rawAssets"], "dex": NOD["dex"], "dexLiterals": NOD["dexLiterals"],
    "isolation": NOD["isolation"], "counts": NOD["counts"],
}
hab_payload = {
    "method": HAB["method"], "repo": HAB["repo"], "commit": HAB["commit"],
    "license": HAB["license"], "user_instruction": HAB["user_instruction"],
    "interpretation": HAB["interpretation"], "constants": HAB["constants"],
    "taskTypes": HAB["taskTypes"],
    "rules": [{"id": r["id"], "group": r["group"], "rule": r["rule"],
               "mimo_mapping": r["mimo_mapping"]} for r in HAB["rules"]],
    "sources": [{"upstream_path": s["upstream_path"], "sha256": s["sha256"],
                 "bytes": s["bytes"]} for s in HAB["sources"]],
    "isolation": HAB["isolation"], "counts": HAB["counts"],
}

# --------------------------------------------------------------------------
# 2. CSS appended last (wins over v5/v6 rules)
# --------------------------------------------------------------------------
CSS7 = r'''
/* ============ v7 · exact Mimo path-map NODES (code + visual cross-check) ============ */
.tabs{grid-template-columns:repeat(6,1fr)}
.tabs .tab{font-size:9px;letter-spacing:0}
.pathwrap.l7{height:560px;margin-top:8px;background:radial-gradient(circle,var(--line2) 1.6px,transparent 1.7px) 0 0/26px 26px;background-color:var(--bg);position:relative;overflow:hidden}
.pathwrap.l7 .connector{position:absolute;inset:0;width:100%;height:100%;pointer-events:none;z-index:0}
.pathwrap.l7 .node{position:absolute;width:92px;height:92px;border-radius:26px;display:flex;align-items:center;justify-content:center;cursor:pointer;z-index:2;color:#fff;transition:transform .12s ease;-webkit-tap-highlight-color:transparent}
.pathwrap.l7 .node:hover{transform:translateY(-2px)}
.pathwrap.l7 .node .ic{width:44px;height:44px}
.pathwrap.l7 .node.done{background:linear-gradient(160deg,var(--purple-light),var(--primary));box-shadow:0 8px 0 var(--primary-hi),0 12px 18px rgba(37,39,70,.18)}
.pathwrap.l7 .node.cur{background:var(--card);border:3px solid var(--primary);box-shadow:0 0 0 7px var(--card),0 0 0 10px var(--progress-weak),0 8px 0 var(--primary-hi),0 12px 18px rgba(37,39,70,.16);color:var(--primary)}
.pathwrap.l7 .node.cur:before{content:"";position:absolute;inset:5px;border:2px solid var(--line2);border-radius:20px}
.pathwrap.l7 .node.cur .ic{position:relative;z-index:1}
.pathwrap.l7 .node.half{background:var(--card);border:3px solid var(--primary);box-shadow:0 0 0 7px var(--card),0 0 0 10px var(--progress-weak),0 8px 0 var(--primary-hi);color:var(--primary)}
.pathwrap.l7 .node.half .hring{width:56px;height:56px;border-radius:50%;background:conic-gradient(var(--primary) 0 50%,var(--progress-bg) 50% 100%);display:flex;align-items:center;justify-content:center;position:relative}
.pathwrap.l7 .node.half .hring:before{content:"";position:absolute;inset:7px;border-radius:50%;background:var(--card)}
.pathwrap.l7 .node.half .hring b{position:relative;z-index:1;font:700 13px/1 system-ui,sans-serif;color:var(--text)}
.pathwrap.l7 .node.locked{background:var(--disabled);box-shadow:0 8px 0 var(--card-pressed);color:#fff}
.pathwrap.l7 .node.practice{background:linear-gradient(160deg,var(--purple-light),var(--primary));box-shadow:0 8px 0 var(--primary-hi),0 12px 18px rgba(37,39,70,.18)}
.pathwrap.l7 .node.practice.charged{background:var(--purple-light);color:var(--primary)}
.pathwrap.l7 .node.practice.locked{background:var(--disabled);box-shadow:0 8px 0 var(--card-pressed);color:#fff;opacity:.92}
.node-start{position:absolute;z-index:3;left:calc(50% - 34px);top:201px;background:var(--primary);color:#fff;border-radius:999px;padding:5px 12px;font:700 11px/1 system-ui,sans-serif;letter-spacing:.8px;text-transform:uppercase;box-shadow:0 3px 0 var(--primary-hi)}
.node-start:after{content:"";position:absolute;left:calc(50% - 5px);bottom:-5px;width:10px;height:10px;background:var(--primary);transform:rotate(45deg)}
.gloss-fab{position:absolute;z-index:4;right:16px;bottom:12px;width:56px;height:56px;border-radius:50%;background:var(--card);border:1px solid var(--line2);display:flex;align-items:center;justify-content:center;color:var(--text);cursor:pointer;box-shadow:0 3px 8px rgba(37,39,70,.12)}
.gloss-fab .ga{position:absolute;font:700 13px/1 system-ui,sans-serif;color:var(--primary)}
.l7n1,.l6n1{left:calc(50% - 46px);top:22px}
.l7n2,.l6n2{left:calc(80% - 46px);top:128px}
.l7n3,.l6n3{left:calc(50% - 46px);top:234px}
.l7n4,.l6n4{left:calc(20% - 46px);top:340px}
.l7n5,.l6n5{left:calc(50% - 46px);top:340px}
.l7b1{left:calc(80% - 46px);top:446px}
.l7b2{left:calc(50% - 46px);top:446px}
/* ---- v7 · section practice (bolt checkpoint quiz = LEARN ONLY) ---- */
.sp-scope{display:inline-block;margin:0 0 10px;background:var(--card-pressed);border-radius:999px;padding:4px 11px;font:700 11px/1 system-ui,sans-serif;color:var(--primary)}
.sp-list{padding:0 18px 6px}
.sp-q{margin:0 0 12px;padding:12px 14px;background:var(--card);border:1px solid var(--line2);border-radius:16px}
.sp-q .sp-stem b{display:block;font:700 15px/1.4 system-ui,sans-serif}
.sp-q .sp-stem small{display:block;margin-top:3px;font:400 11px/1.4 system-ui,sans-serif;color:var(--text-weak);direction:ltr}
.sp-opts{display:grid;grid-template-columns:repeat(4,1fr);gap:7px;margin-top:10px}
.sp-opt{border:1px solid var(--line2);background:var(--card);border-radius:12px;padding:9px 0;font:700 13px/1 system-ui,sans-serif;color:var(--text-weak)}
.sp-opt:hover{border-color:var(--primary)}
.sp-opt.on{background:var(--primary);border-color:var(--primary);color:#fff}
.sp-fb{margin:0 18px 12px;padding:10px 13px;border-radius:12px;background:var(--card-pressed);font:400 12px/1.5 system-ui,sans-serif;color:var(--text-weak)}
.sp-fb b{color:var(--primary)}
/* ---- v7 · quiet Mimo-skinned daily routine ---- */
.rt-head{display:flex;align-items:center;justify-content:space-between;padding:16px 18px 10px}
.rt-head b{display:block;font:700 20px/1.2 system-ui,sans-serif}
.rt-head small{display:block;font:400 12px/1.4 system-ui,sans-serif;color:var(--text-weak)}
.rt-head .rt-ic{color:var(--icon);display:flex}
.rt-card{margin:0 18px 14px;padding:13px 14px;background:var(--card);border:1px solid var(--line2);border-radius:16px}
.rt-stats{display:grid;grid-template-columns:repeat(4,1fr);gap:4px}
.rt-stat{text-align:center;display:flex;flex-direction:column;align-items:center;gap:2px}
.rt-stat .ic{color:var(--icon);display:flex}
.rt-stat b{font:700 15px/1 system-ui,sans-serif}
.rt-stat small{font:400 9px/1.2 system-ui,sans-serif;color:var(--text-weak)}
.rt-bar{height:6px;border-radius:999px;background:var(--progress-bg);margin:12px 0 7px;overflow:hidden}
.rt-bar i{display:block;height:100%;background:var(--progress);border-radius:999px}
.rt-meta{display:flex;justify-content:space-between;font:400 10px/1.3 system-ui,sans-serif;color:var(--text-weak)}
.rt-list{padding:0 18px 4px}
.rt-task{display:flex;align-items:center;gap:9px;margin:0 0 9px;padding:9px 11px;background:var(--card);border:1px solid var(--line2);border-radius:14px}
.rt-task .rt-ic{width:30px;height:30px;border-radius:10px;background:var(--card-pressed);display:flex;align-items:center;justify-content:center;color:var(--icon);flex-shrink:0}
.rt-task .rt-tx{flex:1;min-width:0}
.rt-task .rt-tx b{display:block;font:700 13px/1.3 system-ui,sans-serif}
.rt-task .rt-tx small{display:block;font:400 10px/1.4 system-ui,sans-serif;color:var(--text-weak)}
.rt-task .rt-pri{font:700 10px/1 system-ui,sans-serif;color:var(--text-weak);background:var(--card-pressed);border-radius:999px;padding:4px 7px}
.rt-btn{width:28px;height:28px;flex-shrink:0;border:1px solid var(--line2);background:var(--card);border-radius:10px;color:var(--text-weak);font:700 15px/1 system-ui,sans-serif;display:flex;align-items:center;justify-content:center}
.rt-btn:hover{border-color:var(--primary)}
.rt-btn.on{background:var(--primary);border-color:var(--primary);color:#fff}
.rt-btn.buy{width:auto;padding:0 9px;font:700 10px/1 system-ui,sans-serif}
.rt-foot{display:flex;align-items:center;gap:7px;margin:4px 18px 0;font:400 11px/1.5 system-ui,sans-serif;color:var(--text-weak)}
/* ---- v7 · AI top row tidy + one-line composer ---- */
.ai-top-left{display:flex;gap:6px;flex-wrap:nowrap;min-width:0}
.ai-chip{white-space:nowrap;gap:5px;font-size:10px;padding:4px 9px}
.ai-chip b{font-weight:600;color:var(--text);font-size:10px}
.ai-chip .ic{flex-shrink:0;color:var(--primary)}
.ai-foot{flex-wrap:nowrap;overflow-x:auto;gap:4px;scrollbar-width:none;padding-bottom:1px}
.ai-foot::-webkit-scrollbar{display:none}
.ai-foot .mode{flex-shrink:0}
.ai-foot .mode button{font-size:9px;padding:3px 7px;white-space:nowrap}
.ai-foot .mode .lh{display:none}
.ai-foot-chip{font-size:9px;padding:3px 7px;white-space:nowrap;gap:3px;flex-shrink:0}
.ai-foot-chip .ic{flex-shrink:0;color:var(--primary)}
/* ---- v7 · exam question page: two clean buttons + one quiet bottom line ---- */
.qnav{display:flex;gap:8px;margin:12px 14px 6px}
.qnav .btn{flex:1;display:inline-flex;align-items:center;justify-content:center;gap:6px;font-weight:500;font-size:12px;padding:9px 12px;border-radius:999px;background:var(--card);color:var(--text);border:1px solid var(--line2)}
.qnav .btn:hover{border-color:var(--primary)}
.qnav .ic{color:var(--primary)}
.qfoot{position:sticky;bottom:0;z-index:5;display:flex;gap:6px;flex-wrap:nowrap;overflow-x:auto;align-items:center;margin:10px 0 0;padding:9px 14px;background:var(--card);border-top:1px solid var(--line2);scrollbar-width:none}
.qfoot::-webkit-scrollbar{display:none}
.qfoot .btn{font-weight:400;font-size:11px;padding:5px 10px;color:var(--text-weak);background:var(--card);border:1px solid var(--line2);white-space:nowrap;flex-shrink:0;display:inline-flex;align-items:center;gap:5px}
.qfoot .btn:hover{border-color:var(--primary);color:var(--primary)}
.qfoot .ic{color:var(--primary)}
.qfoot.result-foot{position:static;margin:12px 0 4px;background:transparent;border-top:0}
'''

# --------------------------------------------------------------------------
# 3. Template transformations
# --------------------------------------------------------------------------
t = BASE

t = sub1(t, "<title>طرح رابط کاربری v6 — بازآفرینی ۱۰۰٪ میمو از روی کد (Design Review)</title>",
         "<title>طرح رابط کاربری v7 — بازآفرینی ۱۰۰٪ میمو از روی کد (Design Review)</title>", "title")

t = sub1(t, '<h1>طرح رابط کاربری — دور ششم <span class="ver">DESIGN v6 · REVIEW</span></h1>',
         '<h1>طرح رابط کاربری — دور هفتم <span class="ver">DESIGN v7 · REVIEW</span></h1>', "h1")

t = rx1(t, r"<p>بازآفرینی ۱۰۰٪ بخشهای اصلی میمو.*?</p>",
        "<p>بازآفرینی ۱۰۰٪ بخشهای اصلی میمو <b>از روی کد/مهندسی معکوس</b> · "
        "<b>دور هفتم:</b> گرههای مربعی یادگیری دقیقاً از کد بازسازی شدند (تیک بنفش با سایهٔ سهبعدی، حلقهٔ سفید/پلی، حلقهٔ ½، قفل، "
        "اتور گردگوشه، نقطهچین و دکمهٔ شناور واژهنامه)؛ <b>گرههای رعدوبرق → «تمرین مبحث تا همان فصل»</b>، "
        "<b>جدا از هاب آزمون کنکور</b>؛ نوار بالای AI مرتب با «اضافه کردن فایل» و «زنجیره گفت و گو»؛ خط پایین AI تکخط و ریز؛ "
        "صفحهٔ سؤال دو دکمهٔ تمیز قبل/بعد + کنترلهای کمرنگ در یک خط؛ لیدربورد بدون Promotion Zone؛ "
        "<b>تب ششم کمسر و صدای «روتین روزانه»</b> فقط با سیستم امتیازدهی Habitica. اسکرینشاتها فقط چک بصری.</p>",
        "header-p")

t = sub1(t, '<a class="btn" href="LEARN_CODE_GEOMETRY.json">📚 شواهد زیرصفحات یادگیری</a>',
         '<a class="btn" href="LEARN_CODE_GEOMETRY.json">📚 شواهد زیرصفحات یادگیری</a>\n'
         '    <a class="btn" href="NODE_CODE_GEOMETRY.json">🔷 هندسهٔ گرهها v7</a>\n'
         '    <a class="btn" href="HABITICA_SCORING.json">⚖️ قواعد امتیازدهی روتین</a>', "header-links")

# ---- switcher: 13 -> 15 views ----
SWITCHER = '''<div class="switcher" id="switcher">
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
      <button data-go="routine">۱۱ · روتین روزانه</button>
      <button data-go="exam-hub">۱۲ · هاب آزمونها</button>
      <button data-go="exam-run">۱۳ · اجرای آزمون</button>
      <button data-go="exam-result">۱۴ · صفحهٔ آخر آزمون</button>
      <button data-go="ai">۱۵ · چت AI</button>
    </div>'''
t = rx1(t, r'<div class="switcher" id="switcher">.*?\n    </div>', SWITCHER, "switcher")

# ---- CSS injected before </style> ----
t = sub1(t, "\n</style>", CSS7 + "\n</style>", "css7")

# ---- v7 Learn path-map: exact nodes ----
LEARN7 = r'''      <!-- ============ 1. LEARN / PATH MAP = v7 exact node geometry from code ============ -->
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
        <div class="pathwrap l6 l7">
          <svg class="connector" viewBox="0 0 392 560" preserveAspectRatio="none">
            <path d="M196 68 H270 Q314 68 314 112 V130 Q314 174 270 174 H240 Q196 174 196 218 V236 Q196 280 152 280 H122 Q78 280 78 324 V342 Q78 386 122 386 H148 Q196 386 196 430 V448 Q196 492 240 492 H270 Q314 492 314 448" fill="none" stroke="var(--progress)" stroke-width="10" stroke-linecap="round" stroke-linejoin="round" opacity=".55"/>
            <path d="M196 68 H270 Q314 68 314 112 V130 Q314 174 270 174 H240 Q196 174 196 218 V236 Q196 280 152 280 H122 Q78 280 78 324 V342 Q78 386 122 386 H148 Q196 386 196 430 V448 Q196 492 240 492 H270 Q314 492 314 448" fill="none" stroke="var(--card)" stroke-width="4" stroke-dasharray="1 14" stroke-linecap="round" opacity=".6"/>
          </svg>
          <span class="node-start" data-fa="شروع">START</span>
          <div class="node done l6n1 l7n1" data-icon="ic_check_white" data-size="44" data-mono="1" data-nav="chapter" title="PathMapScreenKt · completed chapter → chapter_toolbar.xml"></div>
          <div class="node done l6n2 l7n2" data-icon="ic_check_white" data-size="44" data-mono="1" data-nav="chapter" title="completed chapter · start_lesson"></div>
          <div class="node cur l6n3 l7n3" id="curNode" data-icon="ic_play" data-size="40" data-mono="1" data-nav="chapter" title="current chapter · white double ring · ic_play"></div>
          <div class="node half l6n4 l7n4" data-nav="chapter" title="1/2 progress ring · glance_circular_progress_indicator.xml"><span class="hring"><b>1/2</b></span></div>
          <div class="node locked l6n5 l7n5" data-icon="ic_lock_alt_02" data-size="38" data-mono="1" data-locked="1" title="alert_msg_section_setion_locked"></div>
          <div class="node practice charged l7b1" data-icon="ic_bolt_charged" data-size="42" data-nav="section-practice" data-practice="3" title="bolt checkpoint → section practice up to section 3 · Fully charged!"></div>
          <div class="node practice locked l7b2" data-icon="ic_bolt" data-size="42" data-mono="1" data-nav="section-practice" data-practice="5" title="bolt checkpoint → section practice up to section 5 · ic_practice_tab_locked"></div>
          <div class="gloss-fab" data-glossary="1" title="floating book / glossary affordance · mimo-01"><span data-icon="ic_file" data-size="30" data-mono="1"></span><b class="ga">A</b></div>
        </div>
      </section>'''
t = rx1(t, r'      <!-- ============ 1\. LEARN.*?</section>', LEARN7, "learn7")

# ---- exam-run: two clean buttons + one quiet bottom line ----
EXAMRUN7 = r'''      <section class="screen konkur" data-screen="exam-run">
        <div class="appbar"><div class="left"><button class="iconbtn" data-nav="exam-hub">→</button><b id="examTitle">آزمون جامع کنکور</b></div><button class="timerchip" id="timerChip">⏱ <span id="timerLabel">تنظیم زمان</span></button></div>
        <div id="examFinished"></div>
        <div class="qmeta"><span>سؤال ۳ از ۲۰</span><span id="timerStateText">زمان تنظیم نشده</span></div>
        <div class="qtext" id="qText">کدامیک از گزینههای زیر دربارهٔ «سمها» درست است؟ اگر پاسخ را نمیدانید میتوانید علامت بزنید و بعداً برگردید.</div>
        <div class="opt" data-opt="1"><span>۱</span> گزینهٔ اول</div><div class="opt" data-opt="2"><span>۲</span> گزینهٔ دوم</div><div class="opt" data-opt="3"><span>۳</span> گزینهٔ سوم</div><div class="opt" data-opt="4"><span>۴</span> گزینهٔ چهارم</div>
        <div class="qnav">
          <button class="btn" id="prevQ"><span data-icon="ic_arrow_left" data-size="16" data-mono="1"></span>سؤال قبل</button>
          <button class="btn" id="nextQ">سؤال بعد<span data-icon="ic_arrow_right" data-size="16" data-mono="1"></span></button>
        </div>
        <div class="hint" id="policyHint">سیاست: <b>عادی / زماندار / تحلیلی</b> ← «پاسخبرگ» (گزینههای زدهشده) و «پاسخنامه» (جواب تشریحی + توضیحات) حین آزمون؛ <b>جامع / جمع بندی / نهایی</b> ← زمان خالص آزمون، و در پایان آزمون صفحهٔ پاسخنامه باز میشود.</div>
        <div class="hint">💡 تنها ایدهٔ جزیی گرفتهشده از EPM: یک دکمهٔ «توضیح با هوش مصنوعی» در همین صفحهٔ سؤالات — بدون پنل یا داک تازه. همان دکمه در صفحهٔ آخر آزمون، صورت اشتباهات + پاسخهای شما + صورت سؤالها را به چت مینیمال منتقل میکند.</div>
        <div class="hint">تایمر معکوس فقط داخل آزمون: کلیک روی chip بالا ← عدد دقیقه ← شروع ← شمارش معکوس. توقف/ادامه و ثبت خودکار در صفر.</div>
        <div class="qfoot">
          <button class="btn" id="answerSheetBtn" data-sheet="paletteSheet">پاسخبرگ</button>
          <button class="btn" id="answerKeyBtn" data-sheet="keySheet">پاسخنامه</button>
          <button class="btn" data-sheet="exitSheet">خروج</button>
          <button class="btn" id="endExam">اتمام آزمون</button>
          <button class="btn" id="askAiBtn"><span data-icon="ic_magic_wand" data-size="15" data-mono="1"></span>توضیح با هوش مصنوعی</button>
          <button class="btn" id="timerPause" style="display:none">توقف</button>
          <button class="btn" id="timerReset" style="display:none">تنظیم مجدد</button>
        </div>
      </section>'''
t = rx1(t, r'      <section class="screen konkur" data-screen="exam-run">.*?</section>', EXAMRUN7, "examrun7")

RESULT_FOOT = '''        <div class="qfoot result-foot">
          <button class="btn" id="resultBargBtn" data-sheet="paletteSheet">پاسخبرگ</button>
          <button class="btn" id="resultKeyBtn" data-sheet="keySheet">پاسخنامه</button>
          <button class="btn" id="askAiResultBtn"><span data-icon="ic_magic_wand" data-size="15" data-mono="1"></span>توضیح با هوش مصنوعی</button>
        </div>'''
t = sub1(t, '''        <div class="krow">
          <button class="btn" id="resultBargBtn" data-sheet="paletteSheet">پاسخبرگ</button>
          <button class="btn" id="resultKeyBtn" data-sheet="keySheet">پاسخنامه</button>
          <button class="btn primary" id="askAiResultBtn" style="display:inline-flex;align-items:center;gap:7px;border-radius:999px;padding:8px 16px;font-weight:bold"><span data-icon="ic_magic_wand" data-size="16" data-mono="1"></span>توضیح با هوش مصنوعی</button>
        </div>''', RESULT_FOOT, "resultfoot7")

# ---- AI top row: attachment + conversation chain, tidy distinct icons ----
AI_TOP7 = r'''        <div class="krow ai-top" style="justify-content:space-between;margin:0 0 6px">
          <div class="ai-top-left">
            <button class="fchip ai-chip" data-lh="Import notes..."><span data-icon="attachment" data-size="14" data-mono="1"></span><b>اضافه کردن فایل</b><span class="lh">Import notes...</span></button>
            <button class="fchip ai-chip" data-lh="Chains"><span data-icon="ic_link_external" data-size="14" data-mono="1"></span><b>زنجیره گفت و گو</b><span class="lh">Chains</span></button>
          </div><span class="cost" data-lh="Cost $0.01">$0.01</span>
        </div>'''
t = sub1(t, '''        <div class="krow" style="justify-content:space-between;margin:0 0 6px">
          <div style="display:flex;gap:6px;flex-wrap:wrap">
            <button class="fchip" data-lh="Chains">🔗 زنجیرهها <span class="lh">Chains</span></button>
            <button class="fchip" data-lh="Import notes...">⬆ یادداشتها <span class="lh">Import notes...</span></button>
          </div><span class="cost" data-lh="Cost $0.01">$0.01</span>
        </div>''', AI_TOP7, "aitop7")

AI_FOOT7 = r'''          <div class="foot ai-foot">
            <span class="mode" id="mode"><button class="on" data-mode="TEACH" data-fa="آموزش">TEACH <span class="lh">TEACH</span></button><button data-mode="PRACTICE" data-fa="تمرین">PRACTICE <span class="lh">PRACTICE</span></button></span>
            <button class="fchip ai-foot-chip" data-lh="Dictate"><span data-icon="ic_microphone" data-size="13" data-mono="1"></span>دیکته <span class="lh">Dictate</span></button>
            <button class="fchip ai-foot-chip" data-lh="Model picker">gemini-flash-lite-latest <span data-icon="ic_chevron_down" data-size="11" data-mono="1"></span></button>
            <button class="fchip ai-foot-chip" data-lh="Effort">medium <span data-icon="ic_chevron_down" data-size="11" data-mono="1"></span></button>
          </div>'''
t = sub1(t, '''          <div class="foot">
            <span class="mode" id="mode"><button class="on" data-mode="TEACH">آموزش <span class="lh">TEACH</span></button><button data-mode="PRACTICE">تمرین <span class="lh">PRACTICE</span></button></span>
            <button class="fchip" data-lh="Dictate">🎙 دیکته <span class="lh">Dictate</span></button>
            <button class="fchip" data-lh="Model picker">gemini-flash-lite-latest ▾</button>
            <button class="fchip" data-lh="Effort">medium ▾</button>
          </div>''', AI_FOOT7, "aifoot7")

# ---- leaderboard: Promotion Zone removed ----
t = sub1(t, '        <div class="promo"><span class="ln"></span><b data-fa="منطقهٔ صعود">Promotion Zone</b><span class="ln"></span></div>\n',
         '', "promo7")

# ---- two NEW screens, inserted before sheets & modal ----
PRACTICE7 = r'''      <!-- ============ v7 · SECTION PRACTICE = bolt checkpoint quiz (LEARN ONLY) ============ -->
      <section class="screen mimo" data-screen="section-practice" data-scope="learn-practice" data-isolated="exam">
        <div class="sp-top"><button class="x" data-nav="learn"><span data-icon="ic_arrow_left" data-size="22" data-mono="1"></span></button><b data-fa="تمرین مبحث">Section practice</b></div>
        <div class="sd-hero">
          <span class="kick">SECTION · PRACTICE</span>
          <h2 id="spTitle">HTML Basics</h2>
          <p>Sharpen your skills with hands-on practice exercises and projects</p>
          <span class="sp-scope" id="spScope">تا فصل ۳ · ۰ درس</span>
          <div class="cbar"><i style="width:43%"></i></div>
        </div>
        <div class="sp-list" id="practiceQuestions"></div>
        <div id="practiceResult"></div>
        <button class="sd-cta" id="practiceStart">Start lesson</button>
        <button class="sd-link" data-modal="practiceModal">Fully charged!</button>
        <p class="sd-note" data-fa="تمرینهای این مبحث و فصلهای پیش از آن">Practice exercises for this section and everything before it.</p>
      </section>

      <!-- ============ v7 · DAILY ROUTINE = Habitica scoring ONLY, Mimo skin ============ -->
      <section class="screen mimo" data-screen="routine" data-scope="routine-only" data-isolated="exam learn leaderboard">
        <div class="rt-head">
          <div><b>روتین روزانه</b><small>Daily goal</small></div>
          <span class="rt-ic" data-icon="ic_calendar" data-size="34" data-mono="1"></span>
        </div>
        <div class="rt-card">
          <div class="rt-stats">
            <div class="rt-stat"><span class="ic" data-icon="ic_sparks" data-size="20"></span><b id="rtXp">0</b><small>XP</small></div>
            <div class="rt-stat"><span class="ic" data-icon="ic_coin" data-size="20"></span><b id="rtGp">0</b><small>GP</small></div>
            <div class="rt-stat"><span class="ic" data-icon="ic_streak_active" data-size="20"></span><b id="rtStreak">0</b><small>Streak</small></div>
            <div class="rt-stat"><span class="ic" data-icon="ic_task_completed" data-size="20"></span><b id="rtLvl">1</b><small>Level</small></div>
          </div>
          <div class="rt-bar"><i id="rtBar" style="width:0%"></i></div>
          <div class="rt-meta"><span id="rtNext">سطح ۲: ۲۵ XP</span><span id="rtHp">سلامت ۵۰ / ۵۰</span></div>
        </div>
        <div class="rt-list" id="rtTasks"></div>
        <div class="rt-foot" id="rtFoot"></div>
        <p class="sd-note" data-fa="هدف روزانه؛ تمرین کم و هرروزه مؤثرترین راه است">Daily goal · practicing little every day is the most effective.</p>
      </section>

'''
t = sub1(t, '      <!-- ============ sheets & modal ============ -->',
         PRACTICE7 + '      <!-- ============ sheets & modal ============ -->', "newscreens7")

PRACTICE_MODAL = r'''      <div class="modal" id="practiceModal"><div class="modal-card ut-card">
        <span class="utx" data-modal-close="practiceModal"><span data-icon="ic_close" data-size="22" data-mono="1"></span></span>
        <div class="ut-art"><span data-icon="ic_mascot_practice" data-size="104"></span></div>
        <h2 id="practiceModalTitle">Fully charged!</h2>
        <p id="practiceModalText">Practicing little every day is proved to be the most effective.</p>
        <button class="utok" data-modal-close="practiceModal">Practice anyway</button>
      </div></div>
'''
t = sub1(t, '      <div class="modal" id="chapterModal">', PRACTICE_MODAL + '      <div class="modal" id="chapterModal">', "practicemodal7")

# ---- bottom nav: 6th low-key tab «روتین روزانه» (MAX still forbidden) ----
TABS7 = r'''      <!-- ============ BOTTOM NAV = 6 tabs (v7 explicit override; MAX forbidden) ============ -->
      <div class="tabs" id="tabs">
        <div class="tab on" data-tab="Learn"><span class="ir i-off" data-icon="ic_cap" data-size="22" data-mono="1"></span><span class="ir i-on" data-icon="ic_cap_filled" data-size="22" data-mono="1"></span><span data-fa="یادگیری">Learn</span></div>
        <div class="tab" data-tab="Practice"><span class="ir i-off" data-icon="ic_flash" data-size="22" data-mono="1"></span><span class="ir i-on" data-icon="ic_flash_filled" data-size="22" data-mono="1"></span><span data-fa="تمرین">Practice</span></div>
        <div class="tab" data-tab="AI"><span class="ir i-off" data-icon="ic_magic_wand" data-size="22" data-mono="1"></span><span class="ir i-on" data-icon="ic_magic_wand_filled" data-size="22" data-mono="1"></span><span>AI</span></div>
        <div class="tab" data-tab="Leaderboard"><span class="ir i-off" data-icon="ic_trophy" data-size="22" data-mono="1"></span><span class="ir i-on" data-icon="ic_trophy_filled" data-size="22" data-mono="1"></span><span data-fa="لیدربورد">Leaderboard</span></div>
        <div class="tab" data-tab="Profile"><span class="ir i-off" data-icon="ic_user_circle" data-size="22" data-mono="1"></span><span class="ir i-on" data-icon="ic_user_circle_filled" data-size="22" data-mono="1"></span><span data-fa="پروفایل">Profile</span></div>
        <div class="tab" data-tab="Routine"><span class="ir i-off" data-icon="ic_calendar" data-size="22" data-mono="1"></span><span class="ir i-on" data-icon="ic_task_completed" data-size="22" data-mono="1"></span><span>روتین روزانه</span></div>
      </div>'''
t = rx1(t, r'      <!-- ============ BOTTOM NAV = 5 tabs.*?\n      </div>', TABS7, "tabs7")

# ---- aside spec ----
ASIDE7 = r'''  <aside class="spec">
    <h3>دور هفتم: گرهها، تمرین مبحث و روتین روزانه</h3>
    <ul>
      <li><b>ابزار تازه:</b> <code>tools/extract_mimo_nodes_v7.py</code> → <code>DESIGN/NODE_CODE_GEOMETRY.json</code> + <code>CATALOGS/MIMO_PATH_NODES.csv</code> (<span id="nodeStats">شمارش…</span>).</li>
      <li><b>منابع خواندهشده:</b> <code>values/values/string.xml</code> (۱۴۱ رشته)، <code>res/drawable/*.xml</code> (۵۵ وکتور <code>pathData</code>), <code>res/layout/*.xml</code> (۱۷ لایه)، <code>res/anim/rc_checkpoint_window_*.xml</code>، <code>res/raw/practice.riv</code>، <code>test-tracks.json</code> (۱۵ فصل / ۲۲۳ <code>tutorialId</code>) و <code>dex/UI_CLASSES.json</code> (۳۸۰ کلاس مرتبط).</li>
      <li><b>گره دقیق:</b> مربع ۹۲px / شعاع ۲۶dp / لبهٔ سهبعدی ۸px (<code>button_primary_highlight</code>)؛ تیک بنفش <code>ic_check_white</code>؛ فعلی = کارت سفید + حلقهٔ دوتایی + <code>ic_play</code>؛ حلقهٔ ½ از <code>glance_circular_progress_indicator.xml</code>؛ قفل = <code>card_disabled</code> + <code>ic_lock_alt_02</code>؛ اتور <b>گردگوشه Q</b> (نه منحنی بزیه)؛ نقطهچین ۲۶px؛ دکمهٔ شناور واژهنامه (<code>ic_file</code> + A)؛ برچسب START.</li>
      <li><b>چک بصری فقط:</b> <code>mimo-01</code> (تیک/پلی/قفل/دو گره رعدوبرق/کتاب)، <code>mimo-02</code> (حلقهٔ ½)، <code>mimo-10</code> (اتور گردگوشه + گره رعدوبرق فعال) — کد ملاک است.</li>
      <li><b>دیالوگهای Smart Practice:</b> <code>section_details_smart_practice_charged_dialog_title = Fully charged!</code>، <code>mastered_dialog_title = You’ve mastered the section!</code>، <code>practice_anyway = Practice anyway</code>، <code>ic_mascot_practice</code>، <code>ModalData$SmartPracticeChargedModal/MasteredModal</code>.</li>
      <li><b>شواهد قبلی:</b> <code>DESIGN/LEARN_CODE_GEOMETRY.json</code> (<span id="learnStats">شمارش…</span>) و <code>DESIGN/CODE_GEOMETRY.json</code> همچنان پابرجا؛ <b>DESIGN v6</b> بایگانی شد.</li>
    </ul>
    <h3>جریان کلیک (همه از کد)</h3>
    <ul>
      <li>سهخط <code>ic_list_bulleted</code> ← <b>Select Path</b> ← نمای مسیر ← داخل مبحث ← کارت شروع فصل ← صفحهٔ درس (همان دور ششم).</li>
      <li>کلیک روی <b>هر گرهٔ درس</b> ← کارت «Start learning» (<code>chapter_toolbar.xml</code> + <code>start_lesson</code>)؛ گرهٔ قفل ← toast <code>alert_msg_section_setion_locked</code>.</li>
      <li><b>گره رعدوبرق ← «تمرین مبحث»</b>: صورت سؤالها از <code>sections[].tutorialIds</code> <b>تا همان فصل</b>؛ فیدبک Mimo + دیالوگ Fully charged / mastered؛ <b>هیچ ارتباطی با هاب آزمون کنکور ندارد</b>.</li>
      <li>تب <b>روتین روزانه</b> ← امتیازدهی خلاصهشدهٔ Habitica در پوستهٔ کمسر و صدای میمو؛ MAX ممنوع.</li>
    </ul>
    <h3>تفکیک سهگانه (نباید قاتی شود)</h3>
    <ul>
      <li><b>تمرین مبحث</b> = <code>data-screen=section-practice</code>، پوستهٔ <code>mimo</code>، بدون تایمر / پاسخبرگ / پاسخنامه / ۲۷۰ دقیقه / POLICY.</li>
      <li><b>آزمون کنکور</b> = <code>exam-hub / exam-run / exam-result</code>، پوستهٔ <code>konkur</code>، ۷ بخش لیبلدار، تایمر فقط داخل آزمون، پاسخبرگ ≠ پاسخنامه، جامع ۲۷۰ دقیقهٔ ثابت.</li>
      <li><b>روتین روزانه</b> = <code>data-screen=routine</code>، فقط قواعد امتیازدهی؛ امتیازاتش به هیچجای دیگر وصل نیست. جدول کامل: <code>CATALOGS/PRACTICE_VS_EXAM.csv</code>.</li>
    </ul>
    <h3>روتین روزانه: فقط سیستم امتیازدهی Habitica</h3>
    <ul>
      <li><span id="habStats">شمارش…</span></li>
      <li><b>قواعد:</b> <code>delta = 0.9747 ^ value</code> · <code>EXP = round(delta × (1+INT×0.025) × priority × crit × 6)</code> · <code>GP = ceil(delta × priority × crit × (1+PER×0.02) × (streak/100+1))</code> · <code>HP</code> با <code>CON</code> · <code>crit</code> تصادفی قطعی · <code>toNextLevel</code> · <code>diminishingReturns</code> · Perfect Day / ۲۱ روز.</li>
      <li><b>چهار نوع کار:</b> عادت / روزانه / کار امروز / پاداش؛ ضریب سختی <code>0.1 / 1 / 1.5 / 2</code> بهصورت چیپ ریز.</li>
      <li><b>حقوقی:</b> کد Habitica GPL-3.0 و داراییها CC-BY-NC-SA؛ <b>هیچ کد/دارایی/رشته/فونت/رنگی کپی نشده</b>، فقط قواعد به زبان خودمان + SHA-256 سورسها (<code>CATALOGS/HABITICA_SOURCES.csv</code>).</li>
      <li><b>پوسته:</b> همان توکنهای میمو (<code>card / primary / progress / TextLabel</code>) و وکتورهای استخراجشده؛ بدون پیکسلآرت، آواتار، آیکون RPG، رنگ/فونت/شعاع/آیکون تازه؛ «زیادی تو چشم نزنه».</li>
    </ul>
    <h3>تغییرات ریز دور هفتم</h3>
    <ul>
      <li><b>نوار بالای AI:</b> ایموجی زنجیر/import حذف → <code>attachment</code> (گیرهٔ کاغذ) + «اضافه کردن فایل» و <code>ic_link_external</code> + «زنجیره گفت و گو»؛ ردیف مرتب، آیکونهای متمایز.</li>
      <li><b>خط پایین AI:</b> «آموزش / TEACH» و «تمرین / PRACTICE» ریز و <b>همان یک خط</b> با <code>Dictate</code> (میکروفن، ویس — جدا نشده)، <code>gemini-flash-lite-latest</code> و <code>medium</code>.</li>
      <li><b>صفحهٔ سؤال:</b> دو دکمهٔ تمیز «سؤال قبل» + «سؤال بعد»؛ پایینش «پاسخبرگ» و بقیهٔ کنترلها در <b>یک خط کمضخامت</b>، بدون bold و بدون حجیمسازی.</li>
      <li><b>لیدربورد:</b> «منطقهٔ صعود / Promotion Zone» حذف شد طبق دستور.</li>
      <li><b>تبها:</b> ششمین تب «روتین روزانه» به دستور صریح اضافه شد؛ حکم قبلی ۵ تب (ناظر به تب MAX) بهروزرسانی شد و MAX همچنان ممنوع.</li>
    </ul>
    <h3>حفظشده از دور قبل</h3>
    <ul>
      <li>هاب تکصفحهای ۷ بخش · تایمر فقط داخل آزمون · ۲۷۰ دقیقهٔ ثابت · «پاسخبرگ» ≠ «پاسخنامه» · دکمهٔ «توضیح با هوش مصنوعی» در سؤالات و نتیجه · لیدربورد اطلاعات خود فرد · ۸ دکمهٔ LH · چت مینیمال + تاریخچه · مشاوره PARKED · بدون Pro/پرداخت/MAX · صفحهٔ ورود حذفشده.</li>
    </ul>
    <h3>توکنهای کد (نمونه)</h3>
    <ul>
      <li><b>bg</b> <code>#F6F7FB</code> / شب <code>#252746</code> · <b>button</b> <code>#7E4BDE</code></li>
      <li><b>progress_chapter</b> <code>#8D60E2</code> · <b>icon_weak</b> <code>#A3A5C3</code></li>
      <li><b>TextH1</b> 24sp · <b>TextP2</b> 16sp · <b>TextLabel3</b> 12sp</li>
      <li><b>toolbar</b> 56dp · <b>lesson_progressbar</b> 6dp · <b>card_radius</b> 12dp</li>
    </ul>
    <h3>یادداشتها (بدون طراحی UI)</h3>
    <ul><li>تنظیمات ← <b>وارد کردن کلید API</b> چت <code>/max</code></li><li>بخش مشاوره = PARKED تا اطلاع ثانوی</li></ul>
    <h3>وضعیت</h3>
    <ul><li><b>DESIGN v7 · REVIEW</b> — منتظر تأیید نهایی</li><li>بعد از تأیید ← مرحلهٔ پیادهمسازی</li><li>هیچ کد محصولی نوشته نشده</li></ul>
  </aside>'''
t = rx1(t, r'  <aside class="spec">.*?</aside>', ASIDE7, "aside7")

t = rx1(t, r'<footer class="foot-note">.*?</footer>',
        r'''<footer class="foot-note">
⚠️ این <b>طرح دور هفتم v7</b> است، نه محصول. گرههای مسیر یادگیری، گرههای رعدوبرق/تمرین مبحث، لیبلها و وکتورها مستقیماً از جداول منبع Mimo 9.35 (<code>ARSC</code>، <code>pathData</code>، <code>AXML</code>، <code>anim</code>، <code>test-tracks.json</code> و DEX) بازتولید شدند؛ ۱۴ اسکرینشات فقط <b>چک بصری</b>اند. «روتین روزانه» تنها <b>سیستم امتیازدهی</b> Habitica را بهصورت خلاصهشده و ایزوله بهکار میبرد: هیچ کد، دارایی، رشته، فونت یا رنگی از آن کپی نشده است. تنها نام درسها/فصلها/مباحث کنکوری شد. هیچ کد محصولی نوشته نشده است.
</footer>''', "footer7")

# ---- inject NODE + HAB script payloads ----
t = sub1(t, "<script>/*__LEARN__*/</script>",
         "<script>/*__LEARN__*/</script>\n<script>/*__NODE__*/</script>\n<script>/*__HAB__*/</script>", "scripts7")

# ---- JS: tabMap / tabScreen / toast / prevQ ----
t = sub1(t, '''  var tabMap={learn:"Learn",chapter:"Learn",lesson:"Learn","select-path":"Learn","path-overview":"Learn","section-detail":"Learn",leaderboard:"Leaderboard","user-profile":"Leaderboard",profile:"Profile","exam-hub":"Practice","exam-run":"Practice","exam-result":"Practice",ai:"AI"};''',
         '''  var tabMap={learn:"Learn",chapter:"Learn",lesson:"Learn","select-path":"Learn","path-overview":"Learn","section-detail":"Learn","section-practice":"Learn",leaderboard:"Leaderboard","user-profile":"Leaderboard",profile:"Profile","exam-hub":"Practice","exam-run":"Practice","exam-result":"Practice",ai:"AI",routine:"Routine"};''', "tabmap7")
t = sub1(t, '''  var tabScreen={Learn:"learn",Practice:"exam-hub",AI:"ai",Leaderboard:"leaderboard",Profile:"profile"};''',
         '''  var tabScreen={Learn:"learn",Practice:"exam-hub",AI:"ai",Leaderboard:"leaderboard",Profile:"profile",Routine:"routine"};''', "tabscreen7")
t = sub1(t, '''  qa("#tabs .tab").forEach(function(t){t.addEventListener("click",function(){go(tabScreen[t.dataset.tab]);toast("تب "+t.dataset.tab+" · ناوبری ۵ تب کنکور")})});''',
         '''  qa("#tabs .tab").forEach(function(t){t.addEventListener("click",function(){go(tabScreen[t.dataset.tab]);toast("تب "+t.dataset.tab+" · ناوبری ۶ تب (۵ تب میمو + روتین روزانه)")})});''', "tabtoast7")
t = sub1(t, '''  q("#nextQ").addEventListener("click",function(){toast("سؤال بعدی (همان چیدمان lesson_interactive میمو)")});''',
         '''  q("#nextQ").addEventListener("click",function(){toast("سؤال بعدی (همان چیدمان lesson_interactive میمو)")});
  q("#prevQ").addEventListener("click",function(){toast("سؤال قبل (همان چیدمان lesson_interactive میمو)")});''', "prevq7")

# ---- NEW v7 JS ----
NEW_JS = r'''
  /* ============ v7 · bolt nodes -> isolated section-practice checkpoint quiz ============ */
  var NS=NODE.strings, NCM=NODE.contentModel, PRACTICE_SECTION=3;
  var P_STEMS=[
    "کدام گزینه تعریف درست این مبحث را میدهد؟",
    "کدام نکته دربارهٔ درسهای تا این فصل صحیح است؟",
    "کدام حالت، نتیجهٔ درست تمرین قبل است؟"
  ];
  function practiceScope(n){
    var arr=NCM.sections.slice(0,n), ids=[];
    arr.forEach(function(s){ids=ids.concat(s.tutorialIds)});
    return {sections:arr,ids:ids};
  }
  function renderPractice(n){
    PRACTICE_SECTION=n;
    var sc=practiceScope(n), sec=NCM.sections[Math.min(n,NCM.sections.length)-1];
    q("#spTitle").textContent=sec.name;
    q("#spScope").textContent="تا فصل "+fa(n)+" · "+fa(sc.ids.length)+" درس";
    var box=q("#practiceQuestions");box.innerHTML="";
    P_STEMS.forEach(function(stem,i){
      var d=document.createElement("div");d.className="sp-q";d.dataset.q=String(i);
      var sname=sc.sections[i%sc.sections.length].name;
      var tid=sc.ids[i%sc.ids.length]||0;
      var opts=[1,2,3,4].map(function(o){return '<button class="sp-opt" data-o="'+o+'">'+fa(o)+'</button>'}).join("");
      d.innerHTML='<div class="sp-stem"><b>'+fa(i+1)+'. '+esc(stem)+'</b><small>'+esc(sname)+' · tutorialId '+fa(tid)+'</small></div><div class="sp-opts">'+opts+'</div>';
      box.appendChild(d);
    });
    q("#practiceResult").innerHTML="";
    q("#practiceStart").textContent="شروع تمرین";
    q("#practiceModalTitle").textContent=NS.practice.section_details_smart_practice_charged_dialog_title;
    q("#practiceModalText").textContent=NS.practice.section_details_smart_practice_charged_dialog_description;
    paintIcons(box);
  }
  q("#practiceStart").addEventListener("click",function(){
    var qs=qa("#practiceQuestions .sp-q"),answered=0,correct=0;
    qs.forEach(function(x,i){var s=q(".sp-opt.on",x);if(s){answered++;if(+s.dataset.o===(i%4)+1)correct++}});
    q("#practiceResult").innerHTML='<div class="sp-fb"><b>'+fa(answered)+' / '+fa(qs.length)+'</b> پاسخ ثبت شد · '+esc(NS.path_nodes.lesson_feedback_keep_going||"Let's keep it going.")+'</div>';
    if(answered===qs.length){
      q("#practiceModalTitle").textContent=NS.practice.section_details_smart_practice_mastered_dialog_title;
      q("#practiceModalText").textContent=NS.practice.section_details_smart_practice_mastered_dialog_description;
      q("#practiceModal").classList.add("on");
      toast(NS.practice.you_finished_all_practice_sessions);
    }else toast("چند سؤال هنوز پاسخ ندادهاند");
  });

  /* ============ v7 · daily routine: Habitica SCORING RULES only, Mimo skin ============ */
  var HC=HAB.constants;
  var RS={xp:0,gp:0,hp:HC.MAX_HEALTH,lvl:1,streak:0,int:0,per:0,str:0,con:0};
  var RT_META={habit:"مرور کوتاه روزانه",daily:"حل ۵ سؤال",todo:"پایان یک فصل",reward:"استراحت ۱۰ دقیقهای"};
  function toNext(l){return l<5?25*l:l===5?150:Math.round((l*l*0.25+10*l+139.75)/10)*10}
  function critMul(s){var x=Math.sin(1+s*0.37)*10000,r=x-Math.floor(x);return r<=HC.CRIT_BASE_CHANCE*(1+s/100)?HC.CRIT_BASE_MULTIPLIER+(4*s)/(s+200):1}
  function diminish(b,mx){return mx*b/(b+mx/2)}
  function scoreTask(dir,pri,kind){
    if(dir==="buy"){if(RS.gp<HC.DEFAULT_REWARD_VALUE){toast("سکهٔ روتین کافی نیست");return}RS.gp-=HC.DEFAULT_REWARD_VALUE;toast("پاداش: "+fa(HC.DEFAULT_REWARD_VALUE)+" سکهٔ روتین");return}
    var d=Math.pow(HC.DELTA_BASE,0)*(dir==="down"?-1:1);
    var c=critMul(RS.str);
    var ex=Math.round(d*(1+RS.int*0.025)*pri*c*HC.EXP_MULTIPLIER);
    var gp=Math.ceil(d*pri*c*(1+RS.per*0.02)*(RS.streak/100+1));
    if(dir==="down"){
      var con=Math.max(0.1,1-Math.min(RS.con,100)/250);
      RS.hp=Math.max(0,Math.min(HC.MAX_HEALTH,RS.hp+d*con*pri*HC.HP_MULTIPLIER));
      toast("امتیاز منفی ثبت شد");
    }else{
      RS.xp+=ex;RS.gp=Math.max(0,RS.gp+gp);
      if(kind==="daily"){
        RS.streak++;
        if(RS.streak%HC.PERFECT_DAY_STREAK_DAYS===0)toast("نشان «روز کامل» · "+fa(HC.PERFECT_DAY_STREAK_DAYS)+" روز پیاپی");
      }
      toast("+ "+fa(ex)+" XP · + "+fa(gp)+" سکهٔ روتین");
    }
    while(RS.xp>=toNext(RS.lvl)){
      RS.xp-=toNext(RS.lvl);RS.lvl++;RS.hp=HC.MAX_HEALTH;
      if(RS.lvl>=HC.MAX_LEVEL)break;
    }
  }
  function rtUpdate(){
    var need=toNext(RS.lvl);
    q("#rtXp").textContent=fa(RS.xp);q("#rtGp").textContent=fa(RS.gp);
    q("#rtStreak").textContent=fa(RS.streak);q("#rtLvl").textContent=fa(RS.lvl);
    q("#rtBar").style.width=Math.min(100,Math.round(RS.xp/need*100))+"%";
    q("#rtNext").textContent="سطح "+fa(RS.lvl+1)+": "+fa(need)+" XP";
    q("#rtHp").textContent="سلامت "+fa(Math.round(RS.hp))+" / "+fa(HC.MAX_HEALTH);
  }
  var RL=q("#rtTasks");RL.innerHTML="";
  HAB.taskTypes.forEach(function(tt){
    var d=document.createElement("div");d.className="rt-task";d.dataset.rt=tt.id;d.dataset.pri=tt.priority;
    var acts=tt.id==="habit"
      ? '<button class="rt-btn" data-rt-act="down">−</button><button class="rt-btn on" data-rt-act="up">+</button>'
      : tt.id==="reward"
        ? '<button class="rt-btn buy" data-rt-act="buy">'+fa(HC.DEFAULT_REWARD_VALUE)+' سکه</button>'
        : '<button class="rt-btn on" data-rt-act="up"><span data-icon="ic_check_white" data-size="16" data-mono="1"></span></button>';
    d.innerHTML='<span class="rt-ic" data-icon="'+tt.icon+'" data-size="22" data-mono="1"></span>'
      +'<span class="rt-tx"><b>'+esc(tt.fa)+'</b><small>'+esc(RT_META[tt.id])+'</small></span>'
      +'<span class="rt-pri">'+tt.priority+'</span>'+acts;
    RL.appendChild(d);
  });
  paintIcons(RL);
  q("#rtFoot").innerHTML='<span data-icon="ic_sparks_alt" data-size="16" data-mono="1"></span> '
    +esc(HAB.rules[16].rule.split(";")[0]);
  paintIcons(q("#rtFoot"));
  rtUpdate();
  renderPractice(3);

  /* v7 delegated interactions: bolt nodes, locked node, glossary, practice options, routine */
  document.addEventListener("click",function(e){
    var b=e.target.closest("[data-practice]");
    if(b){
      var n=+b.dataset.practice;
      if(!n){toast(NS.section.alert_msg_section_setion_locked);return}
      renderPractice(n);
      toast("تمرین مبحث: تا فصل "+fa(n)+" (جدا از آزمون کنکور)");
      return;
    }
    var lk=e.target.closest("[data-locked]");
    if(lk){toast(NS.section.alert_msg_section_setion_locked);return}
    var gl=e.target.closest("[data-glossary]");
    if(gl){toast("واژهنامهٔ مبحث (affordance شناور میمو)");return}
    var o=e.target.closest(".sp-opt");
    if(o){qa(".sp-opt",o.parentNode).forEach(function(x){x.classList.remove("on")});o.classList.add("on");return}
    var a=e.target.closest("[data-rt-act]");
    if(a){
      var row=a.closest("[data-rt]");
      scoreTask(a.dataset.rtAct,+row.dataset.pri,row.dataset.rt);
      rtUpdate();return;
    }
  });

  var n7=q("#nodeStats");
  if(n7)n7.innerHTML="<b>شواهد دور هفتم:</b> "+NODE.counts.strings+" رشتهٔ ARSC · "+NODE.counts.vectors+" وکتور · "+NODE.counts.layouts+" لایه · "+NODE.counts.sections+" فصل / "+NODE.counts.tutorial_ids+" شناسهٔ درس · "+NODE.counts.dex_classes+" کلاس DEX · "+NODE.counts.catalog_rows+" ردیف کاتالوگ";
  var h7=q("#habStats");
  if(h7)h7.innerHTML="<b>شواهد امتیازدهی:</b> Habitica <code>develop@"+HAB.commit.slice(0,12)+"</code> · "+HAB.counts.sources+" فایل منبع با SHA-256 · "+HAB.counts.rules+" قاعده · "+HAB.counts.task_types+" نوع کار · "+HAB.counts.isolation_rules+" قانون ایزولاسیون";
  paintIcons();
'''
t = sub1(t, "  histRender();render();\n})();", NEW_JS + "\n  histRender();render();\n})();", "newjs7")

# ---- write template + built HTML ----
TPL_OUT.write_text(t, encoding="utf-8")
css = build_css()
js = "var GEO=" + json.dumps(payload, ensure_ascii=False, separators=(",", ":")) + ";"
ljs = "var LEARN=" + json.dumps(learn_payload, ensure_ascii=False, separators=(",", ":")) + ";"
njs = "var NODE=" + json.dumps(node_payload, ensure_ascii=False, separators=(",", ":")) + ";"
hjs = "var HAB=" + json.dumps(hab_payload, ensure_ascii=False, separators=(",", ":")) + ";"
html = (t.replace("/*__CSS__*/", css).replace("/*__GEO__*/", js)
         .replace("/*__LEARN__*/", ljs).replace("/*__NODE__*/", njs).replace("/*__HAB__*/", hjs))
for ph in ("/*__CSS__*/", "/*__GEO__*/", "/*__LEARN__*/", "/*__NODE__*/", "/*__HAB__*/"):
    if ph in html:
        raise SystemExit("placeholder not replaced: " + ph)
OUT.write_text(html, encoding="utf-8")
print(json.dumps({
    "output": str(OUT), "bytes": OUT.stat().st_size,
    "template": str(TPL_OUT), "template_bytes": TPL_OUT.stat().st_size,
    "svg_vectors": len(merged), "views": html.count("<button data-go="),
    "tabs": html.count('data-tab="'), "method": GEO["method"],
    "node_catalog_rows": NOD["counts"]["catalog_rows"],
    "habitica_rules": HAB["counts"]["rules"],
}, ensure_ascii=False, indent=1))
