#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build_exam_v12_3.py — ROLL BACK to the accepted v12.1 exam structure.

The four-model v12.2 pass was REJECTED («از بیخ ایراد داره ... پاسخبرگ رو آوردی
گذاشتی بالا کلا قاتی پاتی شده»).  This script therefore starts from the exact
v12.1 snapshot (tools/design_v12_1_template.html, commit d356963) and applies
ONLY three things:

  1. the emblem change the user explicitly asked for in the previous turn
     (ic_mimo_mascot -> ic_survey.xml in exam-hub, ic_cap in exam-result),
  2. the RTL arrow-direction fix the user asked for
     (NEXT arrowhead points LEFT, PREVIOUS/BACK arrowhead points RIGHT),
  3. a reference file recording the RTL sources + the Chinese exam repo used to
     re-check what an exam page should look like.

NOTHING else about the exam page changes: one full-width purple CONTINUE CTA,
two 48dp squares, the answer sheet / answer key as BOTTOM SHEETS (not inline),
no question-number strip above the stem, no model picker, no feedback gimmicks.
Code-first from decoded APK vectors; screenshots VISUAL_CROSSCHECK_ONLY.
"""
from __future__ import annotations
import hashlib
import json
import re
import sys
from pathlib import Path

UP = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
TOOLS, DESIGN = UP / "tools", UP / "DESIGN"
SOURCE = UP.parent / "SOURCE"
html = (TOOLS / "design_v12_1_template.html").read_text(encoding="utf-8")


def rep(old: str, new: str, label: str, count: int = 1):
    global html
    n = html.count(old)
    if n != count:
        raise SystemExit("%s matched %d times (expected %d)" % (label, n, count))
    html = html.replace(old, new, count)


# ---------------------------------------------------------------------------
# 0. decoded APK quiz illustration -> extracted vector payload
# ---------------------------------------------------------------------------
xml = (SOURCE / "res/drawable/ic_survey.xml").read_text(encoding="utf-8")
vw = float(re.search(r'android:viewportWidth="([^"]+)"', xml).group(1))
vh = float(re.search(r'android:viewportHeight="([^"]+)"', xml).group(1))
w = float(re.search(r'android:width="([^"]+)"', xml).group(1).replace("dip", ""))
h = float(re.search(r'android:height="([^"]+)"', xml).group(1).replace("dip", ""))
paths = []
for m in re.finditer(r'<path\s+([^>]*?)/>', xml, re.S):
    a = m.group(1)
    d = re.search(r'android:pathData="([^"]+)"', a)
    f = re.search(r'android:fillColor="([^"]+)"', a)
    if d:
        paths.append({"d": d.group(1), "fill": f.group(1) if f else None,
                      "alpha": None, "fillType": None})
assert len(paths) >= 20
mgeo = re.search(r'<script>var GEO=(.*?);</script>', html, re.S)
geo = json.loads(mgeo.group(1))
geo["vectors"]["ic_survey"] = {
    "source": "res/drawable/ic_survey.xml", "viewport": [vw, vh],
    "size_dp": [w, h], "paths": paths,
    "sha_bytes": hashlib.sha256(xml.encode("utf-8")).hexdigest()[:16],
}
html = (html[:mgeo.start()] + '<script>var GEO='
        + json.dumps(geo, ensure_ascii=False, separators=(",", ":")) + ';</script>'
        + html[mgeo.end():])

# ---------------------------------------------------------------------------
# 1. emblem (kept from the previous turn: the user asked for it explicitly)
# ---------------------------------------------------------------------------
rep('<div class="eh-art"><span data-icon="ic_mimo_mascot" data-size="48"></span></div>',
    '<div class="eh-art" data-code="res/drawable/ic_survey.xml · quiz_introduction_fragment.xml iv_quiz_introduction"><span data-icon="ic_survey" data-size="54"></span></div>',
    "hub emblem")
rep('<div class="rf-art"><span data-icon="ic_mimo_mascot" data-size="72"></span></div>',
    '<div class="rf-art" data-code="res/drawable/ic_cap.xml"><span data-icon="ic_cap" data-size="52" data-mono="1"></span></div>',
    "result emblem")
rep('.exv12 .eh-art{width:64px;height:64px;flex:0 0 64px;border-radius:999px;background:var(--card-pressed);display:flex;align-items:center;justify-content:center;color:var(--primary)}',
    '.exv12 .eh-art{width:68px;height:68px;flex:0 0 68px;border-radius:16px;background:var(--card-pressed);border:1px solid var(--line);display:flex;align-items:center;justify-content:center;color:var(--primary)}',
    "hub emblem frame")
rep('.exv12 .rf-art{width:104px;height:104px;margin:0 auto 10px;border-radius:999px;background:var(--card-pressed);display:flex;align-items:center;justify-content:center;color:var(--primary)}',
    '.exv12 .rf-art{width:104px;height:104px;margin:0 auto 10px;border-radius:999px;background:var(--primary);color:#fff;border:0;display:flex;align-items:center;justify-content:center}',
    "result emblem frame")

# ---------------------------------------------------------------------------
# 2. RTL ARROW DIRECTION — the actual bug the user pointed out
#
#    ic_arrow_left   path M21..H5.31..L3.325,11.115  -> arrowhead LEFT  (←)
#    ic_arrow_right  path M20.675..L14.53..H3        -> arrowhead RIGHT (→)
#    ic_arrow_back_24 path M20,11H7.83...l-8,8        -> arrowhead LEFT  (←)
#
#    RTL rule: NEXT/FORWARD points LEFT; PREVIOUS/BACK points RIGHT.
#    So the exam-run CTA must use ic_arrow_left and the prev square ic_arrow_right.
#    All other LTR-authored arrow icons are mirrored only while dir=rtl; the two
#    explicitly RTL-authored exam buttons are mirrored back when dir=ltr.
# ---------------------------------------------------------------------------
ARROW_CSS = r'''
/* v12.3 · RTL directional icons: NEXT -> left, PREVIOUS/BACK -> right.
   Sources: simplelocalize.io RTL guide / Material bidi / Saudisoft RTL checklist.
   The two exam-run arrows are authored RTL-correct in the markup (data-arrow),
   every other decoded ic_arrow_* glyph is LTR-authored and mirrored in RTL. */
[dir="rtl"] [data-icon^="ic_arrow_"]:not([data-arrow]) svg{transform:scaleX(-1)}
[dir="ltr"] [data-arrow] svg{transform:scaleX(-1)}
.exv12 .lk-cta [data-arrow] svg,.exv12 .lk-square [data-arrow] svg{display:block}
'''
rep("</style>", ARROW_CSS + "\n</style>", "RTL arrow CSS")

rep('<button class="lk-square" id="prevQ" aria-label="سؤال قبل" data-code="btn_undo · 48dp square"><span data-icon="ic_arrow_back_24" data-size="22" data-mono="1"></span></button>',
    '<button class="lk-square" id="prevQ" aria-label="سؤال قبل" data-code="btn_undo · 48dp square"><span data-icon="ic_arrow_right" data-arrow="prev" data-size="22" data-mono="1"></span></button>',
    "prev arrow -> right")
rep('<button class="lk-cta" id="nextQ" data-code="btn_continue_big / btn_submit · lesson_continue=Continue · lesson_submit=Submit"><b id="nextQLabel">ادامه</b><span data-icon="ic_arrow_right" data-size="18" data-mono="1"></span></button>',
    '<button class="lk-cta" id="nextQ" data-code="btn_continue_big / btn_submit · lesson_continue=Continue · lesson_submit=Submit"><b id="nextQLabel">ادامه</b><span data-icon="ic_arrow_left" data-arrow="next" data-size="18" data-mono="1"></span></button>',
    "next arrow -> left")
# the exam-result back button is a BACK arrow: in RTL it must point RIGHT.
rep('<button class="ln-x" data-nav="exam-hub" aria-label="بازگشت"><span data-icon="ic_arrow_back_24" data-size="22" data-mono="1"></span></button>',
    '<button class="ln-x" data-nav="exam-hub" aria-label="بازگشت"><span data-icon="ic_arrow_right" data-arrow="back" data-size="22" data-mono="1"></span></button>',
    "result back arrow -> right")

# ---------------------------------------------------------------------------
# 3. chrome text only (review document, NOT inside the phone UI)
# ---------------------------------------------------------------------------
rep('<title>طرح رابط کاربری v12 — سطوح آزمون بر اساس lesson_interactive میمو (Design Review)</title>',
    '<title>طرح رابط کاربری v12.3 — بازگشت به ساختار تأییدشدهٔ صفحهٔ آزمون + فلشهای RTL (Design Review)</title>',
    "title")
rep('<h1>طرح رابط کاربری — دور دوازدهم <span class="ver">DESIGN v12 · REVIEW</span></h1>',
    '<h1>طرح رابط کاربری — دور دوازدهم <span class="ver">DESIGN v12.3 · REVIEW</span></h1>',
    "h1")
rep('⚠️ این <b>طرح دور دوازدهم v12</b> است، نه محصول.',
    '⚠️ این <b>طرح دور دوازدهم v12.3</b> است، نه محصول.', "footer lead")
rep('در دور دوازدهم سطوح آزمون با معماری واقعی صفحهٔ درس/کوییز میمو هماهنگ شدند.',
    'در دور دوازدهم سطوح آزمون با معماری واقعی صفحهٔ درس/کوییز میمو هماهنگ شدند. '
    '<b>v12.3:</b> چهارمدل v12.2 بهدلیل قاتیشدن پاسخبرگ با بدنهٔ سؤال <b>رد و به همان ساختار v12.1 برگردانده شد</b>؛ '
    'پاسخبرگ و پاسخنامه همچنان <b>کشوی پایین صفحه</b>اند، و فلشها در RTL اصلاح شدند (بعدی ←، قبلی/بازگشت →).',
    "header paragraph rollback note")

# sanity: the rejected v12.2 constructs must not exist
for bad in ('id="ksStrip"', 'class="mf" data-exmodel=', 'modelpick', 'EXAM_PAGE_MODELS'):
    assert bad not in html, bad
assert html.count('class="lk-cta"') == 1
assert html.count('class="lk-square"') == 2
assert 'id="paletteSheet"' in html and 'id="keySheet"' in html

# ---------------------------------------------------------------------------
# 4. reference file: what was checked, what was rejected, why
# ---------------------------------------------------------------------------
REFS = {
    "round": "v12.3",
    "decision": "REJECT v12.2 four-model exam-page redesign; ROLL BACK to the v12.1 exam-run structure (commit d356963), keep only the emblem change + RTL arrow fix",
    "user_feedback": "اون ساختار قبل از تغییرات صفحه ازمون ... اون رفرنس خوبیه / پاسخبرگ رو آوردی گذاشتی بالا کلا قاتی پاتی شده / بعدی نوک پیکان باید به سمت چپ باشه برای قبلی به سمت راست",
    "reference_of_record": {
        "file": "tools/design_v12_1_template.html",
        "commit": "d356963",
        "exam_run": "chapter_toolbar 52dp (X | title+6dp progress | timer | flag) → ScrollView question stem + 4 choice_list_item cards → feedback bottom sheet → quiet tool chips → ONE full-width purple CTA + two 48dp squares + lesson_skip",
        "answer_sheet": "BOTTOM SHEET #paletteSheet opened from #answerSheetBtn or the flag button — never inline above the question",
        "answer_key": "BOTTOM SHEET #keySheet with keyTestSheet / keyDescSheet, per-kind policy; never mixed into the question body",
    },
    "what_was_wrong_in_v12_2": [
        "a 20-bubble inline answer-sheet card was inserted ABOVE the stem, between the step row and the subject chip — it crowded and confused the question body",
        "four swapped footers and a quick 4-bubble row duplicated the option cards and made the page incoherent",
        "the model picker and model badges added review scaffolding to a page that was already accepted",
        "directional arrows stayed LTR: NEXT pointed right, PREVIOUS/BACK pointed left",
    ],
    "rtl_arrow_rule": {
        "statement": "In an RTL (Persian/Arabic) interface NEXT/FORWARD points LEFT (←) and PREVIOUS/BACK points RIGHT (→)",
        "sources": [
            "https://simplelocalize.io/blog/posts/rtl-design-guide-developers/",
            "https://localization.saudisoft.com/rtl-design/",
            "https://www.codestan.com/insights/ux-design-tips-arabic-rtl-2026",
            "https://www.shaheermalik.com/blog/arabic-website-design-rtl",
        ],
        "decoded_vectors": {
            "ic_arrow_left": "M21,11.25H5.31...L3.325,11.115 -> arrowhead LEFT",
            "ic_arrow_right": "M20.675,11.115L14.53,4.97...H3 -> arrowhead RIGHT",
            "ic_arrow_back_24": "M20,11H7.83...l-8,8 -> arrowhead LEFT",
        },
        "applied": {
            "nextQ": "ic_arrow_right -> ic_arrow_left (data-arrow=next)",
            "prevQ": "ic_arrow_back_24 -> ic_arrow_right (data-arrow=prev)",
            "exam-result back": "ic_arrow_back_24 -> ic_arrow_right (data-arrow=back)",
            "all_other_arrows": "[dir=rtl] mirrors LTR-authored ic_arrow_* icons; [dir=ltr] mirrors the three explicitly RTL-authored ones",
        },
    },
    "chinese_repo_crosscheck": {
        "repos": ["https://github.com/mindskip/xzs", "https://github.com/iiSee/uexam"],
        "name": "学之思在线考试系统 (xzs / uexam)",
        "file_read": "source/vue/xzs-student/src/views/exam/paper/do.vue",
        "findings": [
            "the answering page keeps a CLEAN question body: el-card per question, QuestionEdit for the options",
            "question-number tags + 剩余时间 (remaining time) live in a separate compact sticky header row, NOT as a big card inside the question body",
            "one primary 提交 (Submit) button at the end of the paper, plus 取消",
            "answer / 解析 / correct answer are shown AFTER submission in read.vue and QuestionAnswerShow.vue, and in 错题本 (wrong-question book) — not during the exam",
        ],
        "conclusion": "confirms the v12.1 shape: answer sheet and answer key are separate sheets/panels, the question body stays uncluttered, and correctness is revealed after the exam",
        "usage": "UNDERSTANDING / cross-check only — no code, assets or layout copied into this design prototype",
    },
    "sources_policy": "decoded APK resources remain the source of truth for the Mimo skin; web + Chinese repo are cross-checks only; screenshots VISUAL_CROSSCHECK_ONLY",
}
(UP / "DESIGN/EXAM_PAGE_REFERENCES.json").write_text(
    json.dumps(REFS, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

evp = DESIGN / "EXAM_UI_CODE_EVIDENCE.json"
ev = json.loads(evp.read_text(encoding="utf-8"))
ev["v12_3_rollback"] = {
    "status": "APPLIED — v12.2 four-model redesign rejected and reverted",
    "reference": "tools/design_v12_1_template.html @ d356963",
    "reference_file": "DESIGN/EXAM_PAGE_REFERENCES.json",
    "arrow_fix": "next=ic_arrow_left (left), prev/back=ic_arrow_right (right), RTL mirroring CSS",
    "emblem": "ic_survey (hub) / ic_cap (result)",
}
evp.write_text(json.dumps(ev, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

(TOOLS / "design_v12_3_template.html").write_text(html, encoding="utf-8")
(DESIGN / "index.html").write_text(html, encoding="utf-8")
print(json.dumps({
    "output": str(DESIGN / "index.html"), "bytes": len(html.encode("utf-8")),
    "reverted_to": "d356963 / design_v12_1_template.html",
    "single_cta": html.count('class="lk-cta"'),
    "inline_strip_removed": 'id="ksStrip"' not in html,
    "next_arrow": 'data-arrow="next"' in html and 'id="nextQ"' in html,
    "prev_arrow": 'data-arrow="prev"' in html,
    "geo_vectors": len(geo["vectors"]),
    "references": str(UP / "DESIGN/EXAM_PAGE_REFERENCES.json"),
}, ensure_ascii=False, indent=2))
