/**
 * Application controller — independent offline product built on the approved
 * v12.5-fa prototype. UI rendering (icons, screens, exam widgets) stays in
 * assets/proto-ui.js; this file owns state, lifecycle and the three routes.
 *
 * There is NO fetch/XHR/WebSocket anywhere in this app. Everything is local.
 */

import { createStore, memoryStorage } from './store.js';
import {
  createLessonProgress, unlockStatus, scoreSession, grant, enqueue,
  TAB_SCREENS, ROUTES,
} from './engine.js';
import { buildCurriculum, buildQuestionBank, PATHS, LEADERBOARD_PLACEHOLDER } from './fixtures.js';
import { getRoute, setRoute, setPath, planStatus, advancePlan, activatePlan, STUDY_PLAN_STAGES } from './routes.js';
import { mountViews, renderPlan, renderBank, renderLeaderboard, renderSettings, renderExamStatus, renderHarnessStatus } from './views.js';
import { createHarness } from './harness.js';
import { buildExam, buildPracticeSession, templateSummary, EXAM_TEMPLATE, PRACTICE_TEMPLATE } from './exam-template.js';
import { applyOriginalNodes, assertGeometry, NODE_SPEC } from './nodes.js';
import { STARTER_PACKAGE, STARTER_SUMMARY } from './starter-package.js';
import { mountPlus } from './plus.js';

const doc = document;
const PROTO = window.PROTO;
const faNum = (n) => String(n).replace(/\d/g, (d) => '۰۱۲۳۴۵۶۷۸۹'[+d]);

function safeStorage() {
  try {
    const probe = '__mimo_probe__';
    window.localStorage.setItem(probe, '1');
    window.localStorage.removeItem(probe);
    return window.localStorage;
  } catch (_) {
    return memoryStorage();
  }
}

const store = createStore(safeStorage());
const curriculum = buildCurriculum();
const bank = buildQuestionBank(PROTO ? PROTO.questions : []);
const phone = doc.getElementById('phone');

// Tab mapping for the screens added at runtime (the 5 approved tabs are unchanged).
if (PROTO) {
  PROTO.tabMap['study-plan'] = 'Learn';
  PROTO.tabMap['practice-bank'] = 'Practice';
}

const view = mountViews(doc, { store, bank, curriculum });
if (PROTO) PROTO.paintIcons(view.phone || doc);

// LearnHarness-compatible LOCAL teaching harness. The starter package is built
// ONLY from the approved v12.5-fa prototype fixtures (20 real stems/answers/
// explanations); nothing is generated. A user-supplied form package replaces it
// through mountContentPackage() / the AI studio importer.
let harness = createHarness({ store, contentPackage: STARTER_PACKAGE });
const geometryCheck = assertGeometry(typeof NODE !== 'undefined' ? NODE : null);

// One-click output layer: full learning path, the three token structures,
// the four-phase local AI studio, and self-contained HTML / ZIP export.
const plus = mountPlus(doc, {
  store, proto: PROTO, toast,
  harnessRef: () => harness,
  mountPackage: (pkg) => window.APP.mountContentPackage(pkg),
});

// ---------------------------------------------------------------------------
// Settings application (reproduces the prototype's own theme / mirror toggles)
// ---------------------------------------------------------------------------
function applySettings() {
  const s = store.get('settings');
  doc.body.classList.toggle('night', s.theme === 'night');
  if (phone) phone.style.direction = s.rtl ? 'rtl' : 'ltr';
  (view.phone || doc).querySelectorAll('.mimo,.exv12').forEach((el) => {
    el.style.direction = s.rtl ? 'rtl' : 'ltr';
  });
  doc.body.classList.toggle('reduce-motion', Boolean(s.reduceMotion));
}

function toast(msg) { if (PROTO) PROTO.toast(msg); }

function addHarnessBubble(text) {
  const thread = doc.getElementById('chatThread');
  if (!thread) return;
  const b = doc.createElement('div');
  b.className = 'bubble';
  b.setAttribute('data-role', 'harness-message');
  b.textContent = text;
  thread.insertBefore(b, doc.getElementById('typing'));
  thread.scrollTop = thread.scrollHeight;
}

// ---------------------------------------------------------------------------
// Learn path state: approved done / current / locked nodes, driven by real
// local lesson rows (M09 LessonProgress shape). Deterministic local unlock.
// ---------------------------------------------------------------------------
function nodeIds() {
  const pathId = store.get('route.pathId');
  return curriculum.lessonIds.filter((id) => id.startsWith(pathId)).slice(0, 6);
}

function renderLearnProgress(announce = false) {
  const nodes = doc.querySelectorAll('[data-screen="learn"] .pathwrap .node');
  if (!nodes.length) return;
  const ids = nodeIds();
  const completions = store.get('progress.tutorialCompletions') || {};
  let firstOpen = -1;
  const states = ids.map((id, i) => {
    const st = unlockStatus(id, ids, completions);
    if (st === 'open' && firstOpen < 0) firstOpen = i;
    return st;
  });
  nodes.forEach((el, i) => {
    const st = states[i] || 'locked';
    el.classList.remove('done', 'cur', 'locked', 'flash');
    el.classList.add(st === 'done' ? 'done' : st === 'open' ? 'cur' : 'locked');
    el.dataset.lessonId = ids[i] || '';
    el.dataset.state = st;
  });
  if (announce && firstOpen >= 0) {
    const el = nodes[firstOpen];
    if (el) { el.classList.add('just-unlocked'); setTimeout(() => el.classList.remove('just-unlocked'), 900); }
  }
  const card = doc.getElementById('overviewEntry');
  const bar = card && card.querySelector('.oc-bar i');
  if (bar) bar.style.width = `${Math.round((states.filter((s) => s === 'done').length / (states.length || 1)) * 100)}%`;
  // Original-Mimo node states, derived from real progress (not static markup).
  applyOriginalNodes(doc, {
    ids, completions,
    currentVariant: store.get('progress.currentLessonId') ? 'play' : 'half',
    boltIndexes: [4, 5], PROTO,
    seedStates: ['done', 'done', `cur-${store.get('progress.currentLessonId') ? 'play' : 'half'}`,
      'next', 'bolt-active', 'bolt-optional'],
  });
}

function completeCurrentLesson() {
  const ids = nodeIds();
  const completions = { ...(store.get('progress.tutorialCompletions') || {}) };
  const id = ids.find((x) => !completions[x]);
  if (!id) { toast('همهٔ گامهای نمونه انجام شدهاند'); return; }
  const lesson = curriculum.lessons.find((l) => l.id === id);
  const row = createLessonProgress({
    tutorialId: 904, sectionIndex: 1, chapterId: 17742,
    lessonId: id, trackId: 219, tries: 1, attempts: 1,
    isPracticeProgress: false,
  });
  store.push('progress.lessonRows', row);
  completions[id] = true;
  store.set('progress.tutorialCompletions', completions);
  store.set('progress.currentLessonId', id);
  store.patch('progress.unlocks', { [id]: 'done' });
  store.patch('progress.chapterCompletions', { [lesson.chapterId]: (store.get('progress.chapterCompletions') || {})[lesson.chapterId] || 1 });
  enqueue(store.state, { type: 'lesson_progress', lessonId: id });
  grant(store.state, { coins: 0, xp: 0, reason: 'local-lesson-complete' });
  renderLearnProgress(true);
  toast(`گام ${faNum(ids.indexOf(id) + 1)} تکمیل شد · گام بعدی باز شد`);
}

// ---------------------------------------------------------------------------
// Practice sessions (question bank + prototype's isolated section practice)
// ---------------------------------------------------------------------------
let bankFilter = 'all';

function activeSession() {
  let s = store.get('practice.active');
  if (!s) {
    s = { id: `ps-${Date.now()}`, filter: bankFilter, answers: {}, startedAt: Date.now() };
    store.set('practice.active', s);
  }
  return s;
}

function visibleBankQuestions() {
  return bank.filter((q) => bankFilter === 'all' || q.subject === bankFilter);
}

function finishBankSession() {
  const s = activeSession();
  const questions = visibleBankQuestions();
  const result = scoreSession(questions, s.answers);
  const template = buildPracticeSession('bank', questions);
  const record = {
    id: s.id, kind: 'question-bank', filter: bankFilter,
    template: { id: template.id, mode: template.mode, timed: template.timed,
      answeringComponents: template.answeringComponents },
    questionIds: questions.map((q) => q.id), answers: s.answers,
    result, finishedAt: Date.now(), placeholder: true,
  };
  store.push('practice.sessions', record);
  store.set('practice.active', null);
  store.set('practice.bankCursor', (store.get('practice.bankCursor') || 0) + questions.length);
  const out = doc.getElementById('bankResult');
  if (out) out.innerHTML = `<div class="sp-fb"><b>${faNum(result.correct)} / ${faNum(result.total)}</b> پاسخ ثبت شد · ${faNum(result.percent)}٪ درست · نشست بهصورت محلی ذخیره شد</div>`;
  renderBank(doc, { bank, filter: bankFilter, answers: {} });
  toast(`نشست تمرینی ذخیره شد · ${faNum(result.correct)} پاسخ درست`);
}

function recordSectionPractice() {
  const rows = [...doc.querySelectorAll('#practiceQuestions .sp-q')];
  const questions = rows.map((r, i) => ({ id: `sp-${i}`, correctId: i % 4 }));
  const answers = {};
  rows.forEach((r, i) => {
    const sel = r.querySelector('.sp-opt.on');
    if (sel) answers[`sp-${i}`] = Number(sel.dataset.o) - 1;
  });
  const result = scoreSession(questions, answers);
  const template = buildPracticeSession('chapter', questions);
  store.push('practice.sessions', {
    id: `sp-${Date.now()}`, kind: 'section-practice',
    template: { id: template.id, mode: template.mode, timed: false }, scope: doc.getElementById('spScope')?.textContent || '',
    questionIds: questions.map((q) => q.id), answers, result,
    finishedAt: Date.now(), placeholder: true,
  });
  enqueue(store.state, { type: 'practice_session', result });
}

// ---------------------------------------------------------------------------
// Exam lifecycle recording (the exam interaction itself is the prototype's)
// ---------------------------------------------------------------------------
let lastResultAt = 0;
let booting = true; // do not record a bogus result while restoring a saved screen
function recordExamResult() {
  if (!PROTO) return;
  if (Date.now() - lastResultAt < 1200) return;
  lastResultAt = Date.now();
  const snap = PROTO.examState();
  const pct = doc.getElementById('resPct')?.textContent || '—';
  store.push('exam.results', {
    id: `ex-${Date.now()}`, title: snap.exam, kind: snap.kind, qi: snap.qi,
    answers: snap.answers, percentLabel: pct, finishedAt: Date.now(), placeholder: true,
  });
  store.set('exam.status', 'finished');
  store.set('exam.activeKind', snap.kind);
  const n = (store.get('economy.examsTaken') || 0) + 1;
  store.set('economy.examsTaken', n);
  toast('نتیجهٔ آزمون بهصورت محلی ذخیره شد');
}

// ---------------------------------------------------------------------------
// Navigation hook: persists last screen/tab, refreshes dynamic views, animates
// ---------------------------------------------------------------------------
function onNavigate(name) {
  const tab = (PROTO && PROTO.tabMap[name]) || 'Learn';
  const history = [...(store.get('navigation.history') || []), name].slice(-20);
  store.patch('navigation', { screen: name, tab, history });
  doc.querySelectorAll('[data-route]').forEach((b) => b.classList.toggle('on', b.dataset.route === store.get('route.mode')));
  if (name === 'study-plan') renderPlan(doc, store);
  if (name === 'practice-bank') {
    bankFilter = store.get('practice.active')?.filter || bankFilter;
    renderBank(doc, { bank, filter: bankFilter, answers: store.get('practice.active')?.answers || {} });
  }
  if (name === 'leaderboard') {
    renderLeaderboard(doc, { state: store.get('leaderboard.view') || 'weekly', rows: LEADERBOARD_PLACEHOLDER });
    store.set('leaderboard.lastViewedAt', Date.now());
  }
  if (name === 'profile') renderSettings(doc, store);
  if (name === 'ai') renderHarnessStatus(doc, harness.getStatus());
  if (name === 'learn') renderLearnProgress(false);
  if (name === 'exam-hub') {
    const saved = store.get('exam.saved');
    if (PROTO && saved) PROTO.setSaved(saved);
    renderExamStatus(doc, store);
  }
  if (name === 'exam-result' && !booting) recordExamResult();
  const active = doc.querySelector('.screen.on');
  if (active) {
    active.classList.remove('screen-enter');
    void active.offsetWidth; // restart the additive transition
    active.classList.add('screen-enter');
  }
}

window.PROTO_NAV = (name) => { onNavigate(name); if (plus && plus.onNavigate) plus.onNavigate(name); };
window.PROTO_PERSIST = (snapshot) => {
  store.set('exam.saved', snapshot);
  store.set('exam.status', snapshot ? 'paused' : 'idle');
  if (snapshot) toast('پیشرفت آزمون در حافظهٔ دستگاه ذخیره شد');
};

// ---------------------------------------------------------------------------
// Interaction delegation (runs alongside the prototype's own handlers)
// ---------------------------------------------------------------------------
doc.addEventListener('click', (e) => {
  const examRow = e.target.closest('.nodek[data-exam]');
  if (examRow) {
    const built = buildExam(examRow.dataset.kind || 'comprehensive', bank);
    if (built) {
      store.set('exam.activeTemplate', built);
      toast(`قالب ${built.titleFa} · ${faNum(built.questionIds.length)} سؤال · ${faNum(built.minutes)} دقیقه`);
    }
  }
  const harnessAction = e.target.closest('[data-harness-action]');
  if (harnessAction) {
    const input = doc.getElementById('aiInput');
    const goal = (input && input.value.trim()) || 'زیستشناسی دوازدهم';
    const res = harness.start(goal);
    if (res.ok) { harness.plan(80); harness.setPhase('teach'); }
    addHarnessBubble(res.ok
      ? `LearnHarness · جلسه «${goal}» شروع شد · فاز آموزش · ${harness.getStatus().steps} گام از منابع موجود (بدون تولید متن)`
      : 'برای شروع جلسه، هدف یادگیری را بنویسید.');
    renderHarnessStatus(doc, harness.getStatus());
    return;
  }
  const hp = e.target.closest('[data-harness-phase]');
  if (hp) {
    harness.setPhase(hp.dataset.harnessPhase);
    renderHarnessStatus(doc, harness.getStatus());
    toast(`فاز LearnHarness: ${hp.textContent}`);
    return;
  }
  const modeBtn = e.target.closest('#mode button');
  if (modeBtn) {
    harness.setPhase(modeBtn.dataset.mode === 'PRACTICE' ? 'practice' : 'teach');
    renderHarnessStatus(doc, harness.getStatus());
  }
  const routeChip = e.target.closest('[data-route]');
  if (routeChip) {
    const r = setRoute(store, routeChip.dataset.route);
    if (r) {
      doc.querySelectorAll('[data-route]').forEach((b) => b.classList.toggle('on', b.dataset.route === r.key));
      if (PROTO) PROTO.go(r.entry);
      renderPlan(doc, store);
      toast(`مسیر «${r.fa}» انتخاب شد · ${r.description}`);
    }
    return;
  }
  const planPath = e.target.closest('[data-plan-path]');
  if (planPath) {
    setPath(store, planPath.dataset.planPath);
    store.patch('route.studyPlan', { programId: planPath.dataset.planPath });
    renderPlan(doc, store);
    renderLearnProgress(false);
    const p = PATHS.find((x) => x.id === planPath.dataset.planPath);
    const t = doc.getElementById('learnPathTitle');
    if (t && p) t.textContent = p.fa;
    toast(`مسیر «${p ? p.fa : ''}» انتخاب شد`);
    return;
  }
  const planAction = e.target.closest('#planAction');
  if (planAction) {
    const { plan, next } = planStatus(store);
    if (!plan.active) {
      const p = plan.programId || store.get('route.pathId') || 'grade12';
      activatePlan(store, p);
      toast('برنامه فعال شد · وضعیت گامها ذخیره شد');
    } else if (next) {
      const stage = STUDY_PLAN_STAGES.find((s) => s.key === next);
      const res = advancePlan(store, next);
      if (res.ok) toast(stage?.implemented ? `وضعیت: ${stage.fa}` : `ساختار «${stage?.fa}» رزرو شد — هنوز اجرا نمیشود`);
    } else toast('برنامه در آخرین گام ساختاری است');
    renderPlan(doc, store);
    return;
  }
  const planStage = e.target.closest('[data-plan-stage]');
  if (planStage) {
    const st = STUDY_PLAN_STAGES.find((s) => s.key === planStage.dataset.planStage);
    if (st) toast(`${st.fa} · ${st.detail}`);
    return;
  }
  const bankFilterBtn = e.target.closest('[data-bank-filter]');
  if (bankFilterBtn) {
    bankFilter = bankFilterBtn.dataset.bankFilter;
    const s = activeSession();
    store.patch('practice.active', { filter: bankFilter });
    renderBank(doc, { bank, filter: bankFilter, answers: s.answers || {} });
    return;
  }
  const bankOpt = e.target.closest('[data-bank-opt]');
  if (bankOpt) {
    const q = bankOpt.closest('[data-bank-q]');
    if (!q) return;
    const s = activeSession();
    const answers = { ...(s.answers || {}), [q.dataset.bankQ]: Number(bankOpt.dataset.bankOpt) };
    store.patch('practice.active', { answers });
    renderBank(doc, { bank, filter: bankFilter, answers });
    return;
  }
  if (e.target.closest('#bankStart')) { finishBankSession(); return; }
  const lbState = e.target.closest('[data-lb-state]');
  if (lbState) {
    const s = lbState.dataset.lbState;
    store.set('leaderboard.view', s);
    renderLeaderboard(doc, { state: s, rows: LEADERBOARD_PLACEHOLDER });
    toast(`نمای لیدربورد: ${lbState.textContent} · دادهٔ محلی آزمایشی`);
    return;
  }
  const setting = e.target.closest('[data-setting]');
  if (setting) {
    const key = setting.dataset.setting;
    const cur = store.get(`settings.${key}`);
    const next = typeof cur === 'boolean' ? !cur : (cur === 'night' ? 'day' : 'night');
    store.set(`settings.${key}`, next);
    applySettings();
    renderSettings(doc, store);
    toast(`تنظیم «${setting.closest('.selfrow')?.querySelector('span')?.textContent || key}» ذخیره شد`);
    return;
  }
  if (e.target.closest('[data-goal]')) {
    const options = [15, 30, 45, 60];
    const cur = store.get('settings.dailyGoal');
    const next = options[(options.indexOf(cur) + 1) % options.length];
    store.set('settings.dailyGoal', next);
    renderSettings(doc, store);
    toast(`هدف روزانه: ${faNum(next)} دقیقه`);
    return;
  }
  if (e.target.closest('#settingsExport')) {
    try {
      const blob = new Blob([JSON.stringify(store.export(), null, 2)], { type: 'application/json' });
      const url = URL.createObjectURL(blob);
      const a = doc.createElement('a');
      a.href = url; a.download = 'mimo-offline-state.json'; a.click();
      setTimeout(() => URL.revokeObjectURL(url), 2000);
      toast('خروجی وضعیت محلی ساخته شد');
    } catch (_) { toast('خروجی در این محیط پشتیبانی نمیشود'); }
    return;
  }
  if (e.target.closest('#settingsReset')) {
    if (window.confirm('همهٔ دادههای محلی پاک شوند؟')) {
      store.reset();
      applySettings();
      toast('دادههای محلی بازنشانی شدند');
      setTimeout(() => window.location.reload(), 400);
    }
    return;
  }
  if (e.target.closest('.lesson .continue-btn')) { completeCurrentLesson(); return; }
  if (e.target.closest('#startLearning')) {
    store.set('progress.currentLessonId', nodeIds()[0] || null);
    return;
  }
  if (e.target.closest('#timerStart')) { store.set('exam.status', 'running'); return; }
  if (e.target.closest('#timerPause')) {
    store.set('exam.status', store.get('exam.status') === 'paused' ? 'running' : 'paused');
    return;
  }
  if (e.target.closest('#resumeBtn')) { store.set('exam.status', 'paused'); return; }
  const tab = e.target.closest('#tabs .tab');
  if (tab) {
    store.patch('navigation', { tab: tab.dataset.tab });
    return;
  }
}, true);

// Prototype's section-practice button: record the session in capture phase so
// the selected options are still in the DOM when we read them.
doc.addEventListener('click', (e) => {
  if (e.target.closest('#practiceStart')) recordSectionPractice();
}, true);

// AI thread persistence (local only; no AI teacher, no network, no fake reply).
doc.addEventListener('click', (e) => {
  if (e.target.closest('#aiSend')) {
    const input = doc.getElementById('aiInput');
    const text = input ? input.value.trim() : '';
    if (text) {
      store.push('ai.threads', { id: `m-${Date.now()}`, role: 'user', text, at: Date.now(), local: true });
      // Make sure the four-phase local session exists before teaching: the chat
      // input doubles as a diagnostic goal (still no network, no generated text).
      const hst = harness.getStatus();
      if (!hst.active || !(harness.state.plan || []).length) { harness.start(text); harness.plan(60); }
      const step = harness.teach();
      addHarnessBubble(step.ok
        ? `LearnHarness · ${step.proposition.text} (از منبع موجود، بدون تولید متن)`
        : (step.message || 'منبعی در فرم اطلاعاتی ثبت نشده است.'));
      renderHarnessStatus(doc, harness.getStatus());
      toast('گفتگو بهصورت محلی ذخیره شد (بدون سرویس هوش مصنوعی)');
    }
  }
  if (e.target.closest('#newChat')) {
    store.push('ai.threads', { id: `t-${Date.now()}`, role: 'system', text: 'new-chat', at: Date.now(), local: true });
  }
}, true);

// Persist on lifecycle events; localStorage writes are synchronous, this is a
// belt-and-braces flush for browsers that defer unload work.
window.addEventListener('pagehide', () => store.flush());
doc.addEventListener('visibilitychange', () => { if (doc.visibilityState === 'hidden') store.flush(); });

// ---------------------------------------------------------------------------
// Boot / lifecycle recovery
// ---------------------------------------------------------------------------
function restore() {
  bankFilter = store.get('practice.active')?.filter || bankFilter;
  applySettings();
  renderSettings(doc, store);
  renderPlan(doc, store);
  renderBank(doc, { bank, filter: bankFilter, answers: store.get('practice.active')?.answers || {} });
  renderLeaderboard(doc, { state: store.get('leaderboard.view') || 'weekly', rows: LEADERBOARD_PLACEHOLDER });
  renderExamStatus(doc, store);
  renderHarnessStatus(doc, harness.getStatus());
  renderLearnProgress(false);

  const saved = store.get('exam.saved');
  if (saved && PROTO) {
    PROTO.setSaved(saved);
    store.set('exam.status', 'paused');
  }

  const p = PATHS.find((x) => x.id === store.get('route.pathId'));
  const title = doc.getElementById('learnPathTitle');
  if (p && title) title.textContent = p.fa;
  doc.querySelectorAll('[data-route]').forEach((b) => b.classList.toggle('on', b.dataset.route === store.get('route.mode')));
  doc.querySelectorAll('[data-plan-path]').forEach((b) => b.classList.toggle('on', b.dataset.planPath === store.get('route.pathId')));

  // Restore the last screen; exam-run is only safe with a saved snapshot.
  let screen = store.get('navigation.screen') || 'learn';
  const known = [...doc.querySelectorAll('.screen')].some((s) => s.dataset.screen === screen);
  if (!known || (screen === 'exam-run' && !saved)) screen = 'exam-hub';
  if (screen === 'exam-result' && !(store.get('exam.results') || []).length) screen = 'exam-hub';
  if (PROTO) PROTO.go(screen);
  else onNavigate(screen);
  booting = false;

  if (saved) toast('آزمون ذخیرهشده پیدا شد · از نوار «ادامهٔ آزمون» استفاده کنید');
}

restore();

// Public, read-only-ish debug/test surface. Tests use it to drive the app.
window.APP = {
  store, curriculum, bank, view, proto: PROTO,
  harness, harnessStatus: () => harness.getStatus(),
  examTemplate: EXAM_TEMPLATE, practiceTemplate: PRACTICE_TEMPLATE,
  templateSummary: () => templateSummary(),
  nodeSpec: NODE_SPEC, geometryCheck,
  mountContentPackage(pkg) {
    harness = createHarness({ store, contentPackage: pkg });
    window.APP.harness = harness;
    renderHarnessStatus(doc, harness.getStatus());
    if (plus && plus.aiStudio) plus.aiStudio.render();
    return harness.getStatus();
  },
  harnessRef: () => harness,
  plus,
  economy: plus ? plus.economy : null,
  learningPath: plus ? plus.learningPath : null,
  aiStudio: plus ? plus.aiStudio : null,
  outputKit: plus ? plus.outputKit : null,
  starter: STARTER_SUMMARY,
  routes: ROUTES, tabs: TAB_SCREENS,
  go: (name) => (PROTO ? PROTO.go(name) : onNavigate(name)),
  renderPlan: () => renderPlan(doc, store),
  renderBank: () => renderBank(doc, { bank, filter: bankFilter, answers: store.get('practice.active')?.answers || {} }),
  renderLearnProgress,
  renderExamStatus: () => renderExamStatus(doc, store),
  completeCurrentLesson,
  finishBankSession,
  restore,
  version: '1.0.0-offline+one-click',
};
