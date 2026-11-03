#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate the Konkur-upgrade planning deliverable (Persian docs, CSVs, wireframes).

Uses only static evidence already extracted in this workspace. No runtime claims.
Usage: python3 write_upgrade_plan.py <UPGRADE_DIR>
"""
from __future__ import annotations
import csv, json, sys
from pathlib import Path

OUT = Path(sys.argv[1] if len(sys.argv) > 1 else "/home/user/game/mimo-ui/UPGRADE")
CAT = OUT / "CATALOGS"
CAT.mkdir(parents=True, exist_ok=True)


def w(rel, text):
    p = OUT / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text.strip() + "\n", encoding="utf-8")
    print("wrote", rel, len(text))


def wcsv(rel, header, rows):
    with (CAT / rel).open("w", encoding="utf-8", newline="") as f:
        wr = csv.writer(f)
        wr.writerow(header)
        wr.writerows(rows)
    print("wrote CATALOGS/" + rel, len(rows), "rows")


# ---------------------------------------------------------------- 00 --------
w("00_START_HERE.md", r"""
# شروع کنید — پلن ارتقای Mimo به اپ یادگیری کنکور (دور Plan-Only)

**تاریخ:** ۲۰۲۶-۱۱-۰۳ · **شاخه:** `arena/aebb90b7-game` · **پوشهٔ این دور:** `mimo-ui/UPGRADE/`

این دور **فقط برنامه ریزی عمیق و مستندشده** است، طبق خواستهٔ شما: «فعلا همه توانت رو بزار برای پلن ریزی که بعدا بشه آروم آروم اون پلن رو عملی کرد». هیچ کد محصولی پیادهمسازی نشده است.

## آنچه انجام شد

1. `storytold/craft-anything` v0.3.0 کلون، مستندات/اسکیما/فهرست ۳۲۰ ابزار آن در `CRAFT_ANYTHING/upstream_docs/` وندور شد و یک **لایهٔ عاملی قابلاجرا** (`craft_adapter.py`) با همان شناسههای ابزار و همان قرارداد شواهد نصب شد. توضیح صادقانهٔ مسدودبودن باینری native در `01_CRAFT_ANYTHING_INSTALL.md`.
2. دو APK داخل Drive `mimo` دانلود و **استاتیکاً مهندسی معکوس** شد: `همدرس_7.4.4.apk` و `Hadaf Plus_2.0.2.apk`. خروجی کامل در `SOURCE_APPS/` شامل Census تکتک فایلها، مانیفست دیکدشده، ۴۰۸/۶۲۳ AXML، داراییهای متنی Flutter عیناً، رشتههای Dart AOT (ASCII + UTF-16LE فارسی)، مدلهای API، و **سند UX درون اپ همدرس**.
3. تمام کار قبلی ریپو (شاخهٔ `arena/ecb8af07-game`: استخراج ۰تا۱۰۰ Mimo، HANDOFF، `19_KONKUR_PRODUCT_TRANSFER_SPEC.md`، `18_KONKUR_TRANSFER/`) بازخوانی و به این پلن پیوند شد.
4. موتورهای پینشدهٔ خود ریپو (`LearnHarness` و `EPM`) از GitHub کلون و بررسی شدند تا نقشهٔ اتصال واقعی باشد، نه حدسی.
5. **مهمترین کشف وفاداری**: ناوبری واقعی Mimo 9.35 **چهار تب** است (`Learn / Practice / Leaderboard / Profile`؛ سند `SOURCE/res/menu/bottom_navigation_menu.xml`)، نه سه تب و نه پنج تب. نمونهٔ اولیهٔ قبلی ریپو پنج تب داشت (شامل تب `Max`) → این یک انحراف جدی است و در `02_UI_FIDELITY_CONTRACT.md` صریحاً رد میشود.

## ترتیب خواندن

| # | سند | چرا |
|---|---|---|
| 01 | `01_CRAFT_ANYTHING_INSTALL.md` | وضعیت نصب ابزار و محدودیتها |
| 02 | `02_UI_FIDELITY_CONTRACT.md` | **قانون اساسی**؛ قبل از هر چیز بخوانید |
| 03 | `03_EXAM_HUB.md` | هاب آزمونها، گرههای ۳تایی، تایمر، پنلها |
| 04 | `04_AI_LEARN_HARNESS.md` | ظاهر AI دقیقاً همان + بکاند Learn Harness |
| 05 | `05_COUNSELING_HADAF_PLUS.md` | ۷ قالب هدفپلاس، بدون صفحهٔ اشتراک |
| 06 | `06_PROFILE_AND_GAMIFICATION.md` | پروفایل میمو + گیمیفیکشن سراسری |
| 07 | `07_LESSON_STRUCTURE_AND_QUESTIONS.md` | ساختار درس/سؤال/مرور غلطها |
| 08 | `08_NAVIGATION_AND_IA.md` | ۴ تب، مقصدها، دیپلینک |
| 09 | `09_DATA_MODEL_AND_BACKEND.md` | موتورها، پروکسی، آفلاین، RTL |
| 10 | `10_PHASED_ROADMAP.md` | فازها P0…P7 و دروازههای وفاداری |
| 11 | `11_EVIDENCE_AND_CROSSWALK.md` | منبع هر ادعا + هش |
| 12 | `12_RISKS_UNKNOWN_AND_QUESTIONS.md` | فرضها، ناشناختهها، سؤالها |
| — | `wireframes.html` | نمایش بصری قرارداد وفاداری با توکنهای واقعی میمو |
| — | `CATALOGS/*.csv` | پلن ماشینخوان برای اجرای تدریجی |

## تصمیمات کلیدی (یک جا)

- **هیچ تب جدیدی اضافه نمیشود.** هاب آزمون، مشاوره و AI مقصدهایی **درون همان ۴ تب** هستند.
- **هاب آزمون در تب Practice** قرار میگیرد (`practice_tab_fragment.xml` / `cv_practice_tab` ComposeView)، بهصورت شبکهای از باکس/گره در **ردیفهای ۳تایی** با برچسب زیر هر گره، دقیقاً به زبان طراحی گرههای درسی میمو.
- **بخش AI میمو ظاهرش عیناً میماند**؛ فقط بکاند به Learn Harness وصل و دکمههای LH بهصورت ردیف اکشن در همان باتمشیت نمایان میشوند؛ چیزی حذف نمیشود.
- **مشاوره = ۷ قالب آمادهٔ هدفپلاس** (پومودورو، روز مدرسه، سحر، شب، بعد از ۱۰، تعطیل، دوره/مدرسهای) + درخواست مشاور/گزارش/تحلیل آزمون؛ **صفحهٔ اشتراک، سبد خرید، پرداخت و پیامهای «پرو» حذف میشود**.
- **پروفایل** از `profile_fragment.xml` و توابعش ساخته میشود؛ فیلدهای کنکوری (پایه/رشته/تراز/هدف/روزهای تا کنکور) با همان کارتهای میمو نمایش داده میشوند.
- **گیمیفیکشن اجباری و سراسری**: آزمونها، درسها، مشاوره، AI، «دوستان/رقابت»، قالبها و مرور غلطها همگی به همان سیستم Sparks/XP/Streak/League میمو وصلاند؛ یک واحد پول برای هر حالت، طبق سند `19`.
- ساختار درس و سؤال از DSL/graded vectors/HANDOFF میمو گرفته میشود و با ESQ 1.0 (EPM)، FSRS، نسخهبندی پاسخنامه و شبیهسازی نمرهٔ منفی ارتقا مییابد.

## فرضهایی که اگر اشتباه بودند، فقط فاز P0 اصلاح میشود

- «دوسن مت» → بخش **دوستان / رفاقت و رقابت** (همان `comp` همدرس و `leaderboard_*` میمو).
- «۷ تا قالب» → هفت تصویر `assets/images/study_schedule/` هدفپلاس.
- «Learn Harness» → ریپوی پینشدهٔ `amosblomqvist/learnharness` در `mimo/engines/pins.json`.
- «اون پوشه» → `mimo-ui/UPGRADE/` در ریپو + پوشهای همنام در Drive.

## وضعیت اجرا

هیچکدام از فازها شروع نشدهاند: `CRAFT_ANYTHING/workspace/plan.json` = هشت فاز با وضعیت `PLANNED`. خروجی نهایی این دور، خود پلن و شواهد است.
""")

# ---------------------------------------------------------------- 01 --------
w("01_CRAFT_ANYTHING_INSTALL.md", r"""
# نصب `storytold/craft-anything` روی عامل — گزارش صادقانه

درخواست: «الان همینم نصب کن روی خودت» (`https://github.com/storytold/craft-anything.git`).

## آنچه واقعاً نصب شد

| لایه | وضعیت | مسیر |
|---|---|---|
| سورس v0.3.0 (shallow clone) | ✅ | `/home/user/_work/craft-anything` (خارج از ریپو، scratch) |
| مستندات رسمی + `AGENTS.md` + `CLAUDE.md` + ۴ اسکیمای JSON + `tools.md` (فهرست ۳۲۰ ابزار) + لایسنسها | ✅ وندور شده | `UPGRADE/CRAFT_ANYTHING/upstream_docs/` |
| **لایهٔ عاملی قابلاجرا** (همان شناسههای ابزار، همان قرارداد شواهد، چرخهٔ Study → Build → Check → Ready) | ✅ نصب و اجرا شده | `UPGRADE/CRAFT_ANYTHING/craft_adapter.py` |
| workspace با `craft.json` / `investigation.cany.json` / `plan.json` / `unknowns.json` / `brief.md` | ✅ ساخته و پُر شده | `UPGRADE/CRAFT_ANYTHING/workspace/` |
| خروجی شواهد صادرشده | ✅ | `UPGRADE/CATALOGS/EVIDENCE_LEDGER.json` |
| باینری Rust CLI/AppImage/deb v0.3.0 | ❌ نصب نشد | دلیل در ادامه |
| سرور MCP / دسکتاپ egui / کدینگإیجنت خارجی | ❌ | نیاز به باینری و GTK/agent CLI؛ در این محیط موجود نیست |

## چرا باینری native نصب نشد (و دوباره امتحان نشد)

- `gh release download v0.3.0 --pattern 'craft-anything-0.3.0-linux-x86_64.tar.gz'`, الگوی `SHA256SUMS.txt`، `gh api .../releases/assets/702372637 -H 'Accept: application/octet-stream'` و `curl -L` مستقیم، همگی با `TLS EOF` / `SSL_ERROR_SYSCALL` شکست خوردند: داراییهای release روی `release-assets.githubusercontent.com` و `objects.githubusercontent.com` هستند که **خارج از allowlist خروجی این سندباکس** قرار دارند (`github.com`, `codeload.github.com`, `api.github.com`, `registry.npmjs.org`, `pypi.org`, `files.pythonhosted.org` مجازاند).
- `cargo`, `rustc`, `rustup` وجود ندارند؛ `apt-cache policy rustc cargo` هیچ بستهای برنگرداند؛ ساخت از سورس نیاز به Rust 1.97+ و کتابخانههای GTK dev دارد.
- بستهٔ npm به نام `craft-anything` وجود ندارد (`npm view` → 404)؛ پکیج PyPI معادل هم نیست.
- بنابراین **همان مسیر unchanged دوباره امتحان نشد**؛ بهجای آن لایهای نصب شد که عامل واقعاً بتواند فراخوانی کند.

## چگونه از آن استفاده شد (قابل تکرار)

```
python3 UPGRADE/CRAFT_ANYTHING/craft_adapter.py commands
python3 UPGRADE/CRAFT_ANYTHING/craft_adapter.py doctor
python3 ... core-target-open --path <apk> --label <name>
python3 ... core-finding-record --text <...> --confidence VERIFIED_STATIC
python3 ... core-unknown-add --text <...>
python3 ... core-plan-update --phase P0 --status PLANNED
python3 ... core-evidence-show
python3 ... core-evidence-export --out UPGRADE/CATALOGS/EVIDENCE_LEDGER.json
```

نتیجهٔ `doctor`: `READY (agent adapter)`، حالت `deep` (چون داخل APKها را خواندهایم)، ۳ target، ۱۳ رکورد شواهد، ۸ فاز، ۵ ناشناخته.

قرارداد شواهد رعایت شده است: هر رکورد `evidence_id`, `operation`, `toolset`, `subject`/`content`, `confidence`, `authority`, `coverage`, `limitations`, `locations`, `created_ms` دارد. قواعد طلایی upstream که در این دور اعمال شدند: «Evidence is the result»، «Never crash»، «Clean room vs Deep»، «Effects are honest»، «No secrets»، «Thin UI / theme tokens».

## نسبت با REA

`morluto/rea` (الزام قبلی شما) همچنان منبع **انضباط شواهد** و استخراج جاوااسکریپت/WebView میمو است؛ `craft-anything` در این دور بهعنوان **چارچوب مطالعه/ساخت/بررسی و دفتر شواهد** روی همان دادهها سوار شد. هر دو در `11_EVIDENCE_AND_CROSSWALK.md` با سطح اطمینان مشخص شدهاند. تولید اپ همچنان **clean-room** است: هیچ دارایی، کد، نام یا متنی از Mimo/همدرس/هدفپلاس به محصول کپی نمیشود؛ فقط قراردادها و الگوهای رفتاری مستند میشوند.

## محدودیت صریح

این آداپتور **جایگزین موتور ۳۲۰ ابزاری Rust نیست**؛ فقط لایهای است که عامل بتواند همان روش را در این محیط اجرا کند. ابزارهایی که در upstream به باینری وابستهاند (`android_dart_snapshot_show` عمیق، `core_disasm_*`, Ghidra/adb/CDP) اینجا اجرا نشدند؛ معادل استاتیک آنها (`extract_source_apps.py` + androguard + استخراج رشتهها) استفاده شد و در ستون `limitations` ثبت گردید.
""")

# ---------------------------------------------------------------- 02 --------
w("02_UI_FIDELITY_CONTRACT.md", r"""
# قرارداد وفاداری به UI/سازوکار Mimo — **مهمترین سند این دور**

> مشکلی که خودتان گفتید: «بزرگترین مشکل عدم وفاداری به یو آی اصلی اپه… خیلی خیلی خیلی مهمه اینکه اپلیکیشن همون سازکار رو داشته باشه».
> این سند، پاسخ normative و قابلتست به آن است. **هر فاز اجرا بدون عبور از دروازههای F0…F9 مجاز به ادامه نیست.**

## ۱. منبع حقیقت (Source of Truth)

| منبع | مسیر | محتوا |
|---|---|---|
| استخراج ۰تا۱۰۰ دور قبل | `mimo-ui/` | ۱۴٬۳۹۸ عضو APK هش/طبقهبندیشده، ۱۲٬۹۱۵ شناسهٔ منبع، ۵۰٬۴۷۷ ردیف کانفیگ، ۲٬۸۵۹ AXML دیکدشده بدون خطا، **۱٬۲۹۹ لایوت**، **۲۷۶ دوسیه صفحه**، ۱۰۹ اسکلت Kotlin، ۵۳ ویوی سفارشی، ۱۶ سند فارسی |
| اطلس آفلاین | `mimo-ui/ATLAS/index.html` | نمایشگر self-contained تمام صفحات/لایوتها/توکنها |
| توکنها | `mimo-ui/CATALOGS/DESIGN_TOKENS.json`, `ATLAS/tokens.css` | ۱٬۱۹۸ رنگ، ۱٬۴۰۱ dimens/style/drawable، ۱۱۶ لوکال |
| راستیآزمایی | `mimo-ui/CATALOGS/VERIFICATION_REPORT.json` | `PASS` / ۱۸ چک / ۵٬۴۷۴ فایل هششده |

هیچ تصمیم بصری از حافظه، حدس، یا اسکرینشات اپهای دیگر گرفته نمیشود؛ فقط از این منابع.

## ۲. ناوبری واقعی = **۴ تب** (کشف اصلاحی)

`mimo-ui/SOURCE/res/menu/bottom_navigation_menu.xml`:

| ترتیب | id | آیکن | رشته | مقدار |
|---|---|---|---|---|
| ۱ | `bottom_navigation_item_track` | `ic_tab_learn` | `navigation_path` | Learn |
| ۲ | `bottom_navigation_item_practice` | `ic_tab_practice` | `navigation_practice` | Practice |
| ۳ | `bottom_navigation_item_leaderboard` | `ic_tab_leaderboard` | `navigation_leaderboard` | Leaderboard |
| ۴ | `bottom_navigation_item_profile` | `ic_tab_profile` | `navigation_profile` | Profile |

قالب: `main_activity_content.xml` با `contentFrame`, `navigation_bar`, `container_bottombar`.

**رد صریح انحرافها:**

| انحراف | منبع | حکم |
|---|---|---|
| ۵ تب `Learn / Practice / Max / Leaderboard / Profile` | `/home/user/_work/prev/mimo/shell/app.js` (نمونهٔ اولیهٔ قبلی) | ❌ تب `Max` حذف؛ ناوبری ۴تبه بازگردانده شود |
| «۳ تب» در برخی اسناد قدیمی | `18_KONKUR_TRANSFER/ADAPTATION_PLAN.md` | ❌ اصلاح به ۴ تب |
| قرار دادن موتورهای وب بهعنوان تب مستقل | همان پروتوتایپ | ❌ موتورها پشت مقصدهای درونتبی پروکسی میشوند |
| ساختن زبان بصری تازه برای کنکور | ریسک اصلی | ❌ ممنوع؛ فقط ترکیب مجدد کامپوننتهای موجود |

## ۳. قانون طلایی

> **هر صفحهٔ تازه = ترکیبی از کامپوننتها، توکنها، الگوهای ناوبری و رفتارهای ازپیشاستخراجشدهٔ Mimo. هیچ رنگ، فونت، شعاع، فاصله، انیمیشن، آیکن، متن یا الگوی تعامل تازهای تعریف نمیشود.**

بخشهای جدید **مقصد** هستند، نه **تب** و نه **برنامهٔ جدا**:

| بخش تازه | تب میزبان | نقطهٔ ورود از Mimo |
|---|---|---|
| هاب آزمونها | Practice | `practice_tab_fragment.xml` → `cv_practice_tab` (ComposeView) + `include @layout/toolbar` |
| مشاوره + ۷ قالب | Practice (کارت ورودی) / Leaderboard (رقابت) | `base_modal_card.xml`, `bottom_sheet_dialog`, `flash_bar_view.xml` |
| AI (ظاهر unchanged) | همان محل همیشگی | `coding_keyboard_layout.xml` → `btn_ai_tutor`, `iv_ai_tutor_pulse`؛ ۲۸ رشتهٔ `ai_tutor_*`؛ سطح چت Compose |
| پروفایل کنکوری | Profile | `profile_fragment.xml`, `profile_header_view.xml`, `profile_info_card_view.xml`, `profile_certificates_view.xml`, `profile_trophies_item.xml`, `profile_friends_*`, `public_profile_activity.xml`, `settings_fragment.xml` |
| دوستان/رقابت | Leaderboard | `leaderboard_fragment_active.xml`, `leaderboard_item.xml`, `leaderboard_podium_item.xml`, `leaderboard_result_*` |

## ۴. توکنهای الزامی (عیناً از استخراج)

رنگها (روز / شب):

| نقش | روز | شب |
|---|---|---|
| `background_primary` | `#FFF6F7FB` | `#FF252746` |
| `card_enabled` | `#FFFFFFFF` | `#FF3F4273` |
| `card_pressed` | `#FFF6F7FB` | `#FF333661` |
| `card_disabled` | `#FFE4E6F1` | `#FF1D1F32` |
| `card_outline` | `#FF7E4BDE` | `#FF885BDE` |
| `button_primary` | `#FF7E4BDE` | `#FF885BDE` |
| `text_primary` | `#FF252746` | `#FFFFFFFF` |
| `accent_success` | `#FF66BC5A` | `#FFA4E59B` |
| `error_default` | `#FFF05A6E` | `#FFF97F8D` |
| `code_background` | `#FFFFFFFF` | `#FF1D1F32` |
| `progress_chapter_primary` | `#FF8D60E2` | `#FFB89CED` |

ابعاد: فاصلهها `4 / 8 / 12 / 16 / 24 / 32 / 40dp`؛ نسخهٔ `sw600dp` برابر `6 / 12 / 16 / 24 / 36 / 48 / 60dp`؛ شعاع غالب `12dp`، بلوک کد `6dp`؛ `content_max_width 608dp`؛ `bottom_sheet_content_max_width 496dp`؛ `lesson_progressbar_height 6dp` (`sw600dp: 8dp`)؛ `coding_keyboard_height 64dp`؛ `modal_default_width 296dp` (`sw600dp: 360dp`)؛ `streak_calendar_height 264dp` (`sw600dp: 324dp`)؛ `toolbar_height`، `lesson_progress_navbar_height`، `lesson_feedback_sheet_peek_height 112dp`. تایپوگرافی ۱۲…۴۲sp (شمارندهٔ XP = ۴۲sp، متن ادیتور کد = ۱۵sp).

حرکت: ۷۲ `anim/`، ۴۷ `animator/`، ۲۴ interpolator، ۵۹ Rive، `bottom_sheet_slide_in/out`، `fade_in/out`، پالس AI، `ArcProgressView`، `lesson_progressbar`، `avatar_progress_bar`. صفحات تازه از همان منحنیها و مدتها استفاده میکنند.

## ۵. کامپوننتهای قابل استقرار مجدد

- ۷۱ لایوت دارای `ComposeView`، `ViewPager2` (نمایش درسها)، `FragmentContainerView`، `AppBarLayout` + `ChapterToolbar` / `include @layout/toolbar`، ۲٬۷۷۱ `<include>/<merge>`.
- ۵۳ ویوی سفارشی: `ArcProgressView`, `AvatarProgressBar`, `AnswerButtonGrid`, `CodingKeyboardView`, `ExpandableTextView`, `LessonFeedbackView`, `MimoCodeEditor`, `RiveAnimationView`, `ShimmerFrameLayout`, `StreakCalendarView`, `BottomSheetHandleView` …
- قطعات آماده: `base_modal_card.xml` ( modal عمومی )، `flash_bar_view.xml` (پیام/اقدام)، `reward_box.xml`، `daily_sparks_goal_progress_view.xml`، `streak_bottom_sheet_content.xml`، `chapter_finished_fragment.xml` (صفحهٔ نتیجه)، `leaderboard_result_*`، `report_lesson_fragment.xml`، `lesson_interactive_*` (سؤالات تک/چندگزینهای، جایخالی، ورودی اعتبارسنجیشده).

## ۶. دروازههای وفاداری (Fidelity Gates) — برای هر فاز

| id | چک قابلسنجش | معیار قبولی |
|---|---|---|
| F0 | تعداد آیتمهای `bottom_navigation_menu.xml` | دقیقاً ۴، با همان id/آیکن/رشته |
| F1 | تعداد تبهای ساختهشده در shell | ۴؛ هیچ `Max`/`Exam`/`Counseling` tab وجود ندارد |
| F2 | منبع هر رنگ/فاصله/شعاع/فونت صفحهٔ تازه | قابل ردیابی به `DESIGN_TOKENS.json`؛ ۰ مقدار هاردکد تازه |
| F3 | منبع ساختار هر صفحهٔ تازه | حداقل یک دوسیه از `mimo-ui/SCREENS/` یا `LAYOUTS/` بهعنوان الگو ثبت شود |
| F4 | رفتار بازگشت/باتمشیت/مودال | همان زنجیرهٔ مودال Mimo؛ بستن با `iv_modal_close`، `backdrop dismiss` |
| F5 | حالتهای کارت | `card_enabled/pressed/disabled/outline` + نایت مُد، بدون حالت تازه |
| F6 | RTL | همهٔ صفحات فارسی `layoutDirection=rtl`؛ فقط کروم کد/فرمول LTR؛ اعداد فارسی طبق policy |
| F7 | دارایی | ۰ کپی از asset/رشته/کد Mimo، همدرس، هدفپلاس در محصول (clean-room) |
| F8 | تحلیل اثر | لیست `include`/`xref` صفحهٔ تازه با `mimo-ui/CATALOGS/LAYOUT_XREFS.csv` مقایسه شود |
| F9 | مقایسهٔ بصری | diff اطلس: صفحهٔ تازه در کنار دوسیهٔ مرجع، حداقل ۹۰٪ تطابق توکن/فاصله (تست خودکار + نگاه انسانی) |

**هرگونه تغییر ظاهری در بخش AI فقط در حد اضافهشدن ردیف دکمههای Learn Harness مجاز است** (`04_AI_LEARN_HARNESS.md`)؛ حذف هیچ عنصری مجاز نیست.

## ۷. «سازوکار» یعنی چه (غیر از ظاهر)

وفاداری فقط رنگ نیست؛ این رفتارهاهمچنین باید حفظ شوند:

1. **مسیر درسی بهصورت گرههای پیشرونده** با حالتهای قفل/فعال/تکمیلشده و نوار پیشرفت ۶dp؛ هاب آزمون همین الگو را برای گرههای آزمون تکرار میکند.
2. **حلقهٔ درس**: نمایش → پاسخ → بازخورد فوری (`lesson_interactive_feedback_bottom_sheet_dialog.xml`) → XP → صفحهٔ پایان فصل → streak → لیدربورد.
3. **پیشرفت سهگانه** (`chapterProgress`, `tutorialProgress`, `trackProgress`) و `globalStats`؛ هر فیچر تازه باید به همان سهگانه بنشیند.
4. **آفلاین + outbox**: محتوا باندل، نتایج در صف، همگامسازی بعداً؛ موتورها دیتاستور جدا دارند.
5. **Daily goal / Sparks / Streak / League**: همان مدل امتیاز و همان `daily_sparks_goal_progress_view.xml`.
6. **مودال/باتمشیت بهجای صفحهٔ تمامصفحه** برای تنظیمات سریع؛ `contentDescription` و `TextInputLayout` برای دسترسپذیری.
7. **WebView lesson bridge** (`gesture/activity/focus/height`, `MimoLesson.postMessage`) برای درسهای تعاملی موجود؛ سؤالات کنکور یا همین پل را استفاده میکنند یا `lesson_interactive_*` بومی.

## ۸. ضدرگرسیون — چکلیست قبل از هر PR اجرایی

- [ ] `F0…F9` همگی PASS و نتیجه در `CATALOGS/FIDELITY_CHECKS.json` ثبت شده
- [ ] هیچ تب/صفحهای با نام موتور (`Max`, `Practice Machine`, `LearnHarness`) در ناوبری دیده نمیشود
- [ ] هیچ صفحهٔ اشتراک/پرداختی اضافه نشده است
- [ ] رشتههای `ai_tutor_*` تغییر نکردهاند
- [ ] نسخهٔ نایت مُد تست شده
- [ ] `ATLAS/index.html` همچنان مرجع است و دوسیهٔ صفحهٔ تازه به آن اضافه شده
""")

# ---------------------------------------------------------------- 03 --------
w("03_EXAM_HUB.md", r"""
# هاب آزمونها — قلب ارتقا (تب Practice)

خواسته: «تو بخش تمرین همین اپلیکیشن بتونن یه بخش بزرگ باشه که ازمون بدن… آزمونهای زماندار، آزمونهای درسی، آزمونهای جامع، تک درسی، تا مبحث، آزمون این ماه… انگار تعداد زیادی باکس جعبهای هست شبیه همون گرههای درسی میمو، ردیفهای سهتایی باشه خوبه، زیرشم اسم داشته باشه… خودت ازادی تصمیم بگیری… تایمرم بزاری یه سری پان بریزی».

## ۱. جایگاه (بدون تب جدید)

`practice_tab_fragment.xml` از قبل یک `ComposeView` به نام `cv_practice_tab` و یک `AppBarLayout` با `include @layout/toolbar` دارد. تغییر مجاز: **اضافهکردن یک کارت ورودی «آزمونها» به بالای محتوای Compose** و یک مقصد `ExamHub` در همان گراف تب Practice. تبها، `main_activity_content.xml` و `bottom_navigation_menu.xml` دستنخورده باقی میمانند (F0/F1).

## ۲. تصمیم طراحی: شبکهٔ ۳ ستونه RTL از «گره»

چرا ۳تایی: (الف) خواستهٔ صریح شما؛ (ب) با `content_max_width 608dp` و گاتر `16dp`، عرض هر گره `(608 − 2×16)/3 ≈ 192dp` میشود که تقریباً همان مقیاس گره فصل میمو است؛ (ج) در `sw600dp` با ۴ ستون و گاتر `24dp` هم همچنان خوانا است. ترتیب **راست به چپ**: اولین گره ردیف در سمت راست.

```
┌────────────────────────────── AppBar / toolbar (include @layout/toolbar) ───────────────┐
│  آزمونها                                                   [ ⏱ ۱۲:۴۵ ]  [؟]            │  ← تایمر chip با همان lesson_progress_navbar_height
├──────────────────────────────── chips فیلتر (همه / جامع / تکدرسی / مبحثی / این ماه) ─────┤
│   ┌────────┐   ┌────────┐   ┌────────┐                                                   │
│   │  ◇     │   │  ◇     │   │  ◇     │   ← گره: card_enabled + card_outline + 12dp radius│
│   └────────┘   └────────┘   └────────┘                                                   │
│   آزمون جامع    آزمون تکدرسی   آزمون مبحثی   ← برچسب 14sp / text_primary / زیر گره      │
│   ┌────────┐   ┌────────┐   ┌────────┐                                                   │
│   │  ✓     │   │  🔒    │   │  ⏱     │   ← success / disabled / timer badge             │
│   └────────┘   └────────┘   └────────┘                                                   │
│   آزمون این ماه  آزمون نهایی  آزمون زماندار                                               │
└──────────────────────────────────────────────────────────────────────────────────────────┘
                                   [ Learn ] [ Practice ] [ Leaderboard ] [ Profile ]
```

مشخصات گره (همه از توکنهای موجود):

| ویژگی | مقدار |
|---|---|
| پسزمینهٔ عادی / فشرده / قفل / فعال | `card_enabled` / `card_pressed` / `card_disabled` / `card_outline` |
| شعاع / ارتفاع / گاتر | `12dp` / `96dp` (همسان گره فصل) / `16dp` (`sw600dp: 24dp`) |
| پیشرفت | `progress_chapter_primary` + `progress_chapter_background`، ارتفاع `lesson_progressbar_height 6dp` |
| وضعیت موفق/ناموفق | `accent_success` / `error_default` |
| برچسب | ۱۴sp، `text_primary`، حداکثر ۲ خط، `contentDescription` کامل |
| نشانها | تایمر، تعداد سؤال، قفل، «جدید»، `XP`؛ همگی با آیکنهای میمو (۰ آیکن تازه) |
| کلیک | ripple میمو + `bottom_sheet_slide_in` برای پنل تنظیمات آزمون |

گروهبندی پیشنهادی (همان الگوی «فصلها»ی میمو): `آزمونهای این ماه` → `آزمونهای جامع` → `تکدرسی` → `مبحثی` → `تشریحی/دوباره`. هر گروه یک سرتیتر ۱۶sp و یک ردیف ۳تایی یا چند ردیف. تعداد گرهها زیاد است ولی صفحه لایهای میماند، نه لیست بیپایان.

## ۳. انواع آزمون (ترکیب خواستهٔ شما + شواهد دو اپ)

`CATALOGS/EXAM_TYPES.csv` ماشینخوان است. خلاصه:

| دسته | نمونه | محدوده | زمان | نمرهٔ منفی | منبع شاهد |
|---|---|---|---|---|---|
| جامع | آزمون جامع کنکور، سراسری شبیهساز | همهٔ دروس | ۲۷۰ دقیقه | ⅓ | خواسته + `آزمون ماز/گاج` هدفپلاس |
| تکدرسی | زیست، شیمی، فیزیک، ریاضی، عربی… | یک درس | ۴۵…۹۰ | ⅓ | خواسته + `SampleExam/FindAllByLevelAndField` |
| تا مبحث | «سمها»، «تجزیه»، … | یک مبحث | ۱۵…۳۰ | ⅓ | خواسته + `lesson_model.json` هدفپلاس |
| درسی/فصلی | آزمون درسی، آزمون نهایی | یک فصل | ۳۰…۶۰ | ⅓ | خواسته + `آزمون نهایی` همدرس |
| این ماه | آزمون این ماه، آزمون تازه | تقویم ماه | متغیر | ⅓ | خواسته + `آزمون تازه`/`آزمونهای من` هدفپلاس |
| زماندار | آزمون زماندار، پومودورو تست | دلخواه ۵…۴۰۰ سؤال | تایمر کاربر | اختیاری | خواسته + `تعداد سوال باید بین ۵ تا ۴۰۰ باشه` |
| تشریحی | آزمون تشریحی | پاسخ تشریحی | — | — | `آزمون تشریحی` همدرس |
| دوباره / مرور غلطها | آزمون دوباره، تمرین اشتباهها | غلطهای ذخیرهشده | — | — | `آزمون دوباره`، `تمرین اشتباههای تمام مباحث` |
| شخصیساخته | `PersonalExam/Create` | کاربر | — | — | endpoint هدفپلاس |

هر آزمون یک **Blueprint نسخهدار** دارد: `{examId, type, scope[], questionCount, durationSec, negativeMarking, difficultyMix, answerKeyVersion, seed, xpPolicy, retryPolicy, panelSet, version}`. نسخهبندی پاسخنامه از سند `19` الزامی است.

## ۴. تایمر (الزامی)

- نمایش: chip در `ChapterToolbar` (همان `lesson_progress_navbar_height`) با `error_default` در ۱۰٪ پایانی و لرزش هشدار میمو.
- منطق: `elapsedRealtime()` مونوتونیک (نه ساعت دستگاه)، توقف/ادامه، ذخیرهٔ خودکار هر ۵ ثانیه، ادامهٔ خودکار بعد از kill اپ، اتمام خودکار و ثبت پاسخها در صفر.
- پنل تایمر: «زمان هر سؤال»، «زمان اضافه» (ایده از همدرس: با الماسها زمان اضافه بخری → اینجا با همان اقتصاد Sparks، بدون خرید)، «توقف موقت»، «خروج؟» (متن همدرس: «Are you sure that you want to exit the exam?» / «آیا از خروج آزمون اطمینان داری؟»).
- محدودیت سقف مطالعهٔ هدفپلاس («تایمر شما ممکن است در میانه مسیر متوقف شود…») بهصورت **هشدار غیرمسدودکننده** ترجمه میشود، نه قفل.

## ۵. پنلها («پان»ها) — همگی از باتمشیت/مودال میمو

| پنل | کامپوننت میمو | محتوا |
|---|---|---|
| تنظیمات آزمون | `base_modal_card.xml` + `bottom_sheet_slide_in` | تعداد سؤال، سختی، نمرهٔ منفی، زمان، ترتیب، `شروع` |
| پالت سؤالات | باتمشیت با گرید ۳تایی | شمارهها، وضعیت پاسخ/علامت/نزده (ایده `answer_sheet.svg` هدفپلاس) |
| پاسخبرگ | همان گرید | `اسم پاسخبرگ (اختیاری)`, `ثبت پاسخها و محاسبهٔ خودکار درصد` |
| راهنما/رتبهٔ دشواری | `flash_bar_view.xml` | «درجه سختی سؤال»، «دو گزینهٔ غلط رو حذف کن» (همدرس) |
| خروج / اتمام | `base_modal_card.xml` | تأیید خروج، «ثبت پاسخها و پایان آزمون» |
| نتیجه | `chapter_finished_fragment.xml` | درصد، تراز، XP، streak، دکمهٔ ادامه |
| تحلیل | `report_lesson_fragment.xml` + چارت | `Chart of Test Scores`, `Chart of Descriptive Test Score` (همدرس) |
| مرور غلطها | `WrongView` معادل بومی + `reward_box.xml` | پاسخ تشریحی، `تعویض سوال`, `حذف سوال`, FSRS |

عرض باتمشیت `bottom_sheet_content_max_width 496dp`، مودال `296dp`، در `sw600dp` بهترتیب همان مقادیر ارتقایافته.

## ۶. جریان سؤال (سازوکار میمو + ارتقا)

1. بارگذاری Blueprint و بانک سؤال (ESQ 1.0 / JSON میمو) بهصورت آفلاین.
2. نمایش سؤال: `lesson_interactive_singlechoice_fragment.xml` (۴ گزینه)، فرمولها با `<equation>`، شکلها با `<figure>`، `rtlMarker` و نرمالساز فارسی.
3. پاسخ → **بازخورد فوری** میمو (`lesson_interactive_feedback_bottom_sheet_dialog.xml`)؛ در حالت آزمون، بازخورد تا پایان آزمون **به تعویق** میافتد و فقط «ثبت شد» نشان داده میشود (تنها تفاوت رفتاری مجاز، چون ماهیت آزمون است).
4. ذخیرهٔ پاسخ در Room + outbox؛ `answerKeyVersion` و `questionVersion` همراه هر تلاش.
5. اتمام → محاسبه: درصد خام، نمرهٔ منفی ⅓، `تعداد سوالات نزده`, `تعداد سوالات تشریحی`, `تعداد غلط`؛ شبیهساز «اگه غلطها رو نزده میذاشتی، درصدت… » (هدفپلاس)؛ تحلیل بر حسب مبحث (`AnalyisByLessonsScreenWidget` همدرس)؛ نقشهٔ ضعف؛ `تراز`/`رتبه` با `daysRemainingToKunkor`.
6. **مرور/حذف غلطها**: `تمرین اشتباههای تمام مباحث`، `آزمون دوباره`، `مرور مبحث`/هوشمند (همدرس)، FSRS (EPM)، پاسخ تشریحی، قابلیت «تعویض سوال» و «حذف سوال». غلط فقط وقتی از لیست خارج میشود که دو بار متوالی درست پاسخ داده شود (قابل پیکربندی).
7. XP/امتیاز: سختی ۱…۵ (همدرس: ساده/متوسط/سخت/خیلیسخت/المپیادی) × ضریب درس (دروس تخصصی ×۲)، منهای جریمهٔ غلط؛ به همان `daily_sparks_goal_progress_view.xml` و لیگ واریز میشود.

## ۷. پذیرش فاز P1/P2

- [ ] ۳ ستون RTL، برچسب زیر گره، ۰ رنگ/آیکن تازه (F2/F5)
- [ ] حداقل ۹ نوع آزمون قابلانتخاب و ۱۲+ گره قابلنمایش
- [ ] تایمر مونوتونیک + توقف/ادامه + اتمام خودکار + ذخیرهٔ خودکار
- [ ] ۷ پنل بالا با باتمشیتهای میمو
- [ ] نتیجه، تحلیل، مرور غلطها، XP وصل به سیستم سراسری
- [ ] نسخهبندی پاسخنامه و آفلاین/outbox تست شده
""")

# ---------------------------------------------------------------- 04 --------
w("04_AI_LEARN_HARNESS.md", r"""
# بخش هوش مصنوعی میمو — ظاهر عیناً همان، بکاند Learn Harness

خواسته: «دقیقا ظاهر اون بخش هوش مصنوعی میمو رو نگه میداری ولی پشتش بک اندش رو باید وصل کنی لرن هارنس… داخل بقیه اپلیکیشنهای مشاوره هم همچین بخشی هست، هرچند رابط کاربریش مختصر باید تغییر کنه تا دکمههای لرن هارنس داخل یو آی دربیاد و حذف نشه».

## ۱. آنچه **نباید** تغییر کند (Frozen Surface)

از استخراج Mimo 9.35:

- نقطهٔ ورود: `res/layout/coding_keyboard_layout.xml` → `@id/btn_ai_tutor` و `@id/iv_ai_tutor_pulse` (پالس همان انیمیشن).
- متنها: ۲۸ رشتهٔ `ai_tutor_*` و `ai_*` عیناً: `ai_tutor_chat_header`, `ai_tutor_input_placeholder`, `ai_tutor_input_max_characters`, `ai_tutor_first_hint`, `ai_tutor_second_hint`, `ai_tutor_start_message`, `ai_tutor_intro_title`, `ai_tutor_intro_benefit_1..4`, `ai_tutor_intro_disclaimer`, `ai_tutor_error_message_template`, `ai_tutor_offline_description`, `ai_intro_no_chat_history`, `ai_mascot_name`, `ai_initial_prompt_*`, `ai_progress_banner_*`.
- سطح چت **Compose** است (هیچ `ai_tutor_*.xml` جداگانهای وجود ندارد؛ ۷۱ لایوت ComposeView)، بنابراین قرارداد بصری از روی همان کامپوننت Compose و توکنها حفظ میشود: هدر، حبابها، نوار ورودی، `ai_tutor_input_placeholder`، حالت آفلاین، بنر پیشرفت، خطا، ماسکات.
- پالس، `bottom_sheet_slide_in/out`، `flash_bar_view` برای پیامها.

**هیچ عنصری حذف نمیشود.** تنها افزودهٔ مجاز: یک **ردیف اکشن (Action Dock)** زیر نوار ورودی، برای نمایانکردن قابلیتهای Learn Harness.

## ۲. بکاند: Learn Harness پینشدهٔ خود ریپو

`/home/user/_work/prev/mimo/engines/pins.json`:

```json
{"repo": "https://github.com/amosblomqvist/learnharness.git",
 "commit": "e69e85269c064c6c9c49a8b06ae78c06e79c4a63",
 "license": "AGPL-3.0-only",
 "stack": "Next.js 16 (React 19) + its own Node server",
 "run": "next dev --port 3000 with LH_DATA_DIR + LH_AUTH_FILE isolated",
 "integration": "basePath=/max and reverse-proxied at /max (prefix kept)"}
```

- اسکریپت `mimo/engines/prepare_learnharness.py` همان `basePath: "/max"` را تزریق میکند؛ `start-preview.sh` پورت ۳۰۰۰ را پشت `/max/*` پروکسی میکند (پیشوند **حفظ** میشود، برخلاف `/practice/*` که حذف میشود).
- `LH_DATA_DIR` و `LH_AUTH_FILE` جدا از Mimo و EPM؛ **هیچ دیتاستور مشترکی** وجود ندارد (قاعدهٔ سند `19`).
- **LH بازنویسی نمیشود**: همان Next.js اجرا میشود؛ تنها لایهٔ فارسی/RTL و تزریق زمینه (context) به آن اضافه میشود.
- محتوای آموزشی LH: Measure → Plan → Teach → Practice، گراف دانش پایدار، confidence rail، thinking fields، hints، practice sessions. اینها دقیقاً همان «سازوکار یادگیری»ای هستند که باید پشت ظاهر میمو قرار بگیرند.

## ۳. زمینهای که به LH داده میشود (و آنچه داده نمیشود)

داده میشود: `lessonId`, `documentId`, `subject`, `topic`, `userLevel`, `recentMistakes[]`, `visible-if` وضعیت، `progress triple`، زبان `fa`.
**داده نمیشود**: پاسخ صحیح، `answerKey`، `offset`های نمرهدهی، کلید مدل، اطلاعات شخصی (قواعد سند `19` و «No secrets»ی craft-anything).

## ۴. دکمههای LH که باید «داخل UI دیده شوند و حذف نشوند»

از کامپوننتهای واقعی کلونشدهٔ LH (`components/home.tsx`, `new-session.tsx`, `top-bar.tsx`, `composer-actions.tsx`, `practice-cards.tsx`, `question-dock.tsx`, `graph-view.tsx`, `plan-window.tsx`, `confidence-rail.tsx`, `thinking-block.tsx`, `notes-import.tsx`, `dictation.tsx`, `session-navigation.tsx`). فهرست کامل در `CATALOGS/LEARNHARNESS_ACTIONS.csv`.

| اکشن LH | برچسب فارسی در ردیف اکشن میمو | رفتار |
|---|---|---|
| `Start session` / `aria-label="Start session"` | «جلسهٔ تازه» | شروع Measure→Plan |
| `Sessions` + `session-navigation` | «جلسهها» | لیست/ادامهٔ جلسه |
| `Plan window` / `Targets` | «نقشهٔ یادگیری» | نمایش dependency map |
| `Knowledge graph` / `Search nodes` | «گراف دانش» | نمودارگزارهها |
| `Practice` / `Next problem` / `Retest` | «تمرین» / «سؤال بعد» | نشست تمرین مجزا |
| `Check your understanding` | «بفهمم یا نه» | مرحلهٔ Teach |
| `Confidence rail` | «میزان اطمینان» | ثبت confidence |
| `Thinking fields` / «Think out loud» | «فکر کردن با صدای بلند» | فیلد تفکر |
| `Hint rung` | «راهنما» | نردبان راهنما |
| `Notes import` | «یادداشتهام» | واردکردن جزوه |
| `Researcher`, `Figure maker`, `PDF reader`, `Demo builder` | «پژوهش»، «شکل»، «PDF»، «نمونه» | ابزارهای پسزمینهای |
| `Model` / `Context` / `Cost` / `Steps` / `Settings` | «مدل»، «هزینه» | همان chipهای LH |
| `Dictation` | «گفتار» | دیکته (اختیاری) |
| `Stop` / `Abort` / `End this background process` | «توقف» | قطع جریان |

نمایش: همان `flash_bar_view.xml` / ردیف chip با `card_pressed`، `12dp`، `8dp` فاصله، اسکرول افقی RTL، `contentDescription` کامل؛ **بدون تغییر هدر، حباب، نوار ورودی، ماسکات و پالس**. در حالت آفلاین، chipها به `card_disabled` میروند و `ai_tutor_offline_description` نشان داده میشود (نه صفحهٔ خرید).

## ۵. مقایسه با اپهای مشاوره (آموختهها)

- همدرس: `AIChatWebViewScreen`, `AiChatConversationScreen`, `AiChatInputBar`, `AiChatCubit`, `AiChatThemeCubit`, ۲۶ دارایی `assets/ai_chat/` (ربات، `Counselor.svg`, میکروفون، کپی، لایک/دیسلایک، `magic_pen`, `documents`, `gallery-send`, `question-square`, `volume`)، و درسهای UX `ai-ask` و `ai-credit`.
- هدفپلاس: `/Chatbot/conversations`, `/Chatbot/messages/stream`, انیمیشن `chatbot.json`, `اتاق رسمی هدفپلاس`, `/Chat/Admins`, `/Chat/Studying`.
- نتیجه: اپهای مشاوره AI را **بهصورت چتتمامصفحه + اعتبار/خرید** نشان میدهند؛ ما این الگو را **نمیپذیریم**، چون وفاداری به میمو اولویت دارد. فقط ایدهٔ «دکمههای قابلیت کنار ورودی» و «لایک/دیسلایک پاسخ» بهعنوان **چیپهای اختیاری در همان ردیف اکشن** گرفته میشود؛ «اعتبار/بسته/اشتراک» حذف میگردد.

## ۶. پذیرش فاز P4

- [ ] diff رشتههای `ai_tutor_*` = ۰ تغییر؛ `@id/btn_ai_tutor` و `iv_ai_tutor_pulse` سر جای خود
- [ ] `/max/*` پاسخ میدهد، `LH_DATA_DIR` جدا است، prefix حفظ شده
- [ ] ۱۶ اکشن LH در UI قابلرویتاند و هیچکدام پشت منوی پنهان نیستند
- [ ] پاسخ صحیح/کلید/answerKey هرگز در prompt ارسال نمیشود (تست خودکار)
- [ ] حالت آفلاین و خطا با همان رشتههای میمو
- [ ] نایت مُد و RTL تست شده؛ ۰ تب جدید
""")

# ---------------------------------------------------------------- 05 --------
w("05_COUNSELING_HADAF_PLUS.md", r"""
# بخش مشاوره — دقیقاً ۷ قالب هدفپلاس، بدون صفحهٔ اشتراک

خواسته: «یک بخش مشاوره هم مثل هدفپلاس… ۷ تا قالب دارند اونهارو بردار استفاده کن ولی نمیخواد اون صفحهٔ اشتراک رو بزاری… داخل اپلیکیشنهای مشاوره یه بخش یو آی یو ایکس هم میتونی گیر بیاری که توضیحاتی هست، میتونی رد طراحی یه سری بخشهای جدید ازش استفاده کنی».

## ۱. کشف «۷ قالب» (شواهد)

`Hadaf Plus_2.0.2.apk` → `assets/flutter_assets/assets/images/study_schedule/` دقیقاً ۷ تصویر قالب دارد (بهعلاوهٔ ۲ فایل غیرقالب `no_user_study_schedule.png` و `tile_bg.svg`):

| # | فایل | نام پیشنهادی فارسی | کاربرد |
|---|---|---|---|
| ۱ | `pomodoro.jpg` | پومودورو | ۲۵ دقیقه مطالعه / ۵ دقیقه استراحت، ۴ دور + استراحت بلند |
| ۲ | `school.jpg` | روز مدرسه | برنامهٔ بعدازظهرِ روزهای مدرسه |
| ۳ | `dawn.jpg` | سحرخیزی | مطالعهٔ قبل از مدرسه |
| ۴ | `night.jpg` | شبخوانی | بلوک مطالعهٔ آخر شب |
| ۵ | `after10.jpg` | بعد از ساعت ۱۰ | مطالعهٔ دیرهنگام با محدودیت خواب |
| ۶ | `off.jpg` | روز تعطیل | بلوکهای بلند جمعه/تعطیل |
| ۷ | `period.jpg` | دورهٔ فشرده | هفتهٔ جمع بندی/امتحانات |

تأیید متنی از رشتههای UTF-16LE همان APK: «**برنامۀ هفته رو با یه قالب آماده بچین**»، «**دیدن قالبها**»، «**قالبهای آماده مثل پومودورو و روز مدرسه رو به تقویمت اضافه کن**». سطح اطمینان `INFERRED_STRONG` (تطابق نام فایلها با متن)، نه ادعای اجرای زنده. جزئیات در `CATALOGS/HADAF_TEMPLATES.csv`.

## ۲. آنچه **حذف** میشود (دستور صریح)

از هدفپلاس: `/SubscriptionPlans`, `اشتراک پرو`, `اشتراک سالانه`, `اشتراک ۹ ماهه`, `اشتراک سالن مطالعه`, `سبد خرید`, `تأیید نهایی و پرداخت`, `zarinpal.png`, `images/cart/`, `images/pro/`, «% تخفیف ویژه», «ادامه جهت خرید», «+۱۰ ابزار دیگه» (دروازهٔ پرو). همچنین `طرحهای مشاوره` بهعنوان **فهرست خدمات/قیمت** حذف میشود؛ فقط جریان عملی «درخواست مشاوره ← برنامه ← پیگیری» نگه داشته میشود. **هیچ صفحه، بنر یا CTA پرداختی** به Mimo اضافه نمیشود (F7، بند ضدرگرسیون).

## ۳. فیچرهای مشاورهای که نگه داشته میشوند (همه با ظاهر میمو)

| گروه | شاهد هدفپلاس/همدرس | کامپوننت میمو |
|---|---|---|
| درخواست مشاوره | «دلیل اصلی احساس نیازتون به مشاور چیست؟»، «انتظارات خود از مشاور را بیان کنید»، «اگر مشاور خاصی مد نظرته…»، «رشته هدف»، «تراز کل»، «سهمیه»، «در حال دریافت مشاورین»، `/UserAdvisor/FindAdvisorExamsForUser` | `base_modal_card.xml` + فرم `TextInputLayout` |
| لیست/انتخاب مشاور | `لیست انتخاب مشاورین دلخواه`, `خطا در دریافت مشاورین` | `profile_friend_item.xml` / `leaderboard_item.xml` |
| ارتباط | `/Chat/Admins`, `/Chat/Messages`, `/Chat/Studying`, `تماس مشاور`, «اتاق رسمی هدفپلاس» | همان حبابهای چت AI (بدون restyle) |
| برنامهٔ هفتگی + ۷ قالب | `/Advisor/Plans`, `images/study_schedule/*`, `calendar_goals`, `AddPlanButtonWidget` (همدرس) | گرید ۳تایی `03_EXAM_HUB.md` + `streak_bottom_sheet_content.xml` |
| گزارش | `/Report`, `/Report/ActiveStudySchedule`, `report_model.json`, `report_chart_dto_{7,30,90}day`, `ویرایش اهداف`, `یادداشت روزانه`, `ساعت بیداری`, `مدت موبایل` | `daily_sparks_goal_progress_view.xml` + `chapter_finished_fragment.xml` |
| تحلیل آزمون | `تحلیل آزمون`, `ثبت پاسخها و محاسبهٔ خودکار درصد`, `پاسخبرگ`, `تاریخچۀ آزمون`, «بهترین روش برای تحلیل آزمون چیه؟» | `report_lesson_fragment.xml` + پنل نتیجه |
| ابزارها | `answer_sheet`, `estimator`, `percentage_calculator`, `gpa_calculator`, `time_tracker`, `sleep_time_calc`, `flash_card`, `period`, `pomodoro`, `textbook`, `zistbot` | کارتهای `card_enabled` در هاب Practice |
| رقابت/لیگ | `league_model.json` (knockout/ranking), `get_all_Leagues_dto`, `crown.json`, `daysRemainingToKunkor` | `leaderboard_*` موجود |
| انگیزه | `motivational_phrase.json`: «زندگی گذر همین لحظه هاست. برنامت چیه؟» | `flash_bar_view.xml` |

## ۴. سند UX/UI درون اپ همدرس (منبع طراحی بخشهای تازه)

`همدرس_7.4.4.apk` → `assets/flutter_assets/assets/helpcenter/lessons.json` (تولید `2026-10-10`):

- **۸ بخش**: شروع کار، مطالعه، یادگیری، فلشکارت، رفاقت و رقابت، هوش مصنوعی، پروفایل و حساب، سایر.
- **۳۳ درس**، **۱۴۹ گام**، **۱۰۰ اسکرینشات** با `target: {x,y,w,h}` (ناحیهٔ هایلایت).
- متن کامل و قابلخواندن در `SOURCE_APPS/hamdars/HELP_CENTER_UX.md`؛ خود JSON عیناً در `SOURCE_APPS/hamdars/flutter_assets/assets/helpcenter/lessons.json`.

قواعدی که از آن برای بخشهای تازه وام میگیریم (رفتار، نه کپی متن/تصویر):

1. «**هر جا گیر کردی، علامت سؤال را بزن تا راهنمای همان صفحه باز شود**» → برای هاب آزمون، ۷ قالب، AI و پروفایل، یک `؟` context-help در `toolbar` با باتمشیت گامبهگام میمو اضافه میشود.
2. «همهٔ بخشها از همینجا باز میشوند» → هاب Practice همان نقشهٔ خانهٔ همدرس را با گرههای ۳تایی میمو پیاده میکند.
3. «شعله / امتیاز / الماس» → تعریف شفاف سهگانه در همان `daily_sparks_goal_progress_view`؛ هر فیچر تازه مشخص کند کدامیک را میدهد.
4. «با روشن کردن قابلیت مرور مبحث، همدرس هوشمند مرور رو برنامه ریزی میکنه» → الگوی FSRS/مرور غلطها.
5. «برنامهریزی هوشمند: اهمیت درسها + مدت زمان مورد نظر + برنامهٔ هفتگی مدرسه» → مبنای ۷ قالب.
6. «۲۵ دقیقه مطالعه، ۵ دقیقه استراحت، بعد از چهار دوره استراحت ۱۵…۳۰ دقیقه» → پارامترهای قالب پومودورو.
7. «اگر اپ با کرنومتر روشن بسته شود…» → همان هشدار برای تایمر آزمون.
8. «پنج تا دایره… خودت و حریفت به چند سوال و چطور پاسخ دادین» → الگوی خلاصهٔ رقابت در لیدربورد میمو.

## ۵. محل قرارگیری

کارت «مشاوره» در **تب Practice** کنار کارت «آزمونها» (گره ۳تایی)، و رقابت/لیگ آن در **تب Leaderboard**. پروفایل مشاور/گزارشها در **تب Profile**. هیچ تب پنجمی، هیچ صفحهای با تم تازهای. فرمها و قالبها در `base_modal_card.xml` و باتمشیت `496dp` نشستهاند.

## ۶. پذیرش فاز P5

- [ ] ۷ قالب دقیقاً با همان هفت نام/ترتیب، قابل اعمال روی تقویم هفتگی
- [ ] ۰ صفحه/CTA/بنر اشتراک، پرداخت، سبد خرید، پرو (تست رشتهها + تست بصری)
- [ ] درخواست مشاور، لیست، چت، برنامه، گزارش، تحلیل آزمون، ابزارها همگی با کامپوننتهای میمو
- [ ] `؟` راهنمای context-aware برای هر صفحهٔ تازه، با ساختار گام/هایلایت
- [ ] ۰ کپی از متن/تصویر هدفپلاس و همدرس؛ فقط الگوی رفتاری
""")

# ---------------------------------------------------------------- 06 --------
w("06_PROFILE_AND_GAMIFICATION.md", r"""
# پروفایل با ظاهر خود میمو + گیمیفیکشن سراسری و اجباری

خواسته: «یه صفحه هم پروفایل کاربر هست که اون از ظاهر خود میمو استفاده کن… حتما باید گیمیفیکشن داشته باشه امتیاز تو ازمونها و بقیه قسمتها… دوسن مت و اون بخش مشاوره هم یه جورای از همون یه دیزاین اصلی میمو باید استفاده کنی».

## ۱. پروفایل = کامپوننتهای موجود، نه صفحهٔ تازه

| نیاز | لایوت Mimo موجود |
|---|---|
| قاب پروفایل | `profile_fragment.xml`, `profile_header_view.xml`, `profile_header_unlocked.xml`, `public_profile_activity.xml` |
| کارت اطلاعات | `profile_info_card_view.xml`, `settings_user_settings.xml` (نام/ایمیل/بیو/آواتار) |
| گواهیها/دستاوردها | `profile_certificates_view.xml`, `profile_certificates_item.xml`, `profile_certificates_max_item.xml`, `profile_trophies_item.xml`, `profile_empty_trophies_item.xml` |
| دوستان/دعوت | `profile_friend_item.xml`, `profile_friends_header.xml`, `profile_friends_invite_card.xml`, `profile_friends_empty.xml`, `public_profile_code_header_view.xml` |
| تنظیمات | `settings_fragment.xml`, `set_daily_goal_activity.xml`, `set_daily_goal_card.xml` |
| پیشرفت روزانه | `daily_sparks_goal_progress_view.xml` |

فیلدهای تازهٔ کنکور (پایه، رشتهٔ هدف، تراز کل، رتبه/سهمیه، روزهای باقیمانده تا کنکور — شاهد `motivational_phrase.json`) **در همان `profile_info_card_view`** و با همان ۱۲sp/۱۴sp/۱۶sp و `card_enabled` نمایش داده میشوند. رشتهٔ `daysRemainingToKunkor` بهصورت chip ایستا در هدر (همان جای `streak`).

## ۲. سیستم واحد امتیاز (از سند `19`: «one currency per mode»)

| واحد | منبع | کجا خرج/نمایش داده میشود |
|---|---|---|
| **Sparks / XP** | `daily_sparks_goal_progress_view.xml` (شمارندهٔ ۴۲sp)، `chapter_finished_stats` | هدف روزانه، لیگ، صفحهٔ پایان |
| **Streak (شعله)** | `streak_bottom_sheet_content.xml`, `streak_calendar_height 264dp` | تقویم هفتگی، نجاتدهندهٔ روزها |
| **League / رتبه** | `leaderboard_fragment_active.xml`, `leaderboard_league_header_view.xml`, `leaderboard_podium_item.xml`, ۲۴ لایوت نتیجه | تب Leaderboard، لیگ هفتگی |
| **نشان/جایزه** | `reward_box.xml`, `profile_trophies_item.xml`, `chapter_finished_*` | پروفایل، کمد جوایز |
| **تراز/درصد آزمون** | نتیجهٔ آزمون (جدید) | تحلیل آزمون، پروفایل، رقابت — **عدد جدا، نه پول تازه** |

قاعده: «دوسن مت» (تفسیر: بخش **دوستان/رفاقت و رقابت**) و مشاوره هم **در همین سیستم** تعریف میشوند، نه سیستم موازی؛ دقیقاً همان `leaderboard_*` و `profile_friends_*` میمو.

## ۳. جدول امتیازدهی سراسری (ماشینخوان در `CATALOGS/GAMIFICATION_MAP.csv`)

| رویداد | قاعده | واحد | منبع الهام |
|---|---|---|---|
| پاسخ درست در آزمون | `difficulty(1..5) × subjectFactor` (تخصصی ×۲) | XP | همدرس: «1 point for simple… 5 points for Olympiad», «specialized subjects have twice the points» |
| پاسخ غلط | `−⅓ × difficulty` (نمرهٔ منفی، قابلپیکربندی) | XP/درصد | هدفپلاس: `اثر نمرهٔ منفی` |
| اتمام آزمون زماندار | bonus تکمیل + bonus سرعت هوشمند (بدون تشویق عجله) | XP | خواسته |
| اولین تلاش /Without hint | ضریب ۱٫۲ | XP | `visible-if`/hints میمو |
| مرور غلط → درست دوبار متوالی | XP + حذف از لیست غلطها | XP + FSRS | همدرس «تمرین اشتباههای تمام مباحث» |
| درس/فصل کامل میمو | همان منطق `applyResult` موجود (دستنخورده) | Sparks | HANDOFF |
| هدف روزانه | همان `set_daily_goal_*` | Streak | Mimo |
| فعالسازی یکی از ۷ قالب | XP ثابت + streak تقویم | XP/Streak | هدفپلاس |
| اجرای روزِ برنامهٔ مشاور | XP + گزارش روزانه | XP | `report_model.json` |
| جلسهٔ AI/LearnHarness | XP برای «توضیح تفکر» و «بازبینی گراف» (نه صرفاً چت) | XP | LH thinking fields |
| دوستان/رقابت | امتیاز لیگ همان `leaderboard_*`؛ دعوت دوست = جایزهٔ `reward_box` | League | همدرس `comp-*`, هدفپلاس `league_model` |
| تحلیل آزمون ثبتشده | نشان «تحلیلگر» | نشان | هدفپلاس `تحلیل آزمون` |
| فلشکارت/پومودورو/کرنومتر | همان مدل امتیاز همدرس، به واحد میمو ترجمه شود | XP/Streak | helpcenter `start-points`, `study-time`, `study-pomodoro` |

**ضد تورم**: سقف روزانهٔ XP قابل کسب از بخشهای تازه (cap)، ثبت `xpPolicy` در Blueprint هر آزمون، و تست «هیچ مسیری XP بیکران تولید نمیکند».

## ۴. «دوسن مت» — تفسیر و طراحی

عبارت در پیام شما ابهام دارد؛ در این پلن بهعنوان **بخش دوستان / رفاقت و رقابت** تفسیر شد (شواهد: `comp` همدرس با ۶ درس `comp-start/comp-friends/comp-friendship/comp-messages/comp-prize/comp-history`؛ هدفپلاس `league_model.json` و `images/league/`؛ میمو `leaderboard_*` + `profile_friends_*`). if منظور دیگری بود، فقط `CATALOGS/OPEN_QUESTIONS.csv` و فاز P0 اصلاح میشود. طراحی: همان تب Leaderboard، همان `leaderboard_item.xml`، همان `reward_box`؛ چت دوستان با همان حبابهای میمو؛ رقابت «پنج دایره»ی همدرس بهصورت خلاصهٔ نتیجه در `chapter_finished_fragment.xml`.

## ۵. پذیرش فاز P6

- [ ] پروفایل با ۰ لایوت تازه؛ فقط دادهٔ کنکوری در کارتهای موجود
- [ ] تکتک رویدادهای جدول بالا یک `xpEvent` نسخهدار تولید میکنند و در outbox ثبت میشوند
- [ ] نمایش یکپارچه در `daily_sparks_goal_progress_view`, streak, league, trophies
- [ ] بخش مشاوره و دوستان/رقابت هیچ واحد پول/امتیاز جداگانهای نساختهاند
- [ ] نایت مُد، RTL، `contentDescription` و سقف روزانه تست شده
""")

# ---------------------------------------------------------------- 07 --------
w("07_LESSON_STRUCTURE_AND_QUESTIONS.md", r"""
# ساختار داخلی، چیدمان سؤالات و مرور/حذف غلطها

خواسته: «ساختار داخلیش و نحوهٔ سوالات چیده شدن و مرور غلطها هم میتونی همون میمو رو استفاده کنی یا حتی ارتقا بدی… کلی کار قبلا تو ریپو انجام شده حتما ازش استفاده کن».

## ۱. پایهٔ الزامی (از HANDOFF ریپو، بدون تغییر)

| قرارداد | مسیر | قانون |
|---|---|---|
| DSL درس | `mimo/HANDOFF/docs/dsl.md`, `mimo/learn/dsl.js` | ۲۷ تگ، ۱۲ ویژگی، ساختار بلوکی `<lesson><block>...` |
| `visible-if` | `18_KONKUR_TRANSFER/`, `mimo/learn/grade.js` | سه مقدار `true/false/unknown` — ناشناخته ≠ نادرست |
| نمرهدهی آفست | `mimo/HANDOFF/data/grading_vectors.json` | ۱۲ وکتور، `partial`, `offset`، آرایهٔ پاسخ |
| پیشرفت | `mimo/learn/store.js` | `chapterProgress`, `tutorialProgress`, `trackProgress`, `globalStats` |
| آفلاین | بستهٔ محتوا + `outbox` | محتوا باندل، نتایج در صف |
| وبویو | `mimo-ui/REFERENCE/REA_EVIDENCE/JS_EVIDENCE.json` | `gesture/activity/focus/height`, `MimoLesson.postMessage` |

**اینها دستنخورده میمانند**؛ ارتقا فقط لایهای روی آنهاست (قاعدهٔ وفاداری).

## ۲. ارتقاهای مجاز (همگی از شواهد دو اپ/موتورها)

| ارتقا | دلیل/شاهد | پیادهسازی |
|---|---|---|
| `<equation>`, `<figure>`, `<table>` | سؤالات کنکور فرمول/شکل/جدول دارند | بلوکهای تازهٔ DSL در همان پارسر، با MathJax/`flutter_tex`-معادل بومی و LTR محدود به بلوک |
| `rtlMarker`, Persian normalizer | فارسی، اعراب، نیمفاصله، اعداد فارسی | نرمالساز قبل از مقایسهٔ پاسخ |
| `answerKeyVersion`, `questionVersion` | سند `19`: «answer-key versioning, integrity» | هر تلاش دو نسخه را ذخیره کند؛ تغییر کلید، نتایج قدیمی را باطل نمیکند |
| `error_code` + پاسخ تشریحیِ هر گزینه | همدرس: «اشتباه پاسخ دادی، پاسخ تشریحی رو ببین»، «درجه سختی سؤال» | `grading_vectors` با `explanation` و `difficulty(1..5)` غنی شود |
| نمرهٔ منفی ⅓ و `unanswered` | هدفپلاس: «اثر نمرهٔ منفی», «تعداد سوالات نزده» | لایهٔ `examGrade` جدا از `applySubmission` درس |
| شبیهسازی «اگه غلطها رو نزده میذاشتی، درصدت…» | هدفپلاس | محاسبهٔ سه سناریو در پنل نتیجه |
| پاسخبرگ / پالت سؤال | `answer_sheet.svg`, `اسم پاسخبرگ`, `ثبت پاسخها و محاسبهٔ خودکار درصد` | گرید ۳تایی همان گرهها |
| `تعویض سوال` / `حذف سوال` / «دو گزینهٔ غلط رو حذف کن» | همدرس | اکشنهای `lesson_interactive_*` |
| مرور هوشمند FSRS | EPM `WrongView`, `FSRS`, همدرس «مرور مبحث» / «برنامهریزی هوشمند» | صف `reviewQueue` با فاصلهٔ تکرار؛ غلط بعد از ۲ پاسخ درست متوالی خارج شود |
| بانک سؤال نسخهدار | EPM `docs/question-bank-format.md` (ESQ 1.0 ZIP: `manifest/papers/answers/labels/assets`, `paperKey/unitKey/questionKey`, `contentVersion`) | قالب `konkur-bank-v1` الهامگرفته، با `LICENSE` و هش محتوا |
| ۵…۴۰۰ سؤال، ۴ شکل سؤال از ۷ فلشکارت | هدفپلاس «تعداد سوال باید بین ۵ تا ۴۰۰ باشه»؛ همدرس «در هر دور از یادگیری از 7 فلشکارت به ۴ شکل مختلف سوال پرسیده میشه» | محدودهٔ Blueprint + چرخش قالب سؤال |
| تحلیل بر حسب درس/مبحث | `AnalyisByLessonsScreenWidget` همدرس، `Chart of Test Scores` | همان `report_lesson_fragment.xml` |

## ۳. چیدمان سؤال (ثابت، از میمو)

`lesson_interactive_singlechoice_fragment.xml`, `..._multiplechoice_fragment.xml`, `..._fillthegap_fragment.xml`, `..._validatedinput_fragment.xml`, `..._reveal_fragment.xml`, `interaction_keyboard_with_lesson_feedback.xml`, `lesson_interactive_feedback_bottom_sheet_dialog.xml`. ترتیب: صورت سؤال → گزینهها (۴، `AnswerButtonGrid`) → نوار تعامل → باتمشیت بازخورد. در **حالت آزمون** فقط بازخورد تا پایان به تعویق میافتد؛ چیدمان، فونت، فاصله، ریپل و انیمیشنها عیناً میمانند.

## ۴. جریان غلطها (Wrong-Answer Lifecycle)

```
attempt(wrong) → mistake{questionKey, answerKeyVersion, error_code, topicId, difficulty, ts}
   → reviewQueue (FSRS) → «تمرین اشتباههای تمام مباحث» / «آزمون دوباره»
   → پاسخ تشریحی + راهنما + «دو گزینهٔ غلط رو حذف کن» + «تعویض سوال»
   → correct × 2 متوالی → resolved (از لیست خارج، ولی در history میماند)
   → XP «جبران» + نشان + بهروزرسانی نقشهٔ ضعف/تراز
```

قواعد: حذف غلط **هیچوقت بهمعنای پاککردن تاریخچه نیست** (هدفپلاس: «این پاسخبرگ… برای همیشه پاک میشه» → ما فقط پاککردن پاسخبرگ بهدرخواست کاربر را مجاز میکنیم، نه حذف شواهد یادگیری). ثبت در outbox، قابل همگامسازی آفلاین.

## ۵. ردیابی تصمیمات قبلی ریپو

`19_KONKUR_PRODUCT_TRANSFER_SPEC.md` (۴۲ ردیف ماتریس، سه حالت A LearnHarness / B EPM exam centre / C study-plan card path)، `18_KONKUR_TRANSFER/TRANSFER_MATRIX.md` (۳۲ ردیف، ۸ قرارداد، ۱۲ الگو، ۷ ساخت تازه: timed exam، rank/percentile، weakness map، FSRS، parent/teacher report، authoring panel)، `WHAT_NOT_TO_COPY.md`, `ADAPTATION_PLAN.md` (۳ فاز ۸ هفتهای) — همگی خوانده و در `10_PHASED_ROADMAP.md` ادغام شدند؛ موارد «Mimo has no exam mode → needs timer, scoring policy, question-bank rotation, answer-key versioning, integrity» عیناً به فازهای P1…P3 رفتند.

## ۶. پذیرش فاز P2/P3

- [ ] ۱۲ وکتور نمرهدهی قدیمی همچنان PASS (رگرسیون صفر)
- [ ] DSL تازه با ۲۷ تگ قدیمی سازگار است؛ `unknown` همچنان `unknown` است
- [ ] هر تلاش `answerKeyVersion` دارد؛ تغییر کلید، تاریخچه را خراب نمیکند
- [ ] نمرهٔ منفی، نزده، تشریحی و شبیهسازی سهسناریو تست شده
- [ ] FSRS + حذف بعد از ۲ پاسخ درست + تاریخچهٔ پایدار
- [ ] چیدمان سؤال diff بصری با `lesson_interactive_*` = ۰ تغییر
""")

# ---------------------------------------------------------------- 08 --------
w("08_NAVIGATION_AND_IA.md", r"""
# ناوبری و معماری اطلاعات — همان ۴ تب، مقصدهای تازه

## ۱. ساختار ثابت

```
MainActivity (main_activity_content.xml)
├── contentFrame ......................... میزبان ۴ تب
├── container_bottombar
└── navigation_bar (bottom_navigation_menu.xml: ۴ آیتم)
      ├── Learn ................ مسیر درسی میمو (دستنخورده)
      ├── Practice ............. cv_practice_tab  → [ آزمونها ] [ مشاوره ] [ ابزارها ] [ درسهای موجود ]
      ├── Leaderboard .......... لیگ/دوستان/رقابت (همان leaderboard_*)
      └── Profile .............. پروفایل کنکوری (همان profile_*)
```

- ۶۱ اکتیویتی، ۶ alias، ۴۶ `<data>`، ۱ گراف ناوبری، `SplashActivity_default` alias از استخراج Mimo → گراف موجود **توسعه** مییابد، **جایگزین** نمیشود.
- زنجیرهٔ مودال Mimo حفظ شود: onboarding → daily goal → lesson → feedback → chapter finished → streak → leaderboard result. آزمونها به همین زنجیره وصل میشوند (`chapter_finished_fragment.xml` همان صفحهٔ نتیجه است).

## ۲. مقصدها (درون تب، بدون تب تازه)

| مسیر | تب | الگوی میمو | یادداشت |
|---|---|---|---|
| `exam/hub` | Practice | گرههای درسی | گرید ۳تایی |
| `exam/setup/{type}` | Practice | `base_modal_card` | باتمشیت |
| `exam/run/{examId}` | Practice | `lesson_interactive_*` | فولاسکرین موقت، ناوبری پنهان (الگوی خود میمو در درس) |
| `exam/result/{attemptId}` | Practice | `chapter_finished_fragment` | XP/streak |
| `exam/analysis/{attemptId}` | Practice | `report_lesson_fragment` | چارت/نقشهٔ ضعف |
| `exam/review/{topicId}` | Practice | `WrongView` معادل بومی | FSRS |
| `counseling/hub` | Practice | کارت/گره | ۷ قالب + خدمات |
| `counseling/templates` | Practice | گرید ۳تایی | ۷ قالب |
| `counseling/request` | Practice | مودال فرم | بدون پرداخت |
| `counseling/plans|reports|chat` | Practice/Profile | باتمشیت/کارت | `/Advisor/Plans` معادل |
| `ai/tutor` | همان محل | AI Tutor Compose | ظاهر frozen |
| `max/*` | (پشت AI) | پروکسی | prefix حفظ میشود |
| `leaderboard/*` | Leaderboard | موجود | دوستان/رقابت |
| `profile/*` | Profile | موجود | فیلدهای کنکوری |

## ۳. دیپلینکها

`konkur://exam/{examId}`, `konkur://exam/result/{attemptId}`, `konkur://counseling/template/{id}`, `konkur://max/session/{id}`, `konkur://review/{topicId}` — همگی به `contentFrame` تب مربوطه هدایت میشوند و back stack میمو را رعایت میکنند (بازگشت به هاب، نه خروج از اپ).

## ۴. قواعد رفتاری

- دکمهٔ بازگشت سختافزاری: در `exam/run` → پنل «خروج از آزمون؟»؛ در باتمشیتها → dismiss؛ در هاب → تب قبلی.
- در حالت آزمون، `navigation_bar` مثل حالت درس میمو پنهان میشود تا تمرکز حفظ شود (رفتار موجود، نه اختراع تازه).
- وضعیتها: قفل/`card_disabled` تا زمان بازشدن آزمون ماه؛ `card_outline` برای جاری؛ `accent_success` برای گذرانده.
- آفلاین: تمام مقصدها از بستهٔ محتوا/بانک محلی کار میکنند؛ `/max` و `/practice` در نبود سرور پیام `ai_tutor_offline_description` / معادل میمو نشان میدهند.

## ۵. پذیرش

- [ ] `bottom_navigation_menu.xml` عیناً ۴ آیتم (F0)
- [ ] ۰ `<item>` تازه، ۰ tab تازه در shell (F1)
- [ ] هر مقصد تازه یک دوسیهٔ مرجع از `mimo-ui/SCREENS/` دارد (F3)
- [ ] دیپلینکها + back stack + پنهانسازی ناوبری در آزمون تست شده
""")

# ---------------------------------------------------------------- 09 --------
w("09_DATA_MODEL_AND_BACKEND.md", r"""
# مدل داده، موتورها، پروکسی، آفلاین و RTL

## ۱. موتورهای پینشدهٔ خود ریپو (باز استفاده، نه بازنویسی)

`mimo/engines/pins.json`:

| موتور | ریپو / کامیت | لایسنس | استک | مسیر پروکسی |
|---|---|---|---|---|
| LearnHarness | `amosblomqvist/learnharness` @ `e69e85269c064c6c9c49a8b06ae78c06e79c4a63` | AGPL-3.0-only | Next.js 16 / React 19 | `/max/*` — **پیشوند حفظ میشود**، `basePath: "/max"` |
| EPM | `mo9652962-ai/english-multiple-choice-practice-machine` @ `14c1b276297258e51d05281bdc1dfaf750a2b564` | GPL-3.0-only | FastAPI + Vue 3 / Vite | `/practice/*` — **پیشوند حذف میشود**، `base=/practice/`, `VITE_API_ROOT=/practice/api` |

`mimo/start-preview.sh`: shell پورت ۴۰۰۰، EPM ۸۷۶۵، LearnHarness ۳۰۰۰؛ iframe هممیزبان؛ **دیتاستور جدا** (`LH_DATA_DIR`, `LH_AUTH_FILE`, `EPM_DATA_DIR`). این قراردادها عیناً حفظ میشوند؛ فقط لایهٔ فارسی/RTL و تزریق زمینه اضافه میگردد. لایسنسها در `mimo/ATTRIBUTION.md` / `COMPLIANCE_NOTES.fa.md` رعایت شوند.

## ۲. موجودیتها

| موجودیت | کلیدها | منبع |
|---|---|---|
| `UserProfile` | `userId, grade, field, targetMajor, totalScore, quota, daysToKonkur, locale=fa` | فرم هدفپلاس + `user.json`, `motivational_phrase.json` |
| `ExamBlueprint` | `examId, type, scope[], questionCount, durationSec, negativeMarking, difficultyMix, answerKeyVersion, seed, xpPolicy, retryPolicy, panelSet, version` | سند `19` + این پلن |
| `Question` | `questionKey, paperKey, unitKey, subjectId, topicId, difficulty(1..5), options[4], answerKeyVersion, explanationPerOption, error_code, equation, figure, rtlMarker` | ESQ 1.0 + HANDOFF DSL |
| `Attempt` | `attemptId, examId, startedAt(monotonic), elapsedSec, answers[], unanswered[], wrong[], score, percent, simulatedPercent, rank, percentile, xpEarned, synced` | هدفپلاس `report_model` + میمو `applyResult` |
| `Mistake` | `questionKey, attemptId, error_code, topicId, fsrsDue, consecutiveCorrect, resolvedAt` | EPM `WrongView` + FSRS |
| `CounselingPlan` | `templateId(1..7), weekStart, blocks[], advisorId, goals[], report[]` | ۷ تصویر `study_schedule` + `/Advisor/Plans` |
| `XpEvent` | `eventId, source, amount, capBucket, createdAt, outbox` | سیستم واحد میمو |
| `LhSession` | `sessionId, graphRef, contextInjected (بدون answerKey)` | LH |

## ۳.Room و outbox

جدولهای میمو (`HANDOFF/schema`) دستنخورده میمانند؛ جداول تازه `exam_blueprint`, `question_bank`, `attempt`, `mistake`, `counseling_plan`, `xp_event`, `lh_session_ref` به همان الگوی migration و `outbox` اضافه میشوند. تمام نوشتها ابتدا محلی، سپس همگامساز؛ `synced` flag؛ تضادها با `answerKeyVersion` حل میشوند. حداکثر ۴۰ رویداد تحلیلی (قاعدهٔ سند `19`)، بدون Firebase/RevenueCat، بدون صفحهٔ پرداخت.

## ۴. RTL / بومیسازی

- `fa` از قبل در ARSC میمو وجود دارد (۱۱۶ لوکال)، ولی `lessons-fa` وجود نداشت → بستهٔ محتوای فارسی **جدید** ساخته میشود، با همان ساختار JSON میمو.
- جهت `rtl` سراسری؛ فقط بلوک `<equation>`, کد و اعداد لاتین LTR. نیمفاصله، اعداد فارسی، `ۀ`/`ی` عربی نرمالسازی شوند.
- اعداد در چارتها و تایمر: سیاست واحد (پیشنهاد: اعداد فارسی در متن، لاتین در تایمر/فرمول برای ثبات عرض).
- `contentDescription` برای تمام گرهها/چیپها؛ حداقل کنتراست همان توکنهای میمو؛ `TalkBack` و `TalkBack` focus order راست به چپ.

## ۵. امنیت / تمامیت

- پاسخنامه و `answerKey` هرگز به کلاینت AI/LLM ارسال نمیشود.
- `questionContentHash` (ESQ) + `answerKeyVersion` برای جلوگیری از تغییر silently.
- تایمر مونوتونیک + علامت `integrityFlags` برای تشخیص kill/بازگشت به عقب ساعت.
- هیچ کلید/توکن/مسیر محلی در ریپو (قاعدهٔ «No secrets»).

## ۶. پذیرش

- [ ] `/max/*` و `/practice/*` با پیشوند صحیح پاسخ میدهند؛ دیتاستورها جدا
- [ ] قطع شبکه → تمام مسیرهای یادگیری/آزمون/مرور آفلاین کار میکنند
- [ ] migration قدیمی خراب نمیشود؛ outbox دوبارهایجاد نتیجه نمیدهد
- [ ] ۰ پاسخنامه در prompt؛ ۰ کلید در لاگ/ریپو
- [ ] RTL و نایت مُد در تمام صفحات تازه
""")

# ---------------------------------------------------------------- 10 --------
w("10_PHASED_ROADMAP.md", r"""
# نقشهٔ راه فازبندیشده — «بشه آروم آروم عملیش کرد»

هشت فاز، هرکدام: ورودی → خروجی → دروازهٔ وفاداری → معیار پذیرش → وابستگی. هیچ فازی بدون F0…F9 بسته نمیشود. ماشینخوان در `CATALOGS/PHASES.csv`. ترتیب از `19_KONKUR_PRODUCT_TRANSFER_SPEC.md` و `ADAPTATION_PLAN.md` (A skeleton → B assessment → C advantage) گرفته شده، ولی با **اولویت وفاداری UI** بازچیده شده است.

## P0 — تثبیت مبنا و قرارداد وفاداری

- ورودی: `mimo-ui/` (PASS/۱۸)، `UPGRADE/`، شواهد دو APK، موتورهای پینشده.
- خروجی: `UI_FIDELITY_CONTRACT` امضاشده، `FIDELITY_CHECKS.json` خودکار، اصلاح ۵ تب → ۴تب در پروتوتایپ، تأیید فرضهای `12_RISKS_*`.
- دروازه: **F0, F1, F2, F3** + تأیید ۴ تب.
- پذیرش: `tabCount == 4`، ۰ توکن هاردکد، دوسیهٔ مرجع برای هر صفحهای که قرار است ساخته شود، پاسخ ۵ سؤال باز.
- ⚠️ اگر فرض «دوسن مت» یا «Learn Harness» اشتباه باشد، **فقط همینجا** اصلاح میشود.

## P1 — هاب آزمونها (ظاهر)

- خروجی: کارت ورودی در `cv_practice_tab`، گرید ۳ ستونه RTL، برچسب زیر گره، ۹+ نوع آزمون، ۱۲+ گره، فیلتر چیپها، حالتهای قفل/فعال/انجامشده.
- دروازه: F2/F3/F5/F6/F8 + `03_EXAM_HUB.md` §۷.
- پذیرش: diff بصری با گره درسی میمو، ۰ رنگ/آیکن تازه، RTL، نایت مُد.

## P2 — تایمر، پنلها و موتور سؤال

- خروجی: تایمر مونوتونیک، ۷ پنل باتمشیت، `ExamBlueprint`, بانک سؤال، چیدمان `lesson_interactive_*`، بهتعویقافتادن بازخورد، outbox.
- دروازه: F4/F7 + تست ۱۲ وکتور grading قدیمی (رگرسیون صفر).
- پذیرش: توقف/ادامه/اتمام خودکار، `answerKeyVersion`، ۰ تغییر در چیدمان سؤال.

## P3 — نتیجه، تحلیل، مرور غلطها، گیمیفیکشن آزمون

- خروجی: `chapter_finished_fragment` برای نتیجه، درصد/نمرهٔ منفی/شبیهسازی سهسناریو، تراز/رتبه، نقشهٔ ضعف، FSRS، `تمرین اشتباهها`, `آزمون دوباره`, XP/Streak/League.
- دروازه: F9 + `GAMIFICATION_MAP` + سقف روزانه.
- پذیرش: ۰ رگرسیون در `applyResult`؛ غلطها بعد از ۲ پاسخ درست حذف شوند ولی تاریخچه بماند.

## P4 — AI میمو + Learn Harness

- خروجی: پروکسی `/max/*`, `basePath`, جداسازی دیتاستور، ردیف ۱۶ اکشن LH، تزریق زمینه بدون پاسخنامه، حالت آفلاین با رشتههای میمو.
- دروازه: **diff رشتههای `ai_tutor_*` = ۰**، ۰ عنصر حذفشده، `04_AI_LEARN_HARNESS.md` §۶.
- پذیرش: تمام اکشنها قابلرویت؛ تب جدید وجود ندارد؛ تست عدم نشت answerKey.

## P5 — مشاوره و ۷ قالب هدفپلاس

- خروجی: ۷ قالب، درخواست مشاور/لیست/چت، برنامهٔ هفتگی، گزارش ۷/۳۰/۹۰روزه، تحلیل آزمون، ابزارها، `؟` راهنما (الگوی helpcenter همدرس).
- دروازه: ۰ صفحه/CTA اشتراک/پرداخت/پرو؛ F2/F3/F7؛ `05_COUNSELING_HADAF_PLUS.md` §۶.
- پذیرش: تست رشتهها برای نبود `اشتراک|پرداخت|سبد خرید|پرو`؛ ۰ کپی asset.

## P6 — پروفایل و یکپارچگی گیمیفیکشن

- خروجی: فیلدهای کنکوری در `profile_*` موجود، `XpEvent` برای تکتک بخشها، نمایش یکپارچه Sparks/Streak/League/نشانها، «دوسن مت» = دوستان/رقابت در تب Leaderboard.
- دروازه: F0/F2/F3 + `06_PROFILE_AND_GAMIFICATION.md` §۵.
- پذیرش: هر بخش تازه دقیقاً یک واحد امتیاز دارد؛ ضد تورم؛ نایت مُد.

## P7 — RTL، دسترسپذیری، راهنما، پولیش و تحویل

- خروجی: بستهٔ محتوای `fa`, نرمالساز فارسی، `contentDescription` کامل، راهنمای context-aware برای همهٔ صفحات تازه، تست `sw600dp`, تست آفلاین سراسری، بهروزرسانی `ATLAS` با دوسیههای تازه، `VERIFICATION_REPORT` دور جدید، ZIP و آپلود Drive.
- دروازه: **همهٔ F0…F9** + ۱۸ چک دور قبل + چکهای تازه.
- پذیرش: `PASS`، ۰ `NOT_TESTED` بحرانی، مستندات فارسی کامل.

## اصل جریان کار

1. هر فاز یک briefing از `CATALOGS/FEATURE_MAP.csv` میگیرد.
2. قبل از کد، دوسیهٔ مرجع Mimo باز و F2/F3 پر میشود.
3. بعد از کد، `craft_adapter.py core-plan-update --phase Pn --status DONE` + ثبت شواهد جدید.
4. `FIDELITY_CHECKS.json` بهروز میشود؛ شکست = توقف فاز بعدی.
5. موتورها (LH/EPM) هرگز rewrite نمیشوند؛ فقط پروکسی و لایهٔ زبان.

## زمانبندی پیشنهادی (غیرالزامی)

الگوی `ADAPTATION_PLAN.md` (۳ × ۸ هفته) حفظ شود، ولی P0+P1 در همان ۸ هفتهٔٔ اول (skeleton)، P2+P3+P4 در دوم (assessment)، P5+P6+P7 در سوم (advantage). ترتیب داخل فازها قابل جابهجایی نیست، چون وفاداری P0 پیشنیاز همه است.
""")

# ---------------------------------------------------------------- 11 --------
w("11_EVIDENCE_AND_CROSSWALK.md", r"""
# شواهد و ماتریس یادگیری — هر ادعا از کجا آمده

## ۱. هویت منابع (هش SHA-256)

| منبع | اندازه | SHA-256 | محل |
|---|---|---|---|
| `Mimo_9.35 (1).apk` | ۱۴۲٬۳۵۳٬۴۹۹ B | `48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a` | استخراج دور قبل `mimo-ui/` |
| `همدرس_7.4.4.apk` | ۵۳٬۲۷۷٬۶۶۹ B | `9e362f08670174a3e8a3b319b5a2f687da8ecf7896ea78ea2ec70b95dd817be3` | `google_drive/` (gitignored) |
| `Hadaf Plus_2.0.2.apk` | ۵۹٬۴۰۳٬۴۷۷ B | `b282f578b255fecc4b72ee74f2ce79eb5bbcde35f3515690342b7fa37a5bbf43` | `google_drive/` (gitignored) |

پوشهٔ Drive `mimo`: `1yU1PN1GhTZlDeu91H4FSS0JsOT5MjpxB`. شناسهها: همدرس `17jsS0kYMX9rKlISyro6yhW8OdvoGKQ0g`، هدفپلاس `1KGGe61bQqr8B1lCsxim7LDS8CCBsN2KG`.

## ۲. آمار استخراج دو APK (همه در `SOURCE_APPS/`)

| شاخص | همدرس ۷٫۴٫۴ | هدفپلاس ۲٫۰٫۲ |
|---|---|---|
| package | `org.taraz.app` | `app.hadafplus.hadaf_plus` |
| اعضای ZIP | ۱٬۳۶۳ | ۱٬۵۱۶ |
| DEX / `.so` | ۲ / ۳ | ۲ / ۹ |
| `res/` | ۶۱۹ (۴۰۸ AXML دیکدشده، ۱ خطا) | ۸۵۶ (۶۲۳ AXML، ۰ خطا) |
| `flutter_assets` | ۶۲۵ (۴۰۹ متنی کپیشده) | ۵۲۶ (۳۳۹ متنی کپیشده) |
| `lib/arm64-v8a/libapp.so` | ۲۰٬۸۴۱٬۳۹۲ B | ۱۵٬۷۲۹٬۵۸۴ B |
| رشتههای استخراجی | ۴۹٬۱۶۲ | ۲۳٬۹۲۱ |
| کلاسهای UI نامدار | ۱٬۲۳۴ | ۷۶ |
| endpoint / route | ۴۹ / ۴۴ | ۳۲۰ / ۲۷۰ |
| رشتههای فارسی UTF-16LE | ۱٬۱۱۶ | ۲٬۱۲۲ |
| سند کمک UX | ۸ بخش / ۳۳ درس / ۱۴۹ گام / ۱۰۰ شات | — |
| مدلهای API | `cup.json`, `lessons.json` | ۳۱ JSON: `models/*`, `response_dto/*` |

## ۳. ماتریس «چه چیزی از کجا یاد گرفتیم»

| یادگرفته | منبع | سطح | کجا استفاده شد |
|---|---|---|---|
| ۴ تب واقعی میمو | `mimo-ui/SOURCE/res/menu/bottom_navigation_menu.xml` + `navigation_*` strings | `VERIFIED_STATIC` | `02`, `08`, `10` |
| `cv_practice_tab` ComposeView + toolbar include | `practice_tab_fragment.xml` | `VERIFIED_STATIC` | `03`, `08` |
| `btn_ai_tutor` / `iv_ai_tutor_pulse` + ۲۸ رشته | `coding_keyboard_layout.xml`, `values/string.xml` | `VERIFIED_STATIC` | `04` |
| توکنها/ابعاد/انیمیشنها | `DESIGN_TOKENS.json`, `ATLAS/tokens.css` | `VERIFIED_STATIC` | `02`, `wireframes.html` |
| ۷ قالب مطالعاتی | `study_schedule/{after10,dawn,night,off,period,pomodoro,school}.jpg` + متن «دیدن قالبها» | `INFERRED_STRONG` | `05` |
| صفحهٔ اشتراک/پرداخت (برای حذف) | رشتههای `اشتراک پرو`, `/SubscriptionPlans`, `images/cart`, `zarinpal.png` | `VERIFIED_STATIC` | `05` |
| سند UX/UI درون اپ | `assets/helpcenter/lessons.json` همدرس | `VERIFIED_STATIC` | `05`, `03`, `06` |
| انواع آزمون همدرس | `آزمون تستی/تشریحی/دوباره/نهایی`, `AddQuestionView`, `AddResultExamTypeWidget`, `/add_question`, `/report_question` | `VERIFIED_STATIC` | `03`, `CATALOGS/EXAM_TYPES.csv` |
| امتیازدهی ۱…۵ و ضریب تخصصی ×۲ | رشتههای ASCII همدرس | `VERIFIED_STATIC` | `06` |
| مرور/حذف غلطها | `تمرین اشتباههای تمام مباحث`, `پاسخ تشریحی`, `تعویض سوال`, `تعداد غلط` | `VERIFIED_STATIC` | `03`, `07` |
| تحلیل آزمون/پاسخبرگ/نمرهٔ منفی | رشتههای هدفپلاس + `report_*_model.json` | `VERIFIED_STATIC` | `03`, `07` |
| endpointها و مدلها | `/PersonalExam/Create`, `/Report/*`, `/Chatbot/messages/stream`, `/Advisor/Plans`, `league_model.json` | `VERIFIED_STATIC` | `05`, `09` |
| AI چت مشاورهای | `AiChatInputBar`, ۲۶ `ai_chat/*`, `chatbot.json` | `VERIFIED_STATIC` | `04` |
| LearnHarness / EPM pins | `mimo/engines/pins.json`, `bootstrap_engines.sh`, `start-preview.sh` | `VERIFIED_STATIC` | `04`, `09` |
| اکشنهای LH | کلون `components/*.tsx` (start session, sessions, graph, plan, practice, confidence…) | `VERIFIED_STATIC` | `04`, `LEARNHARNESS_ACTIONS.csv` |
| ESQ 1.0 / FSRS / WrongView | `epm/docs/question-bank-format.md`, `frontend/src/views/WrongView.vue` | `VERIFIED_STATIC` | `07`, `09` |
| ماتریس انتقال ۴۲ ردیفی / ۳۲ ردیفی | `19_KONKUR_PRODUCT_TRANSFER_SPEC.md`, `18_KONKUR_TRANSFER/*` | `VERIFIED_STATIC` | `10` |
| رگرسیون ۵ تبه | `/home/user/_work/prev/mimo/shell/app.js` | `VERIFIED_STATIC` | `02`, `10` |
| `craft-anything` v0.3.0 | `/home/user/_work/craft-anything`, `docs/tools.md`, ۴ schema | `VERIFIED_STATIC` | `01` |
| JS/WebView evidence میمو | `mimo-ui/REFERENCE/REA_EVIDENCE/JS_EVIDENCE.json` (REA `rea-agents@6.8.0`) | `VERIFIED_STATIC` + ۸ محدودیت | `07` |

## ۴. سطوح اطمینان (قرارداد craft-anything / REA)

- `VERIFIED_STATIC`: مستقیم از بایتهای APK/فایل ریپو، هششده، قابلتکرار.
- `INFERRED_STRONG`: تطابق چند شاهد مستقل (مثلاً نام ۷ فایل + متن «قالبها») بدون اجرای زنده.
- `INFERRED_WEAK`: حدس از نام کلاس/پوشه — در تصمیمات معماری استفاده نشده، فقط در `OPEN_QUESTIONS`.
- `NOT_TESTED`: رفتار زمان اجرا، اسکرینشات، لمس، عملکرد، شبکه — **هیچ ادعایی در این پلن دربارهٔ آنها نشده است**.
- `UNKNOWN`: محتوای `@BankBookkonkor (26)_extract.pdf` (PDF تصویری بدون لایهٔ متن؛ نیاز به OCR)، معنی دقیق «دوسن مت»، نسخهٔ دقیق LH موردنظر.

## ۵. محدودیتهای روش

- ابزارهای Java/JADX/apktool/aapt2/adb/emulator موجود نیستند → **هیچ decompile DEX/Dart AOT و هیچ اجرای زندهای** انجام نشد؛ `libapp.so` فقط string-mine شد (ASCII + UTF-16LE). نام کلاسها/رشتهها شاهدند، نه کد اجراشده.
- Mimo APK نسخهٔ مودشده (`CN=youarefinished`, Smob obfuscation) است؛ توکنها و لایوتها همچنان معتبرند، ولی رفتار باینری رسمی تضمین نمیشود.
- ۱۸ JS خارج از دامنه و `spieglein/index.html` در evidence REA محدودیت ثبتشده دارند.
- اسکرینشاتهای `helpcenter/shots` (۱۰۰ عدد) بهصورت باینری هش و فهرست شدند، ولی OCR/تفسیر تصویری انجام نشد؛ متن `lessons.json` جایگزین معتبر آنهاست.
""")

# ---------------------------------------------------------------- 12 --------
w("12_RISKS_UNKNOWN_AND_QUESTIONS.md", r"""
# ریسکها، ناشناختهها و سؤالهای غیرمسدودکننده

طبق «سوال داری میتونی بپرسی اگر نه شروع کن»: سؤالی که **مانع شروع** باشد وجود نداشت، کار شروع شد. موارد زیر در **فاز P0** قابل اصلاحاند و در `CRAFT_ANYTHING/workspace/unknowns.json` (U01…U05) و `CATALOGS/OPEN_QUESTIONS.csv` ثبت شدهاند.

| id | مورد | تفسیر/اقدام فعلی | سؤال از شما (فقط اگر خواستید) |
|---|---|---|---|
| U01 | «دوسن مت» | بخش **دوستان / رفاقت و رقابت** (شواهد: `comp-*` همدرس، `league_*` هدفپلاس، `leaderboard_*` و `profile_friends_*` میمو) | منظورتان همین بخش اجتماعی/رقابتی است یا چیز دیگری (مثلاً «متن/داکیومنت»؟) |
| U02 | `@BankBookkonkor (26)_extract.pdf` | ۲۲٬۸۱۲٬۲۰۳ B، **بدون لایهٔ متن**؛ خواندن مجدد ممنوع/بینتیجه؛ نیاز به OCR برای استخراج ساختار سؤالات واقعی کنکور | آیا OCR/نسخهٔ متنیاش را تهیه کنید؟ |
| U03 | اجرای زنده | هیچ runtime/screenshot/emulator/JADX در دسترس نیست؛ وفاداری فقط استاتیک سنجیده شد | آیا دستگاه/اسکرینشات مرجع Mimo فراهم میشود تا F9 دقیق شود؟ |
| U04 | Learn Harness | فرض = ریپوی پینشدهٔ `amosblomqvist/learnharness` @ `e69e8526…` با `basePath=/max` | آیا نسخه/فورک دیگری مدنظر است؟ |
| U05 | حذف پیامهای «پرو» | صفحهٔ اشتراک وهر CTA پرداختی حذف شد | آیا تکمتنهای «پرو» در صفحات دیگر هم باید پاک شوند؟ |

## ریسکها

| ریسک | شدت | کاهش |
|---|---|---|
| انحراف دوباره به ۵ تب / زبان بصری تازه | **بحرانی** (همان مشکل اصلی شما) | F0…F9 در هر فاز؛ `02` امضاشده؛ P0 قبل از هر کد |
| AI ظاهرش عوض شود یا دکمهای حذف شود | بالا | diff رشتههای `ai_tutor_*` = ۰؛ لیست ۱۶ اکشن LH؛ «چیزی حذف نشود» |
| صفحهٔ اشتراک ناخواسته اضافه شود | بالا | تست رشتهها `اشتراک|پرداخت|سبد خرید|پرو`؛ `05` §۲ |
| تورم XP / چند واحد پول موازی | متوسط | `one currency per mode` + cap روزانه + `GAMIFICATION_MAP` |
| بیاعتباری نتایج بعد از تغییر پاسخنامه | متوسط | `answerKeyVersion` + `questionContentHash` + outbox |
| تقلب/خرابی تایمر (kill اپ، تغییر ساعت) | متوسط | `elapsedRealtime` مونوتونیک + `integrityFlags` + ذخیرهٔ هر ۵ ثانیه |
| نشت پاسخنامه به LLM | بالا | قرارداد تزریق زمینه + تست خودکار (`04` §۳) |
| لایسنس AGPL/GPL موتورها | حقوقی | حفظ Attribution/لایسنس، عدم ادغام کد، عدم حذف نوتیسها؛ `mimo/COMPLIANCE_NOTES.fa.md` |
| فارسی/RTL و فرمولهای LTR | متوسط | `rtlMarker`، نرمالساز، بلوکهای جدا، تست `fa` |
| حجم/عملکرد بانک سؤال آفلاین | متوسط | ESQ ZIP + هش + بارگذاری تدریجی، `content_max_width` رعایت شود |
| تفسیر نادرست ۷ قالب | پایین | `INFERRED_STRONG` اعلام شد؛ در P5 قابلتأیید با OCR تصاویر |

## موارد `NOT_TESTED` صریح

هیچکدام از اینها انجام/ادعا نشدهاند: اجرای دو APK روی دستگاه، اسکرینشات واقعی، decompile Dart AOT/DEX، شبکه/API زنده، پرداخت، OCR تصاویر، تست عملکرد/باتری، A/B، نظر کاربر نهایی، نصب باینری native craft-anything.

## چگونه پلن را بهروز کنیم

1. پاسخ خود را بدهید → `CATALOGS/OPEN_QUESTIONS.csv` و U01…U05 بهروز میشود.
2. `python3 UPGRADE/CRAFT_ANYTHING/craft_adapter.py core-unknown-add --text ...` / `core-plan-update --phase P0 --status CONFIRMED`.
3. `python3 UPGRADE/tools/write_upgrade_plan.py UPGRADE` دوباره اجرا میشود؛ تمام اسناد/CSVها بازتولید میگردند.
""")

# ---------------------------------------------------------------- README ----
w("README.md", r"""
# `mimo-ui/UPGRADE/` — پلن ارتقای Mimo → اپ یادگیری کنکور (Plan-Only)

دور کاری `arena/aebb90b7-game` بعد از تحویل `mimo-ui/` (استخراج ۰تا۱۰۰ UI میمو).

- ورود: `00_START_HERE.md`
- قانون اساسی: `02_UI_FIDELITY_CONTRACT.md`
- نمایش بصری: `wireframes.html`
- پلن ماشینخوان: `CATALOGS/*.csv`
- شواهد خام دو اپ مشاورهای: `SOURCE_APPS/{hamdars,hadaf_plus}/`
- لایهٔ نصبشدهٔ craft-anything: `CRAFT_ANYTHING/`
- ابزارهای قابلتکرار: `tools/extract_source_apps.py`, `tools/write_upgrade_plan.py`, `CRAFT_ANYTHING/craft_adapter.py`

**وضعیت:** فقط پلن و شواهد؛ هشت فاز `PLANNED`، هیچ پیادهمسازی محصول انجام نشده است.
""")

# ---------------------------------------------------------------- CSVs ----
wcsv("UI_FIDELITY_RULES.csv", ["id", "rule", "check", "source"],
     [["F0", "ناوبری دقیقاً ۴ تب", "bottom_navigation_menu.xml == 4 items", "mimo-ui/SOURCE/res/menu/bottom_navigation_menu.xml"],
      ["F1", "هیچ تب تازهای (Max/Exam/Counseling)", "shell tabCount == 4", "02_UI_FIDELITY_CONTRACT.md"],
      ["F2", "هر رنگ/فاصله/شعاع/فونت از توکنهای موجود", "0 هاردکد تازه", "mimo-ui/CATALOGS/DESIGN_TOKENS.json"],
      ["F3", "هر صفحهٔ تازه یک دوسیهٔ مرجع دارد", "SCREENS/LAYOUTS ref ثبت شود", "mimo-ui/SCREENS, mimo-ui/LAYOUTS"],
      ["F4", "رفتار باتمشیت/مودال/بازگشت میمو", "back & dismiss تست شود", "mimo-ui/CATALOGS/LAYOUT_XREFS.csv"],
      ["F5", "حالتهای کارت و نایت مُد", "card_enabled/pressed/disabled/outline", "DESIGN_TOKENS.json"],
      ["F6", "RTL سراسری، LTR فقط کد/فرمول", "layoutDirection + numeral policy", "fa locale در ARSC"],
      ["F7", "clean-room: ۰ کپی asset/کد/متن", "diff asset & string", "craft-anything AGENTS.md"],
      ["F8", "include/xref با کاتالوگ مقایسه شود", "LAYOUT_XREFS match", "mimo-ui/CATALOGS/LAYOUT_XREFS.csv"],
      ["F9", "diff بصری با دوسیهٔ مرجع >= 90%", "ATLAS diff + نگاه انسانی", "mimo-ui/ATLAS/index.html"]])

wcsv("FEATURE_MAP.csv", ["feature", "host_tab", "mimo_mechanism", "source_app_evidence", "phase", "fidelity_gates"],
     [["Exam hub grid (3-col nodes)", "Practice", "cv_practice_tab + lesson nodes + card states", "Hamdars helpcenter start-home; Hadaf study_schedule", "P1", "F2,F3,F5,F6,F8"],
      ["9+ exam types", "Practice", "base_modal_card + blueprint", "Hamdars exam types; Hadaf SampleExam/PersonalExam", "P1", "F2,F3"],
      ["Monotonic timer", "Practice", "ChapterToolbar + lesson_progressbar_height", "Hamdars study-time; Hadaf timer warnings", "P2", "F4"],
      ["7 bottom-sheet panels", "Practice", "base_modal_card, flash_bar_view, bottom_sheet_*", "Hadaf answer_sheet / report; Hamdars add_question", "P2", "F4,F5"],
      ["Question layout", "Practice", "lesson_interactive_* unchanged", "Mimo HANDOFF DSL", "P2", "F2,F3,F9"],
      ["Results & analysis", "Practice", "chapter_finished_fragment, report_lesson_fragment", "Hadaf تحلیل آزمون; Hamdars AnalyisByLessons", "P3", "F3,F9"],
      ["Mistake review / FSRS", "Practice", "WrongView equivalent + reward_box", "Hamdars تمرین اشتباهها; EPM FSRS", "P3", "F7"],
      ["AI Tutor (frozen look)", "existing AI entry", "btn_ai_tutor, iv_ai_tutor_pulse, ai_tutor_* strings", "Hamdars AiChatInputBar; Hadaf /Chatbot", "P4", "F2,F3,F7"],
      ["Learn Harness action dock", "AI bottom sheet", "flash_bar_view chips", "LearnHarness components/*.tsx", "P4", "F2,F6"],
      ["Counseling 7 templates", "Practice", "3-col grid + base_modal_card", "Hadaf study_schedule/*.jpg", "P5", "F2,F3,F7"],
      ["Counseling request/chat/report", "Practice/Profile", "modals, cards, charts", "Hadaf /Advisor/Plans, /Report, /Chat", "P5", "F3,F4"],
      ["No subscription page", "all", "removed entirely", "Hadaf /SubscriptionPlans, اشتراک پرو", "P5", "F7"],
      ["Konkur profile fields", "Profile", "profile_info_card_view, profile_header_view", "Hadaf user.json, motivational_phrase", "P6", "F2,F3"],
      ["Unified gamification", "all", "Sparks/Streak/League/Trophies", "Hamdars 1..5 points; Hadaf league_model", "P3,P6", "F2"],
      ["Friends / competition", "Leaderboard", "leaderboard_*, profile_friends_*", "Hamdars comp-*; Hadaf league_*", "P6", "F3"],
      ["Context help per screen", "all", "? in toolbar + step sheet", "Hamdars helpcenter/lessons.json", "P7", "F4"]])

wcsv("EXAM_TYPES.csv", ["exam_type_fa", "slug", "scope", "question_count", "duration", "negative_marking", "xp_policy", "panels", "evidence"],
     [["آزمون جامع کنکور", "comprehensive", "همه دروس", "200-400", "270 دقیقه", "⅓", "difficulty×subjectFactor", "setup,palette,result,analysis", "خواسته + هدفپلاس آزمون ماز/گاج"],
      ["آزمون تکدرسی", "single_subject", "یک درس", "20-60", "45-90 دقیقه", "⅓", "difficulty×2", "setup,palette,result,analysis", "خواسته + SampleExam/FindAllByLevelAndField"],
      ["آزمون تا مبحث", "topic", "یک مبحث", "10-30", "15-30 دقیقه", "⅓", "difficulty×2", "setup,palette,review", "خواسته + lesson_model.json"],
      ["آزمون درسی / فصلی", "lesson", "یک فصل", "20-40", "30-60 دقیقه", "⅓", "difficulty", "setup,palette,result", "خواسته + آزمون نهایی همدرس"],
      ["آزمون این ماه", "this_month", "تقویم ماه", "متغیر", "متغیر", "⅓", "difficulty + monthly bonus", "setup,palette,result,analysis", "خواسته + آزمون تازه هدفپلاس"],
      ["آزمون زماندار", "timed", "دلخواه", "5-400", "تایمر کاربر", "اختیاری", "completion + speed bonus", "setup,timer,palette,result", "خواسته + تعداد سوال باید بین ۵ تا ۴۰۰ باشه"],
      ["آزمون تشریحی", "descriptive", "یک درس/مبحث", "5-20", "—", "—", "manual grading", "setup,result", "آزمون تشریحی همدرس"],
      ["آزمون دوباره / مرور غلطها", "retry_mistakes", "غلطهای ذخیرهشده", "همه غلطها", "—", "—", "recovery XP + FSRS", "review,result", "تمرین اشتباههای تمام مباحث / WrongView"],
      ["آزمون شخصیساخته", "personal", "انتخاب کاربر", "5-400", "دلخواه", "دلخواه", "difficulty", "setup,palette,result", "/PersonalExam/Create هدفپلاس"],
      ["آزمون نهایی/پایانی", "final", "پایان مسیر", "40-80", "90 دقیقه", "⅓", "badge + XP", "setup,palette,result", "آزمون نهایی همدرس"],
      ["آزمون تستی سریع", "quick_quiz", "مبحث جاری", "5-10", "5-10 دقیقه", "⅓", "first-try bonus", "palette,result", "آزمون تستی همدرس"]])

wcsv("HADAF_TEMPLATES.csv", ["n", "asset", "persian_name", "pattern", "mimo_component", "gamification"],
     [[1, "pomodoro.jpg", "پومودورو", "25 دقیقه مطالعه / 5 دقیقه استراحت ×4 + استراحت 15-30", "streak_bottom_sheet_content + 3-col grid", "XP + Streak"],
      [2, "school.jpg", "روز مدرسه", "بلوک بعدازظهر روزهای مدرسه", "card_enabled +Daily goal", "XP + Streak"],
      [3, "dawn.jpg", "سحرخیزی", "مطالعهٔ قبل از مدرسه", "card_enabled + timer chip", "XP + Streak"],
      [4, "night.jpg", "شبخوانی", "بلوک آخر شب", "card_enabled + timer chip", "XP + Streak"],
      [5, "after10.jpg", "بعد از ساعت ۱۰", "مطالعهٔ دیرهنگام با هشدار خواب", "flash_bar_view warning", "XP + Streak"],
      [6, "off.jpg", "روز تعطیل", "بلوکهای بلند تعطیل", "card_enabled + progress", "XP + Streak"],
      [7, "period.jpg", "دورهٔ فشرده", "هفتهٔ جمع بندی/امتحانات", "card_outline + progress_chapter_primary", "XP + Streak + Badge"]])

wcsv("GAMIFICATION_MAP.csv", ["event", "rule", "unit", "cap", "evidence", "phase"],
     [["exam correct", "difficulty(1..5) × subjectFactor (specialized ×2)", "XP", "daily cap", "Hamdars 1..5 points", "P3"],
      ["exam wrong", "−⅓ × difficulty", "XP/percent", "daily cap", "Hadaf اثر نمرهٔ منفی", "P3"],
      ["timed completion", "completion + smart speed bonus", "XP", "per exam", "خواسته", "P3"],
      ["first try / no hint", "×1.2", "XP", "per question", "Mimo visible-if hints", "P3"],
      ["mistake resolved", "2 consecutive correct → XP + FSRS release", "XP + FSRS", "per mistake", "Hamdars تمرین اشتباهها", "P3"],
      ["lesson/chapter complete", "applyResult unchanged", "Sparks", "existing", "HANDOFF", "P1"],
      ["daily goal", "set_daily_goal_* unchanged", "Streak", "existing", "Mimo", "P1"],
      ["activate template", "fixed XP + calendar streak", "XP + Streak", "per week", "Hadaf قالبهای آماده", "P5"],
      ["execute plan day", "XP + daily report", "XP", "daily cap", "Hadaf report_model", "P5"],
      ["LH session (thinking/graph)", "XP for reasoning, not chatting", "XP", "daily cap", "LearnHarness thinking fields", "P4"],
      ["friends/competition", "leaderboard_* league score", "League", "weekly", "Hamdars comp-*, Hadaf league_model", "P6"],
      ["analysis recorded", "تحلیلگر badge", "Badge", "per exam", "Hadaf تحلیل آزمون", "P6"],
      ["flashcard/pomodoro/stopwatch", "mapped to Mimo units", "XP + Streak", "daily cap", "Hamdars helpcenter", "P6"]])

wcsv("PHASES.csv", ["phase", "title", "inputs", "outputs", "fidelity_gates", "acceptance", "depends", "status"],
     [["P0", "تثبیت مبنا و قرارداد وفاداری", "mimo-ui/, UPGRADE/, engines pins", "FIDELITY_CHECKS.json, 4-tab fix, فرضها", "F0,F1,F2,F3", "tabCount==4, 0 hardcode, 5 سؤال پاسخ", "-", "PLANNED"],
      ["P1", "هاب آزمونها (ظاهر)", "P0", "گرید ۳تایی، ۹+ نوع، ۱۲+ گره", "F2,F3,F5,F6,F8", "diff بصری با گره درسی", "P0", "PLANNED"],
      ["P2", "تایمر، پنلها، موتور سؤال", "P1", "تایمر مونوتونیک، ۷ پنل، Blueprint، outbox", "F4,F7", "12 grading vectors PASS", "P1", "PLANNED"],
      ["P3", "نتیجه، تحلیل، مرور غلطها، XP آزمون", "P2", "درصد/تراز/نقشه ضعف/FSRS/XP", "F9", "0 regression, mistake lifecycle", "P2", "PLANNED"],
      ["P4", "AI میمو + Learn Harness", "P0", "/max proxy, 16 action dock, context injection", "ai_tutor diff=0, F2", "0 hidden action, 0 answerKey leak", "P0", "PLANNED"],
      ["P5", "مشاوره و ۷ قالب", "P0,P1", "۷ قالب، درخواست مشاور، گزارش، راهنما", "F2,F3,F7", "0 subscription/payment string", "P0,P1", "PLANNED"],
      ["P6", "پروفایل و گیمیفیکشن یکپارچه", "P3,P4,P5", "XpEvent سراسری، پروفایل کنکوری، دوستان", "F0,F2,F3", "one currency per mode", "P3,P4,P5", "PLANNED"],
      ["P7", "RTL، a11y، راهنما، پولیش", "همه", "fa pack, a11y, ATLAS update, ZIP/Drive", "F0..F9", "PASS, 0 critical NOT_TESTED", "P6", "PLANNED"]])

wcsv("LEARNHARNESS_ACTIONS.csv", ["lh_action", "component", "persian_label", "placement", "mimo_token"],
     [["Start session", "new-session.tsx / aria-label", "جلسهٔ تازه", "action dock", "card_pressed + button_primary"],
      ["Sessions", "top-bar.tsx / session-navigation", "جلسهها", "action dock", "card_pressed"],
      ["Plan window / Targets", "plan-window.tsx", "نقشهٔ یادگیری", "action dock", "card_outline"],
      ["Knowledge graph / Search nodes", "graph-view.tsx", "گراف دانش", "action dock", "card_pressed"],
      ["Practice / Next problem / Retest", "practice-cards.tsx", "تمرین / سؤال بعد", "action dock", "card_pressed"],
      ["Check your understanding", "question-dock.tsx", "بفهمم یا نه", "action dock", "card_pressed"],
      ["Confidence rail", "confidence-rail.tsx", "میزان اطمینان", "action dock", "progress_chapter_primary"],
      ["Thinking fields / Think out loud", "thinking-block.tsx", "فکر کردن با صدای بلند", "action dock", "card_pressed"],
      ["Hint rung", "practice-cards.tsx", "راهنما", "action dock", "card_pressed"],
      ["Notes import", "notes-import.tsx", "یادداشتهام", "action dock", "card_pressed"],
      ["Researcher", "composer-actions.tsx", "پژوهش", "action dock", "card_pressed"],
      ["Figure maker", "composer-actions.tsx", "شکلسازی", "action dock", "card_pressed"],
      ["PDF reader / Demo builder", "composer-actions.tsx", "PDF / نمونه", "action dock", "card_pressed"],
      ["Model / Context / Cost / Steps / Settings", "top-bar.tsx, stats-bar.tsx", "مدل / هزینه / تنظیمات", "status chips", "text_primary"],
      ["Dictation", "dictation.tsx", "گفتار", "action dock", "card_pressed"],
      ["Stop / Abort / End background process", "abort-turn-dialog.tsx", "توقف", "action dock", "error_default"]])

wcsv("EVIDENCE_LEDGER.csv", ["source", "sha256", "class", "confidence", "path"],
     [["Mimo 9.35 APK", "48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a", "baseline UI", "VERIFIED_STATIC", "mimo-ui/"],
      ["Hamdars 7.4.4 APK", "9e362f08670174a3e8a3b319b5a2f687da8ecf7896ea78ea2ec70b95dd817be3", "counseling app", "VERIFIED_STATIC", "UPGRADE/SOURCE_APPS/hamdars/"],
      ["Hadaf Plus 2.0.2 APK", "b282f578b255fecc4b72ee74f2ce79eb5bbcde35f3515690342b7fa37a5bbf43", "counseling app", "VERIFIED_STATIC", "UPGRADE/SOURCE_APPS/hadaf_plus/"],
      ["helpcenter/lessons.json", "-", "in-app UX doc", "VERIFIED_STATIC", "UPGRADE/SOURCE_APPS/hamdars/HELP_CENTER_UX.md"],
      ["7 study_schedule templates", "-", "7 templates", "INFERRED_STRONG", "UPGRADE/SOURCE_APPS/hadaf_plus/ASSET_FOLDERS.csv"],
      ["craft-anything v0.3.0", "-", "workflow/tool catalog", "VERIFIED_STATIC", "UPGRADE/CRAFT_ANYTHING/upstream_docs/"],
      ["REA JS evidence", "ev_a3135ad9dd9a6441f057ed5dd2a23e3dd08c98780f79b2dc13953a0ea62f4a58", "Mimo WebView bridge", "VERIFIED_STATIC + 8 limits", "mimo-ui/REFERENCE/REA_EVIDENCE/JS_EVIDENCE.json"],
      ["LearnHarness pinned", "e69e85269c064c6c9c49a8b06ae78c06e79c4a63", "backend", "VERIFIED_STATIC", "mimo/engines/pins.json"],
      ["EPM pinned", "14c1b276297258e51d05281bdc1dfaf750a2b564", "exam engine", "VERIFIED_STATIC", "mimo/engines/pins.json"],
      ["BankBookkonkor PDF", "-", "Konkur question source", "UNKNOWN (no text layer)", "Drive mimo folder"]])

wcsv("OPEN_QUESTIONS.csv", ["id", "question", "current_assumption", "blocking", "resolve_phase"],
     [["U01", "منظور از «دوسن مت» چیست؟", "بخش دوستان / رفاقت و رقابت", "no", "P0"],
      ["U02", "محتوای PDF BankBookkonkor قابل استخراج است؟", "PDF تصویری بدون لایه متن؛ نیاز به OCR", "no", "P0"],
      ["U03", "اسکرینشات/دستگاه مرجع Mimo هست؟", "فقط شواهد استاتیک", "no", "P0"],
      ["U04", "Learn Harness موردنظر کدام نسخه است؟", "amosblomqvist/learnharness @ e69e8526", "no", "P0"],
      ["U05", "پیامهای «پرو» در سایر صفحات هم حذف شوند؟", "فقط صفحه/CTA اشتراک و پرداخت حذف شد", "no", "P0"]])

# ---------------------------------------------------------------- WIREFRAME ----
WIRE = r"""
<!doctype html>
<html lang="fa" dir="rtl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>قرارداد وفاداری UI — Mimo Konkur (نمایش پلن، نه محصول نهایی)</title>
<style>
:root{
 --bg:#F6F7FB; --card:#FFFFFF; --card-pressed:#F6F7FB; --card-disabled:#E4E6F1;
 --outline:#7E4BDE; --primary:#7E4BDE; --text:#252746; --muted:#6A7180;
 --success:#66BC5A; --error:#F05A6E; --progress:#8D60E2; --progress-bg:#E4E6F1;
 --radius:12px; --gap:16px; --maxw:608px;
}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--text);font-family:Tahoma,"Segoe UI",system-ui,sans-serif;font-size:14px;line-height:1.7}
header{background:var(--card);border-bottom:1px solid var(--card-disabled);padding:18px 24px}
header h1{margin:0;font-size:20px} header p{margin:4px 0 0;color:var(--muted);font-size:13px}
.layout{display:grid;grid-template-columns:minmax(0,1fr) 300px;gap:24px;padding:24px;max-width:1400px;margin:auto}
aside{background:var(--card);border-radius:var(--radius);padding:18px;border:1px solid var(--card-disabled);height:max-content;position:sticky;top:24px}
aside h3{margin:0 0 10px;font-size:15px} aside code{background:var(--card-pressed);padding:1px 5px;border-radius:6px;font-size:11px}
aside ul{margin:0 10px 14px;padding:0;list-style:none} aside li{padding:4px 0;border-bottom:1px dashed var(--card-disabled);font-size:12px}
.badge{display:inline-block;background:var(--card-pressed);border:1px solid var(--outline);color:var(--primary);border-radius:999px;padding:1px 9px;font-size:11px;margin:2px}
.screens{display:grid;grid-template-columns:repeat(auto-fit,minmax(320px,1fr));gap:24px;align-items:start}
.screen{background:var(--card);border:1px solid var(--card-disabled);border-radius:var(--radius);overflow:hidden}
.screen > h2{font-size:14px;margin:0;padding:12px 16px;background:var(--card-pressed);border-bottom:1px solid var(--card-disabled)}
.phone{max-width:var(--maxw);margin:auto;padding:14px}
.appbar{display:flex;align-items:center;justify-content:space-between;background:var(--card);border-bottom:1px solid var(--card-disabled);padding:8px 4px;margin-bottom:12px}
.appbar b{font-size:16px} .timer{background:var(--card-pressed);border:1px solid var(--error);color:var(--error);border-radius:999px;padding:4px 12px;font-size:13px;font-weight:bold}
.chips{display:flex;gap:8px;overflow:auto;margin-bottom:14px;padding-bottom:4px}
.chip{white-space:nowrap;border:1px solid var(--card-disabled);background:var(--card);border-radius:999px;padding:5px 12px;font-size:12px}
.chip.on{background:var(--outline);color:#fff;border-color:var(--outline)}
.grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:var(--gap)}
.node{background:var(--card);border:1px solid var(--card-disabled);border-radius:var(--radius);height:96px;display:flex;align-items:center;justify-content:center;font-size:28px;position:relative;box-shadow:0 1px 2px rgba(37,39,70,.06)}
.node.current{border:2px solid var(--outline)} .node.done{border-color:var(--success);background:#F3FBF2}
.node.locked{background:var(--card-disabled);color:var(--muted);opacity:.75}
.node .mini{position:absolute;top:6px;left:8px;font-size:10px;background:var(--card-pressed);border-radius:6px;padding:1px 5px}
.label{text-align:center;font-size:13px;margin-top:8px;color:var(--text);min-height:38px}
.section-title{font-size:14px;margin:18px 0 10px;color:var(--muted)}
.progress{height:6px;border-radius:6px;background:var(--progress-bg);overflow:hidden;margin:10px 0}
.progress i{display:block;height:100%;width:62%;background:var(--progress)}
.tabs{display:grid;grid-template-columns:repeat(4,1fr);border-top:1px solid var(--card-disabled);background:var(--card)}
.tab{text-align:center;padding:10px 4px;font-size:11px;color:var(--muted)}
.tab.on{color:var(--primary);font-weight:bold;border-top:2px solid var(--primary)}
.ai{border:1px solid var(--card-disabled);border-radius:var(--radius);padding:12px;background:var(--card)}
.ai .head{display:flex;justify-content:space-between;border-bottom:1px solid var(--card-disabled);padding-bottom:8px;font-weight:bold}
.bubble{background:var(--card-pressed);border-radius:var(--radius);padding:8px 12px;margin:10px 0;max-width:82%;font-size:12px}
.bubble.me{background:var(--outline);color:#fff;margin-right:auto}
.dockb{display:flex;gap:8px;overflow:auto;margin:10px 0;padding-bottom:4px}
.dockb span{white-space:nowrap;background:var(--card-pressed);border:1px solid var(--card-disabled);border-radius:999px;padding:5px 10px;font-size:11px}
.input{border:1px solid var(--outline);border-radius:var(--radius);padding:9px 12px;color:var(--muted);font-size:12px}
.tpl{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}
.tpl div{border:1px solid var(--card-disabled);border-radius:var(--radius);padding:10px;text-align:center;font-size:12px;background:var(--card)}
.tpl div.on{border:2px solid var(--outline)}
.pcard{border:1px solid var(--card-disabled);border-radius:var(--radius);padding:12px;margin-bottom:10px;background:var(--card)}
.pcard b{color:var(--primary)}
.kv{display:flex;justify-content:space-between;font-size:12px;border-bottom:1px dashed var(--card-disabled);padding:4px 0}
.note{background:#FFF7E6;border:1px solid #F5D28B;border-radius:var(--radius);padding:10px 14px;font-size:12px;margin:0 24px 24px;max-width:1400px}
@media(max-width:900px){.layout{grid-template-columns:1fr}aside{position:static}}
</style>
</head>
<body>
<header>
  <h1>قرارداد وفاداری UI — ارتقای Mimo به اپ کنکور</h1>
  <p>نمایشگر پلن فاز P1…P6 با توکنهای واقعی استخراجشدهٔ Mimo 9.35. این یک وایرفریم مشخصاتی است، نه محصول نهایی و نه کپیای از اپهای مشاوره.</p>
</header>
<div class="layout">
  <div class="screens">

    <section class="screen">
      <h2>① تب Practice — هاب آزمونها (گرههای ۳تایی، برچسب زیر)</h2>
      <div class="phone">
        <div class="appbar"><b>آزمونها</b><span class="timer">⏱ ۱۲:۴۵</span></div>
        <div class="chips"><span class="chip on">همه</span><span class="chip">جامع</span><span class="chip">تکدرسی</span><span class="chip">مبحثی</span><span class="chip">این ماه</span></div>
        <div class="section-title">آزمونهای این ماه</div>
        <div class="grid">
          <div><div class="node current">◇<span class="mini">⏱</span></div><div class="label">آزمون جامع<br>کنکور</div></div>
          <div><div class="node">◇<span class="mini">۲۰ سؤال</span></div><div class="label">آزمون تکدرسی<br>زیست</div></div>
          <div><div class="node done">✓</div><div class="label">آزمون مبحثی<br>سمها</div></div>
          <div><div class="node">◇<span class="mini">جدید</span></div><div class="label">آزمون این ماه</div></div>
          <div><div class="node locked">🔒</div><div class="label">آزمون نهایی</div></div>
          <div><div class="node">⏱</div><div class="label">آزمون زماندار</div></div>
        </div>
        <div class="progress"><i></i></div>
        <div class="section-title">ادامهٔ مسیر (همان الگوی فصلهای میمو)</div>
        <div class="grid">
          <div><div class="node">◇</div><div class="label">تشریحی</div></div>
          <div><div class="node">◇</div><div class="label">آزمون دوباره</div></div>
          <div><div class="node">◇</div><div class="label">مرور غلطها</div></div>
        </div>
      </div>
      <div class="tabs"><div class="tab">Learn</div><div class="tab on">Practice</div><div class="tab">Leaderboard</div><div class="tab">Profile</div></div>
    </section>

    <section class="screen">
      <h2>② AI میمو — ظاهر ثابت + ردیف دکمههای Learn Harness</h2>
      <div class="phone">
        <div class="appbar"><b>دستیار هوشمند</b><span class="badge">پالس AI</span></div>
        <div class="ai">
          <div class="head"><span>گفتگو</span><span>✕</span></div>
          <div class="bubble">سلام! روی کدوم مبحث میخوای کار کنیم؟</div>
          <div class="bubble me">مشتقات رو برام توضیح بده</div>
          <div class="bubble">اول ببینیم از کجا شروع کنیم… <span class="badge">Think out loud</span></div>
          <div class="dockb">
            <span>جلسهٔ تازه</span><span>جلسهها</span><span>نقشهٔ یادگیری</span><span>گراف دانش</span>
            <span>تمرین</span><span>سؤال بعد</span><span>بفهمم یا نه</span><span>میزان اطمینان</span>
            <span>فکر کردن با صدای بلند</span><span>راهنما</span><span>یادداشتهام</span><span>پژوهش</span>
            <span>شکلسازی</span><span>PDF</span><span>گفتار</span><span>توقف</span>
          </div>
          <div class="input">پیامت رو بنویس… (ai_tutor_input_placeholder)</div>
        </div>
        <p style="font-size:11px;color:var(--muted)">هدر، حبابها، نوار ورودی، ماسکات و پالس بدون تغییر؛ فقط ردیف اکشن اضافه شده است. هیچ عنصری حذف نشده.</p>
      </div>
    </section>

    <section class="screen">
      <h2>③ مشاوره — ۷ قالب هدفپلاس با کارتهای میمو</h2>
      <div class="phone">
        <div class="appbar"><b>مشاوره و برنامه</b><span class="badge">؟ راهنما</span></div>
        <div class="section-title">برنامۀ هفته رو با یه قالب آماده بچین</div>
        <div class="tpl">
          <div class="on">پومودورو</div><div>روز مدرسه</div><div>سحرخیزی</div>
          <div>شبخوانی</div><div>بعد از ۱۰</div><div>روز تعطیل</div>
          <div>دورهٔ فشرده</div>
        </div>
        <div class="pcard" style="margin-top:14px"><b>درخواست مشاور</b><div class="kv"><span>پایه / رشته</span><span>دوازدهم تجربی</span></div><div class="kv"><span>تراز کل</span><span>۶۲۰۰</span></div><div class="kv"><span>هدف</span><span>پزشکی تهران</span></div></div>
        <div class="pcard"><b>گزارش هفتگی</b><div class="kv"><span>ساعت مطالعه</span><span>۱۲:۳۶</span></div><div class="kv"><span>تعداد تست</span><span>۱۱۵</span></div><div class="kv"><span>روزهای تا کنکور</span><span>۲۲۹</span></div></div>
        <p style="font-size:11px;color:var(--muted)">هیچ صفحهٔ اشتراک، سبد خرید، پرداخت یا بنر «پرو» وجود ندارد.</p>
      </div>
    </section>

    <section class="screen">
      <h2>④ پروفایل — همان کارتهای Mimo + دادهٔ کنکور</h2>
      <div class="phone">
        <div class="appbar"><b>پروفایل</b><span class="badge">🔥 ۱۲ روز</span></div>
        <div class="pcard"><b>کاربر کنکور</b><div class="kv"><span>امتیاز امروز</span><span>۴۲ / ۵۰ ⚡</span></div><div class="progress"><i style="width:84%"></i></div></div>
        <div class="pcard"><b>اطلاعات تحصیلی</b><div class="kv"><span>پایه</span><span>دوازدهم</span></div><div class="kv"><span>رشته</span><span>تجربی</span></div><div class="kv"><span>تراز</span><span>۶۲۰۰</span></div><div class="kv"><span>سهمیه</span><span>منطقه ۱</span></div></div>
        <div class="pcard"><b>نشانها</b><div class="tpl" style="grid-template-columns:repeat(4,1fr)"><div>تحلیلگر</div><div>جبران</div><div>منظم</div><div>لیگ</div></div></div>
        <div class="pcard"><b>دوستان و رقابت</b><div class="kv"><span>لیگ هفتگی</span><span>رتبه ۳</span></div></div>
      </div>
      <div class="tabs"><div class="tab">Learn</div><div class="tab">Practice</div><div class="tab">Leaderboard</div><div class="tab on">Profile</div></div>
    </section>

  </div>

  <aside>
    <h3>توکنهای الزامی (عیناً)</h3>
    <ul>
      <li>background <code>#F6F7FB</code> / night <code>#252746</code></li>
      <li>card_enabled <code>#FFFFFF</code> · pressed <code>#F6F7FB</code></li>
      <li>card_disabled <code>#E4E6F1</code> · outline <code>#7E4BDE</code></li>
      <li>button_primary <code>#7E4BDE</code> / night <code>#885BDE</code></li>
      <li>text_primary <code>#252746</code> · success <code>#66BC5A</code></li>
      <li>error_default <code>#F05A6E</code> · progress <code>#8D60E2</code></li>
      <li>radius <code>12dp</code> · gap <code>16dp</code> (<code>sw600dp 24dp</code>)</li>
      <li>content_max_width <code>608dp</code> · sheet <code>496dp</code></li>
      <li>progressbar <code>6dp</code> · keyboard <code>64dp</code> · modal <code>296dp</code></li>
      <li>streak_calendar <code>264dp</code> (<code>sw600dp 324dp</code>)</li>
    </ul>
    <h3>دروازهها</h3>
    <span class="badge">F0 چهار تب</span><span class="badge">F1 بدون تب تازه</span><span class="badge">F2 توکنها</span>
    <span class="badge">F3 دوسیه مرجع</span><span class="badge">F4 مودال/بازگشت</span><span class="badge">F5 حالت کارت</span>
    <span class="badge">F6 RTL</span><span class="badge">F7 clean-room</span><span class="badge">F8 xref</span><span class="badge">F9 diff بصری</span>
    <h3 style="margin-top:16px">ضدرگرسیون</h3>
    <ul>
      <li>❌ پروتوتایپ قبلی ۵ تب داشت (تب <b>Max</b>) → حذف</li>
      <li>❌ «۳ تب» در اسناد قدیمی → اصلاح به ۴</li>
      <li>❌ موتورهای وب بهعنوان تب مستقل → پشت مقصد درونتبی</li>
      <li>❌ صفحهٔ اشتراک هدفپلاس → حذف کامل</li>
      <li>❌ تغییر رشتههای <code>ai_tutor_*</code> → ممنوع</li>
    </ul>
    <h3>منابع</h3>
    <ul>
      <li><code>mimo-ui/ATLAS/index.html</code></li>
      <li><code>mimo-ui/CATALOGS/DESIGN_TOKENS.json</code></li>
      <li><code>UPGRADE/SOURCE_APPS/*</code></li>
      <li><code>UPGRADE/CATALOGS/*.csv</code></li>
      <li><code>UPGRADE/02_UI_FIDELITY_CONTRACT.md</code></li>
    </ul>
  </aside>
</div>
<div class="note">⚠️ این صفحه صرفاً <b>مشخصات بصری پلن</b> است. رنگها، فاصلهها و شعاعها مستقیم از استخراج Mimo 9.35 آمدهاند؛ هیچ دارایی، متن یا تصویری از Mimo، همدرس یا هدفپلاس کپی نشده است. وضعیت اجرا: تمام فازها <b>PLANNED</b>.</div>
</body>
</html>
"""
w("wireframes.html", WIRE)

# ---------------------------------------------------------------- install note ----
w("CRAFT_ANYTHING/INSTALL.md", r"""
# نصب لایهٔ عاملی craft-anything

- منبع: `https://github.com/storytold/craft-anything.git` (v0.3.0)، کلون در `/home/user/_work/craft-anything`.
- وندورشده در `upstream_docs/`: `README.md`, `AGENTS.md`, `CLAUDE.md`, `ATTRIBUTION.md`, `NOTICE`, `LICENSE-MIT`, `LICENSE-APACHE`, `docs/tools.md`, `docs/pitfalls.md`, `docs/extending.md`, `docs/STATUS.md`, `docs/ROADMAP.md`, `docs/schemas/*.json`.
- آداپتور قابلاجرا: `craft_adapter.py` (۳۳ شناسه ابزار، قرارداد شواهد، deep mode، بدون وابستگی خارجی).
- workspace: `workspace/craft.json`, `investigation.cany.json`, `plan.json`, `unknowns.json`, `brief.md`.
- خروجی: `../CATALOGS/EVIDENCE_LEDGER.json` (۱۳ رکورد: ۳ target + ۱۰ finding).
- محدودیت: باینری native بهدلیل محدودیت egress و نبود Rust نصب نشد؛ جزئیات در `../01_CRAFT_ANYTHING_INSTALL.md`.

اجرا:
```
python3 craft_adapter.py doctor
python3 craft_adapter.py core-evidence-show
python3 craft_adapter.py core-plan-update --phase P0 --status DONE
```
""")

print("DONE", OUT)
