# ۴ · وضعیت دقیق امروز (فایلها، دستورات، اعداد)

**HEAD محصول:** `9179b8c4` (مجموعه اسناد `docs/` بعد از آن افزوده شد) · **شاخه:** `arena/aebb90b7-game` · **تاریخ:** ۲۰۲۶-۱۱-۰۵
**فایلهای tracked:** ۱۳٬۶۱۶ (قبل از افزودن این اسناد) · **کامیتها:** ۱۳۷

## ۱) نقشهٔ کامل پوشهها

| مسیر | فایلها (روی دیسک) | tracked | محتوا / چرا وجود دارد |
|---|---|---|---|
| `README.md`, `AGENTS.md` | ۲ | ۰→۲ | **نقطهٔ ورود انسان و ایجنت** (تازه) |
| `REPO_INDEX.json` | ۱ | ۰→۱ | ایندکس ماشینخوان (تازه) |
| `docs/` | ۱۲ | ۰→۱۱ | اسناد تحویل ۰۰…۰۹ + `verify_docs.py` (تازه) |
| `mimo-ui/` | ۷٬۴۳۰ | ۷٬۴۳۰ | استخراج ۰–۱۰۰ UI میمو ۹٫۳۵: `ATLAS/`, `CATALOGS/`, `SCREENS/`, `RECONSTRUCTION/`, `REFERENCE/`, `SOURCE/`, `tools/` |
| `mimo-ui/UPGRADE/` | ۱٬۹۵۵ | ۱٬۹۵۵ | بایگانی ۱۲ دور طراحی؛ ۲۵ سند `00…24_*.md`، `CATALOGS/` (۲۴ کاتالوگ)، `DESIGN/index.html` (v12.5-fa)، `CRAFT_ANYTHING/`, `SOURCE_APPS/`, `tools/` |
| `ANALYSIS/` | ۶٬۰۸۴ | ۶٬۰۷۵ | شواهد مهندسی معکوس: `DECOMPILED/`, `GHIDRA/`, `RUNTIME/`, `_INPUT/`, `_TOOLCHAIN/`, `MISSION_05…09/`، ۱۹+گزارش فارسی/انگلیسی، `MIMO_API_SURFACE.json`, `HADAF_PLUS_AI_API_AUDIT.md` |
| `TOOLS/` | ۴۱٬۴۸۰ | ۵ | سابماجولهای پینشده: `ghidra` (NSA/ghidra) و `rea` (morluto/rea) از `.gitmodules`؛ بقیه فایلهای submoduleـاند، tracked نیستند |
| `google_drive/` | ۶ | **۰** | APKها و PDF منبع، **کاملاً gitignored**: `Mimo_9.35 (1).zip/.z01/.z02`, `Hadaf Plus_2.0.2.apk`, `همدرس_7.4.4.apk`, `@BankBookkonkor (26)_extract.pdf` |
| `app/` | ۳٬۰۳۵ | ۹۸ | محصول؛ ۱٬۷۰۱ فایل آن `app/content/source/` (OCR خام، gitignored) و بقیه `node_modules`/`vendor` |
| `.github/workflows/` | ۳ | ۳ | `mimo-re-toolchain.yml`, `mimo-jadx-proxy.yml`, `mimo-runtime-verification.yml` |
| ریشه (باقی) | ۳ فایل قدیمی | ۳ | `Streets-of-Rage_Genesis_EN.zip`, `pharmacy-inventory (3).html`, `ttac-4.3.6.apk` = محتوای آپلود اولیه، بیهیچ وابستگی به پروژه؛ **عمداً نگه داشته شدند** (اسناد تاریخی پاک نشوند) |

### `app/` با جزئیات

| مسیر | توضیح |
|---|---|
| `app/native/index.html` | پوستهٔ بومی بازسازی ۱: تمام صفحات ناوبری M09 (PathMap, ChapterActivity, Quit, Celebration, SelectPath, PathOverview, SectionDetail, PracticeGate, ExamHub) |
| `app/assets/native.css` | لایهٔ وفاداری بومی + استایل بلوکهای درس (`nl-role`, `nl-answerkey`, `native-chapter-row`) — تنها CSS تازه |
| `app/assets/phone.html`, `proto.css`, `proto-data.js`, `proto-ui.js` | **کپی بایتبهبایت مصوب** v12.5-fa؛ منبع توکنها و دادهها. `phone.html` همچنان حاوی متن دموی چیدمان است (بهعنوان شاهد تاریخی) ولی `native.js` دیگر آن را بهعنوان درسنامه نمیخواند. |
| `app/src/` (۲۲ فایل) | `native.js` (کنترلر)، `content-engine.js` (DSL/A6–A11/پیشرفت)، `content-package.js` (بستهٔ تزریقشده)، `engine.js`, `store.js`, `views.js`, `routes.js`, `nodes.js`, `templates.js`, `harness.js`, `ai-studio.js`, `design-tokens.js`, `token-economy.js`, `learning-path.js`, `exam-template.js`, `starter-package.js`, `output-kit.js`, `plus.js`, `pwa-assets.js`, `fixtures.js`, `util.js`, `app.js` |
| `app/content/` (۱۰ tracked) | `MIMO_INFORMATION_FORM.json/.md` (قرارداد), `CONTENT_FORM_TEMPLATE.json`, `PEDAGOGY.md/.json`, `EXAM_TEMPLATE.json`, `PRACTICE_TEMPLATE.json`, `README.md`, `STARTER_PACKAGE.json` (placeholder), **`STRUCTURED_PACKAGE.json`** (فعلی) |
| `app/content/source/` (۱٬۷۰۱ فایل، gitignored) | JSON صفحات Tesseract، word boxes، `PROCESSED_DRAFT.json`, `PROCESS_REPORT.json` — **هیچکدام وارد اپ نشدهاند** |
| `app/tools/` (۱۵ tracked) | `build_output.py` (بیلدر ۱۵ ماژول), `emit_structured_package.py`, `process_book.py`, `structure_book.py` (قدیمی/شکستخورده), `validate_content.py`, `verify_app.py`, `verify_output.py`, `build_index.py`, `extract_from_prototype.py`, `emit_*`, `ocr_book.py`, `analyze_mimo_lessons.py` |
| `app/tests/` (۶) | `harness.mjs` + ۵ فایل تست؛ از جمله `output.test.mjs` (۱۲ تست بستهبندی + سلسلهمراتب محتوا) |
| `app/docs/` (۷) | `MIMO_CONTENT_MODEL.md` ★, `MIMO_NATIVE_NAVIGATION.md` ★, `OUTPUT_GUIDE.md` ★, `TESTING.md` ★, `ARCHITECTURE.md`, `DEVELOPMENT.md`, `INTEGRATIONS.md` |
| `app/dist/` (۱۲ فایل، ۴٫۵ MB) | ★ **`Mimo.html`**، `index.html` (PWA), `launcher.html`, `Mimo.zip`, `START_HERE.txt`, `README-fa.md`, `BUILD_MANIFEST.json`, `manifest.webmanifest`, `sw.js`, `icons/*` |
| `app/*.md` | `README.md`, `OUTPUT_REPORT.md`, `APP_FINAL_REPORT.md`, `PHASE_2_REPORT.md`, `TESTING.md` (برخی اعداد قدیمی دارند) |
| `app/index.html` | نسخهٔ توسعهای چندفایلهای (http(s) + Service Worker)؛ **خروجی نهایی نیست** |

## ۲) تحویل فعلی

`app/dist/Mimo.html` — **۱٬۸۶۳٬۳۱۲ بایت**، SHA-256
`c6f8cbfbb3c7ee5628cd1f0e7763c9f95ff852d3ce22bc48fa30d691423b2435`،
حاصل ۱۵ ماژول ESM باندلشده در یک IIFE (۳۰۰٬۸۹۰ کاراکتر).
`Mimo.zip` ۹۱۰٬۵۰۹ بایت / ۱۱ فایل هششده. جزئیات هشها ← `BUILD_MANIFEST.json`.

**ناوبری** (M09): MainActivity/تبها → PathMap → ChapterActivity → LessonRenderer
→ QuitDialog / Celebration / SelectPath / PathOverview / SectionDetail /
PracticeGate / ExamHub → AI / Tokens / Output.

**لایهٔ محتوا** (`STRUCTURED_PACKAGE.json`، ۱۷۵٬۴۹۶ بایت):

| متریک | مقدار |
|---|---|
| track / sections / tutorials / chapters | ۱ / ۴ / ۲۰ / ۲۰ |
| ریزدرس (micro-lessons) | **۱۲۰** (۶ نقش × ۲۰ فصل) |
| بلوکهای تایپشده | **۱۶۰** |
| پرسش / پاسخ شناختهشده | ۲۰ / ۲۰ |
| نقشها | `hook → check → feedback → explain → practice → recap` |
| رندررها | `text`, `strong`, `MultipleChoice`, `fillTheGap`, `feedback` |
| وضعیت | `contentStatus:'structured'`, `reviewStatus:'unreviewed'`, `source.kind:'placeholder'` |

`content-engine.js`: پارسر DSL میمو (`p/code/selection/img/webview/interaction/database/output`،
تگ ناشناس رد میشود)، ۹ نوع interaction، ولیدیتورهای A6–A11، ردیف ۱۱فیلدی
`LessonProgress` با `publishSetVersion:753` و `inQueue`، `isSolvedCorrectly ≡ tries>=1`،
صف مرور غلطها. تشریح ← `app/docs/MIMO_CONTENT_MODEL.md`.

## ۳) دستورات (همین الان اجرا شدند، همگی سبز)

```bash
npm test --prefix app       # ۴۵/۴۵ (node --test, jsdom)
npm run verify --prefix app # verify_app.py ۵۴/۵۴  +  verify_output.py ۵۱/۵۱
python3 app/tools/validate_content.py \
  app/content/STARTER_PACKAGE.json app/content/STRUCTURED_PACKAGE.json   # ۲/۲
python3 docs/verify_docs.py  # لینکها، مسیرهای REPO_INDEX.json، نبود CJK
```

ساخت مجدد:

```bash
python3 app/tools/emit_structured_package.py   # → STRUCTURED_PACKAGE.json + content-package.js
python3 app/tools/build_output.py               # → app/dist/*
python3 app/tools/process_book.py               # → app/content/source/ (خارج از گیت، unreviewed)
cd app && npm start                             # → 0.0.0.0:3000 (توسعه)
```

پیشنمایش زندهای که در این نشست بالا آمد: `:3000` (بومی، `Mimo.html`) و
`:3001` (خروجی یککلیکه). بررسی headless Chromium روی هر دو و روی `file://`:
`MIMO=true`, `contentStats().microLessons=120`, ۴ ردیف پاسخنامه، `errors=[]`.

## ۴) پرچمهای صداقت (`BUILD_MANIFEST.json → honest`)

```json
{"llm": false, "network": false, "generatedText": false,
 "externalProvider": "not-configured", "serverConfirmed": false}
```

## ۵) آنچه **هست** و آنچه **نیست**

| ✅ هست | ❌ نیست |
|---|---|
| تکفایل آفلاین خودکفا، PWA، ZIP | نصب فیزیکی PWA روی گوشی (تست نشده) |
| ناوبری بومی M09 + ۵ تب مصوب | محتوای واقعی Practice/Leaderboard/Profile (UNKNOWN) |
| ۱۲۰ ریزدرس تایپشده با `sourceRef` | درسنامهٔ کتاب زیست بهصورت بازبینیشده |
| حداقل ۵ خانوادهٔ رندرر | `InteractiveWebView`, `validatedInput`, `executableFiles`, بلوک `Reveal` (پیاده نشدند) |
| ولیدیتور فرم و بستهٔ محتوا | پاسخهای قطعی OCR (پیشنویس noisy است) |
| اقتصاد توکن و مرور غلطها بهصورت محلی | فرمول پاداش/امتیاز سرور (ServerConfirmed=0) |
| حسابرسی استاتیک API | capture رانتایم endpointها |
| `chapterRefFor()` مبتنی بر بستهٔ ساختاریافته | نگاشت واقعی `chapterRefFor()` به شناسهٔ curriculum میمو (همچنان هشپایه) |
| پاسخبرگ و پاسخنامه جدا | بانک سؤال/آزمون واقعی (`QBANK` همچنان placeholder) |

بعدی: [`05_ROADMAP.md`](05_ROADMAP.md)
