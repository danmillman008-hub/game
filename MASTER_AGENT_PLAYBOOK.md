# نقشه گمشده گنج: سند جامع معماری نرم‌افزار و پلی‌بوک گام‌به‌گام ایجنت خودران
## پروژه: پلتفرم کنکور-میمو × لرن‌هارنس (`danmillman008-hub/game.git`)

> **نحوه استفاده برای کارفرما (بدون نیاز به هیچ دانش برنامه‌نویسی یا جهت‌دهی دستی):**
> این سند حاصل کالبدشکافی خط‌به‌خط تمام شاخه‌ها (`origin/arena/aebb90b7-game` و `origin/arena/ecb8af07-game`) و ۵ آرشیو کد ریپوی `https://github.com/danmillman008-hub/game.git` است.
> شما فقط کافی است این فایل را به عنوان `CLAUDE.md` یا `AGENTS.md` در ریشه پروژه قرار دهید و از **فاز ۰ تا فاز ۱۱**، پرامپت هر فاز را به ایجنت کدنویس (Claude Code / Cursor / Windsurf / Codex) بدهید. ایجنت موظف است در پایان هر فاز، دستورات `Verification Gate` را اجرا کند و تا وقتی ۱۰۰٪ تست‌ها سبز نشده‌اند به فاز بعدی نرود.

---

## ۱. کالبدشکافی دقیق ریپوی `danmillman008-hub/game.git` (کجا متوقف شدیم و چرا طرح «فرانکنشتاینی» شده بود؟)

### ۱.۱ فایل‌ها و شاخه‌های نامرتبط که ایجنت باید ۱۰۰٪ نادیده بگیرد (Quarantined / Ignored)
طبق دستور صریح شما، موارد زیر هیچ ارتباطی به پروژه میموی کنکور ندارند و در فاز ۰ قرنطینه می‌شوند:
1. **پروژه داروسازی و سامانه تیتک:** فایل‌های `ttac-4.3.6.apk` و `pharmacy-inventory (3).html` در ریشه ریپو و کل شاخه `origin/arena/dd2b6beb-game`.
2. **پروژه بازی سگا (Streets of Rage):** فایل `Streets-of-Rage_Genesis_EN.zip` و شاخه‌های `origin/arena/eb3b2453-game`، `f84369df-game` و `e3952d18-game`.

### ۱.۲ قطعات طلایی پازل شما در ریپو که تا امروز به هم بافته نشده بودند
چرا تلاش‌های قبلی به نتیجه نهایی نرسیدند؟ چون کارهای فوق‌العاده‌ای که انجام شده بود در **۲ شاخه مجزا و ۵ آرشیو زیپ** پخش شده بودند و هر کدام یک تکه از حقیقت را داشتند:

| منبع در ریپوی `game.git` | چه چیزی داخلش ساخته شده و آماده است؟ | چه چیزی در آن ناقص مانده بود؟ |
|---|---|---|
| **شاخه `origin/arena/ecb8af07-game`** (`HANDOFF/01..15` و `mimo-re/`) | مهندسی معکوس بایت‌به‌بایت کدهای Kotlin و ۱۳ فایل DEX اپ Mimo 9.35 (`com.getmimo`, SHA `48ce1740…`): گرامر رسمی EBNF زبان درسنامه (`dsl_grammar.ebnf` با ۲۷ تگ)، الگوریتم دقیق نرمال‌ساز و تصحیح‌گر (`qm.i.a` + ۵۴ تست `grading_vectors.json`)، اسکیمای دیتابیس SQLite Room v2 (`mimo.db` با ۳ جدول `lesson_progress`, `tutorial_completions`, `chapter_completions`)، و ۴۵ تصمیم معماری (`D-01..D-45` و `ADD-01..ADD-08`). | ۱) نرمال‌ساز `qm.i.a` برای انگلیسی بود و حروف فارسی (`ی/ي`، `ک/ك`، نیم‌فاصله ZWNJ و اعداد فارسی) را یکسان نمی‌کرد (`Q-44`). ۲) هیچ اتصالی به UI کنکوری `v12.5-fa` و کتاب زیست نداشت. |
| **شاخه `origin/arena/aebb90b7-game`** (`mimo-ui/`, `ANALYSIS/MISSION_05..09`, `app/`, `docs/00..10`) | ۱) پروتوتایپ مصوب `v12.5-fa` (`mimo-ui/UPGRADE/DESIGN/index.html` با SHA `c356068d…`) و قوانین `F2, F10–F47` (۵ تب فارسی، ۳ چیپ، گره‌های ۹۲dp با قوس Q، هاب آزمون ۷بخشی). ۲) ناوبری بومی M09 در `app/src/native.js`. ۳) OCR کامل ۸۴۸ صفحه کتاب زیست دوازدهم (`694,860` جعبه کلمه و `775` پاسخنامه در `process_book.py`). ۴) بسته `STRUCTURED_PACKAGE.json` (۱۲۰ ریزدرس ۶ نقشی). | ۱) `R1`: پیش‌نویس OCR کتاب هنوز غلط‌های املایی (`«یافته»←«یاخته»`) و تداخل دو ستون دارد و `unreviewed` است. ۲) `R2`: تابع `chapterRefFor()` هنوز هش‌پایه است. ۳) `R4–R6`: ۴ خانواده رندرر (`validatedInput`, `InteractiveWebView`, `Reveal`, `executableFiles`) ناقص‌اند. ۴) `R9`: بانک آزمون `QBANK` فقط ۲۰ سوال نمونه است. ۵) `R12`: ماژول `LearnHarness` (`harness.js`) بدون گراف گزاره‌های کتاب استاب شده است. |
| **آرشیو `build-konkur-pedagogical-ai-agent.zip`** (`pedagogy-engine.ts`) | کشف و حل بزرگ‌ترین حلقه مفقوده آموزشی بین میمو و کنکور: تبدیل گام کدنویسی میمو (`code`) به مکانیک‌های کنکوری `token_assembly` (چیدمان بلوکی مسیرهای زیستی/فرمولی با بلوک تله) و `trap_detector` (دیباگر گزاره کنکوری)، تبدیل `fill` به `guided_cloze` روی قیدهای کنکور (`همه/برخی/اغلب/به‌جز`)، و ۱۰ گاردریل الگوریتمی `M1–M10`. | خروجی این کامپایلر به فرمت `STRUCTURED_PACKAGE.json` و ۲۷ تگ DSL میمو متصل نشده بود. |
| **آرشیو `comprehensive-software-development-roadmap.zip`** (`algorithms.ts`) | پیاده‌سازی کامل ریاضیات Knowledge Space Theory (`KST Outer Fringe`)، مدل تسلط `Calibrated BKT` (تفکیک پاسخ مستقل `unaided` از پاسخ با راهنمایی `aided`)، الگوریتم مرور فاصله‌دار `FSRS-5` و کنترلر باند جریان `70%–85%`. | به جداول ۱۱ فیلدی `LessonProgress` میمو و پوسته بومی M09 در `app/` متصل نشده بود. |

---

## ۲. شش علت ریشه‌ای که باعث شد پروتوتایپ قبلی «فرانکنشتاینی» به نظر برسد

1. **توهم درسنامه از روی متن تست فونت (`phone.html`):** در پروتوتایپ `v12.5-fa`، صفحه `lesson` حاوی جمله «گاهی لازم است متن‌ها را با شکستن خطوط، خواناتر کنیم…» بود که طراح صرفاً برای تست چیدمان خط فارسی گذاشته بود! بیلد اولیه همان را به عنوان درس زیست نشان می‌داد و با هش کردن ID درس، یک سوال تصادفی از `QBANK` به ته آن می‌چسباند.
2. **تداخل ستون‌های دوتایی کتاب زیست در OCR:** کتاب‌های کمک‌درسی کنکور دو ستونی (راست به چپ) هستند. اسکریپت اولیه `structure_book.py` سطرها را افقی از راست به چپ کل صفحه می‌خواند و ستون راست و چپ را قاطی می‌کرد (`565` سوال ناقص با `correctIndex: null`). راه حل قطعی در فاز ۵: تفکیک جعبه‌های کلمات (`word boxes`) بر اساس `x >= page_width / 2` (ستون راست) و `x < page_width / 2` (ستون چپ) و اتصال به ۷۷۵ کلید پاسخنامه انتهای کتاب.
3. **حذف شدن مکانیک ساختن کد (`<code>`) در переход از پایتون به کنکور:** راز جذابیت میمو این است که کاربر هر ۱۵ ثانیه یک بلوک کد را می‌سازد یا دیباگ می‌کند. وقتی موضوع کنکور شد، ایجنت‌ها گام `code` را حذف کردند و اپ تبدیل به تست چهارگزینه‌ای خشک شد. راه حل قطعی در فاز ۴: هم‌ریختی پداگوژیک (`token_assembly` و `trap_detector` و `guided_cloze` روی قیدهای کنکور).
4. **خلأ سرور میمو (`SERVER CONFIRMED = 0`):** در اپ اصلی میمو، کلاینت هرگز اتمام فصل یا باز شدن قفل را حساب نمی‌کند و رکوردهای `lesson_progress` را بعد از آپلود `DELETE` می‌کند (`05_SPEC_LEARNER_MODEL.md`). راه حل قطعی در فاز ۱ و ۶: اعمال قوانین `ADD-03` (نگهداری تاریخچه به صورت Append-Only) و `ADD-04` (تکمیل محلی فصل به شرط `tries >= 1` برای تمام ریزدرس‌های فصل).
5. **عدم اتصال `LearnHarness` به گراف گزاره‌های کتاب و گیت‌وی سرور:** تب هوش مصنوعی (`amosblomqvist/learnharness`) نیازمند گراف گزاره‌های کتاب (`Principle i: Unconditional Truth` و `Principle ii: Motivated Discovery`) در حالت آفلاین و یک پروکسی استریم SSE در سمت سرور (`/api/v1/ai/harness` مشابه معماری کشف‌شده در `HADAF_PLUS_AI_API_AUDIT.md`) در حالت آنلاین است.
6. **نگاشت هش‌پایه `chapterRefFor()`:** انتخاب درسنامه با تابع هش به جای جدول صریح `curriculumId`.

---

## ۳. تصمیم معماری نرم‌افزار: کاتلین (Kotlin) یا وب/PWA و نحوه اتصال بک‌اند؟

بر اساس کالبدشکافی بایت‌کد میمو ۹٫۳۵ در `HANDOFF/01_WHAT_MIMO_IS.md` و `app/docs/ARCHITECTURE.md`:
- **حقیقت فنی میمو ۹٫۳۵:** در اپ اصلی میمو، پوسته بیرونی با Kotlin/Compose و دیتابیس با Room SQLite v2 (`mimo.db`) نوشته شده، اما **تمامی ۱۸٬۲۷۲ درسنامه به زبان HTML-DSL (`<!DOCTYPE html><html><body>...`) هستند**!
- **معماری طلایی ۳ لایه (Isomorphic Offline-First + Hybrid Kotlin/PWA + PostgreSQL Gateway):**
  1. **لایه ۱ — هسته خالص دامنه (Pure Isomorphic Core در TypeScript/ESM):** بدون هیچ وابستگی به DOM یا فریم‌ورک؛ شامل پارسر ۲۷ تگ EBNF، نرمال‌ساز `qm.i.a` + فارسی، ماشین ۱۱ فیلدی `LessonProgress`، موتور `LearnHarness` و الگوریتم‌های `KST + BKT + FSRS-5`.
  2. **لایه ۲ — کلاینت چندپلتفرمی (Multi-Target Client):**
     - **خروجی ۱ (فایل تک‌کلیکه آفلاین `app/dist/Mimo.html` و PWA قابل نصب):** بدون نیاز به هیچ سرور یا اینترنتی روی موبایل و دسکتاپ کار می‌کند.
     - **خروجی ۲ (اپلیکیشن اندروید بومی APK):** بسته‌بندی همان هسته و پوسته بومی `v12.5-fa` در قالب Android Kotlin WebView / Capacitor متصل به SQLite Room v2 (`mimo.db` با همان ۳ جدول استاندارد `lesson_progress`, `tutorial_completions`, `chapter_completions`).
  3. **لایه ۳ — بک‌اند و گیت‌وی هوش مصنوعی (Next.js App Router / FastAPI + PostgreSQL Drizzle ORM):**
     - اندپوینت `POST /api/v1/tutorials/[tutorialId]/progress`: دریافت صف `in_queue = 1` از کلاینت‌ها و ذخیره در PostgreSQL.
     - اندپوینت `POST /api/v1/ai/harness`: پروکسی امن Server-Sent Events (SSE) که کلید LLM را در متغیر محیطی سرور (`process.env`) نگه می‌دارد و فازهای `Probe → Plan → Teach → Practice` لرن‌هارنس را روی گراف گزاره‌های کتاب اجرا می‌کند.
     - اندپوینت `POST /api/blueprint/compile-lesson`: خط لوله تبدیل متون و کتاب‌های جدید کنکور به بسته ساختاریافته `STRUCTURED_PACKAGE.json`.

---

## ۴. جدول ریپوزیتوری‌ها و ابزارهای مورد نیاز از اینترنت

| ردیف | نام ابزار / ریپو | آدرس رسمی | کاربرد دقیق در پروژه |
|---|---|---|---|
| ۱ | **LearnHarness** | `https://github.com/amosblomqvist/learnharness` | موتور ۴ فازی هوش مصنوعی (`Measure → Plan → Teach → Practice`)، اصول بدیهی اول و دوم، ضریب اطمینان و گراف گزاره‌ها (`app/src/harness.js`). |
| ۲ | **Gramophone (KST)** | `https://github.com/danmillman008-hub/newlearning` | الگوریتم‌های نظریه فضای دانش (`Outer Fringe`)، حذف دور گراف پیشنیاز (`surmise.py`) و کنترلر باند جریان ۷۰ تا ۸۵ درصد (`adapt.py`). |
| ۳ | **TS-FSRS (FSRS v5)** | `https://github.com/open-spaced-repetition/ts-fsrs` | زمان‌بندی علمی مرور فاصله‌دار برای صف مرور غلط‌ها (`inQueue`) تا روز کنکور. |
| ۴ | **Tesseract 5.5 (`fas`) / MinerU** | `https://github.com/opendatalab/MinerU` | استخراج متن و جعبه‌های کلمات (`word bounding boxes`) از PDF دو ستونی کتاب‌های کنکور (`app/tools/ocr_book.py`). |
| ۵ | **KaTeX + Mermaid** | `https://github.com/KaTeX/KaTeX` | رندر آفلاین تگ‌های علمی `<math>` (فرمول‌های فیزیک/شیمی/ریاضی) و `<diagram>` (درخت پیشنیاز و فلوچارت‌های زیستی). |
| ۶ | **Drizzle ORM + PostgreSQL** | `https://github.com/drizzle-team/drizzle-orm` | دیتابیس سرور، لاگ‌های Append-Only یادگیری و سینک دوطرفه جداول Room میمو. |

---

## ۵. نقشه راه اجرایی ۱۲ فازی وزن‌دار (مجموع وزن = ۱۰۰٪)

1. **فاز ۰ (وزن ۵٪):** یکپارچه‌سازی شاخه‌های `aebb90b7-game` و `ecb8af07-game` (`HANDOFF/`) و قرنطینه کامل فایل‌های داروخانه (`ttac-4.3.6.apk`, `pharmacy-inventory.html`) و بازی سگا.
2. **فاز ۱ (وزن ۸٪):** بستن مهندسی معکوس میمو ۹٫۳۵، پیاده‌سازی نرمال‌ساز `qm.i.a` + لایه فارسی (`Q-44`)، قوانین تکمیل محلی `ADD-03` و `ADD-04`، و پل محلی WebView (`U-WEB-001`).
3. **فاز ۲ (وزن ۸٪):** تثبیت معماری ۳ لایه (Core Engine بدون DOM + پوسته `v12.5-fa` + دیتابیس PostgreSQL/Room v2).
4. **فاز ۳ (وزن ۱۰٪):** تکمیل پارسر ۲۷ تگ EBNF و پیاده‌سازی هر ۹ خانواده رندرر (شامل `validatedInput` با حکم سه‌حالته `PARTIAL`, `InteractiveWebView`, `Reveal`, `executableFiles`) و دروازه `visible-if`.
5. **فاز ۴ (وزن ۱۲٪):** اعمال هم‌ریختی پداگوژیک میمو به کنکور (`concept_bite`, `guided_cloze` روی قیدهای کنکور، `token_assembly`, `trap_detector`, `konkur_test`) و گاردریل‌های ۱۰گانه `M1–M10`.
6. **فاز ۵ (وزن ۱۴٪):** اجرای خط لوله ۶ مرحله‌ای وارد کردن کتاب درسی (`R1` و `R2`): تفکیک دو ستون راست/چپ از روی `word boxes`، دیکشنری اصلاح OCR زیست، اتصال ۷۷۵ پاسخنامه تشریحی، ارتقای `STRUCTURED_PACKAGE.json` به `reviewStatus: 'approved'` و حذف هش از `chapterRefFor()`.
7. **فاز ۶ (وزن ۹٪):** پیاده‌سازی کامل ردیف ۱۱ فیلدی `LessonProgress`، پایدارسازی صف مرور غلط‌ها بین نشست‌ها در `localStorage` (`R8`) و تفکیک پاسخ مستقل (`unaided`) از پاسخ با کمک (`aided`).
8. **فاز ۷ (وزن ۸٪):** تکمیل وفاداری ۱۰۰٪ پوسته بومی `v12.5-fa` و ناوبری `M09` (`PathMap → ChapterActivity → LessonRenderer → QuitDialog / CelebrationModal`)، هندسه گره‌های ۹۲dp و حذف قطعی متن دموی چیدمان خط (`R3`).
9. **فاز ۸ (وزن ۱۰٪):** یکپارچه‌سازی عمیق `LearnHarness` (`Measure → Plan → Teach → Practice`) با گراف گزاره‌های کتاب درسی (دو حالت آفلاین `LocalContentProvider` و استریم آنلاین سروری `/api/v1/ai/harness`) به همراه موتور `KST + BKT + FSRS-5` (`R12`).
10. **فاز ۹ (وزن ۷٪):** اتصال هاب ۷بخشی آزمون کنکور و تمرین (`exam-template.js`) به بانک سوالات واقعی کتاب (`R9`)، فرمول نمره منفی یک‌سوم، تایمر ۲۷۰ دقیقه‌ای داخل آزمون، و تفکیک «پاسخبرگ» از «پاسخنامه تشریحی» (`F39–F43`).
11. **فاز ۱۰ (وزن ۵٪):** یکپارچه‌سازی `learning-path.js` با `STRUCTURED_PACKAGE.json` (`R10`)، تکمیل تب «امتیازها (وضعیت من)» و «پروفایل» (`R11`) و همگام‌سازی هر ۳ ساختار توکن (`D4`).
12. **فاز ۱۱ (وزن ۴٪):** بیلد تکرارپذیر بایت‌به‌بایت (`SOURCE_DATE_EPOCH` در `R15`)، تولید `app/dist/Mimo.html` + PWA + قالب APK اندروید و اجرای زنجیره ۶ گانه ممیزی نهایی.
