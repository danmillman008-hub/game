#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build_exam_models_v12_2.py — FOUR distinct exam-page models + a new hub emblem.

Runs on tools/design_v12_1_template.html.  Design/prototype only, no product code.

WHY four models
---------------
One exam-run sheet cannot serve both a real Konkur sitting and a Mimo practice
lesson.  Konkur: fixed 270 min, you fill an answer sheet AS YOU GO, correctness is
never revealed during the exam, the answer key is published afterwards, and the
prev/next question pair + skip/mark are the primary navigation.  Mimo practice:
one full-width CONTINUE/SUBMIT CTA, immediate green/red feedback with a topic
explanation, AI help.  Analytical exams want BOTH feedback and navigation.
Descriptive exams have no 4 options at all (تعویض سوال / تصحیح دستی).

MODELS (selected automatically by the exam card's data-kind; previewable from the
review panel outside the phone):
  konkur      comprehensive / timed / review — Konkur answer-sheet strip + quick 4
              bubbles (Mimo practice sp-opts grammar) + real prev/next + timer +
              end; NO feedback, key only when policy allows.
  practice    normal — exact Mimo lesson_interactive: one full-width purple
              CONTINUE/SUBMIT CTA, 48dp squares, feedback bottom sheet, AI, skip.
  analytical  analytical — feedback + inline تحلیل card + prev/next squares +
              answer key during exam.
  descriptive descriptive — written answer area instead of options, تعویض سوال /
              تصحیح دستی, prev/next.

CODE-FIRST evidence (screenshots VISUAL_CROSSCHECK_ONLY):
  chapter_toolbar.xml / lesson_interactive_multiplechoice_fragment.xml /
  choice_list_item.xml / interaction_keyboard_view.xml / run_button_view.xml /
  lesson_interactive_feedback_bottom_sheet_dialog.xml / quiz_introduction_fragment.xml
  practice sp-opts grid = DESIGN prototype's section-practice (4 option buttons)
  ic_survey.xml = the APK's real quiz illustration (quiz_introduction_fragment.xml)
  strings: lesson_continue / lesson_submit / lesson_skip / continue_next
"""
from __future__ import annotations
import hashlib
import json
import re
import sys
from pathlib import Path

UP = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
TOOLS = UP / "tools"
DESIGN = UP / "DESIGN"
SOURCE = UP.parent / "SOURCE"          # /home/user/game/mimo-ui/SOURCE
html = (TOOLS / "design_v12_1_template.html").read_text(encoding="utf-8")


def rep(old: str, new: str, label: str, count: int = 1):
    global html
    n = html.count(old)
    if n != count:
        raise SystemExit("%s matched %d times (expected %d)" % (label, n, count))
    html = html.replace(old, new, count)


# ===========================================================================
# 0. add the APK's real quiz illustration to the extracted vector payload
# ===========================================================================
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
                      "alpha": None, "fillType": (re.search(r'android:fillType="([^"]+)"', a).group(1)
                                                  if 'android:fillType' in a else None)})
assert paths
survey_vec = {"source": "res/drawable/ic_survey.xml", "viewport": [vw, vh],
              "size_dp": [w, h], "paths": paths,
              "sha_bytes": hashlib.sha256(xml.encode("utf-8")).hexdigest()[:16]}
mgeo = re.search(r'<script>var GEO=(.*?);</script>', html, re.S)
geo = json.loads(mgeo.group(1))
geo["vectors"]["ic_survey"] = survey_vec
html = html[:mgeo.start()] + '<script>var GEO=' + json.dumps(geo, ensure_ascii=False, separators=(",", ":")) + ';</script>' + html[mgeo.end():]

# ===========================================================================
# 1. the emblem: Mimo mascot -> real APK quiz illustration / graduation cap
# ===========================================================================
rep('<div class="eh-art"><span data-icon="ic_mimo_mascot" data-size="48"></span></div>',
    '<div class="eh-art" data-code="res/drawable/ic_survey.xml · quiz_introduction_fragment.xml iv_quiz_introduction"><span data-icon="ic_survey" data-size="54"></span></div>',
    "hub emblem")
rep('<div class="rf-art"><span data-icon="ic_mimo_mascot" data-size="72"></span></div>',
    '<div class="rf-art" data-code="res/drawable/ic_cap.xml · مدل پایان دوره"><span data-icon="ic_cap" data-size="52" data-mono="1"></span></div>',
    "result emblem")
_exh = html.split('<section class="screen exv12" data-screen="exam-hub"')[1].split("</section>")[0]
_exr = html.split('<section class="screen exv12" data-screen="exam-result"')[1].split("</section>")[0]
assert 'data-icon="ic_mimo_mascot"' not in _exh and 'data-icon="ic_mimo_mascot"' not in _exr

# ===========================================================================
# 2. CSS for the four models + emblem
# ===========================================================================
CSS = r'''
/* ---- v12.2 · FOUR exam-page models ---- */
.exv12 .eh-art{width:68px;height:68px;flex:0 0 68px;border-radius:16px;background:var(--card-pressed);border:1px solid var(--line)}
.exv12 .rf-art{background:var(--primary);color:#fff;border:0}
.exv12 .ln .ln-badge{font:700 9px/1 Tahoma,system-ui,sans-serif;color:var(--primary);background:var(--card-pressed);border-radius:999px;padding:3px 7px;white-space:nowrap}
.exv12 .lb-mode{display:flex;align-items:center;justify-content:space-between;gap:8px;margin:0 0 12px}
.exv12 .lb-mode .mb{font:700 11px/1 Tahoma,system-ui,sans-serif;color:#fff;background:var(--primary);border-radius:999px;padding:5px 10px}
.exv12 .lb-mode .mc{font:400 10px/1.3 Tahoma,system-ui,sans-serif;color:var(--text-weak)}
/* Konkur answer sheet, kept INLINE (not hidden behind a button) */
.exv12 .mk-strip-wrap{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:9px 10px;margin:0 0 14px}
.exv12 .mk-strip-head{display:flex;justify-content:space-between;align-items:center;font:700 11px/1.3 Tahoma,system-ui,sans-serif;color:var(--text);margin:0 0 8px}
.exv12 .mk-strip-head small{font:400 10px/1 Tahoma,system-ui,sans-serif;color:var(--text-weak)}
.exv12 .mk-strip{display:flex;gap:5px;overflow-x:auto;padding-bottom:3px;scrollbar-width:thin}
.exv12 .mk-strip button{width:30px;height:30px;flex:0 0 30px;border:1px solid var(--line);border-radius:8px;background:var(--card);color:var(--text-weak);font:700 11px/1 Tahoma,system-ui,sans-serif;padding:0}
.exv12 .mk-strip button.done{background:var(--progress-bg);border-color:var(--progress);color:var(--text)}
.exv12 .mk-strip button.cur{border:2px solid var(--primary);background:var(--card-pressed);color:var(--primary)}
.exv12 .mk-strip button.flag{border-color:var(--yellow);box-shadow:inset 0 -3px 0 var(--yellow)}
.exv12 .mk-quick-label{font:700 11px/1.3 Tahoma,system-ui,sans-serif;color:var(--text-weak);margin:14px 0 7px}
.exv12 .mk-quick{display:grid;grid-template-columns:repeat(4,1fr);gap:7px}
.exv12 .mk-quick button{height:44px;border:1px solid var(--line2);border-radius:12px;background:var(--card);color:var(--text-weak);font:700 15px/1 Tahoma,system-ui,sans-serif}
.exv12 .mk-quick button:hover{border-color:var(--primary)}
.exv12 .mk-quick button.on{background:var(--primary);border-color:var(--primary);color:#fff;box-shadow:0 3px 0 var(--primary-hi)}
/* Analytical inline analysis */
.exv12 .ma-analysis{background:var(--card);border:1px solid var(--line);border-right:4px solid var(--blue);border-radius:12px;padding:11px 12px;margin:14px 0 0}
.exv12 .ma-analysis[hidden]{display:none}
.exv12 .ma-analysis b{font:700 12px/1.4 Tahoma,system-ui,sans-serif;color:var(--text)}
.exv12 .ma-analysis .ar{display:flex;justify-content:space-between;font:400 11px/1.6 Tahoma,system-ui,sans-serif;color:var(--text-weak);border-bottom:1px dashed var(--line);padding:3px 0}
.exv12 .ma-analysis .ar:last-child{border:0}
.exv12 .ma-analysis .ar span:last-child{font-weight:700;color:var(--text)}
/* Descriptive written answer */
.exv12 .md-answer{margin:14px 0 0}
.exv12 .md-answer textarea{width:100%;min-height:120px;resize:vertical;border:1px solid var(--line);border-radius:12px;background:var(--card);color:var(--text);padding:12px;font:400 14px/1.8 Tahoma,system-ui,sans-serif}
.exv12 .md-answer .md-count{font:400 10px/1.3 Tahoma,system-ui,sans-serif;color:var(--text-weak);margin-top:4px}
.exv12[data-exmodel-active="descriptive"] #exChoices{display:none}
.exv12[data-exmodel-active="descriptive"] .lb-hint{display:none}
/* one interaction keyboard, four model-specific footers */
.exv12 .mf{display:flex;flex-direction:column;gap:6px}
.exv12 .mf[hidden]{display:none!important}
.exv12 .mf-label{text-align:center;font:400 10px/1.2 Tahoma,system-ui,sans-serif;color:var(--text-weak)}
.exv12 .md-actions{display:flex;gap:6px;justify-content:center}
.exv12 .lk-chip{border:1px solid var(--line);background:var(--card);color:var(--text-weak);border-radius:999px;padding:5px 10px;font:400 10px/1 Tahoma,system-ui,sans-serif}
.exv12 .lk-chip:hover{border-color:var(--primary);color:var(--primary)}
/* review panel model picker (outside the phone) */
.modelpick{display:flex;flex-direction:column;gap:5px;margin:4px 0 6px}
.modelpick button{text-align:right;border:1px solid var(--line2);background:var(--card);color:var(--text);border-radius:8px;padding:6px 9px;font-size:11px;cursor:pointer}
.modelpick button:hover{border-color:var(--primary);color:var(--primary)}
.modelpick button.on{background:var(--primary);border-color:var(--primary);color:#fff}
'''
rep("</style>", CSS + "\n</style>", "inject v12.2 CSS")

# ===========================================================================
# 3. one descriptive exam card gets its own model
# ===========================================================================
rep('<div class="nodek" data-exam="آزمون تشریحی" data-kind="normal">',
    '<div class="nodek" data-exam="آزمون تشریحی" data-kind="descriptive">',
    "descriptive kind")

# ===========================================================================
# 4. exam-run BODY: model badge + model-specific blocks
# ===========================================================================
rep('''          <div class="lb-step"><span id="examStep">سؤال ۱ از ۲۰</span><span id="timerStateText">زمان تنظیم نشده</span></div>
          <div class="lb-subject"''',
'''          <div class="lb-step"><span id="examStep">سؤال ۱ از ۲۰</span><span id="timerStateText">زمان تنظیم نشده</span></div>
          <div class="lb-mode" data-code="model selector badge — functional state, not a design note">
            <span class="mb" id="examModelBadge">زمان خالص کنکور</span>
            <span class="mc" id="answeredCount">۰ از ۲۰ پاسخ داده شده</span>
          </div>
          <!-- MODEL K: real Konkur answer sheet, inline and always visible -->
          <div class="mk-strip-wrap" data-exmodel="konkur" data-code="Konkur پاسخبرگ · answer sheet filled during the exam; no correctness revealed">
            <div class="mk-strip-head"><span>پاسخبرگ</span><small>روی شماره بزنید تا به آن سؤال بروید</small></div>
            <div class="mk-strip" id="ksStrip"></div>
          </div>
          <div class="lb-subject"''', "model badge + K strip")

rep('''          <div id="examFinished"></div>
          <div class="hint" id="policyHint" hidden></div>''',
'''          <!-- MODEL K: quick 4-option bubbles, from Mimo section-practice sp-opts grid -->
          <div class="mk-quick-label" data-exmodel="konkur">ثبت سریع پاسخ در پاسخبرگ</div>
          <div class="mk-quick" id="ksQuick" data-exmodel="konkur" data-code="section-practice sp-opts · 4 equal option buttons · answer recorded, not graded">
            <button type="button" data-o="1">۱</button><button type="button" data-o="2">۲</button>
            <button type="button" data-o="3">۳</button><button type="button" data-o="4">۴</button>
          </div>
          <!-- MODEL A: inline analytical panel (بررسی پاسخ + نقشهٔ ضعف) -->
          <div class="ma-analysis" id="maAnalysis" data-exmodel="analytical" data-code="analytical exam · شبیهسازی اگر غلطها نزده میذاشتی · نقشهٔ ضعف">
            <b>تحلیل زندهٔ این سؤال</b>
            <div class="ar"><span>درصد پاسخگویی تا اینجا</span><span>۶۸٪</span></div>
            <div class="ar"><span>اگر غلطها نزده میذاشتی</span><span>۷۴٪</span></div>
            <div class="ar"><span>ضعف مبحث</span><span>زیست · سمها</span></div>
            <div class="ar"><span>میانگین زمان هر سؤال</span><span>۴۲ ثانیه</span></div>
          </div>
          <!-- MODEL D: written answer instead of four options -->
          <div class="md-answer" data-exmodel="descriptive" data-code="آزمون تشریحی · تعویض سوال · تصحیح دستی">
            <textarea id="mdAnswer" placeholder="پاسخ تشریحی خود را بنویسید…"></textarea>
            <div class="md-count" id="mdCount">۰ واژه</div>
          </div>
          <div id="examFinished"></div>
          <div class="hint" id="policyHint" hidden></div>''', "model body blocks")

# ===========================================================================
# 5. exam-run FOOTER: four interaction-keyboard variants
# ===========================================================================
OLD_FOOT = '''        <!-- interaction_keyboard_view.xml / run_button_view.xml : NO prev/next pill pair -->
        <div class="lk" data-code="interaction_keyboard_view.xml · interaction_keyboard_height=68dp · run_button_view.xml">
          <div class="lk-row">
            <button class="lk-square" id="prevQ" aria-label="سؤال قبل" data-code="btn_undo · 48dp square"><span data-icon="ic_arrow_back_24" data-size="22" data-mono="1"></span></button>
            <button class="lk-square" id="markQ" aria-label="علامتگذاری" data-code="btn_reset · 48dp square"><span data-icon="bookmark" data-size="20" data-mono="1"></span></button>
            <button class="lk-cta" id="nextQ" data-code="btn_continue_big / btn_submit · lesson_continue=Continue · lesson_submit=Submit"><b id="nextQLabel">ادامه</b><span data-icon="ic_arrow_right" data-size="18" data-mono="1"></span></button>
          </div>
          <button class="lk-skip" id="skipQ" data-code="lesson_skip=Skip">رد کردن سؤال</button>
        </div>'''
NEW_FOOT = r'''        <!-- interaction_keyboard_view.xml / run_button_view.xml — FOUR model footers, ONE visible at a time -->
        <div class="lk" data-code="interaction_keyboard_view.xml · interaction_keyboard_height=68dp · run_button_view.xml">

          <!-- MODEL K · کنکوری / زمان خالص: prev + full-width NEXT + mark; no feedback -->
          <div class="mf" data-exmodel="konkur" data-code="Konkur navigation · سؤال قبل/بعد are the primary actions · answer key only per policy">
            <div class="lk-row">
              <button class="lk-square" id="prevK" aria-label="سؤال قبل"><span data-icon="ic_arrow_back_24" data-size="22" data-mono="1"></span></button>
              <button class="lk-cta" id="nextK" data-code="btn_continue_big · lesson_continue=Continue · continue_next"><b>سؤال بعد</b><span data-icon="ic_arrow_right" data-size="18" data-mono="1"></span></button>
              <button class="lk-square" id="markK" aria-label="علامتگذاری"><span data-icon="bookmark" data-size="20" data-mono="1"></span></button>
            </div>
            <button class="lk-skip" id="skipK" data-code="lesson_skip=Skip">رد کردن سؤال و رفتن به بعدی</button>
          </div>

          <!-- MODEL P · تمرینی میمو: one CTA (SUBMIT -> feedback -> CONTINUE) -->
          <div class="mf" data-exmodel="practice" hidden data-code="lesson_interactive_multiplechoice_fragment.xml · btn_submit / btn_continue_big">
            <div class="lk-row">
              <button class="lk-square" id="prevQ" aria-label="سؤال قبل" data-code="btn_undo · 48dp square"><span data-icon="ic_arrow_back_24" data-size="22" data-mono="1"></span></button>
              <button class="lk-square" id="markQ" aria-label="علامتگذاری" data-code="btn_reset · 48dp square"><span data-icon="bookmark" data-size="20" data-mono="1"></span></button>
              <button class="lk-cta" id="nextQ" data-code="btn_continue_big / btn_submit · lesson_continue=Continue · lesson_submit=Submit"><b id="nextQLabel">ادامه</b><span data-icon="ic_arrow_right" data-size="18" data-mono="1"></span></button>
            </div>
            <button class="lk-skip" id="skipQ" data-code="lesson_skip=Skip">رد کردن سؤال</button>
          </div>

          <!-- MODEL A · تحلیلی: feedback CTA + BOTH prev/next squares + live analysis -->
          <div class="mf" data-exmodel="analytical" hidden data-code="analytical: feedback matters, so keep btn_submit; navigation still available">
            <div class="lk-row">
              <button class="lk-square" id="prevA" aria-label="سؤال قبل"><span data-icon="ic_arrow_back_24" data-size="22" data-mono="1"></span></button>
              <button class="lk-cta" id="submitA" data-code="btn_submit · lesson_submit=Submit"><b id="submitALabel">بررسی پاسخ</b><span data-icon="ic_check_white" data-size="18" data-mono="1"></span></button>
              <button class="lk-square" id="nextA" aria-label="سؤال بعد"><span data-icon="ic_arrow_right" data-size="20" data-mono="1"></span></button>
            </div>
            <button class="lk-skip" id="toggleAnalysis">نمایش / پنهان کردن تحلیل</button>
          </div>

          <!-- MODEL D · تشریحی: written answer, تعویض سوال / تصحیح دستی -->
          <div class="mf" data-exmodel="descriptive" hidden data-code="آزمون تشریحی · تعویض سوال · تصحیح دستی (section ۷ template)">
            <div class="lk-row">
              <button class="lk-square" id="prevD" aria-label="سؤال قبل"><span data-icon="ic_arrow_back_24" data-size="22" data-mono="1"></span></button>
              <button class="lk-cta" id="saveD"><b>ثبت پاسخ</b><span data-icon="ic_task_completed" data-size="18" data-mono="1"></span></button>
              <button class="lk-square" id="nextD" aria-label="سؤال بعد"><span data-icon="ic_arrow_right" data-size="20" data-mono="1"></span></button>
            </div>
            <div class="md-actions"><button class="lk-chip" id="swapD">تعویض سوال</button><button class="lk-chip" id="gradeD">تصحیح دستی</button></div>
          </div>
        </div>'''
rep(OLD_FOOT, NEW_FOOT, "four footers")

# ===========================================================================
# 6. review-panel model picker + chrome text
# ===========================================================================
rep('    <h3>دور یازدهم', '''    <h3>مدلهای صفحهٔ اجرای آزمون (v12.2)</h3>
    <div class="modelpick" data-open-model-group>
      <button data-open-model="konkur" class="on">۱ · کنکوری / زمان خالص (جامع، زماندار، جمع بندی)</button>
      <button data-open-model="practice">۲ · تمرینی میمو (تکدرسی، مبحثی، مرور)</button>
      <button data-open-model="analytical">۳ · تحلیلی (بررسی پاسخ + تحلیل زنده)</button>
      <button data-open-model="descriptive">۴ · تشریحی (پاسخ نوشتاری، تعویض سوال)</button>
    </div>
    <ul>
      <li>مدل ۱: <b>پاسخبرگ درونصفحهای</b> (۲۰ حباب، پرش مستقیم) + ردیف ۴گانهٔ ثبت سریع از <code>section-practice sp-opts</code> میمو + <b>سؤال قبل/بعد</b> بعنوان ناوبری اصلی + تایمر؛ <b>هیچ اعلام صحت حین آزمون</b>، پاسخنامه فقط طبق policy.</li>
      <li>مدل ۲: دقیقاً <code>lesson_interactive</code> میمو — یک CTA بنفش تمامعرض <code>btn_submit</code> ← پنل feedback سبز/قرمز ← <code>btn_continue_big</code>.</li>
      <li>مدل ۳: همان بررسی پاسخ + کارت تحلیل زنده + هر دو مربع قبل/بعد + پاسخنامه حین آزمون.</li>
      <li>مدل ۴: بدون ۴ گزینه؛ متن آزاد، <code>تعویض سوال</code> و <code>تصحیح دستی</code>.</li>
      <li>شواهد کامل: <code>DESIGN/EXAM_PAGE_MODELS.json</code>. لوگوی هاب = <code>ic_survey.xml</code> (تصویرسازی واقعی کوییز میمو)، لوگوی نتیجه = <code>ic_cap</code>؛ ماسکوت میمو حذف شد.</li>
    </ul>
    <h3>دور یازدهم''', "model picker")
rep("<title>طرح رابط کاربری v12 — سطوح آزمون بر اساس lesson_interactive میمو (Design Review)</title>",
    "<title>طرح رابط کاربری v12.2 — چهار مدل صفحهٔ اجرای آزمون (Design Review)</title>", "title")
rep("<h1>طرح رابط کاربری — دور دوازدهم <span class=\"ver\">DESIGN v12 · REVIEW</span></h1>",
    "<h1>طرح رابط کاربری — دور دوازدهم <span class=\"ver\">DESIGN v12.2 · REVIEW</span></h1>", "h1")
rep("⚠️ این <b>طرح دور دوازدهم v12</b> است، نه محصول.",
    "⚠️ این <b>طرح دور دوازدهم v12.2</b> است، نه محصول.", "footer lead")
rep("دو دکمهٔ هموزن «سؤال قبل / سؤال بعد» و نوار ۷ دکمهای حذف شدند؛ پاسخبرگ، پاسخنامه، AI و تایمر در ردیف چیپهای آرام و پاسخنامهٔ تشریحی بهصورت پنل feedback میمو نمایش داده میشوند.",
    "<b>v12.2:</b> صفحهٔ اجرای آزمون <b>چهار مدل مجزا</b> دارد: ① کنکوری/زمان خالص (پاسخبرگ درونصفحهای ۲۰ حباب + «سؤال قبل/بعد» بعنوان ناوبری اصلی + بدون اعلام صحت)، "
    "② تمرینی میمو (یک CTA بنفش «بررسی پاسخ ← feedback ← ادامه»)، ③ تحلیلی (همان بررسی پاسخ + کارت تحلیل زنده + هر دو جهت ناوبری)، "
    "④ تشریحی (پاسخ نوشتاری + «تعویض سوال»/«تصحیح دستی»). لوگوی هاب به تصویرسازی واقعی <code>ic_survey</code> میمو تغییر کرد. "
    "اسکرینشاتها فقط چک بصری.", "header paragraph four models")

# ===========================================================================
# 7. JS: models, policy, navigation, answer sheet
# ===========================================================================
rep('''    analytical:{label:"تحلیلی · پاسخبرگ + پاسخنامه حین و بعد",during:true,keyDuring:true}
  };''',
'''    analytical:{label:"تحلیلی · پاسخبرگ + پاسخنامه حین و بعد",during:true,keyDuring:true},
    descriptive:{label:"تشریحی · تعویض سوال · تصحیح دستی",during:true,keyDuring:false}
  };''', "policy descriptive")

rep('''    QI=0;MARKS={};q("#examFinished").innerHTML="";resetOptions();renderQuestion();
    T.state="idle";clearInterval(T.timer);T.timer=null;
    applyPolicy();go("exam-run");''',
'''    QI=0;MARKS={};ANSWERS={};q("#examFinished").innerHTML="";resetOptions();renderQuestion();
    T.state="idle";clearInterval(T.timer);T.timer=null;
    applyPolicy();applyExamModel(EXAM_KIND);go("exam-run");''', "openExam model")

rep('var QTOTAL=QBANK.length,QI=0,QCHECKED=false,MARKS={};',
    'var QTOTAL=QBANK.length,QI=0,QCHECKED=false,MARKS={},ANSWERS={};', "answers state")

rep('''    q("#markQ").classList.toggle("marked",!!MARKS[QI]);
  }''',
'''    qa("#markQ,#markK").forEach(function(b){b.classList.toggle("marked",!!MARKS[QI])});
    q("#mdAnswer").value=(ANSWERS[QI]&&ANSWERS[QI].text)||"";
    q("#mdCount").textContent=fa(((ANSWERS[QI]&&ANSWERS[QI].text)||"").trim().split(/\\s+/).filter(Boolean).length)+" واژه";
    syncQuick();updateStrip();
  }''', "renderQuestion model sync")

rep('''  q("#nextQ").addEventListener("click",function(){
    var chosen=q(".opt.on");
    if(chosen&&!QCHECKED){
      var item=QBANK[QI%QBANK.length];
      var ok=+chosen.dataset.opt-1===item.ok;
      QCHECKED=true;
      chosen.classList.remove("on");chosen.classList.add(ok?"correct":"wrong");
      var fb=q("#exFeedback");fb.classList.toggle("bad",!ok);fb.hidden=false;
      q("#exFeedbackTitle").textContent=ok?"پاسخ درست است":"پاسخ نادرست است";
      q("#exFeedbackText").textContent=item.expl;
      q("#nextQLabel").textContent="ادامه";toast(ok?"درست ✔ پاسخنامهٔ تشریحی نشان داده شد":"نادرست ✕ توضیح مبحث نشان داده شد");
      return;
    }
    QI=Math.min(QTOTAL-1,QI+1);renderQuestion();toast("سؤال بعدی · "+fa(QI+1)+" از "+fa(QTOTAL));
  });
  q("#prevQ").addEventListener("click",function(){QI=Math.max(0,QI-1);renderQuestion();toast("سؤال قبل · "+fa(QI+1)+" از "+fa(QTOTAL))});
  q("#skipQ").addEventListener("click",function(){QI=Math.min(QTOTAL-1,QI+1);renderQuestion();toast("سؤال رد شد")});
  q("#markQ").addEventListener("click",function(){
    if(MARKS[QI])delete MARKS[QI];else MARKS[QI]=true;
    q("#markQ").classList.toggle("marked",!!MARKS[QI]);
    toast(MARKS[QI]?"سؤال علامتگذاری شد":"علامت برداشته شد");
  });
  renderQuestion();''',
r'''  function submitOrContinue(){
    var chosen=q(".opt.on");
    if(chosen&&!QCHECKED){
      var item=QBANK[QI%QBANK.length];
      var ok=+chosen.dataset.opt-1===item.ok;
      QCHECKED=true;
      chosen.classList.remove("on");chosen.classList.add(ok?"correct":"wrong");
      var fb=q("#exFeedback");fb.classList.toggle("bad",!ok);fb.hidden=false;
      q("#exFeedbackTitle").textContent=ok?"پاسخ درست است":"پاسخ نادرست است";
      q("#exFeedbackText").textContent=item.expl;
      q("#nextQLabel").textContent="ادامه";q("#submitALabel").textContent="ادامه";
      toast(ok?"درست ✔ پاسخنامهٔ تشریحی نشان داده شد":"نادرست ✕ توضیح مبحث نشان داده شد");
      return;
    }
    goNext();
  }
  q("#nextQ").addEventListener("click",submitOrContinue);
  q("#submitA").addEventListener("click",submitOrContinue);
  q("#prevQ").addEventListener("click",goPrev);
  q("#skipQ").addEventListener("click",goNext);
  q("#markQ").addEventListener("click",toggleMark);
  renderQuestion();

  /* ============ v12.2 · FOUR exam-page models ============ */
  var MODELS={
    konkur:{title:"زمان خالص کنکور",badge:"کنکوری",hint:"پاسخبرگ حین آزمون · بدون اعلام صحت",feedback:false,nav:true},
    practice:{title:"تمرین میمو",badge:"تمرینی",hint:"یک CTA · بررسی پاسخ → ادامه",feedback:true,nav:false},
    analytical:{title:"تحلیلی",badge:"تحلیلی",hint:"بررسی پاسخ + تحلیل زنده",feedback:true,nav:true},
    descriptive:{title:"تشریحی",badge:"تشریحی",hint:"پاسخ نوشتاری · تعویض سوال",feedback:false,nav:true}
  };
  var MODEL_BY_KIND={comprehensive:"konkur",timed:"konkur",review:"konkur",
                     normal:"practice",analytical:"analytical",descriptive:"descriptive"};
  var EXAM_KIND_BY_MODEL={konkur:"comprehensive",practice:"normal",analytical:"analytical",descriptive:"descriptive"};
  var EXAM_TITLE_BY_MODEL={konkur:"آزمون جامع کنکور",practice:"آزمون تکدرسی زیست",
                           analytical:"آزمون تحلیلی زیست",descriptive:"آزمون تشریحی"};
  var CURRENT_MODEL="konkur";
  function applyExamModel(kind){
    CURRENT_MODEL=MODEL_BY_KIND[kind]||"practice";
    var run=q('[data-screen="exam-run"]');
    run.dataset.exmodelActive=CURRENT_MODEL;
    qa('[data-screen="exam-run"] [data-exmodel]').forEach(function(el){
      el.hidden=el.dataset.exmodel.split(" ").indexOf(CURRENT_MODEL)<0;
    });
    var m=MODELS[CURRENT_MODEL];
    q("#examModelBadge").textContent=m.badge+" · "+m.title;
    var badge=q(".ln .ln-badge");if(!badge){
      badge=document.createElement("span");badge.className="ln-badge";
      q('[data-screen="exam-run"] .ln-mid').appendChild(badge);
    }
    badge.textContent=m.badge;
    qa(".modelpick button").forEach(function(b){b.classList.toggle("on",b.dataset.openModel===CURRENT_MODEL)});
    q("#exFeedback").hidden=true;
    q("#nextQLabel").textContent="ادامه";q("#submitALabel").textContent="بررسی پاسخ";
    updateStrip();
  }
  function setQuestion(i){QI=Math.max(0,Math.min(QTOTAL-1,i));renderQuestion()}
  function goNext(){setQuestion(QI+1);toast("سؤال بعدی · "+fa(QI+1)+" از "+fa(QTOTAL))}
  function goPrev(){setQuestion(QI-1);toast("سؤال قبل · "+fa(QI+1)+" از "+fa(QTOTAL))}
  function toggleMark(){
    if(MARKS[QI])delete MARKS[QI];else MARKS[QI]=true;
    qa("#markQ,#markK").forEach(function(b){b.classList.toggle("marked",!!MARKS[QI])});
    updateStrip();toast(MARKS[QI]?"سؤال علامتگذاری شد":"علامت برداشته شد");
  }
  function recordAnswer(o){
    if(T.state==="finished")return;
    ANSWERS[QI]={opt:o};
    qa("#exChoices .opt").forEach(function(x){x.classList.toggle("on",+x.dataset.opt===o)});
    QCHECKED=false;q("#exFeedback").hidden=true;
    syncQuick();updateStrip();toast("پاسخ سؤال "+fa(QI+1)+" در پاسخبرگ ثبت شد");
  }
  function syncQuick(){
    var a=ANSWERS[QI]&&ANSWERS[QI].opt;
    qa("#ksQuick button").forEach(function(b){b.classList.toggle("on",+b.dataset.o===a)});
  }
  function buildStrip(){
    var box=q("#ksStrip");if(!box||box.childNodes.length)return;
    for(var i=0;i<QTOTAL;i++){
      var b=document.createElement("button");b.type="button";b.dataset.qi=String(i);b.textContent=fa(i+1);
      b.addEventListener("click",function(){setQuestion(+this.dataset.qi)});
      box.appendChild(b);
    }
  }
  function updateStrip(){
    buildStrip();
    var done=0;
    qa("#ksStrip button").forEach(function(b,i){
      var a=ANSWERS[i]&&(ANSWERS[i].opt||ANSWERS[i].text);
      if(a)done++;
      b.classList.toggle("done",!!a);b.classList.toggle("cur",i===QI);
      b.classList.toggle("flag",!!MARKS[i]);
    });
    q("#answeredCount").textContent=fa(done)+" از "+fa(QTOTAL)+" پاسخ داده شده";
  }
  /* model K navigation + quick bubbles */
  q("#prevK").addEventListener("click",goPrev);
  q("#nextK").addEventListener("click",goNext);
  q("#skipK").addEventListener("click",goNext);
  q("#markK").addEventListener("click",toggleMark);
  qa("#ksQuick button").forEach(function(b){b.addEventListener("click",function(){recordAnswer(+b.dataset.o)})});
  /* model A navigation + analysis toggle */
  q("#prevA").addEventListener("click",goPrev);
  q("#nextA").addEventListener("click",goNext);
  q("#toggleAnalysis").addEventListener("click",function(){
    var a=q("#maAnalysis");a.hidden=!a.hidden;toast(a.hidden?"تحلیل پنهان شد":"تحلیل زنده نمایش داده شد");
  });
  /* model D navigation + written answer */
  q("#prevD").addEventListener("click",goPrev);
  q("#nextD").addEventListener("click",goNext);
  q("#mdAnswer").addEventListener("input",function(){
    ANSWERS[QI]={text:this.value};
    q("#mdCount").textContent=fa(this.value.trim().split(/\s+/).filter(Boolean).length)+" واژه";
    updateStrip();
  });
  q("#saveD").addEventListener("click",function(){toast("پاسخ تشریحی ذخیره شد")});
  q("#swapD").addEventListener("click",function(){toast("تعویض سوال · سؤال جایگزین همردیف آمد")});
  q("#gradeD").addEventListener("click",function(){toast("تصحیح دستی · پاسخنامهٔ تشریحی باز شد")});
  /* review-panel model picker (outside the phone) */
  qa("[data-open-model]").forEach(function(b){
    b.addEventListener("click",function(){
      var model=b.dataset.openModel,kind=EXAM_KIND_BY_MODEL[model];
      EXAM_KIND=kind;q("#examTitle").textContent=EXAM_TITLE_BY_MODEL[model];
      QI=0;MARKS={};ANSWERS={};q("#examFinished").innerHTML="";resetOptions();renderQuestion();
      T.state="idle";clearInterval(T.timer);T.timer=null;
      applyPolicy();applyExamModel(kind);go("exam-run");
      toast("مدل "+fa(["konkur","practice","analytical","descriptive"].indexOf(model)+1)+" · "+MODELS[model].title);
    });
  });
  applyExamModel(EXAM_KIND);''', "question flow + models")

# global click handler: nothing needed (model picker has its own listeners), but
# guard against accidental [data-go]/[data-nav] collisions on the new buttons.
rep('''    var g=e.target.closest("[data-go]");if(g){go(g.dataset.go);return}''',
'''    var mdl=e.target.closest("[data-open-model]");if(mdl){return}
    var g=e.target.closest("[data-go]");if(g){go(g.dataset.go);return}''', "global click guard")

# ===========================================================================
# 8. machine-readable model spec
# ===========================================================================
SPEC = {
    "round": "v12.2",
    "principle": "ONE exam-run page cannot serve both a real Konkur sitting and a Mimo practice lesson. "
                 "Four separate page models are selected by the exam kind.",
    "method": "CODE_FIRST / decoded APK layouts + Mimo section-practice grammar + real Konkur structure; screenshots VISUAL_CROSSCHECK_ONLY",
    "emblem": {"before": "ic_mimo_mascot (Mimo mascot) in both exam-hub and exam-result heroes",
               "after_hub": "ic_survey.xml — the APK's real quiz illustration (quiz_introduction_fragment.xml iv_quiz_introduction, 180dp)",
               "after_result": "ic_cap.xml — graduation cap, white on button_primary circle",
               "note": "both are decoded APK vectors; no Mimo mascot branding left in the exam surfaces"},
    "models": {
        "konkur": {
            "title": "زمان خالص کنکور", "kinds": ["comprehensive", "timed", "review"],
            "for": "آزمون جامع کنکور، زماندار، سرعتی، پومودورو، جمع بندی، نهایی",
            "body": ["chapter_toolbar 52dp: X | title + 6dp progress + mode badge | timer | flag",
                     "INLINE Konkur answer sheet: 20 numbered bubbles (done / current / flagged), click to jump",
                     "question stem + 4 choice_list_item cards",
                     "quick 4-option bubble row (Mimo section-practice sp-opts grammar) — records the answer, never grades it",
                     "quiet tool chips: پاسخبرگ / پاسخنامه (policy) / AI / اتمام / تایمر / خروج"],
            "footer": "Mimo interaction keyboard: 48dp «سؤال قبل» square | FULL-WIDTH purple «سؤال بعد» CTA | 48dp علامتگذاری square + «رد کردن سؤال» link",
            "feedback": False, "answer_key_during": "policy-driven: comprehensive/review = NO, timed = YES",
            "why": "Konkur never reveals correctness during the exam; the answer sheet is filled while solving; "
                   "270 min is fixed; prev/next/mark/skip ARE the primary navigation; پاسخنامه is published after the exam",
            "apk_evidence": ["chapter_toolbar.xml", "choice_list_item.xml", "interaction_keyboard_view.xml",
                             "run_button_view.xml", "continue_next", "lesson_skip"],
        },
        "practice": {
            "title": "تمرین میمو", "kinds": ["normal"],
            "for": "تکدرسی، مبحثی، این ماه، مرور غلطها، آزمون دوباره",
            "body": ["chapter_toolbar", "question + 4 choice cards", "lesson_interactive_feedback_bottom_sheet_dialog on submit",
                     "tool chips with پاسخبرگ + پاسخنامه + AI"],
            "footer": "exact lesson_interactive: 48dp prev + 48dp bookmark + ONE full-width purple CTA that toggles "
                      "lesson_submit «بررسی پاسخ» -> feedback -> lesson_continue «ادامه»; lesson_skip link",
            "feedback": True, "answer_key_during": True,
            "why": "learning mode, immediate feedback is the point (the user: «در آزمونهای تحلیلی شاید بررسی پاسخ مهم باشه»)",
            "apk_evidence": ["lesson_interactive_multiplechoice_fragment.xml", "choice_view.xml",
                             "lesson_interactive_feedback_bottom_sheet_dialog.xml", "btn_submit", "btn_continue_big"],
        },
        "analytical": {
            "title": "تحلیلی", "kinds": ["analytical"],
            "for": "تحلیل زیست، تحلیل آزمون جامع، تحلیل غلطها",
            "body": ["question + 4 choice cards", "feedback bottom sheet on submit",
                     "INLINE تحلیل زنده card: درصد / اگر غلطها نزده میذاشتی / نقشهٔ ضعف / میانگین زمان"],
            "footer": "48dp prev | full-width «بررسی پاسخ» CTA | 48dp next + تحلیل toggle",
            "feedback": True, "answer_key_during": True,
            "why": "analytical exams need BOTH immediate checking and free navigation + live stats",
            "apk_evidence": ["lesson_interactive_feedback_bottom_sheet_dialog.xml", "run_button_view.xml"],
        },
        "descriptive": {
            "title": "تشریحی", "kinds": ["descriptive"],
            "for": "آزمون تشریحی (section ۷ template: تعویض سوال / تصحیح دستی)",
            "body": ["NO 4 option cards — a written-answer textarea with a word counter", "tool chips"],
            "footer": "48dp prev | full-width «ثبت پاسخ» CTA | 48dp next + «تعویض سوال» / «تصحیح دستی» chips",
            "feedback": False, "answer_key_during": False,
            "why": "a descriptive answer cannot be graded by a 4-way choice widget",
            "apk_evidence": ["EXAM_SECTION_TEMPLATES.csv :: تعویض سوال / تصحیح دستی"],
        },
    },
    "reviewer_control": "aside.spec > .modelpick — 4 buttons preview each model without changing the exam cards",
    "unchanged_contract": ["5 tabs / no MAX / original curved zigzag", "7 labelled exam sections + templates + descriptive answer",
                           "fixed 270 min for comprehensive", "timer only inside exam", "پاسخبرگ≠پاسخنامه",
                           "exactly one exam-hub lock", "one AI button in two places", "isolated section-practice",
                           "20 distinct questions with explanation", "v12 single full-width CTA grammar (per model)",
                           "rollback snapshot tools/design_v11_full.html"],
}
(DESIGN / "EXAM_PAGE_MODELS.json").write_text(json.dumps(SPEC, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

evp = DESIGN / "EXAM_UI_CODE_EVIDENCE.json"
ev = json.loads(evp.read_text(encoding="utf-8"))
ev["exam_page_models_v12_2"] = {
    "spec": "DESIGN/EXAM_PAGE_MODELS.json",
    "count": 4,
    "reason": "user: analytical exams want بررسی پاسخ, timed/other exams want سؤال بعدی/قبلی + پاسخنامه; "
              "build several exam-page models from earlier button designs, Mimo practice and Konkur structure",
    "emblem": "ic_mimo_mascot -> ic_survey (hub) / ic_cap (result)",
}
evp.write_text(json.dumps(ev, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

(TOOLS / "design_v12_2_template.html").write_text(html, encoding="utf-8")
(DESIGN / "index.html").write_text(html, encoding="utf-8")
print(json.dumps({
    "output": str(DESIGN / "index.html"), "bytes": len(html.encode("utf-8")),
    "source": str(TOOLS / "design_v12_1_template.html"),
    "models": 4, "model_footers": html.count('class="mf" data-exmodel='),
    "emblem": "ic_survey" in html and "ic_cap" in html
              and 'data-icon="ic_mimo_mascot"' not in html.split('data-screen="exam-hub"')[1].split("</section>")[0]
              and 'data-icon="ic_mimo_mascot"' not in html.split('data-screen="exam-result"')[1].split("</section>")[0],
    "geo_vectors": len(geo["vectors"]),
    "spec": str(DESIGN / "EXAM_PAGE_MODELS.json"),
    "curved_zigzag_kept": "M242 70 H280 Q312 70 312 102 V140" in html,
}, ensure_ascii=False, indent=2))
