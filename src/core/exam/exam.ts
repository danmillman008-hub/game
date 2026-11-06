import type { MCQ, SubjectId } from "@/core/types";

export type ExamModeId = "diagnostic" | "chapter" | "targeted" | "timed" | "mistakes" | "bank" | "mock";

export interface ExamMode {
  id: ExamModeId;
  titleFa: string;
  subtitleFa: string;
  descriptionFa: string;
  minutes: number;
  count: number;
  negativeMarking: boolean;
}

/** The seven-part Konkur hub (F39–F43). */
export const EXAM_MODES: ExamMode[] = [
  {
    id: "diagnostic",
    titleFa: "آزمون تشخیصی",
    subtitleFa: "کالیبراسیون BKT · ۱۰ سؤال",
    descriptionFa: "قبل از شروع، سطح هر مهارت را می‌سنجیم تا مسیر و باند جریان کالیبره شود.",
    minutes: 15,
    count: 10,
    negativeMarking: false,
  },
  {
    id: "chapter",
    titleFa: "آزمون فصل",
    subtitleFa: "فقط سؤالات فصل انتخابی",
    descriptionFa: "پس از هر فصل، سنجش تمرکز‌یافته روی همان مهارت‌ها.",
    minutes: 25,
    count: 10,
    negativeMarking: true,
  },
  {
    id: "targeted",
    titleFa: "تمرین هدفمند",
    subtitleFa: "حاشیهٔ بیرونی دانش",
    descriptionFa: "موتور KST ضعیف‌ترین مهارت‌های آزادشده را هدف می‌گیرد.",
    minutes: 20,
    count: 8,
    negativeMarking: true,
  },
  {
    id: "timed",
    titleFa: "آزمون زمان‌دار",
    subtitleFa: "فشار زمانی واقعی",
    descriptionFa: "با تایمر معکوس و نمرهٔ منفی یک‌سوم، شبیه‌سازی جلسهٔ آزمون.",
    minutes: 12,
    count: 8,
    negativeMarking: true,
  },
  {
    id: "mistakes",
    titleFa: "آزمون اشتباهات",
    subtitleFa: "از صف مرور FSRS",
    descriptionFa: "همان سؤالاتی که در صف مرور غلط‌ها ثبت شده‌اند.",
    minutes: 15,
    count: 10,
    negativeMarking: true,
  },
  {
    id: "bank",
    titleFa: "بانک تست",
    subtitleFa: "همهٔ سؤالات کتاب",
    descriptionFa: "حالت مطالعه: بدون تایمر و بدون نمرهٔ منفی، فقط حل و تحلیل.",
    minutes: 0,
    count: 15,
    negativeMarking: false,
  },
  {
    id: "mock",
    titleFa: "شبیه‌ساز کنکور",
    subtitleFa: "۲۷۰ دقیقه · نمرهٔ منفی",
    descriptionFa: "آزمون جامع از همهٔ دروس موجود با زمان استاندارد کنکور و پاسخبرگ مستقل.",
    minutes: 270,
    count: 30,
    negativeMarking: true,
  },
];

export interface ExamItem {
  questionId: string;
  lessonId: string;
  subjectId: SubjectId;
  skillId: string;
}

export interface ExamSession {
  id: string;
  mode: ExamModeId;
  titleFa: string;
  startedAt: number;
  minutes: number;
  negativeMarking: boolean;
  items: ExamItem[];
  answers: Record<string, number | null>;
  flagged: string[];
  finishedAt: number | null;
}

export interface ExamItemResult {
  questionId: string;
  lessonId: string;
  subjectId: SubjectId;
  skillId: string;
  chosenIndex: number | null;
  correct: boolean;
  blank: boolean;
}

export interface ExamResult {
  id: string;
  mode: ExamModeId;
  titleFa: string;
  startedAt: number;
  finishedAt: number;
  minutesSpent: number;
  total: number;
  correct: number;
  wrong: number;
  blank: number;
  score: number;
  maxScore: number;
  percent: number;
  negativeMarking: boolean;
  affectedSkills: string[];
  perSubject: Partial<Record<SubjectId, { correct: number; wrong: number; blank: number; total: number }>>;
}

function hashSeed(input: string): number {
  let seed = 2166136261;
  for (const ch of input) {
    seed ^= ch.charCodeAt(0);
    seed = Math.imul(seed, 16777619);
  }
  return seed >>> 0;
}

function mulberry32(seed: number) {
  let a = seed;
  return () => {
    a = (a + 0x6d2b79f5) >>> 0;
    let t = a;
    t = Math.imul(t ^ (t >>> 15), t | 1);
    t ^= t + Math.imul(t ^ (t >>> 7), t | 61);
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}

export function shuffleDeterministic<T>(items: T[], seedText: string): T[] {
  const rand = mulberry32(hashSeed(seedText));
  const arr = [...items];
  for (let i = arr.length - 1; i > 0; i--) {
    const j = Math.floor(rand() * (i + 1));
    [arr[i], arr[j]] = [arr[j], arr[i]];
  }
  return arr;
}

export interface BuildExamOptions {
  mode: ExamModeId;
  titleFa?: string;
  subjectId?: SubjectId;
  chapterId?: string;
  lessonIds?: string[];
  weakSkillIds?: string[];
  mistakeQuestionIds?: string[];
  count?: number;
  minutes?: number;
  now?: number;
  seed?: string;
}

export function buildExam(bank: MCQ[], options: BuildExamOptions): ExamSession {
  const mode = EXAM_MODES.find((m) => m.id === options.mode) ?? EXAM_MODES[0];
  const now = options.now ?? Date.now();
  const seed = options.seed ?? `${options.mode}-${now}`;

  let pool = bank;
  if (options.subjectId) pool = pool.filter((q) => q.subjectId === options.subjectId);
  if (options.chapterId) pool = pool.filter((q) => q.chapterId === options.chapterId);
  if (options.lessonIds?.length) pool = pool.filter((q) => options.lessonIds?.includes(q.lessonId));
  if (options.mode === "targeted" && options.weakSkillIds?.length) {
    const weak = new Set(options.weakSkillIds);
    const targeted = pool.filter((q) => weak.has(q.skillId));
    pool = targeted.length >= 3 ? targeted : pool;
  }
  if (options.mode === "mistakes") {
    const mistakes = new Set(options.mistakeQuestionIds ?? []);
    const targeted = pool.filter((q) => mistakes.has(q.id));
    pool = targeted.length > 0 ? targeted : pool;
  }

  const count = Math.max(1, Math.min(options.count ?? mode.count, pool.length));
  const picked = shuffleDeterministic(pool, seed).slice(0, count);

  return {
    id: `exam-${now}-${Math.floor(Math.random() * 1e6)}`,
    mode: options.mode,
    titleFa: options.titleFa ?? mode.titleFa,
    startedAt: now,
    minutes: options.minutes ?? mode.minutes,
    negativeMarking: mode.negativeMarking,
    items: picked.map((q) => ({
      questionId: q.id,
      lessonId: q.lessonId,
      subjectId: q.subjectId,
      skillId: q.skillId,
    })),
    answers: Object.fromEntries(picked.map((q) => [q.id, null])),
    flagged: [],
    finishedAt: null,
  };
}

export const CORRECT_POINTS = 3;
export const WRONG_PENALTY = 1; // one third of 3 points

export function scoreExam(session: ExamSession, bank: MCQ[], now = Date.now()): ExamResult {
  const byId = new Map(bank.map((q) => [q.id, q]));
  let correct = 0;
  let wrong = 0;
  let blank = 0;
  const perSubject: ExamResult["perSubject"] = {};
  const affected = new Set<string>();

  for (const item of session.items) {
    const question = byId.get(item.questionId);
    if (!question) continue;
    const chosen = session.answers[item.questionId];
    const bucket = (perSubject[item.subjectId] ??= { correct: 0, wrong: 0, blank: 0, total: 0 });
    bucket.total += 1;

    if (chosen === null || chosen === undefined) {
      blank += 1;
      bucket.blank += 1;
      continue;
    }
    const option = question.options[chosen];
    if (option?.correct) {
      correct += 1;
      bucket.correct += 1;
    } else {
      wrong += 1;
      bucket.wrong += 1;
      affected.add(item.skillId);
    }
  }

  const maxScore = session.items.length * CORRECT_POINTS;
  const rawScore = correct * CORRECT_POINTS - (session.negativeMarking ? wrong * WRONG_PENALTY : 0);
  const score = session.negativeMarking ? Math.max(0, rawScore) : correct * CORRECT_POINTS;

  return {
    id: `result-${session.id}`,
    mode: session.mode,
    titleFa: session.titleFa,
    startedAt: session.startedAt,
    finishedAt: now,
    minutesSpent: Math.round((now - session.startedAt) / 60000),
    total: session.items.length,
    correct,
    wrong,
    blank,
    score,
    maxScore,
    percent: maxScore === 0 ? 0 : Math.round((score / maxScore) * 100),
    negativeMarking: session.negativeMarking,
    affectedSkills: [...affected],
    perSubject,
  };
}

export function formatClock(seconds: number): string {
  const clamped = Math.max(0, Math.floor(seconds));
  const h = Math.floor(clamped / 3600);
  const m = Math.floor((clamped % 3600) / 60);
  const s = clamped % 60;
  const pad = (n: number) => String(n).padStart(2, "0");
  return h > 0 ? `${pad(h)}:${pad(m)}:${pad(s)}` : `${pad(m)}:${pad(s)}`;
}
