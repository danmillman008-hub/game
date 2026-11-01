/**
 * Grading — implementation of the recovered Mimo algorithm.
 * spec: HANDOFF/04_SPEC_INTERACTION_AND_GRADING.md §2–§6
 * parity reference: HANDOFF/tools/reference_engine.py (verified by mimo/learn/tests parity test)
 *
 * Invariants that must never be "improved" without a delta id:
 *  1. PARTIAL exists only for validatedInput.
 *  2. CORRECT requires raw equality; a normalised match with different text is PARTIAL.
 *  3. lower-casing uses Locale.US semantics, not the environment default.
 *  4. `tries` is a 0/1 flag, not a counter.
 */

export const CORRECT = 'CORRECT';
export const PARTIAL = 'PARTIAL';
export const INCORRECT = 'INCORRECT';

/** The nine punctuation characters the recovered normaliser keeps. */
const KEEP = new Set(['<', '>', '(', ')', ':', '{', '}', ',', '.']);
const LETTER_OR_DIGIT = /[\p{L}\p{N}]/u;

/** qm.i.a — lower-case (Locale.US), keep letters/digits + < > ( ) : { } , . drop the rest. */
export function normalise(input) {
  const text = String(input ?? '');
  let out = '';
  for (const ch of text) {
    const lower = ch.toLocaleLowerCase('en-US');
    for (const part of lower) {
      if (LETTER_OR_DIGIT.test(part)) out += part;
      else if (KEEP.has(part)) out += part;
    }
  }
  return out;
}

/** The three-way rule. `user` and `expected` are raw strings. */
export function gradeValidatedInput(user, expected) {
  const u = String(user ?? '');
  const e = String(expected ?? '');
  if (normalise(u) !== normalise(e)) return INCORRECT;
  if (u === e) return CORRECT;
  return PARTIAL;
}

/** Selection (single or multiple): chosen set must equal the correct set; empty selection is incorrect. */
export function gradeSelection(items, chosenIndexes) {
  if (!items || !items.length) return INCORRECT;
  const correct = new Set(items.filter((i) => i.correct).map((i) => i.index));
  const chosen = new Set([...(chosenIndexes || [])].filter((i) => Number.isInteger(i)));
  if (!chosen.size) return INCORRECT;
  if (chosen.size !== correct.size) return INCORRECT;
  for (const i of chosen) if (!correct.has(i)) return INCORRECT;
  return CORRECT;
}

/** Fill-the-gap over N ranges: all-or-nothing. */
export function gradeFillTheGap(answers, expected) {
  const a = answers || [];
  const e = expected || [];
  if (a.length !== e.length) return INCORRECT;
  for (let i = 0; i < e.length; i += 1) {
    if (normalise(a[i]) !== normalise(e[i])) return INCORRECT;
  }
  return CORRECT;
}

/** Spelling: joined with '' and compared as one string (two-way). */
export function gradeSpell(letters, expected) {
  const a = (letters || []).join('');
  const e = (expected || []).join('');
  return a === e ? CORRECT : INCORRECT;
}

export const VISIBILITY = Object.freeze({ ALWAYS: 'ALWAYS', CORRECT: 'CORRECT', WRONG: 'WRONG' });

/** `visible-if` gating. PARTIAL renders ALWAYS blocks only (state jm.n). */
export function isVisible(declared, verdict) {
  const v = String(declared || 'ALWAYS').toUpperCase();
  if (v === VISIBILITY.ALWAYS) return true;
  if (v === VISIBILITY.CORRECT) return verdict === CORRECT;
  if (v === VISIBILITY.WRONG) return verdict === INCORRECT;
  return true;
}

/** Feedback state per verdict (jm.m / jm.n / jm.o). */
export function feedbackState(verdict) {
  if (verdict === CORRECT) return 'jm.m';
  if (verdict === PARTIAL) return 'jm.n';
  return 'jm.o';
}

/**
 * The V/W/X/U update sites (HANDOFF/04 §6).
 * `previousWasWrong` is the recovered flag C: true when the last verdict on this lesson was INCORRECT.
 * Returns the next counters plus the new C.
 */
export function applySubmission(verdict, previousWasWrong, attemptsBefore) {
  const attempts = Number(attemptsBefore || 0) + 1;
  const c = previousWasWrong === true;
  if (verdict === CORRECT || verdict === PARTIAL) {
    return { attempts, tries: c ? 0 : 1, previousWasWrong: false };
  }
  if (verdict === INCORRECT) {
    return { attempts, tries: 0, previousWasWrong: true };
  }
  // PROCEED — the "next" path (U): tries mirrors C
  return { attempts, tries: c ? 1 : 0, previousWasWrong: c };
}

export function isSolved(tries) {
  return Number(tries) >= 1;
}

/** ADD-04 — local completion rule replacing Mimo's server-side decision. */
export function chapterIsComplete(lessonRows) {
  if (!lessonRows || !lessonRows.length) return false;
  return lessonRows.every((r) => isSolved(r.tries));
}

export function firstTryCount(rows) {
  return (rows || []).filter((r) => isSolved(r.tries) && r.attempts === 1).length;
}

export function answersInChapter(rows) {
  const list = rows || [];
  return { answeredCorrectly: list.filter((r) => isSolved(r.tries)).length, answeredTotal: list.length };
}
