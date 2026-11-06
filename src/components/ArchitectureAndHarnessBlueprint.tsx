"use client";

import React, { useState } from "react";
import {
  Cpu,
  Database,
  BrainCircuit,
  ExternalLink,
  Layers,
  CheckCircle2,
  ShieldCheck,
  Smartphone,
  Server,
  Sparkles,
} from "lucide-react";
import type {
  ExternalRepoRequirement,
  StackArchitectureLayer,
} from "@/lib/repo-forensics-data";

interface ArchitectureAndHarnessBlueprintProps {
  stackMatrix: StackArchitectureLayer[];
  externalRepos: ExternalRepoRequirement[];
}

const HARNESS_PHASES = [
  {
    phase: "Phase 1 · Measure (Probe)",
    titleFa: "۱. فاز سنجش تشخیصی (Binary-Search Dependency Probe)",
    badge: "جستجوی دودویی روی زنجیره پیشنیازها",
    whatHappens:
      "وقتی داوطلب در یک تست کنکور (مثلاً اپران لک یا همانندسازی دنا) غلط می‌زند یا وارد تب هوش مصنوعی می‌شود، هارنس به جای گفتن جواب، گراف پیشنیازهای آن تست را برمی‌دارد و از وسط زنجیره یک سوال تشخیصی کوتاه می‌پرسد.",
    uiComponents: [
      "سوال تشخیصی تک‌مفهومی از گزاره میانی گراف (`proposition.probeQuestion`)",
      "اسلایدر ضریب اطمینان داوطلب (`Confidence: 0% to 100%`)",
      "باکس «بلند فکر کن» (`thinking` — یک جمله که چرا این گزینه را انتخاب کردی)",
    ],
    stateTransition:
      "اگر داوطلب با اطمینان بالا درست جواب داد، تمام پیشنیازهای قبلی در گراف `mastered` علامت می‌خورند و جستجو به نیمه بالاتر می‌رود؛ اگر غلط یا با شک جواب داد، جستجو به پیشنیازهای پایه‌تر می‌رود تا دقیق‌ترین «گره ریشه‌ای کج‌فهمی» پیدا شود.",
  },
  {
    phase: "Phase 2 · Plan",
    titleFa: "۲. فاز طراحی مسیر شخصی‌سازی‌شده (Minimal Dependency Plan)",
    badge: "از اصل بدیهی اول تا هدف تستی کنکور",
    whatHappens:
      "هارنس کوتاه‌ترین مسیر درختی را از «آخرین گزاره‌ای که داوطلب صددرصد بلد بود (Unconditional Truth)» تا «تست هدف کنکور» رسم می‌کند (معمولاً ۳ تا ۴ پله مفهومی).",
    uiComponents: [
      "نمایش درخت ۳ تا ۴ مرحله‌ای در بالای چت تب AI (`store.ai.harness.plan`)",
      "مشخص کردن گره فعلی با حلقه بنفش `#7E4BDE` و گره‌های بلدشده با تیک سبز",
    ],
    stateTransition:
      "قفل کردن پرش به تست نهایی تا زمانی که هر پله میانی در فاز Teach فعال (`active`) شود.",
  },
  {
    phase: "Phase 3 · Teach (Principles i & ii)",
    titleFa: "۳. فاز آموزش سقراطی مبتنی بر اصول بدیهی و کشف باانگیزه",
    badge: "Principle i (Axioms) + Principle ii (Motivated Discovery)",
    whatHappens:
      "طبق قانون علمی آزمایشگاه شما (`ARCHIVE_FORENSICS.md`)، توضیح دادن صرف (`Explain-only`) فقط توهم یادگیری می‌آورد (انتقال ۰٫۰۸)! بنابراین در فاز Teach، هارنس ابتدا یک «حقیقت بدیهی غیرقابل‌انکار (Principle i)» را یادآوری می‌کند و سپس با یک «سوال کشف هدایت‌شده (Principle ii)» کاری می‌کند که خود داوطلب قانون علمی کتاب درسی را استنتاج کند.",
    uiComponents: [
      "حباب اصل بدیهی اول (`Unconditional Truth`)",
      "میکرو-چک تعاملی کشف نکته قبل از نمایش فرمول/جمع‌بندی",
    ],
    stateTransition:
      "با پاسخ درست داوطلب، وضعیت گزاره در گراف دانش از `unmeasured` به `active (inactive_needs_practice)` تغییر می‌کند.",
  },
  {
    phase: "Phase 4 · Practice (Unaided Retrieval)",
    titleFa: "۴. فاز تمرین بازیابی مستقل و نردبان راهنمایی (Retrieval + Hint Ladder)",
    badge: "تفکیک Aided از Unaided + زمان‌بند FSRS-5",
    whatHappens:
      "گزاره‌ای که تازه در فاز Teach یاد گرفته شده هنوز در حافظه کوتاه‌مدت است. هارنس یک تست هم‌ریخت کنکوری (با تله قیدی مشابه) طرح می‌کند تا داوطلب بدون کمک (`unaided`) آن را حل کند.",
    uiComponents: [
      "کارت تست هم‌ریخت کنکوری با ۴ گزینه",
      "نردبان راهنمایی ۳ پله‌ای (`Hint Ladder`: پله ۱ اشاره به قید، پله ۲ حذف دو گزینه، پله ۳ قانون کتاب)",
      "قفل بودن پاسخ تشریحی (`Model Solution`) تا ثبت تلاش اول",
    ],
    stateTransition:
      "اگر داوطلب بدون باز کردن راهنما درست زد: `unaided_successes++`، ثبت `tries = 1` در `LessonProgress`، افزایش پایداری `FSRS-5` و حذف از صف مرور غلط‌ها (`inQueue = 0`). اگر با راهنما زد: `aided_successes++` و زمان‌بندی مرور مجدد برای فردا!",
  },
];

export function ArchitectureAndHarnessBlueprint({
  stackMatrix,
  externalRepos,
}: ArchitectureAndHarnessBlueprintProps) {
  const [activeHarnessIdx, setActiveHarnessIdx] = useState<number>(0);

  return (
    <div className="space-y-8">
      {/* Part 1: Answering "Kotlin vs Web vs Backend? How should the code be written?" */}
      <section className="rounded-2xl border border-slate-200 bg-white p-6 shadow-xs space-y-5">
        <div className="flex flex-wrap items-start justify-between gap-4 border-b border-slate-100 pb-4">
          <div className="space-y-1">
            <h2 className="text-lg font-bold text-[#252746] flex items-center gap-2">
              <Smartphone className="h-5 w-5 text-[#7E4BDE]" />
              ۱. پاسخ قطعی معماری: کد اپلیکیشن چطور نوشته شود؟ (کاتلین / Room در برابر وب / PWA و اتصال بک‌اند)
            </h2>
            <p className="text-xs text-slate-600 leading-relaxed max-w-4xl">
              در مهندسی معکوس میمو ۹٫۳۵ (<code className="font-mono-code">HANDOFF/01_WHAT_MIMO_IS.md</code>) کشف کردیم که در اپ اصلی میمو، پوسته ظاهری با Kotlin/Compose و دیتابیس با Room SQLite v2 نوشته شده، اما <strong className="text-[#7E4BDE]">تمام ۱۸٬۲۷۲ درسنامه به زبان HTML-DSL هستند!</strong> بنابراین بهترین معماری که شما را از دوباره‌کاری نجات می‌دهد، <strong>معماری هسته ایزومورفیک (Isomorphic Core + Multi-Target Shell)</strong> است:
            </p>
          </div>
        </div>

        {/* 3 Target Outputs Summary Cards */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
          <div className="rounded-xl border border-purple-200 bg-purple-50/50 p-4 space-y-2">
            <div className="flex items-center justify-between">
              <span className="rounded-lg bg-[#7E4BDE] text-white px-2.5 py-0.5 text-xs font-bold">
                لایه ۱: هسته مشترک (Core Engine)
              </span>
              <Cpu className="h-4 w-4 text-[#7E4BDE]" />
            </div>
            <h3 className="font-bold text-sm text-[#252746]">
              TypeScript / ESM خالص (بدون وابستگی به DOM)
            </h3>
            <p className="text-xs text-slate-600 leading-relaxed">
              شامل پارسر ۲۷ تگ DSL، نرمال‌ساز <code className="font-mono-code">qm.i.a</code> + فارسی، ماشین ۱۱ فیلدی <code className="font-mono-code">LessonProgress</code>، موتور <code className="font-mono-code">LearnHarness</code> و الگوریتم‌های <code className="font-mono-code">KST + BKT + FSRS-5</code>. این هسته یک بار نوشته می‌شود و در هر ۳ خروجی زیر کار می‌کند.
            </p>
          </div>

          <div className="rounded-xl border border-emerald-200 bg-emerald-50/50 p-4 space-y-2">
            <div className="flex items-center justify-between">
              <span className="rounded-lg bg-emerald-600 text-white px-2.5 py-0.5 text-xs font-bold">
                لایه ۲: کلاینت آفلاین، PWA و اندروید (Kotlin)
              </span>
              <Smartphone className="h-4 w-4 text-emerald-700" />
            </div>
            <h3 className="font-bold text-sm text-[#252746]">
              Mimo.html تک‌فایلی + PWA + پوسته Kotlin/Capacitor
            </h3>
            <p className="text-xs text-slate-600 leading-relaxed">
              پوسته مصوب <code className="font-mono-code">v12.5-fa</code> (<code className="font-mono-code">app/native/index.html</code>) هم به صورت فایل تک‌کلیکه <code className="font-mono-code">Mimo.html</code> بدون سرور کار می‌کند، و هم داخل یک پروژه سبک Android Kotlin (WebView/Capacitor + Room SQLite v2 <code className="font-mono-code">mimo.db</code>) به فایل <code className="font-mono-code">.apk</code> بومی تبدیل می‌شود.
            </p>
          </div>

          <div className="rounded-xl border border-indigo-200 bg-indigo-50/50 p-4 space-y-2">
            <div className="flex items-center justify-between">
              <span className="rounded-lg bg-[#252746] text-white px-2.5 py-0.5 text-xs font-bold">
                لایه ۳: بک‌اند، دیتابیس و گیت‌وی AI
              </span>
              <Server className="h-4 w-4 text-[#252746]" />
            </div>
            <h3 className="font-bold text-sm text-[#252746]">
              Next.js API Routes + PostgreSQL (Drizzle ORM)
            </h3>
            <p className="text-xs text-slate-600 leading-relaxed">
              مسئول دریافت صف سینک (<code className="font-mono-code">in_queue = 1</code>)، نگهداری دائمی کارنامه‌های آزمون کنکور، کامپایل کتاب‌های جدید، و پروکسی امن استریم هوش مصنوعی (<code className="font-mono-code">/api/v1/ai/harness</code>) بدون افشای کلید API در کلاینت.
            </p>
          </div>
        </div>

        {/* 5-Layer Comparison Matrix */}
        <div className="overflow-x-auto rounded-xl border border-slate-200">
          <table className="w-full text-right text-xs">
            <thead className="bg-[#252746] text-white">
              <tr>
                <th className="p-3.5 font-bold">لایه معماری</th>
                <th className="p-3.5 font-bold">در اپ اصلی Mimo 9.35 (شواهد APK)</th>
                <th className="p-3.5 font-bold">وضعیت فعلی در ریپوی شما</th>
                <th className="p-3.5 font-bold text-amber-300">معماری نهایی یکپارچه در نقشه گنج</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-slate-200 bg-white">
              {stackMatrix.map((row) => (
                <tr key={row.layerNumber} className="hover:bg-slate-50/80 align-top">
                  <td className="p-3.5 font-bold text-[#252746] min-w-[180px]">
                    <div>{row.layerTitle}</div>
                    <div className="mt-1.5 flex flex-wrap gap-1">
                      {row.keyContractsAndFiles.map((f, i) => (
                        <span
                          key={i}
                          className="rounded bg-purple-50 text-[#7E4BDE] border border-purple-200 px-1.5 py-0.5 text-[10px] font-mono-code"
                        >
                          {f}
                        </span>
                      ))}
                    </div>
                  </td>
                  <td className="p-3.5 text-slate-600 leading-relaxed min-w-[200px]">
                    {row.mimoOriginal935}
                  </td>
                  <td className="p-3.5 text-slate-600 leading-relaxed min-w-[200px]">
                    {row.currentRepoPrototype}
                  </td>
                  <td className="p-3.5 text-emerald-950 bg-emerald-50/40 font-medium leading-relaxed min-w-[240px]">
                    {row.targetUnifiedArchitecture}
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </section>

      {/* Part 2: Deep Dive on How to Weave AI with LearnHarness */}
      <section className="rounded-2xl border border-slate-200 bg-white p-6 shadow-xs space-y-5">
        <div className="flex flex-wrap items-center justify-between gap-3 border-b border-slate-100 pb-4">
          <div>
            <h2 className="text-lg font-bold text-[#252746] flex items-center gap-2">
              <BrainCircuit className="h-5 w-5 text-[#7E4BDE]" />
              ۲. معماری دقیق ترکیب هوش مصنوعی با <code className="font-mono-code text-sm bg-purple-100 text-[#7E4BDE] px-2 py-0.5 rounded">LearnHarness</code> (بدون توهم‌زایی و بدون لو رفتن کلید)
            </h2>
            <p className="text-xs text-slate-600 mt-1">
              نحوه کارکرد چرخه ۴ فازی <code className="font-mono-code">Measure → Plan → Teach → Practice</code> روی گراف گزاره‌های کتاب درسی کنکور در دو حالت آفلاین و آنلاین:
            </p>
          </div>
          <span className="rounded-full bg-purple-100 text-[#7E4BDE] px-3 py-1 text-xs font-bold font-mono-code">
            github.com/amosblomqvist/learnharness
          </span>
        </div>

        {/* Interactive 4-Phase Selector */}
        <div className="grid grid-cols-1 md:grid-cols-4 gap-2.5">
          {HARNESS_PHASES.map((hp, idx) => (
            <button
              key={hp.phase}
              type="button"
              onClick={() => setActiveHarnessIdx(idx)}
              className={`rounded-xl border p-3.5 text-right transition cursor-pointer ${
                activeHarnessIdx === idx
                  ? "border-[#7E4BDE] bg-[#252746] text-white shadow-md"
                  : "border-slate-200 bg-[#F6F7FB] hover:bg-white text-[#252746]"
              }`}
            >
              <div className="text-[11px] font-mono-code opacity-80">{hp.phase}</div>
              <div className="font-bold text-xs mt-1 leading-snug">{hp.titleFa}</div>
            </button>
          ))}
        </div>

        {/* Active LearnHarness Phase Detail */}
        {HARNESS_PHASES[activeHarnessIdx] && (
          <div className="rounded-2xl border border-[#7E4BDE]/30 bg-purple-50/30 p-5 space-y-4">
            <div className="flex flex-wrap items-center justify-between gap-2">
              <h3 className="font-extrabold text-base text-[#252746]">
                {HARNESS_PHASES[activeHarnessIdx].titleFa}
              </h3>
              <span className="rounded-lg bg-[#7E4BDE] text-white px-3 py-1 text-xs font-bold">
                {HARNESS_PHASES[activeHarnessIdx].badge}
              </span>
            </div>

            <p className="text-xs md:text-sm text-slate-700 leading-relaxed">
              {HARNESS_PHASES[activeHarnessIdx].whatHappens}
            </p>

            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
              <div className="rounded-xl bg-white border border-slate-200 p-4">
                <h4 className="text-xs font-bold text-[#252746] mb-2 flex items-center gap-1.5">
                  <Layers className="h-4 w-4 text-[#7E4BDE]" />
                  المان‌های رابط کاربری در تب سوم (AI) و داخل درس:
                </h4>
                <ul className="space-y-1.5 text-xs text-slate-700">
                  {HARNESS_PHASES[activeHarnessIdx].uiComponents.map((comp, i) => (
                    <li key={i} className="flex items-start gap-1.5">
                      <CheckCircle2 className="h-3.5 w-3.5 text-emerald-600 shrink-0 mt-0.5" />
                      <span>{comp}</span>
                    </li>
                  ))}
                </ul>
              </div>

              <div className="rounded-xl bg-white border border-slate-200 p-4">
                <h4 className="text-xs font-bold text-[#252746] mb-2 flex items-center gap-1.5">
                  <Sparkles className="h-4 w-4 text-amber-500" />
                  قانون تغییر وضعیت در گراف دانش و دیتابیس:
                </h4>
                <p className="text-xs text-slate-700 leading-relaxed">
                  {HARNESS_PHASES[activeHarnessIdx].stateTransition}
                </p>
              </div>
            </div>
          </div>
        )}

        {/* SQLite Room v2 & Proposition Graph Schema Box */}
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-4">
          <div className="rounded-xl bg-[#1E2038] text-slate-100 p-4 space-y-2">
            <div className="flex items-center justify-between">
              <span className="text-xs font-bold text-emerald-300 flex items-center gap-1.5">
                <Database className="h-4 w-4" />
                اسکیمای رسمی SQLite Room v2 میمو ۹٫۳۵ (mimo.db · 06_SPEC_STORAGE.md):
              </span>
              <span className="text-[11px] font-mono-code text-slate-400">
                hash: 2b8ab6d303d9a501…
              </span>
            </div>
            <pre className="text-[11px] font-mono-code bg-black/40 rounded-lg p-3 overflow-x-auto text-emerald-200 leading-relaxed dir-ltr text-left">
{`CREATE TABLE lesson_progress (
  lesson_id INTEGER NOT NULL,
  tutorial_id INTEGER NOT NULL,
  tutorial_version INTEGER NOT NULL,
  track_id INTEGER NOT NULL,
  publish_set_version INTEGER NOT NULL, -- 753
  tries INTEGER NOT NULL,               -- 0/1 solved flag (tries >= 1)
  attempts INTEGER NOT NULL,            -- session submission counter
  started_at INTEGER NOT NULL,
  completed_at INTEGER NOT NULL,
  is_practice_progress INTEGER NOT NULL,
  in_queue INTEGER NOT NULL,            -- 1 = pending sync / review
  PRIMARY KEY(lesson_id, tutorial_id)
);`}
            </pre>
          </div>

          <div className="rounded-xl bg-[#1E2038] text-slate-100 p-4 space-y-2">
            <div className="flex items-center justify-between">
              <span className="text-xs font-bold text-purple-300 flex items-center gap-1.5">
                <ShieldCheck className="h-4 w-4" />
                قرارداد دولایه LearnHarness (آفلاین محلی + استریم SSE سروری):
              </span>
              <span className="text-[11px] font-mono-code text-slate-400">
                app/src/harness.js
              </span>
            </div>
            <pre className="text-[11px] font-mono-code bg-black/40 rounded-lg p-3 overflow-x-auto text-purple-200 leading-relaxed dir-ltr text-left">
{`// 1. Offline Mode (Default in Mimo.html & PWA):
externalProvider = "not-configured";
provider = new LocalContentProvider(STRUCTURED_PACKAGE.propositions);

// 2. Online Backend Mode (Next.js / FastAPI Gateway):
// Client sends Bearer token to /api/v1/ai/harness (Accept: text/event-stream)
// Server reads process.env.AI_API_KEY and streams Socratic steps
// anchored strictly to STRUCTURED_PACKAGE.propositions[chapterId].`}
            </pre>
          </div>
        </div>
      </section>

      {/* Part 3: Complete Catalog of Required Open-Source Repositories & Tools */}
      <section className="space-y-4">
        <div>
          <h2 className="text-lg font-bold text-[#252746] flex items-center gap-2">
            <ExternalLink className="h-5 w-5 text-[#7E4BDE]" />
            ۳. فهرست کامل ریپوزیتوری‌های متن‌باز و ابزارهای مورد نیاز از اینترنت
          </h2>
          <p className="text-xs text-slate-600 mt-1">
            تمام کتابخانه‌ها، الگوریتم‌ها و ابزارهایی که ایجنت در طول ۱۲ فاز برای تکمیل پروژه استفاده می‌کند:
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          {externalRepos.map((repo) => (
            <div
              key={repo.id}
              className="rounded-2xl border border-slate-200 bg-white p-5 shadow-xs flex flex-col justify-between space-y-3"
            >
              <div className="space-y-2">
                <div className="flex flex-wrap items-center justify-between gap-2">
                  <h3 className="font-bold text-sm text-[#252746]">{repo.name}</h3>
                  <span className="rounded-full bg-[#7E4BDE]/10 text-[#7E4BDE] px-2.5 py-0.5 text-[11px] font-bold">
                    {repo.priority}
                  </span>
                </div>
                <div className="flex flex-wrap items-center gap-2 text-[11px] font-mono-code text-slate-500">
                  <span className="bg-slate-100 px-2 py-0.5 rounded">{repo.repoUrl}</span>
                  <span>· License: {repo.license}</span>
                </div>
                <div className="text-xs font-semibold text-indigo-900 bg-indigo-50/70 px-2.5 py-1 rounded-lg inline-block">
                  {repo.layer}
                </div>
                <p className="text-xs text-slate-700 leading-relaxed">{repo.whyNeeded}</p>
              </div>

              <div className="rounded-xl bg-[#F6F7FB] border border-slate-200 p-3 text-xs text-slate-800 leading-relaxed">
                <strong className="block text-[#252746] mb-0.5">
                  نحوه اتصال گام‌به‌گام توسط ایجنت:
                </strong>
                {repo.howToIntegrateStepByStep}
              </div>
            </div>
          ))}
        </div>
      </section>
    </div>
  );
}
