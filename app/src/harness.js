/**
 * LearnHarness-compatible LOCAL teaching harness for the AI tab.
 *
 * Architecture (measure/plan/teach/practice + knowledge graph) follows
 * github.com/amosblomqvist/learnharness @ 713377f (AGPL-3.0); see
 * app/vendor/LEARNHARNESS_INTEGRATION.md. NO code was copied.
 *
 * HONESTY CONTRACT: the default provider does NOT generate any text,
 * explanation, answer or AI reply. It only selects lessons/questions that
 * already exist in the content form. An empty content package yields an
 * explicit "no source registered" state, never a fabricated answer.
 * No fetch / XHR / WebSocket / API key / token exists in this module.
 */
import { buildPracticeSession } from './exam-template.js';

export const LEARNHARNESS = Object.freeze({
  repo: 'https://github.com/amosblomqvist/learnharness.git',
  commit: '713377f366771e3e4730e6acd1bc290e0ebc6d6e',
  license: 'AGPL-3.0-only',
  phases: Object.freeze(['measure', 'plan', 'teach', 'practice']),
  phaseFa: Object.freeze({ measure: 'سنجش', plan: 'برنامهریزی', teach: 'آموزش', practice: 'تمرین' }),
});

export const PHASE_FA = LEARNHARNESS.phaseFa;

/** Default provider: deterministic selection over EXISTING form content. */
export function LocalContentProvider(pkg = null) {
  const lessons = [];
  const questions = [];
  const topics = new Map();
  if (pkg) {
    for (const track of pkg.tracks || []) {
      for (const section of track.sections || []) {
        for (const tutId of section.tutorialIds || []) {
          const tut = (pkg.tutorials || []).find((t) => t.id === tutId);
          if (!tut) continue;
          for (const ch of tut.chapters || []) {
            for (const l of ch.lessons || []) {
              lessons.push({ ...l, tutorialId: tut.id, chapterId: ch.id, topicId: l.topicId || String(ch.id) });
            }
          }
        }
      }
    }
    for (const q of pkg.questions || []) {
      questions.push(q);
      const key = q.topicId || 'unknown';
      topics.set(key, (topics.get(key) || 0) + 1);
    }
  }
  return {
    id: 'local-content',
    status: 'ready',
    capabilities: ['select-lesson', 'select-question', 'graph'],
    generatesText: false,
    lessons, questions, topics,
  };
}

/** Contract for an eventual real provider. Never instantiated here. */
export const EXTERNAL_PROVIDER_CONTRACT = Object.freeze({
  id: 'learnharness-openai-compatible',
  status: 'not-configured',
  requires: ['user-supplied endpoint', 'server-side proxy', 'user API key (never in browser/git)'],
  note: 'No endpoint is configured in this offline build. Nothing is fabricated.',
});

function emptyHarnessState() {
  return {
    active: false, phase: 'measure', goal: null, measurement: null,
    plan: [], currentStep: 0, confidence: null, reasoning: '',
    graph: { propositions: [] }, sessions: [], provider: 'local-content',
    updatedAt: null,
  };
}

export function createHarness({ store, contentPackage = null, at = () => Date.now() }) {
  const provider = LocalContentProvider(contentPackage);
  const stateKey = 'ai.harness';
  let h = store.get(stateKey);
  if (!h || typeof h !== 'object') { h = emptyHarnessState(); store.set(stateKey, h); }

  function save(patch) {
    h = { ...h, ...patch, updatedAt: at() };
    store.set(stateKey, h);
    return h;
  }

  function start(goal, reasoning = '') {
    if (!goal || !goal.trim()) return { ok: false, reason: 'goal-required' };
    const clean = goal.trim();
    const picked = provider.questions.filter((q) =>
      !clean || (q.topicId && q.topicId.includes(clean)) || (q.stemFa && q.stemFa.includes(clean)));
    const measurement = {
      goal: clean,
      candidateQuestionIds: (picked.length ? picked : provider.questions).slice(0, 5).map((q) => q.id),
      availableQuestions: provider.questions.length,
      availableLessons: provider.lessons.length,
      honest: provider.questions.length === 0 ? 'no-source-registered' : 'measured-from-existing-bank',
    };
    return { ok: true, state: save({ active: true, phase: 'measure', goal: clean, reasoning,
      measurement, plan: [], currentStep: 0 }) };
  }

  function plan(confidence = null) {
    const lessons = provider.lessons;
    const steps = lessons.slice(0, 6).map((l, i) => ({
      index: i, lessonId: l.id, title: l.title || `گام ${i + 1}`,
      pedagogicalRole: l.pedagogicalRole || 'explain',
      topicId: l.topicId,
      // LearnHarness: dependency map from measured starting point to goal.
      dependsOn: i === 0 ? null : lessons[i - 1]?.id ?? null,
    }));
    return { ok: true, state: save({ phase: 'plan', plan: steps, currentStep: 0, confidence }) };
  }

  function teach(stepIndex = h.currentStep) {
    const step = h.plan[stepIndex];
    if (!step) {
      return { ok: false, reason: provider.lessons.length === 0 ? 'no-source-registered' : 'no-step',
        message: 'هیچ درسنامهای در فرم اطلاعاتی ثبت نشده است؛ منابع در مرحلهٔ بعد اضافه میشوند.' };
    }
    const l = provider.lessons.find((x) => String(x.id) === String(step.lessonId));
    const proposition = {
      id: `prop-${at()}-${stepIndex}`,
      text: l?.blocks?.[0]?.contentFa || step.title,
      lessonId: step.lessonId, topicId: step.topicId,
      sourceRef: l?.trace?.sourceRef || null,
      sourcePage: l?.trace?.sourcePage || null,
      confidence: h.confidence, sessionId: `session-${h.updatedAt || at()}`,
      links: step.dependsOn ? [String(step.dependsOn)] : [],
      generated: false,
    };
    const graph = { propositions: [...h.graph.propositions, proposition] };
    return { ok: true, state: save({ phase: 'teach', currentStep: stepIndex, graph }),
      proposition, generated: false };
  }

  function practice(topicId = null) {
    const session = buildPracticeSession('topic', provider.questions, { scope: topicId });
    return { ok: true, state: save({ phase: 'practice' }), session, generated: false };
  }

  function advance() {
    const order = LEARNHARNESS.phases;
    const i = order.indexOf(h.phase);
    const next = order[Math.min(i + 1, order.length - 1)];
    return { ok: true, state: save({ phase: next }) };
  }

  function setPhase(phase) {
    if (!LEARNHARNESS.phases.includes(phase)) return { ok: false, reason: 'unknown-phase' };
    return { ok: true, state: save({ phase }) };
  }

  function stop() { return { ok: true, state: save({ active: false }) }; }

  function getStatus() {
    return {
      active: h.active, phase: h.phase, phaseFa: PHASE_FA[h.phase],
      goal: h.goal, steps: h.plan.length, propositions: h.graph.propositions.length,
      provider: provider.id, providerStatus: provider.status,
      generatesText: provider.generatesText,
      externalProvider: EXTERNAL_PROVIDER_CONTRACT.status,
      availableLessons: provider.lessons.length, availableQuestions: provider.questions.length,
      honest: provider.lessons.length === 0 && provider.questions.length === 0
        ? 'no-source-registered' : 'local-content-only',
      repo: LEARNHARNESS.repo, commit: LEARNHARNESS.commit, license: LEARNHARNESS.license,
    };
  }

  return { start, plan, teach, practice, advance, setPhase, stop, getStatus, get state() { return h; } };
}
