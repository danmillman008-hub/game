"use client";

import React, { useState } from "react";
import {
  Copy,
  Check,
  Download,
  Terminal,
  Sparkles,
  History,
  CheckCircle2,
  FileText,
} from "lucide-react";
import type { BlueprintPhaseRow, AgentExecutionLogRow } from "@/db/schema";

interface MasterPromptAndExportCenterProps {
  masterPrompt: string;
  phases: BlueprintPhaseRow[];
  logs: AgentExecutionLogRow[];
}

export function MasterPromptAndExportCenter({
  masterPrompt,
  phases,
  logs,
}: MasterPromptAndExportCenterProps) {
  const [copiedFull, setCopiedFull] = useState(false);
  const [agentFormat, setAgentFormat] = useState<
    "CLAUDE_MD" | "AGENTS_MD" | "CURSOR_RULES"
  >("CLAUDE_MD");

  const compiledFullDocument = `${masterPrompt}

================================================================================
# فهرست تفصیلی ۱۲ فاز اجرایی وزن‌دار (مجموع وزن = ۱۰۰٪)
================================================================================

${phases
  .map(
    (p) => `## ${p.title} (${p.code} · وزن: ${p.weightPct}٪)
- **وضعیت فعلی در نقشه:** ${p.status}
- **منابع مرجع در ریپو:** ${p.sourceBranchRefs.join(" | ")}
- **پیش‌نیازها:** ${p.prerequisites.join(", ")}
- **هدف مهندسی:** ${p.objective}
- **معماری و نحوه اجرا:**
${p.architecturalDeepDive}
- **فایل‌های هدف:** ${p.targetFiles.join(", ")}
- **قوانین ضد-انحراف (Anti-Drift):**
${p.antiDriftRules.map((r) => `  * ${r}`).join("\n")}
- **پرامپت اجرایی فاز ${p.phaseNumber}:**
${p.agentPrompt}
- **دستورات دروازه تایید (Verification Gate):**
\`\`\`bash
${p.verificationCommands.join("\n")}
\`\`\`
`,
  )
  .join("\n--------------------------------------------------------------------------------\n")}`;

  const handleCopyFullDocument = async () => {
    await navigator.clipboard.writeText(compiledFullDocument);
    setCopiedFull(true);
    setTimeout(() => setCopiedFull(false), 3000);
  };

  return (
    <div className="space-y-6">
      {/* Header Banner */}
      <div className="rounded-2xl border border-[#7E4BDE]/30 bg-white p-6 shadow-xs space-y-4">
        <div className="flex flex-wrap items-start justify-between gap-4">
          <div className="space-y-1.5 max-w-3xl">
            <h2 className="text-lg font-extrabold text-[#252746] flex items-center gap-2">
              <Sparkles className="h-5 w-5 text-[#7E4BDE]" />
              پرامپت مرجع سرتاسری برای تحویل مستقیم به ایجنت هوش مصنوعی (Zero-Touch Handoff)
            </h2>
            <p className="text-xs text-slate-600 leading-relaxed">
              این متن دقیقاً همان چیزی است که بدون نیاز به هیچ توضیحی از طرف شما، کل ریپوی{" "}
              <code className="font-mono-code bg-purple-50 text-[#7E4BDE] px-1.5 py-0.5 rounded">
                danmillman008-hub/game
              </code>{" "}
              را به ایجنت معرفی می‌کند، فایل‌های داروسازی را کنار می‌گذارد و ۱۲ فاز را مرحله به مرحله با تست خودکار پیش می‌برد.
            </p>
          </div>

          <div className="flex flex-wrap gap-2.5">
            <button
              type="button"
              onClick={handleCopyFullDocument}
              className="inline-flex items-center gap-2 rounded-xl bg-[#7E4BDE] hover:bg-[#6939c6] text-white px-4 py-2.5 text-xs font-extrabold shadow-sm transition cursor-pointer"
            >
              {copiedFull ? (
                <>
                  <Check className="h-4 w-4 text-emerald-300" />
                  کل نقشه گنج + ۱۲ فاز کپی شد!
                </>
              ) : (
                <>
                  <Copy className="h-4 w-4" />
                  کپی یکجای کل پرامپت مادر + تمام ۱۲ فاز
                </>
              )}
            </button>

            <a
              href="/MASTER_AGENT_PLAYBOOK.md"
              download="MASTER_AGENT_PLAYBOOK.md"
              className="inline-flex items-center gap-2 rounded-xl bg-[#252746] hover:bg-slate-800 text-white px-4 py-2.5 text-xs font-bold shadow-sm transition"
            >
              <Download className="h-4 w-4" />
              دانلود فایل MASTER_AGENT_PLAYBOOK.md
            </a>
          </div>
        </div>

        {/* Agent Format Selector */}
        <div className="flex flex-wrap items-center gap-2 pt-2 border-t border-slate-100">
          <span className="text-xs font-bold text-slate-700">
            قالب پیشنهادی قرار دادن در ریشه ریپو:
          </span>
          {[
            { id: "CLAUDE_MD", label: "CLAUDE.md (مخصوص Claude Code)" },
            { id: "AGENTS_MD", label: "AGENTS.md (مخصوص OpenAI Codex / Devin)" },
            { id: "CURSOR_RULES", label: ".cursorrules (مخصوص Cursor / Windsurf)" },
          ].map((fmt) => (
            <button
              key={fmt.id}
              type="button"
              onClick={() =>
                setAgentFormat(
                  fmt.id as "CLAUDE_MD" | "AGENTS_MD" | "CURSOR_RULES",
                )
              }
              className={`rounded-lg px-3 py-1.5 text-xs font-bold transition cursor-pointer ${
                agentFormat === fmt.id
                  ? "bg-[#252746] text-white"
                  : "bg-slate-100 text-slate-700 hover:bg-slate-200"
              }`}
            >
              {fmt.label}
            </button>
          ))}
        </div>

        {/* Full Prompt Viewer */}
        <div className="rounded-xl bg-[#1E2038] text-slate-100 p-4 space-y-2">
          <div className="flex items-center justify-between text-xs text-purple-200 border-b border-white/10 pb-2">
            <span className="font-mono-code font-bold flex items-center gap-1.5">
              <FileText className="h-4 w-4 text-amber-300" />
              {agentFormat === "CLAUDE_MD"
                ? "CLAUDE.md"
                : agentFormat === "AGENTS_MD"
                  ? "AGENTS.md"
                  : ".cursorrules"}{" "}
              (Master Autonomous Playbook)
            </span>
            <span className="text-[11px] font-mono-code text-emerald-300">
              12 Weighted Phases · 100% Self-Verifying
            </span>
          </div>
          <pre className="text-xs leading-relaxed whitespace-pre-wrap max-h-[520px] overflow-y-auto p-2 text-slate-100">
            {compiledFullDocument}
          </pre>
        </div>
      </div>

      {/* Database Execution Audit Trail */}
      <div className="rounded-2xl border border-slate-200 bg-white p-6 shadow-xs space-y-4">
        <div className="flex items-center justify-between">
          <h3 className="text-base font-bold text-[#252746] flex items-center gap-2">
            <History className="h-5 w-5 text-[#7E4BDE]" />
            لاگ تراکنش‌های مهندسی و تغییرات نقشه راه در PostgreSQL
          </h3>
          <span className="text-xs font-mono-code text-slate-500">
            {logs.length} رویداد ثبت‌شده
          </span>
        </div>

        <div className="space-y-2">
          {logs.map((log) => (
            <div
              key={log.id}
              className="rounded-xl border border-slate-200 bg-[#F6F7FB] p-3.5 flex flex-wrap items-center justify-between gap-3 text-xs"
            >
              <div className="flex items-start gap-2.5">
                <CheckCircle2 className="h-4 w-4 text-emerald-600 shrink-0 mt-0.5" />
                <div>
                  <div className="font-bold text-[#252746]">{log.summary}</div>
                  <div className="text-[11px] font-mono-code text-slate-500 mt-0.5">
                    Phase: {log.phaseCode} · Action: {log.actionType} · Stack: {log.targetStack}
                  </div>
                </div>
              </div>
              <span className="rounded-md bg-emerald-100 text-emerald-800 px-2.5 py-0.5 text-[11px] font-mono-code font-bold">
                <Terminal className="inline h-3 w-3 mr-1" />
                VERIFIED
              </span>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
