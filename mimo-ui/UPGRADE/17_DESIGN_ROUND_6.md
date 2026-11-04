# دور ششم طراحی — DESIGN v6 (بازبینی زیرصفحات یادگیری)
<!-- v9-banner -->
> ⚠️ **بایگانی / superseded:** طراحی فعلی **[DESIGN v9](21_DESIGN_ROUND_9.md)** است. همچنان فقط پلن/دیزاین؛ هیچ کد محصولی نوشته نشده.
<!-- v8-banner -->
> ⚠️ **بایگانی / superseded:** طراحی فعلی **[DESIGN v8](20_DESIGN_ROUND_8.md)** است. همچنان فقط پلن/دیزاین؛ هیچ کد محصولی نوشته نشده.
<!-- v7-banner -->
> ⚠️ **بایگانی / superseded:** طراحی فعلی **[DESIGN v7](18_DESIGN_ROUND_7.md)** است. همچنان فقط پلن/دیزاین؛ هیچ کد محصولی نوشته نشده.

> **وضعیت:** `DESIGN v6 · REVIEW` — منتظر تأیید نهایی. همچنان **فقط پلن/دیزاین**؛ هیچ کد محصولی نوشته نشده.
> **روش:** کندوکاو **عمیقتر از داخل کد APK**؛ اسکرینشاتها فقط چک بصری. جایگزین `16_DESIGN_ROUND_5.md` است (لاگهای قبل بایگانی شدند).

---

## ۱. ایرادهایی که شما گفتید (کلمهبهکلمه)

| # | گفتهٔ شما | اقدام |
|---|---|---|
| ۱ | «فعلاً به صفحهٔ ورود که صفحهٔ ۷ هست نیازی نداریم» | صفحهٔ `onboarding` **کاملاً از طراحی حذف شد**. شاهدش (`mimo-09-onboarding.webp`) در `REFERENCE/` بایگانی ماند. |
| ۲ | «عمدهترین مشکل در صفحهٔ یادگیری هست که یکم به هم ریخته و نیاز به بازبینی و بازسازی داره… فکر کنم یکم ویرایش کنی اوکی بشه» | صفحهٔ Learn **تمیز بازسازی شد**: ۳ چیپ (سکه ۱٬۲۷۲ / کلید ∞ / استریک ۰)، کارت سربرگ مسیر، مسیر مارپیچ ۵ گرهای؛ **حلقهٔ ۱۲٪، چیپ «پیشرفت ۱/۲» و نوشتهٔ توضیحی داخل UI حذف شدند** (همان عوامل شلوغی). |
| ۳ | «وقتی روی سه تا خط کنار وب دولوپمنت کلیک میکنیم باید صفحهای باز بشه که درسها رو نشون بده، اینها رو بازسازی نکردید» | **`Select Path` ساخته شد**: ۴ کارت «Career Paths» + ۶ ردیف «Courses». سهخط `ic_list_bulleted` دقیقاً به آن وصل است. |
| ۴ | «یا مثلاً داخل خود مبحث وقتی میزنی» | **`Path Overview`** (گواهی + فصلهای شمارهدار ۳…۷) و **`Section detail`** (فهرست درسها) ساخته شدند؛ کلیک روی فصل/گره به داخل مبحث میرود. |
| ۵ | «این بخشها خیلی مهمند… حتماً از داخل کد باید مهندسی معکوس کنی دقیقتر دربیاری که چطور نوشته شدند، یعنی هنوز نتونستی خوب دربیاری تو اپلیکیشن خیلی بخشها رو» | استخراجگر اختصاصی نوشته شد که **زیرصفحات یادگیری** را از ۶ منبع کد بیرون میکشد → `DESIGN/LEARN_CODE_GEOMETRY.json` و **۸۶۸ ردیف** کاتالوگ شواهد. |

---

## ۲. منابع کدی که این بار کندوکاو شدند (همه داخل APK)

| منبع | چه چیزی استخراج شد | تعداد |
|---|---|---|
| `CATALOGS/DESIGN_TOKENS.json` (ARSC) | رشتههای `track_switcher_*` / `select_path` / `path_overview_*` / `certificates_*` / `section_details_*` / `chapter_*` / `lesson_*` | **۱۵۰** رشتهٔ دقیق |
| `SOURCE/res/drawable/*.xml` | `android:pathData` وکتورها: `ic_list_bulleted`، `ic_switch`، `ic_key`، `ic_infinity`، `ic_mimo_mascot`، ۱۲ عدد `ic_badge_*`، ۴ عدد `ic_code_lang_*`، `ic_badge_backend_professional` | **۴۱** وکتور |
| `SOURCE/res/layout/*.xml` | AXML دیکدشده: `onboarding_select_path_fragment`، `onboarding_pick_a_path`، `search_track_fragment`، `search_tracks_list_item`، `profile_certificate_view`، `certificate_activity`، `chapter_toolbar`، `chapter_activity`، `lesson_noninteractive_fragment`، … | **۱۶** لایه |
| `SOURCE/res/navigation/nav_onboarding_graph.xml` | `action_select_path → nav_select_path → OnboardingSelectPathContainerFragment` | ۱ گراف |
| `SOURCE/assets/ui/testdata/test-tracks.json` | **مدل محتوای واقعی**: نسخهٔ ۵۲، ۲۵ مسیر، ۱۵ فصل با `name/description/startIndex/endIndex/tutorialIds`، ۹ درس | ۱۵ فصل / ۱۶ شناسهٔ درس |
| `SOURCE/dex/UI_CLASSES.json` + `UI_STRING_LITERALS.txt` | `ObservePathSwitcherState` (۵۱)، `PathMapScreenKt` (۸۱)، `PathOverviewScreenKt` (۲۱)، `OnboardingSelectPath*` (۲۹)، certificate (۲۶)، `content/model/track/*` (۶۴) ← **۲۷۲ کلاس** + `showPathSwitcher`، `key_path_switcher_on_exit_enabled`، `SectionJson`، `isCareerPath` | ۲۷۲ کلاس / ۱۶ لیترال |
| توکنها | ۶۸ رنگ، ۶۲ دایمنشن، ۲۱۳ استایل | — |

خروجیها: `DESIGN/LEARN_CODE_GEOMETRY.json` (۲۱۴٬۲۱۱ بایت) و `CATALOGS/MIMO_LEARN_SUBSCREENS.csv` (**۸۶۸ ردیف**: هر رشته/وکتور/لایه/action/فصل/درس/کلاس/توکن با منبع دقیق).

### خط لولهٔ قابلتکرار
```
tools/extract_mimo_geometry.py       → DESIGN/CODE_GEOMETRY.json       (۴۶ وکتور، ۴۱ رنگ، …)
tools/extract_mimo_learn_v6.py       → DESIGN/LEARN_CODE_GEOMETRY.json + CATALOGS/MIMO_LEARN_SUBSCREENS.csv
tools/build_design_v6.py             → DESIGN/index.html (۲۸۱٬۱۰۶ بایت) + tools/design_v6_template.html
```
`index.html` **تولید میشود**؛ فهرست فصلها، شناسهٔ درسها، رشتهها و ۲۵ وکتور تازه همگی از JSON استخراجشده در زمان اجرا رندر میشوند.

---

## ۳. بازسازی صفحهٔ یادگیری (چرا «بههمریخته» بود)

| عامل شلوغی v5 | جایگزین v6 | منبع کد |
|---|---|---|
| ۲ چیپ (۲۰۰ سکه / ۱ استریک) | **۳ چیپ**: ۱٬۲۷۲ سکه، کلید ∞، استریک ۰ | `PathToolbarKt$RowWithKeys` + `ic_key` / `ic_infinity` / `ic_coin` / `ic_streak_active` |
| نوار باریک نام درس + آیکن سهخط جدا | همان سهخط کنار نام مسیر، **قابلکلیک** | `ic_list_bulleted` + `select_path` |
| «قرص فصل» با حلقهٔ ۱۲٪ | **کارت سربرگ مسیر**: «Career path» / «3. Arrays & Functions» / نوار پیشرفت ۴۳٪ | `ViewsKt$OverviewEntryPointHeader` + `path_see_course_overview` + `progress_bar_mimo.xml` (شعاع ۱۰۰dp، رنگ `progress_primary`) |
| نوشتهٔ «همان چیدمان PathMapScreenKt…» **داخل گوشی** | حذف شد (توضیح به پنل کناری منتقل شد) | — |
| چیپ «پیشرفت ۱/۲» بهعنوان دکمهٔ دیباگ داخل گوشی | حذف شد | — |
| ۵ گره با تداخل / FAB «A» | مسیر مارپیچ تمیز ۵ گره + خطوط رابط | `PathMapScreenKt` + `ic_check_white` / `ic_flash` |

---

## ۴. صفحات تازه (همه از کد)

### ۴٫۱ `Select Path` — سهخط کنار نام مسیر
- سرتیتر: `X` + `select_path = "Select Path"` (استایل `TextToolbarTitle`).
- `track_switcher_career_paths = "Career Paths"` → ۴ کارت:
  `Full-Stack Developer 1/20`، `Python Developer 2/9`، `Back-End Developer 2/9` (منتخب، کادر `card_outline #FF7E4BDE` + هالهٔ `progress_weak`)، `Front-End Developer`.
  ردیف badgeها از `ic_badge_*`/`ic_code_lang_*`؛ لیبل `section = "SECTION"`؛ نوار `progress_bar_mimo.xml`.
- `courses = "Courses"` → ۶ ردیف: `TypeScript 0/4` (`track_switcher_typescript_label = "JS required"`),
  `React 0/3` (`track_switcher_react_label = "HTML, CSS and JS requi…"` با `ellipsize=end`), `HTML 0/5`, `SQL 0/6`, `CSS 0/4`, `Python 6/14` (کمان بنفش ۴۳٪).
  حلقهها دقیقاً از `profile_certificate_view.xml`: `CircularProgressIndicator` با `indicatorSize=56dp`، `indicatorColor=progress_primary`، `trackColor=progress_empty`، `trackCornerRadius=3dp`.
- کد بایگانیشده (طراحی نشد، چون صفحهٔ جدا لازم نبود): `track_switcher_title = "Coding Path"`، `track_switcher_early_access_label = "Early access"`، `search_tracks = "Search tracks"`.

### ۴٫۲ `Path Overview` — کارت مسیر / گواهی / فصلها
- `onboarding_path_type_career_path = "Career path"` + نام مسیر (`TextH1 24sp`) + دکمهٔ `ic_switch` (دو فلش، ۳۲dp، `fillType=evenodd`) → `Select Path`.
- کارت گواهی: `ic_badge_backend_professional` (۴۸×۶۰، ۲۰ مسیر)،
  `certificates_professional_title = "Professional Certificate"`،
  `path_overview_certificate_percent_complete = "%1$d%% Complete"` → «22% Complete»، `2/9`، نوار پیشرفت.
- فصلها با `path_overview_section_ordinal = "%d. %s"` → شمارههای ۳…۷، حلقهٔ ۴۳٪ / ۰٪،
  و **نام/توضیح/تعداد درس مستقیم از `test-tracks.json :: tracks[0].sections[]`**
  (`JavaScript Basics`, `HTML Intermediate`, `Semantic HTML`, `CSS Intermediate`, `Types and Comparisons`).
  خط عمودی رابط `progress_chapter_primary #FF8D60E2`؛ فصل جاری کارت سفید حاشیهدار.
  لیبلها: `path_overview_section_project_label = "Section Project"`، `path_section_coming_soon = "Coming soon"`، `alert_msg_section_setion_locked`.
- کلاس پشت صفحه: `PathOverviewScreenKt`، `OverviewEtaCardKt`، `PathOverviewHeaderVisibilityKt`، `PathOverviewViewModel`.

### ۴٫۳ `Section detail` — «داخل خود مبحث»
- سربرگ فصل + توضیح + نوار ۴۳٪؛ فهرست درسها با **شناسههای واقعی `tutorialIds`** از همان فصل (۱۶ شناسه)،
  وضعیت ✓ / ▶ / 🔒، ردیف «Section Project» و ردیف «Coming soon» (قفل → `alert_msg_section_setion_locked`).
- دکمهها: `lesson_continue = "Continue"` → کارت شروع فصل → صفحهٔ درس؛ `path_see_course_overview = "See course overview"` → نمای مسیر.
- رشتههای پشتیبان بایگانی: `lesson_skip`، `lesson_submit`، `lesson_try_again`، `section_details_smart_practice_*`، `chapter_end_*`، `path_completion_estimation_*`.

### ۴٫۴ دیالوگ `Unfinished track`
- دقیقاً از `certificates_unfinished_track_dialog_title = "Unfinished track"`،
  `..._text = "Finish the track and receive your personalised certificate"`،
  `..._action = "Ok"`؛ شعاع `m3_alert_dialog_corner_size = 28dp`؛ ماسکات `ic_mimo_mascot` (۲۹ مسیر وکتور).
- باز میشود با: کلیک روی مسیر **غیرمنتخب** در Select Path، کلیک روی کارت گواهی، یا ردیف «Coming soon».

---

## ۵. گراف کلیک (تستشده با اجرای واقعی DOM)

```
Learn ──سهخط ic_list_bulleted──▶ Select Path ──ردیف درس──▶ Section detail ──Continue──▶ Chapter modal ──▶ Lesson
  │                                   ▲                          │
  └──کارت سربرگ مسیر──▶ Path Overview ──ic_switch──────────────┘  └──See course overview──▶ Path Overview
                              │
                              ├──فصل──▶ Section detail
                              └──گواهی / مسیر ناتمام──▶ Unfinished track (Ok → بسته)
```
همچنین ۵ تب `Learn / Practice / AI / Leaderboard / Profile`، ۷ بخش هاب آزمون، تایمر ۲۷۰ دقیقه،
«پاسخبرگ»/`«پاسخنامه»` و دو دکمهٔ «توضیح با هوش مصنوعی» **بدون تغییر** باقی ماندند.

---

## ۶. تفاوت کد / اسکرینشات (کد ملاک است)

| مورد | کد | اسکرینشات | تصمیم |
|---|---|---|---|
| ناوبری | منوی AXML: ۴ تب (`Learn/Practice/Leaderboard/Profile`) | `mimo-10` نسخهای با تب **MAX** نشان میدهد | **حکم صریح شما**: ۵ تب `Learn/Practice/AI/Leaderboard/Profile`؛ MAX راه نیافت |
| نام فصلها | `test-tracks.json`: `HTML Basics`, `CSS Basics`, `JavaScript Basics`… | «Arrays & Functions», «Objects & ES6»… | ساختار/شمارهگذاری/حلقهها/رشتهها از **کد**؛ فقط **نام درس/مبحث** کنکوری شد |
| رنگ `ic_switch` | `#FF333661` (`fillType=evenodd`) | بنفش | رنگ کد اعمال شد |
| RTL | ۱۶۱ کوالیفایر، **۰** مورد `fa/ar/he` | — | نمای پیشفرض LTRِ ۱۰۰٪ میمو + دکمهٔ «فارسی / RTL» |

---

## ۷. تست و وضعیت

- `node --check` روی ۳ اسکریپت ✓
- اجرای واقعی DOM (jsdom): **۰ خطای runtime**، ۱۳ نما، ۵ تب، ۴ کارت مسیر، ۶ ردیف درس،
  ۵ فصل، ۹ ردیف مبحث، **۹۹/۹۹ آیکن SVG رسمشده** (هیچ `data-icon` خالی نماند).
- جریانها: سهخط → Select Path ✓ · کارت مسیر → Path Overview ✓ · `ic_switch` → Select Path ✓ ·
  ردیف درس → Section detail ✓ · فصل → Section detail ✓ · دیالوگ باز/بسته ✓ ·
  RTL/LTR ✓ · حالت شب ✓ · تایمر ۲۷۰ ✓ · پاسخبرگ/پاسخنامه ✓ · دکمههای AI ✓.
- ۱۴ اسکرینشات (۵ تازه: `mimo-10`…`mimo-14`) در `CATALOGS/MIMO_SCREENSHOT_CROSSWALK.csv` با SHA-256 و نقش `VISUAL_CROSSCHECK_ONLY`.
- `VERIFICATION_REPORT.json` → PASS.

**منتظر تأیید نهایی شما**؛ بعد از «مرحلهٔ بعد» میرویم سراغ P0 پیادهمسازی.
