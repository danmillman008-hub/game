import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import { createApp, APP } from './harness.mjs';
import { NODE_SPEC, assertGeometry } from '../src/nodes.js';
import { EXAM_TEMPLATE, PRACTICE_TEMPLATE, buildExam, buildPracticeSession, templateSummary } from '../src/exam-template.js';
import { createHarness, LEARNHARNESS } from '../src/harness.js';
import { createStore, memoryStorage } from '../src/store.js';

const SAMPLE_BANK = [
  { id: 'q1', topicId: 't1', difficulty: 'easy', correctId: 1, stemFa: 'نمونه ۱' },
  { id: 'q2', topicId: 't1', difficulty: 'medium', correctId: 0, stemFa: 'نمونه ۲' },
  { id: 'q3', topicId: 't2', difficulty: 'hard', correctId: 2, stemFa: 'نمونه ۳' },
  { id: 'q4', topicId: 't2', difficulty: 'medium', correctId: 1, stemFa: 'نمونه ۴' },
];

test('node fidelity: geometry constants equal the original code-first measurements', () => {
  assert.equal(NODE_SPEC.size_dp, 92);
  assert.equal(NODE_SPEC.corner_radius_dp, 26);
  assert.equal(NODE_SPEC.lip_dp, 8);
  assert.equal(NODE_SPEC.icon_dp, 48);
  assert.equal(NODE_SPEC.connector_stroke_dp, 10);
  assert.equal(NODE_SPEC.ring.progress_percent, 55);
  const css = fs.readFileSync(`${APP}/assets/node-match.css`, 'utf8');
  for (const token of ['width:92px', 'border-radius:26px', 'box-shadow:0 8px 0', 'conic-gradient', 'gloss-fab']) {
    assert.ok(css.includes(token), token);
  }
  // #fff is the approved white foreground already used throughout proto.css;
  // no OTHER hard-coded colour may be introduced by the fidelity layer.
  const hexes = [...new Set([...css.matchAll(/#[0-9a-fA-F]{3,8}\b/g)].map((m) => m[0].toLowerCase()))];
  assert.deepEqual(hexes, ['#fff'], `unexpected colours: ${hexes.join(',')}`);
});

test('node fidelity: live app matches injected NODE geometry and renders original states', async () => {
  const a = await createApp();
  try {
    assert.equal(a.app.geometryCheck.ok, true, JSON.stringify(a.app.geometryCheck));
    const nodes = a.qa('[data-screen="learn"] .pathwrap .node');
    assert.deepEqual(nodes.map((n) => n.dataset.state),
      ['done', 'done', 'cur-half', 'next', 'bolt-active', 'bolt-optional']);
    assert.ok(a.q('.gloss-fab .abook'), 'original floating dictionary affordance');
    assert.ok(nodes[2].classList.contains('half'));
    assert.ok(nodes[4].classList.contains('bolt'));
  } finally { a.close(); }
});

test('exam template: 7 approved sections, deterministic build, shared answering components', () => {
  assert.equal(EXAM_TEMPLATE.sections.length, 7);
  assert.deepEqual(EXAM_TEMPLATE.sections.map((s) => s.kind),
    ['comprehensive', 'timed', 'single', 'topic', 'monthly', 'analytical', 'review']);
  assert.equal(EXAM_TEMPLATE.sections[0].minutes, 270);
  assert.equal(EXAM_TEMPLATE.answerComponents.sharedWithPractice, true);
  const exam = buildExam('comprehensive', SAMPLE_BANK, { at: 1 });
  assert.equal(exam.kind, 'comprehensive');
  assert.equal(exam.timed, undefined);
  assert.equal(exam.minutes, 270);
  assert.ok(exam.questionIds.length > 0 && exam.questionIds.length <= 20);
  assert.equal(exam.shortfall > 0, true, 'shortfall is reported, never hidden');
  assert.deepEqual(exam.answeringComponents, EXAM_TEMPLATE.answerComponents.list);
  assert.equal(buildExam('nope', SAMPLE_BANK), null);
});

test('practice template: same answering components, NO timer', () => {
  assert.equal(PRACTICE_TEMPLATE.rules.timed, false);
  assert.equal(PRACTICE_TEMPLATE.rules.usesExamAnsweringComponents, true);
  const session = buildPracticeSession('topic', SAMPLE_BANK, { scope: 't1', at: 2 });
  assert.equal(session.timed, false);
  assert.equal(session.minutes, null);
  assert.equal(session.retryAllowed, true);
  assert.deepEqual(session.answeringComponents, EXAM_TEMPLATE.answerComponents.list);
  assert.deepEqual(session.questionIds, ['q1', 'q2']);
  assert.equal(templateSummary().sharedAnsweringComponents, true);
});

test('wiring: exam row click attaches a template, practice sessions record their template', async () => {
  const a = await createApp();
  try {
    a.go('exam-hub');
    a.click(a.q('.nodek[data-exam]'));
    const t = a.app.store.get('exam.activeTemplate');
    assert.ok(t && t.templateVersion === '1.0.0');
    assert.equal(t.minutes, 270);
    a.go('practice-bank');
    a.click(a.q('#bankList [data-bank-opt="0"]'));
    a.click(a.q('#bankStart'));
    const rec = a.app.store.get('practice.sessions')[0];
    assert.equal(rec.template.timed, false);
    assert.equal(rec.template.mode, 'bank');
  } finally { a.close(); }
});

test('LearnHarness: local provider never generates text and is honest about empty sources', () => {
  assert.equal(LEARNHARNESS.commit, '713377f366771e3e4730e6acd1bc290e0ebc6d6e');
  assert.equal(LEARNHARNESS.license, 'AGPL-3.0-only');
  const store = createStore(memoryStorage(), () => 1);
  const h = createHarness({ store, contentPackage: null, at: () => 1 });
  let st = h.getStatus();
  assert.equal(st.provider, 'local-content');
  assert.equal(st.generatesText, false);
  assert.equal(st.honest, 'no-source-registered');
  assert.equal(st.externalProvider, 'not-configured');
  assert.equal(h.start('زیست').ok, true);
  assert.equal(h.getStatus().phaseFa, 'سنجش');
  // no lessons => plan is empty, teach refuses rather than inventing an answer
  assert.equal(h.plan(80).state.plan.length, 0);
  const t = h.teach();
  assert.equal(t.ok, false);
  assert.equal(t.reason, 'no-source-registered');
  assert.equal(t.generated, undefined);
  assert.equal(h.setPhase('practice').state.phase, 'practice');
  assert.equal(h.practice().session.timed, false);
});

test('LearnHarness: attaching a content package fills the graph without generating text', () => {
  const pkg = {
    tracks: [{ id: 1, sections: [{ tutorialIds: [10] }] }],
    tutorials: [{ id: 10, chapters: [{ id: 20, lessons: [
      { id: 30, title: 'گام ۱', pedagogicalRole: 'explain',
        blocks: [{ contentFa: 'متن موجود در کتاب' }],
        trace: { sourceRef: 'book:bio:page-12:block-1', sourcePage: 12 } },
    ] }] }],
    questions: SAMPLE_BANK, exams: [],
  };
  const store = createStore(memoryStorage(), () => 1);
  const h = createHarness({ store, contentPackage: pkg, at: () => 1 });
  assert.equal(h.getStatus().availableLessons, 1);
  assert.equal(h.getStatus().availableQuestions, 4);
  h.start('t1'); h.plan(75);
  assert.equal(h.getStatus().steps, 1);
  const t = h.teach(0);
  assert.equal(t.ok, true);
  assert.equal(t.generated, false);
  assert.equal(t.proposition.sourcePage, 12);
  assert.equal(t.proposition.text, 'متن موجود در کتاب');
  assert.equal(h.getStatus().propositions, 1);
});

test('AI screen surface + no network in any new module', async () => {
  const a = await createApp();
  try {
    a.go('ai');
    assert.ok(a.q('#harnessStatus'));
    assert.equal(a.qa('[data-harness-phase]').length, 4);
    assert.match(a.q('#harnessStatus').textContent, /تولید متن: خیر/);
    assert.match(a.q('#harnessStatus').textContent, /ارائهدهندهٔ خارجی: not-configured/);
    a.click(a.q('[data-harness-action="start"]'));
    assert.equal(a.app.harnessStatus().active, true);
    assert.equal(a.app.harnessStatus().phase, 'teach');
    assert.ok(a.q('[data-role="harness-message"]'), 'harness message uses an approved bubble');
    a.click(a.q('[data-harness-phase="practice"]'));
    assert.equal(a.app.harnessStatus().phase, 'practice');
  } finally { a.close(); }
  for (const rel of ['src/nodes.js', 'src/harness.js', 'src/exam-template.js',
                     'src/templates.js', 'vendor/LEARNHARNESS_INTEGRATION.md']) {
    const text = fs.readFileSync(`${APP}/${rel}`, 'utf8');
    assert.equal(/\bfetch\s*\(/.test(text), false, rel);
    assert.equal(/new\s+(?:XMLHttpRequest|WebSocket|EventSource)\b/.test(text), false, rel);
  }
});
