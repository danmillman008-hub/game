/**
 * The three learning routes and the Study-Plan stage machine.
 * Pure state transitions; no DOM, no server, no invented exam content.
 */

import { ROUTES, canEnterRoute } from './engine.js';

export const STUDY_PLAN_STAGES = Object.freeze([
  { key: 'not-started', fa: 'شروع برنامه', detail: 'مسیر انتخاب نشده است', implemented: true },
  { key: 'initial-exam', fa: 'آزمون اولیه', detail: 'ساختار رزرو شده — محتوا بعداً', implemented: false },
  { key: 'remediation', fa: 'رفع اشکال', detail: 'ساختار رزرو شده — محتوا بعداً', implemented: false },
  { key: 'final-exam', fa: 'آزمون نهایی', detail: 'ساختار رزرو شده — محتوا بعداً', implemented: false },
  { key: 'completed', fa: 'پایان برنامه', detail: 'ساختار رزرو شده — محتوا بعداً', implemented: false },
]);

const ALLOWED = {
  'not-started': ['initial-exam', 'remediation'],
  'initial-exam': ['remediation'],
  remediation: ['final-exam'],
  'final-exam': ['completed', 'remediation'],
  completed: ['not-started'],
};

export function getRoute(store) {
  return ROUTES[store.get('route.mode')] || ROUTES.direct;
}

export function setRoute(store, mode, at = Date.now()) {
  if (!canEnterRoute(mode)) return null;
  store.patch('route', { mode, updatedAt: at });
  return ROUTES[mode];
}

export function setPath(store, pathId) {
  store.patch('route', { pathId });
  return pathId;
}

export function planStatus(store) {
  const plan = store.get('route.studyPlan');
  const index = STUDY_PLAN_STAGES.findIndex((s) => s.key === plan.stage);
  return {
    plan,
    index,
    stage: STUDY_PLAN_STAGES[index] || STUDY_PLAN_STAGES[0],
    next: (ALLOWED[plan.stage] || [])[0] || null,
  };
}

/** Advance only along declared edges; returns {ok, from, to, reason}. */
export function advancePlan(store, target, at = Date.now()) {
  const from = store.get('route.studyPlan.stage');
  const allowed = ALLOWED[from] || [];
  if (!allowed.includes(target)) {
    return { ok: false, from, to: target, reason: 'transition-not-allowed' };
  }
  store.patch('route.studyPlan', { stage: target, active: true, updatedAt: at });
  return { ok: true, from, to: target };
}

export function activatePlan(store, programId, at = Date.now()) {
  store.patch('route.studyPlan', {
    active: true, programId, stage: 'not-started', updatedAt: at,
  });
  store.patch('route', { mode: 'study-plan' });
  return store.get('route.studyPlan');
}

export function routeSummary(store) {
  return Object.values(ROUTES).map((r) => ({
    ...r,
    active: store.get('route.mode') === r.key,
  }));
}
