# ۱۰ · نقشهٔ فایلبهفایل (مرجع سریع)

> مکمل `04_CURRENT_STATE.md`: آنجا «چی هست/چطور اجرا کنیم»، اینجا «هر فایل
> دقیقاً چیست». اعداد با `python3 docs/build_repo_index.py` همخواناند.

## درخت سطحبالا

```text
/home/user/game
├── README.md            ← ورودی انسان + ایجنت
├── AGENTS.md            ← قرارداد سخت ایجنتها
├── CLAUDE.md / GEMINI.md / .github/copilot-instructions.md → همان AGENTS.md
├── REPO_INDEX.json      ← نقشهٔ ماشینخوان
├── docs/                ← ۱۱ سند تحویل + ۲ اسکریپت (این پوشه)
├── ANALYSIS/                6084 فایل (6075 tracked)
├── TOOLS/                  41480 فایل (5 tracked)
├── app/                     3035 فایل (98 tracked)
├── google_drive/               6 فایل (0 tracked)
├── mimo-ui/                 7430 فایل (7430 tracked)
└── .github/             ۳ workflow (رانتایم/پروکسی/تولچین)
```

## ریشه

| فایل | نقش |
|---|---|
| `.gitignore` | حذف `google_drive/`, `app/content/source/`, `node_modules/`, `__pycache__/`, `/TOOLS/_*/` |
| `.gitmodules` | `TOOLS/ghidra` ← NSA/ghidra master · `TOOLS/rea` ← morluto/rea main |
| `Streets-of-Rage_Genesis_EN.zip` | آپلود اولیهٔ ۲۰۲۶-۱۰-۲۴، بیربط؛ بایگانی (حذف نشد) |
| `pharmacy-inventory (3).html` | همان، بیربط؛ بایگانی |
| `ttac-4.3.6.apk` | همان، بیربط؛ بایگانی |
| `.github/workflows/*.yml` | `mimo-re-toolchain`, `mimo-jadx-proxy`, `mimo-runtime-verification` |

## `app/src/` — ۲۲ ماژول ESM

| فایل | نقش |
|---|---|
| `native.js` | ★ کنترلر فعلی: ناوبری M09، لیست فصلها، پخشکنندهٔ ۶گام درس، صادرات `MIMO.contentEngine`/`contentStats()` |
| `content-engine.js` | ★ پارسر DSL، ۹ interaction، ولیدیتور A6–A11، `LessonProgress` ۱۱فیلدی، صف مرور غلطها |
| `content-package.js` | ★ تولیدی: `STRUCTURED_PACKAGE` تزریقشده (دستکاری نشود) |
| `starter-package.js` | تولیدی: بستهٔ آغازین ۲۰ سؤال (`placeholder`) |
| `templates.js` | تولیدی: `EXAM_TEMPLATE` / `PRACTICE_TEMPLATE` |
| `design-tokens.js` | تولیدی: توکنهای CSS استخراجشده از `proto.css` |
| `pwa-assets.js` | تولیدی: آیکونها از وکتور مصوب |
| `app.js` | کنترلر فاز اول (سه مسیر، چرخهٔ حیات) — محصول فعلی از `native.js` استفاده میکند |
| `views.js` | صفحات الحاقی فاز اول (تزریق رانتایم، مارکاپ مصوب دستنخورده) |
| `routes.js` | انتقال حالت خالص سه مسیر + ماشینStudy Plan |
| `engine.js` | منطق خالص بدون DOM (فرمولهای M09 + قواعد محلی) |
| `store.js` | `localStorage` نسخهدار، DOM-free، تزریقپذیر. **`get()` فقط یک آرگومان میگیرد** |
| `nodes.js` | گرههای دیتامحور منطبق بر اپ اصلی (فاز ۲) |
| `fixtures.js` | دادهٔ تستی placeholder، جدای از اسکیمای محتوا |
| `learning-path.js` | مسیر آموزشی ۱۲ درس / ۶۰ فصل / ۱۸۰ درس از `KONKUR` — **ساختگی، R10** |
| `exam-template.js` | سازندهٔ آزمون/تمرین قالبمحور — **placeholder، R9** |
| `harness.js` | LearnHarness محلی چهارفاز، `generatesText:false`, `EXTERNAL_PROVIDER_CONTRACT` |
| `ai-studio.js` | استودیوی محلی AI (بدون LLM)، هزینه `۰٫۰۰ دلار` |
| `token-economy.js` | اقتصاد محلی (`DAILY_XP_CAP=400`، ۶ نوع، ۱۲ قاعده) |
| `output-kit.js` | خروجی دروناپ؛ `SOURCE_SLOT='__MIMO'+'_SOURCE_B64_SLOT__'` |
| `plus.js` | لایهٔ صفحات «مسیر/توکنها/AI/خروجی» فاز اول |
| `util.js` | کمکهایBlob/ZIP محلی، بدون شبکه |

## `app/tools/` — ۱۵ اسکریپت پایتون (بدون وابستگی)

| فایل | نقش |
|---|---|
| `build_output.py` | ★ بیلدر ۱۵ ماژول → `dist/Mimo.html`, `index.html`, ZIP, manifest |
| `emit_structured_package.py` | ★ `STRUCTURED_PACKAGE.json` + `content-package.js` |
| `process_book.py` | ★ بازسازی خط از word boxes → پیشنویس `unreviewed` (خارج از گیت) |
| `validate_content.py` | ولیدیتور بدون وابستگی فرم اطلاعاتی |
| `verify_app.py` | ۵۴ بررسی یکپارچگی (هش داراییها، ۵ تب، …) |
| `verify_output.py` | ۵۱ بررسی خروجی بومی + لایهٔ محتوا |
| `build_index.py` | ساخت `app/index.html` خودکفا (فاز اول) |
| `extract_from_prototype.py` | کپی بایتبهبایت داراییهای مصوب |
| `emit_design_tokens.py`, `emit_icons.py`, `emit_templates.py`, `emit_starter_package.py` | ژنراتورهای فایلهای `GENERATED` |
| `ocr_book.py` | OCR کامل ۸۴۸ صفحه (انجام شده؛ دوباره اجرا نکن) |
| `analyze_mimo_lessons.py` | استخراج پداگوژی از ۱۰٬۲۹۸ فایل درسنامه |
| `structure_book.py` | روش قدیمی دوتستونی، ۵۶۵ کاندیدای `correctIndex:null` — **کنارگذاشتهشده** |

## `app/` سایر فایلها

| مسیر | نقش |
|---|---|
| `app/native/index.html` | ★ پوستهٔ بومی فعلی (تمام صفحات ناوبری + بلوکهای درس) |
| `app/index.html` | نسخهٔ توسعهای فاز اول (چندفایلهای، ESM؛ `file://` کار نمیکند) |
| `app/assets/phone.html` | کپی بایتبهبایت پروتوتایپ مصوب؛ شامل متن دموی چیدمان بهعنوان شاهد تاریخی |
| `app/assets/proto.css` / `proto-data.js` / `proto-ui.js` | کپیهای بایتبهبایت؛ `verify_app.py` هششان را چک میکند |
| `app/assets/native.css` | تنها CSS تازه؛ توکنهای افتاده بیرون `:root` و استایل بلوکهای درس |
| `app/assets/motion.css`, `node-match.css`, `PROVENANCE.json` | الحاقیهها و هشهای فاز اول/دوم |
| `app/server.js` | سرور استاتیک بدون وابستگی، `0.0.0.0` |
| `app/package.json` | `start`, `test` (node --test), `verify` (دو ورایفایر), `build:output` |
| `app/manifest.webmanifest`, `app/sw.js` | PWA فاز اول؛ `app/dist/sw.js` نسخهٔ خروجی (`mimo-native-v4`) |
| `app/tests/` (۶) | `harness.mjs` + تستهای واحد/پذیرش/خروجی/محتوا |
| `app/docs/` (۷) | `MIMO_CONTENT_MODEL.md`★, `MIMO_NATIVE_NAVIGATION.md`★, `OUTPUT_GUIDE.md`★, `TESTING.md`★, `ARCHITECTURE.md`, `DEVELOPMENT.md`, `INTEGRATIONS.md` |
| `app/content/` (۱۰ tracked) | قرارداد + `STRUCTURED_PACKAGE.json`★ + `STARTER_PACKAGE.json` + قالبها + `PEDAGOGY*` |
| `app/content/source/` (۱٬۷۰۱، gitignored) | صفحات OCR، word boxes، `PROCESSED_DRAFT.json`, `PROCESS_REPORT.json` |
| `app/dist/` (۱۲، تولیدی) | `Mimo.html`★, `index.html`, `launcher.html`, `Mimo.zip`, `START_HERE.txt`, `README-fa.md`, `BUILD_MANIFEST.json`, `manifest.webmanifest`, `sw.js`, `icons/*` |
| `app/*.md` | `README.md` (فاز اول، بنر بهروزشده), `OUTPUT_REPORT.md` (گزارش ردشده + سربرگ تازه), `APP_FINAL_REPORT.md`, `PHASE_2_REPORT.md`, `TESTING.md` |

## `ANALYSIS/MISSION_09/` — ۱۹ تحویلی نهایی

`COMPLETE_*` (معماری، شبکه/API، احراز هویت/چرخهٔ حیات، اقتصاد، حالت یادگیرنده،
موتور درس، پیشرفت، کاتالوگ رندررها، بلوپرینت پیادهسازی، گراف درسنامه،
ماشین ناوبری، timeline، system map، evidence database، coverage/test matrix)
+ `FINAL_UNKNOWN_REGISTER.md` ★ + `MISSION_09_FINAL_REPORT.md` +
`MISSION_09_REPRODUCTION_GUIDE.md`.

## `mimo-ui/UPGRADE/` — ۲۵ سند بایگانی

`README.md`, `00_START_HERE.md` (بنرهای متناقض superseded), `01…12` قراردادها و
تحلیلها، `13…24` دورهای طراحی تا v12، `CATALOGS/` (۲۴ CSV/JSON)،
`DESIGN/index.html` ★ تنها فایل **حکم** در این پوشه (v12.5-fa).

## خارج از گیت (اما برای بازتولید لازم)

`google_drive/*` (APKها و PDF)، `/home/user/_work/_analysis/mimo_assets/` (داراییهای
دیکدشده)، `/home/user/_work/ocr_venv/` (Tesseract)، `/home/user/_work/shots/`
(اسکرینشات مرورگر). فهرست کامل ← `06_EVIDENCE_INDEX.md`.

---

قبلی: [`09_COMMIT_LOG.md`](09_COMMIT_LOG.md) · ایندکس: [`../REPO_INDEX.json`](../REPO_INDEX.json)
