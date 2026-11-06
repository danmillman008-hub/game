import fs from "node:fs";
import path from "node:path";
import type {
  AgentExecutionLogRow,
  BlueprintPhaseRow,
  CompiledMicroLessonRow,
} from "@/db/schema";
import { SEED_EXECUTION_PHASES } from "@/lib/phases-playbook-data";
import {
  INITIAL_COMPILED_LESSONS_SEED,
  compileTextbookExcerptToMimoQuest,
  type CompiledLessonInput,
} from "@/lib/konkur-compiler";

/**
 * The blueprint console runs on a durable JSON store so the roadmap stays usable
 * with zero external services. The Drizzle/PostgreSQL schema in `db/schema.ts`
 * remains the production target (Layer 3 of the architecture).
 */

const DATA_DIR = path.join(process.cwd(), ".data");
const FILE = path.join(DATA_DIR, "blueprint.json");

export interface BlueprintStore {
  phases: BlueprintPhaseRow[];
  lessons: CompiledMicroLessonRow[];
  logs: AgentExecutionLogRow[];
}

function readStore(): BlueprintStore | null {
  try {
    const raw = fs.readFileSync(FILE, "utf8");
    const parsed = JSON.parse(raw) as BlueprintStore;
    if (!Array.isArray(parsed.phases) || !Array.isArray(parsed.lessons)) return null;
    return parsed;
  } catch {
    return null;
  }
}

function writeStore(store: BlueprintStore): void {
  try {
    fs.mkdirSync(DATA_DIR, { recursive: true });
    fs.writeFileSync(FILE, JSON.stringify(store, null, 2), "utf8");
  } catch (error) {
    console.error("Failed to persist blueprint store:", error);
  }
}

function seedStore(): BlueprintStore {
  const now = new Date();
  const phases = SEED_EXECUTION_PHASES.map((phase, index) => ({
    id: index + 1,
    phaseNumber: phase.phaseNumber,
    code: phase.code,
    title: phase.title,
    subtitle: phase.subtitle,
    weightPct: phase.weightPct,
    status: phase.status,
    category: phase.category,
    estimatedTurns: phase.estimatedTurns,
    sourceBranchRefs: phase.sourceBranchRefs,
    prerequisites: phase.prerequisites,
    objective: phase.objective,
    architecturalDeepDive: phase.architecturalDeepDive,
    deliverables: phase.deliverables,
    targetFiles: phase.targetFiles,
    antiDriftRules: phase.antiDriftRules,
    verificationCommands: phase.verificationCommands,
    agentPrompt: phase.agentPrompt,
    notes: "",
    updatedAt: now,
  })) as BlueprintPhaseRow[];

  const lessons = INITIAL_COMPILED_LESSONS_SEED.map((item, index) => {
    const compiled = compileTextbookExcerptToMimoQuest(item);
    return {
      id: index + 1,
      chapterCode: item.chapterCode,
      curriculumId: item.curriculumId,
      subject: item.subject,
      grade: item.grade,
      topicTitle: item.topicTitle,
      sourceRef: item.sourceRef,
      rawOcrExcerpt: item.rawOcrExcerpt,
      sanitizedText: compiled.sanitizedText,
      ocrFixesApplied: compiled.ocrFixesApplied,
      unconditionalTruthAxiom: compiled.unconditionalTruthAxiom,
      motivatedDiscoveryHook: compiled.motivatedDiscoveryHook,
      designerTrap: compiled.designerTrap,
      targetQuantifier: compiled.targetQuantifier,
      dslBlocks: compiled.dslBlocks,
      guardrailScore: compiled.guardrailScore,
      guardrailChecks: compiled.guardrailChecks,
      reviewStatus: compiled.guardrailScore === 100 ? "approved" : "unreviewed",
      publishSetVersion: 753,
      createdAt: now,
    } as CompiledMicroLessonRow;
  });

  const logs: AgentExecutionLogRow[] = [
    {
      id: 1,
      phaseCode: "PHASE_00",
      actionType: "FORENSIC_AUDIT",
      targetStack: "Monorepo (aebb90b7 + ecb8af07)",
      summary:
        "کالبدشکافی شاخه‌ها و آرشیوها انجام شد؛ فایل‌های نامرتبط داروسازی و بازی سگا قرنطینه شدند.",
      verificationPassed: true,
      createdAt: new Date(now.getTime() - 5 * 60_000),
    } as AgentExecutionLogRow,
    {
      id: 2,
      phaseCode: "PHASE_01",
      actionType: "RE_CLOSURE",
      targetStack: "Mimo 9.35 Core Engine",
      summary:
        "نرمال‌ساز qm.i.a همراه با لایهٔ یکسان‌ساز یونیکد فارسی (Q-44) پیاده‌سازی و با بردارهای تست پوشش داده شد.",
      verificationPassed: true,
      createdAt: new Date(now.getTime() - 4 * 60_000),
    } as AgentExecutionLogRow,
    {
      id: 3,
      phaseCode: "PHASE_04",
      actionType: "PEDAGOGICAL_COMPILE",
      targetStack: "Konkur × Mimo six-role compiler",
      summary:
        "۱۸ ریزدرس با شش نقش hook → check → feedback → explain → practice → recap و ۱۰ گاردریل M1–M10 کامپایل شد.",
      verificationPassed: true,
      createdAt: new Date(now.getTime() - 3 * 60_000),
    } as AgentExecutionLogRow,
    {
      id: 4,
      phaseCode: "PHASE_06",
      actionType: "ADAPTIVE_ENGINE",
      targetStack: "KST + Calibrated BKT + FSRS-5 + Flow 70–85%",
      summary:
        "گراف دانش، تسلط تفکیک‌شدهٔ unaided/aided، زمان‌بندی مرور فاصله‌دار و کنترلر باند جریان فعال شد.",
      verificationPassed: true,
      createdAt: new Date(now.getTime() - 2 * 60_000),
    } as AgentExecutionLogRow,
    {
      id: 5,
      phaseCode: "PHASE_07",
      actionType: "SHELL_FIDELITY",
      targetStack: "v12.5-fa shell (۵ تب، ۳ چیپ، گره‌های مسیر)",
      summary:
        "پوستهٔ فارسی با پنج تب، سه چیپ بالای صفحه، نقشهٔ مسیر گره‌ای و پخش‌کنندهٔ درس شش‌نقشی پیاده‌سازی شد.",
      verificationPassed: true,
      createdAt: new Date(now.getTime() - 1 * 60_000),
    } as AgentExecutionLogRow,
  ];

  return { phases, lessons, logs };
}

export function getBlueprintStore(): BlueprintStore {
  const existing = readStore();
  if (existing) return existing;
  const seeded = seedStore();
  writeStore(seeded);
  return seeded;
}

export function getBlueprintState(): BlueprintStore {
  const store = getBlueprintStore();
  return {
    phases: [...store.phases].sort((a, b) => a.phaseNumber - b.phaseNumber),
    lessons: [...store.lessons].sort((a, b) => b.id - a.id),
    logs: [...store.logs].sort((a, b) => b.id - a.id).slice(0, 20),
  };
}

export function updatePhase(input: {
  phaseNumber: number;
  status?: string;
  toggleDeliverableId?: string;
  notes?: string;
}): { ok: boolean; error?: string } {
  const store = getBlueprintStore();
  const phase = store.phases.find((item) => item.phaseNumber === input.phaseNumber);
  if (!phase) return { ok: false, error: "فاز مورد نظر یافت نشد" };

  let deliverables = [...phase.deliverables];
  let nextStatus = input.status ?? phase.status;

  if (input.toggleDeliverableId) {
    deliverables = deliverables.map((item) =>
      item.id === input.toggleDeliverableId ? { ...item, done: !item.done } : item,
    );
    if (deliverables.every((item) => item.done) && nextStatus !== "verified") nextStatus = "completed";
    else if (deliverables.some((item) => item.done) && nextStatus === "pending") nextStatus = "in_progress";
  }

  const nextLog: AgentExecutionLogRow = {
    id: Math.max(0, ...store.logs.map((log) => log.id)) + 1,
    phaseCode: phase.code,
    actionType: input.toggleDeliverableId ? "DELIVERABLE_TOGGLE" : "STATUS_UPDATE",
    targetStack: phase.category,
    summary: input.toggleDeliverableId
      ? `وضعیت تسک ${input.toggleDeliverableId} در «${phase.title}» به‌روزرسانی شد (وضعیت فاز: ${nextStatus}).`
      : `وضعیت «${phase.title}» به «${nextStatus}» تغییر یافت.`,
    verificationPassed: nextStatus === "verified" || nextStatus === "completed",
    createdAt: new Date(),
  } as AgentExecutionLogRow;

  writeStore({
    ...store,
    phases: store.phases.map((item) =>
      item.phaseNumber === input.phaseNumber
        ? {
            ...item,
            status: nextStatus,
            deliverables,
            notes: typeof input.notes === "string" ? input.notes : item.notes,
            updatedAt: new Date(),
          }
        : item,
    ),
    logs: [nextLog, ...store.logs].slice(0, 60),
  });

  return { ok: true };
}

export function addCompiledLesson(input: CompiledLessonInput & {
  subject: string;
  grade: string;
  topicTitle: string;
  sourceRef: string;
  rawOcrExcerpt: string;
}): void {
  const store = getBlueprintStore();
  const compiled = compileTextbookExcerptToMimoQuest(input);
  const lesson: CompiledMicroLessonRow = {
    id: Math.max(0, ...store.lessons.map((item) => item.id)) + 1,
    chapterCode: input.chapterCode,
    curriculumId: input.curriculumId,
    subject: input.subject,
    grade: input.grade,
    topicTitle: input.topicTitle,
    sourceRef: input.sourceRef,
    rawOcrExcerpt: input.rawOcrExcerpt,
    sanitizedText: compiled.sanitizedText,
    ocrFixesApplied: compiled.ocrFixesApplied,
    unconditionalTruthAxiom: compiled.unconditionalTruthAxiom,
    motivatedDiscoveryHook: compiled.motivatedDiscoveryHook,
    designerTrap: compiled.designerTrap,
    targetQuantifier: compiled.targetQuantifier,
    dslBlocks: compiled.dslBlocks,
    guardrailScore: compiled.guardrailScore,
    guardrailChecks: compiled.guardrailChecks,
    reviewStatus: compiled.guardrailScore === 100 ? "approved" : "unreviewed",
    publishSetVersion: 753,
    createdAt: new Date(),
  } as CompiledMicroLessonRow;

  const log: AgentExecutionLogRow = {
    id: Math.max(0, ...store.logs.map((item) => item.id)) + 1,
    phaseCode: "PHASE_05",
    actionType: "TEXTBOOK_DSL_COMPILE",
    targetStack: "6-Stage OCR → Mimo 27-Tag DSL + LearnHarness",
    summary: `مبحث «${input.topicTitle}» (${input.chapterCode}) با امتیاز گاردریل ${compiled.guardrailScore}٪ به شش ریزدرس میمو کامپایل شد.`,
    verificationPassed: compiled.guardrailScore >= 85,
    createdAt: new Date(),
  } as AgentExecutionLogRow;

  writeStore({
    ...store,
    lessons: [lesson, ...store.lessons],
    logs: [log, ...store.logs].slice(0, 60),
  });
}
