/**
 * Calibrated Bayesian Knowledge Tracing.
 * The key Mimo/Konkur improvement: an answer produced with a hint (`aided`)
 * carries strictly less evidence than an `unaided` answer.
 */

export interface BktParams {
  pInit: number;
  pLearn: number;
  pSlip: number;
  pGuess: number;
  pGuessAided: number;
}

export const DEFAULT_BKT: BktParams = {
  pInit: 0.16,
  pLearn: 0.22,
  pSlip: 0.1,
  pGuess: 0.2,
  pGuessAided: 0.46,
};

export interface SkillState {
  pKnown: number;
  attempts: number;
  correct: number;
  unaidedCorrect: number;
  aidedCorrect: number;
  lastSeenAt: number | null;
  streak: number;
}

export function initialSkillState(): SkillState {
  return {
    pKnown: DEFAULT_BKT.pInit,
    attempts: 0,
    correct: 0,
    unaidedCorrect: 0,
    aidedCorrect: 0,
    lastSeenAt: null,
    streak: 0,
  };
}

export interface ObservationOptions {
  aided: boolean;
  difficulty?: 1 | 2 | 3;
  params?: Partial<BktParams>;
}

export function updateSkillState(
  previous: SkillState | undefined,
  correct: boolean,
  now: number,
  options: ObservationOptions = { aided: false },
): SkillState {
  const params: BktParams = { ...DEFAULT_BKT, ...options.params };
  const state = previous ?? initialSkillState();
  const pKnown = Math.min(0.999, Math.max(0.001, state.pKnown));

  const guess = options.aided ? params.pGuessAided : params.pGuess;
  const slip = params.pSlip;

  const posterior = correct
    ? (pKnown * (1 - slip)) / (pKnown * (1 - slip) + (1 - pKnown) * guess)
    : (pKnown * slip) / (pKnown * slip + (1 - pKnown) * (1 - guess));

  // Harder items give slightly more learning signal when solved correctly.
  // A wrong, unaided answer is treated as "not yet engaged with the correction"
  // and therefore earns only a small learning increment.
  const difficultyBoost = correct ? 1 + 0.12 * ((options.difficulty ?? 1) - 1) : 1;
  const engagement = correct ? 1 : options.aided ? 0.3 : 0.15;
  const learn = Math.min(0.6, params.pLearn * difficultyBoost * engagement);
  const nextKnown = Math.min(0.995, posterior + (1 - posterior) * learn);

  return {
    pKnown: nextKnown,
    attempts: state.attempts + 1,
    correct: state.correct + (correct ? 1 : 0),
    unaidedCorrect: state.unaidedCorrect + (correct && !options.aided ? 1 : 0),
    aidedCorrect: state.aidedCorrect + (correct && options.aided ? 1 : 0),
    lastSeenAt: now,
    streak: correct ? state.streak + 1 : 0,
  };
}

export function masteryBand(pKnown: number): "novice" | "developing" | "proficient" | "mastered" {
  if (pKnown >= 0.85) return "mastered";
  if (pKnown >= 0.6) return "proficient";
  if (pKnown >= 0.35) return "developing";
  return "novice";
}

export const MASTERY_BAND_FA: Record<ReturnType<typeof masteryBand>, string> = {
  novice: "تازه‌کار",
  developing: "در حال رشد",
  proficient: "مسلط نسبی",
  mastered: "تسلط کامل",
};

/** Guidance weight: how much hinting the learner needs right now. */
export function scaffoldingLevel(pKnown: number): "full" | "partial" | "none" {
  if (pKnown < 0.35) return "full";
  if (pKnown < 0.7) return "partial";
  return "none";
}
