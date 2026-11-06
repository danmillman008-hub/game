/**
 * Shared domain types for the Konkur-Mimo × LearnHarness platform.
 * Layer 1 is framework-free: these types are consumed by the pure engine,
 * the server routes and the React client alike.
 */

export type SubjectId = "bio12" | "chem12" | "phys12";

export type Role = "hook" | "check" | "feedback" | "explain" | "practice" | "recap";

export type Mechanic =
  | "concept_bite"
  | "guided_cloze"
  | "token_assembly"
  | "trap_detector"
  | "konkur_test"
  | "summary_recap";

export type RendererKind = "reveal" | "cloze" | "assembly" | "trap" | "mcq" | "validated_input";

export type Difficulty = 1 | 2 | 3;

export interface Skill {
  id: string;
  lessonId: string;
  labelFa: string;
  kind: "concept" | "application";
  dependsOn: string[];
}

export interface Token {
  id: string;
  text: string;
  kind: "anchor" | "link" | "modifier" | "trap";
  trapHintFa?: string;
}

export interface ClozeSpec {
  sentenceFa: string;
  answer: string;
  distractors: string[];
  hintFa: string;
  quantifiers?: string[];
}

export interface TrapOption {
  id: string;
  textFa: string;
  isTrap: boolean;
  analysisFa: string;
}

export interface MCQOption {
  id: string;
  textFa: string;
  correct: boolean;
  analysisFa: string;
}

export interface MCQ {
  id: string;
  lessonId: string;
  chapterId: string;
  subjectId: SubjectId;
  skillId: string;
  stemFa: string;
  options: MCQOption[];
  difficulty: Difficulty;
  hintFa: string;
  sourceRef: string;
  quantifierFa?: string;
}

export interface LessonBlock {
  id: string;
  lessonId: string;
  role: Role;
  mechanic: Mechanic;
  renderer: RendererKind;
  titleFa: string;
  promptFa: string;
  bodyFa: string[];
  hintFa?: string;
  cloze?: ClozeSpec;
  tokens?: Token[];
  assembly?: {
    instructionFa: string;
    solution: string[]; // token ids in correct order
    answerFa: string;
  };
  trapOptions?: TrapOption[];
  mcq?: MCQ;
  expectedAnswer?: string;
  feedback: { correctFa: string; wrongFa: string; partialFa?: string };
  sourceRef: string;
  skillId: string;
  dsl: string;
}

export interface GuardrailCheck {
  code: string;
  titleFa: string;
  passed: boolean;
  detailFa: string;
}

export interface Lesson {
  id: string;
  curriculumId: number;
  subjectId: SubjectId;
  chapterId: string;
  order: number;
  titleFa: string;
  subtitleFa: string;
  sourceRef: string;
  minutes: number;
  axiomFa: string;
  hookFa: string;
  trapFa: string;
  recapFa: string[];
  propositions: { id: string; textFa: string; quantifierFa?: string }[];
  blocks: LessonBlock[];
  skills: Skill[];
  questions: MCQ[];
  dslHtml: string;
  guardrails: GuardrailCheck[];
  reviewStatus: "approved" | "unreviewed";
}

export interface Chapter {
  id: string;
  subjectId: SubjectId;
  order: number;
  titleFa: string;
  subtitleFa: string;
  lessonIds: string[];
}

export interface Subject {
  id: SubjectId;
  titleFa: string;
  shortFa: string;
  grade: string;
  accent: string;
  chapterIds: string[];
}

export interface Curriculum {
  subjects: Subject[];
  chapters: Chapter[];
  lessons: Lesson[];
  questions: MCQ[];
  lessonById: Map<string, Lesson>;
  chapterById: Map<string, Chapter>;
  subjectById: Map<string, Subject>;
  skillById: Map<string, Skill>;
}
