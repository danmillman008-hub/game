import {
  pgTable,
  serial,
  integer,
  text,
  boolean,
  jsonb,
  timestamp,
} from "drizzle-orm/pg-core";

export interface DeliverableTask {
  id: string;
  title: string;
  specRef: string;
  done: boolean;
}

export interface MimoDslBlockItem {
  role: "hook" | "check" | "feedback" | "explain" | "practice" | "recap";
  titleFa: string;
  interactionKind:
    | "Reveal"
    | "SingleChoice"
    | "MultipleChoice"
    | "fillTheGap"
    | "validatedInput"
    | "InteractiveWebView";
  pedagogicalMechanic:
    | "concept_bite"
    | "guided_cloze"
    | "token_assembly"
    | "trap_detector"
    | "konkur_test"
    | "summary_recap";
  dslHtml: string;
  expectedAnswer: string;
  visibleIfCorrect: string;
  visibleIfWrong: string;
  sourceRef: string;
}

export interface GuardrailCheckItem {
  code: string;
  title: string;
  passed: boolean;
  detail: string;
}

export const blueprintPhases = pgTable("blueprint_phases", {
  id: serial("id").primaryKey(),
  phaseNumber: integer("phase_number").notNull().unique(),
  code: text("code").notNull(),
  title: text("title").notNull(),
  subtitle: text("subtitle").notNull(),
  weightPct: integer("weight_pct").notNull(),
  status: text("status").notNull().default("pending"), // 'pending' | 'in_progress' | 'completed' | 'verified'
  category: text("category").notNull(),
  estimatedTurns: text("estimated_turns").notNull(),
  sourceBranchRefs: jsonb("source_branch_refs").$type<string[]>().notNull(),
  prerequisites: jsonb("prerequisites").$type<string[]>().notNull(),
  objective: text("objective").notNull(),
  architecturalDeepDive: text("architectural_deep_dive").notNull(),
  deliverables: jsonb("deliverables").$type<DeliverableTask[]>().notNull(),
  targetFiles: jsonb("target_files").$type<string[]>().notNull(),
  antiDriftRules: jsonb("anti_drift_rules").$type<string[]>().notNull(),
  verificationCommands: jsonb("verification_commands").$type<string[]>().notNull(),
  agentPrompt: text("agent_prompt").notNull(),
  notes: text("notes").notNull().default(""),
  updatedAt: timestamp("updated_at").defaultNow().notNull(),
});

export const compiledMicroLessons = pgTable("compiled_micro_lessons", {
  id: serial("id").primaryKey(),
  chapterCode: text("chapter_code").notNull(),
  curriculumId: integer("curriculum_id").notNull(),
  subject: text("subject").notNull(),
  grade: text("grade").notNull(),
  topicTitle: text("topic_title").notNull(),
  sourceRef: text("source_ref").notNull(),
  rawOcrExcerpt: text("raw_ocr_excerpt").notNull(),
  sanitizedText: text("sanitized_text").notNull(),
  ocrFixesApplied: jsonb("ocr_fixes_applied").$type<string[]>().notNull(),
  unconditionalTruthAxiom: text("unconditional_truth_axiom").notNull(),
  motivatedDiscoveryHook: text("motivated_discovery_hook").notNull(),
  designerTrap: text("designer_trap").notNull(),
  targetQuantifier: text("target_quantifier").notNull(),
  dslBlocks: jsonb("dsl_blocks").$type<MimoDslBlockItem[]>().notNull(),
  guardrailScore: integer("guardrail_score").notNull(),
  guardrailChecks: jsonb("guardrail_checks").$type<GuardrailCheckItem[]>().notNull(),
  reviewStatus: text("review_status").notNull().default("approved"), // 'unreviewed' | 'approved'
  publishSetVersion: integer("publish_set_version").notNull().default(753),
  createdAt: timestamp("created_at").defaultNow().notNull(),
});

export const agentExecutionLogs = pgTable("agent_execution_logs", {
  id: serial("id").primaryKey(),
  phaseCode: text("phase_code").notNull(),
  actionType: text("action_type").notNull(),
  targetStack: text("target_stack").notNull(),
  summary: text("summary").notNull(),
  verificationPassed: boolean("verification_passed").notNull().default(true),
  createdAt: timestamp("created_at").defaultNow().notNull(),
});

export type BlueprintPhaseRow = typeof blueprintPhases.$inferSelect;
export type CompiledMicroLessonRow = typeof compiledMicroLessons.$inferSelect;
export type AgentExecutionLogRow = typeof agentExecutionLogs.$inferSelect;
