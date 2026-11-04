#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""finalize_v7.py — append v7 catalogs, write v7 docs/banners/MANIFEST.

Idempotent: re-running does not duplicate CSV rows, banners or manifest keys.
"""
from __future__ import annotations
import csv
import json
import re
from pathlib import Path

UP = Path(__file__).resolve().parents[1]
CAT = UP / "CATALOGS"
D = UP / "DESIGN"
MARK = "<!-- v7-banner -->"

# --------------------------------------------------------------------------
# 1. Append v7 rows to the existing catalogs (idempotent by id)
# --------------------------------------------------------------------------
APPEND = {
    "DESIGN_FEEDBACK.csv": ("id", "F-37", [
        ["F-37", "خیلی خیلی خیلی خوبه و نزدیکه ولی چند تا اصلاح ریز مونده", "دور هفتم: ۷ اصلاح ریز انجام شد بدون دستزدن به اصل چارچوب میمو", "18_DESIGN_ROUND_7.md, DESIGN/index.html", "APPLIED"],
        ["F-38", "ساختار گرهها / مربعهایی که کلیک میشه و روش شروع میشه هنوز یه کم کار داره", "بازسازی دقیق گرهها از کد: تیک بنفش با لبهٔ ۳بعدی، کارت سفید حلقهدار + پلی، حلقهٔ ½، قفل، اتور گردگوشه، START، دکمهٔ شناور واژهنامه", "DESIGN/NODE_CODE_GEOMETRY.json, CATALOGS/MIMO_PATH_NODES.csv (50 ردیف), DESIGN/index.html", "APPLIED"],
        ["F-39", "گرههای رعدوبرق وقتی میزنه آزمون از مبحث تا اون بخشه؛ نباید قاتی شه با بخش آزمونی که داریم", "صفحهٔ جداگانهٔ data-screen=section-practice با صورت سؤال از sections[].tutorialIds تا همان فصل، فیدبک میمو و دیالوگ Fully charged/mastered؛ بدون تایمر/پاسخبرگ/پاسخنامه/۲۷۰ دقیقه/POLICY", "CATALOGS/PRACTICE_VS_EXAM.csv (12 ردیف), DESIGN/index.html", "APPLIED"],
        ["F-40", "ایکون زنجیره بالا عوض شه و بنویس الصاق فایل / اضافه کردن فایل؛ کناریشم زنجیره گفت و گو؛ مرتب و ایکون مشخص", "گیرهٔ کاغذ attachment + «اضافه کردن فایل»؛ ic_link_external + «زنجیره گفت و گو»؛ دو چیپ کوتاه در یک ردیف مرتب، بدون ایموجی", "DESIGN/index.html, CATALOGS/AI_PANEL_SPEC.csv", "APPLIED"],
        ["F-41", "آموزش / تمرین ریز بشن تو همون خط پایین مدیوم و جمینی و دیکته؛ دیکته برای ویسه جدا نشه", "TEACH/PRACTICE ریز و همان یک خط؛ Dictate با ic_microphone همان خط ماند؛ gemini-flash-lite-latest و medium با chevron", "DESIGN/index.html, CATALOGS/AI_PANEL_SPEC.csv", "APPLIED"],
        ["F-42", "صفحهٔ آزمون سؤال قبل / سؤال بعد دو دکمهٔ تر و تمیز؛ پایینش پاسخبرگ و بقیه یک خط، زیاد بولد نباشن", "دو دکمهٔ تمیز qnav + یک خط sticky کمضخامت qfoot (پاسخبرگ/پاسخنامه/خروج/اتمام/AI/تایمر) با font-weight 400", "DESIGN/index.html, 18_DESIGN_ROUND_7.md §۴", "APPLIED"],
        ["F-43", "لیدربورد پروموشن زون نیاز نیست", "Promotion Zone / منطقهٔ صعود حذف شد؛ selfbox و اطلاعات خود فرد حفظ شد", "DESIGN/index.html", "APPLIED"],
        ["F-44", "نوار پایین یه بخش دیگه به اسم روتین روزانه؛ سیستم امتیازدهی Habitica؛ هیچی قاتی نشه؛ زیادی تو چشم نزنه", "تب ششم کمسر و صدای «روتین روزانه» با پوستهٔ ۱۰۰٪ میمو؛ فقط قواعد امتیازدهی Habitica (۲۲ قاعده / ۱۳ SHA-256) ایزوله؛ بدون کد/دارایی/محتوا/رنگ/فونت تازه؛ MAX ممنوع", "DESIGN/HABITICA_SCORING.json, CATALOGS/HABITICA_SOURCES.csv, CATALOGS/HABITICA_SCORING.csv, 19_HABITICA_ROUTINE_SPEC.md", "APPLIED"],
    ]),
    "SCOPE_DECISIONS.csv": ("id", "D21", [
        ["D21", "گرههای مسیر یادگیری", "NODE_EXACT_V7", "هندسهٔ گرهها مستقیم از pathData/AXML/DEX + چک بصری mimo-01/02/10؛ کد ملاک است", "بازخورد v7 «ساختار گرهها هنوز یه کم کار داره»", "DESIGN/NODE_CODE_GEOMETRY.json, CATALOGS/MIMO_PATH_NODES.csv"],
        ["D22", "گرههای رعدوبرق", "SECTION_PRACTICE_ISOLATED", "آزمونک «از مبحث تا همان فصل» در data-screen=section-practice؛ سهگانه تفکیک: تمرین مبحث / آزمون کنکور / روتین", "بازخورد v7 «نباید قاتی شه با اون بخش ازمونی که داریم»", "CATALOGS/PRACTICE_VS_EXAM.csv, DESIGN/index.html"],
        ["D23", "نوار بالای چت AI", "ATTACHMENT_AND_CHAIN_LABELS", "attachment + «اضافه کردن فایل» و ic_link_external + «زنجیره گفت و گو»؛ ۸ دکمهٔ LH حفظ شد", "بازخورد v7 «الصاق فایل … کناریشم زنجیره گفت و گو»", "CATALOGS/AI_PANEL_SPEC.csv, DESIGN/index.html"],
        ["D24", "خط پایین چت AI", "ONE_LINE_COMPOSER", "TEACH/PRACTICE ریز در همان خط medium / gemini-flash-lite-latest / Dictate؛ دیکته ویس جدا نشد", "بازخورد v7 «اون دیکته برای ویس هست نمیخواد اونو جدا کن»", "CATALOGS/AI_PANEL_SPEC.csv, DESIGN/index.html"],
        ["D25", "صفحهٔ سؤال و لیدربورد", "QUIET_EXAM_CONTROLS", "دو دکمهٔ تمیز قبل/بعد + یک خط کنترل کمضخامت؛ Promotion Zone حذف", "بازخورد v7 «دو تا دکمه تر تمیز … زیاد بولد نباشند»", "DESIGN/index.html, 18_DESIGN_ROUND_7.md"],
        ["D26", "ناوبری پایین", "SIX_TABS_ROUTINE", "تب ششم «روتین روزانه» به دستور صریح دور هفتم اضافه شد؛ حکم ۵ تب ناظر به MAX بود و MAX همچنان ممنوع است", "بازخورد v7 «یه بخش دیگریم باید اضافه بشود به اسم روتین روزانه»", "18_DESIGN_ROUND_7.md §۶, DESIGN/index.html"],
    ]),
    "UI_FIDELITY_RULES.csv": ("id", "F20", [
        ["F20", "گرهها عین میمو", "done/cur/half/locked/bolt + اتور Q + START + واژهنامه؛ ۹۲px / ۲۶dp / لبهٔ ۸px", "DESIGN/NODE_CODE_GEOMETRY.json + mimo-01/02/10 (VISUAL_CROSSCHECK_ONLY)"],
        ["F21", "تمرین مبحث ≠ آزمون کنکور", "data-scope=learn-practice · class=screen mimo · بدون تایمر/پاسخبرگ/پاسخنامه/POLICY", "CATALOGS/PRACTICE_VS_EXAM.csv"],
        ["F22", "روتین روزانه پوستهٔ میمو", "فقط توکنها و وکتورهای استخراجشدهٔ میمو؛ بدون آواتار/پیکسلآرت/رنگ/فونت/شعاع/آیکون تازه", "CATALOGS/DESIGN_TOKENS.json + CATALOGS/HABITICA_SOURCES.csv"],
        ["F23", "شش تب، MAX ممنوع", "Learn/Practice/AI/Leaderboard/Profile/روتین روزانه؛ data-tab=MAX وجود ندارد", "بازخورد صریح v7 + D26"],
    ]),
    "AI_PANEL_SPEC.csv": ("element", "ai_top_attach_file", [
        ["ai_top_attach_file", "گیرهٔ کاغذ (attachment.xml) + لیبل کوتاه «اضافه کردن فایل»؛ جایگزین ایموجی زنجیر/import", "VISIBLE (ai top row)", "Mimo res/drawable/attachment.xml + ic_file.xml"],
        ["ai_top_conversation_chain", "ic_link_external + «زنجیره گفت و گو» کنار دکمهٔ فایل؛ ردیف مرتب و ایکون متمایز", "VISIBLE (ai top row)", "Mimo res/drawable/ic_link_external.xml + ic_chat_bubble.xml"],
        ["ai_foot_single_line", "TEACH / PRACTICE ریز و همان یک خط با Dictate، gemini-flash-lite-latest و medium؛ flex-wrap:nowrap", "VISIBLE (ai composer foot)", "بازخورد v7 + Mimo ic_chevron_down.xml"],
        ["ai_foot_dictate_voice", "Dictate برای ویس، با ic_microphone، در همان خط باقی ماند (جدا/حذف نشد)", "VISIBLE (ai composer foot)", "Mimo res/drawable/ic_microphone.xml"],
    ]),
    "OPEN_QUESTIONS.csv": ("id", "U06", [
        ["U06", "آیا «روتین روزانه» تب ششم مستقل است یا داخل پروفایل؟", "ASSUMED: تب ششم مستطب و کمسر و صدا، طبق «در نوار پایین یه بخش دیگریم باید اضافه بشود»؛ MAX ممنوع", "no", "تأیید نهایی دیزاین"],
        ["U07", "کدام نام کوتاه برای دکمهٔ فایل: «الصاق فایل» یا «اضافه کردن فایل»؟", "ASSUMED: «اضافه کردن فایل» (کوتاهترین واضح)؛ «الصاق فایل» بهعنوان مترادف در لاگ ثبت شد", "no", "تأیید نهایی دیزاین"],
    ]),
}

for name, (idcol, first_id, new_rows) in APPEND.items():
    p = CAT / name
    with p.open(encoding="utf-8", newline="") as f:
        existing = list(csv.reader(f))
    header, body = existing[0], existing[1:]
    present = {r[0] for r in body if r}
    todo = [r for r in new_rows if r[0] not in present]
    if todo:
        with p.open("a", encoding="utf-8", newline="") as f:
            csv.writer(f).writerows(todo)
    print(name, "appended", len(todo), "rows ->", len(body) + len(todo))

# --------------------------------------------------------------------------
# 2. v7 docs
# --------------------------------------------------------------------------
DOC18 = r'''# دور هفتم طراحی — DESIGN v7 (گرهها، تمرین مبحث، روتین روزانه)

> **وضعیت:** `DESIGN v7 · REVIEW` — منتظر تأیید نهایی. همچنان **فقط پلن/دیزاین**؛ هیچ کد محصولی نوشته نشده.
> **روش:** کندوکاو **عمیقتر از داخل کد APK** (`values/values/string.xml`، `res/drawable/*.xml`، `res/layout/*.xml`، `res/anim/*`، `res/raw/practice.riv`، `test-tracks.json`، DEX) + قواعد امتیازدهی Habitica فقط بهصورت خلاصهشده. اسکرینشاتها فقط **چک بصری**. جایگزین `17_DESIGN_ROUND_6.md` است.
> **گفتۀ شما:** «خیلی خیلی خیلی خوبه … ولی چند تا اصلاح ریز مونده».

---

## ۱. گرههای مسیر یادگیری (code-first)

ابزار تازه `tools/extract_mimo_nodes_v7.py` → `DESIGN/NODE_CODE_GEOMETRY.json` (۱۱۶٬۸۴۹ بایت) و `CATALOGS/MIMO_PATH_NODES.csv` (۵۰ ردیف). شمارش: **۵۵ وکتور دقیق `android:pathData`** (بدون خطا)، **۱۴۱ رشتهٔ ARSC**، **۱۷ لایهٔ AXML**، **۲ انیمیشن checkpoint**، `practice.riv`، **۱۵ فصل / ۲۲۳ شناسهٔ `tutorialId`** از `test-tracks.json`، **۳۸۰ کلاس DEX** و ۴۰ لیترال DEX.

| گره | شکل | سند کد | چک بصری |
|---|---|---|---|
| انجامشده | مربع ۹۲px، شعاع ۲۶dp، گرادیان بنفش، لبهٔ سهبعدی ۸px، `ic_check_white` | `button_primary_highlight`, `cardview_corner_radius_large`, `PathMapScreenKt` | mimo-10, mimo-01 |
| فعلی | کارت سفید + حلقهٔ دوتایی بنفش + `ic_play`، برچسب START | `chapter_toolbar.xml`, `progress_bar_mimo.xml`, `start_lesson` | mimo-01 |
| نیمهتمام | حلقهٔ ½ (conic) روی کارت سفید | `glance_circular_progress_indicator.xml` | mimo-02 |
| قفل | `card_disabled` + `ic_lock_alt_02` | `alert_msg_section_setion_locked` | mimo-01 |
| رعدوبرق | `ic_bolt` / `ic_bolt_charged` / `ic_bolt_mastered`، مربع بنفش یا روشن | `ic_practice_tab_locked`, `res/raw/practice.riv`, `rc_checkpoint_window_enter/exit` (alpha ۲۲۰ms) | mimo-01, mimo-10 |
| اتور | مسیر **Q با گوشهٔ گرد** (راست/پایین/چپ/پایین)، نه منحنی بزیه v6 | `PathMapScreenKt` (۷۳ کلاس)، `progress_chapter_primary` | mimo-10 |
| شناور | دایرهٔ کوچک کتاب/واژهنامه (A) | `ic_file.xml` + `bookmark_no_fill.xml` | mimo-01 |

کد ملاک است: اختلاف `mimo-01` (دو چیپ و کارت فصل ۱۲٪) با `mimo-10` (سه چیپ و کارت نمای مسیر) با **حکم v6 + کد** حل شد؛ ساختار گرهها، اتور و نقطهچین ۲۶px از کد آمدند و عکسها فقط چک شدند. فقط **نام درس/مبحث** کنکوری است. ۰ رنگ/فونت/شعاع/آیکون تازه.

## ۲. گره رعدوبرق ← «تمرین مبحث تا همان فصل» (جدا از آزمون)

صفحهٔ تازهٔ `data-screen="section-practice"` (`class="screen mimo"`, `data-scope="learn-practice"`):

- صورت ۳ سؤال از `test-tracks.json → sections[].tutorialIds` **تا همان فصل** رندر میشود (گرهٔ ۳ ← ۶۱ درس، گرهٔ ۵ ← ۹۰ درس).
- چیدمان سؤال/گزینه از `lesson_interactive_multiplechoice_fragment.xml` + `lesson_interaction_selection_item_layout.xml`؛ فیدبک از `lesson_feedback_keep_going`.
- دیالوگها دقیقاً از ARSC: `section_details_smart_practice_charged_dialog_title = Fully charged!`، `mastered_dialog_title = You've mastered the section!`، `practice_anyway = Practice anyway`، `you_finished_all_practice_sessions`. ماسکات `ic_mascot_practice`، DEX `ModalData$SmartPracticeChargedModal/MasteredModal`.
- **تفکیک سهگانه** (جدول کامل `CATALOGS/PRACTICE_VS_EXAM.csv`، ۱۲ ردیف): تمرین مبحث / آزمون کنکور / روتین روزانه. در تمرین مبحث هیچ `timerChip`، `پاسخبرگ`، `پاسخنامه`، `POLICY`، ۲۷۰ دقیقه، هاب آزمون یا دکمهٔ «توضیح با هوش مصنوعی» وجود ندارد. آزمون کنکور همچنان `exam-hub / exam-run / exam-result` است.

## ۳. چت AI: بالا مرتب، پایین تکخط

- بالا: ایموجیها حذف شدند → **گیرهٔ کاغذ** `attachment.xml` + «**اضافه کردن فایل**» (کوتاهترین واضح؛ «الصاق فایل» مترادف)، و `ic_link_external` + «**زنجیره گفت و گو**». دو چیپ در یک ردیف، آیکون متمایز، بدون شلوغی. ۸ دکمهٔ LH پنل اصلی حفظ شد.
- پایین: **TEACH / PRACTICE ریز** و در **همان یک خط** `Dictate` (با `ic_microphone`، ویس — جدا/حذف نشد)، `gemini-flash-lite-latest` و `medium` (chevron). `flex-wrap:nowrap`، فونت ۹px.
- چت همچنان مینیمال + تاریخچه + تکدکمهٔ «توضیح با هوش مصنوعی» در صفحهٔ سؤالات و نتیجه. «وارد کردن کلید API» فقط یادداشت الزام، بدون UI.

## ۴. صفحهٔ سؤال و لیدربورد

- دو دکمهٔ تمیز **«سؤال قبل» / «سؤال بعد»** (با `ic_arrow_left` / `ic_arrow_right`) در ردیف `qnav`.
- پایینش **یک خط** sticky و کمضخامت (`qfoot`): «پاسخبرگ»، «پاسخنامه»، «خروج»، «اتمام آزمون»، «توضیح با هوش مصنوعی»، «توقف»، «تنظیم مجدد» — `font-weight:400`، بدون `btn primary`، بدون حجیمسازی. همان الگو در صفحهٔ نتیجه (`result-foot`).
- **Promotion Zone / «منطقهٔ صعود» حذف شد**؛ `selfbox` و اطلاعات/امتیازات/آزمونهای خود فرد پابرجا. تایمر و سیاست پاسخبرگ/پاسخنامه دستنخورده.

## ۵. روتین روزانه (تب ششم)

دستور صریح: «در نوار پایین یه بخش دیگریم باید اضافه بشود به اسم روتین روزانه … از این پروژه استفاده کن سیستم امتیازدهیش و هیچی قرار نیست قاتی بشه با اپلیکیشن خود ما … یه جوری باشه فکر کنن برای میمو هست نه خود اپلیکیشن ینی زیادی تو چشم نزنه».

- تب ششم **کمسر و صدا** `Routine` با `ic_calendar` / `ic_task_completed`؛ فونت ۹px؛ **MAX همچنان ممنوع**. حکم قبلی «۵ تب» ناظر به جلوگیری از تب MAX بود و اینک بهروزرسانی شد (`D26`).
- `DESIGN/HABITICA_SCORING.json` + `CATALOGS/HABITICA_SOURCES.csv` (۱۳ فایل منبع با SHA-256، کامیت `12091ca02990533fdf38c2f0947397f0b4e39d59`، شاخهٔ `develop`) + `CATALOGS/HABITICA_SCORING.csv` (۲۲ قاعده) + `19_HABITICA_ROUTINE_SPEC.md`.
- پیادهمسازی تعاملی: چهار نوع کار (عادت / روزانه / کار امروز / پاداش)، ضریب سختی `0.1 / 1 / 1.5 / 2`، نوار XP/سطح، سکهٔ روتین، استریک، سلامت و Perfect Day. فرمولها به زبان خودمان بازنویسی شدند: `delta = 0.9747^value`، `EXP = round(delta × (1+INT×0.025) × priority × crit × 6)`، `GP = ceil(delta × priority × crit × (1+PER×0.02) × (streak/100+1))`، `HP` با `CON`، `crit` قطعی، `toNextLevel`، `diminishingReturns`، ۲۱ روز.
- **ایزولاسیون کامل**: امتیازات روتین به آزمونها، لیدربورد، سکههای Learn یا چت وصل نیست؛ هیچ کد/دارایی/رشته/فونت/رنگ/آیکونی از Habitica کپی نشده (کد آن GPL-3.0 و داراییها CC-BY-NC-SA است)؛ پوسته فقط توکنها و وکتورهای استخراجشدهٔ میمو. جزئیات حقوقی و قواعد در `19_HABITICA_ROUTINE_SPEC.md`.

## ۶. حفظشده / وضعیت

هاب تکصفحهای ۷ بخش لیبلدار · تایمر فقط داخل آزمون (کلیک ← عدد ← شروع ← معکوس، توقف/ادامه، ثبت خودکار در صفر) · جامع ۲۷۰ دقیقهٔ ثابت · «پاسخبرگ» ≠ «پاسخنامه» و بازشدن خودکار کلید در زمان خالص · تکدکمهٔ AI در سؤالات و نتیجه · لیدربورد اطلاعات خود فرد · چت مینیمال + تاریخچه · مشاوره **PARKED** · بدون Pro/پرداخت/MAX · صفحهٔ ورود حذفشده · RTL + حالت شب · ۱۴ اسکرینشات فقط چک بصری.

**DESIGN v6** بایگانی شد. خروجی نهایی: `DESIGN/index.html` (۱۵ نمای تعاملی، ۶ تب، ۹۰ وکتور SVG، ۱۲۵/۱۲۵ آیکن رنگشده، ۰ خطای jsdom). **منتظر تأیید نهایی شما**؛ بعد از «مرحلهٔ بعد» تازه P0 پیادهمسازی شروع میشود.
'''

DOC19 = r'''# روتین روزانه — فقط «سیستم امتیازدهی» Habitica در پوستهٔ میمو

> **وضعیت:** بخشی از `DESIGN v7 · REVIEW`؛ فقط طراحی، هیچ کد محصولی نوشته نشده.
> **دستور کاربر:** «از این پروژه استفاده کن سیستم امتیاز دهیش و هیچی قرار نیست قاتی بشه با اپلیکیشن خود ما صرفا رابط کاربریش رو نمیخواد زیادی تغییر بدی ولی یه جوری باشه فکر کنن برای میمو هست نه خود اپلیکیشن ینی زیادی تو چشم نزنه».
> **تفسیر:** فقط **قواعد امتیازدهی**؛ پوستهٔ کمسر و صدای میمو؛ ایزوله از بقیهٔ اپ؛ بدون دارایی/کد/محتوای Habitica.

---

## ۱. منبع و پاکی حقوقی

| مورد | مقدار |
|---|---|
| مخزن | `https://github.com/habitrpg/habitica` |
| شاخه | `develop` |
| کامیت | `12091ca02990533fdf38c2f0947397f0b4e39d59` |
| پروانه | کد GPL-3.0؛ داراییهای BrowserQuest CC-BY-SA 3.0؛ داراییها/محتوای HabitRPG CC-BY-NC-SA 3.0 |
| فایلهای خواندهشده | ۱۳ فایل، فقط در `/home/user/_work/hab/` (خارج از مخزن تحویلی) |
| چیزی که وارد مخزن شد | **فقط** SHA-256 هر فایل، مسیر upstream، نقش، و خلاصهٔ قواعد به زبان خودمان |
| چیزی که وارد نشد | هیچ خط کد، رشته، دارایی، فونت، رنگ، آیکون، لیبل یا چیدمانی |

فهرست دقیق: `CATALOGS/HABITICA_SOURCES.csv` (۱۳ ردیف) و `CATALOGS/HABITICA_SCORING.csv` (۲۲ ردیف). شواهد ماشینی: `DESIGN/HABITICA_SCORING.json`.

## ۲. قواعد امتیازدهی (بازنویسیشده، نه کپیشده)

| id | قاعده | نگاشت میمو |
|---|---|---|
| HS-01 | چهار نوع کار: habit (+/−)، daily (تیک + استریک)، todo (یکباره + چکلیست)، reward (خرج سکه، بدون delta) | چهار ردیف روتین |
| HS-02 | پیشفرض: `priority=1`، `value=0`، پاداش `value=10`، استریک ۰ | مقادیر اولیه |
| HS-03 | ضرایب سختی `0.1 / 1 / 1.5 / 2` (Trivial/Easy/Medium/Hard) | چیپ ریز روی هر کار |
| HS-04 | `value` محدود به `[-47.27, 21.27]` | محدودکنندهٔ داخلی |
| HS-05 | `delta = 0.9747 ^ clamp(value)`، علامت بر اساس جهت؛ برداشتن تیک معکوس همان delta | امتیاز نرم صعودی/نزولی |
| HS-06 | چکلیست: سهم `completed/total` | چکلیستهای کوچک |
| HS-07 | `exp += round(delta × (1+INT×0.025) × priority × crit × 6)` | نوار XP |
| HS-08 | `gp += ceil(delta × priority × crit × (1+PER×0.02) × (streak/100+1))` | سکهٔ روتین |
| HS-09 | کاهش `hp = delta × (1−min(CON,100)/250 clamp≥0.1) × priority × 2`، سقف ۵۰ | نوار سلامت کمسر و صدا |
| HS-10 | شانس `crit = 0.03×(1+STR/100)`، ضریب `1.5 + 4×STR/(STR+200)` | ضریب شانس اختیاری |
| HS-11 | `predictableRandom` قطعی (seed سینوسی) | منطق قابل تکرار، بدون RNG واقعی |
| HS-12 | `toNextLevel(l) = 25l` (l<5)، `150` (l=5)، `round((l²×0.25+10l+139.75)/10)×10` | سطح و نوار پیشرفت |
| HS-13 | عبور از سطح: `lvl+1`، HP کامل، کسر آستانه، +۱ استات (سقف ۱۰۰) | بدون بنر پر زرقوبرق |
| HS-14 | `diminishingReturns(b,max) = max×b/(b+max/2)` | جلوگیری از انفجار امتیاز |
| HS-15 | MP مثبت، سقف `maxMP` | فقط ثبت شده، در UI نمیآید |
| HS-16 | تکمیل daily → استریک +۱؛ هر ۲۱ روز نشان؛ cron ریست روزانه | شمارندهٔ «روز پیاپی» |
| HS-17 | Perfect Day (همهٔ dailyها) → باف/نشان؛ `max(10,0.1×maxMP) × checked/(due+checked)` | نشان ریز «روز کامل» |
| HS-18 | cron روزانه: Missed-daily damage در `dayStart`، `multiDaysCountAsOneDay=true` | منطق پسزمینه، بدون اعلان پر سر و صدا |
| HS-19 | reward: `gp -= value`، بدون delta/EXP/HP | پاداش کوچک |
| HS-20 | تمام قواعد **فقط** در `data-screen=routine` | «هیچی قاتی نشه» |
| HS-21 | پروانهٔ GPL/CC؛ فقط قواعد + SHA-256 | پاکسازی حقوقی |
| HS-22 | فقط توکنها و وکتورهای میمو؛ بدون پیکسلآرت/آواتار/رنگ/فونت/شعاع تازه | «فکر کنن برای میمو هست» |

## ۳. ایزولاسیون (سهگانه)

1. `data-screen="section-practice"` = تمرین مبحث (از گره رعدوبرق Learn). بدون تایمر/پاسخبرگ/پاسخنامه/۲۷۰ دقیقه.
2. `exam-hub / exam-run / exam-result` = آزمون کنکور. ۷ بخش، تایمر فقط داخل آزمون، پاسخبرگ ≠ پاسخنامه، جامع ۲۷۰ دقیقه.
3. `data-screen="routine" data-scope="routine-only"` = روتین. امتیازاتش **به هیچجای دیگر وصل نیست** (نه نمرهٔ آزمون، نه XP لیدربورد، نه سکههای `1,272`، نه پیشرفت Learn، نه چت AI).

جدول تفکیک: `CATALOGS/PRACTICE_VS_EXAM.csv` (۱۲ ردیف). قوانین ایزولاسیون در `DESIGN/HABITICA_SCORING.json → isolation` (۶ بند).

## ۴. پوسته (Mimo، low-key)

- تنها توکنهای `CATALOGS/DESIGN_TOKENS.json`: `background_primary`, `card_enabled`, `card_pressed`, `button_primary`, `progress_chapter_primary`, `text_primary`, `text_weak`, `line_secondary`, `TextLabel*`, شعاع ۱۲/۱۶/۲۴dp و فاصلههای ۸/۱۲/۱۶/۲۴dp.
- تنها وکتورهای استخراجشده: `ic_calendar`, `ic_task_completed`, `ic_sparks`, `ic_sparks_alt`, `ic_streak_active`, `ic_coin`, `ic_check_white`, `ic_plus`, `ic_chevron_down`.
- رنگ/فونت/شعاع/آیکون **تازه: ۰**. تابلوها، مدال RPG، آواتار، پیکسلآرت، بنرهای درشت و لیبلهای انگلیسی Habitica: **۰**. فونت تب ۹px، کارتها ۱۴px رادیوس، نوار ۶px. «زیادی تو چشم نزنه».
- نمای پیشفرض همان LTR میمو + دکمهٔ «فارسی / RTL» و «حالت شب»؛ APK هیچ کوالیفایر RTL ندارد.

## ۵. نکتهٔ حسابرسی

دو ابهام کوچک در `CATALOGS/OPEN_QUESTIONS.csv` بهصورت `ASSUMED` و غیربلاککننده ثبت شد: (U06) مستقل بودن تب ششم؛ (U07) انتخاب «اضافه کردن فایل» بهجای «الصاق فایل». هر دو در تأیید نهایی قابل برگشتاند. تا آن زمان **هیچ پیادهمسازی محصولی** انجام نمیشود.
'''

NOTES = r'''# یادداشتهای طراحی — DESIGN v7

> نسخهٔ جاری: **DESIGN v7 · REVIEW** (منتظر تأیید نهایی). نسخهٔ **DESIGN v6** و پیش از آن بایگانی حسابرسیاند. همچنان **فقط پلن/دیزاین**؛ هیچ کد محصولی نوشته نشده است.

## ۱. اصل حاکم

بازآفرینی ۱۰۰٪ بخشهای اصلی میمو **از داخل کد و مهندسی معکوس**، نه از روی عکس. جداول منبع Mimo 9.35: `CATALOGS/DESIGN_TOKENS.json` (ARSC)، `SOURCE/values/values/string.xml`، `SOURCE/res/drawable/*.xml` (`android:pathData`)، `SOURCE/res/layout/*.xml`، `SOURCE/res/anim/*`، `SOURCE/res/raw/practice.riv`، `SOURCE/assets/ui/testdata/test-tracks.json`، `SOURCE/dex/UI_CLASSES.json`. ۱۴ اسکرینشات پیوستشده فقط `VISUAL_CROSSCHECK_ONLY`اند. فقط **نام درسها/فصلها/مباحث** کنکوری میشود؛ ۰ رنگ/فونت/شعاع/آیکون تازه.

## ۲. هفت اصلاح دور هفتم

1. **گرهها دقیق شدند**: مربع ۹۲px با لبهٔ سهبعدی ۸px، تیک بنفش، کارت سفید حلقهدار + `ic_play`، حلقهٔ ½، قفل، اتور **گردگوشه Q**، نقطهچین، برچسب START و دکمهٔ شناور واژهنامه. شواهد: `DESIGN/NODE_CODE_GEOMETRY.json` + `CATALOGS/MIMO_PATH_NODES.csv` (۵۰ ردیف).
2. **رعدوبرقها → «تمرین مبحث تا همان فصل»**: `data-screen="section-practice"` جدا از هاب آزمون؛ صورت سؤالها از `sections[].tutorialIds`؛ دیالوگهای `Fully charged!` / `You’ve mastered the section!` / `Practice anyway`. جدول تفکیک: `CATALOGS/PRACTICE_VS_EXAM.csv`.
3. **بالای AI مرتب**: `attachment` + «اضافه کردن فایل» و `ic_link_external` + «زنجیره گفت و گو»؛ بدون ایموجی.
4. **پایین AI تکخط**: «آموزش / TEACH» و «تمرین / PRACTICE» ریز در همان خط `Dictate` (میکروفن، ویس، جدا نشد)، `gemini-flash-lite-latest` و `medium`.
5. **صفحهٔ سؤال**: «سؤال قبل» + «سؤال بعد» دو دکمهٔ تمیز؛ زیرشان یک خط کمضخامت شامل «پاسخبرگ» و بقیهٔ کنترلها، بدون bold.
6. **لیدربورد**: `Promotion Zone` حذف؛ `selfbox` و اطلاعات خود فرد پابرجا.
7. **تب ششم «روتین روزانه»**: فقط **سیستم امتیازدهی** Habitica (۲۲ قاعده / ۱۳ SHA-256 / کامیت `12091ca…`) در پوستهٔ کمسر و صدای میمو؛ ایزوله؛ MAX ممنوع. مستندات: `19_HABITICA_ROUTINE_SPEC.md`.

## ۳. آنچه دستنخورده ماند

هاب آزمون تکصفحهای با ۷ بخش لیبلدار و قالبهای فیلد · تایمر فقط داخل آزمون (کلیک chip ← عدد ← شروع ← شمارش معکوس، توقف/ادامه، ثبت خودکار در صفر) · آزمون جامع ۲۷۰ دقیقهٔ ثابت · «**پاسخبرگ**» = گزینههای زدهشده ≠ «**پاسخنامه**» = جواب تشریحی + کلید تستی · آزمونهای زمان خالص هیچکدام را حین آزمون نشان نمیدهند و در پایان کلید خودکار باز میشود · **یک** دکمهٔ «توضیح با هوش مصنوعی» در صفحهٔ سؤالات و **همان** دکمه در نتیجه (صورت اشتباهات + پاسخهای کاربر + پاسخ صحیح → چت) · لیدربورد اطلاعات/امتیازات/آزمونهای خود فرد · چت مینیمال + تاریخچه + ۸ دکمهٔ LH · «وارد کردن کلید API» فقط یادداشت الزام · مشاوره `PARKED` · بدون Pro/پرداخت/MAX · صفحهٔ ورود حذفشده · RTL/فارسی + حالت شب.

## ۴. تفکیک سهگانه (مهم)

| سطح | جا | نشانه |
|---|---|---|
| تمرین مبحث | `data-screen=section-practice` | `mimo`، بدون تایمر/پاسخبرگ/پاسخنامه/POLICY/۲۷۰ |
| آزمون کنکور | `exam-hub / exam-run / exam-result` | `konkur`، ۷ بخش، تایمر داخل آزمون، پاسخبرگ ≠ پاسخنامه |
| روتین روزانه | `data-screen=routine` | `mimo`، فقط قواعد امتیازدهی، امتیازات ایزوله |

## ۵. حقوقی / clean-room

هیچ دارایی، فونت، رشته یا کدی از Mimo 9.35، Hamdars 7.4.4، Hadaf Plus 2.0.2، LearnHarness، EPM یا Habitica کپی نشده است. از Habitica **فقط قواعد انتزاعی امتیازدهی** به زبان خودمان + SHA-256 منابع ثبت شد (کد آن GPL-3.0، داراییها CC-BY-NC-SA). subscription/cart/Pro هدفپلاس و اسکرینشات رانتایم/امولاتور ممنوعاند.

## ۶. شواهد و اعتبارسنجی

`DESIGN/CODE_GEOMETRY.json` (v5) + `DESIGN/LEARN_CODE_GEOMETRY.json` (v6) + `DESIGN/NODE_CODE_GEOMETRY.json` (v7) + `DESIGN/HABITICA_SCORING.json` (v7) → `tools/build_design_v7.py` → `DESIGN/index.html`. خروجی: ۱۵ نمای تعاملی، ۶ تب، ۹۰ وکتور SVG، ۱۲۵/۱۲۵ آیکن رنگشده، `node --check` OK، jsdom ۰ خطا، ۴۱ تست جریان (گرهها، بولت، روتین، تایمر، پاسخبرگ، AI، RTL، شب). `tools/verify_upgrade.py` و `CATALOGS/VERIFICATION_REPORT.json` حسابرسی نهاییاند.

## ۷. بعد از این

منتظر **تأیید نهایی** شما. فقط بعد از گفتن «مرحلهٔ بعد» پیادهمسازی P0 آغاز میشود؛ تا آن لحظه هیچ کد محصولی نوشته نشده است.
'''

(UP / "18_DESIGN_ROUND_7.md").write_text(DOC18, encoding="utf-8")
(UP / "19_HABITICA_ROUTINE_SPEC.md").write_text(DOC19, encoding="utf-8")
(D / "DESIGN_NOTES.fa.md").write_text(NOTES, encoding="utf-8")
print("docs written")

# --------------------------------------------------------------------------
# 3. v7 banners on archived docs (idempotent)
# --------------------------------------------------------------------------
for p in sorted(UP.glob("*.md")):
    s = p.read_text(encoding="utf-8")
    if MARK in s:
        continue
    current = p.name.startswith("18_") or p.name.startswith("19_")
    banner = (MARK + "\n> " + ("✅ **DESIGN v7 · CURRENT** — لاگ دور هفتم؛ جایگزین نسخههای قبل. "
                              if current else
                              "⚠️ **بایگانی / superseded:** طراحی فعلی **[DESIGN v7](18_DESIGN_ROUND_7.md)** است. ")
              + "همچنان فقط پلن/دیزاین؛ هیچ کد محصولی نوشته نشده.")
    lines = s.split("\n")
    insert_at = 1 if lines and lines[0].startswith("#") else 0
    lines.insert(insert_at, banner)
    p.write_text("\n".join(lines), encoding="utf-8")
print("banners written")

wf = UP / "wireframes.html"
s = wf.read_text(encoding="utf-8")
old = '''<div style="background:#FFF7E6;border:2px solid #7E4BDE;color:#252746;padding:12px 18px;font:700 14px Tahoma,sans-serif;text-align:center">⚠️ وایرفریم v1 بایگانی شد — طراحی فعلی <a href="DESIGN/index.html">DESIGN v6</a> است (حذف صفحهٔ ورود، بازسازی یادگیری، افزودن انتخاب مسیر / نمای مسیر / داخل مبحث). <a href="17_DESIGN_ROUND_6.md">لاگ دور ششم</a></div>'''
new = '''<div style="background:#FFF7E6;border:2px solid #7E4BDE;color:#252746;padding:12px 18px;font:700 14px Tahoma,sans-serif;text-align:center">⚠️ وایرفریم v1 بایگانی شد — طراحی فعلی <a href="DESIGN/index.html">DESIGN v7</a> است (گرههای دقیق، تمرین مبحث جدا از آزمون، روتین روزانه). <a href="18_DESIGN_ROUND_7.md">لاگ دور هفتم</a></div>'''
if old in s:
    s = s.replace(old, new, 1)
    wf.write_text(s, encoding="utf-8")
    print("wireframes banner updated")
elif "DESIGN v7" not in s:
    raise SystemExit("wireframes banner anchor not found")

# --------------------------------------------------------------------------
# 4. MANIFEST.json
# --------------------------------------------------------------------------
mp = UP / "MANIFEST.json"
m = json.loads(mp.read_text(encoding="utf-8"))
files = sorted(p for p in UP.rglob("*") if p.is_file())
m["date"] = "2026-11-04"
m["status"] = "PLAN_ONLY + DESIGN v7 REVIEW (no product implementation)"
dl = m["deliverables"]
dl["persian_docs"] = 21
dl["csv_catalogs"] = 22
dl["extracted_assets_files"] = len(files)
dl["total_bytes"] = sum(p.stat().st_size for p in files)
dl["verification"] = "PASS"
dl["interactive_design_prototype"] = 1
dl["verification_checks"] = 174  # matches tools/verify_upgrade.py final check total
dl["design_round"] = "v7 (REVIEW)"
dl["design_views"] = 15
dl["design_svg_vectors"] = 90
dl["node_code_evidence"] = ("DESIGN/NODE_CODE_GEOMETRY.json (55 vectors / 141 ARSC strings / 17 AXML layouts / "
                            "2 checkpoint animations / practice.riv / 15 sections / 223 tutorialIds / 380 DEX classes) "
                            "+ CATALOGS/MIMO_PATH_NODES.csv (50 rows)")
dl["habitica_scoring_evidence"] = ("DESIGN/HABITICA_SCORING.json (22 rules / 13 upstream SHA-256 / 4 task types / 6 isolation rules) "
                                    "+ CATALOGS/HABITICA_SOURCES.csv + CATALOGS/HABITICA_SCORING.csv + CATALOGS/PRACTICE_VS_EXAM.csv")
dl["bottom_nav_tabs"] = 6
dl["reference_screenshots_role"] = "14 Mimo screenshots, VISUAL_CROSSCHECK_ONLY"
sh = m["source_hashes"]
sh["habitica_develop_commit"] = "12091ca02990533fdf38c2f0947397f0b4e39d59"
sh["habitica_scoreTask_js"] = "fc1d6b5b61b254242876c4cf0c3122b6d8530ea63c4a057d9cd73221d27e3aec"
sh["habitica_statHelpers_js"] = "87e4e7324b318bbb04be6465b1b3ef8509bb309b3c93b09956e02f233dcdaa03"
cf = m["critical_findings"]
v7 = [
    "v7: path-map NODES corrected from code (done 3D-lip squares, white double-ring play, 1/2 ring, locked square, rounded-elbow Q connector, START bubble, floating glossary) — screenshots only cross-check",
    "v7: lightning-bolt nodes open an ISOLATED section-practice checkpoint quiz from tutorialIds up to that section; never mixed with the Konkur exam hub",
    "v7: AI header chain/import emoji replaced by Mimo attachment/file icons + short Persian labels «اضافه کردن فایل» / «زنجیره گفت و گو»",
    "v7: TEACH/PRACTICE miniaturised onto the SAME bottom line as Dictate (mic = voice), gemini-flash-lite-latest and medium",
    "v7: exam question page has two clean prev/next buttons; answer sheet + other controls in ONE quiet bottom line; Promotion Zone removed from leaderboard",
    "v7: 6th low-key Mimo-skinned tab «روتین روزانه» uses ONLY Habitica scoring-system rules (22 rules / 13 SHA-256), no Habitica code/assets/content, fully isolated; MAX still forbidden",
]
for x in v7:
    if x not in cf:
        cf.append(x)
rep = m["reproduce"]
for cmd in ["python3 tools/extract_mimo_nodes_v7.py .",
            "python3 tools/write_habitica_spec.py .",
            "python3 tools/build_design_v7.py .",
            "python3 tools/finalize_v7.py .",
            "python3 tools/verify_upgrade.py ."]:
    if cmd not in rep:
        rep.append(cmd)
m["design_round_6"]["status"] = "DESIGN v6 · SUPERSEDED by DESIGN v7 (18_DESIGN_ROUND_7.md) — archived audit trail"
m["design_round_7"] = {
    "status": "DESIGN v7 · REVIEW — awaiting final approval (CURRENT)",
    "trigger": "user: خیلی خیلی خیلی خوبه ولی ۷ اصلاح ریز + لینک Habitica «سیستم امتیازدهیش»",
    "method": "CODE_FIRST / extract_mimo_nodes_v7.py + write_habitica_spec.py -> NODE_CODE_GEOMETRY.json + HABITICA_SCORING.json -> build_design_v7.py -> DESIGN/index.html",
    "interactive_prototype": "DESIGN/index.html (15 views / 6 tabs / 90 SVG vectors / 125 painted icons / 0 jsdom errors)",
    "new_screens": ["section-practice (bolt checkpoint quiz, LEARN only)", "routine (Habitica scoring only, Mimo skin)"],
    "new_nav": "6 tabs: Learn / Practice / AI / Leaderboard / Profile / روتین روزانه (MAX forbidden)",
    "isolation": "section-practice ≠ exam-hub/run/result ≠ routine; CATALOGS/PRACTICE_VS_EXAM.csv",
    "habitica": "only abstract scoring rules + upstream SHA-256; GPL-3.0 / CC-BY-NC-SA respected; no copied code or assets",
    "final_log": "18_DESIGN_ROUND_7.md",
    "routine_spec": "19_HABITICA_ROUTINE_SPEC.md",
    "design_notes": "DESIGN/DESIGN_NOTES.fa.md",
    "final_approval": "PENDING — no product implementation until user says the design is final",
}
mp.write_text(json.dumps(m, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("MANIFEST updated; files=%d bytes=%d" % (len(files), sum(p.stat().st_size for p in files)))
