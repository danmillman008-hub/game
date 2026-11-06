"use client";

import React, { useState, useEffect, useCallback } from "react";
import {
  Compass,
  ArrowRight,
  Layers,
  BookOpen,
  Cpu,
  Terminal,
  Copy,
  Check,
  Download,
  ShieldCheck,
  GitBranch,
  Sparkles,
} from "lucide-react";
import type {
  BlueprintPhaseRow,
  CompiledMicroLessonRow,
  AgentExecutionLogRow,
} from "@/db/schema";
import type {
  BranchOrArchiveAudit,
  FrankensteinRootCause,
  ExternalRepoRequirement,
  StackArchitectureLayer,
  DeadEndGuardrail,
} from "@/lib/repo-forensics-data";
import { ForensicAuditView } from "@/components/ForensicAuditView";
import { PhasesExecutionWorkbench } from "@/components/PhasesExecutionWorkbench";
import { TextbookPipelineAndDslStudio } from "@/components/TextbookPipelineAndDslStudio";
import { ArchitectureAndHarnessBlueprint } from "@/components/ArchitectureAndHarnessBlueprint";
import { MasterPromptAndExportCenter } from "@/components/MasterPromptAndExportCenter";

type ActiveTab =
  | "forensics"
  | "roadmap"
  | "textbook_dsl"
  | "architecture"
  | "master_prompt";

interface BlueprintStateResponse {
  phases: BlueprintPhaseRow[];
  lessons: CompiledMicroLessonRow[];
  logs: AgentExecutionLogRow[];
  masterPrompt: string;
  forensics: {
    branchesAndArchives: BranchOrArchiveAudit[];
    rootCauses: FrankensteinRootCause[];
    externalRepos: ExternalRepoRequirement[];
    stackMatrix: StackArchitectureLayer[];
    deadEnds: DeadEndGuardrail[];
  };
}

export default function MasterBlueprintCommandCenterPage() {
  const [data, setData] = useState<BlueprintStateResponse | null>(null);
  const [loading, setLoading] = useState(true);
  const [activeTab, setActiveTab] = useState<ActiveTab>("roadmap");
  const [selectedPhaseNumber, setSelectedPhaseNumber] = useState<number>(3);
  const [updatingPhase, setUpdatingPhase] = useState(false);
  const [compilingLesson, setCompilingLesson] = useState(false);
  const [copiedMasterQuick, setCopiedMasterQuick] = useState(false);

  const loadState = useCallback(async () => {
    try {
      const res = await fetch("/api/blueprint/state", { cache: "no-store" });
      if (res.ok) {
        const json: BlueprintStateResponse = await res.json();
        setData(json);
      }
    } finally {
      setLoading(false);
    }
  }, []);

  useEffect(() => {
    loadState();
  }, [loadState]);

  const handleUpdatePhase = async (payload: {
    phaseNumber: number;
    status?: string;
    toggleDeliverableId?: string;
    notes?: string;
  }) => {
    setUpdatingPhase(true);
    try {
      const res = await fetch("/api/blueprint/phase", {
        method: "PATCH",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload),
      });
      if (res.ok) {
        const fresh = await res.json();
        setData((prev) => (prev ? { ...prev, ...fresh } : prev));
      }
    } finally {
      setUpdatingPhase(false);
    }
  };

  const handleCompileNewLesson = async (payload: {
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
  }) => {
    setCompilingLesson(true);
    try {
      const res = await fetch("/api/blueprint/compile-lesson", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload),
      });
      if (res.ok) {
        const fresh = await res.json();
        setData((prev) => (prev ? { ...prev, ...fresh } : prev));
      }
    } finally {
      setCompilingLesson(false);
    }
  };

  const handleJumpToPhase = (phaseCode: string) => {
    if (!data) return;
    const match = data.phases.find((p) => phaseCode.includes(p.code));
    if (match) {
      setSelectedPhaseNumber(match.phaseNumber);
      setActiveTab("roadmap");
    }
  };

  const handleQuickCopyMaster = async () => {
    if (!data) return;
    await navigator.clipboard.writeText(data.masterPrompt);
    setCopiedMasterQuick(true);
    setTimeout(() => setCopiedMasterQuick(false), 2500);
  };

  if (loading || !data) {
    return (
      <div className="min-h-screen flex flex-col items-center justify-center bg-[#F6F7FB] p-6 text-center">
        <div className="h-12 w-12 rounded-2xl bg-[#7E4BDE] text-white flex items-center justify-center animate-pulse shadow-lg mb-4">
          <Compass className="h-6 w-6" />
        </div>
        <h1 className="text-base font-extrabold text-[#252746]">
          در حال بارگذاری نقشه گنج مهندسی کنکور-میمو × لرن‌هارنس...
        </h1>
        <p className="text-xs text-slate-500 mt-1">
          بارگذاری ۱۲ فاز اجرایی وزن‌دار از فروشگاه محلی کنسول (بدون نیاز به سرویس بیرونی)
        </p>
      </div>
    );
  }

  const totalWeight = data.phases.reduce((acc, p) => acc + p.weightPct, 0);
  const completedWeight = data.phases.reduce((acc, p) => {
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

  return (
    <div className="min-h-screen flex flex-col bg-[#F6F7FB]">
      {/* Top Principal Architect Header (#252746 Mimo Night Token) */}
      <header className="bg-[#252746] text-white border-b border-white/10 sticky top-0 z-30 shadow-md">
        <div className="mx-auto max-w-7xl px-4 sm:px-6 py-3.5">
          <div className="flex flex-wrap items-center justify-between gap-4">
            <div className="flex items-center gap-3">
              <div className="h-10 w-10 rounded-xl bg-[#7E4BDE] flex items-center justify-center shadow-inner shrink-0">
                <Compass className="h-5 w-5 text-white" />
              </div>
              <div>
                <div className="flex flex-wrap items-center gap-2">
                  <h1 className="font-extrabold text-sm md:text-base text-white">
                    نقشه گنج مهندسی کنکور-میمو × لرن‌هارنس
                  </h1>
                  <span className="rounded-md bg-[#7E4BDE]/40 border border-[#8D60E2]/60 px-2 py-0.5 text-[11px] font-mono-code text-purple-200">
                    danmillman008-hub/game.git
                  </span>
                </div>
                <p className="text-[11px] text-slate-300 mt-0.5">
                  یکپارچه‌سازی شاخه‌های <code className="font-mono-code">aebb90b7</code> +{" "}
                  <code className="font-mono-code">ecb8af07</code> · معماری Mimo 9.35 + کتاب زیست ۸۴۸ صفحه‌ای + LearnHarness
                </p>
              </div>
            </div>

            {/* Right Metrics & Quick Export Buttons */}
            <div className="flex flex-wrap items-center gap-2.5">
              <div className="rounded-xl bg-white/10 border border-white/10 px-3 py-1.5 text-xs flex items-center gap-2">
                <ShieldCheck className="h-4 w-4 text-emerald-400" />
                <span>پیشرفت نقشه راه:</span>
                <strong className="font-mono-code text-amber-300">
                  {completedWeight}% / {totalWeight}%
                </strong>
              </div>

              <button
                type="button"
                onClick={handleQuickCopyMaster}
                className="inline-flex items-center gap-1.5 rounded-xl bg-[#7E4BDE] hover:bg-[#8D60E2] text-white px-3.5 py-2 text-xs font-bold transition shadow-xs cursor-pointer"
              >
                {copiedMasterQuick ? (
                  <>
                    <Check className="h-4 w-4 text-emerald-300" />
                    پرامپت مادر کپی شد!
                  </>
                ) : (
                  <>
                    <Copy className="h-4 w-4" />
                    کپی سریع پرامپت مادر (CLAUDE.md)
                  </>
                )}
              </button>

              <a
                href="/MASTER_AGENT_PLAYBOOK.md"
                download="MASTER_AGENT_PLAYBOOK.md"
                className="inline-flex items-center gap-1.5 rounded-xl bg-white/10 hover:bg-white/20 text-white px-3 py-2 text-xs font-semibold transition border border-white/15"
              >
                <Download className="h-4 w-4 text-purple-200" />
                دانلود فایل نقشه گنج (.md)
              </a>
            </div>
          </div>

          {/* 5 Navigation Tabs */}
          <nav className="mt-3.5 flex flex-wrap gap-1.5 border-t border-white/10 pt-3">
            {[
              {
                id: "roadmap",
                label: "۱. نقشه اجرایی ۱۲ فازی وزن‌دار ایجنت (100% Weight)",
                icon: Layers,
              },
              {
                id: "forensics",
                label: "۲. کالبدشکافی ریپو و ۶ ریشه طرح فرانکنشتاینی",
                icon: GitBranch,
              },
              {
                id: "textbook_dsl",
                label: "۳. خط لوله ورود کتاب‌ها + کامپایلر DSL و پلیر ۶ نقشی",
                icon: BookOpen,
              },
              {
                id: "architecture",
                label: "۴. معماری کد (کاتلین/وب/بک‌اند) + ترکیب LearnHarness و ریپوها",
                icon: Cpu,
              },
              {
                id: "master_prompt",
                label: "۵. پرامپت جامع یک‌کلیکه (CLAUDE.md / AGENTS.md) و لاگ‌ها",
                icon: Terminal,
              },
            ].map((tab) => {
              const Icon = tab.icon;
              const isActive = activeTab === tab.id;
              return (
                <button
                  key={tab.id}
                  type="button"
                  onClick={() => setActiveTab(tab.id as ActiveTab)}
                  className={`inline-flex items-center gap-2 rounded-xl px-3.5 py-2 text-xs font-bold transition cursor-pointer ${
                    isActive
                      ? "bg-[#7E4BDE] text-white shadow-sm"
                      : "text-slate-300 hover:bg-white/10 hover:text-white"
                  }`}
                >
                  <Icon className="h-4 w-4" />
                  <span>{tab.label}</span>
                </button>
              );
            })}
          </nav>
        </div>
      </header>

      {/* Main Content Container */}
      <main className="mx-auto w-full max-w-7xl flex-1 px-4 sm:px-6 py-6">
        {activeTab === "roadmap" && (
          <PhasesExecutionWorkbench
            phases={data.phases}
            selectedPhaseNumber={selectedPhaseNumber}
            onSelectPhaseNumber={setSelectedPhaseNumber}
            onUpdatePhase={handleUpdatePhase}
            updating={updatingPhase}
          />
        )}

        {activeTab === "forensics" && (
          <ForensicAuditView
            branchesAndArchives={data.forensics.branchesAndArchives}
            rootCauses={data.forensics.rootCauses}
            deadEnds={data.forensics.deadEnds}
            onJumpToPhase={handleJumpToPhase}
          />
        )}

        {activeTab === "textbook_dsl" && (
          <TextbookPipelineAndDslStudio
            lessons={data.lessons}
            onCompileNewLesson={handleCompileNewLesson}
            compiling={compilingLesson}
          />
        )}

        {activeTab === "architecture" && (
          <ArchitectureAndHarnessBlueprint
            stackMatrix={data.forensics.stackMatrix}
            externalRepos={data.forensics.externalRepos}
          />
        )}

        {activeTab === "master_prompt" && (
          <MasterPromptAndExportCenter
            masterPrompt={data.masterPrompt}
            phases={data.phases}
            logs={data.logs}
          />
        )}
      </main>

      {/* Footer */}
      <footer className="border-t border-slate-200 bg-white py-4 px-6 text-xs text-slate-500">
        <div className="mx-auto max-w-7xl flex flex-wrap items-center justify-between gap-2">
          <div className="flex items-center gap-1.5">
            <Sparkles className="h-3.5 w-3.5 text-[#7E4BDE]" />
            <span>
              معماری مهندسی اختصاصی برای ریپوی{" "}
              <code className="font-mono-code text-[#252746]">
                danmillman008-hub/game.git
              </code>{" "}
              (پروژه داروسازی/تیتک قرنطینه و حذف شده است)
            </span>
          </div>
          <div className="font-mono-code text-[11px]">
            Mimo 9.35 v12.5-fa · HANDOFF/01..15 · LearnHarness · publishSetVersion=753
          </div>
        </div>
      </footer>
    </div>
  );
}
