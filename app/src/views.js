/**
 * Additional screens required by the three learning routes, the question bank
 * and the settings surface. They are injected at runtime so that the approved
 * phone markup in assets/phone.html stays BYTE-IDENTICAL to v12.5-fa.
 *
 * Every element here reuses an EXISTING prototype class and CSS token. No new
 * colours, fonts, radii or icon shapes are introduced. These additions add
 * capability, not a redesign.
 */

import { ROUTES } from './engine.js';
import { STUDY_PLAN_STAGES, planStatus } from './routes.js';
import { PATHS, SUBJECTS } from './fixtures.js';

const esc = (v) => String(v).replace(/&/g, '&amp;').replace(/</g, '&lt;')
  .replace(/>/g, '&gt;').replace(/"/g, '&quot;');

export function mountViews(doc, { store, bank, curriculum }) {
  const phone = doc.getElementById('phone');
  const tabs = doc.getElementById('tabs');
  if (!phone || !tabs) return { mounted: false };
  const insert = (html) => {
    const tpl = doc.createElement('template');
    tpl.innerHTML = html.trim();
    const node = tpl.content.firstElementChild;
    phone.insertBefore(node, tabs);
    return node;
  };

  // ---- 1. Route switcher on the approved «انتخاب مسیر» screen ----------------
  const spBody = doc.querySelector('[data-screen="select-path"] .sp-body');
  const routeChips = doc.createElement('div');
  routeChips.className = 'chips';
  routeChips.id = 'routeChips';
  routeChips.setAttribute('data-role', 'route-switcher');
  routeChips.style.padding = '0 0 10px';
  routeChips.innerHTML = Object.values(ROUTES).map((r) =>
    `<button type="button" class="chip" data-route="${r.key}">${esc(r.fa)}</button>`).join('');
  spBody.insertBefore(routeChips, spBody.firstChild);
  const routeNote = doc.createElement('div');
  routeNote.className = 'banner warn';
  routeNote.setAttribute('data-role', 'route-note');
  routeNote.style.margin = '0 0 12px';
  routeNote.textContent = 'مسیر یادگیری خود را انتخاب کنید؛ حالت فعلی در حافظهٔ محلی ذخیره میشود.';
  spBody.insertBefore(routeNote, routeChips.nextSibling);

  // ---- 2. Study-Plan Learning Path screen -----------------------------------
  insert(`
    <section class="screen mimo" data-screen="study-plan" data-role="study-plan">
      <div class="sp-top"><button class="x" data-nav="learn"><span data-icon="ic_arrow_back_24" data-size="24" data-mono="1"></span></button><b>مسیر یادگیری برنامهمحور</b></div>
      <div class="sd-hero">
        <span class="kick">مسیر و وضعیت برنامه</span>
        <h2 id="planTitle">برنامهٔ مطالعاتی</h2>
        <p id="planDesc">مسیر برنامهمحور؛ وضعیت گامها بهصورت محلی نگهداری میشود.</p>
        <span class="sp-scope" id="planStage">شروع برنامه</span>
        <div class="cbar"><i id="planBar" style="width:0%"></i></div>
      </div>
      <div class="chips" id="planPaths" style="padding-bottom:8px">
        ${PATHS.map((p) => `<button type="button" class="chip" data-plan-path="${p.id}">${esc(p.fa)}</button>`).join('')}
      </div>
      <div class="sec-h">گامهای برنامه</div>
      <div class="selfbox" id="planStages"></div>
      <div class="banner warn" style="margin:0 14px 10px">دادهها آزمایشیاند. آزمون اولیه، رفع اشکال و آزمون نهایی فقط بهصورت ساختار/وضعیت رزرو شدهاند و هنوز اجرا نمیشوند.</div>
      <button class="sd-cta" id="planAction">فعال کردن برنامه</button>
      <button class="sd-link" data-nav="select-path">تغییر مسیر</button>
    </section>`);

  // ---- 3. Question bank / practice sessions ----------------------------------
  insert(`
    <section class="screen mimo" data-screen="practice-bank" data-role="practice-bank">
      <div class="sp-top"><button class="x" data-nav="exam-hub"><span data-icon="ic_arrow_back_24" data-size="24" data-mono="1"></span></button><b>بانک سؤال</b></div>
      <div class="sd-hero">
        <span class="kick">ساختار بانک سؤال</span>
        <h2>تمرین بدون محدودیت زمان</h2>
        <p>نشستهای تمرینی از همان کامپوننتهای پاسخگویی آزمون استفاده میکنند.</p>
        <span class="sp-scope" id="bankScope">۰ سؤال نمونه</span>
        <div class="cbar"><i id="bankBar" style="width:0%"></i></div>
      </div>
      <div class="chips" id="bankFilters" style="padding-bottom:8px">
        <button type="button" class="chip on" data-bank-filter="all">همه</button>
        ${SUBJECTS.map((s) => `<button type="button" class="chip" data-bank-filter="${esc(s)}">${esc(s)}</button>`).join('')}
      </div>
      <div id="bankList" style="padding:0 14px"></div>
      <div id="bankResult"></div>
      <button class="sd-cta" id="bankStart">ثبت پاسخها و پایان نشست</button>
      <button class="sd-link" data-nav="exam-hub">بازگشت به آزمونها</button>
    </section>`);

  // ---- 3b. Leaderboard display states (local placeholder views) ------------
  const lb = doc.querySelector('[data-screen="leaderboard"]');
  const lbChips = doc.createElement('div');
  lbChips.className = 'chips';
  lbChips.id = 'leaderboardStates';
  lbChips.style.paddingBottom = '8px';
  lbChips.innerHTML = [
    ['weekly', 'این هفته'], ['all', 'کلی'], ['empty', 'بدون داده'],
  ].map(([k, v], i) => `<button type="button" class="chip ${i === 0 ? 'on' : ''}" data-lb-state="${k}">${esc(v)}</button>`).join('');
  lb.insertBefore(lbChips, lb.firstChild);
  const lbRows = doc.createElement('div');
  lbRows.id = 'leaderboardRows';
  lb.appendChild(lbRows);

  // Profile gear opens the settings modal (existing delegated data-sheet handler).
  const gear = doc.querySelector('[data-screen="profile"] .gear');
  if (gear) gear.setAttribute('data-sheet', 'settingsModal');

  // ---- 3c. Question-bank entry on the Practice landing screen ---------------
  const examHub = doc.querySelector('[data-screen="exam-hub"]');
  const examChips = examHub.querySelector('.chips');
  const statusLine = doc.createElement('div');
  statusLine.className = 'cat-meta';
  statusLine.id = 'examStatusLine';
  statusLine.setAttribute('data-role', 'exam-status');
  examChips.parentNode.insertBefore(statusLine, examChips.nextSibling);
  const bankLink = doc.createElement('div');
  bankLink.className = 'plink';
  bankLink.setAttribute('data-role', 'bank-entry');
  bankLink.innerHTML = '<span>بانک سؤال</span><span data-nav="practice-bank">＋ مرور و تمرین</span>';
  examHub.appendChild(bankLink);

  // ---- 3d. LearnHarness status surface on the approved AI screen -----------
  const ai = doc.querySelector('[data-screen="ai"]');
  const aiTop = ai.querySelector('.krow.ai-top');
  const harnessStatus = doc.createElement('div');
  harnessStatus.className = 'cat-meta';
  harnessStatus.id = 'harnessStatus';
  harnessStatus.setAttribute('data-role', 'harness-status');
  harnessStatus.style.margin = '0 14px 8px';
  aiTop.parentNode.insertBefore(harnessStatus, aiTop.nextSibling);
  const harnessPhases = doc.createElement('div');
  harnessPhases.className = 'chips';
  harnessPhases.id = 'harnessPhases';
  harnessPhases.style.padding = '0 14px 8px';
  harnessPhases.innerHTML = [
    ['measure', 'سنجش'], ['plan', 'برنامهریزی'], ['teach', 'آموزش'], ['practice', 'تمرین'],
  ].map(([k, v], i) => `<button type="button" class="chip ${i === 0 ? 'on' : ''}" data-harness-phase="${k}">${esc(v)}</button>`).join('');
  aiTop.parentNode.insertBefore(harnessPhases, harnessStatus.nextSibling);
  const harnessStart = doc.createElement('button');
  harnessStart.type = 'button';
  harnessStart.className = 'fchip ai-chip';
  harnessStart.id = 'harnessStart';
  harnessStart.setAttribute('data-harness-action', 'start');
  harnessStart.textContent = 'شروع جلسه';
  ai.querySelector('.ai-top-left').appendChild(harnessStart);

  // ---- 4. Settings / profile-actions modal (existing .modal-card language) ---
  insert(`
    <div class="modal" id="settingsModal" data-role="settings">
      <div class="modal-card">
        <div class="mtop"><span class="lbl">تنظیمات</span><button class="btn" data-close="settingsModal">بستن</button></div>
        <h2>پروفایل و تنظیمات</h2>
        <div class="selfbox" id="settingsRows"></div>
        <div class="banner warn" style="margin:12px 0">اپلیکیشن کاملاً آفلاین است؛ هیچ حساب، سرور یا پاسخ شبهای شبیهسازی نمیشود. همهٔ تغییرات روی این دستگاه ذخیره میشوند.</div>
        <div class="krow" style="justify-content:center">
          <button class="btn" id="settingsExport">خروجی گرفتن از وضعیت</button>
          <button class="btn" id="settingsReset">بازنشانی دادهها</button>
        </div>
      </div>
    </div>`);

  return { mounted: true, phone, tabs, bank, curriculum, store,
    routeChips, examHub, routeNote };
}

export function renderPlan(doc, store) {
  const { plan, index, stage } = planStatus(store);
  const title = doc.getElementById('planTitle');
  const stageEl = doc.getElementById('planStage');
  const bar = doc.getElementById('planBar');
  const list = doc.getElementById('planStages');
  const action = doc.getElementById('planAction');
  if (!title || !list) return;
  const path = PATHS.find((p) => p.id === plan.programId) || PATHS.find((p) => p.id === store.get('route.pathId')) || PATHS[0];
  title.textContent = path.fa;
  stageEl.textContent = plan.active ? `وضعیت: ${stage.fa}` : 'برنامه فعال نیست';
  bar.style.width = `${Math.round(((index + (plan.active ? 1 : 0)) / STUDY_PLAN_STAGES.length) * 100)}%`;
  doc.querySelectorAll('[data-plan-path]').forEach((b) => {
    b.classList.toggle('on', b.dataset.planPath === path.id);
  });
  list.innerHTML = STUDY_PLAN_STAGES.map((s, i) => {
    const state = i < index ? 'انجام شد' : (i === index ? (plan.active ? 'فعلی' : 'آماده') : 'قفل');
    return `<div class="selfrow" data-plan-stage="${s.key}"><span>${esc(s.fa)}</span><b>${esc(state)}</b></div>`;
  }).join('');
  action.textContent = plan.active ? 'گام بعدی برنامه' : 'فعال کردن برنامه';
  action.dataset.planAction = plan.active ? 'advance' : 'activate';
}

export function renderBank(doc, { bank, filter = 'all', answers = {} }) {
  const list = doc.getElementById('bankList');
  const scope = doc.getElementById('bankScope');
  const bar = doc.getElementById('bankBar');
  if (!list) return;
  const rows = bank.filter((q) => filter === 'all' || q.subject === filter);
  scope.textContent = `${rows.length} سؤال نمونه · دادهٔ آزمایشی`;
  const answered = rows.filter((q) => answers[q.id] !== undefined).length;
  bar.style.width = `${rows.length ? Math.round((answered / rows.length) * 100) : 0}%`;
  doc.querySelectorAll('[data-bank-filter]').forEach((b) => b.classList.toggle('on', b.dataset.bankFilter === filter));
  list.innerHTML = rows.map((q) => `
    <div class="sp-q" data-bank-q="${esc(q.id)}">
      <div class="sp-stem"><b>${esc(q.stem)}</b><small>${esc(q.topic)} · ${esc(q.id)}</small></div>
      <div class="sp-opts">${q.options.map((o) => `
        <button class="sp-opt ${String(answers[q.id]) === String(o.id) ? 'on' : ''}" data-bank-opt="${o.id}">${esc(String(o.id + 1))}</button>`).join('')}</div>
    </div>`).join('');
}

export function renderExamStatus(doc, store) {
  const line = doc.getElementById('examStatusLine');
  if (!line) return;
  const labels = { idle: 'آماده', running: 'در حال اجرا', paused: 'متوقف / ذخیرهشده', finished: 'تمامشده' };
  const status = labels[store.get('exam.status')] || 'آماده';
  const saved = store.get('exam.saved');
  const results = store.get('exam.results') || [];
  const last = results.at(-1);
  line.textContent = `وضعیت آزمون: ${status} · آزمون ذخیرهشده: ${saved ? 'بله' : 'خیر'} · کارنامههای محلی: ${results.length}`
    + (last ? ` · آخرین: ${last.percentLabel}` : '')
    + ' · همهٔ مقادیر محلی و آزمایشیاند.';
}

export function renderLeaderboard(doc, { state = 'weekly', rows = [] }) {
  const box = doc.getElementById('leaderboardRows');
  if (!box) return;
  doc.querySelectorAll('[data-lb-state]').forEach((b) => b.classList.toggle('on', b.dataset.lbState === state));
  if (state === 'empty') {
    box.innerHTML = '<div class="dash"><b>دادهای برای نمایش نیست</b><p>رتبهبندی سروری وجود ندارد؛ دادهها آزمایشی و محلیاند.</p></div>';
    return;
  }
  const shown = state === 'weekly' ? rows.slice(0, 3) : rows;
  box.innerHTML = shown.map((r, i) => `
    <div class="lb-row ${r.self ? 'me' : ''}">
      <span class="rk">${esc(r.rank ?? i + 1)}</span>
      <span class="av" style="background:${r.self ? '#3890FA' : '#8D60E2'}">${esc(String(r.name || '؟').slice(0, 1))}</span>
      <span class="nm">${esc(r.name)}</span>
      <span class="xp">${esc(r.xp)} ⚡</span>
    </div>`).join('');
}

export function renderSettings(doc, store) {
  const rows = doc.getElementById('settingsRows');
  if (!rows) return;
  const s = store.get('settings');
  const toggles = [
    ['theme', 'حالت شب', s.theme === 'night'],
    ['rtl', 'آینهٔ راستبهچپ', Boolean(s.rtl)],
    ['sound', 'صدا', Boolean(s.sound)],
    ['haptics', 'بازخورد لمسی', Boolean(s.haptics)],
    ['reduceMotion', 'کاهش انیمیشن', Boolean(s.reduceMotion)],
  ];
  rows.innerHTML = toggles.map(([key, label, on]) => `
    <div class="selfrow"><span>${esc(label)}</span><b><button class="btn ${on ? 'primary' : ''}" data-setting="${key}">${on ? 'روشن' : 'خاموش'}</button></b></div>`).join('')
    + `<div class="selfrow"><span>هدف روزانه</span><b><button class="btn" data-goal="1">${esc(store.get('settings.dailyGoal'))} دقیقه</button></b></div>`
    + `<div class="selfrow"><span>شناسهٔ محلی</span><b>${esc(store.get('identity.id'))}</b></div>`;
}

/** Render the LearnHarness-compatible local harness status (no fake AI). */
export function renderHarnessStatus(doc, status) {
  const box = doc.getElementById('harnessStatus');
  if (!box) return;
  doc.querySelectorAll('[data-harness-phase]').forEach((b) =>
    b.classList.toggle('on', b.dataset.harnessPhase === status.phase));
  const honest = status.honest === 'no-source-registered'
    ? 'منبعی در فرم اطلاعاتی ثبت نشده؛ منابع در مرحلهٔ بعد اضافه میشوند.'
    : `از ${status.availableLessons} درس و ${status.availableQuestions} تست موجود استفاده میشود.`;
  box.textContent = `LearnHarness (موتور محلی) · فاز: ${status.phaseFa} · `
    + `گزارهها: ${status.propositions} · ارائهدهندهٔ خارجی: ${status.externalProvider} · `
    + `تولید متن: خیر · ${honest}`;
}
