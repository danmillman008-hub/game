"use client";

import React, { useState } from "react";
import {
  CheckCircle2,
  Clock,
  Copy,
  Check,
  Terminal,
  ShieldAlert,
  FileCode,
  Sparkles,
  PlayCircle,
  Award,
  Layers,
  Save,
} from "lucide-react";
import type { BlueprintPhaseRow } from "@/db/schema";

interface PhasesExecutionWorkbenchProps {
  phases: BlueprintPhaseRow[];
  selectedPhaseNumber: number;
  onSelectPhaseNumber: (num: number) => void;
  onUpdatePhase: (payload: {
    phaseNumber: number;
    status?: string;
    toggleDeliverableId?: string;
    notes?: string;
  }) => Promise<void>;
  updating: boolean;
}

export function PhasesExecutionWorkbench({
  phases,
  selectedPhaseNumber,
  onSelectPhaseNumber,
  onUpdatePhase,
  updating,
}: PhasesExecutionWorkbenchProps) {
  const [copiedPhaseCode, setCopiedPhaseCode] = useState<string | null>(null);
  const [noteDraft, setNoteDraft] = useState<Record<number, string>>({});

  const activePhase =
    phases.find((p) => p.phaseNumber === selectedPhaseNumber) ?? phases[0];

  const totalWeight = phases.reduce((acc, p) => acc + p.weightPct, 0);
  const completedWeight = phases.reduce((acc, p) => {
    if (p.status === "verified" || p.status === "completed") {
      return acc + p.weightPct;
    }
    if (p.status === "in_progress") {
      const totalDeliv = p.deliverables.length || 1;
      const doneDeliv = p.deliverables.filter((d) => d.done).length;
      return acc + Math.round((p.weightPct * doneDeliv) / totalDeliv);
    }
    return acc;
  }, 0);

  const handleCopyPrompt = async (phase: BlueprintPhaseRow) => {
    const fullPhasePrompt = `# دستور اجرایی خودران — ${phase.title} (وزن از کل پروژه: ${phase.weightPct}٪)
# کد فاز: ${phase.code} | پیش‌نیازها: ${phase.prerequisites.join(", ")}
# منابع مرجع در ریپو: ${phase.sourceBranchRefs.join(" · ")}

## ۱. هدف مهندسی این فاز
${phase.objective}

## ۲. معماری و جزئیات پیاده‌سازی
${phase.architecturalDeepDive}

## ۳. تسک‌های تحویلی الزامی (Deliverables)
${phase.deliverables.map((d, i) => `${i + 1}. [${d.id}] ${d.title} (مرجع: ${d.specRef})`).join("\n")}

## ۴. فایل‌های هدف برای ایجاد یا ویرایش
${phase.targetFiles.map((f) => `- ${f}`).join("\n")}

## ۵. قوانین ضد-انحراف (Anti-Drift Guardrails — هرگز نقض نکن!)
${phase.antiDriftRules.map((r) => `• ${r}`).join("\n")}

## ۶. دستورالعمل گام‌به‌گام برای تو (ایجنت کدنویس)
${phase.agentPrompt}

## ۷. دروازه تایید الزامی پایان فاز (Verification Gate)
قبل از اعلام اتمام این فاز، باید تمام دستورات زیر را اجرا کنی و خروجی ۱۰۰٪ سبز بگیری:
\`\`\`bash
${phase.verificationCommands.join("\n")}
\`\`\``;

    await navigator.clipboard.writeText(fullPhasePrompt);
    setCopiedPhaseCode(phase.code);
    setTimeout(() => setCopiedPhaseCode(null), 2500);
  };

  if (!activePhase) return null;

  const currentNotes =
    noteDraft[activePhase.phaseNumber] !== undefined
      ? noteDraft[activePhase.phaseNumber]
      : activePhase.notes || "";

  const statusBadge = (status: string) => {
    switch (status) {
      case "verified":
        return (
          <span className="inline-flex items-center gap-1 rounded-full bg-emerald-100 text-emerald-800 px-2.5 py-0.5 text-xs font-bold">
            <Award className="h-3.5 w-3.5 text-emerald-600" />
            تاییدشده (Verified)
          </span>
        );
      case "completed":
        return (
          <span className="inline-flex items-center gap-1 rounded-full bg-teal-100 text-teal-800 px-2.5 py-0.5 text-xs font-bold">
            <CheckCircle2 className="h-3.5 w-3.5 text-teal-600" />
            تکمیل‌شده (Completed)
          </span>
        );
      case "in_progress":
        return (
          <span className="inline-flex items-center gap-1 rounded-full bg-amber-100 text-amber-800 px-2.5 py-0.5 text-xs font-bold">
            <PlayCircle className="h-3.5 w-3.5 text-amber-600" />
            در حال اجرا (In Progress)
          </span>
        );
      default:
        return (
          <span className="inline-flex items-center gap-1 rounded-full bg-slate-100 text-slate-700 px-2.5 py-0.5 text-xs font-semibold">
            <Clock className="h-3.5 w-3.5 text-slate-500" />
            در نوبت ایجنت (Pending)
          </span>
        );
    }
  };

  return (
    <div className="space-y-6">
      {/* Top Weighted Progress Overview */}
      <div className="rounded-2xl border border-slate-200 bg-white p-5 shadow-xs">
        <div className="flex flex-wrap items-center justify-between gap-4 mb-3">
          <div>
            <h2 className="text-lg font-bold text-[#252746] flex items-center gap-2">
              <Layers className="h-5 w-5 text-[#7E4BDE]" />
              نقشه اجرایی ۱۲ فازی وزن‌دار ایجنت هوش مصنوعی (مجموع وزن = {totalWeight}٪)
            </h2>
            <p className="text-xs text-slate-600 mt-0.5">
              هر فاز دارای وزن مهندسی دقیق، پیش‌نیاز، فایل‌های هدف، قوانین ضد-انحراف و پرامپت مستقل قابل کپی برای ایجنت است.
            </p>
          </div>
          <div className="flex items-center gap-3">
            <div className="text-left">
              <div className="text-xs text-slate-500">پیشرفت وزنی کل نقشه گنج</div>
              <div className="text-xl font-extrabold text-[#7E4BDE] font-mono-code">
                {completedWeight}% / {totalWeight}%
              </div>
            </div>
          </div>
        </div>

        {/* Segmented Weight Bar */}
        <div className="h-3 w-full rounded-full bg-slate-100 overflow-hidden flex gap-0.5 p-0.5 border border-slate-200">
          {phases.map((p) => {
            const isSelected = p.phaseNumber === activePhase.phaseNumber;
            const bgClass =
              p.status === "verified" || p.status === "completed"
                ? "bg-emerald-500"
                : p.status === "in_progress"
                  ? "bg-[#7E4BDE]"
                  : "bg-slate-300";
            return (
              <button
                key={p.code}
                type="button"
                onClick={() => onSelectPhaseNumber(p.phaseNumber)}
                style={{ width: `${p.weightPct}%` }}
                title={`${p.title} (${p.weightPct}%)`}
                className={`h-full transition-all rounded-xs ${bgClass} ${
                  isSelected ? "ring-2 ring-amber-400 opacity-100" : "opacity-80 hover:opacity-100"
                }`}
              />
            );
          })}
        </div>

        {/* Quick Phase Pills */}
        <div className="mt-4 flex flex-wrap gap-1.5">
          {phases.map((p) => {
            const isSelected = p.phaseNumber === activePhase.phaseNumber;
            return (
              <button
                key={p.code}
                type="button"
                onClick={() => onSelectPhaseNumber(p.phaseNumber)}
                className={`rounded-xl px-3 py-1.5 text-xs font-bold transition flex items-center gap-1.5 border ${
                  isSelected
                    ? "bg-[#252746] text-white border-[#252746] shadow-xs"
                    : p.status === "verified" || p.status === "completed"
                      ? "bg-emerald-50 text-emerald-900 border-emerald-200 hover:bg-emerald-100"
                      : p.status === "in_progress"
                        ? "bg-purple-50 text-[#7E4BDE] border-purple-200 hover:bg-purple-100"
                        : "bg-slate-50 text-slate-700 border-slate-200 hover:bg-slate-100"
                }`}
              >
                <span className="font-mono-code">فاز {p.phaseNumber}</span>
                <span className="opacity-75 font-mono-code">({p.weightPct}%)</span>
              </button>
            );
          })}
        </div>
      </div>

      {/* Main Split View: Left Phase List + Right Active Phase Inspector */}
      <div className="grid grid-cols-1 lg:grid-cols-12 gap-6 items-start">
        {/* Sidebar List of 12 Phases */}
        <div className="lg:col-span-4 space-y-2.5">
          {phases.map((p) => {
            const isSelected = p.phaseNumber === activePhase.phaseNumber;
            const doneCount = p.deliverables.filter((d) => d.done).length;
            const totalCount = p.deliverables.length;

            return (
              <button
                key={p.code}
                type="button"
                onClick={() => onSelectPhaseNumber(p.phaseNumber)}
                className={`w-full text-right rounded-2xl border p-4 transition-all block ${
                  isSelected
                    ? "border-[#7E4BDE] bg-white ring-2 ring-[#7E4BDE]/20 shadow-md"
                    : "border-slate-200 bg-white/90 hover:border-slate-300 hover:bg-white"
                }`}
              >
                <div className="flex items-center justify-between gap-2 mb-1.5">
                  <span className="rounded-lg bg-[#252746] text-white px-2.5 py-0.5 text-xs font-bold font-mono-code">
                    {p.code} · {p.weightPct}% وزن
                  </span>
                  {statusBadge(p.status)}
                </div>
                <h3 className="font-bold text-sm text-[#252746] leading-snug">{p.title}</h3>
                <div className="mt-2.5 flex items-center justify-between text-[11px] text-slate-500">
                  <span>{p.category}</span>
                  <span className="font-mono-code font-semibold text-[#7E4BDE]">
                    {doneCount}/{totalCount} تسک انجام‌شده
                  </span>
                </div>
              </button>
            );
          })}
        </div>

        {/* Detailed Phase Specification & Prompt Panel */}
        <div className="lg:col-span-8 space-y-5">
          <div className="rounded-2xl border border-slate-200 bg-white p-6 shadow-xs space-y-6">
            {/* Phase Header */}
            <div className="flex flex-wrap items-start justify-between gap-4 border-b border-slate-100 pb-4">
              <div className="space-y-1.5">
                <div className="flex flex-wrap items-center gap-2">
                  <span className="rounded-lg bg-[#7E4BDE] text-white px-3 py-1 text-xs font-bold font-mono-code">
                    {activePhase.code} · وزن مهندسی: {activePhase.weightPct}٪
                  </span>
                  <span className="rounded-lg bg-slate-100 text-slate-700 px-2.5 py-1 text-xs font-medium">
                    تخمین اجرا: {activePhase.estimatedTurns}
                  </span>
                  {statusBadge(activePhase.status)}
                </div>
                <h3 className="text-xl font-extrabold text-[#252746] leading-snug">
                  {activePhase.title}
                </h3>
                <p className="text-xs font-mono-code text-slate-500">{activePhase.subtitle}</p>
              </div>

              {/* Copy Phase Prompt CTA */}
              <button
                type="button"
                onClick={() => handleCopyPrompt(activePhase)}
                className="inline-flex items-center gap-2 rounded-xl bg-[#7E4BDE] hover:bg-[#6939c6] text-white px-4 py-2.5 text-xs font-bold shadow-sm transition cursor-pointer"
              >
                {copiedPhaseCode === activePhase.code ? (
                  <>
                    <Check className="h-4 w-4 text-emerald-300" />
                    پرامپت کامل فاز {activePhase.phaseNumber} کپی شد!
                  </>
                ) : (
                  <>
                    <Copy className="h-4 w-4" />
                    کپی پرامپت فاز {activePhase.phaseNumber} برای دادن به ایجنت
                  </>
                )}
              </button>
            </div>

            {/* Status Switcher Bar */}
            <div className="flex flex-wrap items-center justify-between gap-3 rounded-xl bg-[#F6F7FB] p-3.5 border border-slate-200/80">
              <span className="text-xs font-bold text-[#252746]">
                تغییر وضعیت اجرایی این فاز در دیتابیس:
              </span>
              <div className="flex flex-wrap gap-1.5">
                {[
                  { key: "pending", label: "در نوبت (Pending)" },
                  { key: "in_progress", label: "در حال اجرا (In Progress)" },
                  { key: "completed", label: "تکمیل‌شده (Completed)" },
                  { key: "verified", label: "تایید نهایی (Verified)" },
                ].map((st) => (
                  <button
                    key={st.key}
                    type="button"
                    disabled={updating}
                    onClick={() =>
                      onUpdatePhase({
                        phaseNumber: activePhase.phaseNumber,
                        status: st.key,
                      })
                    }
                    className={`rounded-lg px-3 py-1.5 text-xs font-bold transition cursor-pointer ${
                      activePhase.status === st.key
                        ? "bg-[#252746] text-white shadow-xs"
                        : "bg-white text-slate-700 border border-slate-200 hover:bg-slate-100"
                    }`}
                  >
                    {st.label}
                  </button>
                ))}
              </div>
            </div>

            {/* Source Branch & Prerequisite Badges */}
            <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
              <div className="rounded-xl bg-purple-50/60 border border-purple-200/70 p-3.5">
                <div className="text-xs font-bold text-[#252746] mb-1.5">
                  منابع حقیقت مورد استفاده از ریپوی شما:
                </div>
                <div className="flex flex-wrap gap-1.5">
                  {activePhase.sourceBranchRefs.map((ref, idx) => (
                    <span
                      key={idx}
                      className="rounded-md bg-white border border-purple-200 px-2 py-0.5 text-[11px] font-mono-code text-[#7E4BDE]"
                    >
                      {ref}
                    </span>
                  ))}
                </div>
              </div>

              <div className="rounded-xl bg-slate-50 border border-slate-200 p-3.5">
                <div className="text-xs font-bold text-[#252746] mb-1.5">
                  پیش‌نیازهای شروع این فاز:
                </div>
                <div className="flex flex-wrap gap-1.5">
                  {activePhase.prerequisites.map((pre, idx) => (
                    <span
                      key={idx}
                      className="rounded-md bg-white border border-slate-200 px-2.5 py-0.5 text-xs font-mono-code text-slate-700"
                    >
                      {pre}
                    </span>
                  ))}
                </div>
              </div>
            </div>

            {/* Objective & Deep Architectural Breakdown */}
            <div className="space-y-3">
              <div className="rounded-xl bg-indigo-50/60 border border-indigo-200/80 p-4">
                <h4 className="text-xs font-extrabold text-indigo-950 mb-1">
                  هدف مهندسی فاز {activePhase.phaseNumber}:
                </h4>
                <p className="text-sm text-indigo-950 leading-relaxed">{activePhase.objective}</p>
              </div>

              <div className="rounded-xl bg-white border border-slate-200 p-4">
                <h4 className="text-xs font-extrabold text-[#252746] mb-2 flex items-center gap-1.5">
                  <Sparkles className="h-4 w-4 text-[#7E4BDE]" />
                  تشریح عمیق معماری و نحوه پیاده‌سازی:
                </h4>
                <div className="text-xs md:text-sm text-slate-700 leading-relaxed whitespace-pre-line">
                  {activePhase.architecturalDeepDive}
                </div>
              </div>
            </div>

            {/* Interactive Deliverables Checklist */}
            <div className="space-y-2.5">
              <h4 className="text-sm font-bold text-[#252746]">
                چک‌لیست تحویلی‌های الزامی (کلیک کنید تا وضعیت در دیتابیس ذخیره شود):
              </h4>
              <div className="space-y-2">
                {activePhase.deliverables.map((deliv) => (
                  <button
                    key={deliv.id}
                    type="button"
                    disabled={updating}
                    onClick={() =>
                      onUpdatePhase({
                        phaseNumber: activePhase.phaseNumber,
                        toggleDeliverableId: deliv.id,
                      })
                    }
                    className={`w-full text-right rounded-xl border p-3.5 transition flex items-start gap-3 cursor-pointer ${
                      deliv.done
                        ? "border-emerald-200 bg-emerald-50/50 text-emerald-950"
                        : "border-slate-200 bg-white hover:bg-slate-50 text-slate-800"
                    }`}
                  >
                    <input
                      type="checkbox"
                      checked={deliv.done}
                      readOnly
                      className="mt-1 h-4 w-4 rounded accent-[#7E4BDE]"
                    />
                    <div className="flex-1">
                      <div
                        className={`text-xs md:text-sm font-semibold leading-relaxed ${
                          deliv.done ? "line-through opacity-80" : ""
                        }`}
                      >
                        {deliv.title}
                      </div>
                      <div className="mt-1 text-[11px] font-mono-code text-slate-500">
                        Code: {deliv.id} · Spec Ref: {deliv.specRef}
                      </div>
                    </div>
                  </button>
                ))}
              </div>
            </div>

            {/* Target Files & Anti-Drift Guardrails */}
            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
              <div className="rounded-xl bg-slate-50 border border-slate-200 p-4">
                <h4 className="text-xs font-bold text-[#252746] flex items-center gap-1.5 mb-2.5">
                  <FileCode className="h-4 w-4 text-[#7E4BDE]" />
                  فایل‌های هدف در ریپو (Target Files):
                </h4>
                <ul className="space-y-1.5 text-xs font-mono-code text-slate-700">
                  {activePhase.targetFiles.map((file, idx) => (
                    <li
                      key={idx}
                      className="rounded-lg bg-white border border-slate-200/80 px-2.5 py-1.5"
                    >
                      {file}
                    </li>
                  ))}
                </ul>
              </div>

              <div className="rounded-xl bg-rose-50/70 border border-rose-200 p-4">
                <h4 className="text-xs font-bold text-rose-900 flex items-center gap-1.5 mb-2.5">
                  <ShieldAlert className="h-4 w-4 text-rose-600" />
                  قوانین ضد-انحراف این فاز (Anti-Drift Rules):
                </h4>
                <ul className="space-y-2 text-xs text-rose-950 leading-relaxed">
                  {activePhase.antiDriftRules.map((rule, idx) => (
                    <li key={idx} className="flex items-start gap-1.5">
                      <span className="text-rose-600 font-bold">•</span>
                      <span>{rule}</span>
                    </li>
                  ))}
                </ul>
              </div>
            </div>

            {/* Verification Gate Commands */}
            <div className="rounded-xl bg-[#1E2038] text-slate-100 p-4 space-y-2.5">
              <div className="flex items-center justify-between">
                <h4 className="text-xs font-bold text-emerald-300 flex items-center gap-1.5">
                  <Terminal className="h-4 w-4" />
                  دروازه تایید پایان فاز (Verification Gate — شرط عبور ایجنت به فاز بعدی):
                </h4>
                <span className="text-[11px] font-mono-code text-slate-400">
                  100% Pass Required
                </span>
              </div>
              <pre className="text-xs font-mono-code bg-black/40 rounded-lg p-3 overflow-x-auto text-emerald-200 leading-relaxed dir-ltr text-left">
                {activePhase.verificationCommands.join("\n")}
              </pre>
            </div>

            {/* Ready-to-Copy Agent Prompt Box */}
            <div className="rounded-xl border-2 border-[#7E4BDE]/30 bg-purple-50/40 p-4 space-y-2.5">
              <div className="flex flex-wrap items-center justify-between gap-2">
                <h4 className="text-xs font-extrabold text-[#252746]">
                  متن پرامپت مستقیم فاز {activePhase.phaseNumber} (آماده کپی برای Claude Code / Cursor / Codex):
                </h4>
                <button
                  type="button"
                  onClick={() => handleCopyPrompt(activePhase)}
                  className="inline-flex items-center gap-1.5 rounded-lg bg-[#7E4BDE] text-white px-3 py-1 text-xs font-bold hover:bg-[#6939c6] transition cursor-pointer"
                >
                  <Copy className="h-3.5 w-3.5" />
                  کپی پرامپت کامل این فاز
                </button>
              </div>
              <pre className="text-xs bg-white border border-purple-200 rounded-lg p-3.5 whitespace-pre-wrap leading-relaxed text-slate-800">
                {activePhase.agentPrompt}
              </pre>
            </div>

            {/* Engineering Notes Input */}
            <div className="rounded-xl bg-slate-50 border border-slate-200 p-4 space-y-2">
              <label className="block text-xs font-bold text-[#252746]">
                یادداشت فنی یا گزارش اجرای ایجنت روی این فاز (ذخیره در PostgreSQL):
              </label>
              <div className="flex gap-2">
                <input
                  type="text"
                  value={currentNotes}
                  onChange={(e) =>
                    setNoteDraft((prev) => ({
                      ...prev,
                      [activePhase.phaseNumber]: e.target.value,
                    }))
                  }
                  placeholder="مثلاً: خروجی تست‌های این فاز در تاریخ امروز بررسی و تایید شد..."
                  className="flex-1 rounded-xl border border-slate-300 bg-white px-3.5 py-2 text-xs text-slate-800 focus:border-[#7E4BDE] focus:outline-none"
                />
                <button
                  type="button"
                  disabled={updating}
                  onClick={() =>
                    onUpdatePhase({
                      phaseNumber: activePhase.phaseNumber,
                      notes: currentNotes,
                    })
                  }
                  className="inline-flex items-center gap-1.5 rounded-xl bg-[#252746] hover:bg-slate-800 text-white px-4 py-2 text-xs font-bold transition cursor-pointer"
                >
                  <Save className="h-3.5 w-3.5" />
                  ذخیره یادداشت
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
