/**
 * FSRS-5 spaced-repetition scheduler (default 19-parameter weights).
 * Used for the «صف مرور» queue: every wrong or scaffolded answer becomes a card.
 */

export const FSRS_WEIGHTS = [
  0.40255, 1.18385, 3.173, 15.69105, 7.1949, 0.5345, 1.4604, 0.0046, 1.54575, 0.1192, 1.01925, 1.9395, 0.11, 0.29605,
  2.2698, 0.2315, 2.9898, 0.51655, 0.6621,
] as const;

export const FSRS_DECAY = -0.5;
export const FSRS_FACTOR = 19 / 81;
export const DEFAULT_RETENTION = 0.9;
export const DAY_MS = 24 * 60 * 60 * 1000;

export type Rating = 1 | 2 | 3 | 4; // Again | Hard | Good | Easy
export type CardState = "new" | "learning" | "review" | "relearning";

export interface FsrsCard {
  id: string;
  lessonId: string;
  skillId: string;
  questionId?: string;
  promptFa: string;
  answerFa: string;
  stability: number;
  difficulty: number;
  due: number;
  lastReview: number | null;
  reps: number;
  lapses: number;
  state: CardState;
  scheduledDays: number;
}

const clamp = (value: number, min: number, max: number) => Math.min(max, Math.max(min, value));

function initDifficulty(rating: Rating, w = FSRS_WEIGHTS): number {
  return clamp(w[4] - Math.exp(w[5] * (rating - 1)) + 1, 1, 10);
}

function initStability(rating: Rating, w = FSRS_WEIGHTS): number {
  return Math.max(0.1, w[rating - 1]);
}

function nextDifficulty(difficulty: number, rating: Rating, w = FSRS_WEIGHTS): number {
  const next = w[7] * initDifficulty(4, w) + (1 - w[7]) * (difficulty - w[6] * (rating - 3));
  return clamp(next, 1, 10);
}

export function retrievability(card: Pick<FsrsCard, "stability" | "lastReview">, now = Date.now()): number {
  if (card.lastReview === null) return 0;
  const elapsedDays = Math.max(0, (now - card.lastReview) / DAY_MS);
  return Math.pow(1 + (FSRS_FACTOR * elapsedDays) / Math.max(0.1, card.stability), FSRS_DECAY);
}

function nextRecallStability(
  difficulty: number,
  stability: number,
  recall: number,
  rating: Rating,
  w = FSRS_WEIGHTS,
): number {
  const hardPenalty = rating === 2 ? w[15] : 1;
  const easyBonus = rating === 4 ? w[16] : 1;
  return (
    stability *
    (1 +
      Math.exp(w[8]) *
        (11 - difficulty) *
        Math.pow(stability, -w[9]) *
        (Math.exp(w[10] * (1 - recall)) - 1) *
        hardPenalty *
        easyBonus)
  );
}

function nextForgetStability(difficulty: number, stability: number, recall: number, w = FSRS_WEIGHTS): number {
  return (
    w[11] *
    Math.pow(difficulty, -w[12]) *
    (Math.pow(stability + 1, w[13]) - 1) *
    Math.exp(w[14] * (1 - recall))
  );
}

export function intervalDays(stability: number, retention = DEFAULT_RETENTION): number {
  const days = (stability / FSRS_FACTOR) * (Math.pow(retention, 1 / FSRS_DECAY) - 1);
  return clamp(Math.round(days), 1, 365);
}

export function createCard(input: {
  id: string;
  lessonId: string;
  skillId: string;
  questionId?: string;
  promptFa: string;
  answerFa: string;
  now?: number;
}): FsrsCard {
  const now = input.now ?? Date.now();
  return {
    id: input.id,
    lessonId: input.lessonId,
    skillId: input.skillId,
    questionId: input.questionId,
    promptFa: input.promptFa,
    answerFa: input.answerFa,
    stability: 0,
    difficulty: 0,
    due: now,
    lastReview: null,
    reps: 0,
    lapses: 0,
    state: "new",
    scheduledDays: 0,
  };
}

export function scheduleCard(card: FsrsCard, rating: Rating, now = Date.now()): FsrsCard {
  const isNew = card.state === "new" || card.lastReview === null;
  let stability: number;
  let difficulty: number;
  let state: CardState;
  let lapses = card.lapses;

  if (isNew) {
    stability = initStability(rating);
    difficulty = initDifficulty(rating);
    state = rating === 1 ? "learning" : "review";
  } else {
    const recall = retrievability(card, now);
    difficulty = nextDifficulty(card.difficulty, rating);
    if (rating === 1) {
      stability = nextForgetStability(card.difficulty, card.stability, recall);
      state = "relearning";
      lapses += 1;
    } else {
      stability = nextRecallStability(card.difficulty, card.stability, recall, rating);
      state = "review";
    }
  }

  const days = rating === 1 ? 1 : intervalDays(stability);
  return {
    ...card,
    stability,
    difficulty,
    due: now + days * DAY_MS,
    lastReview: now,
    reps: card.reps + 1,
    lapses,
    state,
    scheduledDays: days,
  };
}

/** Map a graded answer to an FSRS rating. */
export function ratingForOutcome(outcome: {
  correct: boolean;
  aided: boolean;
  secondsSpent?: number;
}): Rating {
  if (!outcome.correct) return 1;
  if (outcome.aided) return 2;
  if (outcome.secondsSpent !== undefined && outcome.secondsSpent < 12) return 4;
  return 3;
}

export interface ReviewForecastBucket {
  dayOffset: number;
  label: string;
  count: number;
}

export function forecast(cards: FsrsCard[], now = Date.now(), horizonDays = 7): ReviewForecastBucket[] {
  const buckets: ReviewForecastBucket[] = Array.from({ length: horizonDays }, (_, i) => ({
    dayOffset: i,
    label: i === 0 ? "امروز" : i === 1 ? "فردا" : `${i} روز بعد`,
    count: 0,
  }));

  for (const card of cards) {
    const offset = Math.floor(Math.max(0, card.due - now) / DAY_MS);
    if (offset < horizonDays) buckets[offset].count += 1;
  }
  return buckets;
}

export function dueCards(cards: FsrsCard[], now = Date.now()): FsrsCard[] {
  return cards.filter((c) => c.due <= now).sort((a, b) => a.due - b.due);
}
