#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""finalize_v12.py — round-12 docs/catalogs/banners/MANIFEST. Idempotent."""
from __future__ import annotations
import csv
import json
from pathlib import Path

UP = Path(__file__).resolve().parents[1]
CAT = UP / "CATALOGS"
D = UP / "DESIGN"
MARK = "<!-- v12-banner -->"

APPEND = {
    "DESIGN_FEEDBACK.csv": [
        ["F-63", "بخش آزمون خیلی جدا و ناهماهنگ با پروتوتایپ اصلی میمو است",
         "سه صفحهٔ آزمون از کلاس جداگانهٔ konkur خارج و روی معماری واقعی lesson_interactive میمو بازسازی شدند؛ همان توکنها/وکتورها/تایپوگرافی",
         "DESIGN/EXAM_UI_CODE_EVIDENCE.json, DESIGN/index.html#exam-hub", "APPLIED"],
        ["F-64", "دکمهٔ «سؤال بعدی / سؤال قبلی» اشتباه گذاشته شده",
         "دو دکمهٔ هموزن .qnav و نوار ۷ دکمهای .qfoot حذف؛ یک CTA بنفش تمامعرض (btn_continue_big) + مربع ۴۸dp سؤال قبل (btn_undo) + مربع علامتگذاری + لینک lesson_skip",
         "interaction_keyboard_view.xml / run_button_view.xml", "APPLIED"],
        ["F-65", "ساختار دکمهها و بقیه از روی اپلیکیشن اصلی ساخته شود",
         "chapter_toolbar(52dp) + ChoiceView/choice_list_item + feedback bottom sheet + quiz_introduction + celebration نتیجه؛ چرخهٔ انتخاب←بررسی←بازخورد←ادامه",
         "DESIGN/index.html#exam-run, DESIGN/index.html#exam-result", "APPLIED"],
    ],
    "SCOPE_DECISIONS.csv": [
        ["D43", "سطوح آزمون", "EXAM_SURFACES_CODE_FIRST_V12",
         "حکم نهایی از XML/DEX/ARSC میمو؛ اسکرینشات فقط VISUAL_CROSSCHECK_ONLY. کلاس konkur حذف و سه صفحه exv12 شدند",
         "بازخورد صریح دور دوازدهم", "DESIGN/EXAM_UI_CODE_EVIDENCE.json"],
        ["D44", "ناوبری سؤال", "SINGLE_FULLWIDTH_CTA_V12",
         "بدون دکمهٔ قبلی/بعدی هموزن؛ prevQ = آیکون مربعی ۴۸dp، nextQ = تنها CTA تمامعرض، پیمایش با همان دکمه + پاسخبرگ",
         "interaction_keyboard_view.xml + mimo-04-lesson-continue.jpg", "24_DESIGN_ROUND_12.md §۲"],
        ["D45", "برگشتپذیری", "V11_ROLLBACK_SNAPSHOT_V12",
         "tools/design_v11_full.html نگه داشته شد؛ در صورت نپسندیدن v12 میتوان عقب برگشت. مصوبات v8/v11 پابرجا میمانند",
         "دستور کاربر: نهایت برمیگردیم عقب", "tools/design_v11_full.html"],
    ],
    "UI_FIDELITY_RULES.csv": [
        ["F39", "نوار بالای آزمون", "chapter_toolbar.xml: X + pb_chapter ۶dp + پرچم، ارتفاع ۵۲dp، خط ۱dp. بدون appbar جداگانه",
         "SOURCE/res/layout/chapter_toolbar.xml"],
        ["F40", "فوتر آزمون", "interaction_keyboard_view.xml: خط ۱dp + مربعهای ۴۸dp چپ + یک CTA بنفش تمامعرض؛ ممنوع: دکمههای قبلی/بعدی هموزن و نوار اسکرولی چنددکمهای",
         "SOURCE/res/layout/interaction_keyboard_view.xml / run_button_view.xml"],
        ["F41", "گزینهها و بازخورد", "choice_list_item.xml: شعاع ۱۲dp، minHeight ۴۸dp، padding ۱۶/۱۲، حالتهای selected/correct/wrong؛ بازخورد در پنل lesson_interactive_feedback_bottom_sheet_dialog",
         "SOURCE/res/layout/choice_list_item.xml + drawable/multiplechoice_background_*.xml"],
    ],
    "OPEN_QUESTIONS.csv": [
        ["U13", "آیا ساختارشکنی v12 در بخش آزمون تأیید میشود؟",
         "PENDING REVIEW: کاربر اجازهٔ تغییرات زیاد و ساختارشکنی داد و گفت «نهایت برمیگردیم عقب». نسخهٔ v11 در tools/design_v11_full.html محفوظ است",
         "yes", "تأیید نهایی دیزاین"],
    ],
}
for name, new_rows in APPEND.items():
    p = CAT / name
    with p.open(encoding="utf-8", newline="") as f:
        body = list(csv.reader(f))[1:]
    present = {r[0] for r in body if r}
    todo = [r for r in new_rows if r[0] not in present]
    if todo:
        with p.open("a", encoding="utf-8", newline="") as f:
            csv.writer(f).writerows(todo)
    print(name, "+", len(todo), "->", len(body) + len(todo))

# --------------------------------------------------------------------------
DOC24 = r'''# دور دوازدهم طراحی — DESIGN v12 (بازسازی سطوح آزمون روی معماری واقعی میمو)

> **وضعیت:** `DESIGN v12 · REVIEW` — منتظر تأیید نهایی. همچنان **فقط پلن/دیزاین**؛ هیچ کد محصولی نوشته نشده.
> جایگزین `23_DESIGN_ROUND_11.md` بهعنوان حکم فعلی **سطوح آزمون**. معماری قوسدار، ۵ تب، لیدربورد «وضعیت من» و ۳ کارت برنامهمحور **دستنخورده**اند.
> **مسیر برگشت:** `tools/design_v11_full.html` (همان نسخهٔ تحویلشدهٔ قبل از این دور).

---

## ۱. مشکل و حکم

بخش آزمون یک «پوستهٔ جداگانه» (`class="screen konkur"`) با رنگ/تایپ/چیدمان خودش بود و انگار از اپ دیگری آمده بود. این دور آن پوسته **حذف** شد؛ سه صفحهٔ `exam-hub` / `exam-run` / `exam-result` حالا `exv12`اند و دقیقاً از همان توکنهای ARSC، وکتورها و تایپوگرافی بقیهٔ پروتوتایپ میمو استفاده میکنند.

**کد مبناست، اسکرینشات فقط چک بصری.** شواهد ماشینخوان: `DESIGN/EXAM_UI_CODE_EVIDENCE.json`.

## ۲. اصلاح دکمهها (موضوع اصلی درخواست)

| قبل (v11) | **بعد (v12)** |
|---|---|
| `.qnav`: دو دکمهٔ هموزن «سؤال قبل» + «سؤال بعد» | `.lk-row`: **یک** CTA بنفش تمامعرض `#nextQ` |
| `.qfoot`: نوار افقی اسکرولی ۷ دکمهای | دو مربع ۴۸dp چپ: `#prevQ` (سؤال قبل) و `#markQ` (علامتگذاری) |
| گزینهها: ردیفهای ساده با حاشیهٔ بنفش | `choice_list_item.xml`: کارت ۱۲dp، رادیو، minHeight ۴۸dp |
| بدون بازخورد | پنل `lesson_interactive_feedback_bottom_sheet_dialog` (سبز/قرمز + توضیح مبحث) |

منبع ساختار: **`interaction_keyboard_view.xml`** — خط ۱dp بالا، `btn_reset`/`btn_undo` مربعی ۴۸dp سمت چپ، و `RunButton` سمت راست که یا `btn_play` ۴۸dp نشان میدهد یا **`btn_continue_big` / `btn_submit` تمامعرض**. `run_button_view.xml` تأیید میکند CTA عرض کامل و حداقل ۱۴۰dp دارد. اسکرینشات `mimo-04-lesson-continue.jpg` همان دکمهٔ بنفش تمامعرض `CONTINUE` را نشان میدهد (فقط چک بصری).

**چرخهٔ واقعی سؤال** (از روی رشتهها):
1. `interaction_hint_single_choice` = «Tap the correct answer» → «گزینهٔ درست را انتخاب کنید».
2. انتخاب گزینه → CTA میشود `lesson_submit` = «بررسی پاسخ».
3. کلیک → `multiplechoice_background_correct/wrong` + پنل بازخورد با توضیح مبحث و ارجاع به کتاب.
4. CTA میشود `lesson_continue` = **«ادامه»** → سؤال بعد.
5. `lesson_skip` = «رد کردن سؤال» لینک آرام زیر فوتر؛ `#prevQ` سؤال قبل؛ پرش مستقیم از طریق پاسخبرگ.

## ۳. سه صفحه، جزءبهجزء

### نوار بالا — `chapter_toolbar.xml` (۵۲dp)
`btn_lesson_close` (`ic_close` → خروج) | مرکز: نام آزمون + `pb_chapter` نوار پیشرفت **۶dp** (`lesson_progressbar_height`, استایل `ProgressBarChapter`) | `timerChip` (تایمر، فقط داخل آزمون، ۲۷۰ دقیقهٔ ثابت) | `btn_lesson_report` (`ic_flag` → پاسخبرگ). خط زیرین ۱dp `line_primary`.

### بدنه — `lesson_interactive_multiplechoice_fragment.xml`
`ScrollView` با `lesson_content_margin_top=8dp`؛ `LessonDescriptionView` (TextH2 ۲۰sp / TextP1 ۱۸sp) بعنوان صورت سؤال؛ `tv_multiplechoice_hint`؛ `rv_multiplechoice_options` با ۴ گزینه (شعاع ۱۲dp، حاشیهٔ ۲dp، `selection_selected` / `support_green` / `support_coral`). فاصلهها ۴/۸/۱۲/۱۶/۲۴/۳۲dp و شعاعها ۱۲/۱۶dp مستقیماً از `dimen.xml`.

اقدامات ثانویه (پاسخبرگ، پاسخنامه، AI، اتمام، توقف/تنظیم مجدد تایمر، خروج) از نوار اسکرولی به **ردیف چیپهای آرام** بالای فوتر منتقل شدند؛ هیچکدام حذف نشدند.

### هاب آزمونها — `quiz_introduction_fragment.xml`
کارت معرفی (`ic_mimo_mascot` + عنوان + توضیح) + چیپهای فیلتر + **۷ بخش لیبلدار** (همان قالبها و «زمان ثابت ۲۷۰ دقیقه» محفوظ). شبکهٔ ۳ ستونهٔ گرهمانند تبدیل شد به **ردیفهای لیستی میمو**: آیکون ۴۴dp در مربع ۱۲dp + عنوان + حاشیهٔ `card_pressed`؛ دقیقاً ۲۱ ردیف و همان **یک قفل** «آزمون نهایی».

### نتیجه — `lesson_awesome_fragment.xml` / `chapter_finished_*`
صفحهٔ celebration: ماسکوت، «آزمون تمام شد!»، کارت آمار، کارت «صورت اشتباهات (منتقلشونده به AI)» و ردیف ۳ دکمه. پاسخنامه بهصورت خودکار بعد از آزمون جامع باز میشود.

## ۴. شواهد کد (همه از APK دیکدشده)

| فایل | آنچه گرفتیم |
|---|---|
| `chapter_toolbar.xml` | X، نوار ۶dp، پرچم، خط ۱dp، ارتفاع ۵۲dp |
| `lesson_interactive_fragment.xml` / `..._multiplechoice_fragment.xml` | ساختار ScrollView + Description + ChoiceView + Keyboard |
| `choice_view.xml` / `choice_list_item.xml` / `layout_choice_card_item.xml` | hint، RecyclerView، رادیو، TextP1 ۱۸sp، ۴۸dp |
| `multiplechoice_background_*.xml` | ۴ حالت unselected/selected/correct/wrong |
| `interaction_keyboard_view.xml` / `run_button_view.xml` | فوتر ۶۸dp، مربعهای ۴۸dp، CTA تمامعرض |
| `lesson_interactive_feedback_bottom_sheet_dialog.xml` | پنل بازخورد، `drawer_bottom_sheet_background` |
| `quiz_introduction_fragment.xml` | کارت معرفی + CTA شروع |
| `string.xml` | `lesson_continue` / `lesson_submit` / `lesson_skip` / `interaction_hint_single_choice` |
| `dimen.xml` / `color.xml` / `style.xml` | ۴…۴۰dp، رنگها، TextH1/H2/P1/P2/Label1/Button1 |

## ۵. بدون تغییر (مصوبات پابرجا)

معماری اورجینال قوسدار (۸۰/۱۹۶/۳۱۲، فاصلهٔ ۲۴dp، زانوهای `Q` ۳۲dp) · ۵ تب و `MAX` ممنوع · لیدربورد فقط «وضعیت من» · ۳ کارت برنامهمحور + ۱۲ کورس مبحثی · بدون آرم برنامهنویسی · روتین/Habitica و دیکته حذفشده · بدون یادداشت داخل UI · **۷ بخش لیبلدار + قالب فیلد + پاسخنامهٔ تشریحی** · تایمر فقط داخل آزمون و ۲۷۰ دقیقهٔ ثابت · «پاسخبرگ»≠«پاسخنامه» · تکدکمهٔ AI · **صفر قفل یادگیری** و تنها قفل «آزمون نهایی / دو هفتگی» · بولت ← `section-practice` جدا · چت مینیمال · ۱۴ اسکرینشات فقط **چک بصری**.

## ۶. تحویل

`tools/build_design_v12.py` (از `design_v11_full.html`) → `DESIGN/index.html` ۴۰۶٬۶۱۶ بایت / ۱۴ نما / ۵ تب / ۹۳ وکتور / ۰ خطای jsdom. `tools/finalize_v12.py` → کاتالوگها/داکیومنتها/منیفست. `verify_upgrade.py` PASS، `check_v12.js`، `node --check` OK. تأیید نهایی همچنان **PENDING**؛ هیچ کد محصولی نوشته نشده.
'''

NOTES = r'''# یادداشتهای طراحی — DESIGN v12

> نسخهٔ جاری: **DESIGN v12 · REVIEW** (منتظر تأیید نهایی). نسخههای **DESIGN v6 / DESIGN v7 / DESIGN v8 / DESIGN v9 / DESIGN v10 / DESIGN v11** بایگانی حسابرسیاند. همچنان **فقط پلن/دیزاین**؛ هیچ کد محصولی نوشته نشده.

## ۱. اصل

کد مبناست (`ARSC`، `dimen.xml`، `drawable/*.xml`، `style.xml`، `DEX`، `test-tracks.json`)؛ ۱۴ اسکرینشات فقط `VISUAL_CROSSCHECK_ONLY`. `NODE_CODE_GEOMETRY.json` همچنان حکم هندسهٔ مسیر است. فقط **نام درس/فصل/مبحث و لیبلها** کنکوری میشود؛ ۰ رنگ/فونت/شعاع/آیکون تازه.

## ۲. معماری اورجینال قوسدار (دستنخورده)

سه لاین `۸۰/۱۹۶/۳۱۲`، فاصلهٔ **۲۴dp**، گام ۱۱۶dp، زانوهای گرد `Q` شعاع **۳۲dp** (`A/B/A/B/B`)، دو قطعهٔ رنگی، `viewBox 392×720`، شعاع گره ۲۶dp، ضخامت مسیر ۱۰dp، آیکن ۴۸dp. صفر قفل یادگیری.

## ۳. دور دوازدهم — آزمونها هماهنگ با میمو

پوستهٔ جداگانهٔ `konkur` **حذف** شد؛ `exam-hub` / `exam-run` / `exam-result` حالا `exv12`اند و از همان توکنها/وکتورها/تایپ استفاده میکنند. نوار بالا از `chapter_toolbar.xml` (X + نوار پیشرفت ۶dp + پرچم، ۵۲dp)، بدنه از `lesson_interactive_multiplechoice_fragment.xml` و `choice_list_item.xml`، فوتر از `interaction_keyboard_view.xml`. **دو دکمهٔ هموزن «سؤال قبل/سؤال بعد» و نوار ۷ دکمهای حذف شدند**؛ حالا یک CTA بنفش تمامعرض (`lesson_continue`/`lesson_submit`) + مربع ۴۸dp سؤال قبل + مربع علامتگذاری + لینک `lesson_skip`. چرخه: انتخاب ← بررسی پاسخ ← بازخورد سبز/قرمز با توضیح مبحث ← ادامه. شواهد: `DESIGN/EXAM_UI_CODE_EVIDENCE.json`. مسیر برگشت `tools/design_v11_full.html`.

## ۴. دور یازدهم (محفوظ)

لیدربورد فقط **«My status / وضعیت من»** + ۳ کارت آمار + «آزمونها و امتیازات من». `Career Paths` → **«یادگیری برنامه محور»**؛ `Courses` → **«یادگیری مبحثی»**. **سه کارت درشت** = ۳ برنامهٔ دوازدهم/یازدهم/دهم (کارت تکراری مبحثی حذف شد). ۱۲ کورس = ۴ درس × ۳ پایه. نمای مسیر: «مدرک پایان دوره» / «۲۲ درصد کامل شده» / `2/9` / **۱۰ بازهٔ دو هفتهای ۱ آبان..۱۵ اسفند** با «دروس: زیست، شیمی، ریاضی، فیزیک». کورسها همان نما را با **فصل + درس** (`KONKUR_CURRICULUM.json`: ۶۰ فصل / ۱۸۰ درس) پر میکنند. هیچ آرم/نشان برنامهنویسیای وجود ندارد.

## ۵. مصوبات پابرجا

۵ تب (`MAX` ممنوع) · حذف روتین/Habitica و دیکته · حذف یادداشتهای داخل UI · **نگهداری ۷ بخش لیبلدار / قالب فیلد / پاسخنامهٔ تشریحی** · تایمر فقط داخل آزمون / ۲۷۰ دقیقه / «پاسخبرگ»≠«پاسخنامه» · تکدکمهٔ AI · **صفر گرهٔ قفلی** و تنها یک قفل «آزمون نهایی / دو هفتگی» · بولت ← `section-practice` جدا · لیدربورد بدون Promotion Zone · چت مینیمال · RTL/شب · بدون Pro/پرداخت.

## ۶. clean-room و وضعیت

هیچ دارایی/کدی از Mimo، همدرس، Hadaf Plus، LearnHarness، EPM یا Habitica کپی نشده. `DESIGN/index.html` از payloadهای استخراجشده رندر میشود: ۱۴ نما / ۵ تب / ۹۳ وکتور / ۰ خطای jsdom / وریفایر PASS. منتظر **تأیید نهایی**؛ بعدش تازه P0.
'''

(UP / "24_DESIGN_ROUND_12.md").write_text(DOC24, encoding="utf-8")
(D / "DESIGN_NOTES.fa.md").write_text(NOTES, encoding="utf-8")
print("docs written")

for p in sorted(UP.glob("*.md")):
    s = p.read_text(encoding="utf-8")
    if MARK in s:
        continue
    current = p.name.startswith("24_")
    banner = (MARK + "\n> " + ("✅ **DESIGN v12 · CURRENT** — لاگ دور دوازدهم، جایگزین v11. "
                              if current else
                              "⚠️ **بایگانی / superseded:** طراحی فعلی **[DESIGN v12](24_DESIGN_ROUND_12.md)** است. ")
              + "همچنان فقط پلن/دیزاین؛ هیچ کد محصولی نوشته نشده.")
    lines = s.split("\n")
    insert_at = 1 if lines and lines[0].startswith("#") else 0
    lines.insert(insert_at, banner)
    p.write_text("\n".join(lines), encoding="utf-8")
print("banners written")

wf = UP / "wireframes.html"
s = wf.read_text(encoding="utf-8")
s = s.replace("DESIGN/index.html\">DESIGN v11</a>", "DESIGN/index.html\">DESIGN v12</a>")
s = s.replace("<a href=\"23_DESIGN_ROUND_11.md\">لاگ دور یازدهم</a>", "<a href=\"24_DESIGN_ROUND_12.md\">لاگ دور دوازدهم</a>")
wf.write_text(s, encoding="utf-8")
print("wireframes banner updated")

mp = UP / "MANIFEST.json"
m = json.loads(mp.read_text(encoding="utf-8"))
stable = [p for p in UP.rglob("*") if p.is_file() and p.name not in ("SHA256SUMS.txt", "VERIFICATION_REPORT.json")]
m["date"] = "2026-11-04"
m["status"] = "PLAN_ONLY + DESIGN v12 REVIEW (no product implementation)"
dl = m["deliverables"]
dl["persian_docs"] = len(list(UP.glob("*.md")))
dl["csv_catalogs"] = len(list(CAT.glob("*.csv")))
dl["extracted_assets_files"] = len(stable)
dl["total_bytes"] = sum(p.stat().st_size for p in stable)
dl["verification"] = "PASS"
dl["verification_checks"] = 0
dl["design_round"] = "v12 (REVIEW)"
dl["design_views"] = 14
dl["design_svg_vectors"] = 93
dl["bottom_nav_tabs"] = 5
dl["v12_exam_ui"] = ("EXAM_UI_CODE_EVIDENCE.json (chapter_toolbar / lesson_interactive_multiplechoice / "
                     "choice_list_item / interaction_keyboard_view / run_button_view) — single full-width CTA, "
                     "no equal prev/next pill pair, no separate konkur skin")
cf = m["critical_findings"]
for x in [
    "v12: exam surfaces (hub/run/result) rebuilt code-first from decoded Mimo lesson layouts; separate 'konkur' skin removed, all three now use the same ARSC tokens/vectors/type as the rest of the prototype",
    "v12: WRONG equal-weight prev/next pill pair (.qnav) and 7-button scrolling .qfoot REMOVED; one full-width purple CONTINUE/SUBMIT CTA (#nextQ) + 48dp square back (#prevQ) + 48dp bookmark + lesson_skip link, per interaction_keyboard_view.xml / run_button_view.xml",
    "v12: real question cycle — choice selection -> lesson_submit (بررسی پاسخ) -> multiplechoice correct/wrong feedback bottom sheet with topic explanation -> lesson_continue (ادامه) -> next question",
    "v12: exam hub converted to Mimo list rows + quiz_introduction hero; result converted to Mimo celebration screen; 7 labelled sections, fixed 270 min, one exam-hub lock, one AI button and isolated section-practice all preserved",
    "v12: rollback snapshot kept at tools/design_v11_full.html (user allowed structural break, 'at worst we go back')",
]:
    if x not in cf:
        cf.append(x)
for cmd in ["python3 tools/build_design_v12.py .", "python3 tools/finalize_v12.py ."]:
    if cmd not in m["reproduce"]:
        m["reproduce"].append(cmd)
m["design_round_11"]["status"] = "DESIGN v11 · SUPERSEDED by round 12 (exam surfaces only) — leaderboard/tracks/cards KEPT"
m["design_round_12"] = {
    "status": "DESIGN v12 · REVIEW — awaiting final approval (CURRENT)",
    "trigger": "user: پروتوتایپ بخش آزمون خیلی بد و جدا از اپلیکیشن است، شبیهترش کن به پروتوتایپ اصلی میمو؛ دکمهٔ سؤال بعدی/قبلی را اشتباه گذاشتی؛ ساختار دکمهها و بقیه را از روی اپ اصلی بساز؛ اجازهٔ تغییرات زیاد و حتی ساختارشکنی (نهایت برمیگردیم عقب)",
    "method": "CODE_FIRST / decoded APK layouts, dimens, colors, styles, strings; screenshots VISUAL_CROSSCHECK_ONLY",
    "evidence_file": "DESIGN/EXAM_UI_CODE_EVIDENCE.json",
    "screens_rebuilt": ["exam-hub", "exam-run", "exam-result"],
    "skin": "separate `konkur` class removed from all exam screens; new `exv12` uses the same Mimo tokens",
    "navbar": "chapter_toolbar.xml — 52dp: ic_close | pb_chapter 6dp + examTitle | timerChip | ic_flag; 1dp line_primary",
    "question_body": "lesson_interactive_multiplechoice_fragment.xml — ScrollView, LessonDescriptionView (TextH2/P1), tv_multiplechoice_hint, rv_multiplechoice_options with 4 choice_list_item cards (12dp radius, 48dp min, selected/correct/wrong backgrounds)",
    "footer": "interaction_keyboard_view.xml / run_button_view.xml — 68dp, 1dp top border, two 48dp square buttons (prevQ=btn_undo, markQ=btn_reset), ONE full-width primary CTA nextQ (btn_continue_big / btn_submit), lesson_skip link",
    "button_correction": {"before": "two equal-weight pill buttons «سؤال قبل» + «سؤال بعد» in .qnav, plus 7-button scrolling .qfoot",
                          "after": "single full-width purple CTA + 48dp icon-only back square; secondary actions collapse into a quiet chip row"},
    "flow": ["interaction_hint_single_choice", "select option", "lesson_submit = بررسی پاسخ",
             "lesson_interactive_feedback_bottom_sheet_dialog (correct/wrong + توضیح مبحث)",
             "lesson_continue = ادامه → سؤال بعدی", "lesson_skip = رد کردن سؤال"],
    "hub": "quiz_introduction_fragment.xml hero + Mimo list rows; 7 labelled cat-meta sections, 21 tiles, exactly ONE lock",
    "result": "lesson_awesome_fragment / chapter_finished celebration + stats + 3-button row; descriptive answer + AI transfer kept",
    "unchanged": ["original curved zigzag path map (v10)", "5 tabs / no MAX", "leaderboard My-status-only (v11)",
                  "3 program cards + 12 topic courses (v11.1)", "zero programming emblems",
                  "7 labelled exam sections + templates + descriptive answer", "fixed 270 min",
                  "timer only inside exam", "پاسخبرگ≠پاسخنامه", "one pre-existing exam-hub lock",
                  "one AI button in two places", "no UI annotations", "isolated section-practice"],
    "rollback": "tools/design_v11_full.html (exact v11.1 output before this round)",
    "final_log": "24_DESIGN_ROUND_12.md",
    "design_notes": "DESIGN/DESIGN_NOTES.fa.md",
    "final_approval": "PENDING — no product implementation until the user says the design is final",
}
mp.write_text(json.dumps(m, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("MANIFEST updated; docs=%d csv=%d files=%d bytes=%d" %
      (dl["persian_docs"], dl["csv_catalogs"], len(stable), sum(p.stat().st_size for p in stable)))
