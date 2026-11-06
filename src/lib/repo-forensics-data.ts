export interface BranchOrArchiveAudit {
  id: string;
  name: string;
  type: "شاخه گیت (Git Branch)" | "آرشیو کد (Zip Archive)" | "فایل کنارگذاشته‌شده (Excluded)";
  commitOrHash: string;
  status: "منبع حقیقت هسته (Core Truth)" | "قطعه مکمل معماری (Key Module)" | "حذف‌شده طبق دستور شما (Ignored)";
  whatIsInside: string;
  verifiedStrengths: string[];
  brokenOrIncompleteParts: string[];
  exactRoleInFinalPlan: string;
}

export interface FrankensteinRootCause {
  id: string;
  title: string;
  symptomSeenByUser: string;
  technicalRootCause: string;
  evidenceLocationInRepo: string;
  engineeringFixInPlan: string;
  targetPhaseCode: string;
}

export interface ExternalRepoRequirement {
  id: string;
  name: string;
  repoUrl: string;
  license: string;
  layer: string;
  priority: "حیاتی (P0 - Core)" | "ضروری (P1 - High)" | "ابزار مهندسی (Toolchain)";
  whyNeeded: string;
  howToIntegrateStepByStep: string;
}

export interface StackArchitectureLayer {
  layerNumber: number;
  layerTitle: string;
  mimoOriginal935: string;
  currentRepoPrototype: string;
  targetUnifiedArchitecture: string;
  keyContractsAndFiles: string[];
}

export interface DeadEndGuardrail {
  id: string;
  category: "محتوا و OCR" | "موتور درس و DSL" | "مهندسی معکوس و سرور" | "رابط کاربری و CSS" | "محیط و ابزار";
  whatFailedBefore: string;
  whyItFailed: string;
  strictRuleForAgent: string;
}

export const REPO_BRANCHES_AND_ARCHIVES: BranchOrArchiveAudit[] = [
  {
    id: "BRANCH_AEBB90B7",
    name: "شاخه origin/arena/aebb90b7-game (۱۳۷ کامیت · HEAD: 0949db0f / 9179b8c4)",
    type: "شاخه گیت (Git Branch)",
    commitOrHash: "9179b8c4 / dd18775f",
    status: "منبع حقیقت هسته (Core Truth)",
    whatIsInside:
      "شامل استخراج کامل ۰ تا ۱۰۰ رابط کاربری میمو ۹٫۳۵ در `mimo-ui/` (۷٬۴۳۰ فایل)، پروتوتایپ مصوب `v12.5-fa` در `mimo-ui/UPGRADE/DESIGN/index.html` (SHA: c356068d…)، شواهد مأموریت‌های رانتایم `ANALYSIS/MISSION_05..09`، خط لوله OCR کتاب زیست دوازدهم (`848/848` صفحه، `694,860` واژه در `ocr_book.py` و `process_book.py`)، اپلیکیشن آفلاین ۱۵ ماژوله در `app/` و مستندات `docs/00..10`.",
    verifiedStrengths: [
      "پروتوتایپ مصوب v12.5-fa با قوانین F2 و F10–F47: ۵ تب فارسی (یادگیری، تمرین، هوش مصنوعی، امتیازها، پروفایل)، ۳ چیپ بالا (سکه، کلید ∞، استریک) و توکن‌های اصلی ARSC.",
      "ماشین وضعیت ناوبری بومی M09 در `app/src/native.js` و `app/native/index.html` (PathMap → ChapterActivity → LessonRenderer → QuitDialog / CelebrationModal).",
      "هندسه دقیق گره‌های مسیر در `app/src/nodes.js` و `node-match.css` (۹۲dp squircle، شعاع ۲۶dp، لبه سه‌بعدی ۸dp، قوس Q با شعاع ۳۲dp، گرید نقطه‌ای ۲۶dp و دکمه شناور واژه‌نامه A).",
      "تکمیل ۱۰۰٪ OCR کتاب زیست دوازدهم (۸۴۸ صفحه) و استخراج ۷۷۵ مدخل پاسخنامه و ۶۰۰ جفت سوال-پاسخ اولیه.",
      "پاس شدن ۴۵/۴۵ تست واحد و یکپارچگی + ۵۴ بررسی verify_app.py + ۵۱ بررسی verify_output.py.",
    ],
    brokenOrIncompleteParts: [
      "R1: خروجی OCR کتاب زیست (`PROCESSED_DRAFT.json`) هنوز دارای غلط‌های املایی OCR («یافته» به جای «یاخته»، «هغز استفوان» به جای «مغز استخوان») و تداخل ستون‌های دوتایی است و وضعیت آن `unreviewed` مانده است.",
      "R2: تابع `chapterRefFor()` هنوز به جای اتصال قطعی به `curriculumId` از هش رشته‌ای (ID Hash) استفاده می‌کند.",
      "R4–R6: تنها ۵ خانواده رندرر پیاده شده و ۴ خانواده مهم (`validatedInput`, `InteractiveWebView`, `Reveal`, `executableFiles`) هنوز کامل نیستند.",
      "R9: بانک سوال آزمون (`QBANK`) هنوز یک آرایه نمونه ۲۰ سوالی است و به بسته ساختاریافته کتاب متصل نشده است.",
      "R12: پل `LearnHarness` در `app/src/harness.js` فقط روی `LocalContentProvider` استاب شده و فاقد اتصال به سرور/LLM یا گراف گزاره‌های کتاب است.",
    ],
    exactRoleInFinalPlan:
      "ستون فقرات UI/UX، ناوبری بومی M09، توکن‌های طراحی ARSC، خط لوله OCR کتاب درسی و ساختار بسته محتوایی (`STRUCTURED_PACKAGE.json`).",
  },
  {
    id: "BRANCH_ECB8AF07",
    name: "شاخه origin/arena/ecb8af07-game (بسته مهندسی معکوس HANDOFF/01..15 و mimo-re/)",
    type: "شاخه گیت (Git Branch)",
    commitOrHash: "c0d6056d / eebebb22",
    status: "منبع حقیقت هسته (Core Truth)",
    whatIsInside:
      "کالبدشکافی بایت‌به‌بایت کدهای Kotlin و ۱۳ فایل DEX اپلیکیشن Mimo 9.35 (`sha256: 48ce1740…`): شامل گرامر رسمی EBNF زبان درسنامه (`dsl_grammar.ebnf` با ۲۹ تگ)، الگوریتم دقیق نرمال‌ساز و تصحیح‌گر (`04_SPEC_INTERACTION_AND_GRADING.md` + ۵۴ تست `grading_vectors.json`)، اسکیمای دیتابیس SQLite Room v2 (`mimo.db` با ۳ جدول و ۱۵ کوئری DAO)، کاتالوگ ۶۲ اندپوینت Retrofit و زنجیره اینترسپتورها (`hg.e → fh.b → fh.a`)، و فهرست ۴۵ تصمیم معماری (`D-01..D-45` و `ADD-01..ADD-08`).",
    verifiedStrengths: [
      "استخراج قطعی الگوریتم تصحیح بایت‌به‌بایت (`qm.i.a`) و حکم سه‌حالته (`CORRECT | PARTIAL | INCORRECT`) به همراه ۵۴ بردار تست طلایی (`grading_vectors.json`).",
      "کشف واقعیت حیاتی مدل دانش‌آموز (`05_SPEC_LEARNER_MODEL.md`): فیلد `tries` یک پرچم ۰ یا ۱ است (`isSolvedCorrectly = tries >= 1`)، `attempts` شمارنده نشست است، و جدول `lesson_progress` یک صف خروجی (Outbox) است.",
      "کشف مرز سرور (`Completion Boundary`): اپ اصلی میمو هرگز تکمیل فصل یا باز شدن قفل گره را در کلاینت حساب نمی‌کند بلکه از سرور می‌پرسد؛ بنابراین قانون محلی `ADD-04` برای نسخه کنکور تعریف شده است.",
      "موتور مرجع پایتونی `HANDOFF/tools/reference_engine.py` و اسکریپت ممیزی `verify_handoff.py` (۱۰/۱۰ سبز).",
    ],
    brokenOrIncompleteParts: [
      "تله Q-44 در نرمال‌ساز: تابع `qm.i.a` برای زبان انگلیسی نوشته شده و حروف فارسی/عربی (`ی/ي`، `ک/ك`، نیم‌فاصله ZWNJ و اعداد فارسی `۰-۹`) را یکسان‌سازی نمی‌کند.",
      "ساختار فریم‌های WebSocket و رابط جاوااسکریپت WebView (`Q-96` و `Q-140`) در استاتیک قابل استخراج نبودند و باید با قرارداد محلی جایگزین شوند.",
      "این شاخه هیچ‌گونه اتصال به رابط کاربری کنکوری `v12.5-fa` و خط لوله کتاب زیست شاخه `aebb90b7-game` ندارد.",
    ],
    exactRoleInFinalPlan:
      "قانون اساسی موتور زیرین (Core Engine Spec): گرامر ۲۷ تگ DSL، الگوریتم تصحیح، اسکیمای دیتابیس Room/SQLite و قوانین `ADD-01..ADD-08` مستقیماً از این شاخه وارد هسته محصول می‌شوند.",
  },
  {
    id: "ZIP_PEDAGOGICAL_AGENT",
    name: "آرشیو build-konkur-pedagogical-ai-agent.zip (موتور هم‌ریختی پداگوژیک و گاردریل‌های M1–M10)",
    type: "آرشیو کد (Zip Archive)",
    commitOrHash: "pedagogy-engine.ts",
    status: "قطعه مکمل معماری (Key Module)",
    whatIsInside:
      "اپلیکیشن Next.js + PostgreSQL شامل تحلیل ۵ نقص بنیادی فرم‌های اولیه میمو برای کنکور (`LEGACY_MIMO_FORM_DEFECTS`)، ماتریس هم‌ریختی دروس کنکور (زیست، شیمی، فیزیک، ریاضی) به مکانیک‌های تعاملی میمو، و کامپایلر مقید با ۱۰ گاردریل الگوریتمی (`M1` تا `M10`).",
    verifiedStrengths: [
      "حل بزرگ‌ترین حلقه مفقوده پداگوژیک: تبدیل گام `code` میمو (که برای پایتون/SQL بود) به دو مکانیک کنکوری `token_assembly` (چیدمان بلوکی مسیرهای زیستی/فرمولی با بلوک تله) و `trap_detector` (دیباگر گزاره‌های کنکوری).",
      "تبدیل جای خالی معمولی (`fill`) به `guided_cloze` قیدمحور که منحصراً روی قیدهای کنکوری («همه»، «برخی»، «اغلب»، «به‌جز»، «مستقیماً») می‌نشیند.",
      "الزام ماتریس کالبدشکافی ۴ گزینه (`optionDiagnostics`) و تکنیک سرعتی رد گزینه (`eliminationShortcut`) در هر تست کنکور.",
    ],
    brokenOrIncompleteParts: [
      "خروجی این کامپایلر در جدول مجزایی ذخیره می‌شد و به فرمت استاندارد `STRUCTURED_PACKAGE.json` و تگ‌های DSL میمو (`<selection>`, `<interaction type=\"fillTheGap\">`) خروجی نمی‌داد.",
    ],
    exactRoleInFinalPlan:
      "در فاز ۴ و فاز ۵ به عنوان «لایه کامپایلر پداگوژیک» بین متن تمیزشده کتاب درسی (OCR) و تولیدکننده فایل `STRUCTURED_PACKAGE.json` قرار می‌گیرد تا هیچ درسنامه کنکوری خشک یا سطحی تولید نشود.",
  },
  {
    id: "ZIP_ROADMAP_AND_HARNESS",
    name: "آرشیو comprehensive-software-development-roadmap.zip (موتور KST + FSRS-5 + LearnHarness)",
    type: "آرشیو کد (Zip Archive)",
    commitOrHash: "algorithms.ts",
    status: "قطعه مکمل معماری (Key Module)",
    whatIsInside:
      "پیاده‌سازی کامل ریاضیات نظریه فضای دانش (KST Outer/Inner Fringe از ریپوی `newlearning`)، مدل تسلط بیزی کالیبره‌شده (BKT با تفکیک پاسخ مستقل `unaided` از پاسخ با راهنمایی `aided` از ریپوی `my-first`)، الگوریتم مرور فاصله‌دار `FSRS-5`، کنترلر باند جریان ۷۰ تا ۸۵ درصد، و چرخه ۴ فازی `LearnHarness` (`Probe → Plan → Teach → Practice`).",
    verifiedStrengths: [
      "کدهای آماده و تست‌شده TypeScript در `src/lib/algorithms.ts` برای `updateBKTMastery`, `updateFSRSState`, `computeFlowBandAction` و `computeKSTStates`.",
      "شبیه‌ساز پاسخ‌برگ نوری کنکور با فرمول نمره منفی یک‌سوم و اتصال خودکار غلط‌ها و نزده‌ها به صف ترمیم.",
    ],
    brokenOrIncompleteParts: [
      "این آرشیو بر اساس ریپوهای قدیمی‌تر (`newlearning` و `my-first`) نوشته شده بود و جزئیات شاخه‌های `aebb90b7-game` و `ecb8af07-game` (مانند ناوبری بومی M09، ۲۷ تگ DSL میمو، و OCR کتاب زیست ۸۴۸ صفحه‌ای) را در برنامه اجرایی خود نداشت.",
    ],
    exactRoleInFinalPlan:
      "توابع ریاضی `algorithms.ts` (KST + BKT + FSRS-5 + Flow Controller) مستقیماً به موتور پیشرفت محلی میمو (`LessonProgress`) و تب هوش مصنوعی (`LearnHarness`) متصل می‌شوند.",
  },
  {
    id: "ZIP_REBUILD_AND_DEVELOP",
    name: "آرشیوهای rebuild-complete-software-application.zip و develop-konkur-learning-application.zip",
    type: "آرشیو کد (Zip Archive)",
    commitOrHash: "mimo-engine.ts / engine.ts",
    status: "قطعه مکمل معماری (Key Module)",
    whatIsInside:
      "پورت React/Next.js پوسته ۵ تبه `v12.5-fa` به همراه وکتورهای آیکون‌های ARSC (`mimo-vectors.ts`)، اسکریپت `lesson-webview.js`، و میزکار تست ۵۴ بردار تصحیح و جداول Room در PostgreSQL.",
    verifiedStrengths: [
      "کامپوننت‌های آماده React برای هر ۵ تب، مودال درس، هاب آزمون ۷بخشی و آیکون‌های وکتوری استخراج‌شده از APK.",
      "پیاده‌سازی دقیق TypeScript نرمال‌ساز `normalise()` و `gradeValidatedInput()` منطبق با بایت‌کد میمو.",
    ],
    brokenOrIncompleteParts: [
      "دو پروژه جداگانه بودند: یکی فقط میزکار دیتابیس Room بود و دیگری پوسته ظاهری React بدون دیتابیس و بدون کامپایلر کتاب.",
    ],
    exactRoleInFinalPlan:
      "ادغام کامپوننت‌های UI و موتور تصحیح TypeScript در معماری یکپارچه نهایی.",
  },
  {
    id: "EXCLUDED_PHARMACY_AND_SOR",
    name: "پروژه داروسازی (ttac-4.3.6.apk، pharmacy-inventory.html، شاخه dd2b6beb) و بازی شورش در شهر",
    type: "فایل کنارگذاشته‌شده (Excluded)",
    commitOrHash: "dd2b6beb / eb3b2453",
    status: "حذف‌شده طبق دستور شما (Ignored)",
    whatIsInside:
      "اپلیکیشن انبارداری داروخانه و استعلام سامانه تیتک (`ttac-4.3.6.apk` و `pharmacy-inventory (3).html`) و رام بازی سگا (`Streets-of-Rage_Genesis_EN.zip`).",
    verifiedStrengths: [],
    brokenOrIncompleteParts: [
      "هیچ ارتباطی به پروژه آموزشی کنکور-میمو ندارند و صرفاً از آپلودهای اولیه در ریشه ریپو باقی مانده‌اند.",
    ],
    exactRoleInFinalPlan:
      "طبق دستور صریح شما کاملاً کنار گذاشته می‌شوند. در فاز ۰ در `.gitignore` / پوشه بایگانی قرنطینه می‌شوند تا هیچ ایجنتی با دیدن آن‌ها دچار انحراف نشود.",
  },
];

export const FRANKENSTEIN_ROOT_CAUSES: FrankensteinRootCause[] = [
  {
    id: "RC_01_TYPOGRAPHY_DEMO_AS_LESSON",
    title: "۱. اشتباه گرفتن متن تست فونت پروتوتایپ به عنوان «درسنامه واقعی»!",
    symptomSeenByUser:
      "وقتی در پروتوتایپ یا بیلد اول وارد درس می‌شدید، به جای درس زیست‌شناسی، جمله عجیب «گاهی لازم است متن‌ها را با شکستن خطوط، خواناتر کنیم…» نمایش داده می‌شد و زیرش یک تست تصادفی می‌آمد!",
    technicalRootCause:
      "در فایل `mimo-ui/UPGRADE/DESIGN/index.html` (`phone.html`)، طراح UI صفحه `lesson` را صرفاً برای تست شکستن خطوط فارسی (Line-break Typography Demo) ساخته بود. ایجنت قبلی در بیلد `543a20ba` همان متن استاتیک HTML را به عنوان درسنامه خوانده بود و با هش کردن ID درس، یک سوال تصادفی از آرایه ۲۰ تایی `QBANK` به ته آن چسبانده بود!",
    evidenceLocationInRepo:
      "شاخه `aebb90b7-game`: فایل‌های `docs/03_ERRORS_AND_DEAD_ENDS.md` §1 و `app/docs/MIMO_CONTENT_MODEL.md` §1.",
    engineeringFixInPlan:
      "حذف کامل خوانش متن از `phone.html`؛ اتصال ۱۰۰٪ رندرر درس به فایل ساختاریافته `STRUCTURED_PACKAGE.json` با سلسله‌مراتب ۶ نقشی (`hook → check → feedback → explain → practice → recap`) و بلوک‌های تایپ‌شده DSL.",
    targetPhaseCode: "PHASE_03 & PHASE_07",
  },
  {
    id: "RC_02_TWO_COLUMN_OCR_COLLISION",
    title: "۲. قاطی شدن ستون‌های دوتایی کتاب زیست در OCR و سوالات بدون کلید (`correctIndex: null`)",
    symptomSeenByUser:
      "با اینکه ۸۴۸ صفحه کتاب زیست OCR شده بود، سوالات استخراج‌شده جملات بریده‌بریده داشتند و گزینه صحیح هیچ‌کدام مشخص نبود!",
    technicalRootCause:
      "کتاب کمک‌درسی زیست (`@BankBookkonkor (26)_extract.pdf`) دو ستونی (راست به چپ) است و پاسخنامه تشریحی آن در صفحات انتهایی هر فصل قرار دارد. اسکریپت اولیه `structure_book.py` خروجی خام `GetTSVText()` را افقی می‌خواند (سطر ستون راست با سطر ستون چپ قاطی می‌شد) و ۵۶۵ سوال ناقص با `correctIndex: null` تولید می‌کرد.",
    evidenceLocationInRepo:
      "شاخه `aebb90b7-game`: فایل‌های `app/tools/process_book.py` و `docs/05_ROADMAP.md` (R1).",
    engineeringFixInPlan:
      "استفاده از مختصات جعبه‌های کلمات (`694,860 word bounding boxes`) برای تفکیک ستون راست (`x > W/2`) از ستون چپ (`x < W/2`)، اجرای دیکشنری اصلاح غلط‌های رایج OCR فارسی («یافته»←«یاخته»، «هغز استفوان»←«مغز استخوان»)، و اتصال پارسر پاسخنامه (`775` کلید) به سوالات قبل از تایید (`reviewStatus: 'approved'`).",
    targetPhaseCode: "PHASE_05",
  },
  {
    id: "RC_03_CODING_TO_KONKUR_MISMATCH",
    title: "۳. بی‌معنی شدن گام کدنویسی میمو (`<code>`) در دروس کنکور و تبدیل شدن اپ به بانک تست خشک",
    symptomSeenByUser:
      "در اپ اصلی میمو، کاربر کد پایتون یا HTML را تکه به تکه می‌سازد و حس بازی و ساختن دارد؛ اما در پروتوتایپ کنکور، درس‌ها فقط متن ساده و تست ۴ گزینه‌ای تکراری شده بودند.",
    technicalRootCause:
      "در میمو ۱۸۹٬۹۵۶ بلوک `<code>` با ۲۱٬۶۸۶ تعامل `fillTheGap` و `validatedInput` وجود دارد. وقتی موضوع از برنامه‌نویسی به زیست/شیمی/فیزیک تغییر کرد، ایجنت‌ها چون «کد پایتون» نداشتند، کل مکانیک ساختن و دیباگ کردن را حذف کردند و فقط `<p>` و `<selection>` گذاشتند!",
    evidenceLocationInRepo:
      "آرشیو `build-konkur-pedagogical-ai-agent.zip`: فایل `src/lib/pedagogy-engine.ts` (`DEFECT_02_CODE_STEP_MISMATCH`).",
    engineeringFixInPlan:
      "پیاده‌سازی «هم‌ریختی پداگوژیک» (Pedagogical Isomorphism) روی همان موتور DSL میمو: استفاده از بلوک `<code>` و `<interaction>` میمو برای ۱) چیدمان بلوکی مسیرهای زیستی/فرمولی با بلوک تله (`token_assembly`)، ۲) شکار قید غلط در گزاره‌های ترکیبی کنکور (`trap_detector`) و ۳) جای خالی روی قیدهای تصمیم‌ساز کنکور (`همه / برخی / اغلب / به‌جز`).",
    targetPhaseCode: "PHASE_04",
  },
  {
    id: "RC_04_SERVER_COMPLETION_VACUUM",
    title: "۴. خلأ منطق سرور میمو (`SERVER CONFIRMED = 0`) و پاک شدن تاریخچه پس از سینک",
    symptomSeenByUser:
      "مشخص نبود چطور قفل فصل‌ها باز می‌شود، چطور سکه و استریک حساب می‌شود و چرا در کدهای مهندسی معکوس، جدول پیشرفت بعد از ارسال پاک می‌شود!",
    technicalRootCause:
      "طبق کالبدشکافی بایت‌کد در `HANDOFF/05_SPEC_LEARNER_MODEL.md`، اپ اصلی میمو هیچ منطقی برای محاسبه اتمام فصل یا باز کردن گره بعدی در کلاینت ندارد و جدول `lesson_progress` صرفاً یک صف انتظار (Outbox) است که بعد از `POST /v1/tutorials/{id}/progress` رکوردهایش `DELETE` می‌شوند!",
    evidenceLocationInRepo:
      "شاخه `ecb8af07-game`: فایل‌های `HANDOFF/05_SPEC_LEARNER_MODEL.md` §6–§7 و `HANDOFF/12_DELTA_REGISTER.md` (`ADD-03`, `ADD-04`).",
    engineeringFixInPlan:
      "اعمال رسمی قوانین `ADD-03` (نگهداری تاریخچه محلی به صورت Append-Only و عدم حذف رکوردهای حل‌شده) و `ADD-04` (محاسبه قطعی اتمام فصل در کلاینت وقتی تمامی ریزدرس‌های فصل دارای `tries >= 1` باشند + محاسبه لبه بیرونی KST).",
    targetPhaseCode: "PHASE_01 & PHASE_06",
  },
  {
    id: "RC_05_DISCONNECTED_LEARNHARNESS",
    title: "۵. نیمه‌کاره ماندن ترکیب هوش مصنوعی و `LearnHarness` در تب سوم",
    symptomSeenByUser:
      "تب هوش مصنوعی و دکمه‌های `Measure → Plan → Teach → Practice` ظاهر قشنگی داشتند، اما یا پیام ثابت نشان می‌دادند یا معلوم نبود چطور باید بدون لو رفتن کلید API و بدون توهم‌زایی (Hallucination) با کتاب درسی کار کنند.",
    technicalRootCause:
      "در شاخه `aebb90b7-game`، به دلیل قانون صداقت مهندسی معکوس (`externalProvider: 'not-configured'`)، فایل `app/src/harness.js` هیچ ارتباطی با LLM یا سرور نداشت و از طرفی ممیزی اپ هدف‌پلاس (`HADAF_PLUS_AI_API_AUDIT.md`) نشان داد که اپ‌های تجاری کلید LLM را در کلاینت نمی‌گذارند بلکه از گیت‌وی سرور (`gateway.hadafplus.app/ZistAI/*`) با استریم SSE استفاده می‌کنند.",
    evidenceLocationInRepo:
      "شاخه `aebb90b7-game`: `ANALYSIS/HADAF_PLUS_AI_API_AUDIT.md`، `app/src/harness.js` و شاخه `ecb8af07-game`: `HANDOFF/08_SPEC_STREAMING_AND_TUTOR.md`.",
    engineeringFixInPlan:
      "معماری دولایه `LearnHarness`: ۱) در حالت آفلاین، تغذیه فازهای `Probe → Plan → Teach → Practice` از گراف گزاره‌های تاییدشده کتاب (`STRUCTURED_PACKAGE.json`) و ۲) در حالت آنلاین، اتصال به اندپوینت بک‌اند `/api/v1/ai/harness` (پروکسی SSE سمت سرور با کلید امن در `.env`) که دقیقاً روی همان گراف گزاره‌های کتاب استدلال سقراطی انجام می‌دهد.",
    targetPhaseCode: "PHASE_08",
  },
  {
    id: "RC_06_HASH_BASED_CURRICULUM_ROUTING",
    title: "۶. نگاشت هش‌پایه `chapterRefFor()` و عدم اتصال نقشه مسیر به گراف واقعی کتاب",
    symptomSeenByUser:
      "کلیک روی گره‌های مختلف نقشه یادگیری یا فصل‌ها گاهی درس‌های تکراری یا نامرتبط باز می‌کرد و مسیر یادگیری ۱۲ درس کنکور (`learning-path.js`) ساختگی بود.",
    technicalRootCause:
      "در `app/src/content-engine.js`، تابع `chapterRefFor()` هنوز از هش رشته شناسه برای انتخاب یکی از ۲۰ درسنامه استفاده می‌کرد و `learning-path.js` از یک آرایه ساختگی `KONKUR` جدا از `STRUCTURED_PACKAGE.json` تغذیه می‌شد.",
    evidenceLocationInRepo:
      "شاخه `aebb90b7-game`: `docs/05_ROADMAP.md` (`R2` و `R10`).",
    engineeringFixInPlan:
      "جایگزینی کامل `chapterRefFor()` با جدول نگاشت صریح و قطعی `curriculumId` (بدون هیچ `hashCode` یا انتخاب تصادفی) و تولید کل درخت مسیر یادگیری مستقیماً از `STRUCTURED_PACKAGE.json`.",
    targetPhaseCode: "PHASE_05 & PHASE_10",
  },
];

export const EXTERNAL_REPOS_AND_TOOLS: ExternalRepoRequirement[] = [
  {
    id: "EXT_01_LEARNHARNESS",
    name: "LearnHarness (چارچوب ۴ فازی آموزش شناختی)",
    repoUrl: "https://github.com/amosblomqvist/learnharness",
    license: "AGPL-3.0-only (پین‌شده در کامیت 713377f3)",
    layer: "لایه ۴: موتور هوش مصنوعی و تدریس سقراطی",
    priority: "حیاتی (P0 - Core)",
    whyNeeded:
      "هسته اصلی تب سوم (هوش مصنوعی) و کمک‌آموزگار داخل درس: شامل ۴ فاز `Measure (Probe) → Plan → Teach → Practice`، اصل اول (Unconditional Truth / بدیهیات پایه)، اصل دوم (Motivated Discovery / کشف باانگیزه)، اسلایدر ضریب اطمینان و باکس بلند فکر کردن (`thinking`)، به همراه پایپ‌لاین استخراج گراف گزاره‌ها (`Extractor → Auditor → Merger`).",
    howToIntegrateStepByStep:
      "۱) ماژول `app/src/harness.js` وضعیت ۴ فاز و گراف گزاره‌ها را در `store.ai.harness` نگه می‌دارد. ۲) هر فصل کتاب در کامپایلر فاز ۵ به گزاره‌های اتمیک (`propositions[]`) با پیشنیازهایش تبدیل می‌شود. ۳) در حالت آفلاین `LocalContentProvider` و در حالت آنلاین استریم SSE بک‌اند `/api/v1/ai/harness` فازها را پیش می‌برد.",
  },
  {
    id: "EXT_02_GRAMOPHONE_NEWLEARNING",
    name: "Gramophone / newlearning (موتور KST و باند جریان ۷۰-۸۵٪)",
    repoUrl: "https://github.com/danmillman008-hub/newlearning",
    license: "MIT / Internal",
    layer: "لایه ۲ و ۳: نظریه فضای دانش (KST) و تطبیق دشواری",
    priority: "حیاتی (P0 - Core)",
    whyNeeded:
      "الگوریتم‌های اثبات‌شده `surmise.py` (حذف دور از گراف پیشنیاز با DFS)، `spacing.py` (محاسبه لبه بیرونی یادگیری `Outer Fringe` و لبه درونی مرور `Inner Fringe` بر اساس قضایای Birkhoff) و `adapt.py` (کنترلر باند جریان که دقت داوطلب را در ناحیه طلایی ۷۰٪ تا ۸۵٪ نگه می‌دارد).",
    howToIntegrateStepByStep:
      "توابع پایتونی به TypeScript خالص در `src/lib/algorithms.ts` پورت شده‌اند و مستقیماً روی جدول `lesson_progress` و گراف پیشنیاز درسنامه‌های کنکور اجرا می‌شوند تا گره بعدی پیشنهاد شود.",
  },
  {
    id: "EXT_03_TS_FSRS",
    name: "TS-FSRS (الگوریتم تکرار فاصله‌دار مدرن FSRS v5)",
    repoUrl: "https://github.com/open-spaced-repetition/ts-fsrs",
    license: "MIT",
    layer: "لایه ۳: موتور حافظه بلندمدت و صف مرور غلط‌ها",
    priority: "حیاتی (P0 - Core)",
    whyNeeded:
      "جایگزین علمی لایتنر قدیمی برای زمان‌بندی مرور تا روز کنکور: محاسبه پایداری حافظه ($S$)، دشواری ذاتی مبحث ($D$) و احتمال بازیابی در لحظه ($R = (1 + F \\cdot t / S)^C$).",
    howToIntegrateStepByStep:
      "هر بار که یک ریزدرس یا تست کنکور حل می‌شود، علاوه بر آپدیت ردیف ۱۱ فیلدی `LessonProgress` میمو (`tries`, `attempts`, `inQueue`)، پارامترهای FSRS-5 آن گره آپدیت شده و زمان مرور بعدی تعیین می‌گردد.",
  },
  {
    id: "EXT_04_TESSERACT_SURYA_MINERU",
    name: "Tesseract 5.5 (fas) + Surya OCR / MinerU (خط لوله استخراج کتاب‌های کنکور)",
    repoUrl: "https://github.com/opendatalab/MinerU",
    license: "Apache-2.0",
    layer: "لایه ۱: خط لوله ورود کتاب‌های درسی، جزوات و آزمون‌ها",
    priority: "حیاتی (P0 - Core)",
    whyNeeded:
      "تبدیل PDF کتاب‌های درسی و کمک‌درسی کنکور (که دو ستونی، دارای فرمول، جدول و پاسخنامه تشریحی هستند) به JSON ساختاریافته همراه با مختصات دقیق کلمات (`word bounding boxes`).",
    howToIntegrateStepByStep:
      "برای کتاب زیست دوازدهم، OCR کامل ۸۴۸ صفحه با Tesseract انجام شده و ۶۹۴٬۸۶۰ جعبه کلمه موجود است (` دوباره OCR نکنید!`). برای کتاب‌های بعدی (شیمی، فیزیک، ریاضی)، خروجی PDF از طریق اسکریپت `ocr_book.py` یا `MinerU` به `process_book.py` (نسخه تفکیک‌کننده دو ستون RTL) داده می‌شود.",
  },
  {
    id: "EXT_05_KATEX_MERMAID",
    name: "KaTeX + Mermaid.js (رندرر فرمول‌های ریاضی/شیمی و درخت پیشنیاز)",
    repoUrl: "https://github.com/KaTeX/KaTeX",
    license: "MIT",
    layer: "لایه ۵: رندرر بلوک‌های توسعه‌یافته DSL کنکور (`<math>`, `<diagram>`)",
    priority: "ضروری (P1 - High)",
    whyNeeded:
      "در مشخصات `HANDOFF/03_SPEC_LESSON_DSL.md` §6، چهار تگ توسعه‌ای `<math>`, `<diagram>`, `<grammar>`, `<audio>` برای محصول جدید پیش‌بینی شده است تا فرمول‌های فیزیک/شیمی/ریاضی و فلوچارت‌های زیست‌شناسی بدون نیاز به عکس رندر شوند.",
    howToIntegrateStepByStep:
      "افزودن رندرر آفلاین `<math>` و `<diagram>` به `content-engine.js` با حفظ ۱۰۰٪ سازگاری عقب‌رو با ۲۷ تگ اصلی میمو.",
  },
  {
    id: "EXT_06_CAPACITOR_OR_KOTLIN_SHELL",
    name: "Android Kotlin WebView / Capacitor + Room SQLite Bridge",
    repoUrl: "https://github.com/ionic-team/capacitor",
    license: "MIT",
    layer: "لایه ۵ و ۶: بسته‌بندی نهایی اندروید (APK) + PWA تک‌فایلی",
    priority: "ضروری (P1 - High)",
    whyNeeded:
      "تبدیل بدون دردسر موتور وب/PWA (`app/dist/Mimo.html` و Next.js) به فایل نصبی اندروید (`APK`) با پشتیبانی ۱۰۰٪ آفلاین و دیتابیس SQLite محلی، یا پیاده‌سازی پوسته بومی Kotlin Compose روی همان اسکیمای Room v2 (`mimo.db`).",
    howToIntegrateStepByStep:
      "موتور هسته (`dsl`, `grade`, `learn`, `content-engine`) ۱۰۰٪ مستقل از فریم‌ورک است؛ هم مستقیماً در `Mimo.html` / PWA اجرا می‌شود، هم در WebView/Capacitor اندروید قرار می‌گیرد و هم با جداول Room v2 کاتلین هم‌ریخت است.",
  },
];

export const STACK_ARCHITECTURE_DECISION_MATRIX: StackArchitectureLayer[] = [
  {
    layerNumber: 1,
    layerTitle: "لایه ۱: موتور هسته درس، پارسر DSL و تصحیح‌گر (Core Lesson & Grading Engine)",
    mimoOriginal935:
      "کدهای Kotlin در پکیج‌های مبهم‌شده (`te.c` دیسپچر ۷ پارسر `te.a..te.g`، نرمال‌ساز `qm.i.a`، وضعیت‌های بازخورد `jm.m/n/o`).",
    currentRepoPrototype:
      "در شاخه `ecb8af07`: موتور مرجع پایتون (`reference_engine.py`) + در شاخه `aebb90b7`: ماژول جاوااسکریپت `app/src/content-engine.js` و در آرشیو Next.js: `src/lib/mimo/engine.ts`.",
    targetUnifiedArchitecture:
      "ماژول یکپارچه و بدون وابستگی (Zero-Dependency TypeScript/ESM) که هر ۲۷ تگ اصلی میمو + ۲ تگ کنکوری (`<math>`, `<diagram>`) را پارس می‌کند، نرمال‌ساز `qm.i.a` را به همراه پشتیبانی استاندارد یونیکد فارسی (`Q-44 fix`) اجرا می‌کند و ۱۰۰٪ از ۵۴ بردار تست `grading_vectors.json` را پاس می‌نماید.",
    keyContractsAndFiles: [
      "HANDOFF/data/dsl_grammar.ebnf",
      "HANDOFF/data/grading_vectors.json",
      "app/src/content-engine.js",
      "src/lib/mimo/engine.ts",
    ],
  },
  {
    layerNumber: 2,
    layerTitle: "لایه ۲: دیتابیس محلی و مدل پیشرفت دانش‌آموز (Local Persistence & Sync Outbox)",
    mimoOriginal935:
      "دیتابیس Android Room SQLite v2 (`mimo.db`، هش `2b8ab6d303d9a501bd8c8fb78d8352fc`) با ۳ جدول (`lesson_progress` ۱۱ فیلدی، `tutorial_completions`، `chapter_completions`) و ۱۵ کوئری DAO.",
    currentRepoPrototype:
      "در `app/src/store.js`: ذخیره‌سازی در `localStorage` مرورگر (`store v1`)؛ در آرشیو `rebuild`: جداول Drizzle PostgreSQL.",
    targetUnifiedArchitecture:
      "معماری Offline-First دوطرفه: ۱) در سمت کلاینت (وب/PWA/اندروید)، نگهداری دقیق همان ۳ جدول با کلید مرکب `(lesson_id, tutorial_id)` به علاوه قوانین `ADD-03` (عدم حذف تاریخچه پس از سینک) و `ADD-04` (محاسبه محلی تکمیل فصل وقتی همه دروس `tries >= 1` دارند). ۲) در سمت سرور، دیتابیس PostgreSQL با Drizzle ORM که صف `in_queue = 1` را دریافت و سینک می‌کند.",
    keyContractsAndFiles: [
      "HANDOFF/data/room_schema.json",
      "HANDOFF/data/progress_vectors.json",
      "app/src/store.js",
      "src/db/schema.ts",
    ],
  },
  {
    layerNumber: 3,
    layerTitle: "لایه ۳: خط لوله کتاب‌های درسی و کامپایلر پداگوژیک (Textbook OCR & Isomorphism Pipeline)",
    mimoOriginal935:
      "۱۰٬۳۱۷ فایل JSON استاتیک داخل APK (`assets/lessons-en/tracks/tutorial-<id>.json` با `publishSetVersion = 753`).",
    currentRepoPrototype:
      "اسکریپت‌های پایتون `ocr_book.py`، `process_book.py` و `emit_structured_package.py` + `STRUCTURED_PACKAGE.json` (۲۰ فصل / ۱۲۰ ریزدرس با وضعیت `unreviewed`).",
    targetUnifiedArchitecture:
      "خط لوله ۶ مرحله‌ای آفلاین/سروری: ۱) تفکیک دو ستون RTL از روی `word boxes`، ۲) اصلاح دیکشنری OCR فارسی، ۳) اتصال پاسخنامه تشریحی (`775` مدخل)، ۴) کامپایلر هم‌ریختی پداگوژیک با گاردریل‌های `M1–M10` (`concept_bite`, `guided_cloze`, `token_assembly`, `trap_detector`, `konkur_test`)، ۵) تولید `STRUCTURED_PACKAGE.json` با نگاشت قطعی `curriculumId`، و ۶) دروازه اعتبارسنجی `validate_content.py`.",
    keyContractsAndFiles: [
      "app/content/MIMO_INFORMATION_FORM.json",
      "app/content/STRUCTURED_PACKAGE.json",
      "app/tools/process_book.py",
      "app/tools/validate_content.py",
    ],
  },
  {
    layerNumber: 4,
    layerTitle: "لایه ۴: هوش مصنوعی، `LearnHarness` و موتور تطبیقی KST / BKT / FSRS-5",
    mimoOriginal935:
      "استریم SSE برای AI Tutor (در وضعیت فیدبک غلط `jm.o`) + تصمیم‌گیری سروری.",
    currentRepoPrototype:
      "ماژول `app/src/harness.js` (پین‌شده به `amosblomqvist/learnharness`) با `LocalContentProvider` آفلاین + الگوریتم‌های KST/BKT/FSRS در `algorithms.ts`.",
    targetUnifiedArchitecture:
      "ترکیب کامل `LearnHarness` (`Probe → Plan → Teach → Practice`) با گراف گزاره‌های کتاب درسی: در حالت بدون اینترنت، از گزاره‌ها و نردبان راهنمایی داخل `STRUCTURED_PACKAGE.json` پاسخ می‌دهد؛ در حالت متصل به بک‌اند، از طریق اندپوینت امن `/api/v1/ai/harness` (پروکسی SSE سمت سرور مشابه معماری کشف‌شده در `HADAF_PLUS_AI_API_AUDIT.md`) تدریس سقراطی زنده انجام می‌دهد و ضریب تسلط BKT (`aided` در برابر `unaided`) و زمان مرور `FSRS-5` را آپدیت می‌کند.",
    keyContractsAndFiles: [
      "app/src/harness.js",
      "HANDOFF/08_SPEC_STREAMING_AND_TUTOR.md",
      "ANALYSIS/HADAF_PLUS_AI_API_AUDIT.md",
      "src/lib/algorithms.ts",
    ],
  },
  {
    layerNumber: 5,
    layerTitle: "لایه ۵: پوسته رابط کاربری بومی `v12.5-fa` و خروجی چندپلتفرمی (Web / PWA / Android APK)",
    mimoOriginal935:
      "اندروید بومی با Kotlin + Jetpack Compose + XML Views + WebView داخلی برای درس‌های تعاملی.",
    currentRepoPrototype:
      "پوسته مصوب `app/native/index.html` + `app/src/native.js` + `app/assets/native.css` و خروجی یک‌کلیکه `app/dist/Mimo.html` + پورت Next.js.",
    targetUnifiedArchitecture:
      "حفظ ۱۰۰٪ وفاداری بصری به حکم کاربر در `v12.5-fa` (قوانین `F2, F10–F47`: ۵ تب فارسی، ۳ چیپ، گره‌های ۹۲dp با قوس Q، هاب آزمون ۷بخشی با تفکیک پاسخبرگ و پاسخنامه) با قابلیت خروجی همزمان به عنوان: ۱) اپلیکیشن وب فول‌استک Next.js، ۲) فایل تک‌کلیکه آفلاین `Mimo.html` و PWA قابل نصب روی موبایل، و ۳) اپلیکیشن اندروید (از طریق پوسته Kotlin WebView / Capacitor یا Compose).",
    keyContractsAndFiles: [
      "mimo-ui/UPGRADE/DESIGN/index.html",
      "app/native/index.html",
      "app/src/native.js",
      "app/tools/build_output.py",
    ],
  },
];

export const DEAD_ENDS_AND_ANTI_DRIFT_GUARDRAILS: DeadEndGuardrail[] = [
  {
    id: "DE_01_NO_RE_OCR",
    category: "محتوا و OCR",
    whatFailedBefore: "اجرای مجدد OCR روی ۸۴۸ صفحه کتاب زیست یا دانلود/آنزیپ مجدد آرشیو چندبخشی گوگل درایو.",
    whyItFailed:
      "OCR کل ۸۴۸ صفحه (۲۵۹۱ ثانیه) و استخراج ۶۹۴٬۸۶۰ جعبه کلمه (۱۶۶۹ ثانیه) قبلاً به طور کامل انجام شده است. همچنین `unzip` مستقیم روی آرشیو چندبخشی با خطای `BadZipFile` شکست می‌خورد.",
    strictRuleForAgent:
      "هرگز `ocr_book.py` را از صفر روی کتاب زیست اجرا نکن! مستقیماً از فایل‌های JSON و جعبه‌های کلمه موجود در `app/content/source/` استفاده کن.",
  },
  {
    id: "DE_02_NO_FAKE_PHONE_CHROME_OR_TYPO_DEMO",
    category: "رابط کاربری و CSS",
    whatFailedBefore: "بیلد `543a20ba` که کاربر آن را «فاجعه» خواند و رد کرد.",
    whyItFailed:
      "ایجنت یک کادر شبیه‌ساز موبایل با نوار وضعیت جعلی `9:41` و پنل‌های ادمین دور اپ کشیده بود و داخل صفحه درس، همان متن تست چیدمان خط («گاهی لازم است متن‌ها را با شکستن خطوط…») را نشان می‌داد.",
    strictRuleForAgent:
      "هیچ نوار وضعیت جعلی، کادر دور گوشی یا پنل دیباگ قابل رویت در محصول نهایی نگذار. متن درسنامه منحصراً باید از بلوک‌های تایپ‌شده `STRUCTURED_PACKAGE.json` رندر شود.",
  },
  {
    id: "DE_03_PROTO_CSS_ROOT_TRAP",
    category: "رابط کاربری و CSS",
    whatFailedBefore: "بهم ریختن عرض دکمه Continue به ۱۸۰px و کار نکردن ارتفاع ۶dp نوار پیشرفت.",
    whyItFailed:
      "پنج متغیر مصوب (`--sp-m`, `--sp-s`, `--toolbar`, `--progressbar`, `--radius-card`) در فایل محافظت‌شده `proto.css` بیرون از بلاک `:root` افتاده بودند و مرورگر آن‌ها را نادیده می‌گرفت!",
    strictRuleForAgent:
      "فایل `proto.css` را دستکاری نکن (تا هش `verify_app.py` نشکند)؛ در عوض آن ۵ متغیر را در `:root` فایل `app/assets/native.css` نگه دار و از `calc(100% - var(--sp-m) - var(--sp-m))` استفاده کن.",
  },
  {
    id: "DE_04_SILENT_PROTO_NAV_CATCH",
    category: "رابط کاربری و CSS",
    whatFailedBefore: "باگ‌های ناوبری بدون هیچ خطایی در کنسول مرورگر بلعیده می‌شدند.",
    whyItFailed:
      "در فایل `proto-ui.js`، تابع `go()` فراخوانی هوک را داخل `try { window.PROTO_NAV(name) } catch(e) {}` قرار داده است و خطاها را بی‌صدا قورت می‌دهد!",
    strictRuleForAgent:
      "هنگام تست و دیباگ ناوبری، مستقیماً `window.PROTO_NAV(name)` را در تست‌ها فراخوانی کن تا هرگونه استثنا فوراً آشکار شود.",
  },
  {
    id: "DE_05_PERSIAN_NORMALISER_TRAP",
    category: "موتور درس و DSL",
    whatFailedBefore: "رد شدن پاسخ‌های تایپ‌شده فارسی در تعامل‌های `fillTheGap` و `validatedInput` (`Q-44`).",
    whyItFailed:
      "نرمال‌ساز اصلی میمو (`qm.i.a`) فقط `toLowerCase(Locale.US)` انجام می‌دهد و تفاوت «ی/ي»، «ک/ك»، نیم‌فاصله (`\\u200c`)، اعراب و ارقام فارسی/انگلیسی (`۰-۹` در برابر `0-9`) را در نظر نمی‌گیرد.",
    strictRuleForAgent:
      "برای ورودی‌های انگلیسی/کد، تابع `normalise()` را بایت‌به‌بایت طبق `04_SPEC` نگه دار تا ۵۴ تست `grading_vectors.json` پاس شوند؛ اما قبل از مقایسه رشته‌های فارسی، لایه یکسان‌ساز یونیکد فارسی (`normalizePersianText`) را اعمال کن.",
  },
  {
    id: "DE_06_SW_INJECTION_STRING_CORRUPTION",
    category: "محیط و ابزار",
    whatFailedBefore: "خراب شدن فایل باندل `index.html` با `SyntaxError` هنگام تزریق اسکریپت Service Worker.",
    whyItFailed:
      "استفاده از `html.replace('</body>', swScript, 1)` در پایتون اولین رشته `'</body>'` را که داخل کد جاوااسکریپت باندل‌شده بود جایگزین کرد، نه تگ پایانی سند را!",
    strictRuleForAgent:
      "در بیلدر تک‌فایلی (`build_output.py`)، همیشه از `rfind('</body>')` برای تزریق در انتهای سند استفاده کن و نبود لیترال `</script` داخل JSON/JS اینلاین‌شده را assert نما.",
  },
  {
    id: "DE_07_NO_BROAD_RUNTIME_RE_MISSIONS",
    category: "مهندسی معکوس و سرور",
    whatFailedBefore: "تلاش برای اجرای شبیه‌ساز اندروید روی سندباکس بدون KVM یا هوک‌های کورکورانه Frida (`M03/M07`).",
    whyItFailed:
      "طبق گزارش `FINAL_UNKNOWN_REGISTER.md`، تمام استخراج استاتیک و رانتایم ممکن انجام شده است و موارد باقی‌مانده سرور (`SERVER CONFIRMED = 0`) نیازمند سرور خصوصی میمو هستند نه تحلیل بایت‌کد بیشتر.",
    strictRuleForAgent:
      "هرگز وقت را صرف مهندسی معکوس مجدد APK نکن! از مشخصات قطعی `HANDOFF/01..15` و قوانین محلی `ADD-01..ADD-08` برای ساخت موتور استفاده کن.",
  },
];
