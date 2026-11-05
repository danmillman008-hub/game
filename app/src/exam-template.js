/** Template-driven exam & practice builders. No network, no invented content. */
import { EXAM_TEMPLATE, PRACTICE_TEMPLATE } from './templates.js';
import { scoreSession } from './engine.js';

export { EXAM_TEMPLATE, PRACTICE_TEMPLATE };

const byId = (q) => String(q.id);
const stable = (arr) => [...arr].sort((a, b) => byId(a).localeCompare(byId(b)));

/** Pick questions deterministically from the form-conformant bank. */
export function selectQuestions(questions, selection = {}, count = 10, opts = {}) {
  const all = stable(Array.isArray(questions) ? questions : []);
  const mode = selection.topicIds || 'all';
  let pool = all;
  if (mode === 'one') {
    const topic = opts.topicId || all[0]?.topicId;
    pool = all.filter((q) => q.topicId === topic);
  } else if (mode === 'recent') {
    pool = all.filter((q) => !opts.recentTopicIds || opts.recentTopicIds.includes(q.topicId));
    if (!pool.length) pool = all;
  } else if (Array.isArray(mode)) {
    pool = all.filter((q) => mode.includes(q.topicId));
  }
  const mix = selection.difficulty || {};
  const quotas = {};
  for (const [level, ratio] of Object.entries(mix)) quotas[level] = Math.round(count * ratio);
  const chosen = [];
  const used = new Set();
  for (const [level, quota] of Object.entries(quotas)) {
    const candidates = pool.filter((q) => (q.difficulty || 'unknown') === level && !used.has(q.id));
    chosen.push(...candidates.slice(0, quota));
    candidates.slice(0, quota).forEach((q) => used.add(q.id));
  }
  for (const q of pool) {
    if (chosen.length >= count) break;
    if (!used.has(q.id)) { chosen.push(q); used.add(q.id); }
  }
  return {
    questionIds: chosen.map((q) => q.id),
    questions: chosen,
    shortfall: Math.max(0, count - chosen.length),
    mode,
  };
}

/** Build an exam instance from a template section + question bank. */
export function buildExam(kind, questions, opts = {}) {
  const section = EXAM_TEMPLATE.sections.find((s) => s.kind === kind);
  if (!section) return null;
  const picked = selectQuestions(questions, section.selection, section.questionCount, opts);
  return {
    id: `exam-${kind}-${opts.at || Date.now()}`,
    templateVersion: EXAM_TEMPLATE.templateVersion,
    kind: section.kind, titleFa: section.titleFa, sectionIndex: section.index,
    minutes: section.minutes, policy: section.policy,
    topicIds: picked.mode, questionIds: picked.questionIds, shortfall: picked.shortfall,
    answeringComponents: EXAM_TEMPLATE.answerComponents.list,
    resultScreen: EXAM_TEMPLATE.result.screen,
    contentStatus: EXAM_TEMPLATE.contentStatus,
    placeholder: true,
  };
}

/** Build a practice session (same answering components, NO timer). */
export function buildPracticeSession(modeId, questions, opts = {}) {
  const mode = PRACTICE_TEMPLATE.modes.find((m) => m.id === modeId) || PRACTICE_TEMPLATE.modes[2];
  const scope = opts.scope ?? null;
  let pool = stable(Array.isArray(questions) ? questions : []);
  if (scope && mode.scope === 'topicId') pool = pool.filter((q) => q.topicId === scope);
  if (scope && mode.scope === 'chapterId') pool = pool.filter((q) => String(q.chapterId) === String(scope));
  if (mode.id === 'mistakes' && Array.isArray(scope)) pool = pool.filter((q) => scope.includes(q.id));
  const n = typeof mode.questionCount === 'number' ? mode.questionCount : pool.length;
  const chosen = pool.slice(0, Math.min(n, pool.length));
  return {
    id: `practice-${mode.id}-${opts.at || Date.now()}`,
    templateVersion: PRACTICE_TEMPLATE.templateVersion,
    mode: mode.id, titleFa: mode.titleFa, entry: mode.entry, scope,
    questionIds: chosen.map((q) => q.id), questions: chosen,
    timed: PRACTICE_TEMPLATE.rules.timed,
    minutes: null,
    retryAllowed: PRACTICE_TEMPLATE.rules.retryAllowed,
    immediateFeedback: PRACTICE_TEMPLATE.rules.immediateFeedback,
    answeringComponents: EXAM_TEMPLATE.answerComponents.list,
    placeholder: true,
  };
}

export function scorePracticeSession(session, answers) {
  return scoreSession(session.questions || [], answers || {});
}

export function templateSummary() {
  return {
    examSections: EXAM_TEMPLATE.sections.map((s) => ({ kind: s.kind, minutes: s.minutes, count: s.questionCount })),
    practiceModes: PRACTICE_TEMPLATE.modes.map((m) => ({ id: m.id, timed: false, count: m.questionCount })),
    sharedAnsweringComponents: EXAM_TEMPLATE.answerComponents.sharedWithPractice,
  };
}
