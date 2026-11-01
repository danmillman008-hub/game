/**
 * Mimo shell — five-tab Persian application (Learn / Practice / Max / Leaderboard / Profile).
 *
 * Learn is implemented here against the recovered Mimo contracts (HANDOFF/). Practice and Max are the *real*
 * independent engines (EPM and LearnHarness), served by the preview host and embedded unchanged apart from the
 * Persian localization layer. Nothing is shared between the three engines except this navigation chrome.
 */

import { loadPack, nextLesson, DEFAULT_PACK } from '../learn/content.js';
import { parseLesson } from '../learn/dsl.js';
import { renderDocument, el } from '../learn/render.js';
import { createLessonRuntime, wireInteractions } from '../learn/lesson.js';
import {
  loadState, saveState, clearState, ensureRow, getRow, applyResult,
  chapterProgress, tutorialProgress, trackProgress, globalStats,
} from '../learn/store.js';
import { CORRECT, PARTIAL, INCORRECT, applySubmission } from '../learn/grade.js';

const PACK_ID = new URLSearchParams(location.search).get('pack') || DEFAULT_PACK;
const RESUME_KEY = 'mimo.learn.resume.v1';

const state = {
  pack: null,
  progress: loadState(),
  route: { name: 'learn' },
  lessonRuntime: null,
  tab: 'learn',
  engines: { practice: false, max: false },
};

const dom = {
  app: document.getElementById('app'),
  topbarTitle: document.getElementById('topbar-title'),
  topbar: document.getElementById('topbar'),
  learnRoot: document.getElementById('learn-root'),
  learnLoading: document.getElementById('learn-loading'),
  learnError: document.getElementById('learn-error'),
  leaderboard: document.getElementById('screen-leaderboard'),
  profile: document.getElementById('screen-profile'),
  tabbar: document.getElementById('tabbar'),
  toast: document.getElementById('toast'),
};

/* ============================================================================================================
 * boot
 * ========================================================================================================== */

async function boot() {
  try {
    state.pack = await loadPack(PACK_ID, 'content');
    dom.learnLoading.hidden = true;
    if (state.pack.errors.length) showPackErrors(state.pack.errors);
    if (!state.progress.publishSetVersion) {
      state.progress.publishSetVersion = state.pack.publishSetVersion;
      saveState(state.progress);
    }
  } catch (err) {
    dom.learnLoading.hidden = true;
    dom.learnError.hidden = false;
    dom.learnError.innerHTML = `<strong>بستهٔ محتوایی بارگذاری نشد.</strong><div>${escapeHtml(err.message)}</div>`;
    return;
  }
  bindChrome();
  window.addEventListener('hashchange', () => render());
  render();
  probeEngines();
}

function bindChrome() {
  dom.tabbar.addEventListener('click', (ev) => {
    const btn = ev.target.closest('.tab');
    if (!btn) return;
    navigateToTab(btn.dataset.tab);
  });
  window.addEventListener('scroll', () => {
    dom.topbar.classList.toggle('is-scrolled', window.scrollY > 4);
  }, { passive: true });
  document.getElementById('btn-reload-learn').addEventListener('click', async () => {
    state.pack = await loadPack(PACK_ID, 'content');
    toast('محتوا دوباره بارگذاری شد');
    render();
  });
  for (const frame of ['practice-frame', 'max-frame']) {
    const f = document.getElementById(frame);
    f.addEventListener('load', () => {
      try {
        // same-origin: the localization layer is injected by the preview host, but we also set the document
        // direction defensively in case the engine's own HTML wins.
        const doc = f.contentDocument;
        if (doc && doc.documentElement) {
          doc.documentElement.setAttribute('dir', 'rtl');
          doc.documentElement.setAttribute('lang', 'fa');
        }
      } catch { /* cross-origin fallback: the host handles it */ }
    });
  }
}

function navigateToTab(tab) {
  const routes = {
    learn: () => { const last = readResume(); location.hash = last ? `#/lesson/${last.tutorialId}/${last.lessonId}` : '#/learn'; },
    practice: () => { location.hash = '#/practice'; },
    max: () => { location.hash = '#/max'; },
    leaderboard: () => { location.hash = '#/leaderboard'; },
    profile: () => { location.hash = '#/profile'; },
  };
  if (tab === 'learn' && state.route.name.startsWith('lesson')) return; // already in Learn
  (routes[tab] || routes.learn)();
}

/* ============================================================================================================
 * router
 * ========================================================================================================== */

function parseRoute() {
  const raw = (location.hash || '#/learn').replace(/^#/, '');
  const parts = raw.split('/').filter(Boolean);
  if (!parts.length) return { name: 'learn' };
  const [head, a, b] = parts;
  if (head === 'track') return { name: 'track', trackId: Number(a) };
  if (head === 'tutorial') return { name: 'tutorial', trackId: Number(a), tutorialId: Number(b) };
  if (head === 'lesson') return { name: 'lesson', tutorialId: Number(a), lessonId: Number(b) };
  if (head === 'practice') return { name: 'practice' };
  if (head === 'max') return { name: 'max' };
  if (head === 'leaderboard') return { name: 'leaderboard' };
  if (head === 'profile') return { name: 'profile' };
  return { name: 'learn' };
}

function render() {
  state.route = parseRoute();
  const route = state.route;
  const tab = route.name === 'practice' ? 'practice'
    : route.name === 'max' ? 'max'
      : route.name === 'leaderboard' ? 'leaderboard'
        : route.name === 'profile' ? 'profile' : 'learn';
  state.tab = tab;
  setTab(tab);
  for (const section of ['learn', 'practice', 'max', 'leaderboard', 'profile']) {
    const node = document.getElementById(`screen-${section}`);
    if (node) node.hidden = section !== tab;
  }
  switch (route.name) {
    case 'learn': renderLearnHome(); break;
    case 'track': renderTrack(route.trackId); break;
    case 'tutorial': renderTutorial(route.trackId, route.tutorialId); break;
    case 'lesson': renderLesson(route.tutorialId, route.lessonId); break;
    case 'practice': activateEngine('practice'); break;
    case 'max': activateEngine('max'); break;
    case 'leaderboard': renderLeaderboard(); break;
    case 'profile': renderProfile(); break;
    default: renderLearnHome();
  }
  window.scrollTo({ top: 0, behavior: 'instant' in window ? 'instant' : 'auto' });
}

function setTab(tab) {
  const labels = { learn: 'یادگیری', practice: 'تمرین و آزمون', max: 'مکس', leaderboard: 'رتبه‌بندی', profile: 'پروفایل' };
  dom.topbarTitle.textContent = labels[tab] || 'میمو';
  for (const btn of dom.tabbar.querySelectorAll('.tab')) {
    if (btn.dataset.tab === tab) btn.setAttribute('aria-current', 'page');
    else btn.removeAttribute('aria-current');
  }
}

/* ============================================================================================================
 * Learn — home
 * ========================================================================================================== */

function renderLearnHome() {
  const root = dom.learnRoot;
  root.innerHTML = '';
  const stats = globalStats(state.progress);
  const resume = readResume();
  const lastLesson = resume ? state.pack.findByKey(`${resume.tutorialId}:${resume.lessonId}`) : null;

  const hero = el('section', { class: 'hero' });
  hero.appendChild(el('h1', {}, 'مسیر یادگیری شما'));
  hero.appendChild(el('p', {}, `${state.pack.title} — ${state.pack.tracks.length} مسیر، ${countLessons()} درس. همهٔ درس‌ها بدون اینترنت باز می‌شوند.`));
  const actions = el('div', { class: 'hero__actions' });
  const primary = el('button', { class: 'btn btn--accent' }, lastLesson ? 'ادامهٔ یادگیری' : 'شروع یادگیری');
  primary.addEventListener('click', () => {
    if (lastLesson) location.hash = `#/lesson/${lastLesson.tutorialId}/${lastLesson.lessonId}`;
    else location.hash = `#/track/${state.pack.tracks[0].id}`;
  });
  actions.appendChild(primary);
  const browse = el('button', { class: 'btn btn--ghost' }, 'همهٔ مسیرها');
  browse.style.color = '#eaf6ee';
  browse.style.borderColor = 'rgba(234,246,238,.35)';
  browse.addEventListener('click', () => {
    document.querySelector('.tracks-section')?.scrollIntoView({ behavior: 'smooth', block: 'start' });
  });
  actions.appendChild(browse);
  hero.appendChild(actions);

  const heroStats = el('div', { class: 'hero__stats' });
  heroStats.appendChild(statBlock(`${stats.lessonsSolved}`, 'درس حل‌شده'));
  heroStats.appendChild(statBlock(`${stats.firstTry}`, 'پاسخ درست در تلاش اول'));
  heroStats.appendChild(statBlock(`${stats.accuracy}٪`, 'دقت کلی'));
  hero.appendChild(heroStats);
  root.appendChild(hero);

  if (lastLesson) {
    root.appendChild(el('div', { class: 'section-head' }, el('h2', {}, 'آخرین درس')));
    const card = el('div', { class: 'card track-card' });
    card.appendChild(el('div', { class: 'track-card__meta' }, `${lastLesson.tutorialTitle} • ${lastLesson.chapterTitle}`));
    card.appendChild(el('h3', {}, lastLesson.lesson.title || `درس ${lastLesson.lessonId}`));
    const btn = el('button', { class: 'btn btn--block' }, 'ادامه');
    btn.addEventListener('click', () => { location.hash = `#/lesson/${lastLesson.tutorialId}/${lastLesson.lessonId}`; });
    card.appendChild(btn);
    root.appendChild(card);
  }

  const section = el('section', { class: 'tracks-section' });
  section.appendChild(el('div', { class: 'section-head' },
    el('h2', {}, 'مسیرهای یادگیری'),
    el('span', { class: 'chip' }, 'محتوای نمایشی')));
  const stack = el('div', { class: 'stack' });
  for (const track of state.pack.tracks) {
    stack.appendChild(trackCard(track));
  }
  section.appendChild(stack);
  root.appendChild(section);

  root.appendChild(el('div', { class: 'section-head' }, el('h2', {}, 'پیشنهاد برای امروز')));
  const tiles = el('div', { class: 'tile-grid' });
  tiles.appendChild(tile(`${stats.attempts}`, 'تلاش ثبت‌شده'));
  tiles.appendChild(tile(`${countLessons() - stats.lessonsSolved}`, 'درس باقی‌مانده'));
  tiles.appendChild(tile('آفلاین', 'وضعیت موتور یادگیری'));
  root.appendChild(tiles);
}

function statBlock(value, label) {
  const box = el('div', {});
  box.appendChild(el('b', {}, value));
  box.appendChild(el('span', {}, label));
  return box;
}

function tile(value, label) {
  const node = el('div', { class: 'tile' });
  node.appendChild(el('b', {}, value));
  node.appendChild(el('span', {}, label));
  return node;
}

function trackCard(track) {
  const progress = trackProgress(state.progress, track, state.pack.tutorialsById);
  const card = el('button', { class: 'card track-card' });
  const top = el('div', { class: 'track-card__top' });
  top.appendChild(el('h3', {}, track.title || `مسیر ${track.id}`));
  top.appendChild(el('span', { class: 'chip' }, `${progress.percent}٪`));
  card.appendChild(top);
  if (track.description) card.appendChild(el('div', { class: 'track-card__meta' }, track.description));
  const bar = el('div', { class: 'progress' }, el('span', { style: `width:${progress.percent}%` }));
  card.appendChild(bar);
  card.appendChild(el('div', { class: 'progress-label' },
    el('span', {}, `${progress.solved} از ${progress.total} درس`),
    el('span', {}, `${(track.sections || []).length} بخش`)));
  card.addEventListener('click', () => { location.hash = `#/track/${track.id}`; });
  return card;
}

/* ============================================================================================================
 * Learn — track & tutorial
 * ========================================================================================================== */

function renderTrack(trackId) {
  const track = state.pack.tracks.find((t) => Number(t.id) === Number(trackId));
  const root = dom.learnRoot;
  root.innerHTML = '';
  if (!track) { root.appendChild(el('div', { class: 'error-box' }, 'این مسیر پیدا نشد.')); return; }
  root.appendChild(crumbs([['یادگیری', '#/learn'], [track.title || 'مسیر', null]]));
  const progress = trackProgress(state.progress, track, state.pack.tutorialsById);
  const head = el('div', { class: 'card' });
  head.appendChild(el('h1', {}, track.title || `مسیر ${track.id}`));
  if (track.description) head.appendChild(el('p', { class: 'muted tiny' }, track.description));
  head.appendChild(el('div', { class: 'progress' }, el('span', { style: `width:${progress.percent}%` })));
  head.appendChild(el('div', { class: 'progress-label' },
    el('span', {}, `${progress.solved} از ${progress.total} درس`), el('span', {}, `${progress.percent}٪`)));
  root.appendChild(head);

  for (const section of track.sections || []) {
    const block = el('section', { class: 'section-block' });
    block.appendChild(el('div', { class: 'section-block__title' }, section.name || 'بخش'));
    for (const ref of section.tutorials || []) {
      const tutorial = state.pack.tutorialsById.get(Number(ref.id));
      if (!tutorial) continue;
      const tp = tutorialProgress(state.progress, tutorial);
      const row = el('button', { class: 'tutorial-row' });
      row.appendChild(el('span', { class: 'tutorial-row__icon' }, tutorial.type === 'practice' ? '🏋️' : '📘'));
      const body = el('span', { class: 'grow' });
      body.appendChild(el('span', { class: 'tutorial-row__title truncate' }, tutorial.title || `توتوریال ${tutorial.id}`));
      body.appendChild(el('span', { class: 'tutorial-row__sub' }, `${(tutorial.chapters || []).length} فصل • ${tp.total} درس`));
      row.appendChild(body);
      row.appendChild(el('span', { class: 'tutorial-row__ring' }, `${tp.percent}٪`));
      row.addEventListener('click', () => { location.hash = `#/tutorial/${track.id}/${tutorial.id}`; });
      block.appendChild(row);
    }
    root.appendChild(block);
  }
}

function renderTutorial(trackId, tutorialId) {
  const root = dom.learnRoot;
  root.innerHTML = '';
  const track = state.pack.tracks.find((t) => Number(t.id) === Number(trackId));
  const tutorial = state.pack.tutorialsById.get(Number(tutorialId));
  if (!track || !tutorial) { root.appendChild(el('div', { class: 'error-box' }, 'این توتوریال پیدا نشد.')); return; }
  root.appendChild(crumbs([['یادگیری', '#/learn'], [track.title, `#/track/${track.id}`], [tutorial.title, null]]));
  const tp = tutorialProgress(state.progress, tutorial);
  const head = el('div', { class: 'card' });
  head.appendChild(el('h1', {}, tutorial.title || `توتوریال ${tutorial.id}`));
  if (tutorial.summary) head.appendChild(el('p', { class: 'muted tiny' }, tutorial.summary));
  head.appendChild(el('div', { class: 'progress' }, el('span', { style: `width:${tp.percent}%` })));
  head.appendChild(el('div', { class: 'progress-label' },
    el('span', {}, `${tp.solved} از ${tp.total} درس`), el('span', {}, `${tp.percent}٪`)));
  root.appendChild(head);

  for (const chapter of tutorial.chapters || []) {
    const cp = chapterProgress(state.progress, chapter, tutorial.id);
    const box = el('div', { class: 'chapter' });
    const headRow = el('div', { class: 'chapter__head' });
    headRow.appendChild(el('span', { class: 'lesson-dot' + (cp.complete ? ' is-solved' : '') }, cp.complete ? '✓' : '•'));
    const grow = el('div', { class: 'grow' });
    grow.appendChild(el('div', { class: 'tutorial-row__title' }, chapter.title || `فصل ${chapter.id}`));
    grow.appendChild(el('div', { class: 'tutorial-row__sub' }, `${cp.solved} از ${cp.total} درس حل شده`));
    headRow.appendChild(grow);
    headRow.appendChild(el('span', { class: 'chip' + (cp.complete ? ' chip--ok' : '') }, cp.complete ? 'کامل' : 'در جریان'));
    box.appendChild(headRow);
    const body = el('div', { class: 'chapter__body' });
    for (const lesson of chapter.lessons || []) {
      const row = getRow(state.progress, lesson.id, tutorial.id);
      const solved = row && row.tries >= 1;
      const started = row && row.attempts > 0;
      const item = el('button', { class: 'lesson-row' });
      item.appendChild(el('span', { class: 'lesson-dot' + (solved ? ' is-solved' : started ? ' is-progress' : '') }, solved ? '✓' : started ? '●' : ''));
      const g = el('div', { class: 'grow' });
      g.appendChild(el('div', { class: 'lesson-row__title' }, lesson.title || `درس ${lesson.id}`));
      const meta = [lesson.contentType === 'executableFiles' ? 'اجرایی' : 'تعاملی'];
      if (row) meta.push(`تلاش ${row.attempts}`);
      g.appendChild(el('div', { class: 'lesson-row__meta' }, meta.join(' • ')));
      item.appendChild(g);
      item.appendChild(el('span', { class: 'chip' }, solved ? 'حل‌شده' : started ? 'نیمه‌کاره' : 'شروع'));
      item.addEventListener('click', () => { location.hash = `#/lesson/${tutorial.id}/${lesson.id}`; });
      body.appendChild(item);
    }
    box.appendChild(body);
    root.appendChild(box);
  }
}

/* ============================================================================================================
 * Learn — lesson player
 * ========================================================================================================== */

function renderLesson(tutorialId, lessonId) {
  const root = dom.learnRoot;
  root.innerHTML = '';
  const entry = state.pack.findByKey(`${tutorialId}:${lessonId}`);
  if (!entry) {
    root.appendChild(el('div', { class: 'error-box' }, 'این درس در بستهٔ محتوایی نیست.'));
    return;
  }
  const { lesson, tutorialId: tid, trackId, tutorialVersion, chapterTitle, tutorialTitle, chapterId } = entry;
  const row = ensureRow(state.progress, {
    lessonId: lesson.id,
    tutorialId: tid,
    tutorialVersion,
    trackId,
    publishSetVersion: state.pack.publishSetVersion,
    isPractice: false,
  });
  saveState(state.progress);
  writeResume({ tutorialId: tid, lessonId: lesson.id });

  const screen = el('div', { class: 'lesson-screen' });
  const top = el('div', { class: 'lesson-top' });
  const back = el('button', { class: 'icon-btn', title: 'بازگشت' }, '→');
  back.addEventListener('click', () => { location.hash = `#/tutorial/${trackId}/${tid}`; });
  top.appendChild(back);
  const tp = tutorialProgress(state.progress, state.pack.tutorialsById.get(Number(tid)));
  const barWrap = el('div', { class: 'lesson-top__progress' });
  barWrap.appendChild(el('div', { class: 'progress' }, el('span', { style: `width:${Math.max(6, tp.percent)}%` })));
  top.appendChild(barWrap);
  top.appendChild(el('span', { class: 'chip' }, `${chapterTitle || 'فصل'} • ${tutorialTitle || ''}`));
  screen.appendChild(top);
  screen.appendChild(el('h1', { class: 'lesson-title' }, lesson.title || `درس ${lesson.id}`));
  if (Array.isArray(lesson.objectives) && lesson.objectives.length) {
    const obj = el('div', { class: 'lesson-objectives' });
    obj.appendChild(el('h3', {}, 'در این درس یاد می‌گیرید'));
    const ul = el('ul');
    for (const goal of lesson.objectives) ul.appendChild(el('li', {}, goal));
    obj.appendChild(ul);
    screen.appendChild(obj);
  }

  const bodySource = lesson.body || lesson.interactiveContent?.body || '';
  const { ast, errors, warnings } = parseLesson(bodySource);
  if (errors.length) {
    const box = el('div', { class: 'error-box' });
    box.appendChild(el('strong', {}, 'سند درس خطای ساختاری دارد:'));
    const ul = el('ul');
    for (const e of errors) ul.appendChild(el('li', {}, `${e.message} (موقعیت ${e.offset})`));
    box.appendChild(ul);
    screen.appendChild(box);
  }

  const bodyHost = el('div', {});
  const runtime = createLessonRuntime({ node: bodyHost, lesson, handlers: {} });
  const { root: rendered, blocks } = renderDocument(ast, runtime.ctx);
  const bodyWrap = el('div', { class: 'lesson-body' });
  bodyWrap.appendChild(rendered);
  bodyHost.appendChild(bodyWrap);
  screen.appendChild(bodyHost);
  if (warnings.length) {
    screen.appendChild(el('div', { class: 'chip chip--warn', title: warnings.join(' | ') }, `${warnings.length} هشدار ساختاری در سند درس`));
  }

  const feedback = el('div', { class: 'feedback', hidden: '' });
  screen.appendChild(feedback);

  const actions = el('div', { class: 'lesson-actions' });
  const inner = el('div', { class: 'lesson-actions__inner' });
  const primary = el('button', { class: 'btn btn--accent btn--block' }, runtime.answers.size ? 'بررسی پاسخ' : 'ادامه');
  const hint = el('span', { class: 'tiny muted' }, runtime.answers.size ? 'Enter برای بررسی' : 'بدون پرسش');
  inner.appendChild(primary);
  inner.appendChild(hint);
  actions.appendChild(inner);
  screen.appendChild(actions);
  root.appendChild(screen);

  wireInteractions(bodyHost);
  state.lessonRuntime = runtime;
  let phase = 'answering';

  bodyHost.addEventListener('answer-submit', () => { if (phase === 'answering') primary.click(); });

  primary.addEventListener('click', () => {
    if (phase === 'answering') {
      const { verdict, results } = runtime.submit();
      runtime.applyVisibility(bodyHost);
      applyResult(state.progress, row, verdict, applySubmission);
      saveState(state.progress);
      paintFeedback(feedback, verdict, results, lesson);
      phase = verdict === CORRECT ? 'done' : 'retry';
      primary.textContent = verdict === CORRECT ? 'ادامه' : 'تلاش دوباره';
      primary.classList.toggle('btn--accent', verdict === CORRECT);
      hint.textContent = verdict === CORRECT ? 'درس ثبت شد' : 'می‌توانید پاسخ را اصلاح کنید';
      if (verdict === CORRECT) toast('درس حل شد و در پیشرفت ذخیره شد');
      return;
    }
    if (phase === 'retry') {
      phase = 'answering';
      feedback.hidden = true;
      resetLessonMarks();
      return;
    }
    // done → next lesson or back to chapter
    const next = nextLesson(state.pack, { tutorialId: tid, lessonId: lesson.id });
    if (next) location.hash = `#/lesson/${next.tutorialId}/${next.lessonId}`;
    else { location.hash = `#/tutorial/${trackId}/${tid}`; toast('پایان این بخش'); }
  });

  function resetLessonMarks() {
    for (const wrapper of runtime.answers.keys()) {
      wrapper.classList.remove('is-correct', 'is-partial', 'is-wrong');
      const fb = wrapper.querySelector?.('.inline-feedback');
      if (fb) fb.textContent = '';
    }
    runtime.applyVisibility(bodyHost);
    primary.textContent = 'بررسی پاسخ';
    hint.textContent = 'Enter برای بررسی';
  }
}

function paintFeedback(panel, verdict, results, lesson) {
  panel.hidden = false;
  panel.className = `feedback feedback--${verdict === CORRECT ? 'correct' : verdict === PARTIAL ? 'partial' : 'wrong'}`;
  panel.innerHTML = '';
  const titles = {
    [CORRECT]: '✅ درست است',
    [PARTIAL]: '🟡 تقریباً درست',
    [INCORRECT]: '❌ درست نیست',
  };
  panel.appendChild(el('div', { class: 'feedback__title' }, titles[verdict]));
  const notes = {
    [CORRECT]: 'پاسخ ثبت شد. بلوک‌های «درست» و «همیشه» نمایش داده می‌شوند.',
    [PARTIAL]: 'متن پاسخ با پاسخ درست یکسان است اما نوشتار دقیق آن متفاوت است؛ در Mimo این حالت فقط برای پاسخ‌های متنی ممکن است.',
    [INCORRECT]: 'بلوک‌های راهنما و پاسخ صحیح نمایش داده می‌شود. می‌توانید دوباره تلاش کنید.',
  };
  panel.appendChild(el('div', { class: 'feedback__body' }, notes[verdict]));
  if (Array.isArray(lesson.feedback) && lesson.feedback.length) {
    const ul = el('ul');
    for (const item of lesson.feedback) ul.appendChild(el('li', {}, item));
    panel.appendChild(ul);
  }
  if (results.length) {
    const list = el('div', { class: 'stack' });
    for (const r of results) {
      const label = r.spec.kind === 'selection'
        ? 'انتخاب گزینه'
        : 'پاسخ متنی';
      list.appendChild(el('div', { class: 'setting-row' },
        el('span', {}, label),
        el('span', { class: `chip ${r.verdict === CORRECT ? 'chip--ok' : r.verdict === PARTIAL ? 'chip--warn' : 'chip--danger'}` },
          r.verdict === CORRECT ? 'درست' : r.verdict === PARTIAL ? 'نزدیک' : 'نادرست')));
    }
    panel.appendChild(list);
  }
}

/* ============================================================================================================
 * Leaderboard & profile (local, no server)
 * ========================================================================================================== */

function renderLeaderboard() {
  const root = dom.leaderboard;
  root.innerHTML = '';
  const stats = globalStats(state.progress);
  root.appendChild(el('div', { class: 'section-head' },
    el('h2', {}, 'رتبه‌بندی'),
    el('span', { class: 'chip' }, 'محلی و نمایشی')));
  root.appendChild(el('p', { class: 'tiny muted' },
    'رتبه‌بندی در Mimo از سرور می‌آمد. در این پیش‌نمایش آفلاین، جدول فقط از پیشرفت محلی شما ساخته می‌شود و '
    + 'هیچ داده‌ای به بیرون فرستاده نمی‌شود.'));

  const peers = [
    { name: 'شما', score: stats.lessonsSolved * 10 + stats.firstTry * 4, me: true },
    { name: 'کاربر نمونهٔ الف', score: 120 },
    { name: 'کاربر نمونهٔ ب', score: 95 },
    { name: 'کاربر نمونهٔ پ', score: 60 },
  ].sort((a, b) => b.score - a.score);

  const top3 = peers.slice(0, 3);
  const podium = el('div', { class: 'podium' });
  [top3[1], top3[0], top3[2]].forEach((p, i) => {
    if (!p) return;
    const item = el('div', { class: `podium__item ${i === 1 ? 'podium__item--first' : ''}` });
    item.appendChild(el('div', { class: 'podium__avatar' }, p.name.slice(0, 1)));
    item.appendChild(el('div', { class: 'tiny' }, p.name));
    item.appendChild(el('div', { class: 'podium__bar' }));
    podium.appendChild(item);
  });
  root.appendChild(podium);

  const list = el('div', { class: 'stack' });
  peers.forEach((p, idx) => {
    const row = el('div', { class: `rank-row ${p.me ? 'is-me' : ''}` });
    row.appendChild(el('div', { class: 'rank-row__pos' }, `${idx + 1}`));
    const g = el('div', { class: 'grow' });
    g.appendChild(el('div', { class: 'lesson-row__title' }, p.name));
    g.appendChild(el('div', { class: 'lesson-row__meta' }, p.me ? 'پیشرفت واقعی شما' : 'کاربر نمونه'));
    row.appendChild(g);
    row.appendChild(el('span', { class: 'chip' }, `${p.score} امتیاز`));
    list.appendChild(row);
  });
  root.appendChild(list);
}

function renderProfile() {
  const root = dom.profile;
  root.innerHTML = '';
  const stats = globalStats(state.progress);
  const head = el('div', { class: 'profile-head' });
  head.appendChild(el('div', { class: 'profile-avatar' }, 'م'));
  head.appendChild(el('h1', {}, 'کاربر محلی'));
  head.appendChild(el('div', { class: 'tiny muted' }, 'پیشرفت روی همین دستگاه ذخیره می‌شود'));
  root.appendChild(head);

  const tiles = el('div', { class: 'tile-grid' });
  tiles.appendChild(tile(`${stats.lessonsSolved}`, 'درس حل‌شده'));
  tiles.appendChild(tile(`${stats.firstTry}`, 'تلاش اول'));
  tiles.appendChild(tile(`${stats.attempts}`, 'کل تلاش‌ها'));
  tiles.appendChild(tile(`${stats.accuracy}٪`, 'دقت'));
  root.appendChild(tiles);

  root.appendChild(el('div', { class: 'section-head' }, el('h2', {}, 'تنظیمات')));
  const list = el('div', { class: 'settings-list' });

  list.appendChild(settingRow('ذخیره‌سازی پیشرفت', 'محلی (localStorage)', 'آفلاین'));
  list.appendChild(settingRow('نسخهٔ بستهٔ محتوایی', `publishSetVersion ${state.pack.publishSetVersion}`, `${countLessons()} درس`));
  list.appendChild(settingRow('موتور تمرین و آزمون', state.engines.practice ? 'در دسترس' : 'خارج از دسترس', 'EPM'));
  list.appendChild(settingRow('موتور مکس', state.engines.max ? 'در دسترس' : 'خارج از دسترس', 'LearnHarness'));

  const exportBtn = el('button', { class: 'btn btn--ghost btn--sm' }, 'دریافت فایل پشتیبان');
  exportBtn.addEventListener('click', () => {
    const blob = new Blob([JSON.stringify(state.progress, null, 2)], { type: 'application/json' });
    const a = document.createElement('a');
    a.href = URL.createObjectURL(blob);
    a.download = 'mimo-progress-backup.json';
    a.click();
    URL.revokeObjectURL(a.href);
    toast('فایل پشتیبان ساخته شد');
  });
  const resetBtn = el('button', { class: 'btn btn--ghost btn--sm' }, 'پاک کردن پیشرفت');
  resetBtn.addEventListener('click', () => {
    if (!confirm('همهٔ پیشرفت محلی پاک شود؟ این عمل بازگشت‌پذیر نیست.')) return;
    clearState();
    state.progress = loadState();
    toast('پیشرفت پاک شد');
    render();
  });
  const row = el('div', { class: 'setting-row' },
    el('span', {}, 'مدیریت داده'),
    el('span', { class: 'row' }, exportBtn, resetBtn));
  list.appendChild(row);
  root.appendChild(list);

  root.appendChild(el('div', { class: 'section-head' }, el('h2', {}, 'دربارهٔ سه موتور')));
  const about = el('div', { class: 'card' });
  about.appendChild(el('p', { class: 'tiny', style: 'margin:0' },
    'این برنامه سه موتور مستقل را در یک پوسته کنار هم می‌گذارد: «یادگیری» موتور آفلاین Mimo، «تمرین و آزمون» موتور EPM و '
    + '«مکس» موتور LearnHarness. هیچ‌کدام داده‌شان را با دیگری به اشتراک نمی‌گذارند و بین آن‌ها همگام‌سازی خودکار وجود ندارد.'));
  root.appendChild(about);
}

function settingRow(label, value, chip) {
  return el('div', { class: 'setting-row' },
    el('span', {}, label),
    el('span', { class: 'row' }, el('span', { class: 'tiny muted' }, value), chip ? el('span', { class: 'chip' }, chip) : null));
}

/* ============================================================================================================
 * Engines
 * ========================================================================================================== */

async function activateEngine(name) {
  const frame = document.getElementById(`${name}-frame`);
  const status = document.getElementById(`${name}-status`);
  const offline = document.getElementById(`${name}-offline`);
  if (!frame.dataset.loaded) {
    frame.src = name === 'practice' ? '/practice/' : '/max/';
    frame.dataset.loaded = '1';
  }
  const up = await checkEngine(name);
  state.engines[name] = up;
  status.textContent = up ? 'متصل' : 'خارج از دسترس';
  status.classList.toggle('is-up', up);
  status.classList.toggle('is-down', !up);
  if (offline) offline.hidden = up;
  if (frame) frame.hidden = !up;
}

async function checkEngine(name) {
  const url = name === 'practice' ? '/practice/api/health' : '/max/api/health';
  try {
    const res = await fetch(url, { method: 'GET', cache: 'no-store' });
    if (res.ok) return true;
    // engines that do not expose /api/health are still "up" if their root answers
    const root = await fetch(name === 'practice' ? '/practice/' : '/max/', { cache: 'no-store' });
    return root.ok;
  } catch {
    return false;
  }
}

async function probeEngines() {
  state.engines.practice = await checkEngine('practice');
  state.engines.max = await checkEngine('max');
}

/* ============================================================================================================
 * helpers
 * ========================================================================================================== */

function crumbs(items) {
  const node = el('div', { class: 'crumbs' });
  items.forEach(([label, href], idx) => {
    if (href) {
      const b = el('button', {}, label);
      b.addEventListener('click', () => { location.hash = href; });
      node.appendChild(b);
    } else {
      node.appendChild(el('span', {}, label));
    }
    if (idx < items.length - 1) node.appendChild(el('span', {}, '‹'));
  });
  return node;
}

let toastTimer = null;
function toast(message) {
  dom.toast.textContent = message;
  dom.toast.classList.add('is-visible');
  clearTimeout(toastTimer);
  toastTimer = setTimeout(() => dom.toast.classList.remove('is-visible'), 2400);
}

function readResume() {
  try { return JSON.parse(localStorage.getItem(RESUME_KEY) || 'null'); } catch { return null; }
}
function writeResume(value) {
  try { localStorage.setItem(RESUME_KEY, JSON.stringify(value)); } catch { /* ignore quota */ }
}

function countLessons() {
  let total = 0;
  for (const track of state.pack?.tracks || []) {
    for (const section of track.sections || []) {
      for (const ref of section.tutorials || []) {
        const tutorial = state.pack.tutorialsById.get(Number(ref.id));
        for (const chapter of tutorial?.chapters || []) total += (chapter.lessons || []).length;
      }
    }
  }
  return total;
}

function showPackErrors(errors) {
  dom.learnError.hidden = false;
  dom.learnError.innerHTML = `<strong>بستهٔ محتوایی هشدار دارد:</strong><ul>${errors.map((e) => `<li>${escapeHtml(e)}</li>`).join('')}</ul>`;
}

function escapeHtml(text) {
  return String(text).replace(/[&<>"']/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
}

boot();
