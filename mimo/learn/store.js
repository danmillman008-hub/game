/**
 * Local persistence — the learner model.
 * spec: HANDOFF/05_SPEC_LEARNER_MODEL.md, HANDOFF/06_SPEC_STORAGE.md
 *
 * The engine mirrors Mimo's three tables in one namespaced localStorage document:
 *   lesson_progress      (11 fields, PK lesson_id + tutorial_id)
 *   chapter_completions  (computed locally — ADD-04; Mimo filled it from the server)
 *   tutorial_completions (computed locally — ADD-04)
 *
 * Differences from Mimo are deliberate and listed in mimo/docs/DELTAS.md:
 *   D-14/ADD-08  a `user` partition key exists (local single-user: "local")
 *   C-22         rows are NOT deleted after an "upload" — there is no upload
 *   ADD-06       schemaVersion with a non-destructive migration path
 */

const STORAGE_KEY = 'mimo.learn.progress.v1';
export const SCHEMA_VERSION = 1;
export const LOCAL_USER = 'local';

export function emptyState() {
  return {
    schemaVersion: SCHEMA_VERSION,
    user: LOCAL_USER,
    publishSetVersion: null,
    rows: {},
    createdAt: new Date().toISOString(),
  };
}

export function loadState(storage = globalThis.localStorage) {
  try {
    const raw = storage?.getItem(STORAGE_KEY);
    if (!raw) return emptyState();
    const parsed = JSON.parse(raw);
    return migrate(parsed);
  } catch {
    return emptyState();
  }
}

/** ADD-06 — additive, non-destructive migration. */
export function migrate(state) {
  const next = { ...emptyState(), ...state };
  if (!Number.isFinite(Number(next.schemaVersion))) next.schemaVersion = SCHEMA_VERSION;
  // v0 (pre-preview) had `progress` as an array instead of a keyed map.
  if (Array.isArray(next.progress)) {
    next.rows = next.rows || {};
    for (const row of next.progress) {
      if (row?.lessonId != null && row?.tutorialId != null) {
        next.rows[`${row.tutorialId}:${row.lessonId}`] = { ...row, migratedFrom: 0 };
      }
    }
    delete next.progress;
  }
  next.rows = next.rows || {};
  if (Number(next.schemaVersion) < SCHEMA_VERSION) next.schemaVersion = SCHEMA_VERSION;
  return next;
}

export function saveState(state, storage = globalThis.localStorage) {
  const payload = JSON.stringify(state);
  storage?.setItem(STORAGE_KEY, payload);
  return payload;
}

export function clearState(storage = globalThis.localStorage) {
  storage?.removeItem(STORAGE_KEY);
}

/* --- rows ------------------------------------------------------------------------------------------------ */

export function getRow(state, lessonId, tutorialId) {
  return state.rows[`${Number(tutorialId)}:${Number(lessonId)}`] || null;
}

export function ensureRow(state, { lessonId, tutorialId, tutorialVersion, trackId, publishSetVersion, isPractice = false }, now = new Date()) {
  const key = `${Number(tutorialId)}:${Number(lessonId)}`;
  const existing = state.rows[key];
  if (existing) {
    // keep startedAt stable; refresh content version when the pack moved forward
    existing.tutorialVersion = tutorialVersion ?? existing.tutorialVersion;
    existing.publishSetVersion = publishSetVersion ?? existing.publishSetVersion;
    return existing;
  }
  const iso = now.toISOString();
  const row = {
    lessonId: Number(lessonId),
    tutorialId: Number(tutorialId),
    tutorialVersion: Number(tutorialVersion ?? 0),
    trackId: Number(trackId ?? 0),
    publishSetVersion: Number(publishSetVersion ?? 0),
    tries: 0,
    attempts: 0,
    startedAt: iso,
    completedAt: iso,
    isPracticeProgress: Boolean(isPractice),
    inQueue: false, // no outbox: this engine is offline-only (D-18 / C-22)
    previousWasWrong: false,
    lastVerdict: null,
    user: LOCAL_USER,
  };
  state.rows[key] = row;
  return row;
}

export function applyResult(state, row, verdict, applySubmission) {
  const counters = applySubmission(verdict, row.previousWasWrong, row.attempts);
  row.attempts = counters.attempts;
  row.tries = counters.tries;
  row.previousWasWrong = counters.previousWasWrong;
  row.lastVerdict = verdict;
  row.completedAt = new Date().toISOString();
  return row;
}

/* --- derived views --------------------------------------------------------------------------------------- */

export function rowsForTutorial(state, tutorialId) {
  return Object.values(state.rows).filter((r) => Number(r.tutorialId) === Number(tutorialId));
}

export function rowsForLessons(state, lessonIds, tutorialId) {
  const wanted = new Set(lessonIds.map((id) => `${Number(tutorialId)}:${Number(id)}`));
  return Object.entries(state.rows)
    .filter(([key]) => wanted.has(key))
    .map(([, row]) => row);
}

export function chapterProgress(state, chapter, tutorialId) {
  const lessons = (chapter.lessons || []).map((l) => l.id);
  const rows = rowsForLessons(state, lessons, tutorialId);
  const solved = rows.filter((r) => r.tries >= 1).length;
  return {
    total: lessons.length,
    solved,
    complete: lessons.length > 0 && solved === lessons.length,
    answeredTotal: rows.length,
  };
}

export function tutorialProgress(state, tutorial) {
  const chapters = tutorial.chapters || [];
  let total = 0;
  let solved = 0;
  for (const chapter of chapters) {
    const p = chapterProgress(state, chapter, tutorial.id);
    total += p.total;
    solved += p.solved;
  }
  return { total, solved, complete: total > 0 && solved === total, percent: total ? Math.round((solved / total) * 100) : 0 };
}

export function trackProgress(state, track, tutorialsById) {
  let total = 0;
  let solved = 0;
  for (const section of track.sections || []) {
    for (const ref of section.tutorials || []) {
      const tutorial = tutorialsById.get(Number(ref.id));
      if (!tutorial) continue;
      const p = tutorialProgress(state, tutorial);
      total += p.total;
      solved += p.solved;
    }
  }
  return { total, solved, percent: total ? Math.round((solved / total) * 100) : 0 };
}

export function globalStats(state) {
  const rows = Object.values(state.rows);
  const solvedRows = rows.filter((r) => r.tries >= 1);
  const totalAttempts = rows.reduce((acc, r) => acc + (r.attempts || 0), 0);
  return {
    lessonsTouched: rows.length,
    lessonsSolved: solvedRows.length,
    firstTry: solvedRows.filter((r) => r.attempts === 1).length,
    attempts: totalAttempts,
    accuracy: totalAttempts ? Math.round((solvedRows.length / totalAttempts) * 100) : 0,
  };
}

export { STORAGE_KEY };
