"use client";

import React, { useState } from "react";
import {
  GitBranch,
  Archive,
  Ban,
  AlertTriangle,
  CheckCircle2,
  XCircle,
  ShieldAlert,
  FileCode2,
  Wrench,
  Layers,
} from "lucide-react";
import type {
  BranchOrArchiveAudit,
  FrankensteinRootCause,
  DeadEndGuardrail,
} from "@/lib/repo-forensics-data";

interface ForensicAuditViewProps {
  branchesAndArchives: BranchOrArchiveAudit[];
  rootCauses: FrankensteinRootCause[];
  deadEnds: DeadEndGuardrail[];
  onJumpToPhase: (phaseCode: string) => void;
}

export function ForensicAuditView({
  branchesAndArchives,
  rootCauses,
  deadEnds,
  onJumpToPhase,
}: ForensicAuditViewProps) {
  const [selectedCategory, setSelectedCategory] = useState<string>("ALL");

  const categories = [
    "ALL",
    "محتوا و OCR",
    "موتور درس و DSL",
    "مهندسی معکوس و سرور",
    "رابط کاربری و CSS",
    "محیط و ابزار",
  ];

  const filteredDeadEnds =
    selectedCategory === "ALL"
      ? deadEnds
      : deadEnds.filter((d) => d.category === selectedCategory);

  return (
    <div className="space-y-8">
      {/* Executive Forensic Summary Banner */}
      <div className="rounded-2xl border border-[#7E4BDE]/25 bg-gradient-to-l from-[#252746] via-[#2D2F56] to-[#3B2667] p-6 text-white shadow-lg">
        <div className="flex flex-wrap items-center justify-between gap-4">
          <div className="space-y-2 max-w-4xl">
            <div className="inline-flex items-center gap-2 rounded-full bg-[#7E4BDE]/30 border border-[#8D60E2]/50 px-3.5 py-1 text-xs font-semibold text-purple-200">
              <Layers className="h-3.5 w-3.5" />
              گزارش کالبدشکافی مهندسی ریپوی github.com/danmillman008-hub/game.git
            </div>
            <h2 className="text-xl md:text-2xl font-bold leading-snug">
              چرا تلاش‌های قبلی به نتیجه نهایی نرسیدند و چطور این رشته‌های پراکنده به هم بافته می‌شوند؟
            </h2>
            <p className="text-sm text-slate-200 leading-relaxed">
              کالبدشکافی کامل ریپوی شما نشان داد که شما <strong className="text-amber-300">۲ شاخه مهندسی فوق‌العاده ارزشمند</strong> (شاخه{" "}
              <code className="font-mono-code bg-black/30 px-1.5 py-0.5 rounded text-purple-200">arena/ecb8af07-game</code>{" "}
              حاوی مهندسی معکوس بایت‌به‌بایت کدهای Kotlin و دیتابیس Room میمو ۹٫۳۵ و شاخه{" "}
              <code className="font-mono-code bg-black/30 px-1.5 py-0.5 rounded text-purple-200">arena/aebb90b7-game</code>{" "}
              حاوی پروتوتایپ مصوب <code className="font-mono-code">v12.5-fa</code>، ناوبری بومی M09 و OCR کامل ۸۴۸ صفحه کتاب زیست دوازدهم) به همراه{" "}
              <strong className="text-amber-300">۵ آرشیو مکمل</strong> در اختیار دارید؛ اما هیچ ایجنتی تا امروز این دو شاخه و کامپایلر پداگوژیک کنکور را به هم متصل نکرده بود! همچنین فایل‌های پروژه داروسازی (<code className="font-mono-code">ttac-4.3.6.apk</code> و <code className="font-mono-code">pharmacy-inventory.html</code>) طبق دستور شما کاملاً شناسایی و قرنطینه شدند.
            </p>
          </div>
          <div className="grid grid-cols-2 gap-3 min-w-[240px]">
            <div className="rounded-xl bg-white/10 p-3.5 backdrop-blur-sm border border-white/10 text-center">
              <div className="text-2xl font-extrabold text-emerald-300 font-mono-code">2 + 5</div>
              <div className="text-xs text-slate-300 mt-1">شاخه اصلی + آرشیو مکمل</div>
            </div>
            <div className="rounded-xl bg-white/10 p-3.5 backdrop-blur-sm border border-white/10 text-center">
              <div className="text-2xl font-extrabold text-amber-300 font-mono-code">848 / 848</div>
              <div className="text-xs text-slate-300 mt-1">صفحه کتاب زیست OCRشده</div>
            </div>
            <div className="rounded-xl bg-white/10 p-3.5 backdrop-blur-sm border border-white/10 text-center">
              <div className="text-2xl font-extrabold text-purple-200 font-mono-code">27 Tags</div>
              <div className="text-xs text-slate-300 mt-1">گرامر رسمی DSL میمو ۹٫۳۵</div>
            </div>
            <div className="rounded-xl bg-rose-500/20 p-3.5 backdrop-blur-sm border border-rose-400/30 text-center">
              <div className="text-2xl font-extrabold text-rose-300 font-mono-code">قرنطینه</div>
              <div className="text-xs text-rose-200 mt-1">حذف کامل فایل‌های داروسازی</div>
            </div>
          </div>
        </div>
      </div>

      {/* Section 1: Detailed Audit of All Branches and Zip Archives */}
      <section className="space-y-4">
        <div className="flex items-center justify-between flex-wrap gap-2">
          <div>
            <h3 className="text-lg font-bold text-[#252746] flex items-center gap-2">
              <GitBranch className="h-5 w-5 text-[#7E4BDE]" />
              ۱. نقشه کالبدشکافی شاخه‌ها و آرشیوهای داخل ریپوی <code className="font-mono-code text-sm bg-purple-100 text-[#7E4BDE] px-2 py-0.5 rounded">danmillman008-hub/game</code>
            </h3>
            <p className="text-xs text-slate-600 mt-1">
              مشخصات دقیق هر بخش، کارهای انجام‌شده، بخش‌های نیمه‌کاره و نقش دقیق هر کدام در نقشه جامع ۱۲ فازی:
            </p>
          </div>
        </div>

        <div className="grid grid-cols-1 gap-4">
          {branchesAndArchives.map((item) => {
            const isExcluded = item.status === "حذف‌شده طبق دستور شما (Ignored)";
            const isCore = item.status === "منبع حقیقت هسته (Core Truth)";

            return (
              <div
                key={item.id}
                className={`rounded-2xl border p-5 transition-all ${
                  isExcluded
                    ? "border-rose-200 bg-rose-50/60"
                    : isCore
                      ? "border-[#7E4BDE]/35 bg-white shadow-sm"
                      : "border-slate-200 bg-white shadow-xs"
                }`}
              >
                <div className="flex flex-wrap items-start justify-between gap-3 border-b border-slate-100 pb-3.5">
                  <div className="flex items-start gap-3">
                    <div
                      className={`mt-0.5 rounded-xl p-2.5 ${
                        isExcluded
                          ? "bg-rose-100 text-rose-700"
                          : isCore
                            ? "bg-[#7E4BDE]/15 text-[#7E4BDE]"
                            : "bg-indigo-50 text-indigo-700"
                      }`}
                    >
                      {isExcluded ? (
                        <Ban className="h-5 w-5" />
                      ) : item.type.includes("شاخه") ? (
                        <GitBranch className="h-5 w-5" />
                      ) : (
                        <Archive className="h-5 w-5" />
                      )}
                    </div>
                    <div>
                      <div className="flex flex-wrap items-center gap-2">
                        <h4 className="font-bold text-base text-[#252746]">{item.name}</h4>
                        <span
                          className={`rounded-full px-2.5 py-0.5 text-xs font-semibold ${
                            isExcluded
                              ? "bg-rose-200/80 text-rose-900"
                              : isCore
                                ? "bg-[#7E4BDE] text-white"
                                : "bg-amber-100 text-amber-900"
                          }`}
                        >
                          {item.status}
                        </span>
                      </div>
                      <p className="text-xs text-slate-500 mt-1 font-mono-code">
                        Type: {item.type} · Ref: {item.commitOrHash}
                      </p>
                    </div>
                  </div>
                </div>

                <p className="mt-3.5 text-sm text-slate-700 leading-relaxed">{item.whatIsInside}</p>

                {!isExcluded && (
                  <div className="mt-4 grid grid-cols-1 lg:grid-cols-2 gap-4">
                    <div className="rounded-xl bg-emerald-50/70 border border-emerald-200/80 p-3.5">
                      <div className="text-xs font-bold text-emerald-900 flex items-center gap-1.5 mb-2">
                        <CheckCircle2 className="h-4 w-4 text-emerald-600 shrink-0" />
                        دستاوردهای آماده و تاییدشده (نباید از صفر نوشته شوند):
                      </div>
                      <ul className="space-y-1.5 text-xs text-emerald-950 leading-relaxed">
                        {item.verifiedStrengths.map((str, idx) => (
                          <li key={idx} className="flex items-start gap-1.5">
                            <span className="text-emerald-600 font-bold">•</span>
                            <span>{str}</span>
                          </li>
                        ))}
                      </ul>
                    </div>

                    <div className="rounded-xl bg-amber-50/70 border border-amber-200/80 p-3.5">
                      <div className="text-xs font-bold text-amber-900 flex items-center gap-1.5 mb-2">
                        <AlertTriangle className="h-4 w-4 text-amber-600 shrink-0" />
                        نقاط ناقص / نیمه‌کاره که باعث توقف پروژه شده بودند:
                      </div>
                      <ul className="space-y-1.5 text-xs text-amber-950 leading-relaxed">
                        {item.brokenOrIncompleteParts.map((brk, idx) => (
                          <li key={idx} className="flex items-start gap-1.5">
                            <span className="text-amber-600 font-bold">•</span>
                            <span>{brk}</span>
                          </li>
                        ))}
                      </ul>
                    </div>
                  </div>
                )}

                <div
                  className={`mt-3.5 rounded-xl px-4 py-2.5 text-xs font-medium flex items-center gap-2 ${
                    isExcluded
                      ? "bg-rose-100/80 text-rose-900"
                      : "bg-[#F6F7FB] text-[#252746] border border-slate-200/80"
                  }`}
                >
                  <Wrench className="h-4 w-4 text-[#7E4BDE] shrink-0" />
                  <span>
                    <strong>حکم معماری در نقشه گنج:</strong> {item.exactRoleInFinalPlan}
                  </span>
                </div>
              </div>
            );
          })}
        </div>
      </section>

      {/* Section 2: The 6 Root Causes of the "Frankenstein" State */}
      <section className="space-y-4">
        <div>
          <h3 className="text-lg font-bold text-[#252746] flex items-center gap-2">
            <AlertTriangle className="h-5 w-5 text-amber-600" />
            ۲. کالبدشکافی ۶ مشکل ریشه‌ای که باعث شدند پروتوتایپ قبلی «فرانکنشتاینی و ناقص» شود
          </h3>
          <p className="text-xs text-slate-600 mt-1">
            هر یک از این ۶ باگ معماری در کدهای فعلی ریپو ردیابی شده و راه‌حل قطعی آن در فازهای اجرایی تعبیه شده است:
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          {rootCauses.map((rc) => (
            <div
              key={rc.id}
              className="rounded-2xl border border-slate-200 bg-white p-5 shadow-xs flex flex-col justify-between"
            >
              <div className="space-y-3">
                <div className="flex items-start justify-between gap-2">
                  <h4 className="font-bold text-sm text-[#252746] leading-snug">{rc.title}</h4>
                  <button
                    type="button"
                    onClick={() => onJumpToPhase(rc.targetPhaseCode.split(" ")[0])}
                    className="shrink-0 rounded-lg bg-[#7E4BDE]/10 hover:bg-[#7E4BDE]/20 text-[#7E4BDE] px-2.5 py-1 text-xs font-bold font-mono-code transition"
                  >
                    {rc.targetPhaseCode}
                  </button>
                </div>

                <div className="rounded-xl bg-rose-50/70 border border-rose-200/70 p-3 text-xs text-rose-950 leading-relaxed">
                  <strong className="block text-rose-800 mb-0.5">علامت ظاهری که شما دیدید:</strong>
                  {rc.symptomSeenByUser}
                </div>

                <div className="rounded-xl bg-slate-50 border border-slate-200/80 p-3 text-xs text-slate-700 leading-relaxed">
                  <strong className="block text-slate-900 mb-0.5">ریشه فنی دقیق در کد ریپو:</strong>
                  {rc.technicalRootCause}
                  <div className="mt-1.5 text-[11px] font-mono-code text-slate-500 flex items-center gap-1">
                    <FileCode2 className="h-3.5 w-3.5 text-[#7E4BDE]" />
                    {rc.evidenceLocationInRepo}
                  </div>
                </div>
              </div>

              <div className="mt-3 rounded-xl bg-emerald-50/80 border border-emerald-200 p-3 text-xs text-emerald-950 leading-relaxed">
                <strong className="block text-emerald-800 mb-0.5">راه‌حل مهندسی در پلن ما:</strong>
                {rc.engineeringFixInPlan}
              </div>
            </div>
          ))}
        </div>
      </section>

      {/* Section 3: Dead Ends & Anti-Drift Guardrails from 03_ERRORS_AND_DEAD_ENDS.md */}
      <section className="space-y-4">
        <div className="flex flex-wrap items-center justify-between gap-3">
          <div>
            <h3 className="text-lg font-bold text-[#252746] flex items-center gap-2">
              <ShieldAlert className="h-5 w-5 text-rose-600" />
              ۳. بانک بن‌بست‌ها و خطاهای ممنوعه (<code className="font-mono-code text-sm bg-rose-100 text-rose-800 px-2 py-0.5 rounded">03_ERRORS_AND_DEAD_ENDS.md</code>)
            </h3>
            <p className="text-xs text-slate-600 mt-1">
              این قوانین مستقیماً در پرامپت ایجنت تزریق شده‌اند تا هیچ ایجنتی دوباره وقت و توکن شما را روی مسیرهای شکست‌خورده هدر ندهد:
            </p>
          </div>

          <div className="flex flex-wrap gap-1.5">
            {categories.map((cat) => (
              <button
                key={cat}
                type="button"
                onClick={() => setSelectedCategory(cat)}
                className={`rounded-lg px-3 py-1.5 text-xs font-semibold transition ${
                  selectedCategory === cat
                    ? "bg-[#252746] text-white"
                    : "bg-white text-slate-700 border border-slate-200 hover:bg-slate-50"
                }`}
              >
                {cat === "ALL" ? "همه دسته‌ها" : cat}
              </button>
            ))}
          </div>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-3.5">
          {filteredDeadEnds.map((de) => (
            <div
              key={de.id}
              className="rounded-xl border border-slate-200 bg-white p-4 shadow-xs space-y-2"
            >
              <div className="flex items-center justify-between gap-2">
                <span className="rounded-md bg-rose-100 text-rose-800 px-2 py-0.5 text-[11px] font-bold">
                  {de.category}
                </span>
                <span className="text-xs font-mono-code text-slate-400">{de.id}</span>
              </div>
              <div className="text-xs font-bold text-slate-900 flex items-start gap-1.5">
                <XCircle className="h-4 w-4 text-rose-600 shrink-0 mt-0.5" />
                <span>خطای قبلی: {de.whatFailedBefore}</span>
              </div>
              <p className="text-xs text-slate-600 leading-relaxed">
                <strong>چرا شکست خورد:</strong> {de.whyItFailed}
              </p>
              <div className="rounded-lg bg-[#252746] text-purple-100 p-2.5 text-xs leading-relaxed">
                <strong className="text-amber-300">فرمان بازدارنده برای ایجنت: </strong>
                {de.strictRuleForAgent}
              </div>
            </div>
          ))}
        </div>
      </section>
    </div>
  );
}
