import type { SubjectId } from "@/core/types";

export interface SeedQuestion {
  stemFa: string;
  options: [string, string, string, string];
  correctIndex: 0 | 1 | 2 | 3;
  analyses: [string, string, string, string];
  difficulty: 1 | 2 | 3;
  hintFa: string;
}

/**
 * A textbook-derived micro-lesson authored as structured data.
 * The compiler turns each seed into the exact six-role Mimo quest,
 * a full 27-tag DSL document and a ten-guardrail audit record.
 */
export interface LessonSeed {
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
  trap: {
    statementFa: string;
    explanationFa: string;
    decoysFa: [string, string];
  };
  propositions: { textFa: string; quantifierFa?: string }[];
  cloze: {
    sentenceFa: string;
    answer: string;
    distractors: string[];
    hintFa: string;
  };
  assembly: {
    instructionFa: string;
    solution: string[];
    traps: string[];
    answerFa: string;
  };
  questions: SeedQuestion[];
  recapFa: string[];
  dependsOnLessonIds?: string[];
}

export interface SeedChapter {
  id: string;
  subjectId: SubjectId;
  order: number;
  titleFa: string;
  subtitleFa: string;
}

export interface SeedSubject {
  id: SubjectId;
  titleFa: string;
  shortFa: string;
  grade: string;
  accent: string;
}
