import { initialSkillState, updateSkillState, type SkillState } from "@/core/algorithms/bkt";
import {
  createCard,
  dueCards,
  ratingForOutcome,
  scheduleCard,
  type FsrsCard,
  type Rating,
} from "@/core/algorithms/fsrs";
import type { ExamResult, ExamSession } from "@/core/exam/exam";
import type { Verdict } from "@/core/text/grade";
import type { Curriculum, Lesson, MCQ } from "@/core/types";

export type ThemeMode = "day" | "night";

export interface LearnerProfile {
  name: string;
  grade: string;
  major: string;
  examDate: string; // ISO date
  dailyGoalMin: number;
  theme: ThemeMode;
}

export interface Wallet {
  coins: number;
  xp: number;
  keys: number;
}

export interface Streak {
  count: number;
  lastActiveDay: string | null;
  freezes: number;
}

export interface LessonProgress {
  tries: number;
  completions: number;
  lastAttemptAt: number | null;
  stars: number;
  bestAccuracy: number;
}

export interface AttemptRecord {
  id: string;
  at: number;
  lessonId: string;
  blockId?: string;
  questionId?: string;
  skillId: string;
  correct: boolean;
  aided: boolean;
  verdict?: Verdict;
  seconds: number;
  context: "lesson" | "review" | "exam";
}

export interface LearnerState {
  version: 2;
  profile: LearnerProfile;
  wallet: Wallet;
  streak: Streak;
  skills: Record<string, SkillState>;
  lessons: Record<string, LessonProgress>;
  reviewCards: FsrsCard[];
  attempts: AttemptRecord[];
  examResults: ExamResult[];
  lastLessonId: string | null;
}

const MAX_ATTEMPTS = 800;

export function todayKey(now = Date.now()): string {
  return new Date(now).toISOString().slice(0, 10);
}

export function createInitialLearnerState(now = Date.now()): LearnerState {
  const examDate = new Date(now);
  examDate.setMonth(examDate.getMonth() + 5);
  return {
    version: 2,
    profile: {
      name: "دانش‌آموز",
      grade: "دوازدهم",
      major: "تجربی",
      examDate: examDate.toISOString().slice(0, 10),
      dailyGoalMin: 45,
      theme: "day",
    },
    wallet: { coins: 120, xp: 0, keys: 3 },
    streak: { count: 0, lastActiveDay: null, freezes: 0 },
    skills: {},
    lessons: {},
    reviewCards: [],
    attempts: [],
    examResults: [],
    lastLessonId: null,
  };
}

function bumpStreak(streak: Streak, now: number): Streak {
  const today = todayKey(now);
  if (streak.lastActiveDay === today) return streak;
  const yesterday = todayKey(now - 24 * 60 * 60 * 1000);
  const count = streak.lastActiveDay === yesterday ? streak.count + 1 : 1;
  return { ...streak, count, lastActiveDay: today };
}

export interface RecordAttemptInput {
  lessonId: string;
  skillId: string;
  correct: boolean;
  aided: boolean;
  verdict?: Verdict;
  seconds?: number;
  context?: AttemptRecord["context"];
  questionId?: string;
  blockId?: string;
  difficulty?: 1 | 2 | 3;
  /** For review cards */
  promptFa?: string;
  answerFa?: string;
  now?: number;
}

export function recordAttempt(state: LearnerState, input: RecordAttemptInput): LearnerState {
  const now = input.now ?? Date.now();
  const aided = input.aided;
  const skill = updateSkillState(state.skills[input.skillId], input.correct, now, {
    aided,
    difficulty: input.difficulty,
  });

  const attempt: AttemptRecord = {
    id: `a-${now}-${Math.floor(Math.random() * 1e6)}`,
    at: now,
    lessonId: input.lessonId,
    blockId: input.blockId,
    questionId: input.questionId,
    skillId: input.skillId,
    correct: input.correct,
    aided,
    verdict: input.verdict,
    seconds: input.seconds ?? 0,
    context: input.context ?? "lesson",
  };

  const gainedXp = input.correct ? (aided ? 4 : 9) : 1;
  const gainedCoins = input.correct ? (aided ? 1 : 3) : 0;

  const progress = state.lessons[input.lessonId] ?? {
    tries: 0,
    completions: 0,
    lastAttemptAt: null,
    stars: 0,
    bestAccuracy: 0,
  };

  let reviewCards = state.reviewCards;
  const outcomeRating: Rating = ratingForOutcome({
    correct: input.correct,
    aided,
    secondsSpent: input.seconds,
  });

  if (!input.correct || aided) {
    const cardKey = `${input.skillId}::${input.questionId ?? input.blockId ?? "core"}`;
    const existing = reviewCards.find((c) => c.id === cardKey);
    if (existing) {
      reviewCards = reviewCards.map((c) =>
        c.id === cardKey ? scheduleCard(c, outcomeRating, now) : c,
      );
    } else if (input.promptFa && input.answerFa) {
      const card = createCard({
        id: cardKey,
        lessonId: input.lessonId,
        skillId: input.skillId,
        questionId: input.questionId,
        promptFa: input.promptFa,
        answerFa: input.answerFa,
        now,
      });
      reviewCards = [...reviewCards, scheduleCard(card, outcomeRating, now)];
    }
  }

  return {
    ...state,
    skills: { ...state.skills, [input.skillId]: skill },
    lessons: {
      ...state.lessons,
      [input.lessonId]: { ...progress, tries: progress.tries + 1, lastAttemptAt: now },
    },
    wallet: {
      ...state.wallet,
      xp: state.wallet.xp + gainedXp,
      coins: state.wallet.coins + gainedCoins,
    },
    streak: bumpStreak(state.streak, now),
    reviewCards,
    attempts: [attempt, ...state.attempts].slice(0, MAX_ATTEMPTS),
    lastLessonId: input.lessonId,
  };
}

export function completeLesson(
  state: LearnerState,
  lessonId: string,
  accuracy: number,
  now = Date.now(),
): LearnerState {
  const progress = state.lessons[lessonId] ?? {
    tries: 0,
    completions: 0,
    lastAttemptAt: null,
    stars: 0,
    bestAccuracy: 0,
  };
  const stars = accuracy >= 0.95 ? 3 : accuracy >= 0.8 ? 2 : accuracy >= 0.6 ? 1 : 0;
  const firstCompletion = progress.completions === 0;

  return {
    ...state,
    lessons: {
      ...state.lessons,
      [lessonId]: {
        ...progress,
        completions: progress.completions + 1,
        lastAttemptAt: now,
        stars: Math.max(progress.stars, stars),
        bestAccuracy: Math.max(progress.bestAccuracy, accuracy),
      },
    },
    wallet: {
      ...state.wallet,
      xp: state.wallet.xp + (firstCompletion ? 40 : 12),
      coins: state.wallet.coins + (firstCompletion ? 30 : 6),
    },
    streak: bumpStreak(state.streak, now),
    lastLessonId: lessonId,
  };
}

export function reviewCard(
  state: LearnerState,
  cardId: string,
  rating: Rating,
  now = Date.now(),
): LearnerState {
  const card = state.reviewCards.find((c) => c.id === cardId);
  if (!card) return state;
  const scheduled = scheduleCard(card, rating, now);
  const correct = rating >= 3;
  return {
    ...state,
    skills: {
      ...state.skills,
      [card.skillId]: updateSkillState(state.skills[card.skillId], correct, now, { aided: false }),
    },
    reviewCards: state.reviewCards.map((c) => (c.id === cardId ? scheduled : c)),
    wallet: {
      ...state.wallet,
      xp: state.wallet.xp + (correct ? 6 : 1),
      coins: state.wallet.coins + (correct ? 2 : 0),
    },
    streak: bumpStreak(state.streak, now),
    attempts: [
      {
        id: `a-${now}-${Math.floor(Math.random() * 1e6)}`,
        at: now,
        lessonId: card.lessonId,
        questionId: card.questionId,
        skillId: card.skillId,
        correct,
        aided: false,
        seconds: 0,
        context: "review" as const,
      },
      ...state.attempts,
    ].slice(0, MAX_ATTEMPTS),
  };
}

export function finishExam(
  state: LearnerState,
  session: ExamSession,
  result: ExamResult,
  bank: MCQ[],
  now = Date.now(),
): LearnerState {
  const byId = new Map(bank.map((q) => [q.id, q]));
  let next: LearnerState = {
    ...state,
    examResults: [result, ...state.examResults].slice(0, 40),
    wallet: {
      ...state.wallet,
      xp: state.wallet.xp + result.correct * 6,
      coins: state.wallet.coins + result.correct * 2,
    },
    streak: bumpStreak(state.streak, now),
    attempts: state.attempts,
  };

  next = {
    ...next,
    attempts: [
      ...session.items.map((item, index) => {
        const question = byId.get(item.questionId);
        const chosen = session.answers[item.questionId] ?? null;
        const correct = chosen !== null && Boolean(question?.options[chosen]?.correct);
        return {
          id: `exam-${result.id}-${index}`,
          at: now,
          lessonId: item.lessonId,
          questionId: item.questionId,
          skillId: item.skillId,
          correct,
          aided: false,
          seconds: 0,
          context: "exam" as const,
        };
      }),
      ...next.attempts,
    ].slice(0, MAX_ATTEMPTS),
  };

  // BKT update for every answered item + FSRS cards for mistakes.
  for (const item of session.items) {
    const question = byId.get(item.questionId);
    if (!question) continue;
    const chosen = session.answers[item.questionId] ?? null;
    if (chosen === null) continue;
    const correct = Boolean(question.options[chosen]?.correct);
    next = {
      ...next,
      skills: {
        ...next.skills,
        [item.skillId]: updateSkillState(next.skills[item.skillId], correct, now, {
          aided: false,
          difficulty: question.difficulty,
        }),
      },
    };
    if (!correct) {
      const cardKey = `${item.skillId}::${item.questionId}`;
      if (!next.reviewCards.some((c) => c.id === cardKey)) {
        const card = createCard({
          id: cardKey,
          lessonId: item.lessonId,
          skillId: item.skillId,
          questionId: item.questionId,
          promptFa: question.stemFa,
          answerFa: question.options.find((o) => o.correct)?.textFa ?? "",
          now,
        });
        next = {
          ...next,
          reviewCards: [...next.reviewCards, scheduleCard(card, 1, now)],
        };
      }
    }
  }

  return next;
}

export function setProfile(state: LearnerState, patch: Partial<LearnerProfile>): LearnerState {
  return { ...state, profile: { ...state.profile, ...patch } };
}

export function setTheme(state: LearnerState, theme: ThemeMode): LearnerState {
  return { ...state, profile: { ...state.profile, theme } };
}

export function resetLearner(profile?: Partial<LearnerProfile>): LearnerState {
  const fresh = createInitialLearnerState();
  return { ...fresh, profile: { ...fresh.profile, ...profile } };
}

/* ------------------------------------------------------------------ */
/* Derived selectors                                                   */
/* ------------------------------------------------------------------ */

export function masteryMap(state: LearnerState): Record<string, number> {
  const map: Record<string, number> = {};
  for (const [skillId, skill] of Object.entries(state.skills)) map[skillId] = skill.pKnown;
  return map;
}

export type LessonLock = "locked" | "available" | "in_progress" | "mastered";

export function lessonLock(state: LearnerState, lesson: Lesson): LessonLock {
  const progress = state.lessons[lesson.id];
  if (progress?.completions) {
    const concept = state.skills[`${lesson.id}.concept`]?.pKnown ?? 0;
    const application = state.skills[`${lesson.id}.application`]?.pKnown ?? 0;
    return concept >= 0.75 && application >= 0.75 ? "mastered" : "in_progress";
  }
  if (progress?.tries) return "in_progress";
  // ADD-04: local chapter completion unlocks the next lesson once tries >= 1.
  const dependency = lesson.skills[0]?.dependsOn?.[0];
  if (!dependency) return "available";
  const dependencyLessonId = dependency.replace(/\.concept$/, "");
  const dependencyProgress = state.lessons[dependencyLessonId];
  if (dependencyProgress && (dependencyProgress.tries > 0 || dependencyProgress.completions > 0)) return "available";
  return "locked";
}

export function unlockedLessonIds(state: LearnerState, lessons: Lesson[]): Set<string> {
  return new Set(lessons.filter((l) => lessonLock(state, l) !== "locked").map((l) => l.id));
}

export function dueReviewCards(state: LearnerState, now = Date.now()): FsrsCard[] {
  return dueCards(state.reviewCards, now);
}

export function recentAccuracy(state: LearnerState, window = 8): boolean[] {
  return state.attempts.slice(0, window).map((a) => a.correct);
}

export function accuracyOf(attempts: AttemptRecord[]): number {
  if (attempts.length === 0) return 0;
  return attempts.filter((a) => a.correct).length / attempts.length;
}

export function unaidedAccuracy(attempts: AttemptRecord[]): number {
  const unaided = attempts.filter((a) => !a.aided);
  return accuracyOf(unaided);
}

export interface LearnerSummary {
  totalAttempts: number;
  correct: number;
  accuracy: number;
  unaidedAccuracy: number;
  aidedShare: number;
  masteredSkills: number;
  totalSkills: number;
  completedLessons: number;
  totalLessons: number;
  streak: number;
  xp: number;
  coins: number;
  dueReviews: number;
  minutesPracticed: number;
}

export function summarize(state: LearnerState, curriculum: Curriculum, now = Date.now()): LearnerSummary {
  const totalSkills = curriculum.lessons.reduce((sum, l) => sum + l.skills.length, 0);
  const masteredSkills = Object.values(state.skills).filter((s) => s.pKnown >= 0.75).length;
  const correct = state.attempts.filter((a) => a.correct).length;
  const aided = state.attempts.filter((a) => a.aided).length;

  return {
    totalAttempts: state.attempts.length,
    correct,
    accuracy: accuracyOf(state.attempts),
    unaidedAccuracy: unaidedAccuracy(state.attempts),
    aidedShare: state.attempts.length ? aided / state.attempts.length : 0,
    masteredSkills,
    totalSkills,
    completedLessons: Object.values(state.lessons).filter((l) => l.completions > 0).length,
    totalLessons: curriculum.lessons.length,
    streak: state.streak.count,
    xp: state.wallet.xp,
    coins: state.wallet.coins,
    dueReviews: dueReviewCards(state, now).length,
    minutesPracticed: Math.round(
      state.attempts.reduce((sum, a) => sum + Math.max(a.seconds, 6), 0) / 60,
    ),
  };
}
