# شواهد و ماتریس یادگیری — هر ادعا از کجا آمده

> ⚠️ **بایگانی / superseded:** این سند مربوط به دورهای قبل است. طراحی فعلی **[DESIGN v6](17_DESIGN_ROUND_6.md)** است؛ صفحهٔ ورود حذف، یادگیری بازسازی و زیرصفحات «انتخاب مسیر / نمای مسیر / داخل مبحث» از کد اضافه شدند. لاگهای قدیمی صرفاً ردپای حسابرسیاند.

> 🔄 **DESIGN v5 (حکم فعلی) — بازآفرینی ۱۰۰٪ از داخل کد:** لاگ کامل ← `16_DESIGN_ROUND_5.md`، prototype ← `DESIGN/index.html`، هندسهٔ استخراجشده ← `DESIGN/CODE_GEOMETRY.json`.
> اصلاحیهٔ نامگذاری: دکمهٔ قدیمی «پاسخنامه» = **«پاسخبرگ»** (گزینههای زدهشده)؛ «پاسخنامه» دکمهای **جداگانه** برای جواب تشریحی/توضیحات است. یک دکمهٔ «توضیح با هوش مصنوعی» در صفحهٔ سؤالات + همان دکمه در صفحۀ آخر آزمون. لیدربورد اطلاعات/امتیازات/آزمونهای خود فرد را نشان میدهد. متن پایینتر، بایگانی دور قبل است و فقط برای ردیابی نگه داشته شده.


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
| ۴ تب واقعی میمو (**شاهد بایگانی**؛ طرح محصول v4 = ۵ تب) | `mimo-ui/SOURCE/res/menu/bottom_navigation_menu.xml` + `navigation_*` strings | `VERIFIED_STATIC` | `02`, `08`, `10`, `15` |
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
| رگرسیون پنجتب پیشین | `/home/user/_work/prev/mimo/shell/app.js` | `VERIFIED_STATIC` | `02`, `10` |
| کنترلهای واقعی LH (TEACH/PRACTICE, Chains, Import notes, Dictate, Model, medium, Cost, Sessions, Knowledge graph, Background agents, Settings) | اسکرینشات پیوستشدهٔ کاربر + کامپوننتهای کلونشدهٔ LH | `VERIFIED_STATIC` | `04`, `DESIGN/index.html`, `LEARNHARNESS_ACTIONS.csv` |
| پنل اصلی LH (Knowledge graph / What do you want to learn? / TEACH-PRACTICE / Dictate / model / medium / Cost) | اسکرینشات دوم پیوستشدهٔ کاربر (`DESIGN/REFERENCE/learnharness-main-panel-user-screenshot.png`, SHA `514a6167…890e6`) | `VERIFIED_STATIC` | `14_DESIGN_ROUND_3.md`, `AI_PANEL_SPEC.csv` |
| چت + تاریخچه + پاسخ جریانی EPM | `frontend/src/views/ChatView.vue`, `frontend/src/components/AiAssistant.vue`, README feature table | `VERIFIED_STATIC` | `04` §۴٫۲, `DESIGN/index.html`, `EPM_MINOR_OPTIONS.csv` |
| ۳ آپشن جزیی آزمون (shuffle / unanswered / redo-wrong-only) | README ریپوی EPM | `VERIFIED_STATIC` | `EPM_MINOR_OPTIONS.csv`, `14_DESIGN_ROUND_3.md` §۴ |
| دکمههای پنل اصلی LH (composer + topbar) | `DESIGN/REFERENCE/lh-composer-user-screenshot.png` (SHA `3b37831a…`), `lh-topbar-user-screenshot.png` (SHA `0bd72dae…`) | `VERIFIED_STATIC` | `04` §۴٫۴, `AI_PANEL_SPEC.csv` |
| پاسخنامهٔ تستی/تشریحی + تحلیل | همدرس («پاسخ تشریحی», «تعویض سوال», «تعداد غلط», `AnalyisByLessonsScreenWidget`) + EPM (`WrongView`, `answer key`) | `VERIFIED_STATIC` | `03` §۴٫۱, `EXAM_TYPES.csv` |
| ۷ بخش لیبلدار / فیلد قالب / زمان ثابت جامع | بازخورد v4 + `CATALOGS/EXAM_SECTION_TEMPLATES.csv` | `VERIFIED_STATIC` | `15_DESIGN_ROUND_4.md` §۴ |
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
