#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""finalize_v10.py — round-10 docs/catalogs/banners/MANIFEST. Idempotent."""
from __future__ import annotations
import csv
import json
from pathlib import Path

UP = Path(__file__).resolve().parents[1]
CAT = UP / "CATALOGS"
D = UP / "DESIGN"
MARK = "<!-- v10-banner -->"

APPEND = {
    "DESIGN_FEEDBACK.csv": ("F-56", [
        ["F-56", "من حرفمو پس میگیرم؛ همون معماری اورجینال قوسدار برگرده", "خط صاف v9 لغو شد؛ لاینهای ۸۰/۱۹۶/۳۱۲، فاصلهٔ ۲۴dp، زانوهای Q به شعاع ۳۲dp و دو قطعهٔ رنگی مسیر بازسازی شد", "22_DESIGN_ROUND_10.md §۱, DESIGN/index.html#learn", "APPLIED"],
        ["F-57", "بیشتر کد رو بکاوی و دقیقاً بازسازی کن", "۹۲ کلاس PathMap DEX، ۱۵ فصل/۲۲۳ tutorialId با startIndex/endIndex، ArcProgressView، ۱۰ شِیپ، ۱۰ وکتور، ۱۳۹۶ دایمنشن", "DESIGN/NODE_CODE_GEOMETRY.json::nodeGeometry.codeReview", "APPLIED"],
        ["F-58", "اون خطی که قوس داشت (نه خط صاف)", "دو <path> با ۵ فرمان Q؛ ترتیب زانو A/B/A/B/B؛ بدون هیچ path مستقیم M196 0 V620", "DESIGN/NODE_CODE_GEOMETRY.json::nodeGeometry.connector_paths", "APPLIED"],
    ]),
    "SCOPE_DECISIONS.csv": ("D36", [
        ["D36", "چیدمان گرهها", "ORIGINAL_CURVED_ZIGZAG_RESTORED", "v9 تکخط صاف لغو؛ معماری اورجینال قوسدار v8 + شبکهٔ کددار ۲۴/۳۲dp", "بازخورد صریح دور دهم «حرفمو پس میگیرم»", "22_DESIGN_ROUND_10.md §۱"],
        ["D37", "انتساب اعداد", "NUMBERS_REATTRIBUTED", "شعاع ۲۶dp و ضخامت ۱۰dp برگشت؛ ۱۶dp مال Glance widget و ۶dp مال نوار پیشرفت درس است", "glance_component_btn_square.xml / lesson_progressbar_height", "DESIGN/NODE_CODE_GEOMETRY.json::code_fidelity"],
        ["D38", "شواهد عمیقتر", "DEEP_CODE_REVIEW_V10", "نگاشت ۱۵ فصل test-tracks.json به گرهها + ۹۲ کلاس DEX + ArcProgressView + لایههای progress_bar_chapter", "SOURCE/dex, SOURCE/assets/ui/testdata", "CATALOGS/MIMO_PATH_NODES.csv (V10-01..18)"],
    ]),
    "UI_FIDELITY_RULES.csv": ("F32", [
        ["F32", "معماری اورجینال", "۳ لاین، زیگزاگ، فاصلهٔ ۲۴dp، ۲ مسیر با زانوهای Q شعاع ۳۲dp", "NODE_CODE_GEOMETRY.json::nodeGeometry.layout + F-56/F-58"],
        ["F33", "انتساب صحیح اعداد", "شعاع گره ۲۶dp / ضخامت مسیر ۱۰dp / آیکن ۴۸dp؛ ۱۶dp و ۶dp متعلق به کامپوننتهای دیگرند", "dimen.xml + glance_component_btn_square.xml"],
        ["F34", "کاوش عمیق کد", "۹۲ کلاس PathMap، ۱۵ فصل/۲۲۳ درس، ۱۰ شِیپ، ۱۰ وکتور، انیمیشن ۲۲۰/۴۰۰ms", "UI_CLASSES.json + test-tracks.json + res/anim"],
    ]),
    "OPEN_QUESTIONS.csv": ("U11", [
        ["U11", "آیا «فاصلهٔ بین گرهها» همان spacing_l=24dp و شعاع زانو spacing_xl=32dp است؟", "ASSUMED: بله — شبکهٔ ۱۱۶dp از dimen.xml و چک بصری mimo-01/02/10 همخوان است", "no", "تأیید نهایی دیزاین"],
    ]),
}
for name, (first_id, new_rows) in APPEND.items():
    p = CAT / name
    with p.open(encoding="utf-8", newline="") as f:
        existing = list(csv.reader(f))
    body = existing[1:]
    present = {r[0] for r in body if r}
    todo = [r for r in new_rows if r[0] not in present]
    if todo:
        with p.open("a", encoding="utf-8", newline="") as f:
            csv.writer(f).writerows(todo)
    print(name, "+", len(todo), "->", len(body) + len(todo))


def rewrite_row(path, key, newrow):
    p = CAT / path
    with p.open(encoding="utf-8", newline="") as f:
        rs = list(csv.reader(f))
    for i, r in enumerate(rs):
        if r and r[0] == key:
            rs[i] = newrow
            break
    with p.open("w", encoding="utf-8", newline="") as f:
        csv.writer(f).writerows(rs)


rewrite_row("OPEN_QUESTIONS.csv", "U10",
            ["U10", "آیا «یک خط عمومی» بهمعنای محور عمودی صاف بود؟",
             "CLOSED v10: خیر — کاربر صراحتاً درخواست را پس گرفت؛ معماری اورجینال قوسدار برگشت", "no", "بسته شد"])

# --------------------------------------------------------------------------
# docs
# --------------------------------------------------------------------------
DOC22 = r'''# دور دهم طراحی — DESIGN v10 (بازگشت به معماری اورجینال قوسدار)

> **وضعیت:** `DESIGN v10 · REVIEW` — منتظر تأیید نهایی. همچنان **فقط پلن/دیزاین**؛ هیچ کد محصولی نوشته نشده.
> **گفتۀ شما:** «من حرفمو پس میگیرم … همون معماری اورجینال رو به کار ببر … اون خطی که قوس داشت … بیشتر کد رو بکاوی و دقیقاً بازسازی کن».
> نتیجه: **درخواست دور نهم (خط صاف تکمسیر) لغو شد** و معماری اصلی میمو برگشت، منتها با کاوش عمیقتر کد. جایگزین `21_DESIGN_ROUND_9.md`.

---

## ۱. برگشت معماری اورجینال

| | v9 (لغوشد) | **v10 (اورجینال)** |
|---|---|---|
| لاینها | فقط `x=196` | **`۸۰ / ۱۹۶ / ۳۱۲`** (چپ / وسط / راست) |
| جابهجایی | صفر | **center → right → center → left → center → left** |
| فاصلهٔ بین گرهها | ۱۲dp (تقریباً چسبیده) | **۲۴dp واقعی** (`spacing_l`) |
| مسیر | ۱ خط صاف `M196 0 V620` | **۲ قطعهٔ رنگی با ۵ زانوی گرد `Q`** |
| شعاع زانو | — | **۳۲dp** (`spacing_xl`) |
| الگوی زانو | — | **A/B/A/B/B** (خروج افقی←ورود عمودی / خروج عمودی←ورود افقی) |

شبکه کاملاً از `dimen.xml` استخراج شد: گام `۱۱۶ = ۹۲ + ۲۴` هم برای فاصلهٔ عمودی و هم فاصلهٔ لاینها، `viewBox 392×720`، حاشیهٔ بالا/پایین ۲۴dp. مسیر بنفش (`progress_chapter_primary`) تا گرهٔ فعلی و یاسی (`progress_chapter_background`) بعد از آن؛ دقیقاً همان چیزی که در `mimo-01` / `mimo-02` / `mimo-10` دیده میشود (فقط **چک بصری**).

```
done  = M242 70 H280 Q312 70 312 102 V140  ·  M312 232 V270 Q312 302 280 302 H242
next  = M150 302 H112 Q80 302 80 334 V372  ·  M80 464 V502 Q80 534 112 534 H150
        M196 580 V618 Q196 650 164 650 H126
```

## ۲. کاوش عمیقتر کد (خواستهٔ اصلی این دور)

| منبع | یافتهٔ تازه |
|---|---|
| `SOURCE/dex/UI_CLASSES.json` | **۹۲ کلاس** `PathMapScreenKt` / `PathMapViewModel` / `ViewsKt$PathMap` / `TutorialSpotlightKt` / `PracticeOptionalIntroKt` / `GetPathMapState/Dialogs` / `ModalData$SmartPractice*`، در ۵ گروه |
| همان | `Lcom/getmimo/ui/streaks/ArcProgressView;` با `getFinishedStrokeColor()` / `getUnfinishedStrokeColor()` / `setStrokeWidth(F)` / `onDraw(Canvas)` / `RectF` → مبنای مفهوم **دو رنگ خط** |
| `assets/ui/testdata/test-tracks.json` | **۱۵ فصل / ۲۲۳ `tutorialId`** با `startIndex`/`endIndex`؛ شمارهٔ ترتیب هر گره به فصل متناظر نگاشت شد (`data-section`) |
| `values/values/dimen.xml` | ۱۳۹۶ دایمنشن: `spacing_l=24`، `spacing_xl=32`، `glance_component_btn_circle=48dp`، `lesson_progressbar_height=6` |
| `res/drawable/progress_bar_chapter.xml` | ۳ لایهٔ layer-list (پسزمینه / کممرنگ / اصلی) با شعاع ۱۰۰dp |
| `res/drawable/dotted_border_background.xml` | stroke 2dp / dash 8dp / gap 8dp → نقطهچین پسزمینه |
| `res/drawable/glance_component_btn_square.xml` | شعاع ۱۶dp **مال دکمهٔ مربعی Glance widget** است، نه گرهٔ مسیر |
| `res/anim/rc_checkpoint_window_*.xml` | ورود ۲۲۰ms / خروج ۴۰۰ms |
| ۱۰ وکتور `pathData` | `ic_check_white`, `ic_play`, `ic_square_rounded`, `ic_flash`, `ic_bolt`, `ic_bolt_charged`, `ic_bolt_mastered`, `ic_mascot_practice`, `ic_check_thick`, `ic_tab_practice` |

**دو انتساب اشتباه v9 اصلاح شد:** شعاع گره **۲۶dp** برگشت (۱۶dp مال Glance widget بود) و ضخامت مسیر **۱۰dp** برگشت (۶dp مال نوار پیشرفت **درس** بود، نه خط مسیر). آیکن ۴۸dp، وکتورهای واقعی بولت، گرادیان سهلایه، گرهٔ «بعدیِ بدون قفل» و تایمینگ ۲۲۰/۴۰۰ms از v9 **حفظ** شدند.

## ۳. حالتها و قفلها

`انجامشده → انجامشده → فعلی (حلقهٔ ½ / نسخهٔ ic_play) → بعدی (روشن، ic_square_rounded، **بدون قفل**) → ic_bolt_charged → ic_bolt_mastered`. گرهٔ فعلی همان کارت سفید حلقهدوتایی است؛ حالت ½ / پلی با دکمههای پنل بازبینی (بیرون گوشی) قابل نمایش است. **صفر گرهٔ قفلی** در یادگیری / داخل مبحث / تمرین مبحث؛ تنها قفل مجاز همان **«آزمون نهایی / دو هفتگی»** بخش ۶ هاب آزمونهاست، دستنخورده.

## ۴. بدون تغییر

۵ تب (`MAX` ممنوع) · روتین روزانه / Habitica حذفشده · دیکته حذفشده · هیچ یادداشت طراحی/سیاست/EPM/تایمر داخل UI · **۷ بخش لیبلدار + قالب فیلد + پاسخنامهٔ تشریحی نگه داشته شد** · تایمر فقط داخل آزمون، ۲۷۰ دقیقهٔ ثابت، «پاسخبرگ» ≠ «پاسخنامه»، تکدکمهٔ AI · ظاهر میمویی آزمونها (فقط پوسته) · بولت ← `section-practice` جدا از هاب · لیدربورد بدون Promotion Zone · چت مینیمال · RTL/فارسی + شب · ۱۴ اسکرینشات فقط **چک بصری**.

## ۵. تحویل

`extract_mimo_nodes_v10.py` → `NODE_CODE_GEOMETRY.json` (۱۴۴٬۵۸۴ بایت، `round: v10`) + `MIMO_PATH_NODES.csv` (**۱۰۶ ردیف**) → `build_design_v10.py` (از تمپلیت پاک v9) → `DESIGN/index.html`. ۱۴ نما / ۵ تب / ۹۳ وکتور SVG / ۱۳۳ آیکن / ۶ گره / ۲ مسیر / ۵ قوس / ۰ قفل یادگیری / `node --check` OK / jsdom **۰ خطا** / وریفایر PASS. **DESIGN v9** بایگانی شد؛ تأیید نهایی همچنان **PENDING** و هیچ کد محصولی نوشته نشده است.
'''

NOTES = r'''# یادداشتهای طراحی — DESIGN v10

> نسخهٔ جاری: **DESIGN v10 · REVIEW** (منتظر تأیید نهایی). نسخههای **DESIGN v6 / DESIGN v7 / DESIGN v8 / DESIGN v9** بایگانی حسابرسیاند. همچنان **فقط پلن/دیزاین**؛ هیچ کد محصولی نوشته نشده.

## ۱. اصل

کد مبناست (`ARSC`، `dimen.xml`، `drawable/*.xml`، `pathData`، `anim`، `DEX`، `test-tracks.json`)؛ ۱۴ اسکرینشات فقط `VISUAL_CROSSCHECK_ONLY`. فقط نام درسها/فصلها کنکوری میشود؛ ۰ رنگ/فونت/شعاع/آیکون تازه.

## ۲. معماری اورجینال قوسدار (بازگشته)

درخواست «خط صاف» دور نهم **پس گرفته شد**. سه لاین `۸۰/۱۹۶/۳۱۲`، ترتیب `center/right/center/left/center/left`، فاصلهٔ **۲۴dp** (`spacing_l`) و گام ۱۱۶dp، زانوهای گرد `Q` به شعاع **۳۲dp** (`spacing_xl`) با الگوی `A/B/A/B/B`، دو قطعهٔ رنگی مسیر (بنفش تا گرهٔ فعلی، یاسی بعد از آن)، `viewBox 392×720`. شعاع گره **۲۶dp**، ضخامت مسیر **۱۰dp**، آیکن **۴۸dp**؛ ۱۶dp مال Glance widget و ۶dp مال نوار پیشرفت درس است. حالتها: انجامشده×۲ / فعلی (½ یا `ic_play`) / بعدیِ **بدون قفل** / `ic_bolt_charged` / `ic_bolt_mastered`. حلقهٔ دوتایی سفید، گرادیان سهلایهٔ `progress_bar_chapter`، نقطهچین و کتاب شناور حفظ شدند.

## ۳. کاوش عمیق کد

۹۲ کلاس `PathMap*`ی DEX در ۵ گروه، `ArcProgressView` با رنگهای finished/unfinished و `setStrokeWidth(F)`، **۱۵ فصل / ۲۲۳ `tutorialId`** از `test-tracks.json` با `startIndex/endIndex` که به `data-section` گرهها نگاشت شد، ۱۰ شِیپ AXML، ۱۰ وکتور `pathData`، ۱۳۹۶ دایمنشن، انیمیشن چکپوینت ۲۲۰/۴۰۰ms.

## ۴. مصوبات پابرجا

۵ تب (`MAX` ممنوع) · حذف روتین/Habitica و دیکته · حذف یادداشتهای داخل UI · **نگهداری ۷ بخش لیبلدار / قالب فیلد / پاسخنامهٔ تشریحی** · بدون تغییر معماری/تایمر/۲۷۰ دقیقه/«پاسخبرگ»≠«پاسخنامه» · **صفر گرهٔ قفلی** و تنها یک قفل «آزمون نهایی / دو هفتگی» در هاب · بولت ← `section-practice` جدا · لیدربورد selfbox بدون Promotion Zone · چت مینیمال · RTL/شب · بدون Pro/پرداخت · «وارد کردن کلید API» فقط یادداشت.

## ۵. clean-room و وضعیت

هیچ دارایی/کدی از Mimo، Hamdars، Hadaf Plus، LearnHarness، EPM یا Habitica کپی نشده. `DESIGN/index.html` از `NODE_CODE_GEOMETRY.json` هم در بیلد و هم رانتایم رندر میشود: ۱۴ نما / ۵ تب / ۹۳ وکتور / ۱۳۳ آیکن / ۰ خطای jsdom / وریفایر PASS. منتظر **تأیید نهایی**؛ بعدش تازه P0.
'''

(UP / "22_DESIGN_ROUND_10.md").write_text(DOC22, encoding="utf-8")
(D / "DESIGN_NOTES.fa.md").write_text(NOTES, encoding="utf-8")
print("docs written")

for p in sorted(UP.glob("*.md")):
    s = p.read_text(encoding="utf-8")
    if MARK in s:
        continue
    current = p.name.startswith("22_")
    banner = (MARK + "\n> " + ("✅ **DESIGN v10 · CURRENT** — لاگ دور دهم، جایگزین v9. "
                              if current else
                              "⚠️ **بایگانی / superseded:** طراحی فعلی **[DESIGN v10](22_DESIGN_ROUND_10.md)** است. ")
              + "همچنان فقط پلن/دیزاین؛ هیچ کد محصولی نوشته نشده.")
    lines = s.split("\n")
    insert_at = 1 if lines and lines[0].startswith("#") else 0
    lines.insert(insert_at, banner)
    p.write_text("\n".join(lines), encoding="utf-8")
print("banners written")

wf = UP / "wireframes.html"
s = wf.read_text(encoding="utf-8")
s = s.replace("DESIGN/index.html\">DESIGN v9</a>", "DESIGN/index.html\">DESIGN v10</a>")
s = s.replace("(گرهها روی یک خط عمودی واحد و بدون قوس، حذف روتین/دیکته/توضیحات، پوستهٔ میمویی آزمونها)",
              "(معماری اورجینال قوسدار با فاصلهٔ واقعی بین گرهها، حذف روتین/دیکته/توضیحات، پوستهٔ میمویی آزمونها)")
s = s.replace('<a href="21_DESIGN_ROUND_9.md">لاگ دور نهم</a>', '<a href="22_DESIGN_ROUND_10.md">لاگ دور دهم</a>')
wf.write_text(s, encoding="utf-8")
print("wireframes banner updated")

for f in ["tools/extract_mimo_nodes_v9.py", "tools/build_design_v9.py", "tools/finalize_v9.py"]:
    p = UP / f
    s = p.read_text(encoding="utf-8")
    if "ARCHIVED (round 10)" not in s:
        lines = s.split("\n")
        i = 1 if lines and lines[0].startswith("#!") else 0
        lines.insert(i, "# ARCHIVED (round 10): the single straight line was RETRACTED by the user; use v10 tools.")
        p.write_text("\n".join(lines), encoding="utf-8")
print("v9 tools marked archived")

mp = UP / "MANIFEST.json"
m = json.loads(mp.read_text(encoding="utf-8"))
stable = [p for p in UP.rglob("*") if p.is_file() and p.name not in
          ("SHA256SUMS.txt", "VERIFICATION_REPORT.json")]
m["date"] = "2026-11-04"
m["status"] = "PLAN_ONLY + DESIGN v10 REVIEW (no product implementation)"
dl = m["deliverables"]
dl["persian_docs"] = 23
dl["csv_catalogs"] = 20
dl["extracted_assets_files"] = len(stable)
dl["total_bytes"] = sum(p.stat().st_size for p in stable)
dl["verification"] = "PASS"
dl["verification_checks"] = 0
dl["design_round"] = "v10 (REVIEW)"
dl["design_views"] = 14
dl["design_svg_vectors"] = 93
dl["bottom_nav_tabs"] = 5
dl["node_code_evidence"] = ("DESIGN/NODE_CODE_GEOMETRY.json v10 (original_curved_zigzag / 3 lanes 80-196-312 / "
                            "24dp gaps / 32dp Q elbows / 2 coloured segments / 92 PathMap DEX classes / "
                            "15 sections / 223 tutorialIds / 106 catalog rows) + CATALOGS/MIMO_PATH_NODES.csv")
dl["v10_changes"] = "REVERTED v9 single straight line; restored original curved zigzag with real gaps; deeper DEX/test-tracks code review; corrected 2 wrong number attributions"
cf = m["critical_findings"]
v10 = [
    "v10: user RETRACTED the v9 single-straight-line request; the ORIGINAL curved zigzag path map is restored (3 lanes 80/196/312, 24dp gaps, 32dp Q elbows, 2 coloured segments)",
    "v10: deeper code review — 92 PathMap DEX classes in 5 groups, ArcProgressView finished/unfinished stroke APIs, test-tracks.json 15 sections / 223 tutorialIds with startIndex/endIndex mapped to node ordinals, 10 AXML shapes, 10 vectors, 1396 dimens",
    "v10: corrected two v9 misattributions — 26dp node corner (16dp belongs to Glance widget square buttons) and 10dp connector stroke (6dp belongs to the LESSON progress bar)",
    "v10: still ZERO Learn locks; one pre-existing exam-hub lock untouched; all v8 corrections unchanged",
]
for x in v10:
    if x not in cf:
        cf.append(x)
rep = m["reproduce"]
for cmd in ["python3 tools/extract_mimo_nodes_v10.py .",
            "python3 tools/build_design_v10.py .",
            "python3 tools/finalize_v10.py ."]:
    if cmd not in rep:
        rep.append(cmd)
m["design_round_9"]["status"] = "DESIGN v9 · SUPERSEDED / RETRACTED by user in round 10 (single straight line) — archived audit trail"
m["design_round_10"] = {
    "status": "DESIGN v10 · REVIEW — awaiting final approval (CURRENT)",
    "trigger": "user: من حرفمو پس میگیرم / همون معماری اورجینال رو به کار ببر / اون خطی که قوس داشت / بیشتر کد رو بکاوی و دقیقاً بازسازی کن",
    "reverted": "v9 single_vertical_line (M196 0 V620, one path, no curves, all nodes on x=196)",
    "main_task": "restore ORIGINAL curved path-map architecture + deeper code review + exact reconstruction",
    "method": "CODE_FIRST / extract_mimo_nodes_v10.py -> NODE_CODE_GEOMETRY.json -> build_design_v10.py -> DESIGN/index.html",
    "layout": {"mode": "original_curved_zigzag", "lanes": [80, 196, 312],
               "lane_sequence": ["center", "right", "center", "left", "center", "left"],
               "node_gap_dp": 24, "pitch_dp": 116, "elbow_radius_dp": 32,
               "elbow_sequence": ["A", "B", "A", "B", "B"],
               "connector_paths": 2, "curve_commands": 5,
               "corner_radius_dp": 26, "stroke_dp": 10, "icon_dp": 48,
               "viewBox": [392, 720]},
    "code_review": {"pathmap_dex_classes": 92, "sections": 15, "tutorial_ids": 223,
                    "shapes": 10, "vectors": 10, "dimens": 1396,
                    "animations_ms": {"enter": 220, "exit": 400}},
    "interactive_prototype": "DESIGN/index.html (14 views / 5 tabs / 93 SVG vectors / 133 painted icons / 6 nodes / 0 Learn locks / 0 jsdom errors)",
    "unchanged": ["5 tabs / no MAX", "routine + Habitica removed", "Dictate removed", "no UI annotations",
                  "7 labelled exam sections + descriptive answer text",
                  "exam architecture / timer / 270 min / پاسخبرگ≠پاسخنامه",
                  "one pre-existing exam-hub lock", "bolt section-practice isolated"],
    "final_log": "22_DESIGN_ROUND_10.md",
    "design_notes": "DESIGN/DESIGN_NOTES.fa.md",
    "final_approval": "PENDING — no product implementation until user says the design is final",
}
mp.write_text(json.dumps(m, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("MANIFEST updated; stable files=%d bytes=%d" % (len(stable), sum(p.stat().st_size for p in stable)))
