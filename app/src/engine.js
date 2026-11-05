/**
 * Pure, DOM-free domain logic.
 *
 * Evidence tags (from ANALYSIS/MISSION_09, read-only reference):
 *   VERIFIED       – observed in runtime/static evidence (M07/M08/M09 claims)
 *   SHAPE_ONLY     – only the data shape is documented, no server semantics
 *   DESIGN_CHOICE  – our own independent offline rule, NOT a claim about Mimo
 *
 * Nothing in this file contacts a server or invents a server response.
 */

/** VERIFIED (M07 stage 6): isSolvedCorrectly() == tries >= 1. */
export function isSolvedCorrectly(row) {
  return Number(row?.tries ?? 0) >= 1;
}

/** VERIFIED (M07 stage 6, LessonProgress constructor): exact 11-field shape.
 *  We store the same field names locally; `inQueue` feeds our local outbox. */
export function createLessonProgress(input, now = Date.now()) {
  return {
    id: input.id ?? `lp-${now}-${Math.random().toString(36).slice(2, 9)}`,
    tutorialId: input.tutorialId,
    sectionIndex: input.sectionIndex ?? 1,
    chapterId: input.chapterId,
    lessonId: input.lessonId,
    trackId: input.trackId,
    tries: input.tries ?? 1,
    attempts: input.attempts ?? 1,
    isPracticeProgress: Boolean(input.isPracticeProgress),
    inQueue: true,
    publishSetVersion: 753,
    createdAt: now,
  };
}

/** VERIFIED (M07 validators): selection == all(selected == isCorrect). */
export function validateSelection(selectedIds, options) {
  if (!Array.isArray(options) || options.length === 0) return false;
  const selected = new Set(selectedIds ?? []);
  return options.every((o) => Boolean(o.isCorrect) === selected.has(o.id));
}

/** VERIFIED (M07 validators): fillTheGap / spell == ordered list equality. */
export function validateOrdered(answer, expected) {
  if (!Array.isArray(answer) || !Array.isArray(expected)) return false;
  return answer.length === expected.length && answer.every((v, i) => v === expected[i]);
}

/** Score a placeholder session. This is OUR local rule, not Mimo scoring. */
export function scoreSession(questions, answers) {
  let correct = 0; let wrong = 0; let blank = 0;
  questions.forEach((q) => {
    const a = answers[q.id];
    if (a === undefined || a === null || a === '') { blank += 1; return; }
    if (q.correctId === undefined || q.correctId === null) { blank += 1; return; }
    if (String(a) === String(q.correctId)) correct += 1;
    else wrong += 1;
  });
  const answered = correct + wrong;
  return { total: questions.length, answered, correct, wrong, blank,
    percent: answered ? Math.round((correct / answered) * 100) : 0 };
}

/** DESIGN_CHOICE: deterministic sequential unlock for offline placeholder data.
 *  M09 could not confirm the real unlock policy on device; we do NOT present
 *  this as Mimo behaviour. */
export function unlockStatus(lessonId, orderedIds, completions) {
  const index = orderedIds.indexOf(lessonId);
  if (index < 0) return 'locked';
  if (completions[lessonId]) return 'done';
  if (index === 0) return 'open';
  return completions[orderedIds[index - 1]] ? 'open' : 'locked';
}

/** SHAPE_ONLY: chapter completion from local lesson rows. */
export function chapterCompletion(lessonRows, chapterId) {
  const rows = lessonRows.filter((r) => r.chapterId === chapterId);
  const solved = rows.filter(isSolvedCorrectly).length;
  return { rows: rows.length, solved, ratio: rows.length ? solved / rows.length : 0 };
}

/** DESIGN_CHOICE: local reward ledger. Award formulas are UNKNOWN in M09, so
 *  every grant is an explicit, labelled app action (never a Mimo claim). */
export function grant(state, { coins = 0, xp = 0, reason, at = Date.now() }) {
  state.economy.coins += coins;
  state.economy.xp += xp;
  state.economy.weeklyXp += xp;
  state.syncQueue.push({ type: 'reward', reason, coins, xp, at, status: 'local-only' });
  return state.economy;
}

/** DESIGN_CHOICE: durable local outbox entry (no transport exists). */
export function enqueue(state, entry, at = Date.now()) {
  const row = { ...entry, at, status: 'local-only' };
  state.syncQueue.push(row);
  return row;
}

/** Pure navigation reducer: the 5 approved tabs only. No "Max" tab exists. */
export const TAB_SCREENS = {
  Learn: 'learn',
  Practice: 'exam-hub',
  AI: 'ai',
  Leaderboard: 'leaderboard',
  Profile: 'profile',
};

export const TAB_LABELS_FA = {
  Learn: 'یادگیری',
  Practice: 'تمرین',
  AI: 'هوش مصنوعی',
  Leaderboard: 'امتیازها',
  Profile: 'پروفایل',
};

export const ROUTES = {
  direct: { key: 'direct', fa: 'یادگیری مستقیم', en: 'Direct Learning',
    entry: 'learn', description: 'ورود به مسیر بدون آزمون ورودی' },
  exam: { key: 'exam', fa: 'آزمون', en: 'Exam',
    entry: 'exam-hub', description: 'ساختار آزمون، تایمر، پاسخگویی، نتیجه و وضعیت' },
  'study-plan': { key: 'study-plan', fa: 'مسیر یادگیری برنامهمحور', en: 'Study-Plan Learning Path',
    entry: 'study-plan', description: 'مسیر و وضعیت برنامه؛ آزمون اولیه/ترمیم/نهایی در مراحل بعد' },
};

export function canEnterRoute(route /*, state */) {
  // DESIGN_CHOICE: all three routes are locally reachable; none is server-gated.
  return Object.hasOwn(ROUTES, route);
}
