import test from 'node:test';
import assert from 'node:assert/strict';
import { createStore, memoryStorage, SCHEMA_VERSION, STORAGE_KEY } from '../src/store.js';
import {
  isSolvedCorrectly, createLessonProgress, validateSelection, validateOrdered,
  scoreSession, unlockStatus, chapterCompletion, grant, enqueue, TAB_SCREENS, ROUTES,
} from '../src/engine.js';
import { buildCurriculum, buildQuestionBank, PATHS, EXAM_KINDS, PLACEHOLDER } from '../src/fixtures.js';
import { setRoute, activatePlan, advancePlan, planStatus, STUDY_PLAN_STAGES, getRoute } from '../src/routes.js';

const fresh = () => createStore(memoryStorage(), () => 1000);

test('store: defaults, dotted access, mutation and restart recovery', () => {
  const storage = memoryStorage();
  const a = createStore(storage, () => 1000);
  assert.equal(a.get('schemaVersion'), SCHEMA_VERSION);
  assert.equal(a.get('meta.serverConfirmed'), false);
  assert.equal(a.get('economy.coins'), 1272);
  a.set('settings.theme', 'night');
  a.patch('route', { mode: 'study-plan' });
  a.push('practice.sessions', { id: 'ps-1', placeholder: true });
  a.push('progress.lessonRows', { lessonId: 'l1', tries: 1, inQueue: true });

  const b = createStore(storage, () => 2000); // simulates close + reopen
  assert.equal(b.get('settings.theme'), 'night');
  assert.equal(b.get('route.mode'), 'study-plan');
  assert.equal(b.get('practice.sessions').length, 1);
  assert.equal(b.get('progress.lessonRows')[0].lessonId, 'l1');
  assert.equal(b.get('createdAt'), 1000);
  assert.equal(b.get('meta.serverConfirmed'), false); // capability flags never trusted from disk
});

test('store: corrupt payload and unknown keys never break boot', () => {
  const storage = memoryStorage();
  storage.setItem(STORAGE_KEY, '{not json');
  const a = createStore(storage, () => 1);
  assert.equal(a.get('schemaVersion'), SCHEMA_VERSION);
  assert.match(String(a.corruption), /./);
  a.import({ schemaVersion: 999, economy: 'broken', route: { mode: 'nonsense' },
    navigation: { screen: 'profile' }, unknownKey: 42 });
  assert.equal(a.get('schemaVersion'), SCHEMA_VERSION);
  assert.equal(a.get('route.mode'), 'direct');
  assert.equal(a.get('navigation.screen'), 'profile');
  assert.equal(a.get('economy.coins'), 1272);
  assert.equal(a.get('unknownKey'), undefined);
});

test('store: reset clears durable state; subscribe observes writes', () => {
  const storage = memoryStorage();
  const s = createStore(storage, () => 1);
  let seen = 0;
  s.subscribe(() => { seen += 1; });
  s.set('settings.rtl', true);
  assert.equal(seen, 1);
  s.reset();
  assert.equal(s.get('settings.rtl'), false);
  assert.ok(seen >= 2);
});

test('engine: M09-verified local formulas', () => {
  assert.equal(isSolvedCorrectly({ tries: 1 }), true);
  assert.equal(isSolvedCorrectly({ tries: 0 }), false);
  assert.equal(isSolvedCorrectly(null), false);
  const row = createLessonProgress({ tutorialId: 904, chapterId: 17742, lessonId: 'L', trackId: 219 });
  for (const key of ['id', 'tutorialId', 'sectionIndex', 'chapterId', 'lessonId', 'trackId',
    'tries', 'attempts', 'isPracticeProgress', 'inQueue', 'publishSetVersion', 'createdAt']) {
    assert.ok(Object.hasOwn(row, key), key);
  }
  assert.equal(row.inQueue, true);
  assert.equal(row.publishSetVersion, 753);
  const options = [{ id: 0, isCorrect: false }, { id: 1, isCorrect: true }];
  assert.equal(validateSelection([1], options), true);
  assert.equal(validateSelection([0, 1], options), false);
  assert.equal(validateOrdered(['a', 'b'], ['a', 'b']), true);
  assert.equal(validateOrdered(['b', 'a'], ['a', 'b']), false);
});

test('engine: scoring, sequential unlock, chapter completion, ledger', () => {
  const qs = [{ id: 'a', correctId: 1 }, { id: 'b', correctId: 0 }, { id: 'c', correctId: 2 }];
  const r = scoreSession(qs, { a: 1, b: 3 });
  assert.deepEqual(r, { total: 3, answered: 2, correct: 1, wrong: 1, blank: 1, percent: 50 });
  const ids = ['l1', 'l2', 'l3'];
  assert.equal(unlockStatus('l1', ids, {}), 'open');
  assert.equal(unlockStatus('l2', ids, {}), 'locked');
  assert.equal(unlockStatus('l2', ids, { l1: true }), 'open');
  assert.equal(unlockStatus('l1', ids, { l1: true }), 'done');
  const rows = [{ chapterId: 'c1', tries: 1 }, { chapterId: 'c1', tries: 0 }, { chapterId: 'c2', tries: 1 }];
  assert.deepEqual(chapterCompletion(rows, 'c1'), { rows: 2, solved: 1, ratio: 0.5 });
  const s = fresh();
  grant(s.state, { coins: 5, xp: 10, reason: 'test' });
  enqueue(s.state, { type: 'lesson_progress' });
  assert.equal(s.state.economy.coins, 1277);
  assert.equal(s.state.syncQueue.length, 2);
  assert.ok(s.state.syncQueue.every((x) => x.status === 'local-only'));
});

test('engine: exactly three routes and exactly five tabs (no Max)', () => {
  assert.deepEqual(Object.keys(ROUTES), ['direct', 'exam', 'study-plan']);
  assert.deepEqual(Object.keys(TAB_SCREENS), ['Learn', 'Practice', 'AI', 'Leaderboard', 'Profile']);
  assert.equal(TAB_SCREENS.Practice, 'exam-hub');
});

test('fixtures: placeholder graph uses M09 shape, no content is fabricated', () => {
  const c = buildCurriculum();
  assert.equal(c.tracks.length, 3);
  assert.equal(c.sections.length, 9);
  assert.equal(c.chapters.length, 27);
  assert.equal(c.lessons.length, 108);
  assert.equal(c.lessonIds.length, 108);
  assert.equal(new Set(c.lessonIds).size, 108);
  assert.equal(c.meta.contentReady, false);
  assert.equal(c.meta.serverConfirmed, false);
  assert.ok(c.lessons.every((l) => l.placeholder && l.chapterId && l.trackId));
  assert.equal(PATHS.length, 3);
  assert.equal(EXAM_KINDS.length, 7);
  assert.equal(PLACEHOLDER.tag, 'PLACEHOLDER');
  const bank = buildQuestionBank([
    { sub: 'زیست · تست', stem: 'سؤال نمونه', opts: ['۱', '۲', '۳', '۴'], ok: 2, expl: 'توضیح نمونه' },
  ]);
  assert.equal(bank.length, 1);
  assert.equal(bank[0].correctId, 2);
  assert.equal(bank[0].options[2].isCorrect, true);
  assert.equal(bank[0].placeholder, true);
});

test('routes: mode switching, study-plan transitions and invalid edges', () => {
  const s = fresh();
  assert.equal(getRoute(s).key, 'direct');
  assert.equal(setRoute(s, 'exam').entry, 'exam-hub');
  assert.equal(setRoute(s, 'study-plan').entry, 'study-plan');
  assert.equal(setRoute(s, 'bogus'), null);
  assert.equal(getRoute(s).key, 'study-plan');
  activatePlan(s, 'grade12');
  assert.equal(planStatus(s).stage.key, 'not-started');
  assert.equal(advancePlan(s, 'completed').ok, false); // skipping stages is not allowed
  assert.equal(advancePlan(s, 'initial-exam').ok, true);
  assert.equal(advancePlan(s, 'remediation').ok, true);
  assert.equal(advancePlan(s, 'final-exam').ok, true);
  assert.equal(advancePlan(s, 'completed').ok, true);
  assert.equal(planStatus(s).index, STUDY_PLAN_STAGES.length - 1);
  assert.equal(s.get('route.studyPlan.programId'), 'grade12');
});
