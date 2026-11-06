import type { DeliverableTask } from "@/db/schema";

export interface SeedPhaseSpec {
  phaseNumber: number;
  code: string;
  title: string;
  subtitle: string;
  weightPct: number;
  status: "verified" | "completed" | "in_progress" | "pending";
  category: string;
  estimatedTurns: string;
  sourceBranchRefs: string[];
  prerequisites: string[];
  objective: string;
  architecturalDeepDive: string;
  deliverables: DeliverableTask[];
  targetFiles: string[];
  antiDriftRules: string[];
  verificationCommands: string[];
  agentPrompt: string;
}

export const MASTER_AUTONOMOUS_AGENT_PROMPT = `# نقش تو: سرمهندس ارشد و ایجنت خودران ساخت پلتفرم کنکور-میمو × لرن‌هارنس
# ریپوزیتوری هدف: https://github.com/danmillman008-hub/game.git

تو یک ایجنت مهندسی نرم‌افزار خودران هستی که وظیفه داری پروژه «کنکور-میمو (Konkur-Mimo × LearnHarness)» را بدون نیاز به هیچ‌گونه جهت‌دهی انسانی از وضعیت فعلی (پروتوتایپ‌های تکهتکه در شاخه‌های گیت و فایل‌های زیپ) به محصول نهایی، یکپارچه و ۱۰۰٪ کارا برسانی.

## ۱. نقشه توپولوژی ریپو (قبل از نوشتن حتی یک خط کد بخوان!)
در این ریپو دو شاخه اصلی مهندسی و چند فایل زیپ وجود دارد که باید آن‌ها را به هم ببافی، و چند فایل نامرتبط هست که باید کاملاً نادیده بگیری:
- **فایل‌ها و شاخه‌های ممنوعه (کاملاً نادیده بگیر و وارد بیلد نکن):**
  1. \`pharmacy-inventory (3).html\` و \`ttac-4.3.6.apk\` و شاخه \`origin/arena/dd2b6beb-game\` (پروژه انبارداری داروخانه و تیتک — هیچ ربطی به پروژه ما ندارد).
  2. \`Streets-of-Rage_Genesis_EN.zip\` و شاخه‌های \`eb3b2453-game\` / \`f84369df-game\` / \`e3952d18-game\`.
- **منابع حقیقت پروژه کنکور-میمو (قطعات پازل که باید یکپارچه شوند):**
  1. **شاخه \`origin/arena/ecb8af07-game\` (\`HANDOFF/01..15\` و \`mimo-re/\`):** مشخصات مهندسی معکوس بایت‌به‌بایت اپ Mimo 9.35 (\`com.getmimo\`, SHA-256 \`48ce1740…\`) شامل گرامر ۲۷ تگ DSL (\`dsl_grammar.ebnf\`)، نرمال‌ساز و تصحیح‌گر دقیق (\`04_SPEC\` + ۵۴ بردار \`grading_vectors.json\`)، اسکیمای ۳ جدول SQLite Room v2 (\`mimo.db\` + \`progress_vectors.json\`)، و تصمیمات \`D-01..D-45\` و \`ADD-01..ADD-08\`.
  2. **شاخه \`origin/arena/aebb90b7-game\` (\`mimo-ui/\`, \`ANALYSIS/MISSION_05..09\`, \`app/\`, \`docs/00..10\`):** پروتوتایپ مصوب کاربر \`v12.5-fa\` (\`mimo-ui/UPGRADE/DESIGN/index.html\` با SHA \`c356068d…\`)، قوانین \`F2\` و \`F10–F47\` (۵ تب فارسی، ۳ چیپ بالا، گره‌های ۹۲dp با قوس Q، هاب آزمون ۷بخشی با تفکیک پاسخبرگ و پاسخنامه)، پوسته ناوبری بومی M09 (\`app/native/index.html\` و \`app/src/native.js\`)، خط لوله OCR کتاب زیست دوازدهم (\`848/848\` صفحه، \`694,860\` جعبه کلمه در \`app/tools/process_book.py\`) و پل \`LearnHarness\` (\`app/src/harness.js\`).
  3. **موتور هم‌ریختی پداگوژیک کنکور (\`build-konkur-pedagogical-ai-agent.zip\` → \`pedagogy-engine.ts\`) و موتور ریاضی تطبیقی (\`comprehensive-software-development-roadmap.zip\` → \`algorithms.ts\`):** تبدیل گام‌های کدنویسی میمو به مکانیک‌های کنکوری (\`concept_bite\`, \`guided_cloze\`, \`token_assembly\`, \`trap_detector\`, \`konkur_test\`) با گاردریل‌های ۱۰گانه \`M1–M10\` و الگوریتم‌های \`KST Outer Fringe\` + \`Calibrated BKT\` + \`FSRS-5\` + \`Flow-Band 70%–85%\`.

## ۲. قوانین آهنین معماری (هرگز نقض نکن!)
1. **وفاداری ۱۰۰٪ به طرح مصوب \`v12.5-fa\`:** ۵ تب دقیق («یادگیری / تمرین / هوش مصنوعی / امتیازها / پروفایل»)، ۳ چیپ بالا (سکه / کلید ∞ / استریک)، توکن‌های رنگ ARSC (\`#F6F7FB\` روز، \`#252746\` شب، \`#7E4BDE\` دکمه اصلی، \`#8D60E2\` نوار پیشرفت ۶dp)، بدون نوار وضعیت جعلی گوشی و بدون هیچ صفحه Onboarding اضافی (\`F18\`).
2. **ممنوعیت مطلق متن دموی چیدمان و سوالات تصادفی:** هرگز پاراگراف «گاهی لازم است متن‌ها را با شکستن خطوط…» از \`phone.html\` را به عنوان درسنامه نشان نده و هرگز با هش کردن ID درس، سوال تصادفی به درس نچسبان! هر فصل باید دقیقاً از \`STRUCTURED_PACKAGE.json\` با ۶ نقش (\`hook → check → feedback → explain → practice → recap\`) و نگاشت قطعی \`curriculumId\` خوانده شود.
3. **قوانین تکمیل محلی (\`ADD-03\` و \`ADD-04\`):** از آنجا که در میمو اصلی \`SERVER CONFIRMED = 0\` است، اتمام فصل و باز شدن گره‌ها در کلاینت بر اساس \`tries >= 1\` روی تمام ریزدرس‌های فصل محاسبه می‌شود و تاریخچه \`lesson_progress\` هرگز پس از سینک پاک نمی‌شود.
4. **صداقت محتوایی و منبعی:** هیچ جمله علمی خارج از کتاب درسی اختراع نکن. تمام درسنامه‌ها باید دارای \`trace.sourceRef\` به صفحه و شماره سوال کتاب درسی باشند.

## ۳. پروتکل اجرای گام‌به‌گام (Phase-by-Phase Execution Loop)
مراحل را به ترتیب از **فاز ۰ تا فاز ۱۱** طبق وزن‌دهی زیر اجرا کن. در پایان هر فاز، **تمامی دستورات بخش \`Verification Gate\`** را اجرا کن. تا وقتی خروجی تمام تست‌های یک فاز ۱۰۰٪ سبز نشده است، حق رفتن به فاز بعدی را نداری. از کاربر هیچ سوالی نپرس؛ تصمیمات مهندسی در این سند به طور کامل تعیین شده‌اند.`;

export const SEED_EXECUTION_PHASES: SeedPhaseSpec[] = [
  {
    phaseNumber: 0,
    code: "PHASE_00",
    title: "فاز ۰: یکپارچه‌سازی شاخه‌های گیت، قرنطینه فایل‌های داروخانه و تثبیت ساختار مونوریپو",
    subtitle: "Branch Unification (aebb90b7 + ecb8af07) & Quarantine of Unrelated Pharmacy/Game Files",
    weightPct: 5,
    status: "verified",
    category: "زیرساخت و یکپارچه‌سازی ریپو",
    estimatedTurns: "۳ تا ۵ گام اجرایی ایجنت",
    sourceBranchRefs: [
      "origin/arena/aebb90b7-game",
      "origin/arena/ecb8af07-game",
      "build-konkur-pedagogical-ai-agent.zip",
    ],
    prerequisites: ["دسترسی به ریپوی گیت danmillman008-hub/game"],
    objective:
      "ادغام بدون تداخل دارایی‌های مهندسی معکوس شاخه `ecb8af07-game` (`HANDOFF/` و `mimo-re/`) با اپلیکیشن و خط لوله OCR شاخه `aebb90b7-game` (`mimo-ui/`, `ANALYSIS/`, `app/`, `docs/`) و قرنطینه کامل فایل‌های نامرتبط داروسازی (`ttac-4.3.6.apk`, `pharmacy-inventory (3).html`) و بازی سگا.",
    architecturalDeepDive:
      "مشکل اصلی ریپوی فعلی این است که بهترین مشخصات فنی موتور میمو (گرامر EBNF، ۵۴ بردار تصحیح `grading_vectors.json` و اسکیمای Room v2) در شاخه `ecb8af07-game` قرار دارند، در حالی که بهترین رابط کاربری مصوب (`v12.5-fa`)، ناوبری بومی M09 و خروجی OCR کتاب زیست ۸۴۸ صفحه‌ای در شاخه `aebb90b7-game` هستند و موتور هم‌ریختی پداگوژیک کنکور داخل آرشیو زیپ در شاخه `main` افتاده است. در این فاز، همه این لایه‌ها در یک ساختار پوشه‌بندی استاندارد قرار می‌گیرند.",
    deliverables: [
      {
        id: "P0_D1",
        title: "قرنطینه فایل‌های نامرتبط داروسازی (ttac-4.3.6.apk، pharmacy-inventory.html) و Streets-of-Rage از مسیر بیلد و ایندکس ایجنت",
        specRef: "docs/04_CURRENT_STATE.md §1",
        done: true,
      },
      {
        id: "P0_D2",
        title: "انتقال پوشه HANDOFF/ (شامل 01..15 و data/*.json و tools/verify_handoff.py) از شاخه ecb8af07-game در کنار app/ و docs/ شاخه aebb90b7-game",
        specRef: "HANDOFF/START_HERE.md",
        done: true,
      },
      {
        id: "P0_D3",
        title: "حفظ بایت‌به‌بایت دارایی‌های مصوب دارای هش محافظت‌شده (mimo-ui/UPGRADE/DESIGN/index.html با SHA c356068d… و app/assets/proto.*)",
        specRef: "docs/02_DECISIONS.md §2–§3",
        done: true,
      },
      {
        id: "P0_D4",
        title: "به‌روزرسانی REPO_INDEX.json و اجرای همزمان verify_handoff.py + verify_docs.py + verify_app.py",
        specRef: "REPO_INDEX.json",
        done: true,
      },
    ],
    targetFiles: [
      "REPO_INDEX.json",
      "AGENTS.md",
      "CLAUDE.md",
      "HANDOFF/data/MANIFEST.json",
      "app/tools/verify_app.py",
      "docs/verify_docs.py",
    ],
    antiDriftRules: [
      "هرگز به شاخه origin/arena/dd2b6beb-game (پروژه تیتک/داروخانه) سوئیچ نکن و هیچ کدی از آن برندار.",
      "فایل‌های محافظت‌شده mimo-ui/UPGRADE/DESIGN/index.html و app/assets/phone.html را ویرایش نکن تا هش‌های verify_app.py نشکنند.",
    ],
    verificationCommands: [
      "python3 HANDOFF/tools/verify_handoff.py",
      "python3 docs/verify_docs.py",
      "npm run verify --prefix app",
    ],
    agentPrompt: `فاز ۰ را اجرا کن:
۱. شاخه کاری را بر مبنای origin/arena/aebb90b7-game قرار بده و پوشه HANDOFF/ را از origin/arena/ecb8af07-game به ریشه پروژه بیاور (git checkout origin/arena/ecb8af07-game -- HANDOFF).
۲. فایل‌های pharmacy-inventory (3).html، ttac-4.3.6.apk و Streets-of-Rage_Genesis_EN.zip را در تمام اسکریپت‌های بیلد و ایندکس ایجنت در لیست سیاه (ignore) قرار بده تا هیچ ماژولی به آن‌ها ارجاع ندهد.
۳. بدون دست زدن به فایل‌های محافظت‌شده در mimo-ui/UPGRADE/DESIGN/index.html و app/assets/، ایندکس REPO_INDEX.json را به‌روز کن.
۴. دستورات تایید را اجرا کن:
   python3 HANDOFF/tools/verify_handoff.py
   python3 docs/verify_docs.py
   npm run verify --prefix app
تنها زمانی که هر سه دستور با موفقیت ۱۰۰٪ پاس شدند، پایان فاز ۰ را گزارش کن.`,
  },
  {
    phaseNumber: 1,
    code: "PHASE_01",
    title: "فاز ۱: بستن پرونده مهندسی معکوس میمو ۹٫۳۵ و پیاده‌سازی قوانین جایگزین سرور (ADD-01..08)",
    subtitle: "Closing Static/Runtime RE Gaps, Persian Normaliser (Q-44) & Local Completion Rules (ADD-04)",
    weightPct: 8,
    status: "verified",
    category: "مهندسی معکوس و قوانین هسته",
    estimatedTurns: "۴ تا ۶ گام اجرایی ایجنت",
    sourceBranchRefs: [
      "HANDOFF/04_SPEC_INTERACTION_AND_GRADING.md",
      "HANDOFF/05_SPEC_LEARNER_MODEL.md",
      "HANDOFF/12_DELTA_REGISTER.md",
      "HANDOFF/13_KNOWN_UNKNOWNS.md",
    ],
    prerequisites: ["PHASE_00"],
    objective:
      "تبدیل نقاط بازمانده مهندسی معکوس (`SERVER CONFIRMED = 0`, `Q-44` نرمال‌ساز فارسی، `Q-140` پل WebView و `ADD-01..ADD-08`) به کدهای قطعی و تست‌شده در موتور محلی بدون نیاز به سرور خصوصی میمو.",
    architecturalDeepDive:
      "در اپ اصلی میمو ۹٫۳۵، کلاینت فقط پاسخ را تصحیح می‌کند (`qm.i.a`) و ردیف ۱۱ فیلدی `LessonProgress` را با `in_queue = 1` می‌سازد؛ اما محاسبه اینکه «آیا فصل تمام شد؟»، «چند سکه و استریک بدهیم؟» و «کدام گره باز شود؟» روی سرور میمو انجام می‌شد و رکوردهای محلی پس از `POST` پاک می‌شدند (`C-22`). در این فاز، ما هر ۸ قانون `ADD-01` تا `ADD-08` از `HANDOFF/12_DELTA_REGISTER.md` را پیاده‌سازی می‌کنیم و باگ `Q-44` (عدم پشتیبانی نرمال‌ساز میمو از ی/ک عربی، نیم‌فاصله و اعداد فارسی) را حل می‌نماییم.",
    deliverables: [
      {
        id: "P1_D1",
        title: "پیاده‌سازی بایت‌به‌بایت نرمال‌ساز qm.i.a (حفظ حروف، اعداد و فقط علائم <>():{},.) + لایه یکسان‌ساز فارسی (Q-44: تبدیل ي/ك به ی/ک، حذف نیم‌فاصله و تبدیل ارقام ۰-۹ به 0-9)",
        specRef: "HANDOFF/04_SPEC §2 & Q-44",
        done: true,
      },
      {
        id: "P1_D2",
        title: "پیاده‌سازی قانون ADD-04 (Local Completion Boundary): فصل زمانی تکمیل می‌شود که تمامی ریزدرس‌های آن دارای tries >= 1 باشند؛ درسنامه (Tutorial) زمانی تکمیل می‌شود که تمامی فصل‌هایش کامل شوند",
        specRef: "HANDOFF/05_SPEC §7 & ADD-04",
        done: true,
      },
      {
        id: "P1_D3",
        title: "پیاده‌سازی قانون ADD-03 (Non-Destructive Outbox): تغییر رفتار sync از DELETE رکورد به synced_at timestamp تا تاریخچه تحلیلی داوطلب کنکور روی دستگاه پاک نشود",
        specRef: "HANDOFF/05_SPEC §6 & ADD-03",
        done: true,
      },
      {
        id: "P1_D4",
        title: "بستن شکاف U-WEB-001 / Q-140: پیاده‌سازی پل ارتباطی امن postMessage برای بلوک‌های <webview interaction=\"feedback|unlock\"> با ۵ رویداد استاندارد محلی",
        specRef: "HANDOFF/08_SPEC §3 & R5",
        done: true,
      },
    ],
    targetFiles: [
      "app/src/content-engine.js",
      "app/src/engine.js",
      "HANDOFF/tools/reference_engine.py",
      "app/tests/unit.test.mjs",
    ],
    antiDriftRules: [
      "رفتار نرمال‌ساز روی ورودی‌های انگلیسی/کد نباید تغییر کند؛ هر ۵۴ تست فایل HANDOFF/data/grading_vectors.json و progress_vectors.json باید ۱۰۰٪ سبز بمانند.",
      "فیلد tries یک شمارنده افزایشی نیست! طبق بایت‌کد میمو tries فقط پرچم حل شدن (0 یا 1) است و isSolvedCorrectly معادل tries >= 1 است؛ تعداد تلاش‌های نشست در فیلد attempts ثبت می‌شود.",
    ],
    verificationCommands: [
      "python3 -m pytest -q HANDOFF/tests",
      "npm test --prefix app",
    ],
    agentPrompt: `فاز ۱ (بستن مهندسی معکوس و قوانین ADD-01..08) را اجرا کن:
۱. در موتور تصحیح (app/src/content-engine.js و src/lib/mimo/engine.ts)، الگوریتم نرمال‌ساز qm.i.a را دقیقاً مطابق HANDOFF/04_SPEC_INTERACTION_AND_GRADING.md §2 پیاده کن و لایه نرمال‌ساز یونیکد فارسی (رفع Q-44: یکسان‌سازی ی/ي، ک/ك، حذف نیم‌فاصله \\u200c و تبدیل اعداد فارسی/عربی به انگلیسی) را به آن اضافه کن به طوری که هر ۵۴ بردار تست grading_vectors.json و تست‌های فارسی هر دو پاس شوند.
۲. قوانین ADD-03 (حفظ تاریخچه محلی پس از سینک outbox) و ADD-04 (قانون تکمیل محلی فصل و درسنامه بر مبنای tries >= 1) را مطابق HANDOFF/05_SPEC_LEARNER_MODEL.md پیاده‌سازی کن.
۳. پل پیام‌رسان محلی WebView (بستن Q-140 / U-WEB-001) را برای رویدادهای feedback و unlock بدون هیچ وابستگی به شبکه خارجی پیاده کن.
۴. تست‌های HANDOFF/tests و npm test --prefix app را اجرا و سبز بودن ۱۰۰٪ را تایید کن.`,
  },
  {
    phaseNumber: 2,
    code: "PHASE_02",
    title: "فاز ۲: معماری کد کلاینت و بک‌اند (هسته ایزومورفیک TypeScript/ESM + پوسته اندروید Kotlin/PWA + سرور PostgreSQL)",
    subtitle: "Client & Backend Software Architecture: Isomorphic Core + Kotlin/Android Wrapper + Next.js/PostgreSQL Backend",
    weightPct: 8,
    status: "verified",
    category: "معماری نرم‌افزار و پشته فنی",
    estimatedTurns: "۴ تا ۶ گام اجرایی ایجنت",
    sourceBranchRefs: [
      "HANDOFF/10_BUILD_THE_MIMO_PROJECT.md",
      "app/docs/ARCHITECTURE.md",
      "rebuild-complete-software-application.zip",
    ],
    prerequisites: ["PHASE_01"],
    objective:
      "پاسخ مهندسی قطعی به این سوال که «نرم‌افزار باید با کاتلین نوشته شود یا وب و چطور به بک‌اند وصل شود؟»: پیاده‌سازی معماری ۳ لایه تمیز (Clean Hexagonal Architecture) که هسته آن هم به صورت آفلاین تک‌فایلی/PWA/اندروید کار می‌کند و هم به بک‌اند PostgreSQL و گیت‌وی هوش مصنوعی متصل می‌شود.",
    architecturalDeepDive:
      "اپ اصلی میمو ۹٫۳۵ در سال‌های گذشته با Kotlin + Jetpack Compose + Room SQLite v2 + WebView داخلی نوشته شده بود؛ اما همان‌طور که در مهندسی معکوس مشخص شد، کل درسنامه‌های میمو فایل‌های HTML-DSL (`<!DOCTYPE html><html><body>...`) هستند که به کامپوننت‌های بصری ترجمه می‌شوند! بنابراین بهترین، سریع‌ترین و پایدارترین معماری برای تیم شما (که هم روی وب، هم به صورت فایل تک‌کلیکه `Mimo.html`، هم PWA آیفون/اندروید و هم APK اندروید کار کند) **معماری هسته ایزومورفیک (Isomorphic Offline-First Architecture)** است:\n" +
      "۱. **لایه هسته دامنه (`core/` — TypeScript/ESM بدون وابستگی به DOM):** شامل پارسر DSL، تصحیح‌گر `qm.i.a`، ماشین وضعیت `LessonProgress`، الگوریتم‌های `KST/BKT/FSRS-5` و موتور `LearnHarness`.\n" +
      "۲. **لایه رابط کاربری و کلاینت (`app/native/` + Next.js App Router + Android Kotlin WebView/Capacitor Shell):** پوسته دقیق `v12.5-fa` که در مرورگر/PWA با `localStorage/IndexedDB` و در اندروید با پل SQLite Room v2 (`mimo.db`) کار می‌کند.\n" +
      "۳. **لایه بک‌اند و گیت‌وی هوش مصنوعی (`src/app/api/` + Drizzle ORM + PostgreSQL):** مسئول دریافت صف `in_queue`، ذخیره کارنامه‌های آزمون، کامپایل کتاب‌های جدید و استریم SSE برای `LearnHarness`.",
    deliverables: [
      {
        id: "P2_D1",
        title: "ایجاد تفکیک سخت‌گیرانه بین لایه Core Engine (DOM-free)، لایه UI Adapter (v12.5-fa) و لایه Persistence/Sync",
        specRef: "HANDOFF/10_BUILD §0 & app/docs/ARCHITECTURE.md",
        done: true,
      },
      {
        id: "P2_D2",
        title: "تعریف اینترفیس واحد StorageAdapter که هم روی localStorage/IndexedDB آفلاین و هم روی SQLite Room v2 / PostgreSQL کار کند",
        specRef: "HANDOFF/06_SPEC_STORAGE.md",
        done: true,
      },
      {
        id: "P2_D3",
        title: "تعریف اسکیمای کامل Drizzle PostgreSQL در src/db/schema.ts منطبق با ۳ جدول Room میمو + جداول کنکور و LearnHarness",
        specRef: "src/db/schema.ts",
        done: true,
      },
      {
        id: "P2_D4",
        title: "مستندسازی و ساخت قالب پروژه Android Kotlin WebView/Room Bridge برای خروجی APK بومی از باندل آفلاین",
        specRef: "app/docs/OUTPUT_GUIDE.md",
        done: true,
      },
    ],
    targetFiles: [
      "src/db/schema.ts",
      "src/db/index.ts",
      "app/src/store.js",
      "app/src/engine.js",
    ],
    antiDriftRules: [
      "هرگز منطق تصحیح درس یا محاسبه پیشرفت را داخل کامپوننت‌های UI یا کنترلرهای DOM ننویس؛ تمام منطق باید در توابع خالص (Pure Functions) قابل تست در Node.js باشد.",
      "کلاینت آفلاین (Mimo.html) باید بدون نیاز به اجرای سرور بک‌اند هم ۱۰۰٪ کار کند (Offline-First Degradation).",
    ],
    verificationCommands: [
      "npx drizzle-kit push",
      "npm exec tsc -- --noEmit",
      "npm test --prefix app",
    ],
    agentPrompt: `فاز ۲ (معماری ۳ لایه کلاینت/بک‌اند و دیتابیس) را اجرا کن:
۱. اطمینان حاصل کن که تمام منطق دامنه (DSL parser, grader, learner progress, KST/FSRS-5) مستقل از DOM و قابل اجرا در هر دو محیط مرورگر/WebView و سرور Node.js باشد.
۲. اسکیمای PostgreSQL در src/db/schema.ts را با npx drizzle-kit push روی دیتابیس اعمال کن.
۳. اینترفیس ذخیره‌ساز محلی (app/src/store.js) را طوری تنظیم کن که در حالت آفلاین ۱۰۰٪ مستقل کار کند و در صورت وجود بک‌اند، ردیف‌های دارای in_queue = 1 را بدون حذف تاریخچه سینک نماید.
۴. دستورات تایید را اجرا کن:
   npx drizzle-kit push
   npm exec tsc -- --noEmit
   npm test --prefix app`,
  },
  {
    phaseNumber: 3,
    code: "PHASE_03",
    title: "فاز ۳: پیاده‌سازی کامل پارسر ۲۷ تگ DSL میمو و هر ۹ خانواده رندرر تعاملی (R4–R6)",
    subtitle: "Full 27-Tag EBNF Lesson DSL Parser + All 9 Interactive Renderer Families + 3-State Feedback Gating",
    weightPct: 10,
    status: "in_progress",
    category: "موتور درس و رندررهای DSL",
    estimatedTurns: "۶ تا ۸ گام اجرایی ایجنت",
    sourceBranchRefs: [
      "HANDOFF/03_SPEC_LESSON_DSL.md",
      "HANDOFF/04_SPEC_INTERACTION_AND_GRADING.md",
      "HANDOFF/data/dsl_grammar.ebnf",
      "docs/05_ROADMAP.md (R4, R5, R6)",
    ],
    prerequisites: ["PHASE_01", "PHASE_02"],
    objective:
      "تکمیل پارسر DSL میمو در `app/src/content-engine.js` برای پوشش کامل گرامر `dsl_grammar.ebnf` و پیاده‌سازی ۴ رندرر باقی‌مانده در نقشه راه (`validatedInput`, `InteractiveWebView`, `Reveal`, `executableFiles`) به همراه ۲ تگ علمی کنکور (`<math>` و `<diagram>`).",
    architecturalDeepDive:
      "طبق بررسی `docs/04_CURRENT_STATE.md` §5، در حال حاضر فقط ۵ خانواده رندرر (`text`, `strong`, `MultipleChoice`, `fillTheGap`, `feedback`) در `content-engine.js` پیاده شده‌اند و ۴ خانواده مهم دیگر (`validatedInput`, `InteractiveWebView`, `Reveal`, `executableFiles`) ناقص هستند. در این فاز:\n" +
      "۱. رندرر `validatedInput` با پشتیبانی از `startIndex` و `endIndex` داخل بلوک `<code>` و حکم سه‌حالته (`CORRECT` اگر متن خام برابر باشد، `PARTIAL` اگر فقط نرمال‌شده برابر باشد — مثلاً فراموش کردن نیم‌فاصله یا علامت، و `INCORRECT`) ساخته می‌شود.\n" +
      "۲. دروازه نمایش `visible-if=\"always | correct | wrong\"` روی تمام بلوک‌های `<p>` و بازخورد اعمال می‌گردد تا پس از زدن دکمه Continue/Run، کادر سبز `jm.m` (پاسخ درست)، کادر زرد `jm.n` (پاسخ ناقص/نزدیک) یا کادر قرمز `jm.o` (پاسخ غلط + بررسی سایر گزینه‌ها + دکمه کمک هوش مصنوعی) نمایش داده شود.",
    deliverables: [
      {
        id: "P3_D1",
        title: "تکمیل پارسر AST منطبق با HANDOFF/data/dsl_ast_schema.json برای ۲۷ تگ اصلی میمو + ۲ تگ <math> و <diagram>",
        specRef: "HANDOFF/03_SPEC_LESSON_DSL.md §2–§6",
        done: true,
      },
      {
        id: "P3_D2",
        title: "پیاده‌سازی رندرر و ولیدیتور validatedInput با اسلات متنی هایلایت‌شده (startIndex..endIndex) و فیدبک PARTIAL (R4)",
        specRef: "docs/05_ROADMAP.md R4 & HANDOFF/04_SPEC §3",
        done: false,
      },
      {
        id: "P3_D3",
        title: "پیاده‌سازی رندرر بلوک‌های Reveal (کارت کشف تدریجی نکته)، executableFiles و جدول‌های مقایسه‌ای <database>/<table> (R6)",
        specRef: "docs/05_ROADMAP.md R6",
        done: false,
      },
      {
        id: "P3_D4",
        title: "پیاده‌سازی رندرر محلی InteractiveWebView (بدون شبکه خارجی) برای نمودارها و آزمایشگاه‌های تعاملی زیست و شیمی (R5)",
        specRef: "docs/05_ROADMAP.md R5",
        done: false,
      },
      {
        id: "P3_D5",
        title: "اعمال دقیق visible-if سه حالته (always / correct / wrong) و ولیدیتورهای استاتیک A6 تا A11 روی تمام ریزدرس‌ها",
        specRef: "app/docs/MIMO_CONTENT_MODEL.md",
        done: true,
      },
    ],
    targetFiles: [
      "app/src/content-engine.js",
      "app/src/native.js",
      "app/assets/native.css",
      "app/tests/unit.test.mjs",
      "app/tests/output.test.mjs",
    ],
    antiDriftRules: [
      "حکم PARTIAL فقط برای validatedInput وجود دارد؛ سایر انواع تعامل (Selection, FillTheGap, MultipleChoice) دوحالته (CORRECT یا INCORRECT) هستند.",
      "در تعامل چندگزینه‌ای (<selection multiple=\"multiple\">)، قانون تصحیح All-or-Nothing است (همه گزینه‌های درست و هیچ گزینه غلطی نباید انتخاب شده باشد).",
    ],
    verificationCommands: [
      "npm test --prefix app",
      "python3 -m pytest -q HANDOFF/tests",
      "npm run verify --prefix app",
    ],
    agentPrompt: `فاز ۳ (تکمیل پارسر ۲۷ تگ DSL و ۹ خانواده رندرر R4–R6) را اجرا کن:
۱. در فایل app/src/content-engine.js و app/src/native.js، ۴ خانواده رندرر باقی‌مانده از نقشه راه (R4: validatedInput با حکم سه‌حالته CORRECT/PARTIAL/INCORRECT، R5: InteractiveWebView محلی بدون شبکه، R6: بلوک‌های Reveal و executableFiles و <table>/<database>) به همراه تگ‌های علمی <math> و <diagram> را پیاده‌سازی کن.
۲. دروازه نمایش visible-if="always|correct|wrong" و وضعیت‌های بازخورد سه گانه (jm.m, jm.n, jm.o) را روی تمام بلوک‌ها اعمال کن.
۳. برای هر ۹ خانواده رندرر در app/tests/unit.test.mjs تست رندر و تصحیح بنویس.
۴. دستورات تایید را اجرا کن:
   npm test --prefix app
   python3 -m pytest -q HANDOFF/tests
   npm run verify --prefix app`,
  },
  {
    phaseNumber: 4,
    code: "PHASE_04",
    title: "فاز ۴: مهندسی هم‌ریختی پداگوژیک میمو به کنکور و گاردریل‌های ۱۰گانه (M1–M10)",
    subtitle: "Mimo-to-Konkur Pedagogical Isomorphism Engine: Converting Code Mechanics into Konkur Concept/Trap Mechanics",
    weightPct: 12,
    status: "in_progress",
    category: "پداگوژی کنکور و گاردریل‌های محتوا",
    estimatedTurns: "۵ تا ۷ گام اجرایی ایجنت",
    sourceBranchRefs: [
      "build-konkur-pedagogical-ai-agent.zip (src/lib/pedagogy-engine.ts)",
      "app/content/PEDAGOGY.md",
      "app/content/MIMO_INFORMATION_FORM.json",
    ],
    prerequisites: ["PHASE_03"],
    objective:
      "حل قطعی مشکل «درسنامه‌های خشک و فرانکنشتاینی»: ترکیب موتور گاردریل پداگوژیک (`M1–M10` از `pedagogy-engine.ts`) با چرخه ۶ نقشی میمو (`hook → check → feedback → explain → practice → recap`) تا هر درس کنکور دقیقاً همان حس اعتیادآور ساختن و دیباگ کردن کد در میمو را داشته باشد.",
    architecturalDeepDive:
      "چرا میمو در آموزش پایتون اعتیادآور است ولی کپی‌های معمولی آن در کنکور کسل‌کننده می‌شوند؟ چون در میمو میانگین طول هر ریزدرس فقط **۲۱٫۲ کلمه** است (`PEDAGOGY.md`) و کاربر هر ۱۵ ثانیه یک عمل سازنده انجام می‌دهد! در این فاز، ما ۵ مکانیک هم‌ریخت کنکوری را مستقیماً به تگ‌های DSL میمو مقید می‌کنیم:\n" +
      "۱. **`hook` & `explain` ← مکانیک `concept_bite` (گاردریل M1/M2):** حداکثر ۲۰ تا ۸۵ کلمه در هر صفحه، با هایلایت قیدهای کنکوری داخل `<strong>` و ممنوعیت دیوار متنی.\n" +
      "۲. **`check` ← مکانیک `guided_cloze` روی `<interaction type=\"fillTheGap\">` (گاردریل M5):** جای خالی منحصراً باید روی **قیدهای تصمیم‌ساز کنکور** («همه»، «برخی»، «اغلب»، «به‌جز»، «مستقیماً»، «بدون دخالت») یا متغیر کلیدی فرمول بنشیند، نه کلمات ربط تصادفی!\n" +
      "۳. **`practice` (نوع ۱) ← مکانیک `token_assembly` روی `<code>` + `<interaction>` (گاردریل M4):** چیدمان ترتیبی مراحل یک فرآیند زیستی (مثلاً مراحل رونویسی یا انقباض سارکومر) یا زنجیره استوکیومتری شیمی با حضور حداقل ۱ بلوک انحرافی تله‌دار.\n" +
      "۴. **`practice` (نوع ۲) ← مکانیک `trap_detector` (دیباگر کنکوری):** نمایش یک گزاره ترکیبی ۴ بخشی کنکور داخل بلوک کد/متن و پیدا کردن دقیقاً همان کلمه/قیدی که طراح کنکور به عنوان «تله» عوض کرده است.\n" +
      "۵. **`feedback` & `recap` ← ماتریس `optionDiagnostics` (گاردریل M6/M9):** کالبدشکافی هر ۴ گزینه (چرا گزینه ۱ تله تعمیم افراطی است، چرا گزینه ۳ تله جابجایی علت و معلول است) + تکنیک سرعتی رد گزینه (`eliminationShortcut`).",
    deliverables: [
      {
        id: "P4_D1",
        title: "ادغام ۱۰ گاردریل الگوریتمی M1 تا M10 (کنترل تعداد کلمات ≤۸۵، الزام قید کنکوری در جای خالی، الزام token_assembly و trap_detector، و ماتریس ۴ گزینه) در ولیدیتور محتوا",
        specRef: "pedagogy-engine.ts & app/tools/validate_content.py",
        done: true,
      },
      {
        id: "P4_D2",
        title: "تعریف مبدل رسمی (Isomorphic DSL Emitter) که ۵ مکانیک کنکوری را به تگ‌های استاندارد DSL میمو (<code>, <selection>, <interaction type=\"fillTheGap|validatedInput\">) ترجمه کند",
        specRef: "app/tools/emit_structured_package.py",
        done: true,
      },
      {
        id: "P4_D3",
        title: "پیاده‌سازی چرخه ۷ مرحله‌ای سختی و بازیابی (HOOK → CHECK → FEEDBACK → EXPLAIN → PRACTICE → RECAP + سطوح سختی challengeLevel 0..2 در R7)",
        specRef: "docs/05_ROADMAP.md R7 & app/content/PEDAGOGY.md",
        done: false,
      },
    ],
    targetFiles: [
      "app/tools/validate_content.py",
      "app/tools/emit_structured_package.py",
      "app/content/MIMO_INFORMATION_FORM.json",
      "src/lib/konkur-compiler.ts",
    ],
    antiDriftRules: [
      "هرگز اجازه نده یک ریزدرس بیش از ۸۵ کلمه متن پیوسته بدون تعامل داشته باشد (گاردریل M1).",
      "هرگز در بخش پاسخنامه تشریحی جمله کلیشه‌ای «طبق متن کتاب درسی گزینه X صحیح است» را بدون تحلیل گزینه‌های غلط نپذیر (گاردریل M9).",
    ],
    verificationCommands: [
      "python3 app/tools/validate_content.py app/content/STARTER_PACKAGE.json app/content/STRUCTURED_PACKAGE.json",
      "npm test --prefix app",
    ],
    agentPrompt: `فاز ۴ (مهندسی هم‌ریختی پداگوژیک میمو به کنکور و گاردریل‌های M1–M10) را اجرا کن:
۱. قوانین گاردریل M1 تا M10 (سقف ۸۵ کلمه در هر کارت، الزام نشستن fillTheGap روی قیدهای کنکوری همه/برخی/اغلب/به‌جز، تبدیل گام کدنویسی میمو به چیدمان بلوکی مسیرهای علمی token_assembly و شکارچی تله طراح trap_detector، و الزام ماتریس تشریح هر ۴ گزینه optionDiagnostics) را به app/tools/validate_content.py و emit_structured_package.py اضافه کن.
۲. سطوح دشواری (hardModeSelected, challengeLevel 0..2 طبق R7 در docs/05_ROADMAP.md) را در موتور محتوا فعال کن.
۳. دستورات تایید را اجرا کن:
   python3 app/tools/validate_content.py app/content/STARTER_PACKAGE.json app/content/STRUCTURED_PACKAGE.json
   npm test --prefix app`,
  },
  {
    phaseNumber: 5,
    code: "PHASE_05",
    title: "فاز ۵: خط لوله ۶ مرحله‌ای وارد کردن کتاب‌های درسی، اصلاح OCR دو ستونی و نگاشت قطعی (R1 & R2)",
    subtitle: "6-Stage Textbook & OCR Ingestion Pipeline: 2-Column RTL BBox Splitter, Persian Sanitizer & Deterministic chapterRefFor()",
    weightPct: 14,
    status: "pending",
    category: "خط لوله کتاب و منابع کنکور",
    estimatedTurns: "۶ تا ۹ گام اجرایی ایجنت",
    sourceBranchRefs: [
      "docs/05_ROADMAP.md (R1, R2)",
      "app/tools/process_book.py",
      "app/tools/emit_structured_package.py",
      "app/docs/MIMO_CONTENT_MODEL.md",
    ],
    prerequisites: ["PHASE_04"],
    objective:
      "اجرای کامل اولویت `P0` نقشه راه (`R1` و `R2`): تبدیل پیش‌نویس OCR کتاب زیست دوازدهم (`848` صفحه، `694,860` جعبه کلمه، `775` پاسخنامه) و هر منبع/جزوه جدید به بسته محتوای بازبینی‌شده (`reviewStatus: 'approved'`) و حذف کامل هش تصادفی در `chapterRefFor()`.",
    architecturalDeepDive:
      "این فاز مهم‌ترین بخش برای وارد کردن کتاب‌ها و منابع کنکور است. خط لوله ورود کتاب (`app/tools/process_book.py` و `/api/ingest`) دقیقاً از ۶ فیلتر پیاپی عبور می‌کند:\n" +
      "۱. **مرحله ۱ — تفکیک ستون‌های دوتایی راست‌به‌چپ (RTL Two-Column BBox De-columnizer):** صفحات کتاب‌های کمک‌درسی کنکور دو ستونی هستند. به جای خواندن خط‌به‌خط افقی کل صفحه، جعبه‌های کلمات (`word boxes`) بر اساس محور افقی `x_center` نسبت به خط میانی صفحه (`page_width / 2`) به دو لیست مجزا تقسیم می‌شوند: ابتدا **ستون راست** (`x_center >= page_width / 2`) از بالا به پایین (`y` صعودی) و سپس **ستون چپ** (`x_center < page_width / 2`) از بالا به پایین بازسازی می‌شود.\n" +
      "۲. **مرحله ۲ — پالایشگر دیکشنری زیست و علوم کنکور (Domain OCR Sanitizer):** اصلاح خودکار خطاهای پرتکرار Tesseract فارسی روی فونت‌های کتاب درسی (مانند `«یافته» ← «یاخته»`، `«هغز استفوان» ← «مغز استخوان»`، `«دی ان ای» ← «دنا (DNA)»`، `«آدنوزین تری فسفات»`، اصلاح شماره گزینه‌های `۱) ۲) ۳) ۴)` که با پرانتز برعکس افتاده‌اند).\n" +
      "۳. **مرحله ۳ — پیونددهنده هوشمند پاسخنامه تشریحی (Answer-Key Linker):** استخراج کلید صحیح (`correctIndex ∈ {0,1,2,3}`) و بخش «بررسی سایر گزینه‌ها» از صفحات پاسخنامه انتهای هر فصل و اتصال قطعی آن به شماره سوال مربوطه. هر سوالی که کلید آن پیدا نشود هرگز وارد بسته نهایی نمی‌شود (هیچ کلیدی حدس زده نمی‌شود!).\n" +
      "۴. **مرحله ۴ — کامپایلر ۶ نقشی میمو (`hook → check → feedback → explain → practice → recap`):** تبدیل هر مبحث و تست تاییدشده به ۶ ریزدرس پیوسته با فیلد اجباری `trace.sourceRef` (شماره صفحه و شماره تست کتاب).\n" +
      "۵. **مرحله ۵ — نگاشت قطعی `chapterRefFor()` (`R2`):** حذف کامل هرگونه `hashCode` یا انتخاب تصادفی؛ اتصال صریح هر یک از ۲۰ فصل و درسنامه‌ها به `curriculumId` ثابت.\n" +
      "۶. **مرحله ۶ — دروازه تایید و ارتقای وضعیت (`reviewStatus: 'approved'`):** اجرای `validate_content.py` و ارتقای `source.kind` به `'converted-book'`.",
    deliverables: [
      {
        id: "P5_D1",
        title: "ارتقای اسکریپت app/tools/process_book.py با الگوریتم تفکیک دو ستون راست/چپ مبتنی بر مختصات BBox و دیکشنری اصلاح واژگان زیست کنکور",
        specRef: "docs/05_ROADMAP.md R1",
        done: false,
      },
      {
        id: "P5_D2",
        title: "اتصال قطعی ۷۷۵ مدخل پاسخنامه تشریحی به سوالات، حذف سوالات فاقد کلید یا دارای join مشکوک، و تولید STRUCTURED_PACKAGE.json با reviewStatus: 'approved'",
        specRef: "docs/05_ROADMAP.md R1 & app/docs/MIMO_CONTENT_MODEL.md",
        done: false,
      },
      {
        id: "P5_D3",
        title: "بازنویسی کامل تابع chapterRefFor() در app/src/content-engine.js بر اساس جدول نگاشت صریح curriculumId بدون هیچ‌گونه hashCode یا random (R2)",
        specRef: "docs/05_ROADMAP.md R2",
        done: false,
      },
      {
        id: "P5_D4",
        title: "ایجاد اندپوینت و رابط کامپایلر منبع جدید (POST /api/blueprint/compile-lesson) برای وارد کردن سایر کتاب‌ها و جزوات (شیمی، فیزیک، ریاضی) با همان فرمت استاندارد",
        specRef: "app/content/MIMO_INFORMATION_FORM.json",
        done: true,
      },
    ],
    targetFiles: [
      "app/tools/process_book.py",
      "app/tools/emit_structured_package.py",
      "app/content/STRUCTURED_PACKAGE.json",
      "app/src/content-engine.js",
      "app/src/content-package.js",
      "app/tests/output.test.mjs",
    ],
    antiDriftRules: [
      "فایل‌های خام OCR و PDF در پوشه app/content/source/ دارای حق نشر هستند و در .gitignore قرار دارند؛ هرگز پوشه source/ را git add نکن!",
      "هرگز برای سوالی که در پاسخنامه کلید ندارد، به صورت تصادفی correctIndex انتخاب نکن؛ فقط سوالات دارای کلید قطعی و پاسخ تشریحی تاییدشده را وارد STRUCTURED_PACKAGE.json کن.",
    ],
    verificationCommands: [
      "python3 app/tools/process_book.py",
      "python3 app/tools/emit_structured_package.py",
      "python3 app/tools/validate_content.py app/content/STARTER_PACKAGE.json app/content/STRUCTURED_PACKAGE.json",
      "npm test --prefix app",
    ],
    agentPrompt: `فاز ۵ (خط لوله وارد کردن کتاب درسی R1 و نگاشت قطعی R2) را اجرا کن:
۱. در app/tools/process_book.py، الگوریتم بازسازی خطوط از word boxes را طوری ارتقا بده که ستون راست (x >= W/2) و ستون چپ (x < W/2) هر صفحه کاملاً جداگانه از بالا به پایین پردازش شوند و دیکشنری اصلاح خطاهای OCR زیست‌شناسی («یافته»→«یاخته»، «هغز استفوان»→«مغز استخوان» و ...) روی متن اعمال گردد.
۲. سوالات دارای پیوند قطعی با پاسخنامه تشریحی را استخراج کرده و از طریق app/tools/emit_structured_package.py فایل app/content/STRUCTURED_PACKAGE.json و app/src/content-package.js را با source.kind:'converted-book'، contentStatus:'reviewed' و reviewStatus:'approved' تولید کن.
۳. در app/src/content-engine.js، تابع chapterRefFor() را بازنویسی کن تا هیچ hashCode یا انتخاب تصادفی در آن نباشد و هر ورودی به طور قطعی به شناسه درسنامه خودش نگاشت شود (R2). یک تست واحد در app/tests/output.test.mjs اضافه کن که قطعی بودن ۱۰۰٪ نگاشت را اثبات کند.
۴. دستورات تایید را اجرا کن:
   python3 app/tools/emit_structured_package.py
   python3 app/tools/validate_content.py app/content/STARTER_PACKAGE.json app/content/STRUCTURED_PACKAGE.json
   npm test --prefix app`,
  },
  {
    phaseNumber: 6,
    code: "PHASE_06",
    title: "فاز ۶: دیتابیس پیشرفت ۱۱ فیلدی LessonProgress، صف مرور غلط‌های پایدار (R8) و سینک بک‌اند",
    subtitle: "11-Field LessonProgress Entity, Persistent Cross-Session Mistake Queue (R8) & Idempotent Backend Outbox Sync",
    weightPct: 9,
    status: "pending",
    category: "دیتابیس و وضعیت دانش‌آموز",
    estimatedTurns: "۴ تا ۶ گام اجرایی ایجنت",
    sourceBranchRefs: [
      "HANDOFF/05_SPEC_LEARNER_MODEL.md",
      "HANDOFF/06_SPEC_STORAGE.md",
      "docs/05_ROADMAP.md (R8)",
      "app/src/store.js",
    ],
    prerequisites: ["PHASE_02", "PHASE_05"],
    objective:
      "پیاده‌سازی کامل مدل وضعیت دانش‌آموز (`COMPLETE_LEARNER_STATE_SPEC.md` و `05_SPEC_LEARNER_MODEL.md`) شامل ردیف ۱۱ فیلدی `LessonProgress`، پایدارسازی صف مرور غلط‌ها (`inQueue`) بین نشست‌ها در `localStorage` و PostgreSQL (`R8`)، و تفکیک پاسخ مستقل (`unaided`) از پاسخ با کمک (`aided`).",
    architecturalDeepDive:
      "در میمو ۹٫۳۵، هر بار که داوطلب یک ریزدرس را حل می‌کند، یک رکورد ۱۱ فیلدی ساخته می‌شود:\n" +
      "`(lessonId, tutorialId, tutorialVersion, trackId, publishSetVersion=753, tries, attempts, startedAt, completedAt, isPracticeProgress, inQueue)`.\n" +
      "در این فاز، ما علاوه بر پاس کردن تمام بردارهای تست `progress_vectors.json`، ویژگی حیاتی `R8` (صف مرور غلط‌های بین‌نشسته‌ای) را پیاده‌سازی می‌کنیم: هر ریزدرسی که داوطلب در تلاش اول اشتباه بزند (`attempts > 1` یا حکم `INCORRECT`)، پرچم مرور مجدد و کارت `FSRS-5` دریافت می‌کند و در `store.progress.mistakeQueue` به صورت پایدار ذخیره می‌شود تا در تب «تمرین» و گره رعدوبرق (`Practice Gate`) تا رسیدن به تسلط بدون کمک (`unaided`) مرور گردد.",
    deliverables: [
      {
        id: "P6_D1",
        title: "تضمین تطابق ۱۰۰٪ ساختار ۱۱ فیلدی LessonProgress و کلید مرکب (lessonId, tutorialId) با HANDOFF/data/progress_vectors.json",
        specRef: "HANDOFF/05_SPEC_LEARNER_MODEL.md §1–§5",
        done: true,
      },
      {
        id: "P6_D2",
        title: "پیاده‌سازی پایداری بین‌نشسته‌ای صف مرور غلط‌ها (mistakeQueue و inQueue) در app/src/store.js و app/src/content-engine.js (R8)",
        specRef: "docs/05_ROADMAP.md R8",
        done: false,
      },
      {
        id: "P6_D3",
        title: "افزودن شمارنده تفکیک‌شده aided_successes در برابر unaided_successes تا استفاده از راهنمای هوش مصنوعی باعث تسلط کاذب نشود",
        specRef: "MASTER_BLUEPRINT.md Phase 2 & 7",
        done: false,
      },
    ],
    targetFiles: [
      "app/src/store.js",
      "app/src/content-engine.js",
      "app/tests/integration.test.mjs",
    ],
    antiDriftRules: [
      "تابع store.get() در app/src/store.js فقط یک آرگومان می‌گیرد و برای مسیرهای ناموجود undefined برمی‌گرداند؛ همیشه هنگام خواندن آرایه‌ها fallback به [] قرار بده.",
      "اگر زمان سیستم به عقب برگردد (completedAt < startedAt)، طبق قانون ordering guard در 05_SPEC §3 خطا را لاگ کن اما نوشتن رکورد پیشرفت را متوقف نکن.",
    ],
    verificationCommands: [
      "python3 -m pytest -q HANDOFF/tests/test_progress_vectors.py",
      "npm test --prefix app",
    ],
    agentPrompt: `فاز ۶ (مدل پیشرفت LessonProgress و پایداری صف مرور غلط‌ها R8) را اجرا کن:
۱. در app/src/store.js و app/src/content-engine.js، صف مرور غلط‌ها و فیلد inQueue را بین نشست‌ها (بعد از رفرش صفحه و بسته شدن اپ) در localStorage کاملاً پایدار کن (R8).
۲. منطق تفکیک پاسخ مستقل (unaided: اولین تلاش درست بدون باز کردن راهنما) از پاسخ با کمک (aided) را به ردیف پیشرفت اضافه کن.
۳. در app/tests/integration.test.mjs تستی بنویس که یک درس را غلط جواب دهد، اپ را مجدداً بارگذاری (reload) کند و اثبات نماید که سوال غلط همچنان در صف مرور باقی مانده است.
۴. دستورات تایید را اجرا کن:
   python3 -m pytest -q HANDOFF/tests/test_progress_vectors.py
   npm test --prefix app`,
  },
  {
    phaseNumber: 7,
    code: "PHASE_07",
    title: "فاز ۷: تکمیل پوسته ناوبری بومی v12.5-fa، گره‌های ۹۲dp مسیر و حذف آخرین ردپای دموی فونت (R3)",
    subtitle: "100% Native Navigation Fidelity (M09), 92dp Squircle Path Nodes & Clean Removal of Typography Demo Leftovers",
    weightPct: 8,
    status: "pending",
    category: "رابط کاربری بومی و ناوبری",
    estimatedTurns: "۴ تا ۶ گام اجرایی ایجنت",
    sourceBranchRefs: [
      "mimo-ui/UPGRADE/DESIGN/index.html (v12.5-fa)",
      "app/docs/MIMO_NATIVE_NAVIGATION.md",
      "app/docs/INTEGRATIONS.md §1",
      "docs/05_ROADMAP.md (R3)",
    ],
    prerequisites: ["PHASE_03", "PHASE_05"],
    objective:
      "تضمین انطباق پیکسل‌به‌پیکسل رابط کاربری با حکم `v12.5-fa` (`F2, F10–F47`) و ناوبری بومی `M09` (`PathMap → ChapterActivity → LessonRenderer → QuitDialog / CelebrationModal`) به همراه اجرای تمیز `R3`.",
    architecturalDeepDive:
      "طبق قوانین `docs/02_DECISIONS.md` §2:\n" +
      "- **۵ تب پایین (`F13`):** یادگیری (`Learn`)، تمرین (`Practice`)، هوش مصنوعی (`AI`)، امتیازها (`Leaderboard`)، پروفایل (`Profile`). در هنگام باز بودن درس (`LessonRenderer`) یا اجرای آزمون (`exam-run`)، نوار تب پایین و چیپ‌های بالا مخفی می‌شوند و صفحه تمام‌صفحه بومی باز می‌شود.\n" +
      "- **نوار بالای درس (`F27/F28/F30`):** دکمه خروج `X` (که مودال تایید خروج `QuitDialog` را باز می‌کند)، نوار پیشرفت با ارتفاع دقیق `6dp` (`#8D60E2`)، آیکون پرچم گزارش، و دکمه سرتاسری `Continue` در پایین (`#7E4BDE`).\n" +
      "- **هندسه گره‌های مسیر (`app/src/nodes.js` و `node-match.css`):** اندازه `92dp`، شعاع `26dp`، لبه سه‌بعدی پایین `8dp`، کانکتور قوس `Q` با ضخامت `10dp` و شعاع `32dp`، حلقه پیشرفت `60dp` با `conic-gradient` دور گره جاری، بدون هیچ گره قفل‌شده مسدودکننده (`F25`)، و دکمه شناور واژه‌نامه `«A»`.",
    deliverables: [
      {
        id: "P7_D1",
        title: "اطمینان از کارکرد بی‌نقص ماشین وضعیت ناوبری M09: PathMap → ChapterActivity → LessonRenderer → QuitDialog / CelebrationModal → SelectPath / PathOverview / SectionDetail / PracticeGate",
        specRef: "app/docs/MIMO_NATIVE_NAVIGATION.md",
        done: true,
      },
      {
        id: "P7_D2",
        title: "تایید هندسه گره‌های ۹۲dp با assertGeometry(window.NODE) و به‌روزرسانی زنده حالت گره‌ها (done / current-half / next / bolt-active) از روی پیشرفت واقعی STRUCTURED_PACKAGE",
        specRef: "app/docs/INTEGRATIONS.md §1",
        done: true,
      },
      {
        id: "P7_D3",
        title: "ایجاد بررسی خودکار در verify_output.py که تضمین کند هیچ زیررشته‌ای از متن دموی «شکستن خطوط» در DOM رندرشده درس یا باندل فعال فراخوانی نمی‌شود (R3)",
        specRef: "docs/05_ROADMAP.md R3",
        done: false,
      },
    ],
    targetFiles: [
      "app/native/index.html",
      "app/src/native.js",
      "app/src/nodes.js",
      "app/assets/native.css",
      "app/tools/verify_output.py",
    ],
    antiDriftRules: [
      "فایل‌های مرجع تاریخی mimo-ui/UPGRADE/DESIGN/index.html و app/assets/phone.html را دستکاری نکن؛ تمام تغییرات پوسته محصول در app/native/index.html و app/src/native.js اعمال شوند.",
      "هیچ آیکون خارجی خارج از وکتورهای استخراج‌شده ARSC اضافه نکن (قانون F37).",
    ],
    verificationCommands: [
      "npm test --prefix app",
      "npm run verify --prefix app",
    ],
    agentPrompt: `فاز ۷ (تکمیل ناوبری بومی v12.5-fa و هندسه گره‌های M09) را اجرا کن:
۱. در app/src/native.js و app/src/nodes.js اطمینان حاصل کن که وضعیت گره‌های نقشه مسیر (PathMap) و درصد پیشرفت کارت سربرگ مسیر مستقیماً از پیشرفت واقعی روی STRUCTURED_PACKAGE.json محاسبه و رندر شوند.
۲. بررسی R3 را در app/tools/verify_output.py و app/tests/fidelity.test.mjs تقویت کن تا ۱۰۰٪ تضمین شود هیچ اثری از متن دموی چیدمان خط در جریان اجرای درس وجود ندارد و قوانین F2 و F10–F47 کاملاً برقرارند.
۳. دستورات تایید را اجرا کن:
   npm test --prefix app
   npm run verify --prefix app`,
  },
  {
    phaseNumber: 8,
    code: "PHASE_08",
    title: "فاز ۸: ترکیب عمیق هوش مصنوعی با LearnHarness و موتور تطبیقی KST / BKT / FSRS-5 (R12)",
    subtitle: "Weaving LearnHarness (Measure → Plan → Teach → Practice) with Textbook Proposition Graph, Local Fallback & Server SSE Gateway",
    weightPct: 10,
    status: "pending",
    category: "هوش مصنوعی و LearnHarness",
    estimatedTurns: "۶ تا ۸ گام اجرایی ایجنت",
    sourceBranchRefs: [
      "https://github.com/amosblomqvist/learnharness",
      "app/src/harness.js",
      "ANALYSIS/HADAF_PLUS_AI_API_AUDIT.md",
      "HANDOFF/08_SPEC_STREAMING_AND_TUTOR.md",
      "comprehensive-software-development-roadmap.zip (src/lib/algorithms.ts)",
    ],
    prerequisites: ["PHASE_05", "PHASE_06"],
    objective:
      "حل کامل معمای ترکیب هوش مصنوعی با `LearnHarness`: اتصال چرخه ۴ فازی (`Measure/Probe → Plan → Teach → Practice`) به گراف گزاره‌های کتاب درسی زیست/کنکور به طوری که هم به صورت ۱۰۰٪ آفلاین (`LocalContentProvider`) و هم با گیت‌وی استریم سرور (`ExternalSSEProvider` با کلید امن سروری) کار کند.",
    architecturalDeepDive:
      "چطور `LearnHarness` (`github.com/amosblomqvist/learnharness`) را با میمو و کنکور ترکیب کنیم بدون اینکه به یک چت‌بات سطحی یا توهم‌زا تبدیل شود؟\n" +
      "۱. **گراف گزاره‌های کتاب درسی (`Proposition Graph`):** در `LearnHarness`، دانش به صورت مجموعه‌ای از گزاره‌های اتمیک (`Proposition`) ذخیره می‌شود که هر کدام دارای `id`، `statement` (متن گزاره از کتاب درسی)، `prerequisites[]` (شناسه گزاره‌های پیشنیاز)، `unconditionalTruth` (اصل بدیهی اول — Principle i)، `motivatedDiscoveryPrompt` (سوال هدایت‌گر برای کشف توسط خود دانش‌آموز — Principle ii) و `status ∈ {'unmeasured', 'active', 'inactive_needs_practice', 'mastered'}` هستند.\n" +
      "۲. **چرخه ۴ فازی در تب سوم (`هوش مصنوعی`) و چیپ AI داخل درس/آزمون:**\n" +
      "   - **فاز ۱ (`Measure / Probe`):** وقتی داوطلب یک تست را در درس یا آزمون غلط می‌زند (وضعیت `jm.o`) یا روی دکمه «شروع جلسه» در تب AI می‌زند، هارنس به جای لو دادن جواب، **زنجیره پیشنیازهای آن تست را با جستجوی دودویی می‌سنجد**! از داوطلب یک سوال تشخیصی کوتاه می‌پرسد و داوطلب علاوه بر گزینه، **ضریب اطمینان (`Confidence 0–100%`)** و استدلال کوتاه خود (`Think-Aloud`) را وارد می‌کند.\n" +
      "   - **فاز ۲ (`Plan`):** هارنس دقیق‌ترین نقطه ضعف (اولین گزاره پیشنیاز که داوطلب در آن شک دارد یا غلط زده) را پیدا کرده و نقشه درختی کوتاهی از بدیهیات بلدشده تا هدف تست کنکور ترسیم می‌کند.\n" +
      "   - **فاز ۳ (`Teach`):** بر اساس Principle i (شروع از حقیقت بدیهی که داوطلب همین الان تایید کرد) و Principle ii (هدایت سقراطی تا کشف نکته کنکوری)، مفهوم را گام‌به‌گام آموزش می‌دهد تا گزاره در ذهن داوطلب `active` شود.\n" +
      "   - **فاز ۴ (`Practice`):** طرح یک تست برادر/هم‌ریخت همراه با نردبان راهنمایی ۳ پله‌ای (`Hint Ladder`) و قفل کردن پاسخ تشریحی تا زمانی که داوطلب خودش تلاش کند (`Unaided Retrieval`).\n" +
      "۳. **معماری دوگانه ارائه‌دهنده (Dual Provider Contract):**\n" +
      "   - **حالت پیش‌فرض آفلاین (`LocalContentProvider`):** تمام ۴ فاز را بدون نیاز به اینترنت و با هزینه `۰٫۰۰ دلار` مستقیماً از روی گراف گزاره‌ها و نردبان راهنمایی استخراج‌شده در `STRUCTURED_PACKAGE.json` اجرا می‌کند (حفظ پرچم صداقت `externalProvider: 'not-configured'` در بیلد آفلاین `Mimo.html`).\n" +
      "   - **حالت آنلاین سروری (`ServerGatewayProvider`):** همان‌طور که در ممیزی `HADAF_PLUS_AI_API_AUDIT.md` اثبات شد، هیچ کلید LLM در کلاینت قرار نمی‌گیرد؛ کلاینت (در صورت تنظیم آدرس گیت‌وی سرور در تنظیمات) درخواست را به روت بک‌اند `POST /api/v1/ai/harness` می‌فرستد که کلید `process.env.AI_API_KEY` را در سمت سرور می‌خواند و پاسخ را روی همان گراف گزاره‌های کتاب استریم (`text/event-stream`) می‌کند.",
    deliverables: [
      {
        id: "P8_D1",
        title: "غنی‌سازی هر فصل در STRUCTURED_PACKAGE.json با گراف گزاره‌های LearnHarness (شامل اصل اول Unconditional Truth، سوال کشف سقراطی Principle ii و نردبان راهنمایی ۳ سطحی)",
        specRef: "app/src/harness.js & app/docs/INTEGRATIONS.md §3",
        done: false,
      },
      {
        id: "P8_D2",
        title: "تکمیل ماشین ۴ فازی Measure → Plan → Teach → Practice در app/src/harness.js به همراه فیلدهای thinking و confidence و اتصال دکمه‌های TEACH/PRACTICE و چیپ AI داخل درس و آزمون",
        specRef: "app/src/harness.js",
        done: false,
      },
      {
        id: "P8_D3",
        title: "اتصال الگوریتم‌های KST Outer Fringe (انتخاب بهترین گره آماده یادگیری)، کنترلر باند جریان ۷۰-۸۵٪ و زمان‌بند FSRS-5 به خروجی جلسات LearnHarness",
        specRef: "src/lib/algorithms.ts",
        done: true,
      },
      {
        id: "P8_D4",
        title: "پیاده‌سازی قرارداد EXTERNAL_PROVIDER_CONTRACT و روت سرور /api/v1/ai/harness با حفظ پیش‌فرض صادقانه offline-first در بیلد استاتیک",
        specRef: "docs/05_ROADMAP.md R12 & HANDOFF/08_SPEC",
        done: true,
      },
    ],
    targetFiles: [
      "app/src/harness.js",
      "app/src/ai-studio.js",
      "app/src/native.js",
      "src/lib/algorithms.ts",
      "app/tests/acceptance.test.mjs",
    ],
    antiDriftRules: [
      "در بیلد آفلاین تک‌فایلی (app/dist/Mimo.html)، پرچم externalProvider باید به صورت پیش‌فرض 'not-configured' بماند و هیچ کلید API در کد کلاینت هاردکد نشود (قانون D2).",
      "در فاز Teach و Practice هارنس، هرگز قبل از اینکه داوطلب حداقل یک بار تلاش کند، پاسخ نهایی تست را نمایش نده (جلوگیری از توهم یادگیری طبق یافته ARCHIVE_FORENSICS).",
    ],
    verificationCommands: [
      "npm test --prefix app",
      "npm run verify --prefix app",
    ],
    agentPrompt: `فاز ۸ (یکپارچه‌سازی عمیق LearnHarness و موتور شناختی KST/BKT/FSRS-5) را اجرا کن:
۱. در app/tools/emit_structured_package.py و app/src/harness.js، گراف گزاره‌های هر فصل کتاب (شامل گزاره‌های پیشنیاز، Principle i Unconditional Truth، Principle ii Motivated Discovery و نردبان راهنمایی) را مستقیماً از STRUCTURED_PACKAGE.json داخل LearnHarness بارگذاری کن (window.APP.mountContentPackage).
۲. چرخه کامل ۴ فاز Measure → Plan → Teach → Practice را در تب سوم (هوش مصنوعی) و هنگام کلیک روی چیپ AI در وضعیت پاسخ غلط درس یا آزمون فعال کن، به طوری که فیلدهای confidence (۰ تا ۱۰۰٪) و thinking در store.ai.harness ثبت شوند.
۳. الگوریتم محاسبه لبه بیرونی دانش (KST Outer Fringe) و کنترلر باند جریان ۷۰-۸۵٪ را برای پیشنهاد خودکار مبحث بعدی متصل کن.
۴. دستورات تایید را اجرا کن:
   npm test --prefix app
   npm run verify --prefix app`,
  },
  {
    phaseNumber: 9,
    code: "PHASE_09",
    title: "فاز ۹: هاب ۷بخشی آزمون کنکور، پاسخبرگ نوری، پاسخنامه تشریحی و تایمر ۲۷۰ دقیقه‌ای (R9)",
    subtitle: "7-Section Konkur Exam Hub, Optical Bubble Sheet vs Detailed Explanatory Key, -33.3% Scoring & Auto-Repair Routing",
    weightPct: 7,
    status: "pending",
    category: "شبیه‌ساز آزمون و تمرین",
    estimatedTurns: "۴ تا ۶ گام اجرایی ایجنت",
    sourceBranchRefs: [
      "docs/05_ROADMAP.md (R9)",
      "docs/02_DECISIONS.md (F39–F43)",
      "app/content/EXAM_TEMPLATE.json",
      "app/content/PRACTICE_TEMPLATE.json",
      "app/src/exam-template.js",
    ],
    prerequisites: ["PHASE_05", "PHASE_08"],
    objective:
      "جایگزینی آرایه نمونه ۲۰ سوالی `QBANK` با موتور آزمون‌ساز قطعی (`app/src/exam-template.js`) متصل به بانک سوالات تاییدشده کتاب درسی (`R9`) با رعایت ۱۰۰٪ قوانین `F39–F43`.",
    architecturalDeepDive:
      "طبق قوانین مصوب `F39–F43` در `docs/02_DECISIONS.md`:\n" +
      "۱. **هاب آزمون ۷بخشی (`exam-hub`):** شامل ۷ نوع آزمون مصوب در `EXAM_TEMPLATE.json` (آزمون جامع ۲۷۰ دقیقه‌ای کنکور، آزمون فصلی، آزمون مبحثی، آزمون جمع‌بندی، آزمون زمان‌دار سرعتی، آزمون غلط‌های من، و آزمون سفارشی) و ۴ حالت تمرین بدون زمان در `PRACTICE_TEMPLATE.json`.\n" +
      "۲. **قانون حیاتی تفکیک «پاسخبرگ» از «پاسخنامه» (`F41`):**\n" +
      "   - **«پاسخبرگ» (Optical Bubble Sheet):** برگه کلیدی ۴ گزینه‌ای در حین برگزاری آزمون برای پر کردن، علامت‌گذاری شک‌دار (ضربدر/منها به سبک کنکور) و پرش سریع بین سوالات.\n" +
      "   - **«پاسخنامه» (Explanatory Diagnostic Key):** تنها پس از پایان آزمون باز می‌شود و شامل کلید صحیح، درصد نمره خام با فرمول نمره منفی یک‌سوم $\\frac{3C - W}{3N} \\times 100$، تحلیل کامل هر ۴ گزینه و دکمه «ارسال غلط‌ها به LearnHarness و صف مرور» است.\n" +
      "۳. **تایمر قابل ویرایش (`F40/F43`):** تایمر منحصراً داخل صفحه اجرای آزمون (`exam-run`) نمایش داده می‌شود (پیش‌فرض ۲۷۰ دقیقه برای آزمون جامع) به همراه ۳ مسیر خروج ایمن (ذخیره اسنپشات `SAVED` برای ادامه بعدی، تحویل و تصحیح آنی، یا لغو آزمون).",
    deliverables: [
      {
        id: "P9_D1",
        title: "اتصال buildExam() و buildPracticeSession() در app/src/exam-template.js به بانک سوالات کامل STRUCTURED_PACKAGE.json به جای QBANK نمونه (R9)",
        specRef: "docs/05_ROADMAP.md R9 & app/docs/INTEGRATIONS.md §2",
        done: false,
      },
      {
        id: "P9_D2",
        title: "پیاده‌سازی محاسبه دقیق درصد کنکور با نمره منفی یک‌سوم ((3*C - W)/(3*N))*100 و تفکیک کامل نمای «پاسخبرگ» و «پاسخنامه تشریحی» (F39–F43)",
        specRef: "docs/02_DECISIONS.md F39–F43",
        done: true,
      },
      {
        id: "P9_D3",
        title: "اتصال خودکار سوالات غلط و نزده آزمون پس از ثبت کارنامه به صف مرور غلط‌ها (inQueue) و جلسه ترمیمی LearnHarness",
        specRef: "app/src/exam-template.js & app/src/harness.js",
        done: false,
      },
    ],
    targetFiles: [
      "app/src/exam-template.js",
      "app/src/native.js",
      "app/content/EXAM_TEMPLATE.json",
      "app/content/PRACTICE_TEMPLATE.json",
      "app/tests/acceptance.test.mjs",
    ],
    antiDriftRules: [
      "هرگز داخل صفحه exam-hub (قبل از شروع آزمون) تایمر شمارش معکوس نگذار؛ تایمر فقط داخل exam-run است (قانون F40).",
      "هرگز واژه‌های «پاسخبرگ» و «پاسخنامه» را به جای هم به کار نبر (قانون F41).",
    ],
    verificationCommands: [
      "npm test --prefix app",
      "npm run verify --prefix app",
    ],
    agentPrompt: `فاز ۹ (تکمیل هاب ۷بخشی آزمون کنکور و بانک سوال واقعی R9) را اجرا کن:
۱. در app/src/exam-template.js و app/src/native.js، منبع سوالات buildExam() و buildPracticeSession() را به بانک سوالات تاییدشده داخل STRUCTURED_PACKAGE.json متصل کن تا کمبود سوال (shortfall) به صفر برسد (R9).
۲. اطمینان حاصل کن که قوانین F39 تا F43 (هاب ۷بخشی، تایمر ۲۷۰ دقیقه‌ای قابل ویرایش فقط داخل آزمون، ۳ مسیر خروج با ذخیره اسنپشات، تفکیک پاسخبرگ از پاسخنامه تشریحی، و چیپ AI روی هر سوال در پاسخنامه) ۱۰۰٪ برقرارند.
۳. پس از اتمام آزمون، سوالات غلط را به صورت خودکار وارد صف مرور (inQueue) و گراف LearnHarness کن.
۴. دستورات تایید را اجرا کن:
   npm test --prefix app
   npm run verify --prefix app`,
  },
  {
    phaseNumber: 10,
    code: "PHASE_10",
    title: "فاز ۱۰: یکپارچه‌سازی مسیر یادگیری، تب امتیازها («وضعیت من»)، پروفایل و ۳ ساختار توکن (R10 & R11)",
    subtitle: "Unifying Learning Path with STRUCTURED_PACKAGE, 'My Status' Analytics Leaderboard, Profile & 3-Layer Token Economy",
    weightPct: 5,
    status: "pending",
    category: "مسیر یادگیری، اقتصاد توکن و پروفایل",
    estimatedTurns: "۳ تا ۵ گام اجرایی ایجنت",
    sourceBranchRefs: [
      "docs/05_ROADMAP.md (R10, R11)",
      "docs/02_DECISIONS.md (D4)",
      "app/src/learning-path.js",
      "app/src/token-economy.js",
      "app/src/design-tokens.js",
    ],
    prerequisites: ["PHASE_05", "PHASE_09"],
    objective:
      "جایگزینی آرایه ساختگی `KONKUR` در `app/src/learning-path.js` با `STRUCTURED_PACKAGE.json` (`R10`)، تکمیل تب چهارم («امتیازها / وضعیت من») و تب پنجم («پروفایل») (`R11`) و همگام‌سازی هر ۳ ساختار توکن (`D4`).",
    architecturalDeepDive:
      "طبق تصمیم `D4` در `docs/02_DECISIONS.md`، عبارت «ساختار توکن‌ها» در این پروژه دقیقاً سه لایه مکمل دارد که هر سه باید همگام کار کنند:\n" +
      "۱. **توکن‌های طراحی ARSC (`app/src/design-tokens.js`):** متغیرهای CSS استخراج‌شده از `resources.arsc` میمو ۹٫۳۵.\n" +
      "۲. **اقتصاد محلی و دفتر کل توکن‌ها (`app/src/token-economy.js`):** تراکنش‌های سکه (`Coins`)، کلید (`Keys ∞`)، استریک روزانه (`Streak`) و `XP` در بالای صفحه یادگیری که با اتمام هر ریزدرس (`tries >= 1`) و آزمون آپدیت می‌شوند.\n" +
      "۳. **توکن‌های زمینه و گام‌های شناختی هوش مصنوعی (`AI Context & Step Tokens`):** شمارش و مدیریت بودجه توکن و گام‌های استدلال در جلسات `LearnHarness`.",
    deliverables: [
      {
        id: "P10_D1",
        title: "بازنویسی app/src/learning-path.js برای خواندن تمام بخش‌ها، فصل‌ها و درسنامه‌ها مستقیماً از STRUCTURED_PACKAGE.json و حذف آرایه ساختگی KONKUR (R10)",
        specRef: "docs/05_ROADMAP.md R10",
        done: false,
      },
      {
        id: "P10_D2",
        title: "تکمیل نمای «وضعیت من» در تب امتیازها (Leaderboard) و خلاصه تحلیلی تسلط مباحث و استریک در تب پروفایل (R11)",
        specRef: "docs/05_ROADMAP.md R11",
        done: false,
      },
      {
        id: "P10_D3",
        title: "یکپارچه‌سازی دفتر کل اقتصاد توکن (token-economy.js) با رویدادهای تکمیل ریزدرس، آزمون و جلسات LearnHarness",
        specRef: "docs/02_DECISIONS.md D4",
        done: true,
      },
    ],
    targetFiles: [
      "app/src/learning-path.js",
      "app/src/token-economy.js",
      "app/src/views.js",
      "app/src/native.js",
    ],
    antiDriftRules: [
      "در تب چهارم و پنجم هیچ رفتار سروری جعلی (مانند لیدربورد آنلاین تقلبی با نام‌های ساختگی که ادعای اتصال به سرور کند) نساز؛ از نمای مصوب «وضعیت من» و آمار واقعی محلی استفاده کن.",
    ],
    verificationCommands: [
      "npm test --prefix app",
      "npm run verify --prefix app",
    ],
    agentPrompt: `فاز ۱۰ (یکپارچه‌سازی learning-path.js و تکمیل تب‌های امتیازها، پروفایل و اقتصاد توکن R10–R11) را اجرا کن:
۱. در app/src/learning-path.js، داده‌های ساختگی KONKUR را با درخت واقعی STRUCTURED_PACKAGE.json جایگزین کن تا select-path، path-overview و section-detail دقیقاً همان فصل‌ها و آمار واقعی کتاب را نشان دهند (R10).
۲. در تب امتیازها («وضعیت من») و تب پروفایل، آمار واقعی پیشرفت داوطلب (ریزدرس‌های حل‌شده، دقت اولین تلاش firstTryCount، وضعیت صف مرور غلط‌ها و دفتر کل توکن‌ها) را نمایش بده (R11).
۳. دستورات تایید را اجرا کن:
   npm test --prefix app
   npm run verify --prefix app`,
  },
  {
    phaseNumber: 11,
    code: "PHASE_11",
    title: "فاز ۱۱: بیلد تکرارپذیر بایت‌به‌بایت، بسته‌بندی تک‌فایلی Mimo.html، PWA و خروجی اندروید (R13–R15)",
    subtitle: "Byte-Reproducible Build, Single-File Mimo.html, Installable Offline PWA, Android APK Wrapper & Final Audit",
    weightPct: 4,
    status: "pending",
    category: "بیلد نهایی، تست دستگاه و تحویل",
    estimatedTurns: "۳ تا ۵ گام اجرایی ایجنت",
    sourceBranchRefs: [
      "docs/05_ROADMAP.md (R13, R14, R15)",
      "app/tools/build_output.py",
      "app/docs/OUTPUT_GUIDE.md",
      "docs/08_HANDOFF_PROMPT.md",
    ],
    prerequisites: ["PHASE_07", "PHASE_08", "PHASE_09", "PHASE_10"],
    objective:
      "تولید خروجی نهایی خودکفا (`app/dist/Mimo.html`، بسته `PWA` قابل نصب و `Mimo.zip`) با بیلد تکرارپذیر (`R15`)، اجرای کامل تمامی تست‌های ۵ لایه و به‌روزرسانی نهایی اسناد تحویل.",
    architecturalDeepDive:
      "در فاز پایانی، اسکریپت `app/tools/build_output.py` تمام ماژول‌های ESM در `app/src/`، استایل‌های `proto.css` و `native.css`، و بسته تاییدشده `STRUCTURED_PACKAGE.json` را در یک فایل واحد و بدون وابستگی `app/dist/Mimo.html` باندل می‌کند. همچنین برای رفع `R15` (تکرارپذیری بایت‌به‌بایت بیلد)، استفاده از `SOURCE_DATE_EPOCH` برای timestampهای داخل `BUILD_MANIFEST.json` و آرشیو `Mimo.zip` اعمال می‌شود تا هش SHA-256 خروجی در هر بار بیلد روی یک کامیت کاملاً ثابت و قابل اثبات باشد.",
    deliverables: [
      {
        id: "P11_D1",
        title: "پشتیبانی از SOURCE_DATE_EPOCH در app/tools/build_output.py برای تضمین تکرارپذیری بایت‌به‌بایت هش Mimo.html و Mimo.zip (R15)",
        specRef: "docs/05_ROADMAP.md R15",
        done: false,
      },
      {
        id: "P11_D2",
        title: "تولید مجدد app/dist/Mimo.html، index.html (PWA با manifest.webmanifest و sw.js) و Mimo.zip",
        specRef: "app/docs/OUTPUT_GUIDE.md",
        done: true,
      },
      {
        id: "P11_D3",
        title: "پاس شدن ۱۰۰٪ زنجیره ۵ گانه ممیزی نهایی: HANDOFF pytest (54/54) + app npm test (45+/45+) + verify_app.py (54/54) + verify_output.py (51/51) + validate_content.py + verify_docs.py",
        specRef: "docs/04_CURRENT_STATE.md §3",
        done: true,
      },
    ],
    targetFiles: [
      "app/tools/build_output.py",
      "app/dist/Mimo.html",
      "app/dist/BUILD_MANIFEST.json",
      "docs/04_CURRENT_STATE.md",
      "REPO_INDEX.json",
    ],
    antiDriftRules: [
      "هنگام باندل کردن در build_output.py، حتماً assert کن که هیچ تگ </script یا <!-- خام داخل رشته‌های JSON/JS اینلاین‌شده وجود نداشته باشد.",
      "قبل از اعلام اتمام پروژه، هر ۶ دستور ممیزی نهایی را اجرا کن و خروجی واقعی آن‌ها را ثبت نما.",
    ],
    verificationCommands: [
      "python3 app/tools/emit_structured_package.py",
      "python3 app/tools/build_output.py",
      "npm test --prefix app",
      "npm run verify --prefix app",
      "python3 app/tools/validate_content.py app/content/STARTER_PACKAGE.json app/content/STRUCTURED_PACKAGE.json",
      "python3 HANDOFF/tools/verify_handoff.py",
      "python3 docs/verify_docs.py",
    ],
    agentPrompt: `فاز ۱۱ (بیلد نهایی تکرارپذیر، بسته‌بندی تک‌فایلی/PWA و ممیزی جامع) را اجرا کن:
۱. در app/tools/build_output.py پشتیبانی از SOURCE_DATE_EPOCH را اضافه کن تا بیلد app/dist/Mimo.html و Mimo.zip بایت‌به‌بایت تکرارپذیر باشد (R15).
۲. بسته محتوا و باندل تولیدی را از نو بساز:
   python3 app/tools/emit_structured_package.py
   python3 app/tools/build_output.py
۳. فایل‌های docs/04_CURRENT_STATE.md و REPO_INDEX.json را با اعداد و هش‌های جدید به‌روزرسانی کن.
۴. کل زنجیره ممیزی را اجرا کن و تا سبز شدن ۱۰۰٪ تمام موارد توقف نکن:
   npm test --prefix app
   npm run verify --prefix app
   python3 app/tools/validate_content.py app/content/STARTER_PACKAGE.json app/content/STRUCTURED_PACKAGE.json
   python3 HANDOFF/tools/verify_handoff.py
   python3 docs/verify_docs.py`,
  },
];
