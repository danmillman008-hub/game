/**
 * Offline, durable application state.
 *
 * This module is DOM-free and storage-injectable so it can be unit-tested in
 * Node and reused by the browser without any dependency. It is an INDEPENDENT
 * implementation: nothing here claims to reproduce Mimo's Room database. Only
 * field *shapes* documented in ANALYSIS/MISSION_09 are mirrored, and every
 * value is local until an explicit sync gateway exists (there is none here).
 */

export const SCHEMA_VERSION = 1;
export const STORAGE_KEY = 'mimo.offline.app.v1';

export function defaultState(now = Date.now()) {
  return {
    schemaVersion: SCHEMA_VERSION,
    createdAt: now,
    updatedAt: now,
    identity: {
      id: 'local-guest',
      displayName: 'کاربر مهمان',
      guest: true,            // no account, no auth token, no server
      locale: 'fa',
    },
    meta: {
      offlineOnly: true,
      serverConfirmed: false,
      placeholderContent: true,
      designVersion: 'v12.5-fa',
    },
    economy: {
      coins: 1272,            // prototype header value; treated as local seed data
      keys: 1,
      streak: 0,
      xp: 480,
      weeklyXp: 330,
      examsTaken: 7,
      trophies: [],
    },
    settings: {
      theme: 'day',           // 'day' | 'night'
      rtl: false,             // prototype's mirror toggle
      sound: true,
      haptics: true,
      reduceMotion: false,
      dailyGoal: 15,
    },
    route: {
      mode: 'direct',         // 'direct' | 'exam' | 'study-plan'
      pathId: 'grade12',
      studyPlan: {
        active: false,
        programId: null,
        stage: 'not-started', // not-started | initial-exam | remediation | final-exam | completed
        initialExamId: null,
        finalExamId: null,
        remediationIds: [],
        updatedAt: null,
      },
    },
    progress: {
      // Exact M09 LessonProgress field names; local rows only.
      lessonRows: [],
      chapterCompletions: {},
      tutorialCompletions: {},
      unlocks: {},            // lessonId -> 'locked' | 'open' | 'done'
      currentLessonId: null,
    },
    exam: {
      saved: null,            // prototype SAVED snapshot, persisted across restarts
      status: 'idle',         // idle | running | paused | finished
      activeKind: null,
      results: [],            // local result records (placeholder scoring)
    },
    practice: {
      sessions: [],           // completed practice sessions
      active: null,           // in-flight session, recoverable
      bankCursor: 0,
    },
    leaderboard: {
      // placeholder rows, clearly separated from any server ranking
      rows: [],
      lastViewedAt: null,
    },
    ai: {
      threads: [],            // local chat log; no AI teacher / no network
      harness: null,          // LearnHarness-compatible local teaching session
    },
    navigation: {
      screen: 'learn',
      tab: 'Learn',
      history: [],
    },
    syncQueue: [],            // durable local outbox (independent design decision)
  };
}

/** Merge persisted data into a fresh default tree. Unknown keys are dropped;
 *  missing/older shapes are upgraded. Corrupt data never breaks boot. */
function migrate(raw, now) {
  const base = defaultState(now);
  if (!raw || typeof raw !== 'object' || Array.isArray(raw)) return base;
  const merged = { ...base };
  for (const key of Object.keys(base)) {
    const incoming = raw[key];
    if (incoming === undefined || incoming === null) continue;
    if (Array.isArray(base[key])) {
      if (Array.isArray(incoming)) merged[key] = incoming;
    } else if (typeof base[key] === 'object') {
      if (typeof incoming === 'object' && !Array.isArray(incoming)) {
        merged[key] = { ...base[key], ...incoming };
      }
    } else if (typeof incoming === typeof base[key]) {
      merged[key] = incoming;
    }
  }
  merged.schemaVersion = SCHEMA_VERSION;
  merged.createdAt = Number.isFinite(raw.createdAt) ? raw.createdAt : now;
  merged.updatedAt = now;
  // invariants
  if (!['direct', 'exam', 'study-plan'].includes(merged.route.mode)) merged.route.mode = 'direct';
  if (!['day', 'night'].includes(merged.settings.theme)) merged.settings.theme = 'day';
  if (!Array.isArray(merged.progress.lessonRows)) merged.progress.lessonRows = [];
  merged.meta = { ...base.meta }; // never trust persisted capability flags
  return merged;
}

export function memoryStorage() {
  const map = new Map();
  return {
    getItem: (k) => (map.has(k) ? map.get(k) : null),
    setItem: (k, v) => map.set(k, String(v)),
    removeItem: (k) => map.delete(k),
  };
}

function readPath(obj, path) {
  const parts = path.split('.');
  let cur = obj;
  for (const part of parts) {
    if (cur === null || cur === undefined || typeof cur !== 'object') return undefined;
    cur = cur[part];
  }
  return cur;
}

function writePath(obj, path, value) {
  const parts = path.split('.');
  let cur = obj;
  for (let i = 0; i < parts.length - 1; i += 1) {
    if (typeof cur[parts[i]] !== 'object' || cur[parts[i]] === null) cur[parts[i]] = {};
    cur = cur[parts[i]];
  }
  cur[parts.at(-1)] = value;
}

export function createStore(storage = globalThis.localStorage, now = () => Date.now()) {
  let state;
  let corruption = null;
  try {
    const raw = storage.getItem(STORAGE_KEY);
    state = migrate(raw ? JSON.parse(raw) : null, now());
  } catch (err) {
    corruption = String(err && err.message ? err.message : err);
    state = defaultState(now());
  }

  const listeners = new Set();

  function persist() {
    state.updatedAt = now();
    try {
      storage.setItem(STORAGE_KEY, JSON.stringify(state));
    } catch (err) {
      // Quota / private mode: keep the in-memory session usable, report it.
      corruption = String(err && err.message ? err.message : err);
    }
    for (const fn of listeners) {
      try { fn(state); } catch (_) { /* listener must not break persistence */ }
    }
  }

  const api = {
    get state() { return state; },
    get corruption() { return corruption; },
    get(path) { return readPath(state, path); },
    set(path, value) { writePath(state, path, value); persist(); return value; },
    patch(path, value) {
      const current = readPath(state, path);
      const next = (current && typeof current === 'object' && !Array.isArray(current))
        ? { ...current, ...value }
        : { ...value };
      return api.set(path, next);
    },
    push(path, value) {
      const arr = Array.isArray(readPath(state, path)) ? [...readPath(state, path)] : [];
      arr.push(value);
      api.set(path, arr);
      return value;
    },
    subscribe(fn) { listeners.add(fn); return () => listeners.delete(fn); },
    flush() { persist(); },
    reset() { storage.removeItem(STORAGE_KEY); state = defaultState(now()); persist(); return state; },
    export() { return JSON.parse(JSON.stringify(state)); },
    import(data) { state = migrate(data, now()); persist(); return state; },
  };
  return api;
}
