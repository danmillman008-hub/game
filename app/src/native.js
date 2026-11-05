/**
 * MIMO NATIVE — one-click offline application controller.
 *
 * NAVIGATION (measured in M08/M09 against com.getmimo 9.35):
 *   MainActivity -> bottom tabs Learn / Practice / Leaderboard / Profile
 *   Learn        -> PathMap -> ChapterActivity -> lesson renderer -> quit dialog
 *                -> celebration -> PathMap
 *   Path picker  -> Select Path -> Path overview -> Section detail -> Lesson
 *   Practice     -> guest gate -> exam hub / bank
 *
 * The approved v12.5-fa prototype markup, CSS, vectors, data and UI renderer
 * stay byte-identical. This controller only drives them with the REAL 9.35
 * navigation state machine and wires the local offline engines into screens
 * that look like Mimo. No server, no fetch, no API key, no generated text.
 */
import { createStore, memoryStorage } from './store.js';
import { esc, faNum, stamp, saveText, saveBytes, makeZip, b64ToText, toBytes } from './util.js';
import { createEconomy, TOKEN_KINDS, ECONOMY_RULES } from './token-economy.js';
import { createLearningPath } from './learning-path.js';
import { createHarness, LEARNHARNESS, EXTERNAL_PROVIDER_CONTRACT } from './harness.js';
import { createOutputKit } from './output-kit.js';
import { DESIGN_TOKENS } from './design-tokens.js';
import { STARTER_PACKAGE, STARTER_SUMMARY } from './starter-package.js';

const win = window;
const doc = document;
const PROTO = win.PROTO;
const KONKUR = win.KONKUR || { courses: [], programs: [] };
const $ = (s, r) => (r || doc).querySelector(s);
const $$ = (s, r) => Array.prototype.slice.call((r || doc).querySelectorAll(s));
const fa = faNum;
const ic = (n, s, m) => (PROTO && PROTO.icon ? PROTO.icon(n, s || 24, m === undefined ? 1 : m) : '');
const toast = (m) => { try { PROTO.toast(m); } catch (_) { /* no toast element */ } };

let storage;
try { storage = win.localStorage; storage.getItem('mimo.native.probe'); }
catch (_) { storage = memoryStorage(); }
const store = createStore(storage);
const economy = createEconomy(store);
const learningPath = createLearningPath(store, economy, PROTO, STARTER_PACKAGE.questions);
let harness = createHarness({ store, contentPackage: STARTER_PACKAGE });

/* ---------------------------------------------------------------------------
   Local, content-driven AI studio (four LearnHarness phases). No LLM.
   --------------------------------------------------------------------------- */
const aiStudio = (() => {
  let phase = 'measure';
  let measureAnswers = {};
  let practiceAnswer = null;
  let sessions = [];
  let contextUnits = 0;
  let chosenGoal = '';

  const PHASE_FA = LEARNHARNESS.phaseFa;
  const QUESTIONS = (PROTO && PROTO.questions && PROTO.questions.length
    ? PROTO.questions : STARTER_PACKAGE.questions).slice(0, 5);

  function sourceQuestions() {
    return (PROTO && PROTO.questions && PROTO.questions.length ? PROTO.questions
      : STARTER_PACKAGE.questions.map((q) => ({ stem: q.stemFa, opts: q.options,
        ok: q.correctIndex, expl: q.explanationFa })));
  }

  function tokenStructure() {
    const st = harness.getStatus();
    return [
      { fa: 'مدل', value: 'local-content (بدون LLM)' },
      { fa: 'زمینه', value: `${fa(contextUnits)} واحد محلی` },
      { fa: 'هزینه', value: '۰٫۰۰ دلار' },
      { fa: 'گامها', value: `${fa(st.steps)} گام` },
      { fa: 'تنظیمات', value: 'تولید متن: خیر · شبکه: خیر' },
    ];
  }

  function state() {
    return { phase, phaseFa: PHASE_FA[phase], measureScore: Object.keys(measureAnswers).length,
      practiceAnswer, sessions, contextUnits, chosenGoal };
  }

  function render() {
    const body = $('#nsBody');
    if (!body) return;
    const st = harness.getStatus();
    contextUnits = st.steps * 12 + st.propositions * 8 + Object.keys(measureAnswers).length * 4;
    const chipBox = $('#nsTokenChips');
    if (chipBox) chipBox.innerHTML = tokenStructure().map((t) =>
      `<span class="chip on">${esc(t.fa)}: ${esc(t.value)}</span>`).join('');
    const honest = $('#nsHonest');
    if (honest) honest.textContent = `مدل: ${st.provider} · تولید متن: خیر · ارائهدهندهٔ خارجی: ${st.externalProvider}`;
    const graph = $('#nsGraph');
    if (graph) graph.innerHTML = LEARNHARNESS.phases.map((p, i) =>
      `<span><b>${esc(fa(i + 1))}. ${esc(PHASE_FA[p])}</b>${p === phase ? ' · فعلی' : ''}</span>`).join('');

    if (phase === 'measure') {
      body.innerHTML = `<div class="native-hero"><span class="kick">فاز ۱ · سنجش</span>
        <h2>از کجا شروع کنیم؟</h2><p>پنج پرسش از همان بانک سؤال پروتوتایپ؛ نتیجه فقط تعیین نقطهٔ شروع است.</p></div>
        ${QUESTIONS.map((q, qi) => `<div class="native-card"><b>${esc(fa(qi + 1))}. ${esc(q.stem || q.stemFa || '')}</b>
          ${(q.opts || q.options || []).map((o, oi) => `<button type="button" class="native-row" data-ai="mopt" data-q="${qi}" data-o="${oi}">
            <span class="native-st">${esc(fa(oi + 1))}</span><span class="native-tx"><b>${esc(o)}</b></span></button>`).join('')}
        </div>`).join('')}
        <button type="button" class="native-cta" data-ai="plan">برنامهریزی ←</button>`;
    } else if (phase === 'plan') {
      const steps = harness.state.plan || [];
      body.innerHTML = `<div class="native-hero"><span class="kick">فاز ۲ · برنامهریزی</span>
        <h2>مسیر «${esc(chosenGoal || 'یادگیری')}»</h2><p>${fa(steps.length)} گام از محتوای موجود، بهترتیب وابستگی.</p>
        <div class="native-bar"><i style="width:16%"></i></div></div>
        <ul class="native-steps">${steps.map((s, i) => `<li><i>${esc(fa(i + 1))}</i><span>${esc(s.title)}</span></li>`).join('')}</ul>
        <button type="button" class="native-cta" data-ai="teach">شروع آموزش ←</button>`;
    } else if (phase === 'teach') {
      const prop = (harness.state.graph.propositions || []).slice(-1)[0];
      body.innerHTML = `<div class="native-hero"><span class="kick">فاز ۳ · آموزش</span>
        <h2>${esc(prop ? prop.text : 'درسی ثبت نشده است')}</h2>
        <p>${esc(prop && prop.sourceRef ? prop.sourceRef : 'بستهٔ محتوای محلی')}</p></div>
        <div class="native-banner">این متن عیناً از بستهٔ محتوا خوانده شده؛ هیچ جملهای تولید نشده است.</div>
        <button type="button" class="native-cta" data-ai="practice">رفتن سراغ تمرین ←</button>`;
    } else {
      const q = sourceQuestions()[0] || { stem: '', opts: [], ok: 0, expl: '' };
      const session = harness.practice().session;
      const shown = (session && session.questions && session.questions[0]) || q;
      const opts = shown.options || shown.opts || [];
      const ok = shown.correctIndex !== undefined ? shown.correctIndex : shown.ok;
      const expl = shown.explanationFa || shown.explanation || shown.expl || '';
      const stem = shown.stemFa || shown.stem || '';
      body.innerHTML = `<div class="native-hero"><span class="kick">فاز ۴ · تمرین</span>
        <h2>${esc(stem)}</h2></div>
        <div class="native-card">${opts.map((o, oi) => `<button type="button" class="native-row" data-ai="popt" data-o="${oi}">
          <span class="native-st">${esc(fa(oi + 1))}</span><span class="native-tx"><b>${esc(o)}</b></span></button>`).join('')}</div>
        <div id="nsPracticeFeedback"></div>
        <button type="button" class="native-cta secondary" data-ai="again">جلسهٔ تازه</button>`;
      body.dataset.correct = String(ok);
      body.dataset.expl = expl;
    }
  }

  function answerMeasure(qi, oi, el) {
    measureAnswers[qi] = oi;
    $$('[data-ai="mopt"][data-q="' + qi + '"]').forEach((b) => b.classList.remove('done'));
    el.classList.add('done');
    contextUnits += 4;
    const st = harness.getStatus();
    const chipBox = $('#nsTokenChips');
    if (chipBox) chipBox.innerHTML = tokenStructure().map((t) =>
      `<span class="chip on">${esc(t.fa)}: ${esc(t.value)}</span>`).join('');
    void st;
  }

  function answerPractice(oi, el) {
    const body = $('#nsBody');
    const ok = Number(body.dataset.correct);
    practiceAnswer = oi;
    $$('[data-ai="popt"]').forEach((b) => b.classList.remove('done'));
    el.classList.add('done');
    sessions.push({ at: stamp(), correct: oi === ok, generated: false });
    const box = $('#nsPracticeFeedback');
    if (box) box.innerHTML = `<div class="native-banner ${oi === ok ? 'ok' : 'no'}">
      <b>${oi === ok ? 'درست!' : 'پاسخ درست گزینهٔ ' + fa(ok + 1)}</b><br>${esc(body.dataset.expl || '')}</div>`;
    contextUnits += 8;
    const chipBox = $('#nsTokenChips');
    if (chipBox) chipBox.innerHTML = tokenStructure().map((t) =>
      `<span class="chip on">${esc(t.fa)}: ${esc(t.value)}</span>`).join('');
  }

  function plan() {
    chosenGoal = 'یادگیری مبحثی';
    harness.start(chosenGoal);
    harness.plan(60);
    phase = 'plan';
    render();
  }
  function teach() { harness.teach(0); phase = 'teach'; render(); }
  function practice() { harness.practice(); phase = 'practice'; render(); }
  function again() {
    measureAnswers = {}; practiceAnswer = null; phase = 'measure';
    harness.stop(); harness.start('یادگیری مبحثی'); render();
  }
  function setPhase(p) { if (LEARNHARNESS.phases.includes(p)) { phase = p; harness.setPhase(p); render(); } }
  function exportSession() {
    const ok = saveText('جلسه-هوش-مصنوعی.json', JSON.stringify({
      generatedAt: stamp(), phases: LEARNHARNESS.phases, state: state(),
      harness: harness.getStatus(), tokenStructure: tokenStructure(), sessions,
      honest: { llm: false, network: false, generatedText: false,
        externalProvider: EXTERNAL_PROVIDER_CONTRACT.status, serverConfirmed: false },
    }, null, 2), 'application/json');
    toast(ok ? 'جلسهٔ محلی ذخیره شد' : 'ذخیره در این محیط پشتیبانی نمیشود');
    return ok;
  }
  return { render, state, tokenStructure, exportSession, plan, teach, practice, again,
    setPhase, answerMeasure, answerPractice,
    get phase() { return phase; }, get contextUnits() { return contextUnits; } };
})();

const outputKit = createOutputKit({ doc, store, economy, learningPath, aiStudio, toast });

/* ---------------------------------------------------------------------------
   Mimo-native screens (inserted into the approved phone, before #tabs)
   --------------------------------------------------------------------------- */
const phone = $('#phone');
const tabs = $('#tabs');

function insertScreen(name, tab, html) {
  const sec = doc.createElement('section');
  sec.className = 'screen native';
  sec.dataset.screen = name;
  sec.innerHTML = html;
  phone.insertBefore(sec, tabs);
  PROTO.tabMap[name] = tab;
  return sec;
}

function head(title, back, act) {
  return `<div class="native-head"><button type="button" class="native-back" data-nav="${esc(back)}" aria-label="بازگشت">${ic('ic_arrow_back_24', 24, 1)}</button>
    <b>${esc(title)}</b>${act || ''}</div>`;
}

insertScreen('native-studio', 'AI',
  head('استودیو یادگیری', 'ai') +
  `<div class="native-scroll"><div class="native-chips" id="nsPhases">
     ${LEARNHARNESS.phases.map((p, i) => `<button type="button" class="native-chip ${i === 0 ? 'on' : ''}" data-ai="phase" data-p="${p}">${esc(LEARNHARNESS.phaseFa[p])}</button>`).join('')}
   </div>
   <div class="native-chips" id="nsTokenChips"></div>
   <div id="nsBody"></div>
   <div class="native-h">گراف دانش محلی</div><div class="native-grid" id="nsGraph"></div>
   <div class="native-banner" id="nsHonest"></div>
   <div class="native-card"><b>بستهٔ محتوا</b>
     <button type="button" class="native-row" data-n="import"><span class="native-st">＋</span><span class="native-tx"><b>وارد کردن بستهٔ محتوا</b><small>فایل JSON محلی · بدون شبکه</small></span></button>
     <button type="button" class="native-row" data-n="ai:export"><span class="native-st">↓</span><span class="native-tx"><b>خروجی جلسه</b><small>گزارش محلی چهار فاز</small></span></button>
   </div><input type="file" id="nsFile" accept="application/json,.json" class="native-hidden"></div>`);

insertScreen('native-tokens', 'Profile',
  head('ساختار توکنها', 'profile') +
  `<div class="native-scroll"><div class="native-hero"><span class="kick">سه معنای «توکن»</span>
     <h2>طراحی · پاداش · زمینه</h2></div>
   <div class="native-chips" id="tkChips">
     <button type="button" class="native-chip on" data-tk="design">توکنهای طراحی</button>
     <button type="button" class="native-chip" data-tk="economy">توکنهای پاداش</button>
     <button type="button" class="native-chip" data-tk="ai">توکنهای هوش مصنوعی</button></div>
   <div id="tkBody"></div></div>`);

insertScreen('native-output', 'Profile',
  head('خروجی گرفتن', 'profile') +
  `<div class="native-scroll"><div class="native-hero"><span class="kick">یک کلیک</span>
     <h2>همین فایل را ببر</h2><span class="native-meta" id="outStatus">—</span></div>
   <div id="outBody"></div></div>`);

insertScreen('native-gate', 'Practice',
  head('تمرین', 'learn') +
  `<div class="native-scroll"><div class="native-gate"><div class="native-gicon">${ic('ic_lock_alt_02', 54, 1)}</div>
     <h2>یادگیریت رو تثبیت کن</h2><p>برای دسترسی به تمرینها، یک پروفایل محلی بساز. هیچ حساب، ایمیل، رمز یا سروری لازم نیست؛ همهچیز روی همین دستگاه میماند.</p></div>
   <button type="button" class="native-cta" data-n="profile:create">ساخت پروفایل محلی</button>
   <button type="button" class="native-cta secondary" data-nav="learn">بعداً</button></div>`);

insertScreen('native-done', 'Learn',
  `<div class="native-scroll"><div class="native-celebrate"><div class="native-cbadge">${ic('ic_check_white', 60, 1)}</div>
     <h2>درس تمام شد!</h2><p id="doneText">گام بعدی مسیر باز شد.</p>
     <div class="native-stats" id="doneStats"></div></div>
   <button type="button" class="native-cta" data-nav="learn">ادامهٔ مسیر ←</button></div>`);

/* Quit dialog — three measured choices from M09 / ChapterActivity. */
const quit = doc.createElement('div');
quit.className = 'native-dialog';
quit.id = 'nativeQuit';
quit.innerHTML = `<div class="native-dcard"><h3>از درس خارج میشوید؟</h3>
  <p>پیشرفت این درس از دست میرود.</p>
  <button type="button" class="native-drow primary" data-quit="stay">ادامهٔ درس</button>
  <button type="button" class="native-drow" data-quit="path">انتخاب مسیر دیگر</button>
  <button type="button" class="native-drow" data-quit="quit">خروج از درس</button></div>`;
phone.appendChild(quit);

/* Lesson player replaces ONLY the runtime content of the approved lesson screen. */
const lessonScreen = $('[data-screen="lesson"]');
const ORIGINAL_LESSON = lessonScreen ? lessonScreen.innerHTML : '';
const lessonParas = $$('[data-screen="lesson"] .lesson-body p').map((p) => p.textContent.trim()).filter(Boolean);
const browserBits = $$('[data-screen="lesson"] .browser-in h3, [data-screen="lesson"] .browser-in p')
  .map((p) => p.textContent.trim()).filter(Boolean);
if (lessonScreen) {
  lessonScreen.className = 'screen native';
  lessonScreen.innerHTML = `<div class="native-lesson">
    <div class="nl-top"><button type="button" class="nl-x" data-n="lesson:quit" aria-label="خروج">${ic('ic_close', 24, 1)}</button>
      <div class="nl-prog"><i id="nlProg" style="width:0%"></i></div>
      <button type="button" class="nl-flag" data-n="lesson:report" aria-label="گزارش">${ic('ic_flag', 24, 1)}</button></div>
    <div class="nl-body" id="nlBody"></div>
    <div class="nl-feedback native-hidden" id="nlFeedback"></div>
    <div class="nl-foot"><button type="button" class="native-cta" id="nlContinue" data-n="lesson:next">ادامه</button></div>
  </div>`;
}

/* Profile rows + AI studio entry, all using Mimo-native rows. */
const profile = $('[data-screen="profile"]');
if (profile) profile.insertAdjacentHTML('beforeend',
  `<div class="native-card"><b>ابزارهای یادگیری</b>
    <button type="button" class="native-row" data-nav="path-overview"><span class="native-st">▤</span><span class="native-tx"><b>مسیر آموزشی</b><small>۱۲ کتاب · ۶۰ فصل · ۱۸۰ درس</small></span><span class="native-chev">${ic('ic_arrow_back_24', 16, 1)}</span></button>
    <button type="button" class="native-row" data-nav="native-studio"><span class="native-st">✦</span><span class="native-tx"><b>استودیو یادگیری محلی</b><small>چهار فاز · بدون مدل زبانی</small></span><span class="native-chev">${ic('ic_arrow_back_24', 16, 1)}</span></button>
    <button type="button" class="native-row" data-nav="native-tokens"><span class="native-st">◈</span><span class="native-tx"><b>ساختار توکنها</b><small>طراحی · پاداش · زمینه</small></span><span class="native-chev">${ic('ic_arrow_back_24', 16, 1)}</span></button>
    <button type="button" class="native-row" data-nav="native-output"><span class="native-st">↓</span><span class="native-tx"><b>خروجی گرفتن / نصب اپ</b><small>تکفایل، ZIP، CSV، گزارش</small></span><span class="native-chev">${ic('ic_arrow_back_24', 16, 1)}</span></button>
  </div>`);
const aiTop = $('.ai-top-left');
if (aiTop) aiTop.insertAdjacentHTML('beforeend',
  `<button type="button" class="fchip ai-chip" data-nav="native-studio"><b>استودیو</b></button>`);

/* ---------------------------------------------------------------------------
   Learn / PathMap — Mimo 9.35 PathMapScreenKt states, driven by real progress.
   --------------------------------------------------------------------------- */
let selectedChapter = 0;
let currentLessonId = null;
let lesson = { id: null, steps: [], index: 0, selected: null, correct: false, before: null };

function curriculumCourse() { return learningPath.course(); }

function renderHeader() {
  const e = economy.read();
  const pills = $$('[data-screen="learn"] .mimo-hdr .pill');
  if (pills[0]) { const b = $('b', pills[0]); if (b) b.textContent = fa(e.coins); }
  if (pills[1]) { const inf = $('span.inf', pills[1]); if (inf) inf.textContent = '∞'; }
  if (pills[2]) { const b = $('b', pills[2]); if (b) b.textContent = fa(e.streak); }
  const p = learningPath.progress();
  const bar = $('#overviewEntry .oc-bar i');
  if (bar) bar.style.width = `${p.percent}%`;
  const c = curriculumCourse();
  const curId = currentLessonId || learningPath.nextId();
  const cur = curId ? learningPath.byId(curId) : null;
  const ch = cur && c ? c.chapters.find((x) => x.id === cur.chapterId) : null;
  const kicker = $('#overviewEntry .oc-kicker');
  if (kicker && c) { kicker.textContent = c.name; kicker.dataset.fa = c.name; }
  const ocTitle = $('#overviewEntry .oc-title');
  if (ocTitle && ch) {
    const t = `فصل ${fa(ch.ordinal)} · ${ch.name}`;
    ocTitle.textContent = t; ocTitle.dataset.fa = t;
  }
  const title = $('#learnPathTitle');
  if (title) { const pr = (KONKUR.programs || []).find((x) => x.key === learningPath.state().programKey);
    const t = pr ? pr.label : (curriculumCourse() ? curriculumCourse().name : 'یادگیری');
    title.textContent = t; title.dataset.fa = t; }
}

function renderLearn() {
  renderHeader();
  const ids = learningPath.flat().slice(0, 6).map((l) => l.id);
  const nodes = $$('[data-screen="learn"] .pathwrap .node');
  nodes.forEach((el, i) => {
    if (i >= 4) return; // bolt practice checkpoints keep their approved vectors
    const id = ids[i];
    el.dataset.lessonId = id || '';
    el.removeAttribute('id');
    const st = id ? learningPath.statusOf(id) : 'locked';
    const cls = st === 'done' ? 'done' : (st === 'current' || st === 'open') ? 'cur' : 'next';
    el.className = `node ${cls} l10n${i + 1}`;
    el.dataset.state = st;
    el.dataset.nav = 'chapter';
    if (cls === 'cur') {
      el.id = 'curNode';
      el.innerHTML = '<span class="cur-inner" id="curInner"><span class="hring"><b>۱/۲</b></span></span>';
      el.removeAttribute('data-icon');
    } else if (cls === 'done') {
      el.dataset.icon = 'ic_check_white';
      el.dataset.size = '48';
      el.dataset.mono = '1';
      el.innerHTML = ic('ic_check_white', 48, 1);
    } else {
      el.dataset.icon = 'ic_play';
      el.dataset.size = '48';
      el.dataset.mono = '1';
      el.innerHTML = ic('ic_play', 48, 1);
    }
  });
  // No locked node in learning: the "next" node is always unlocked (F25).
  if (PROTO.paintIcons) PROTO.paintIcons(phone);
}

function renderProfile() {
  if (!profile) return;
  const c = curriculumCourse();
  const b = $('.prof-course b', profile); if (b && c) { b.textContent = c.name; b.dataset.fa = c.name; }
  const pct = $('.prof-course .pct', profile);
  if (pct) pct.textContent = `${fa(learningPath.progress().percent)}%`;
}
function renderLeaderboard() {
  const e = economy.read();
  const cards = $$('[data-screen="leaderboard"] .statcard b');
  if (cards[0]) cards[0].textContent = fa(e.streak);
  if (cards[1]) cards[1].textContent = fa(e.xp);
  if (cards[2]) cards[2].textContent = fa(e.weeklyXp);
}

/* ---------------------------------------------------------------------------
   Chapter modal + lesson renderer (ChapterActivity / ViewPager)
   --------------------------------------------------------------------------- */
function setChapterModal(id) {
  const ls = learningPath.byId(id);
  const c = curriculumCourse();
  const modal = $('#chapterModal');
  if (!modal) return;
  const h = $('h2', modal); if (h && ls) { h.textContent = ls.title; h.dataset.fa = ls.title; }
  const row = $('.chapter-row', modal);
  if (row) {
    const p = learningPath.progress();
    row.innerHTML = `<span>${esc(c ? c.name : 'فصل')}</span><span>${fa(p.done)}/${fa(p.total)}</span>`;
  }
  const bar = $('.mprogress i', modal);
  if (bar) bar.style.width = `${learningPath.progress().percent}%`;
}

function lessonSteps(id) {
  const q = learningPath.questionFor(id);
  const ls = learningPath.byId(id);
  const c = curriculumCourse();
  const ch = ls ? c.chapters.find((x) => x.id === ls.chapterId) : null;
  return [
    { kind: 'slide', title: ls ? ls.title : 'درس', course: c ? c.name : '', chapter: ch ? ch.name : '' },
    { kind: 'choice', q },
    { kind: 'gap', q },
    { kind: 'reveal', q },
  ];
}

function optionText(o) { return String(o == null ? '' : o); }

function renderStep() {
  const step = lesson.steps[lesson.index];
  const body = $('#nlBody');
  const fb = $('#nlFeedback');
  const btn = $('#nlContinue');
  const prog = $('#nlProg');
  if (!step || !body) return;
  if (prog) prog.style.width = `${Math.round(((lesson.index + 1) / lesson.steps.length) * 100)}%`;
  fb.className = 'nl-feedback native-hidden';
  fb.innerHTML = '';
  lesson.selected = null;
  btn.disabled = false;
  btn.textContent = lesson.index === lesson.steps.length - 1 ? 'پایان درس' : 'ادامه';

  if (step.kind === 'slide') {
    body.innerHTML = `${lessonParas.map((t) => `<p>${esc(t)}</p>`).join('')}
      <div class="nl-panel"><h3>${esc(step.title)}</h3>
        <div class="nl-gap">${esc(step.course)}</div>
        <p style="font-size:14px;color:var(--text-weak)">${esc(step.chapter)}</p></div>
      ${browserBits.length ? `<div class="nl-file">${ic('ic_file', 16, 1)}<span>${esc(browserBits[0])}</span></div>
        <div class="nl-editor">${esc(browserBits.slice(1).join(' · '))}</div>` : ''}`;
    return;
  }
  const q = step.q;
  if (!q) { body.innerHTML = '<p>محتوای این درس هنوز ثبت نشده است.</p>'; return; }
  const opts = q.options || q.opts || [];
  if (step.kind === 'choice') {
    body.innerHTML = `<p>${esc(q.stem || q.stemFa || '')}</p>
      <div class="nl-hint">${ic('ic_help', 16, 1)}<span>گزینهٔ درست را انتخاب کنید</span></div>
      <div class="nl-choices">${opts.map((o, i) => `<button type="button" class="nl-choice" data-n="lesson:option" data-o="${i}">
        <span class="nl-num">${esc(fa(i + 1))}</span><span>${esc(optionText(o))}</span></button>`).join('')}</div>`;
  } else if (step.kind === 'gap') {
    body.innerHTML = `<p>${esc(q.stem || q.stemFa || '')}</p>
      <div class="nl-hint">${ic('ic_help', 16, 1)}<span>پاسخ درست را از قطعهها انتخاب کنید</span></div>
      <div class="nl-panel"><h3>جاهای خالی</h3><div class="nl-gap">＿＿＿＿</div>
        <div class="nl-snips">${opts.map((o, i) => `<button type="button" class="nl-snip" data-n="lesson:option" data-o="${i}">${esc(optionText(o).slice(0, 14))}</button>`).join('')}</div></div>`;
  } else {
    const ok = q.correctIndex !== undefined ? q.correctIndex : q.ok;
    body.innerHTML = `<p><strong>${esc(q.stem || q.stemFa || '')}</strong></p>
      <div class="nl-panel"><h3>توضیح درس</h3><p style="font-size:14px;line-height:1.9">${esc(q.explanation || q.expl || '')}</p>
      <div class="nl-gap">${esc(optionText(opts[ok] || ''))}</div></div>
      <div class="native-banner">پاسخ درست: گزینهٔ ${fa(Number(ok) + 1)} · ${esc(q.ref || 'prototype:v12.5-fa')}</div>
      <button type="button" class="native-chip" data-n="lesson:ai">توضیح با هوش مصنوعی</button>`;
  }
}

function openLesson(id) {
  if (!id) id = learningPath.nextId();
  const ls = learningPath.byId(id);
  if (!ls) return;
  currentLessonId = id;
  lesson = { id, steps: lessonSteps(id), index: 0, selected: null, correct: false,
    before: economy.read() };
  renderStep();
  PROTO.go('lesson');
}

function checkAnswer(oi, el) {
  const step = lesson.steps[lesson.index];
  const q = step && step.q;
  if (!q) return;
  const ok = q.correctIndex !== undefined ? q.correctIndex : q.ok;
  lesson.selected = oi;
  const correct = oi === Number(ok);
  if (step.kind === 'choice') {
    $$('#nlBody .nl-choice').forEach((b, i) => {
      b.classList.toggle('correct', i === Number(ok));
      b.classList.toggle('wrong', i === oi && !correct);
      b.classList.remove('selected');
    });
  } else {
    $$('#nlBody .nl-snip').forEach((b, i) => {
      b.classList.toggle('correct', i === Number(ok));
      b.classList.toggle('wrong', i === oi && !correct);
    });
  }
  if (correct) lesson.correct = true;
  const fb = $('#nlFeedback');
  fb.className = `nl-feedback ${correct ? 'ok' : 'no'}`;
  fb.innerHTML = `<b>${correct ? 'درست!' : 'پاسخ درست گزینهٔ ' + fa(Number(ok) + 1)}</b>
    <p>${esc(q.explanation || q.expl || '')}</p>`;
  void el;
}

function finishLesson() {
  const before = lesson.before || economy.read();
  learningPath.complete(lesson.id, lesson.correct);
  const after = economy.read();
  const dxp = Math.max(0, after.xp - before.xp);
  const dcoin = Math.max(0, after.coins - before.coins);
  const p = learningPath.progress();
  const stats = $('#doneStats');
  if (stats) stats.innerHTML = `<div><b>+${fa(dxp)}</b><small>امتیاز تجربه</small></div>
    <div><b>+${fa(dcoin)}</b><small>سکه</small></div><div><b>${fa(p.done)}/${fa(p.total)}</b><small>درس</small></div>`;
  const txt = $('#doneText');
  if (txt) txt.textContent = `گام بعدی «${curriculumCourse().name}» باز شد.`;
  renderLearn(); renderProfile(); renderLeaderboard();
  PROTO.go('native-done');
}

function nextStep() {
  if (lesson.index < lesson.steps.length - 1) { lesson.index += 1; renderStep(); return; }
  finishLesson();
}

/* ---------------------------------------------------------------------------
   Native screens: tokens / output / studio / gate
   --------------------------------------------------------------------------- */
let tokenTab = 'design';
function renderTokens() {
  const body = $('#tkBody');
  if (!body) return;
  $$('#tkChips .native-chip').forEach((c) => c.classList.toggle('on', c.dataset.tk === tokenTab));
  if (tokenTab === 'design') {
    const names = [];
    (DESIGN_TOKENS.groups || []).forEach((g) => (g.names || []).forEach((n) => names.push(n)));
    const seen = new Set(); const list = names.filter((n) => (seen.has(n) ? false : seen.add(n)));
    const style = getComputedStyle(doc.documentElement);
    body.innerHTML = `<div class="native-h">${fa(list.length)} توکن طراحی از proto.css</div>
      <div class="native-grid">${list.map((n) => {
        const v = (style.getPropertyValue(n) || '').trim();
        return `<span><div class="native-swatch" style="background:${esc(v || 'var(--card)')}"></div><b>${esc(n)}</b>${esc(v)}</span>`;
      }).join('')}</div>`;
  } else if (tokenTab === 'economy') {
    const e = economy.read();
    body.innerHTML = `<div class="native-h">دفتر توکنها · سقف XP روزانه ${fa(economy.cap)}</div>
      <div class="native-card">${economy.structure().map((k) => `<div class="native-kv"><b>${esc(k.fa)}</b><span>${esc(k.valueFa)}</span></div>`).join('')}
        <div class="native-kv"><b>رویدادهای دفتر</b><span>${fa((e.ledger || []).length)}</span></div></div>
      <button type="button" class="native-cta" data-tk="goal">ثبت هدف روزانه</button>
      <button type="button" class="native-cta secondary" data-tk="spend">خرج یک کلید برای راهنمایی</button>
      <div class="native-h">قواعد محلی (تأییدنشده)</div>
      <div class="native-card">${ECONOMY_RULES.map((r) => `<div class="native-kv"><b>${esc(r.fa)}</b><span>${esc(r.formula)}</span></div>`).join('')}</div>`;
  } else {
    body.innerHTML = `<div class="native-h">شمارش زمینه و هزینه · کاملاً محلی</div>
      <div class="native-card">${aiStudio.tokenStructure().map((k) => `<div class="native-kv"><b>${esc(k.fa)}</b><span>${esc(k.value)}</span></div>`).join('')}</div>
      <div class="native-banner">بدون مدل زبانی، بدون اینترنت و بدون تولید متن. استنتاج از سرور میمو تأیید نشده است.</div>`;
  }
}

function renderOutput() {
  const body = $('#outBody');
  const status = $('#outStatus');
  if (status) status.textContent = outputKit.hasSource() ? 'فایل تکهای این اپ درون خودش موجود است؛ خروجی دقیقاً همین فایل را میسازد.' : 'نسخهٔ چندفایله؛ فایل dist/Mimo.html را دانلود کنید.';
  if (!body) return;
  const rows = [
    ['out:html', 'دانلود Mimo.html', 'تکفایل، دوبار کلیک کنید'],
    ['out:zip', 'دانلود Mimo.zip', 'شامل PWA و آیکنها'],
    ['out:state', 'وضعیت محلی', 'JSON ذخیرهشده روی دستگاه'],
    ['out:csv', 'مسیر آموزشی', 'CSV با ۱۸۰ درس'],
    ['out:report', 'گزارش چاپی', 'HTML قابل چاپ'],
    ['out:session', 'جلسهٔ هوش مصنوعی', 'چهار فاز محلی'],
    ['out:install', 'نصب اپلیکیشن', 'افزودن به صفحهٔ اصلی'],
  ];
  body.innerHTML = `<div class="native-card">${rows.map((r) => `<button type="button" class="native-row" data-n="${r[0]}">
      <span class="native-st">↓</span><span class="native-tx"><b>${esc(r[1])}</b><small>${esc(r[2])}</small></span></button>`).join('')}</div>`;
}

function renderStudio() { aiStudio.render(); }

function renderGate() {
  const guest = store.get('identity.guest') !== false;
  PROTO.tabScreen.Practice = guest ? 'native-gate' : 'exam-hub';
}

/* ---------------------------------------------------------------------------
   PROTO_NAV hook: render on every navigation, persist last screen.
   --------------------------------------------------------------------------- */
const SAFE_RESTORE = new Set(['learn', 'select-path', 'path-overview', 'section-detail',
  'exam-hub', 'leaderboard', 'profile', 'ai', 'section-practice', 'study-plan',
  'practice-bank', 'native-studio', 'native-tokens', 'native-output', 'native-gate']);

const FULLSCREEN = new Set(['lesson', 'native-done', 'exam-run']);
win.PROTO_NAV = (name) => {
  try { store.set('navigation.screen', name); } catch (_) { /* storage blocked */ }
  phone.dataset.fullscreen = FULLSCREEN.has(name) ? '1' : '0';
  if (name === 'learn' || name === 'select-path' || name === 'path-overview' || name === 'section-detail') renderLearn();
  if (name === 'profile') renderProfile();
  if (name === 'leaderboard') renderLeaderboard();
  if (name === 'native-tokens') renderTokens();
  if (name === 'native-output') renderOutput();
  if (name === 'native-studio') renderStudio();
  if (name === 'native-gate') renderGate();
  if (name === 'chapter') setChapterModal(currentLessonId);
};

win.PROTO_PERSIST = (saved) => {
  try { store.set('exam.saved', saved); } catch (_) { /* storage blocked */ }
};

/* ---------------------------------------------------------------------------
   One delegated capture handler for all native actions.
   proto-ui.js owns [data-nav] / [data-v11] / tabs; we only ADD behaviour.
   --------------------------------------------------------------------------- */
doc.addEventListener('click', (ev) => {
  const t = ev.target;

  // MainActivity tabs: navigate without the prototype's review toast.
  const tab = t.closest('#tabs .tab');
  if (tab) {
    ev.stopPropagation(); ev.preventDefault();
    const dest = PROTO.tabScreen[tab.dataset.tab];
    if (dest) PROTO.go(dest);
    return;
  }

  // The approved prototype chat must not invent an answer: intercept it.
  if (t.closest('#aiSend')) {
    ev.stopPropagation(); ev.preventDefault(); aiChatSend(); return;
  }
  if (t.closest('#askAiBtn') || t.closest('#askAiResultBtn')) {
    ev.stopPropagation(); ev.preventDefault(); PROTO.go('native-studio'); return;
  }

  // Capture the selected course / chapter / lesson behind the approved screens.
  const v11 = t.closest('[data-v11]');
  if (v11) {
    const parts = (v11.dataset.v11 || '').split(':');
    if (parts[0] === 'course' && parts[1]) learningPath.setCourse(parts[1]);
    if (parts[0] === 'program' && parts[1]) learningPath.setProgram(parts[1]);
    currentLessonId = learningPath.nextId();
    renderLearn();
  }
  const sec = t.closest('[data-v11section]');
  if (sec) selectedChapter = Number(sec.dataset.v11section) || 0;
  const row = t.closest('[data-screen="section-detail"] .sd-row');
  if (row) {
    const rows = $$('[data-screen="section-detail"] .sd-row');
    const i = rows.indexOf(row);
    const c = curriculumCourse();
    if (c) {
      const ch = c.chapters[Math.min(selectedChapter, c.chapters.length - 1)];
      const ls = ch && ch.lessons[Math.min(i, ch.lessons.length - 1)];
      currentLessonId = ls ? ls.id : learningPath.nextId();
    }
  }
  const node = t.closest('[data-screen="learn"] .pathwrap .node');
  if (node && node.dataset.lessonId) currentLessonId = node.dataset.lessonId;
  if (t.closest('#startLearning')) openLesson(currentLessonId);

  // quit dialog
  const q = t.closest('[data-quit]');
  if (q) {
    quit.classList.remove('on');
    if (q.dataset.quit === 'path') PROTO.go('select-path');
    else if (q.dataset.quit === 'quit') PROTO.go('learn');
    return;
  }

  const n = t.closest('[data-n]');
  if (!n) {
    const tk = t.closest('[data-tk]');
    if (tk && tk.dataset.tk === 'goal') { economy.apply('daily-goal'); renderTokens(); renderHeader(); toast('هدف روزانه ثبت شد'); }
    else if (tk && tk.dataset.tk === 'spend') { const ok = economy.spend('keys'); toast(ok ? 'یک کلید خرج شد' : 'کلیدی باقی نمانده'); renderTokens(); renderHeader(); }
    else if (tk && tk.dataset.tk) { tokenTab = tk.dataset.tk; renderTokens(); }
    const ai = t.closest('[data-ai]');
    if (ai) {
      const k = ai.dataset.ai;
      if (k === 'mopt') aiStudio.answerMeasure(Number(ai.dataset.q), Number(ai.dataset.o), ai);
      else if (k === 'popt') aiStudio.answerPractice(Number(ai.dataset.o), ai);
      else if (k === 'plan') aiStudio.plan();
      else if (k === 'teach') aiStudio.teach();
      else if (k === 'practice') aiStudio.practice();
      else if (k === 'again') aiStudio.again();
      else if (k === 'phase') { aiStudio.setPhase(ai.dataset.p);
        $$('#nsPhases .native-chip').forEach((c) => c.classList.toggle('on', c.dataset.p === ai.dataset.p)); }
    }
    return;
  }
  const key = n.dataset.n;
  if (key === 'lesson:quit') { quit.classList.add('on'); return; }
  if (key === 'lesson:report') { toast('گزارش این صفحه ثبت شد'); return; }
  if (key === 'lesson:option') { checkAnswer(Number(n.dataset.o), n); return; }
  if (key === 'lesson:next') { nextStep(); return; }
  if (key === 'lesson:ai') { PROTO.go('native-studio'); return; }
  if (key === 'profile:create') {
    store.set('identity.guest', false);
    store.set('identity.displayName', 'یادگیرندهٔ میمو');
    renderGate(); toast('پروفایل محلی ساخته شد'); PROTO.go('exam-hub'); return;
  }
  if (key === 'import') { const f = $('#nsFile'); if (f) f.click(); return; }
  if (key === 'ai:export') { aiStudio.exportSession(); return; }
  const out = {
    'out:html': () => outputKit.downloadHtml(),
    'out:zip': () => outputKit.downloadZip(),
    'out:state': () => outputKit.downloadState(),
    'out:csv': () => outputKit.downloadCsv(),
    'out:report': () => outputKit.printReport(),
    'out:session': () => outputKit.downloadSession(),
    'out:install': () => outputKit.install(),
  };
  if (out[key]) out[key]();
}, true);

/* Local-content chat: the reply is a lesson/explanation already in the package. */
function aiChatSend() {
  const input = $('#aiInput');
  const thread = $('#chatThread');
  if (!input || !thread) return;
  const text = (input.value || '').trim();
  if (!text) return;
  const me = doc.createElement('div'); me.className = 'bubble me'; me.textContent = text;
  const typing = $('#typing');
  if (typing) thread.insertBefore(me, typing); else thread.appendChild(me);
  input.value = '';
  harness.start(text);
  harness.plan(60);
  const t = harness.teach(0);
  const reply = doc.createElement('div');
  reply.className = 'bubble';
  if (t.ok && t.proposition) {
    reply.innerHTML = `${esc(t.proposition.text)}<div class="native-ctx">${esc(t.proposition.sourceRef || 'بستهٔ محتوای محلی')} · متن تولید نشده است</div>`;
  } else {
    reply.textContent = 'درسنامهای در بستهٔ محتوا ثبت نشده است.';
  }
  if (typing) thread.insertBefore(reply, typing); else thread.appendChild(reply);
  aiStudio.render();
}

/* Import a local content package (FileReader, no network). */
const fileInput = $('#nsFile');
if (fileInput) fileInput.addEventListener('change', () => {
  const f = fileInput.files && fileInput.files[0];
  if (!f) return;
  const reader = new win.FileReader();
  reader.onload = () => {
    try {
      const pkg = JSON.parse(String(reader.result));
      harness = createHarness({ store, contentPackage: pkg });
      aiStudio.again(); aiStudio.render(); renderTokens();
      toast('بستهٔ محتوا بارگذاری شد');
    } catch (err) { toast('فایل JSON معتبر نیست'); }
  };
  try { reader.readAsText(f); } catch (_) { toast('خواندن فایل ممکن نشد'); }
});

/* ---------------------------------------------------------------------------
   Boot
   --------------------------------------------------------------------------- */
function mountContentPackage(pkg) {
  harness = createHarness({ store, contentPackage: pkg });
  aiStudio.again(); aiStudio.render(); renderTokens();
  return harness.getStatus();
}

renderHeader(); renderLearn(); renderProfile(); renderLeaderboard();
renderTokens(); renderOutput(); renderStudio(); renderGate();
if (PROTO.paintIcons) PROTO.paintIcons(phone);

const savedScreen = store.get('navigation.screen');
const start = savedScreen && SAFE_RESTORE.has(savedScreen) ? savedScreen : 'learn';
PROTO.go(start);

/* Public, read-only-ish surface for tests and debugging. */
win.MIMO = {
  version: '2.0.0-native+mimo935',
  store, economy, learningPath, aiStudio, outputKit, proto: PROTO,
  harnessRef: () => harness, harnessStatus: () => harness.getStatus(),
  mountContentPackage, curriculum: learningPath.curriculum, starter: STARTER_SUMMARY,
  routes: { learn: 'PathMap', chapter: 'ChapterActivity', lesson: 'LessonRenderer',
    quit: 'QuitDialog', done: 'Celebration', practiceGate: 'PracticeGate' },
  go: (name) => PROTO.go(name),
  state: () => ({ screen: PROTO.currentScreen(), tab: PROTO.tabMap[PROTO.currentScreen()],
    lessonId: currentLessonId, lessonStep: lesson.index, lessonSteps: lesson.steps.length,
    phase: aiStudio.phase, guest: store.get('identity.guest') !== false,
    progress: learningPath.progress() }),
  openLesson, renderLearn, renderHeader, renderTokens, renderOutput, renderStudio,
  originalLessonHtml: ORIGINAL_LESSON,
};
win.APP = win.MIMO; // compatibility with the earlier verifier/tests
