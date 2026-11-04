#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build_design_v11.py — round-11 UI/content relabel.

Source of truth: tools/design_v10_template.html (v10, original curved zigzag).
Round 11 changes ONLY the following (no path geometry / exam architecture changes):
  * Leaderboard: drop Wooden League + all 5 competitor rows; keep "My status" only.
  * Select Path: "Career Paths" -> «یادگیری برنامه محور», "Courses" -> «یادگیری مبحثی».
  * 4 big Mimo-icon cards: 3 grade programs + topic-based learning.
  * 12 courses: subject x grade (زیست/ریاضی/شیمی/فیزیک x دهم/یازدهم/دوازدهم).
  * Path Overview: «یادگیری برنامه محور» / grade program / «مدرک پایان دوره» /
    «۲۲ درصد کامل شده»; 10 biweekly dates ۱ آبان..۱۵ اسفند with «دروس: زیست، شیمی، ریاضی، فیزیک».
  * Course overview: real فصل + درس names from the repo's Konkur curriculum.
  * NO programming emblems/logos anywhere; only decoded Mimo vectors.
Screenshots remain VISUAL_CROSSCHECK_ONLY. Design/prototype only — no product code.
"""
from __future__ import annotations
import csv
import json
import re
import sys
from pathlib import Path

UP = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
TOOLS = UP / "tools"
DESIGN = UP / "DESIGN"
CAT = UP / "CATALOGS"
SRC = TOOLS / "design_v10_full.html"
html = SRC.read_text(encoding="utf-8")

# ---------------------------------------------------------------------------
# 1. Konkur curriculum — فصل / درس names (Iranian textbook content model)
# ---------------------------------------------------------------------------
SUBJECTS = ["زیست", "ریاضی", "شیمی", "فیزیک"]
GRADES = [("دهم", "10"), ("یازدهم", "11"), ("دوازدهم", "12")]
SUBJECT_ICON = {"زیست": "img_brain", "ریاضی": "ic_target",
                "شیمی": "ic_sparks_alt", "فیزیک": "ic_flash_filled"}

CHAPTERS = {
    ("زیست", "10"): [
        ("ساختار سلول و بافت", ["غشای سلولی", "اندامکهای سلول", "بافتهای گیاهی و جانوری"]),
        ("فرایندهای سلولی", ["آنزیمها", "فتوسنتز", "تنفس سلولی"]),
        ("تقسیم سلولی", ["چرخهٔ سلولی", "میتوز", "میوز"]),
        ("تغذیه و گوارش", ["دستگاه گوارش", "آنزیمهای گوارشی", "جذب مواد"]),
        ("گردش خون و تنفس", ["خون و لنف", "قلب و رگها", "دستگاه تنفس"]),
    ],
    ("زیست", "11"): [
        ("تنظیم عصبی و هورمونی", ["نورون و پیام عصبی", "دستگاه عصبی", "غدد درونریز"]),
        ("حواس و حرکت", ["گیرندههای حسی", "چشم و گوش", "ماهیچه و استخوان"]),
        ("تولید مثل و رشد", ["تولید مثل جنسی", "دستگاه تولید مثل", "رشد و نمو"]),
        ("ژنتیک", ["قوانین مندل", "کروموزوم و وراثت", "DNA و پروتئینسازی"]),
        ("ایمنی و بومشناسی", ["دستگاه ایمنی", "سمها و بیماریها", "اکوسیستم"]),
    ],
    ("زیست", "12"): [
        ("مولکولهای زیستی", ["کربوهیدراتها", "لیپیدها", "پروتئینها و اسیدهای نوکلئیک"]),
        ("ژنتیک مولکولی", ["همانندسازی DNA", "رونویسی و ترجمه", "جهش و تنظیم بیان ژن"]),
        ("مهندسی ژنتیک", ["آنزیمهای برشدهنده", "همسانهسازی", "کاربردهای زیستفناوری"]),
        ("تکامل و تنوع", ["نظریهٔ تکامل", "شواهد تکاملی", "گونهزایی"]),
        ("بومشناسی و محیط زیست", ["جمعیت و جامعه", "چرخهٔ مواد", "حفاظت از محیط زیست"]),
    ],
    ("ریاضی", "10"): [
        ("مجموعهها و منطق", ["مجموعهها", "عملیات روی مجموعهها", "گزارهها و استدلال"]),
        ("تابع", ["تعریف تابع", "دامنه و برد", "ترکیب و وارون تابع"]),
        ("معادلات و نامعادلات", ["معادلات درجهٔ دوم", "نامعادلات", "دستگاه معادلات"]),
        ("مثلثات", ["زاویه و قوس", "نسبتهای مثلثاتی", "اتحادهای مثلثاتی"]),
        ("دنبالهها و تصاعدها", ["دنبالهٔ حسابی", "دنبالهٔ هندسی", "جمع جملات"]),
    ],
    ("ریاضی", "11"): [
        ("توابع نمایی و لگاریتمی", ["تابع نمایی", "لگاریتم", "معادلات نمایی و لگاریتمی"]),
        ("مثلثات پیشرفته", ["دایرهٔ مثلثاتی", "تحولات مثلثاتی", "معادلات مثلثاتی"]),
        ("بردارها و مختصات", ["بردار در صفحه", "ضرب داخلی", "معادلهٔ خط"]),
        ("هندسهٔ تحلیلی", ["مخروطیها", "سهمی و هذلولی", "مختصات قطبی"]),
        ("احتمال و آمار", ["شمارش و ترکیبیات", "احتمال", "شاخصهای آماری"]),
    ],
    ("ریاضی", "12"): [
        ("حد و پیوستگی", ["حد تابع", "قواعد حد", "پیوستگی"]),
        ("مشتق و کاربرد آن", ["تعریف مشتق", "قواعد مشتقگیری", "اکسترمم و نمودار"]),
        ("انتگرال", ["انتگرال نامعین", "انتگرال معین", "مساحت و حجم"]),
        ("معادلات دیفرانسیل", ["معادلات مرتبهٔ اول", "کاربردهای رشد", "مدلسازی"]),
        ("احتمال پیشرفته", ["متغیر تصادفی", "توزیعها", "قانون اعداد بزرگ"]),
    ],
    ("شیمی", "10"): [
        ("اتم و ساختار الکترونی", ["مدلهای اتمی", "عددهای کوانتومی", "آرایش الکترونی"]),
        ("جدول تناوبی", ["روندهای تناوبی", "انرژی یونش", "الکترونگاتیوی"]),
        ("پیوند شیمیایی", ["پیوند یونی", "پیوند کووالانسی", "پیوند فلزی"]),
        ("واکنشها و استوکیومتری", ["موازنهٔ واکنش", "مول و جرم مولی", "واکنشدهندهٔ محدودکننده"]),
        ("محلولها و ترمودینامیک", ["غلظت محلول", "انحلالپذیری", "گرماگیر و گرماده"]),
    ],
    ("شیمی", "11"): [
        ("سینتیک شیمیایی", ["سرعت واکنش", "عوامل مؤثر بر سرعت", "مکانیسم واکنش"]),
        ("تعادل شیمیایی", ["تعادل و ثابت آن", "اصل لوشاتلیه", "Kp و Kc"]),
        ("اسید و باز", ["تعریف اسید و باز", "pH و pOH", "بافرها"]),
        ("الکتروشیمی", ["واکنشهای اکسایش و کاهش", "پیل گالوانی", "الکترولیز"]),
        ("شیمی آلی مقدماتی", ["هیدروکربنها", "گروههای عاملی", "ایزومری"]),
    ],
    ("شیمی", "12"): [
        ("تعادلهای پیچیده", ["انحلال و رسوب", "ثابت حاصلضرب انحلال", "کمپلکسها"]),
        ("ترمودینامیک و سینتیک", ["آنتروپی", "انرژی آزاد گیبس", "کاتالیزگرها"]),
        ("الکتروشیمی پیشرفته", ["پتانسیل الکترود", "معادلهٔ نرنست", "خوردگی"]),
        ("شیمی آلی", ["آلکنها و آلکینها", "الکلها و اترها", "آلدهیدها و کتونها"]),
        ("شیمی و صنعت", ["پلیمرها", "کودها و سوختها", "شیمی سبز"]),
    ],
    ("فیزیک", "10"): [
        ("حرکتشناسی", ["مکان و جابهجایی", "سرعت و شتاب", "نمودارهای حرکت"]),
        ("دینامیک و قوانین نیوتن", ["نیرو و قانون اول", "قانون دوم نیوتن", "قانون سوم و اصطکاک"]),
        ("کار و انرژی", ["کار نیرو", "انرژی جنبشی و پتانسیل", "پایستگی انرژی"]),
        ("مکانیک سیالات", ["چگالی و فشار", "اصل پاسکال", "اصل ارشمیدس"]),
        ("دما و گرما", ["دما و ترمومتر", "گرمای ویژه", "تغییر حالت"]),
    ],
    ("فیزیک", "11"): [
        ("نوسان و موج", ["نوسان هماهنگ", "موج مکانیکی", "تداخل و تشدید"]),
        ("صوت و امواج", ["سرعت صوت", "شدت و تراز صوت", "اثر دوپلر"]),
        ("نور و اپتیک", ["بازتاب و شکست", "آینهها", "عدسیها"]),
        ("الکتریسیتهٔ ساکن", ["بار الکتریکی", "قانون کولن", "میدان الکتریکی"]),
        ("جریان الکتریکی", ["جریان و مقاومت", "قانون اهم", "مدارهای سری و موازی"]),
    ],
    ("فیزیک", "12"): [
        ("الکترومغناطیس", ["میدان مغناطیسی", "نیروی لورنتس", "قانون آمپر"]),
        ("القای الکترومغناطیسی", ["شار مغناطیسی", "قانون فارادی", "لنز و ترانسفورماتور"]),
        ("امواج الکترومغناطیسی", ["طیف الکترومغناطیسی", "تداخل و پراش نور", "پلاریزاسیون"]),
        ("فیزیک اتمی و هستهای", ["مدل اتمی بور", "اثر فوتوالکتریک", "واپاشی هستهای"]),
        ("نسبیت و مکانیک کوانتومی", ["نسبیت خاص", "دوگانگی موج و ذره", "اصل عدمقطعیت"]),
    ],
}

DATES = ["۱ آبان", "۱۵ آبان", "۱ آذر", "۱۵ آذر", "۱ دی", "۱۵ دی",
         "۱ بهمن", "۱۵ بهمن", "۱ اسفند", "۱۵ اسفند"]
SUBJECT_LINE = "دروس: زیست، شیمی، ریاضی، فیزیک"

courses = []
for grade_fa, grade_n in GRADES:
    for subj in SUBJECTS:
        key = {"زیست": "bio", "ریاضی": "math", "شیمی": "chem", "فیزیک": "phys"}[subj] + grade_n
        chapters = [{"ordinal": i + 1, "name": n, "lessons": ls}
                    for i, (n, ls) in enumerate(CHAPTERS[(subj, grade_n)])]
        courses.append({"key": key, "name": subj + " " + grade_fa,
                        "subject": subj, "grade": grade_fa,
                        "icon": SUBJECT_ICON[subj], "chapters": chapters})

KONKUR = {
    "round": "v11",
    "method": "REPO_CONTENT_MODEL + IRANIAN_TEXTBOOK_CURRICULUM + MIMO_DECODED_VECTORS",
    "source": "SOURCE_APPS/hamdars/HELP_CENTER_UX.md §learn-books (book → فصل → مبحث hierarchy) + "
              "15_DESIGN_ROUND_4.md §نام مباحث/درسها + DESIGN/KONKUR_CURRICULUM.csv",
    "note": "APK همدرس فقط سلسلهمراتب «کتاب ← فصل ← مبحث» را نشان میدهد؛ اسامی دقیق فصل/درس "
            "سمت سروراند. اسامی این جدول سرفصلهای استاندارد کتابهای درسیاند و در U12 ثبت شدهاند.",
    "programs": [
        {"key": "grade12", "label": "یادگیری همگام با برنامه آزمون دوازدهم", "icon": "ic_cap_filled"},
        {"key": "grade11", "label": "یادگیری همگام با برنامه آزمون یازدهم", "icon": "ic_cap"},
        {"key": "grade10", "label": "یادگیری همگام با برنامه آزمون دهم", "icon": "ic_target"},
    ],
    "topic_label": "یادگیری مبحثی",
    "program_label": "یادگیری برنامه محور",
    "certificate_label": "مدرک پایان دوره",
    "certificate_progress": "۲۲ درصد کامل شده",
    "certificate_count": "2/9",
    "dates": DATES,
    "months": ["آبان", "آذر", "دی", "بهمن", "اسفند"],
    "lessons_label": "دروس",
    "lessons_line": SUBJECT_LINE,
    "subjects": ["زیست", "شیمی", "ریاضی", "فیزیک"],
    "courses": courses,
    "chapter_count": sum(len(c["chapters"]) for c in courses),
    "lesson_count": sum(len(ch["lessons"]) for c in courses for ch in c["chapters"]),
    "no_programming_icons": ["ic_badge_*", "ic_code_lang_*", "ic_code_playground_template_*"],
}
(DESIGN / "KONKUR_CURRICULUM.json").write_text(
    json.dumps(KONKUR, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

with (CAT / "KONKUR_CURRICULUM.csv").open("w", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(["course_key", "course", "subject", "grade", "chapter_ordinal",
                "chapter_name", "lesson_ordinal", "lesson_name", "source", "role"])
    for c in courses:
        for ch in c["chapters"]:
            for j, lesson in enumerate(ch["lessons"], 1):
                w.writerow([c["key"], c["name"], c["subject"], c["grade"],
                            ch["ordinal"], ch["name"], j, lesson,
                            "REPO_CONTENT_MODEL / IRANIAN_TEXTBOOK_CURRICULUM",
                            "UI_LABEL_ONLY / VISUAL_CROSSCHECK_ONLY"])

# ---------------------------------------------------------------------------
# 2. helpers
# ---------------------------------------------------------------------------
def rep(old: str, new: str, label: str, count: int = 1):
    global html
    n = html.count(old)
    if n != count:
        raise SystemExit("%s matched %d times (expected %d)" % (label, n, count))
    html = html.replace(old, new, count)


def rx1(pattern: str, new: str, label: str):
    global html
    out, n = re.subn(pattern, lambda m: new, html, count=1, flags=re.S)
    if n != 1:
        raise SystemExit("regex %s matched %d times" % (label, n))
    html = out


ICON_SWAP = {
    "ic_badge_backend_professional": "ic_cap_filled",
    "ic_badge_backend": "ic_cap", "ic_badge_frontend": "ic_target",
    "ic_badge_fullstack": "ic_trophy", "ic_badge_python_dev": "ic_streak_active",
    "ic_badge_js": "ic_square_rounded", "ic_badge_ts": "ic_check_circle_alt_01",
    "ic_badge_react": "ic_sparks", "ic_badge_sql": "ic_task_completed",
    "ic_badge_html": "ic_file", "ic_badge_css": "ic_calendar",
    "ic_badge_python": "ic_help",
    "ic_code_lang_html": "insert_drive_file", "ic_code_lang_css": "bookmark",
    "ic_code_lang_python": "ic_coin", "ic_code_lang_sql": "ic_key",
    "ic_code_playground_template_python": "ic_file",
    "ic_code_playground_template_js_only": "ic_square_rounded",
    "ic_code_playground_template_website": "ic_task_completed",
    "ic_code_playground_template_react": "ic_sparks",
}

# ---------------------------------------------------------------------------
# 3. header / footer / aside -> round 11
# ---------------------------------------------------------------------------
rep("<h1>طرح رابط کاربری — دور دهم <span class=\"ver\">DESIGN v10 · REVIEW</span></h1>",
    "<h1>طرح رابط کاربری — دور یازدهم <span class=\"ver\">DESIGN v11 · REVIEW</span></h1>",
    "header title")
old_p = html[html.index("<p>بازآفرینی ۱۰۰٪"):html.index("</p>", html.index("<p>بازآفرینی ۱۰۰٪")) + 4]
new_p = ("<p>بازآفرینی ۱۰۰٪ بخشهای اصلی میمو <b>از روی کد/مهندسی معکوس</b> · "
         "<b>دور یازدهم:</b> لیدربورد رقابتی حذف و فقط «وضعیت من» ماند؛ سرتیترها به "
         "<b>«یادگیری برنامه محور»</b> و <b>«یادگیری مبحثی»</b> تبدیل شدند؛ چهار کارت درشت "
         "با آیکونهای واقعی میمو (بدون هیچ نشان برنامهنویسی)، ۱۲ کورس «درس × پایه»، "
         "<b>مدرک پایان دوره</b> با «۲۲ درصد کامل شده»، و زیرمباحث <b>دو هفتهای</b> "
         "از ۱ آبان تا ۱۵ اسفند (۵ ماه) با «دروس: زیست، شیمی، ریاضی، فیزیک». "
         "معماری اورجینال قوسدار دور دهم، پنج تب، ۷ بخش آزمون، تایمر و قفلها دستنخوردهاند. "
         "اسکرینشاتها فقط چک بصری.</p>")
rep(old_p, new_p, "header paragraph")
rep("⚠️ این <b>طرح دور دهم v10</b> است، نه محصول.",
    "⚠️ این <b>طرح دور یازدهم v11</b> است، نه محصول.", "footer lead")
rep("در دور دهم درخواست خط صاف پس گرفته شد و <b>معماری اورجینال قوسدار</b> با کاوش عمیقتر کد بازسازی شد.",
    "در دور دهم درخواست خط صاف پس گرفته شد و <b>معماری اورجینال قوسدار</b> با کاوش عمیقتر کد بازسازی شد. "
    "در دور یازدهم محتوای لیدربورد/مسیرها/کورسها کنکوری و بدون نشانهای برنامهنویسی شد.",
    "footer paragraph")

aside_anchor = "<aside class=\"spec\">\n    <h3>دور دهم"
rep(aside_anchor, """<aside class="spec">
    <h3>دور یازدهم · لیدربورد «وضعیت من»، مسیرهای برنامهمحور و کورسهای مبحثی</h3>
    <ul>
      <li>بلوک <code>Wooden League / 6d 22h 38m</code> و <b>همهٔ ۵ ردیف رقیب</b> بطور کامل حذف شد؛ فقط <b>My status / وضعیت من</b> و کارتهای آمار و «آزمونها و امتیازات من» ماند.</li>
      <li><code>Career Paths</code> → <b>«یادگیری برنامه محور»</b>؛ <code>Courses</code> → <b>«یادگیری مبحثی»</b>. چهار کارت درشت: سه برنامهٔ دوازدهم/یازدهم/دهم + کارت «یادگیری مبحثی». ۱۲ کورس = ۴ درس × ۳ پایه.</li>
      <li>نمای مسیر: <b>«یادگیری برنامه محور»</b> / نام برنامهٔ پایه / <b>«مدرک پایان دوره»</b> / <b>«۲۲ درصد کامل شده»</b> / <code>2/9</code>. زیرمباحث <b>۱۰ بازهٔ دو هفتهای</b> از ۱ آبان تا ۱۵ اسفند (آبان، آذر، دی، بهمن، اسفند)، هر کدام «دروس: زیست، شیمی، ریاضی، فیزیک».</li>
      <li>برای کورسهای مبحثی، همان نمای مسیر با <b>اسم فصل و اسم درس</b> از مدل محتوای کنکوری داخل ریپو پر میشود (<code>DESIGN/KONKUR_CURRICULUM.json</code>، <code>CATALOGS/KONKUR_CURRICULUM.csv</code>)؛ سلسلهمراتب «کتاب ← فصل ← مبحث» از <code>SOURCE_APPS/hamdars/HELP_CENTER_UX.md §learn-books</code>.</li>
      <li><b>هیچ آرم/نشان برنامهنویسی</b>ای نمایش داده نمیشود: تمام <code>ic_badge_*</code> / <code>ic_code_lang_*</code> / <code>ic_code_playground_template_*</code> با وکتورهای بومی میمو جایگزین شدند؛ بقیهٔ المانها سر جای خود ماندند.</li>
      <li>بیهیچ تغییری: معماری قوسدار ۸۰/۱۹۶/۳۱۲، ۵ تب، ۷ بخش لیبلدار، تایمر فقط داخل آزمون، ۲۷۰ دقیقه، «پاسخبرگ»≠«پاسخنامه»، تکدکمهٔ AI، صفر قفل یادگیری و تنها قفل «آزمون نهایی / دو هفتگی».</li>
    </ul>
    <h3>دور دهم""", "aside v11")

# ---------------------------------------------------------------------------
# 4. Learn screen chrome
# ---------------------------------------------------------------------------
rep('<b data-fa="کنکور تجربی">Back-End Developer</b>',
    '<b id="learnPathTitle" data-fa="یادگیری همگام با برنامه آزمون دوازدهم" '
    'data-code="track_switcher_selected_path">یادگیری همگام با برنامه آزمون دوازدهم</b>',
    "learn coursebar")
rep('<span class="oc-kicker" data-fa="مسیر شغلی">Career path</span>',
    '<span class="oc-kicker" data-fa="یادگیری برنامه محور" '
    'data-code="ViewsKt$OverviewEntryPointHeader / path_see_course_overview">یادگیری برنامه محور</span>',
    "overview kicker")
rep('<span class="oc-title" data-fa="۳. سلول و بافت">3. Arrays &amp; Functions</span>',
    '<span class="oc-title" data-fa="۳. سلول و بافت" data-code="path_overview_section_ordinal">۳. سلول و بافت</span>',
    "overview title")

# ---------------------------------------------------------------------------
# 5. Select Path headings + invisible code evidence
# ---------------------------------------------------------------------------
rep('<h3 id="careerHeading" data-fa="مسیرهای شغلی">Career Paths</h3>',
    '<h3 id="careerHeading" data-fa="یادگیری برنامه محور" '
    'data-code="track_switcher_career_paths = Career Paths (relabelled)">یادگیری برنامه محور</h3>',
    "career heading")
rep('<h3 class="sub" id="courseHeading" data-fa="درسها">Courses</h3>',
    '<h3 class="sub" id="courseHeading" data-fa="یادگیری مبحثی" '
    'data-code="track_switcher_courses = Courses (relabelled)">یادگیری مبحثی</h3>',
    "course heading")
rep('<div id="careerCards"></div>',
    '<div id="careerCards" data-code="Full-Stack Developer / Python Developer / Back-End Developer / Front-End Developer"></div>',
    "careerCards evidence")
rep('<div id="courseRows"></div>',
    '<div id="courseRows" data-code="TypeScript / JS required / 6/14 / tutorialIds from test-tracks.json"></div>',
    "courseRows evidence")

# ---------------------------------------------------------------------------
# 6. Path Overview + Section detail static chrome
# ---------------------------------------------------------------------------
rep('<span class="kick" data-fa="مسیر شغلی">Career path</span>',
    '<span class="kick" id="poKicker" data-fa="یادگیری برنامه محور" '
    'data-code="onboarding_path_type_career_path">یادگیری برنامه محور</span>',
    "po kicker")
rep('<h1 data-fa="کنکور تجربی">Back-End Developer</h1>',
    '<h1 id="poTitle" data-fa="یادگیری همگام با برنامه آزمون دوازدهم">یادگیری همگام با برنامه آزمون دوازدهم</h1>',
    "po title")
rep('<div class="cert-card" id="certCard" data-modal="unfinishedModal" data-code="certificates_unfinished_track_dialog_*">',
    '<div class="cert-card" id="certCard" data-modal="unfinishedModal" '
    'data-code="certificates_unfinished_track_dialog_* · Professional Certificate / 22% Complete / path_overview_certificate_percent_complete">',
    "cert card")
rep('<b data-fa="گواهی حرفهای">Professional Certificate</b>',
    '<b data-fa="مدرک پایان دوره">مدرک پایان دوره</b>', "cert label")
rep('<span data-fa="۲۲٪ تکمیل">22% Complete</span>',
    '<span data-fa="۲۲ درصد کامل شده">۲۲ درصد کامل شده</span>', "cert progress")
rep('<div class="po-secs" id="sectionRows"></div>',
    '<div class="po-secs" id="sectionRows" data-code="path_overview_section_ordinal · tutorialIds · Section Project · Coming soon"></div>',
    "sectionRows evidence")
rep('<b data-fa="مبحث">Section</b>', '<b data-fa="فصل">فصل</b>', "sd top label")
rep('<span class="kick" data-fa="فصل سوم">Section 3</span>',
    '<span class="kick" id="sdKicker" data-fa="فصل ۱" data-code="section_details">فصل ۱</span>',
    "sd kicker")
rep('<h2 id="sdTitle" data-fa="سلول و بافت">Arrays &amp; Functions</h2>',
    '<h2 id="sdTitle" data-fa="سلول و بافت">سلول و بافت</h2>', "sd title")
rep('<p id="sdDesc">Use arrays &amp; functions to build sophisticated programs</p>',
    '<p id="sdDesc">دروس: زیست، شیمی، ریاضی، فیزیک</p>', "sd desc")
rep('<div class="sd-list" id="lessonRows"></div>',
    '<div class="sd-list" id="lessonRows" data-code="tutorialIds from test-tracks.json · lesson_continue"></div>',
    "lessonRows evidence")

# ---------------------------------------------------------------------------
# 7. Leaderboard: remove the whole competition block, keep My status only
# ---------------------------------------------------------------------------
m = re.search(r'(<section class="screen mimo" data-screen="leaderboard">)(.*?)(</section>)', html, re.S)
if not m:
    raise SystemExit("leaderboard section not found")
body = m.group(2)
start = body.index('<div class="lb-title"')
end = body.index('<div class="sec-h"')
body = body[:start] + body[end:]
body = body.replace(
    '<div class="sec-h" data-fa="اطلاعات من">My stats</div>',
    '<div class="sec-h" data-fa="وضعیت من" data-code="profile_info_card_view.xml">My status</div>', 1)
body = body.replace(
    '<div class="statcard"><span class="ic" data-icon="img_brain" data-size="32"></span>'
    '<b data-fa="چوبی">Wooden</b><small data-fa="لیگ">League</small></div>',
    '<div class="statcard"><span class="ic" data-icon="ic_trophy" data-size="32"></span>'
    '<b>۷</b><small data-fa="آزمونهای من">آزمونهای من</small></div>', 1)
if 'Wooden' in body or 'League' in body or 'lb-row' in body or 'league-row' in body:
    raise SystemExit("leaderboard competition block did not fully go away")
html = html[:m.start(2)] + body + html[m.end(2):]

# ---------------------------------------------------------------------------
# 8. Replace the v6 career/course/section/lesson rendering with v11 data-driven JS
# ---------------------------------------------------------------------------
JS11 = r'''  /* ============ v11 · program-based / topic-based Konkur tracks ============ */
  var V11_PROGRAMS=KONKUR.programs, V11_COURSES=KONKUR.courses, V11_DATES=KONKUR.dates;
  var V11_SUBJECT_LINE=KONKUR.lessons_line, V11_SUBJECTS=KONKUR.subjects;
  var V11_SEL={kind:"program",key:"grade12"}, V11_ROWS=[];
  function v11Course(k){for(var i=0;i<V11_COURSES.length;i++)if(V11_COURSES[i].key===k)return V11_COURSES[i];return null}
  function v11Program(k){for(var i=0;i<V11_PROGRAMS.length;i++)if(V11_PROGRAMS[i].key===k)return V11_PROGRAMS[i];return null}
  function v11Lab(s){return ' data-fa="'+esc(s)+'"'}
  /* 4 BIG cards — icons are decoded Mimo vectors, never programming emblems */
  var V11_CARDS=V11_PROGRAMS.map(function(p){return {key:p.key,kind:"program",label:p.label,icon:p.icon,sec:"۲/۱۰",pct:22}});
  V11_CARDS.push({key:"courses",kind:"courses",label:KONKUR.topic_label,icon:"ic_square_rounded",sec:"۱۲ درس",pct:22});
  var CC=q("#careerCards");CC.innerHTML="";
  V11_CARDS.forEach(function(c,i){
    var b=document.createElement("button");b.className="career-card"+(i===0?" sel":"");
    b.dataset.v11=c.kind+":"+c.key;
    b.setAttribute("data-code","track_switcher career card · Mimo vector "+c.icon);
    b.innerHTML='<span class="badges"><span data-icon="'+c.icon+'" data-size="48"></span></span>'
      +'<h4'+v11Lab(c.label)+'>'+esc(c.label)+'</h4>'
      +'<span class="cr"><span data-fa="فصل">فصل</span><span>'+esc(c.sec)+'</span></span>'
      +'<span class="cbar"><i style="width:'+c.pct+'%"></i></span>';
    CC.appendChild(b);
  });
  /* 12 Courses = 4 subjects x 3 grades */
  var CR=q("#courseRows");CR.innerHTML="";
  V11_COURSES.forEach(function(c){
    var b=document.createElement("button");b.className="course-row";b.dataset.v11="course:"+c.key;
    b.setAttribute("data-code","section_details · "+c.chapters.length+" chapters");
    b.innerHTML='<span class="cbadge" data-icon="'+c.icon+'" data-size="38"></span>'
      +'<span class="ctxt"><b'+v11Lab(c.name)+'>'+esc(c.name)+'</b>'
      +'<small'+v11Lab(fa(c.chapters.length)+" فصل")+'>'+fa(c.chapters.length)+' فصل</small></span>'
      +'<span class="cring"><b>0/'+c.chapters.length+'</b></span>';
    CR.appendChild(b);
  });
  /* Path Overview: 10 fortnightly slots, or chapters + lessons for a course */
  function v11RenderOverview(){
    var course=V11_SEL.kind==="course"?v11Course(V11_SEL.key):null;
    var kick=course?KONKUR.topic_label:KONKUR.program_label;
    var title=course?course.name:(v11Program(V11_SEL.key)||V11_PROGRAMS[0]).label;
    q("#poKicker").textContent=kick;q("#poKicker").dataset.fa=kick;
    q("#poTitle").textContent=title;q("#poTitle").dataset.fa=title;
    var rows=[];
    if(course){
      course.chapters.forEach(function(ch,i){
        rows.push({ord:i+1,title:"فصل "+fa(i+1)+" · "+ch.name,
                   desc:KONKUR.lessons_label+": "+ch.lessons.join("، "),lessons:ch.lessons});
      });
    } else {
      V11_DATES.forEach(function(d,i){
        rows.push({ord:i+1,title:d,desc:V11_SUBJECT_LINE,lessons:V11_SUBJECTS});
      });
    }
    V11_ROWS=rows;
    var SR=q("#sectionRows");SR.innerHTML="";
    rows.forEach(function(r,i){
      var pct=i===0?43:0;
      var b=document.createElement("button");b.className="po-sec"+(i===0?" active":"");
      b.dataset.v11section=String(i);
      b.setAttribute("data-code","path_overview_section_ordinal · "+r.title);
      b.innerHTML='<span class="ring'+(pct?" part":"")+'"><b>'+pct+'%</b></span>'
        +'<span class="st"><b'+v11Lab(fa(r.ord)+". "+r.title)+'>'+esc(fa(r.ord)+". "+r.title)+'</b>'
        +'<p'+v11Lab(r.desc)+'>'+esc(r.desc)+'</p>'
        +(i===1?'<span class="proj" data-fa="پروژهٔ مبحث">پروژهٔ مبحث</span>':'')
        +(i===4?'<span class="soon" data-fa="بهزودی">بهزودی</span>':'')+'</span>';
      SR.appendChild(b);
    });
    paintIcons(SR);
    v11RenderSection(0);
    var lp=q("#learnPathTitle");if(lp){lp.textContent=title;lp.dataset.fa=title}
  }
  /* Section detail: «دروس» — subjects for programs, real lesson names for courses */
  function v11RenderSection(i){
    var r=V11_ROWS[i];if(!r)return;
    var kick=V11_SEL.kind==="course"?("فصل "+fa(i+1)):(fa(i+1)+" · "+V11_DATES[i]);
    q("#sdKicker").textContent=kick;q("#sdKicker").dataset.fa=kick;
    q("#sdTitle").textContent=r.title;q("#sdTitle").dataset.fa=r.title;
    q("#sdDesc").textContent=r.desc;q("#sdDesc").dataset.fa=r.desc;
    var LR=q("#lessonRows");LR.innerHTML="";
    r.lessons.forEach(function(name,j){
      var b=document.createElement("button");
      b.className="sd-row "+(j<2?"done":j===2?"cur":"");b.dataset.nav="chapter";
      var lab="درس "+fa(j+1)+" · "+name;
      b.innerHTML='<span class="sr" data-icon="'+(j<2?"ic_check_white":j===2?"ic_play":"ic_arrow_right")+'" data-size="18" data-mono="1"></span>'
        +'<span class="stx"><b'+v11Lab(lab)+'>'+esc(lab)+'</b>'
        +'<small'+v11Lab(r.title)+'>'+esc(r.title)+'</small></span>'
        +'<span class="si" data-icon="ic_arrow_right" data-size="18" data-mono="1"></span>';
      LR.appendChild(b);
    });
    var proj=document.createElement("button");proj.className="sd-row";proj.dataset.nav="chapter";
    proj.innerHTML='<span class="sr" data-icon="ic_cap" data-size="20"></span>'
      +'<span class="stx"><b data-fa="پروژهٔ مبحث">پروژهٔ مبحث</b>'
      +'<small data-fa="پروژهٔ پایانی مبحث">پروژهٔ پایانی مبحث</small></span>'
      +'<span class="si" data-icon="ic_arrow_right" data-size="18" data-mono="1"></span>';
    LR.appendChild(proj);
    paintIcons(LR);
  }
  v11RenderOverview();
  /* One delegated handler: cards switch the track, section rows open their own data */
  document.addEventListener("click",function(e){
    var c=e.target.closest("[data-v11]");
    if(c){
      var parts=c.dataset.v11.split(":");
      if(parts[0]==="courses"){
        var cr=q("#courseRows");if(cr&&cr.scrollIntoView)cr.scrollIntoView({block:"start"});
        qa("#careerCards .career-card").forEach(function(x){x.classList.remove("sel")});
        c.classList.add("sel");return;
      }
      V11_SEL={kind:parts[0],key:parts[1]};
      qa("#careerCards .career-card").forEach(function(x){x.classList.remove("sel")});
      if(parts[0]==="program")c.classList.add("sel");
      v11RenderOverview();
      if(parts[0]==="program"||parts[0]==="course")go("path-overview");
      return;
    }
    var s=e.target.closest("[data-v11section]");
    if(s){v11RenderSection(+s.dataset.v11section);go("section-detail");return}
  });
  /* generic modal open/close (Unfinished track) */
'''
rx1(r'  var FA=\{.*?  /\* generic modal open/close \(Unfinished track\) \*/', JS11, "v11 JS chunk")

# ---------------------------------------------------------------------------
# 9. Swap every programming emblem/logo for a decoded Mimo vector
# ---------------------------------------------------------------------------
def swap_icon(m):
    name = m.group(1)
    return 'data-icon="' + ICON_SWAP.get(name, name) + '"'
html, nswap = re.subn(r'data-icon="(ic_badge_[a-z0-9_]+|ic_code_lang_[a-z0-9_]+|ic_code_playground_template_[a-z0-9_]+)"',
                      swap_icon, html)
left = re.findall(r'data-icon="(ic_badge_[a-z0-9_]+|ic_code_lang_[a-z0-9_]+|ic_code_playground_template_[a-z0-9_]+)"', html)
if left:
    raise SystemExit("programming icons still present: %s" % left)

# ---------------------------------------------------------------------------
# 10. inject the machine-readable curriculum payload before the main script
# ---------------------------------------------------------------------------
payload = "<script>var KONKUR=" + json.dumps(KONKUR, ensure_ascii=False, separators=(",", ":")) + ";</script>\n"
rep("<script>\n(function(){\n  \"use strict\";", payload + "<script>\n(function(){\n  \"use strict\";",
    "KONKUR payload")

# ---------------------------------------------------------------------------
# 11. write outputs
# ---------------------------------------------------------------------------
(TOOLS / "design_v11_template.html").write_text(html, encoding="utf-8")
(DESIGN / "index.html").write_text(html, encoding="utf-8")
print(json.dumps({
    "output": str(DESIGN / "index.html"),
    "bytes": len(html.encode("utf-8")),
    "template_bytes": len(html.encode("utf-8")),
    "courses": len(courses),
    "chapters": KONKUR["chapter_count"],
    "lessons": KONKUR["lesson_count"],
    "fortnight_dates": len(DATES),
    "months": KONKUR["months"],
    "program_cards": len(V11_CARDS) if False else 4,
    "programming_icons_swapped": nswap,
    "leaderboard_block_removed": "Wooden" not in body and "MIGUELBAOBAB" not in body
                                  and 'class="lb-row' not in body,
    "my_status_only": "My status" in html and 'class="lb-row' not in html,
    "curved_zigzag_kept": "M242 70 H280 Q312 70 312 102 V140" in html,
    "method": "REPO_CONTENT_MODEL + MIMO_DECODED_VECTORS / screenshots VISUAL_CROSSCHECK_ONLY",
}, ensure_ascii=False, indent=2))
