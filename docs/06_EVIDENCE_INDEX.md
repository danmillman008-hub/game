# ۶ · ایندکس شواهد (هر ادعا از کجا میآید)

## واژگان اعتبار (`FINAL_UNKNOWN_REGISTER.md`)

`VERIFIED_STATIC` (DEX/منیفست، اجرا نشده) · `VERIFIED_RUNTIME` (دیدهشده در اجرا) ·
`VERIFIED_ASSET` (داراییهای shipped APK) · `VERIFIED_DATABASE` ·
`VERIFIED_NETWORK_OBSERVATION` · `INFERRED` · `UNKNOWN` · `SERVER_DEPENDENT`.
**`SERVER CONFIRMED = 0` بر تمام گزارشها حاکم است.**

## الف) واقعیت میمو ۹٫۳۵

| ادعا | سند |
|---|---|
| APK هدف `com.getmimo` 9.35، `versionCode=1792759685`، ۱۴۲٬۳۵۳٬۴۹۹ B، SHA `48ce1740aa…` | `ANALYSIS/MISSION_09/FINAL_UNKNOWN_REGISTER.md` سربرگ |
| معماری کلی، ۱۲ DEX، کامپوننتها، Coroutineها | `ANALYSIS/COMPLETE_SYSTEM_ARCHITECTURE.fa.md`, `COMPLETE_COMPONENT_GRAPH.json`, `DEX_INVENTORY.json`, `COROUTINE_STATE_MACHINES.json` |
| افعال HTTP و ۵۳ endpoint استاتیک | `ANALYSIS/HTTP_VERBS_RESOLVED.json`, `MIMO_RETROFIT_ENDPOINTS.json`, `MIMO_API_SURFACE.json`, `MISSION_09/COMPLETE_NETWORK_API_CONTRACT.md` |
| ماشین حالت ناوبری، ۴ مسیر تب، ۴۶ صفحه / ۴۵ یال | `ANALYSIS/MISSION_09/COMPLETE_NAVIGATION_STATE_MACHINE.json`, `MISSION_08` هفت گزارش اصلی |
| گراف درسنامه: ۱۰ لوکال / ۱۹ track / ۱۴۴ section / ۱٬۰۲۹ tutorial / ۱٬۹۴۷ chapter / ۳۷٬۱۸۳ placement / ۱۸٬۲۷۲ ریزدرس یکتا / ۱۰٬۲۹۸ فایل معتبر | `ANALYSIS/MISSION_09/COMPLETE_CURRICULUM_GRAPH.json`, `COMPLETE_PROGRESSION_ENGINE_SPEC.md` |
| DSL درس، رندررها، A6–A11، `isSolvedCorrectly≡tries>=1`، جایگذاری رندررها | `ANALYSIS/MISSION_09/COMPLETE_LESSON_ENGINE_SPEC.md`, `COMPLETE_UI_RENDERER_CATALOG.md`, `COMPLETE_ECONOMY_SPEC.md` |
| پداگوژی: ۹٫۳۸ ریزدرس/فصل، میانگین ۲۱٫۲ کلمه، چرخهٔ HOOK→…→RECOVERY | `app/content/PEDAGOGY.md`, `PEDAGOGY_STATS.json` |
| ردیف `LessonProgress` / `DELETE … WHERE in_queue=1` | `MISSION_09/COMPLETE_LEARNER_STATE_SPEC.md`, `COMPLETE_EVIDENCE_DATABASE.json`, `COMPLETE_RUNTIME_TIMELINE.jsonl` |
| تنها رفتار اندازهگیریشدهٔ پاسخ (Q→Try again / D→Correct!) | `ANALYSIS/RUNTIME/MISSION_07/`, `MISSION_09/COMPLETE_LESSON_ENGINE_SPEC.md` |
| شکافهای باز و شرط بستنشان | `ANALYSIS/MISSION_09/FINAL_UNKNOWN_REGISTER.md` ★ |

**ابزار/خام:** `ANALYSIS/DECOMPILED/` (JADX)، `GHIDRA/`، `RUNTIME/` (اسکرینشات،
UI hierarchy، لاگها، DB)، `_INPUT/`، `_TOOLCHAIN/`، `.github/workflows/*`.

## ب) طرح تأییدشدهٔ کاربر (v12.5-fa)

| ادعا | سند |
|---|---|
| قرارداد وفاداری UI، یادداشتها، ۵ تب، ۳ چیپ، بدون تب مکس | `mimo-ui/UPGRADE/02_UI_FIDELITY_CONTRACT.md`, `CATALOGS/UI_FIDELITY_RULES.csv`, `FEATURE_MAP.csv`, `SCOPE_DECISIONS.csv` |
| هاب ۷بخشی، تایمر ۲۷۰ دقیقه، پاسخبرگ/پاسخنامه، ۳ مسیر خروج | `mimo-ui/UPGRADE/03_EXAM_HUB.md`, `CATALOGS/EXAM_SECTION_TEMPLATES.csv`, `ANSWER_SHEET_POLICY.csv`, `EXAM_TYPES.csv` |
| هوش مصنوعی محلی LearnHarness (۲۹ اکشن بکند) | `mimo-ui/UPGRADE/04_AI_LEARN_HARNESS.md`, `CATALOGS/LEARNHARNESS_ACTIONS.csv`, `AI_PANEL_SPEC.csv` |
| نقشهٔ گرهها و توکنهای ابعاد | `CATALOGS/MIMO_PATH_NODES.csv`, `MIMO_CODE_GEOMETRY.csv`, `MIMO_LEARN_SUBSCREENS.csv` |
| پلن ۸ فاز و تصمیمات دورها | `mimo-ui/UPGRADE/10_PHASED_ROADMAP.md`, `13…24_DESIGN_ROUND_*.md`, `DESIGN_FEEDBACK.csv`, `KONKUR_CURRICULUM.csv` |
| **پروتوتایپ مصوب** (تمام صفحات، `data-code`/`data-lh`) | `mimo-ui/UPGRADE/DESIGN/index.html` — SHA `c356068daa5ccafbee46599897ad18bdf1e4f91f1ca23f36b1b8bd153dbfdb78` |
| یکپارچگی فایلها | `CATALOGS/SHA256SUMS.txt`, `VERIFICATION_REPORT.json`, `EVIDENCE_LEDGER.csv/.json` |
| استخراج ۰–۱۰۰ UI (مرجع مستقل) | `mimo-ui/00…14_*.md`, `ATLAS/`, `SCREENS/`, `RECONSTRUCTION/`, `REFERENCE/`, `SOURCE/` |

> ⚠️ `mimo-ui/UPGRADE/00_START_HERE.md` و `README.md` بنرها و «حکم فعلی»ای
> مربوط به دورهای قدیمی دارند (مثلاً «حکم فعلی = DESIGN v4»). **بایگانیاند**؛
> حکم محصول امروز `app/dist/Mimo.html` است. `01_CHRONOLOGY.md` ترتیب دورها را
> نشان میدهد.

## ج) اپ / محصول

| ادعا | سند |
|---|---|
| قرارداد ورود محتوا (اسکیما، enumها، `trace.sourceRef`, `reviewStatus`) | `app/content/MIMO_INFORMATION_FORM.json`, `MIMO_INFORMATION_FORM.md` |
| تشخیص ریشهٔ ایراد درسنامه و مدل اندازهگیریشدهٔ میمو | **`app/docs/MIMO_CONTENT_MODEL.md`** ★ |
| ناوبری بومی و یادداشتهای v12.5-fa در پیادهسازی | `app/docs/MIMO_NATIVE_NAVIGATION.md` ★ |
| خروجی تکفایل / PWA / ZIP و نحوهٔ استفاده | `app/docs/OUTPUT_GUIDE.md`, `app/dist/START_HERE.txt`, `app/dist/README-fa.md` |
| تستها و اعداد بررسی | `app/docs/TESTING.md`, `app/TESTING.md`, `app/tests/*.test.mjs` |
| پرچمها، هشها، فهرست ۱۵ ماژول | `app/dist/BUILD_MANIFEST.json` |
| بستهٔ محتوای فعلی (۱/۴/۲۰/۲۰/۱۲۰/۱۶۰/۲۰) | `app/content/STRUCTURED_PACKAGE.json` |
| پیشنویس کتاب (خارج از گیت، `unreviewed`) | `app/content/source/biology-12/PROCESSED_DRAFT.json`, `PROCESS_REPORT.json` |
| حسابرسی API هدفپلاس / «شرکت یارانی» | `ANALYSIS/HADAF_PLUS_AI_API_AUDIT.md` ★ |

## د) منابع بیرونی (gitignored — داخل ریپو نیستند)

| مسیر | نقش |
|---|---|
| `google_drive/Mimo_9.35 (1).zip/.z01/.z02` | APK اصلی ( splitsشده؛ مستقیم `unzip` نکن ) |
| `google_drive/@BankBookkonkor (26)_extract.pdf` | PDF بازسازیشدهٔ کتاب زیست (۸۴۸ صفحه) |
| `google_drive/Hadaf Plus_2.0.2.apk` | SHA `b282f578…`، ۵۹٬۴۰۳٬۴۷۷ B، هدف حسابرسی API |
| `google_drive/همدرس_7.4.4.apk` | مرجع مشاورهٔ تحصیلی (PARKED) |
| `/home/user/_work/_analysis/mimo_assets/assets/lessons-*/tracks/tutorial-*.json` | داراییهای دیکدشدهٔ APK (۱۰٬۲۹۸ فایل)، خارج از گیت |
| `/home/user/_work/shots/*.png` | ۴۰+ اسکرینشات مرورگر واقعی، خارج از گیت |
| `/home/user/_work/ocr_venv/` | محیط Tesseract/Pillow |

## ه) قاعدهٔ طلایی

> استاتیک ≠ رانتایم ≠ سرور. اگر سندی `VERIFIED_STATIC` است، هرگز در پاسخ
> ننویس «سرور اینطور رفتار میکند». `INFERRED` و `UNKNOWN` را همانطور بنویس.
> فهرست کامل شکافها: `ANALYSIS/MISSION_09/FINAL_UNKNOWN_REGISTER.md`.

بعدی: [`07_GLOSSARY.md`](07_GLOSSARY.md)
