import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import { createApp, APP } from './harness.mjs';

const SCREENS = ['learn', 'select-path', 'path-overview', 'section-detail', 'lesson',
  'leaderboard', 'user-profile', 'profile', 'exam-hub', 'exam-run', 'exam-result',
  'ai', 'section-practice', 'study-plan', 'practice-bank'];

test('acceptance: real app boots, every page is reachable, 5 tabs only', async () => {
  const a = await createApp();
  try {
    assert.ok(a.w.APP, 'window.APP must exist');
    assert.ok(a.w.PROTO, 'window.PROTO renderer must exist');
    const present = a.qa('.screen').map((s) => s.dataset.screen);
    for (const s of SCREENS) assert.ok(present.includes(s), `missing screen ${s}`);
    assert.deepEqual(a.qa('#tabs .tab').map((t) => t.dataset.tab),
      ['Learn', 'Practice', 'AI', 'Leaderboard', 'Profile']);
    assert.equal(a.qa('#tabs .tab').length, 5);

    // Every approved + new screen can be shown and the active tab follows.
    for (const s of SCREENS) {
      a.go(s);
      assert.equal(a.proto.currentScreen(), s, `cannot reach ${s}`);
      assert.equal(a.qa('.screen.on').length, 1, `more than one active screen on ${s}`);
      assert.equal(a.app.store.get('navigation.screen'), s, `navigation not persisted for ${s}`);
    }
    // All five bottom-bar tabs navigate to their approved landing screen.
    const landings = { Learn: 'learn', Practice: 'exam-hub', AI: 'ai',
      Leaderboard: 'leaderboard', Profile: 'profile' };
    for (const [tab, screen] of Object.entries(landings)) {
      a.click(a.q(`#tabs .tab[data-tab="${tab}"]`));
      assert.equal(a.proto.currentScreen(), screen);
      assert.ok(a.q(`#tabs .tab[data-tab="${tab}"]`).classList.contains('on'));
      assert.equal(a.app.store.get('navigation.tab'), tab);
    }
    assert.equal(a.qa('svg.ic').length > 100, true, 'approved SVG icons must be painted');
  } finally { a.close(); }
});

test('acceptance: Learn path — enter path, change lesson states, unlock feedback', async () => {
  const a = await createApp();
  try {
    a.go('learn');
    const nodes = a.qa('[data-screen="learn"] .pathwrap .node');
    assert.equal(nodes.length, 6);
    assert.equal(nodes[0].dataset.state, 'done', 'original-Mimo baseline: completed node');
    assert.equal(nodes[1].dataset.state, 'done');
    assert.equal(nodes[2].dataset.state, 'cur-half');
    assert.equal(nodes[4].dataset.state, 'bolt-active');
    assert.ok(a.q('.gloss-fab'), 'original-Mimo floating dictionary affordance restored');
    a.click(a.q('#pathSwitchBtn'));
    assert.equal(a.proto.currentScreen(), 'select-path');
    assert.equal(a.qa('[data-route]').length, 3);
    a.click(a.q('[data-route="direct"]'));
    assert.equal(a.app.store.get('route.mode'), 'direct');

    a.click(a.q('#curNode'));
    assert.ok(a.q('#chapterModal').classList.contains('on'), 'chapter modal opens');
    a.click(a.q('#startLearning'));
    assert.equal(a.proto.currentScreen(), 'lesson');
    assert.ok(a.app.store.get('progress.currentLessonId'));

    a.click(a.q('.lesson .continue-btn'));
    const rows = a.app.store.get('progress.lessonRows');
    assert.equal(rows.length, 1);
    assert.equal(rows[0].inQueue, true);
    assert.equal(rows[0].isPracticeProgress, false);
    assert.equal(rows[0].publishSetVersion, 753);
    assert.ok(a.app.store.get('progress.tutorialCompletions')[rows[0].lessonId]);
    const ns = a.qa('[data-screen="learn"] .pathwrap .node');
    assert.equal(ns[0].dataset.state, 'done');
    assert.ok(['cur-play', 'cur-half'].includes(ns[1].dataset.state), 'next lesson becomes current');
  } finally { a.close(); }
});

test('acceptance: Practice — question bank, answering components, session persistence', async () => {
  const a = await createApp();
  try {
    a.click(a.q('#tabs .tab[data-tab="Practice"]'));
    assert.equal(a.proto.currentScreen(), 'exam-hub');
    assert.ok(a.q('[data-role="bank-entry"]'), 'bank entry exists on Practice landing');
    a.click(a.q('[data-role="bank-entry"] [data-nav="practice-bank"]'));
    assert.equal(a.proto.currentScreen(), 'practice-bank');
    const all = a.qa('#bankList .sp-q').length;
    assert.ok(all >= 15, `placeholder bank must expose the prototype fixture questions, got ${all}`);

    a.click(a.q('[data-bank-filter="زیست"]'));
    const filtered = a.qa('#bankList .sp-q').length;
    assert.ok(filtered > 0 && filtered < all, 'subject filter is functional');
    assert.equal(a.app.store.get('practice.active.filter'), 'زیست');

    a.click(a.q('#bankList [data-bank-opt="0"]'));
    assert.deepEqual(Object.keys(a.app.store.get('practice.active.answers')).length, 1);
    assert.ok(a.q('#bankList .sp-opt.on'), 'selected answer is reflected in the UI');

    a.click(a.q('#bankStart'));
    assert.equal(a.app.store.get('practice.sessions').length, 1);
    assert.equal(a.app.store.get('practice.active'), null);
    assert.match(a.q('#bankResult').textContent, /نشست/);

    // The prototype's isolated section-practice screen also records a session.
    a.go('section-practice');
    const q = a.q('#practiceQuestions .sp-q');
    if (q) a.click(q.querySelector('.sp-opt'));
    a.click(a.q('#practiceStart'));
    assert.equal(a.app.store.get('practice.sessions').length, 2);
    assert.equal(a.app.store.get('practice.sessions')[1].kind, 'section-practice');
  } finally { a.close(); }
});

test('acceptance: full placeholder Exam cycle — timer, answering, result, status, save', async () => {
  const a = await createApp();
  try {
    a.go('exam-hub');
    assert.ok(a.q('#examStatusLine'), 'exam status surface is visible');
    assert.match(a.q('#examStatusLine').textContent, /وضعیت آزمون/);
    a.click(a.q('.nodek[data-exam]'));
    assert.equal(a.proto.currentScreen(), 'exam-run');
    assert.equal(a.app.store.get('exam.status') === 'idle' || a.app.store.get('exam.status') === 'paused', true);
    assert.equal(a.q('#examTitle').textContent.length > 0, true);
    assert.equal(a.qa('#exChoices .opt').length, 4, 'exam answering components present');

    a.click(a.q('#timerChip'));
    assert.ok(a.q('#timerSheet').classList.contains('on'), 'timer sheet opens');
    a.click(a.q('#timerStart'));
    assert.equal(a.app.store.get('exam.status'), 'running');

    a.click(a.q('#exChoices .opt'));
    a.click(a.q('#nextQ'));              // first click: بررسی پاسخ
    a.click(a.q('#nextQ'));              // second click: ادامه
    assert.match(a.q('#examStep').textContent, /۲|2/, 'question index advances');

    a.click(a.q('#exitSaveBtn'));        // خروج و ذخیره
    const saved = a.app.store.get('exam.saved');
    assert.ok(saved, 'saved exam snapshot persisted');
    assert.equal(saved.kind, 'comprehensive');
    assert.equal(a.app.store.get('exam.status'), 'paused');
    assert.equal(a.q('#resumeBar').hidden, false);

    // finish a run through the palette sheet -> result screen
    a.click(a.q('#submitExam'));
    assert.equal(a.proto.currentScreen(), 'exam-result');
    assert.equal(a.app.store.get('exam.results').length, 1);
    assert.equal(a.app.store.get('exam.status'), 'finished');
    assert.equal(a.app.store.get('exam.saved'), null, 'finished run clears the snapshot');
    assert.ok(a.q('#resPct').textContent.length > 0);
  } finally { a.close(); }
});

test('acceptance: Study-Plan route — path/status, stage structure, no fake implementation', async () => {
  const a = await createApp();
  try {
    a.click(a.q('#pathSwitchBtn'));
    a.click(a.q('[data-route="study-plan"]'));
    assert.equal(a.proto.currentScreen(), 'study-plan');
    assert.equal(a.app.store.get('route.mode'), 'study-plan');
    assert.equal(a.qa('[data-plan-stage]').length, 5, 'five declared plan stages');
    assert.match(a.q('[data-screen="study-plan"] .banner.warn').textContent, /آزمایشی/);

    a.click(a.q('[data-plan-path="grade11"]'));
    assert.equal(a.app.store.get('route.pathId'), 'grade11');
    assert.match(a.q('#planTitle').textContent, /یازدهم/);

    a.click(a.q('#planAction'));   // activate
    assert.equal(a.app.store.get('route.studyPlan.active'), true);
    a.click(a.q('#planAction'));   // advance to reserved initial-exam structure
    assert.equal(a.app.store.get('route.studyPlan.stage'), 'initial-exam');
  } finally { a.close(); }
});

test('acceptance: Profile/settings, Leaderboard states, AI local thread', async () => {
  const a = await createApp();
  try {
    a.click(a.q('#tabs .tab[data-tab="Profile"]'));
    assert.equal(a.proto.currentScreen(), 'profile');
    a.click(a.q('.gear'));
    assert.ok(a.q('#settingsModal').classList.contains('on'));
    a.click(a.q('[data-setting="theme"]'));
    assert.equal(a.app.store.get('settings.theme'), 'night');
    assert.ok(a.w.document.body.classList.contains('night'));
    a.click(a.q('[data-setting="rtl"]'));
    assert.equal(a.app.store.get('settings.rtl'), true);
    assert.equal(a.q('#phone').style.direction, 'rtl');
    a.click(a.q('[data-goal]'));
    assert.equal(a.app.store.get('settings.dailyGoal'), 30);

    a.click(a.q('#tabs .tab[data-tab="Leaderboard"]'));
    a.click(a.q('[data-lb-state="empty"]'));
    assert.equal(a.app.store.get('leaderboard.view'), 'empty');
    assert.match(a.q('#leaderboardRows').textContent, /دادهای برای نمایش نیست/);
    a.click(a.q('[data-lb-state="all"]'));
    assert.ok(a.qa('#leaderboardRows .lb-row').length >= 3);

    a.click(a.q('#tabs .tab[data-tab="AI"]'));
    a.q('#aiInput').value = 'پیام آزمایشی';
    a.click(a.q('#aiSend'));
    assert.equal(a.app.store.get('ai.threads').length, 1);
    assert.equal(a.app.store.get('ai.threads')[0].local, true);
  } finally { a.close(); }
});

test('acceptance: restart recovery — settings, route, progress, exam, sessions, navigation', async () => {
  const a = await createApp();
  let seed;
  try {
    a.click(a.q('#tabs .tab[data-tab="Profile"]'));
    a.click(a.q('.gear'));
    a.click(a.q('[data-setting="theme"]'));            // night
    a.click(a.q('#pathSwitchBtn'));
    a.click(a.q('[data-route="study-plan"]'));
    a.click(a.q('#planAction'));                        // activate plan
    a.go('learn');
    a.click(a.q('#curNode'));
    a.click(a.q('#startLearning'));
    a.click(a.q('.lesson .continue-btn'));             // finish one lesson
    a.go('practice-bank');
    a.click(a.q('#bankList [data-bank-opt="1"]'));
    a.click(a.q('#bankStart'));                        // one practice session
    a.go('exam-hub');
    a.click(a.q('.nodek[data-exam]'));
    a.click(a.q('#exChoices .opt'));
    a.click(a.q('#exitSaveBtn'));                      // saved exam
    a.go('select-path');
    seed = a.snapshot();
    assert.ok(seed && seed.length > 500);
  } finally { a.close(); }

  const b = await createApp({ seed });
  try {
    assert.equal(b.app.store.get('settings.theme'), 'night');
    assert.ok(b.w.document.body.classList.contains('night'), 'theme must be re-applied on boot');
    assert.equal(b.app.store.get('route.mode'), 'study-plan');
    assert.equal(b.app.store.get('route.studyPlan.active'), true);
    assert.equal(b.app.store.get('progress.lessonRows').length, 1);
    assert.equal(b.app.store.get('practice.sessions').length, 1);
    assert.ok(b.app.store.get('exam.saved'), 'saved exam restored');
    assert.equal(b.proto.currentScreen(), 'select-path', 'last screen restored');
    assert.equal(b.q('#resumeBar').hidden, false, 'resume bar visible after reopen');
    assert.equal(b.qa('[data-screen="learn"] .pathwrap .node')[0].dataset.state, 'done');
    b.click(b.q('#resumeBtn'));
    assert.equal(b.proto.currentScreen(), 'exam-run', 'saved exam resumes into the run screen');
    assert.equal(b.app.store.get('exam.saved'), null, 'resuming consumes the snapshot');
  } finally { b.close(); }
});

test('source contains no network calls, no backend and no server simulation', () => {
  const files = ['src/app.js', 'src/store.js', 'src/engine.js', 'src/fixtures.js',
    'src/routes.js', 'src/views.js', 'server.js', 'assets/proto-ui.js'];
  for (const rel of files) {
    const text = fs.readFileSync(`${APP}/${rel}`, 'utf8');
    assert.equal(/\bfetch\s*\(/.test(text), false, `${rel} must not call fetch`);
    assert.equal(/new\s+(?:XMLHttpRequest|WebSocket|EventSource)\b/.test(text), false,
      `${rel} must not open a connection`);
  }
  // The service worker only re-requests same-origin static files for caching.
  const sw = fs.readFileSync(`${APP}/sw.js`, 'utf8');
  assert.match(sw, /req\.method !== 'GET'/);
  assert.match(sw, /new URL\(req\.url\)\.origin !== self\.location\.origin/);
  const app = fs.readFileSync(`${APP}/src/app.js`, 'utf8');
  assert.equal(/serverConfirmed:\s*true/.test(app), false);
  assert.match(fs.readFileSync(`${APP}/src/store.js`, 'utf8'), /serverConfirmed: false/);
});
