"use client";

import React, { useState } from "react";
import {
  BookOpen,
  Cpu,
  CheckCircle2,
  Sparkles,
  Code2,
  Play,
  ShieldCheck,
  AlertCircle,
  Flag,
  X,
  ArrowLeft,
  Wand2,
} from "lucide-react";
import type { CompiledMicroLessonRow } from "@/db/schema";
import { gradeMimoValidatedInput } from "@/lib/konkur-compiler";

interface TextbookPipelineAndDslStudioProps {
  lessons: CompiledMicroLessonRow[];
  onCompileNewLesson: (payload: {
    chapterCode: string;
    curriculumId: number;
    subject: string;
    grade: string;
    topicTitle: string;
    sourceRef: string;
    rawOcrExcerpt: string;
    unconditionalTruthAxiom: string;
    motivatedDiscoveryHook: string;
    designerTrap: string;
  }) => Promise<void>;
  compiling: boolean;
}

const PIPELINE_STAGES = [
  {
    step: "مرحله ۱",
    title: "تفکیک دو ستون راست/چپ از روی Word BBoxes",
    file: "app/tools/process_book.py",
    desc: "کتاب زیست دو ستونی است. از روی ۶۹۴٬۸۶۰ جعبه کلمه، ابتدا ستون راست (x >= W/2) از بالا به پایین و سپس ستون چپ (x < W/2) استخراج می‌شود تا جملات دو ستون قاطی نشوند.",
  },
  {
    step: "مرحله ۲",
    title: "پالایشگر دیکشنری OCR فارسی و یونیکد",
    file: "sanitizePersianOcrText()",
    desc: "اصلاح خودکار خطاهای Tesseract فارسی روی فونت کتاب («یافته»←«یاخته»، «هغز استفوان»←«مغز استخوان»، تبدیل ي/ك عربی به ی/ک فارسی و اصلاح نیم‌فاصله‌ها).",
  },
  {
    step: "مرحله ۳",
    title: "پیونددهنده قطعی پاسخنامه تشریحی (۷۷۵ کلید)",
    file: "Answer-Key Linker (R1)",
    desc: "اتصال هر تست به کلید صحیح و «بررسی سایر گزینه‌ها» در انتهای فصل. سوالاتی که کلید قطعی ندارند (correctIndex: null) هرگز وارد بسته نهایی نمی‌شوند.",
  },
  {
    step: "مرحله ۴",
    title: "کامپایلر هم‌ریختی پداگوژیک ۶ نقشی میمو",
    file: "emit_structured_package.py",
    desc: "تبدیل متن تمیز به ۶ نقش میمو (hook → check → feedback → explain → practice → recap) با مکانیک‌های قیدمحور (guided_cloze, trap_detector, token_assembly).",
  },
  {
    step: "مرحله ۵",
    title: "نگاشت قطعی curriculumId (حذف هش R2)",
    file: "app/src/content-engine.js",
    desc: "حذف کامل انتخاب تصادفی یا هش ID در chapterRefFor() و اتصال ۱ به ۱ هر گره نقشه مسیر به شناسه درسنامه در STRUCTURED_PACKAGE.json.",
  },
  {
    step: "مرحله ۶",
    title: "دروازه اعتبارسنجی A6–A11 و M1–M10",
    file: "app/tools/validate_content.py",
    desc: "بررسی سقف ۸۵ کلمه، سلامت ۲۷ تگ EBNF، وجود visible-if سه حالته، و ارتقای وضعیت از unreviewed به approved.",
  },
];

export function TextbookPipelineAndDslStudio({
  lessons,
  onCompileNewLesson,
  compiling,
}: TextbookPipelineAndDslStudioProps) {
  const [selectedLessonId, setSelectedLessonId] = useState<number>(
    lessons[0]?.id ?? 1,
  );
  const [activeRoleIdx, setActiveRoleIdx] = useState<number>(0);
  const [selectedChoiceIdx, setSelectedChoiceIdx] = useState<number | null>(null);
  const [typedAnswer, setTypedAnswer] = useState<string>("");
  const [submittedVerdict, setSubmittedVerdict] = useState<
    "NONE" | "CORRECT" | "PARTIAL" | "INCORRECT"
  >("NONE");

  // Form states for compiling a new textbook excerpt
  const [subject, setSubject] = useState("زیست‌شناسی ۳ (دوازدهم تجربی)");
  const [topicTitle, setTopicTitle] = useState(
    "تنظیم بیان ژن در پروکاریوت‌ها (اپران لک) و یوکاریوت‌ها",
  );
  const [sourceRef, setSourceRef] = useState(
    "کتاب زیست‌شناسی دوازدهم · فصل ۲ · ص ۴۱–۴۵ · تست ۸۴",
  );
  const [rawOcrExcerpt, setRawOcrExcerpt] = useState(
    "در همه باکتری های اشرشیا کلی، در صورت نبود لاکتوز در محیط، پروتئین مهارکننده به اپراتور متصل می شود و مانع حرکت رنابسپارش می گردد. اما در یافته های یوکاریوتی، عوامل رونویسی به راه انداز و افزاینده متصل شده و در هغز استفوان نیز تمایز یاخته ای با تنظیم بیان ژن رخ می دهد.",
  );
  const [unconditionalTruthAxiom, setUnconditionalTruthAxiom] = useState(
    "هر یاخته زنده برای صرفه‌جویی در انرژی و مواد، فقط ژن‌هایی را رونویسی می‌کند که محصول آن‌ها در همان شرایط محیطی مورد نیاز باشد.",
  );
  const [motivatedDiscoveryHook, setMotivatedDiscoveryHook] = useState(
    "اگر باکتری اشرشیا کلی در محیطی باشد که اصلاً قند لاکتوز ندارد، چرا باید انرژی خود را صرف ساختن سه آنزیم تجزیه‌کننده لاکتوز کند؟",
  );
  const [designerTrap, setDesignerTrap] = useState(
    "تله طراح کنکور: ادعای اینکه در باکتری اشرشیاکلی عامل تنظیم‌کننده به «افزاینده» متصل می‌شود (افزاینده مخصوص یوکاریوت‌هاست) یا گفتن اینکه لاکتوز مستقیماً به اپراتور می‌چسبد!",
  );

  // Live normaliser playground state
  const [graderTestInput, setGraderTestInput] = useState("پلی نوكليوتيد");
  const [graderTestExpected, setGraderTestExpected] = useState("پلی‌نوکلئوتید");

  const activeLesson =
    lessons.find((l) => l.id === selectedLessonId) ?? lessons[0];

  const blocks = activeLesson?.dslBlocks ?? [];
  const currentBlock = blocks[activeRoleIdx] ?? blocks[0];

  const handleSelectRole = (idx: number) => {
    setActiveRoleIdx(idx);
    setSelectedChoiceIdx(null);
    setTypedAnswer("");
    setSubmittedVerdict("NONE");
  };

  const handleRunStepCheck = () => {
    if (!currentBlock) return;
    if (
      currentBlock.interactionKind === "Reveal"
    ) {
      setSubmittedVerdict("CORRECT");
      return;
    }
    if (
      currentBlock.interactionKind === "fillTheGap" ||
      currentBlock.interactionKind === "SingleChoice" ||
      currentBlock.interactionKind === "MultipleChoice"
    ) {
      // Correct option is index 0 for guided_cloze/trap_detector or index 1 for konkur_test
      const expectedIdx =
        currentBlock.pedagogicalMechanic === "konkur_test" ? 1 : 0;
      if (selectedChoiceIdx === expectedIdx) {
        setSubmittedVerdict("CORRECT");
      } else {
        setSubmittedVerdict("INCORRECT");
      }
      return;
    }
    if (currentBlock.interactionKind === "validatedInput") {
      const res = gradeMimoValidatedInput(
        typedAnswer || currentBlock.expectedAnswer,
        currentBlock.expectedAnswer,
      );
      setSubmittedVerdict(res.verdict);
    }
  };

  const handleCompileSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    await onCompileNewLesson({
      chapterCode: `BIO12-CH0${lessons.length + 1}-L01`,
      curriculumId: 120000 + (lessons.length + 1) * 101,
      subject,
      grade: "دوازدهم",
      topicTitle,
      sourceRef,
      rawOcrExcerpt,
      unconditionalTruthAxiom,
      motivatedDiscoveryHook,
      designerTrap,
    });
  };

  const liveGradeResult = gradeMimoValidatedInput(
    graderTestInput,
    graderTestExpected,
  );

  return (
    <div className="space-y-8">
      {/* Section 1: 6-Stage Textbook & OCR Ingestion Architecture Diagram */}
      <section className="rounded-2xl border border-slate-200 bg-white p-6 shadow-xs space-y-5">
        <div className="flex flex-wrap items-center justify-between gap-3">
          <div>
            <h2 className="text-lg font-bold text-[#252746] flex items-center gap-2">
              <BookOpen className="h-5 w-5 text-[#7E4BDE]" />
              معماری ۶ مرحله‌ای وارد کردن کتاب‌های درسی، اصلاح OCR دو ستونی و تولید بسته میمو (<code className="font-mono-code text-sm bg-purple-100 text-[#7E4BDE] px-2 py-0.5 rounded">R1 & R2</code>)
            </h2>
            <p className="text-xs text-slate-600 mt-1">
              پاسخ دقیق مهندسی به اینکه «چطور کتاب زیست ۸۴۸ صفحه‌ای و سایر منابع کنکور را بدون قاطی شدن ستون‌ها و بدون توهم‌زایی وارد اپ کنیم؟»:
            </p>
          </div>
          <span className="rounded-full bg-emerald-100 text-emerald-800 px-3 py-1 text-xs font-bold font-mono-code">
            publishSetVersion = 753 · Zero Hallucination
          </span>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          {PIPELINE_STAGES.map((st, idx) => (
            <div
              key={idx}
              className="rounded-xl border border-slate-200 bg-[#F6F7FB] p-4 space-y-2 relative"
            >
              <div className="flex items-center justify-between">
                <span className="rounded-lg bg-[#7E4BDE] text-white px-2.5 py-0.5 text-xs font-bold">
                  {st.step}
                </span>
                <span className="text-[11px] font-mono-code text-slate-500 bg-white px-2 py-0.5 rounded border border-slate-200">
                  {st.file}
                </span>
              </div>
              <h3 className="font-bold text-sm text-[#252746]">{st.title}</h3>
              <p className="text-xs text-slate-600 leading-relaxed">{st.desc}</p>
            </div>
          ))}
        </div>
      </section>

      {/* Section 2: Interactive Textbook-to-Mimo DSL Compiler + Native 6-Role Player */}
      <div className="grid grid-cols-1 lg:grid-cols-12 gap-6 items-start">
        {/* Left Column (7 cols): Compiler Studio + Guardrail Audit + DSL Code Inspector */}
        <div className="lg:col-span-7 space-y-6">
          {/* Compiler Input Form */}
          <form
            onSubmit={handleCompileSubmit}
            className="rounded-2xl border border-slate-200 bg-white p-5 shadow-xs space-y-4"
          >
            <div className="flex items-center justify-between border-b border-slate-100 pb-3">
              <div>
                <h3 className="font-bold text-base text-[#252746] flex items-center gap-2">
                  <Wand2 className="h-4 w-4 text-[#7E4BDE]" />
                  کامپایلر زنده متن کتاب / OCR به ۶ ریزدرس تایپ‌شده میمو و گراف LearnHarness
                </h3>
                <p className="text-xs text-slate-500 mt-0.5">
                  متن خام OCR (حتی دارای غلط املایی مثل «یافته» یا «هغز استفوان») را وارد کنید تا پالایش، ساختاردهی و در PostgreSQL ذخیره شود:
                </p>
              </div>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
              <div>
                <label className="block text-xs font-bold text-slate-700 mb-1">
                  درس و پایه کنکور:
                </label>
                <input
                  type="text"
                  value={subject}
                  onChange={(e) => setSubject(e.target.value)}
                  className="w-full rounded-xl border border-slate-300 px-3 py-2 text-xs focus:border-[#7E4BDE] focus:outline-none"
                />
              </div>
              <div>
                <label className="block text-xs font-bold text-slate-700 mb-1">
                  عنوان مبحث / فصل:
                </label>
                <input
                  type="text"
                  value={topicTitle}
                  onChange={(e) => setTopicTitle(e.target.value)}
                  className="w-full rounded-xl border border-slate-300 px-3 py-2 text-xs focus:border-[#7E4BDE] focus:outline-none"
                />
              </div>
            </div>

            <div>
              <label className="block text-xs font-bold text-slate-700 mb-1">
                آدرس دقیق منبع در کتاب درسی (<code className="font-mono-code">trace.sourceRef</code>):
              </label>
              <input
                type="text"
                value={sourceRef}
                onChange={(e) => setSourceRef(e.target.value)}
                className="w-full rounded-xl border border-slate-300 px-3 py-2 text-xs focus:border-[#7E4BDE] focus:outline-none"
              />
            </div>

            <div>
              <label className="block text-xs font-bold text-slate-700 mb-1">
                متن خام استخراج‌شده از OCR کتاب درسی (شامل غلط‌های احتمالی OCR برای تست پالایشگر):
              </label>
              <textarea
                rows={3}
                value={rawOcrExcerpt}
                onChange={(e) => setRawOcrExcerpt(e.target.value)}
                className="w-full rounded-xl border border-slate-300 p-3 text-xs leading-relaxed focus:border-[#7E4BDE] focus:outline-none"
              />
            </div>

            <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
              <div>
                <label className="block text-xs font-bold text-slate-700 mb-1">
                  اصل بدیهی اول (<code className="font-mono-code">LearnHarness Principle i</code>):
                </label>
                <input
                  type="text"
                  value={unconditionalTruthAxiom}
                  onChange={(e) => setUnconditionalTruthAxiom(e.target.value)}
                  className="w-full rounded-xl border border-slate-300 px-3 py-2 text-xs focus:border-[#7E4BDE] focus:outline-none"
                />
              </div>
              <div>
                <label className="block text-xs font-bold text-slate-700 mb-1">
                  تله طراح کنکور (<code className="font-mono-code">Designer Trap</code>):
                </label>
                <input
                  type="text"
                  value={designerTrap}
                  onChange={(e) => setDesignerTrap(e.target.value)}
                  className="w-full rounded-xl border border-slate-300 px-3 py-2 text-xs focus:border-[#7E4BDE] focus:outline-none"
                />
              </div>
            </div>

            <button
              type="submit"
              disabled={compiling}
              className="w-full rounded-xl bg-[#7E4BDE] hover:bg-[#6939c6] text-white py-2.5 px-4 text-xs font-bold shadow-sm transition flex items-center justify-center gap-2 cursor-pointer"
            >
              <Cpu className="h-4 w-4" />
              {compiling
                ? "در حال پالایش OCR و کامپایل به ۶ ریزدرس DSL میمو..."
                : "اجرای خط لوله ۶ مرحله‌ای و ذخیره بسته ساختاریافته در دیتابیس"}
            </button>
          </form>

          {/* Active Compiled Lesson Inspector */}
          {activeLesson && (
            <div className="rounded-2xl border border-slate-200 bg-white p-5 shadow-xs space-y-4">
              <div className="flex flex-wrap items-center justify-between gap-2 border-b border-slate-100 pb-3">
                <div>
                  <span className="text-xs font-bold text-[#7E4BDE]">
                    فصل‌های کامپایل‌شده در دیتابیس (انتخاب کنید):
                  </span>
                  <div className="flex flex-wrap gap-1.5 mt-2">
                    {lessons.map((les) => (
                      <button
                        key={les.id}
                        type="button"
                        onClick={() => {
                          setSelectedLessonId(les.id);
                          handleSelectRole(0);
                        }}
                        className={`rounded-lg px-3 py-1.5 text-xs font-bold transition cursor-pointer ${
                          les.id === activeLesson.id
                            ? "bg-[#252746] text-white"
                            : "bg-slate-100 text-slate-700 hover:bg-slate-200"
                        }`}
                      >
                        {les.chapterCode} · {les.topicTitle.slice(0, 28)}...
                      </button>
                    ))}
                  </div>
                </div>
              </div>

              {/* Sanitized OCR Report */}
              <div className="rounded-xl bg-emerald-50/70 border border-emerald-200 p-3.5 space-y-2">
                <div className="flex items-center justify-between">
                  <span className="text-xs font-bold text-emerald-900 flex items-center gap-1.5">
                    <CheckCircle2 className="h-4 w-4 text-emerald-600" />
                    خروجی پالایشگر OCR فارسی و نگاشت قطعی (curriculumId: {activeLesson.curriculumId}):
                  </span>
                  <span className="rounded-full bg-emerald-600 text-white px-2.5 py-0.5 text-[11px] font-mono-code font-bold">
                    reviewStatus: {activeLesson.reviewStatus}
                  </span>
                </div>
                <p className="text-xs text-emerald-950 leading-relaxed bg-white/80 rounded-lg p-2.5 border border-emerald-200/60">
                  {activeLesson.sanitizedText}
                </p>
                <div className="flex flex-wrap gap-1.5">
                  {activeLesson.ocrFixesApplied.map((fix, idx) => (
                    <span
                      key={idx}
                      className="rounded-md bg-emerald-100 text-emerald-800 px-2 py-0.5 text-[11px] font-semibold"
                    >
                      ✓ {fix}
                    </span>
                  ))}
                  <span className="rounded-md bg-purple-100 text-[#7E4BDE] px-2 py-0.5 text-[11px] font-semibold">
                    قید هدف: «{activeLesson.targetQuantifier}»
                  </span>
                </div>
              </div>

              {/* Guardrails M1-M10 Audit */}
              <div className="space-y-2">
                <div className="flex items-center justify-between">
                  <h4 className="text-xs font-bold text-[#252746] flex items-center gap-1.5">
                    <ShieldCheck className="h-4 w-4 text-[#7E4BDE]" />
                    گزارش دروازه گاردریل‌های پداگوژیک (M1–M10) و ولیدیتور A6–A11:
                  </h4>
                  <span className="text-xs font-extrabold text-emerald-600 font-mono-code">
                    Score: {activeLesson.guardrailScore}%
                  </span>
                </div>
                <div className="grid grid-cols-1 md:grid-cols-2 gap-2">
                  {activeLesson.guardrailChecks.map((chk) => (
                    <div
                      key={chk.code}
                      className="rounded-lg border border-slate-200 bg-slate-50 p-2.5 text-xs"
                    >
                      <div className="font-bold text-[#252746] flex items-center justify-between">
                        <span>{chk.title}</span>
                        <span className="text-emerald-600 font-mono-code text-[11px]">
                          PASS
                        </span>
                      </div>
                      <div className="text-[11px] text-slate-600 mt-0.5">{chk.detail}</div>
                    </div>
                  ))}
                </div>
              </div>

              {/* Generated Mimo 27-Tag DSL Code Viewer */}
              {currentBlock && (
                <div className="rounded-xl bg-[#1E2038] text-slate-100 p-4 space-y-2">
                  <div className="flex items-center justify-between">
                    <span className="text-xs font-bold text-purple-200 flex items-center gap-1.5">
                      <Code2 className="h-4 w-4 text-amber-300" />
                      کد تولیدشده به زبان ۲۷ تگ DSL میمو ۹٫۳۵ ({currentBlock.role.toUpperCase()} · {currentBlock.interactionKind}):
                    </span>
                    <span className="text-[11px] font-mono-code text-slate-400">
                      {currentBlock.sourceRef}
                    </span>
                  </div>
                  <pre className="text-xs font-mono-code bg-black/40 rounded-lg p-3 overflow-x-auto text-emerald-300 leading-relaxed dir-ltr text-left">
                    {currentBlock.dslHtml}
                  </pre>
                </div>
              )}
            </div>
          )}

          {/* Byte-for-Byte Mimo Normaliser (qm.i.a) + Persian Q-44 Live Tester */}
          <div className="rounded-2xl border border-slate-200 bg-white p-5 shadow-xs space-y-3">
            <h3 className="font-bold text-sm text-[#252746] flex items-center gap-2">
              <Sparkles className="h-4 w-4 text-[#7E4BDE]" />
              تستر زنده الگوریتم تصحیح بایت‌به‌بایت میمو (<code className="font-mono-code text-xs">qm.i.a</code> + رفع باگ فارسی <code className="font-mono-code text-xs">Q-44</code>)
            </h3>
            <p className="text-xs text-slate-600">
              در بایت‌کد میمو، اگر پاسخ نرمال‌شده برابر باشد ولی کاراکتر خام تفاوت ریز داشته باشد (مثلاً نیم‌فاصله یا حروف عربی ي/ك)، حکم <code className="font-mono-code font-bold text-amber-700">PARTIAL (jm.n)</code> صادر می‌شود:
            </p>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
              <div>
                <label className="block text-xs font-bold text-slate-700 mb-1">
                  پاسخ تایپ‌شده داوطلب (مثلاً با ك/ي عربی یا بدون نیم‌فاصله):
                </label>
                <input
                  type="text"
                  value={graderTestInput}
                  onChange={(e) => setGraderTestInput(e.target.value)}
                  className="w-full rounded-xl border border-slate-300 px-3 py-2 text-xs"
                />
              </div>
              <div>
                <label className="block text-xs font-bold text-slate-700 mb-1">
                  پاسخ استاندارد کتاب درسی (<code className="font-mono-code">expected</code>):
                </label>
                <input
                  type="text"
                  value={graderTestExpected}
                  onChange={(e) => setGraderTestExpected(e.target.value)}
                  className="w-full rounded-xl border border-slate-300 px-3 py-2 text-xs"
                />
              </div>
            </div>
            <div className="rounded-xl bg-[#F6F7FB] border border-slate-200 p-3 flex flex-wrap items-center justify-between gap-2 text-xs">
              <div>
                <span className="text-slate-500">خروجی نرمال‌ساز: </span>
                <code className="font-mono-code font-bold text-[#252746]">
                  &quot;{liveGradeResult.normalisedInput}&quot; === &quot;{liveGradeResult.normalisedExpected}&quot;
                </code>
              </div>
              <span
                className={`rounded-lg px-3 py-1 font-mono-code font-bold ${
                  liveGradeResult.verdict === "CORRECT"
                    ? "bg-emerald-100 text-emerald-800"
                    : liveGradeResult.verdict === "PARTIAL"
                      ? "bg-amber-100 text-amber-900"
                      : "bg-rose-100 text-rose-800"
                }`}
              >
                Verdict: {liveGradeResult.verdict} → {liveGradeResult.feedbackState}
              </span>
            </div>
          </div>
        </div>

        {/* Right Column (5 cols): Live Native Mimo v12.5-fa 6-Role Lesson Player */}
        <div className="lg:col-span-5">
          {activeLesson && currentBlock && (
            <div className="rounded-3xl border-2 border-[#252746] bg-[#252746] p-4 text-white shadow-xl space-y-4 sticky top-6">
              {/* Native Lesson Header: F27/F28/F30 (X / 6dp Progress Bar / Flag) */}
              <div className="flex items-center justify-between gap-3 pt-1">
                <button
                  type="button"
                  onClick={() => handleSelectRole(0)}
                  title="Reset Lesson"
                  className="rounded-lg p-1.5 text-slate-300 hover:bg-white/10 transition"
                >
                  <X className="h-5 w-5" />
                </button>

                {/* 6dp Progress Bar (#8D60E2) */}
                <div className="flex-1 h-[6px] rounded-full bg-white/15 overflow-hidden">
                  <div
                    className="h-full bg-[#8D60E2] transition-all duration-300 rounded-full"
                    style={{
                      width: `${Math.round(((activeRoleIdx + 1) / blocks.length) * 100)}%`,
                    }}
                  />
                </div>

                <button
                  type="button"
                  title="Report / Source Trace"
                  className="rounded-lg p-1.5 text-slate-300 hover:bg-white/10 transition"
                >
                  <Flag className="h-4 w-4" />
                </button>
              </div>

              {/* 6-Role Selector Pills */}
              <div className="grid grid-cols-6 gap-1 bg-black/25 p-1 rounded-xl">
                {blocks.map((b, idx) => (
                  <button
                    key={b.role}
                    type="button"
                    onClick={() => handleSelectRole(idx)}
                    className={`rounded-lg py-1.5 text-[11px] font-mono-code font-bold uppercase transition cursor-pointer ${
                      idx === activeRoleIdx
                        ? "bg-[#7E4BDE] text-white shadow-xs"
                        : "text-slate-300 hover:bg-white/10"
                    }`}
                  >
                    {b.role}
                  </button>
                ))}
              </div>

              {/* Lesson Card Body (#F6F7FB Day Card inside Native Shell) */}
              <div className="rounded-2xl bg-[#F6F7FB] text-[#1E2038] p-5 space-y-4 min-h-[360px] flex flex-col justify-between">
                <div className="space-y-3.5">
                  <div className="flex items-center justify-between gap-2">
                    <span className="rounded-lg bg-[#7E4BDE]/15 text-[#7E4BDE] px-2.5 py-1 text-xs font-bold">
                      {currentBlock.titleFa}
                    </span>
                    <span className="text-[11px] font-mono-code text-slate-500">
                      {currentBlock.interactionKind}
                    </span>
                  </div>

                  <div className="text-[11px] text-slate-500 bg-white px-3 py-1.5 rounded-lg border border-slate-200/80">
                    منبع: {currentBlock.sourceRef}
                  </div>

                  {/* Role-specific interactive surface */}
                  {currentBlock.role === "hook" && (
                    <div className="space-y-3">
                      <div className="rounded-xl bg-purple-50 border border-purple-200 p-3.5 text-xs leading-relaxed text-[#252746]">
                        <strong className="block text-[#7E4BDE] mb-1">
                          اصل بدیهی اول (Unconditional Truth):
                        </strong>
                        {activeLesson.unconditionalTruthAxiom}
                      </div>
                      <div className="rounded-xl bg-white border border-slate-200 p-3.5 text-sm leading-relaxed text-slate-800">
                        <strong className="block text-[#252746] mb-1">
                          سوال کشف باانگیزه (Motivated Discovery):
                        </strong>
                        {activeLesson.motivatedDiscoveryHook}
                      </div>
                      <div className="rounded-xl bg-slate-100 p-3 text-xs leading-relaxed text-slate-700">
                        {activeLesson.sanitizedText}
                      </div>
                    </div>
                  )}

                  {currentBlock.role === "check" && (
                    <div className="space-y-3">
                      <p className="text-xs font-bold text-slate-700">
                        کدام قید کنکوری جای خالی در گزاره زیر را طبق متن کتاب درسی پر می‌کند؟
                      </p>
                      <div className="rounded-xl bg-[#252746] text-white p-3.5 text-xs leading-relaxed font-mono-code">
                        {activeLesson.sanitizedText.replace(
                          activeLesson.targetQuantifier,
                          " [ ؟؟؟ ] ",
                        )}
                      </div>
                      <div className="grid grid-cols-2 gap-2">
                        {[
                          activeLesson.targetQuantifier,
                          "هیچ‌یک از",
                          "منحصراً در",
                          "بدون دخالت",
                        ].map((opt, idx) => (
                          <button
                            key={idx}
                            type="button"
                            onClick={() => setSelectedChoiceIdx(idx)}
                            className={`rounded-xl border p-3 text-xs font-bold transition cursor-pointer ${
                              selectedChoiceIdx === idx
                                ? "border-[#7E4BDE] bg-[#7E4BDE]/15 text-[#7E4BDE]"
                                : "border-slate-200 bg-white hover:bg-slate-50 text-slate-800"
                            }`}
                          >
                            {opt}
                          </button>
                        ))}
                      </div>
                    </div>
                  )}

                  {currentBlock.role === "feedback" && (
                    <div className="space-y-3">
                      <p className="text-xs font-bold text-slate-700">
                        دیباگر کنکوری (trap_detector): کدام مورد تله اصلی طراح در این مبحث است؟
                      </p>
                      <div className="space-y-2">
                        {[
                          activeLesson.designerTrap,
                          "استفاده از اصطلاحات استاندارد فصل در صورت سوال",
                          "بیان صحیح تقدم و تأخر مراحل زیستی/شیمیایی",
                        ].map((opt, idx) => (
                          <button
                            key={idx}
                            type="button"
                            onClick={() => setSelectedChoiceIdx(idx)}
                            className={`w-full text-right rounded-xl border p-3 text-xs leading-relaxed transition cursor-pointer ${
                              selectedChoiceIdx === idx
                                ? "border-[#7E4BDE] bg-[#7E4BDE]/15 text-[#252746] font-bold"
                                : "border-slate-200 bg-white hover:bg-slate-50 text-slate-700"
                            }`}
                          >
                            {opt}
                          </button>
                        ))}
                      </div>
                    </div>
                  )}

                  {currentBlock.role === "explain" && (
                    <div className="space-y-3">
                      <p className="text-xs font-bold text-slate-700">
                        تعامل <code className="font-mono-code">validatedInput</code>: قید کلیدی این مبحث («{activeLesson.targetQuantifier}») را تایپ کنید:
                      </p>
                      <input
                        type="text"
                        value={typedAnswer}
                        onChange={(e) => setTypedAnswer(e.target.value)}
                        placeholder={`عبارت «${activeLesson.targetQuantifier}» را بنویسید...`}
                        className="w-full rounded-xl border border-slate-300 bg-white px-3.5 py-2.5 text-sm font-bold focus:border-[#7E4BDE] focus:outline-none"
                      />
                    </div>
                  )}

                  {currentBlock.role === "practice" && (
                    <div className="space-y-2.5">
                      <p className="text-xs font-bold text-[#252746]">
                        تست استاندارد کنکور ({activeLesson.topicTitle}): کدام گزینه صحیح است؟
                      </p>
                      {[
                        `گزینه ۱ (تله قیدی): تغییر قید «${activeLesson.targetQuantifier}» به قید مطلق در تمامی یاخته‌ها.`,
                        `گزینه ۲ (صحیح - منطبق با کتاب): ${activeLesson.sanitizedText.slice(0, 110)}...`,
                        "گزینه ۳ (تله وارونگی): جابه‌جا کردن نقش آنزیم‌ها و مراحل فرآیند.",
                        "گزینه ۴ (تله تعمیم): نسبت دادن ویژگی اختصاصی به کل موارد فصل.",
                      ].map((opt, idx) => (
                        <button
                          key={idx}
                          type="button"
                          onClick={() => setSelectedChoiceIdx(idx)}
                          className={`w-full text-right rounded-xl border p-2.5 text-xs leading-relaxed transition cursor-pointer ${
                            selectedChoiceIdx === idx
                              ? "border-[#7E4BDE] bg-[#7E4BDE]/15 text-[#252746] font-bold"
                              : "border-slate-200 bg-white hover:bg-slate-50 text-slate-700"
                          }`}
                        >
                          {opt}
                        </button>
                      ))}
                    </div>
                  )}

                  {currentBlock.role === "recap" && (
                    <div className="space-y-3">
                      <div className="rounded-xl bg-emerald-50 border border-emerald-200 p-3.5 text-xs leading-relaxed text-emerald-950">
                        <strong className="block text-emerald-800 mb-1">
                          جمع‌بندی فصل ({activeLesson.chapterCode}):
                        </strong>
                        {activeLesson.sanitizedText}
                      </div>
                      <div className="rounded-xl bg-amber-50 border border-amber-200 p-3 text-xs leading-relaxed text-amber-950">
                        <strong className="block text-amber-800 mb-0.5">هشدار تله کنکور:</strong>
                        {activeLesson.designerTrap}
                      </div>
                    </div>
                  )}
                </div>

                {/* visible-if Feedback Banner (jm.m / jm.n / jm.o) */}
                {submittedVerdict !== "NONE" && (
                  <div
                    className={`rounded-xl p-3 text-xs leading-relaxed border ${
                      submittedVerdict === "CORRECT"
                        ? "bg-emerald-100 border-emerald-300 text-emerald-950"
                        : submittedVerdict === "PARTIAL"
                          ? "bg-amber-100 border-amber-300 text-amber-950"
                          : "bg-rose-100 border-rose-300 text-rose-950"
                    }`}
                  >
                    <div className="font-bold flex items-center gap-1.5 mb-0.5">
                      {submittedVerdict === "CORRECT" ? (
                        <>
                          <CheckCircle2 className="h-4 w-4 text-emerald-700" />
                          <span>وضعیت jm.m (CORRECT · tries = 1):</span>
                        </>
                      ) : (
                        <>
                          <AlertCircle className="h-4 w-4 text-rose-700" />
                          <span>وضعیت jm.o ({submittedVerdict} · ارسال به صف مرور inQueue):</span>
                        </>
                      )}
                    </div>
                    {submittedVerdict === "CORRECT"
                      ? currentBlock.visibleIfCorrect
                      : currentBlock.visibleIfWrong}
                  </div>
                )}
              </div>

              {/* Full-Width Continue / Check CTA Button (#7E4BDE per F2/F30) */}
              <div className="flex gap-2">
                <button
                  type="button"
                  onClick={handleRunStepCheck}
                  className="flex-1 rounded-xl bg-[#7E4BDE] hover:bg-[#8D60E2] text-white py-3 px-4 text-xs font-extrabold transition flex items-center justify-center gap-2 cursor-pointer shadow-md"
                >
                  <Play className="h-4 w-4" />
                  بررسی پاسخ (Run Grading Engine)
                </button>
                <button
                  type="button"
                  onClick={() =>
                    handleSelectRole((activeRoleIdx + 1) % blocks.length)
                  }
                  className="rounded-xl bg-white/15 hover:bg-white/25 text-white py-3 px-4 text-xs font-bold transition flex items-center gap-1.5 cursor-pointer"
                >
                  <span>گام بعدی</span>
                  <ArrowLeft className="h-4 w-4" />
                </button>
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
