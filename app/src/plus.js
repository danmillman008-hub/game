/**
 * One-click output layer — mounts the 「مسیر آموزشی」「ساختار توکنها」
 * 「هوش مصنوعی」「خروجی」 screens and wires them to the local engines.
 *
 * Every screen reuses approved prototype classes/CSS tokens. New CSS lives in
 * assets/extra.css and introduces no new colour, font, radius or icon shape.
 */
import { esc, faNum, saveText, stamp } from './util.js';
import { createEconomy } from './token-economy.js';
import { createLearningPath, PATH_DISCLAIMER } from './learning-path.js';
import { createAiStudio } from './ai-studio.js';
import { createOutputKit } from './output-kit.js';
import { DESIGN_TOKENS } from './design-tokens.js';
import { STARTER_PACKAGE, STARTER_SUMMARY } from './starter-package.js';

const SCREENS = { 'learning-path': 'Learn', 'lesson-studio': 'Learn',
  tokens: 'Profile', 'ai-studio': 'AI', output: 'Profile' };

export function mountPlus(doc, { store, proto, toast, harnessRef, mountPackage }) {
  const tabs = doc.getElementById('tabs');
  const phone = doc.getElementById('phone');
  if (!tabs || !phone) return { mounted: false };
  const economy = createEconomy(store);
  const learningPath = createLearningPath(store, economy, proto, STARTER_PACKAGE.questions);
  const aiStudio = createAiStudio({ doc, store, economy, harnessRef, mountPackage, toast,
    starterPackage: STARTER_PACKAGE });
  const outputKit = createOutputKit({ doc, store, economy, learningPath, aiStudio, toast });

  Object.entries(SCREENS).forEach(([s, t]) => { if (proto) proto.tabMap[s] = t; });

  const insert = (html) => {
    const tpl = doc.createElement('template'); tpl.innerHTML = html.trim();
    const node = tpl.content.firstElementChild; phone.insertBefore(node, tabs); return node;
  };
  const entry = (label, target, primary) =>
    `<button type="button" class="plus-entry ${primary ? 'primary' : ''}" data-plus-nav="${target}">${esc(label)}</button>`;

  // ---- learning path screen -------------------------------------------------
  insert(`<section class="screen mimo plus-screen" data-screen="learning-path">
    <div class="sp-top"><button type="button" class="x" data-nav="learn"><span data-icon="ic_arrow_back_24" data-size="24" data-mono="1"></span></button><b>مسیر آموزشی کامل</b></div>
    <div class="sd-hero plus-hero"><span class="kick">مسیر برنامه محور</span>
      <h2 id="lpTitle">یادگیری گامبهگام</h2><p>${esc(PATH_DISCLAIMER)}</p>
      <span class="sp-scope" id="lpScope">—</span>
      <div class="cbar"><i id="lpBar" style="width:0%"></i></div></div>
    <div class="chips" id="lpPrograms"></div>
    <div class="chips" id="lpCourses"></div>
    <div id="lpChapters"></div>
    <button type="button" class="plus-entry primary" data-plus="lp:continue">ادامهٔ مسیر ←</button>
    <div class="plus-note" id="lpFoot"></div>
  </section>`);

  // ---- interactive lesson studio -------------------------------------------
  insert(`<section class="screen mimo plus-screen" data-screen="lesson-studio">
    <div class="sp-top"><button type="button" class="x" data-plus-nav="learning-path"><span data-icon="ic_arrow_back_24" data-size="24" data-mono="1"></span></button><b>درس تعاملی</b></div>
    <div class="sd-hero plus-hero"><span class="kick">گام فعلی</span><h2 id="lsTitle">—</h2>
      <p id="lsNote"></p><div class="cbar"><i id="lsBar" style="width:0%"></i></div></div>
    <div id="lsBody"></div>
  </section>`);

  // ---- token structure screen ----------------------------------------------
  insert(`<section class="screen mimo plus-screen" data-screen="tokens">
    <div class="sp-top"><button type="button" class="x" data-nav="profile"><span data-icon="ic_arrow_back_24" data-size="24" data-mono="1"></span></button><b>ساختار توکنها</b></div>
    <div class="sd-hero plus-hero"><span class="kick">سه معنای «توکن»، بهصورت کامل</span>
      <h2>طراحی · پاداش · هوش مصنوعی</h2>
      <p>همهٔ مقادیر زنده، قابل خروجیگیری و ذخیرهشده روی همین دستگاهاند. هیچکس آنها را به سرور نمیفرستد.</p></div>
    <div class="chips" id="tkTabs">
      <button type="button" class="chip on" data-plus="tk:design">توکنهای طراحی</button>
      <button type="button" class="chip" data-plus="tk:economy">توکنهای پاداش</button>
      <button type="button" class="chip" data-plus="tk:ai">توکنهای AI</button>
    </div>
    <div id="tkBody"></div>
  </section>`);

  // ---- AI studio + output screens ------------------------------------------
  aiStudio.mount(tabs);
  insert(`<section class="screen mimo plus-screen" data-screen="output">
    <div class="sp-top"><button type="button" class="x" data-nav="profile"><span data-icon="ic_arrow_back_24" data-size="24" data-mono="1"></span></button><b>خروجی گرفتن</b></div>
    <div class="sd-hero plus-hero"><span class="kick">یک کلیک، بی دردسر</span>
      <h2>همین فایل را ببر</h2>
      <p>فایل تکهای HTML، بستهٔ ZIP شامل PWA، وضعیت محلی، مسیر آموزشی و گزارش چاپی. بدون اینترنت و بدون آپلود.</p>
      <span class="sp-scope" id="outStatus">—</span></div>
    <div id="outBody"></div>
    <div class="banner warn plus-note">استنتاج از سرور میمو تأیید نشده است (SERVER CONFIRMED=0). قواعد پاداش و محتوای درسها محلی/آزمایشیاند.</div>
  </section>`);

  // ---- entry points on the APPROVED screens (additive nodes only) -----------
  const overview = doc.getElementById('overviewEntry');
  if (overview) overview.insertAdjacentHTML('afterend', entry('مسیر آموزشی کامل · ۱۸۰ درس', 'learning-path', true));
  const aiScreen = doc.querySelector('[data-screen="ai"]');
  if (aiScreen) aiScreen.insertAdjacentHTML('beforeend', entry('استودیو یادگیری محلی (۴ فاز کامل)', 'ai-studio', true));
  const profile = doc.querySelector('[data-screen="profile"]');
  if (profile) profile.insertAdjacentHTML('beforeend',
    entry('ساختار توکنها', 'tokens', false) + entry('خروجی گرفتن / نصب اپ', 'output', true));
  const lessonBody = doc.querySelector('[data-screen="lesson"] .lesson-body');
  if (lessonBody) lessonBody.insertAdjacentHTML('beforeend',
    `<div class="plus-card" id="plusLessonPanel"><b>مسیر آموزشی تعاملی</b>
      <p class="plus-note">گام فعلی مسیر را با پرسش، پاسخ و توضیح واقعی موجود در پروتوتایپ تمرین کنید.</p>
      ${entry('باز کردن درس تعاملی', 'lesson-studio', true)}</div>`);

  if (proto && proto.paintIcons) proto.paintIcons(phone);

  // ---- rendering ------------------------------------------------------------
  let tokenTab = 'design';
  let lessonSelected = null, lessonAnswer = null, lessonChecked = false;

  function renderPath() {
    const c = learningPath.course(), p = learningPath.progress();
    const title = doc.getElementById('lpTitle'); if (title) title.textContent = c ? c.name : '—';
    const scope = doc.getElementById('lpScope');
    if (scope) scope.textContent = `پیشرفت: ${p.doneFa} از ${p.totalFa} درس (${p.percentFa}٪)`;
    const bar = doc.getElementById('lpBar'); if (bar) bar.style.width = `${p.percent}%`;
    doc.getElementById('lpPrograms').innerHTML = learningPath.curriculum.programs.map((g) =>
      `<button type="button" class="chip ${learningPath.state().programKey === g.key ? 'on' : ''}" data-plus="lp:program" data-key="${esc(g.key)}">${esc(g.label)}</button>`).join('');
    doc.getElementById('lpCourses').innerHTML = learningPath.curriculum.courses.map((x) =>
      `<button type="button" class="chip ${c && c.key === x.key ? 'on' : ''}" data-plus="lp:course" data-key="${esc(x.key)}">${esc(x.name)}</button>`).join('');
    doc.getElementById('lpChapters').innerHTML = c ? c.chapters.map((ch) => `
      <div class="plus-card"><b>${faNum(ch.ordinal)}. ${esc(ch.name)}</b>
        ${ch.lessons.map((ls) => {
          const st = learningPath.statusOf(ls.id);
          return `<button type="button" class="plus-row ${st === 'done' ? 'done' : ''}" data-plus="lp:lesson" data-id="${esc(ls.id)}" ${st === 'locked' ? 'disabled' : ''}>
            <span class="plus-state ${esc(st)}">${st === 'done' ? '✓' : st === 'current' ? '▶' : st === 'open' ? '○' : '🔒'}</span>
            <span>${esc(ls.title)}</span></button>`;
        }).join('')}
      </div>`).join('') : '';
    const foot = doc.getElementById('lpFoot');
    if (foot) foot.textContent = `${faNum(learningPath.curriculum.courses.length)} کتاب · ${faNum(learningPath.curriculum.totalChapters)} فصل · ${faNum(learningPath.curriculum.totalLessons)} درس (سرفصلهای پروتوتایپ تأییدشده)`;
  }

  function renderLesson() {
    const id = lessonSelected || learningPath.nextId();
    const ls = id ? learningPath.byId(id) : null;
    const c = learningPath.course(), p = learningPath.progress();
    doc.getElementById('lsTitle').textContent = ls ? ls.title : 'مسیر کامل شد';
    doc.getElementById('lsNote').textContent = ls
      ? `درس «${c ? c.name : ''}» · ${PATH_DISCLAIMER}` : 'همهٔ گامها تکمیل شد.';
    const bar = doc.getElementById('lsBar'); if (bar) bar.style.width = `${p.percent}%`;
    const q = ls ? learningPath.questionFor(id) : null;
    const body = doc.getElementById('lsBody');
    if (!ls || !q) { body.innerHTML = '<div class="banner plus-ok">مسیر تکمیل شد. کتاب دیگری انتخاب کنید.</div>'; return; }
    body.innerHTML = `<div class="plus-card"><b>گام ${faNum(ls.index)} · تمرین از بانک موجود</b>
      <p class="plus-note">منبع: ${esc(q.ref)} · پاسخ و توضیح از همان پروتوتایپ خوانده میشود.</p>
      <div class="plus-q"><p>${esc(q.stem)}</p>
        ${q.options.map((o, i) => {
          let cls = 'plus-opt';
          if (lessonAnswer === i) cls += ' sel';
          if (lessonChecked && i === q.correctIndex) cls += ' ok';
          if (lessonChecked && lessonAnswer === i && i !== q.correctIndex) cls += ' bad';
          return `<button type="button" class="${cls}" data-plus="ls:opt" data-oi="${i}" ${lessonChecked ? 'disabled' : ''}>${esc(o)}</button>`;
        }).join('')}
      </div>
      ${!lessonChecked ? `<button type="button" class="plus-entry primary" data-plus="ls:check">بررسی پاسخ</button>`
        : `<div class="banner ${lessonAnswer === q.correctIndex ? 'plus-ok' : 'plus-bad'}">
             ${lessonAnswer === q.correctIndex ? 'درست' : 'نادرست'} · ${esc(q.explanation)}</div>
           <div class="chips">
             <button type="button" class="chip" data-plus="ls:retry">تکرار</button>
             <button type="button" class="chip" data-plus="ls:complete">تکمیل و گام بعدی ←</button>
           </div>`}
    </div>`;
  }

  function liveCss(name, fallback) {
    try { const v = getComputedStyle(doc.documentElement).getPropertyValue(name).trim(); return v || fallback; }
    catch (_) { return fallback; }
  }

  function renderTokens() {
    const tabsEl = doc.getElementById('tkTabs');
    [...tabsEl.children].forEach((b) => b.classList.toggle('on', b.dataset.plus === `tk:${tokenTab}`));
    const body = doc.getElementById('tkBody');
    if (tokenTab === 'design') {
      body.innerHTML = `<div class="plus-card"><b>۱ · توکنهای طراحی (CSS custom properties)</b>
        <p class="plus-note">${faNum(DESIGN_TOKENS.count)} توکن زنده، عیناً از <code>proto.css</code> تأییدشده. کاتالوگ APK: ${faNum(DESIGN_TOKENS.catalogCounts.colors)} رنگ · ${faNum(DESIGN_TOKENS.catalogCounts.dimens)} dimens · ${faNum(DESIGN_TOKENS.catalogCounts.strings)} رشته · ${faNum(DESIGN_TOKENS.catalogCounts.styles)} استایل.</p>
        ${DESIGN_TOKENS.groups.map((g) => `<div class="plus-card"><b>${esc(g.title)}</b>
          ${g.names.map((n) => {
            const t = DESIGN_TOKENS.tokens.find((x) => x.name === n) || {};
            return `<div class="plus-row"><span class="plus-swatch" style="background:${esc(liveCss(n, t.day))}"></span>
              <code>${esc(n)}</code><span class="plus-note">${esc(liveCss(n, t.day))}</span>
              <span class="plus-note">شب: ${esc(t.night || '—')}</span></div>`;
          }).join('')}</div>`).join('')}
        <div class="chips"><button type="button" class="chip" data-plus="tk:night">تغییر حالت روز/شب</button>
        <button type="button" class="chip" data-plus="tk:css">خروجی CSS</button>
        <button type="button" class="chip" data-plus="tk:json">خروجی JSON</button></div>
      </div>`;
    } else if (tokenTab === 'economy') {
      const s = economy.snapshot();
      body.innerHTML = `<div class="plus-card"><b>۲ · توکنهای پاداش (اقتصاد محلی)</b>
        <p class="plus-note">قواعد زیر برداشت محلی از ۱۲ رویداد <code>GAMIFICATION_MAP.csv</code> است؛ فرمول سرور تأیید نشده. سقف XP روزانه: ${faNum(s.dailyXp)} / ${faNum(economy.cap)}.</p>
        <div class="plus-grid">${economy.structure().map((k) => `<span>${esc(k.fa)}</span><b>${esc(k.valueFa)}</b>`).join('')}</div>
        <div class="chips"><button type="button" class="chip" data-plus="tk:earn-lesson">تکمیل درس (پاداش)</button>
        <button type="button" class="chip" data-plus="tk:earn-goal">هدف روزانه</button>
        <button type="button" class="chip" data-plus="tk:spend-key">خرج ۱ کلید (راهنمایی)</button>
        <button type="button" class="chip" data-plus="tk:csv">خروجی دفتر CSV</button></div>
        <b>قواعد</b>${economy.rules.map((r) => `<div class="plus-row"><span>${esc(r.fa)}</span><span class="plus-note">${esc(r.formula)}</span></div>`).join('')}
        <b>دفتر توکنها (آخرین رویدادها)</b>
        ${s.ledger.length ? s.ledger.slice(-10).reverse().map((e) => `<div class="plus-row"><span>${esc(e.reason)}</span>
          <span class="plus-note">${esc(e.at)} · XP ${faNum(e.xp)} · سکه ${faNum(e.coins)} · کلید ${faNum(e.keys)}</span></div>`).join('')
          : '<p class="plus-note">هنوز رویدادی ثبت نشده است.</p>'}
      </div>`;
    } else {
      body.innerHTML = `<div class="plus-card"><b>۳ · توکنها / زمینهٔ هوش مصنوعی</b>
        <p class="plus-note">در این نسخه مدل زبانی، کلید API، توکن ورودی/خروجی و هزینهای وجود ندارد. ساختار زیر صادقانه و قابلاستفاده است.</p>
        ${aiStudio.tokenStructure().map((t) => `<div class="plus-row"><span><b>${esc(t.fa)}</b> · ${esc(t.value)}</span>
          <span class="plus-note">${esc(t.detail)}</span></div>`).join('')}
        <div class="chips"><button type="button" class="chip" data-plus-nav="ai-studio">باز کردن استودیو</button></div>
      </div>`;
    }
  }

  function renderOutput() {
    const st = doc.getElementById('outStatus');
    if (st) st.textContent = outputKit.hasSource()
      ? 'منبع تکفایل درون همین صفحه جاسازی شده؛ خروجی دوباره قابلexport است.'
      : 'نسخهٔ چندفایله؛ فایل dist/Mimo.html را از پوشهٔ خروجی بگیرید.';
    doc.getElementById('outBody').innerHTML = `
      <div class="plus-card"><b>۱ · گرفتن خود اپلیکیشن</b>
        <p class="plus-note">Mimo.html فقط یک فایل است؛ دوبار کلیک کنید، تمام شد. Mimo.zip شامل همان فایل + پوشهٔ نصبشدنی PWA است.</p>
        <button type="button" class="plus-entry primary" data-plus="out:html">دانلود Mimo.html (تکفایل)</button>
        <button type="button" class="plus-entry" data-plus="out:zip">دانلود Mimo.zip (کامل + PWA)</button>
        <a class="plus-entry" href="./Mimo.html" download>لینک مستقیم فایل تکهای</a>
      </div>
      <div class="plus-card"><b>۲ · نصب روی گوشی</b>
        <p class="plus-note">پیشنمایش HTTPS را در مرورگر گوشی باز کنید و دکمهٔ زیر یا منوی «افزودن به صفحهٔ اصلی» را بزنید. آیکونها و Service Worker همراه بستهاند.</p>
        <button type="button" class="plus-entry primary" data-plus="out:install">نصب اپلیکیشن</button>
        <button type="button" class="plus-entry" data-plus="out:link">کپی نشانی پیشنمایش</button>
      </div>
      <div class="plus-card"><b>۳ · خروجی دادهها و گزارش</b>
        <button type="button" class="plus-entry" data-plus="out:state">وضعیت محلی (JSON)</button>
        <button type="button" class="plus-entry" data-plus="out:csv">مسیر آموزشی (CSV)</button>
        <button type="button" class="plus-entry" data-plus="out:session">جلسهٔ AI (JSON)</button>
        <button type="button" class="plus-entry" data-plus="out:print">گزارش قابلچاپ / PDF</button>
      </div>`;
  }

  function renderAll(name) {
    if (name === 'learning-path') renderPath();
    if (name === 'lesson-studio' || name === 'lesson') renderLesson();
    if (name === 'tokens') renderTokens();
    if (name === 'ai-studio' || name === 'ai') aiStudio.render();
    if (name === 'output') renderOutput();
  }

  // ---- one delegated listener (capture) for all plus actions ----------------
  doc.addEventListener('click', (e) => {
    const nav = e.target.closest('[data-plus-nav]');
    if (nav) { e.preventDefault(); e.stopPropagation(); if (proto) proto.go(nav.dataset.plusNav); return; }
    const el = e.target.closest('[data-plus]');
    if (!el) return;
    const act = el.dataset.plus; e.preventDefault(); e.stopPropagation();
    if (act.startsWith('tk:')) {
      const tab = act.slice(3);
      if (['design', 'economy', 'ai'].includes(tab)) { tokenTab = tab; renderTokens(); return; }
      if (tab === 'night') {
        const cur = store.get('settings.theme');
        store.set('settings.theme', cur === 'night' ? 'day' : 'night');
        doc.body.classList.toggle('night', cur !== 'night'); renderTokens();
        toast(`حالت ${cur === 'night' ? 'روز' : 'شب'} فعال شد`); return;
      }
      if (tab === 'css') {
        const css = [':root{', ...DESIGN_TOKENS.tokens.map((t) => `  ${t.name}:${t.day};`), '}',
          'body.night{', ...DESIGN_TOKENS.tokens.map((t) => `  ${t.name}:${t.night};`), '}'].join('\n');
        const ok = saveText('mimo-design-tokens.css', css, 'text/css;charset=utf-8');
        toast(ok ? 'توکنهای طراحی دانلود شد' : 'دانلود ممکن نشد'); return;
      }
      if (tab === 'json') {
        const ok = saveText('mimo-design-tokens.json', JSON.stringify(DESIGN_TOKENS, null, 2), 'application/json');
        toast(ok ? 'کاتالوگ توکنها دانلود شد' : 'دانلود ممکن نشد'); return;
      }
      if (tab === 'earn-lesson') { economy.apply('lesson-complete', { reason: 'دکمهٔ ساختار توکنها' }); renderTokens(); toast('پاداش تکمیل درس ثبت شد'); return; }
      if (tab === 'earn-goal') { economy.apply('daily-goal'); renderTokens(); toast('هدف روزانه ثبت شد؛ Streak +۱'); return; }
      if (tab === 'spend-key') { const ok = economy.spend('keys', 1); renderTokens(); toast(ok ? 'یک کلید خرج شد' : 'کلید کافی نیست'); return; }
      if (tab === 'csv') {
        const s = economy.snapshot();
        const rows = [['زمان', 'رویداد', 'شرح', 'XP', 'سکه', 'کلید', 'پیوستگی', 'سقفخورده'],
          ...s.ledger.map((x) => [x.at, x.ruleId, x.reason, x.xp, x.coins, x.keys, x.streak, x.capped])];
        const csv = '\uFEFF' + rows.map((r) => r.map((v) => `"${String(v).replace(/"/g, '""')}"`).join(',')).join('\r\n');
        const ok = saveText('دفتر-توکنها.csv', csv, 'text/csv;charset=utf-8');
        toast(ok ? 'دفتر توکنها دانلود شد' : 'دانلود ممکن نشد'); return;
      }
    }
    if (act.startsWith('lp:')) {
      if (act === 'lp:program') { learningPath.setProgram(el.dataset.key); renderPath(); return; }
      if (act === 'lp:course') { learningPath.setCourse(el.dataset.key); lessonSelected = null; renderPath(); return; }
      if (act === 'lp:lesson') {
        const r = learningPath.open(el.dataset.id);
        if (!r.ok) { toast('این گام قفل است؛ گام قبل را کامل کنید'); return; }
        lessonSelected = el.dataset.id; lessonAnswer = null; lessonChecked = false;
        renderLesson(); if (proto) proto.go('lesson-studio'); return;
      }
      if (act === 'lp:continue') {
        const id = learningPath.nextId();
        if (!id) { toast('مسیر کامل شد'); return; }
        const r = learningPath.open(id);
        if (!r.ok) { toast('گام بعدی قفل است'); return; }
        lessonSelected = id; lessonAnswer = null; lessonChecked = false;
        renderLesson(); if (proto) proto.go('lesson-studio'); return;
      }
    }
    if (act === 'ls:opt') { lessonAnswer = Number(el.dataset.oi); renderLesson(); return; }
    if (act === 'ls:check') {
      if (lessonAnswer === null) { toast('یک گزینه انتخاب کنید'); return; }
      lessonChecked = true; renderLesson(); return;
    }
    if (act === 'ls:retry') { lessonAnswer = null; lessonChecked = false; renderLesson(); return; }
    if (act === 'ls:complete') {
      const id = lessonSelected || learningPath.nextId();
      const q = id ? learningPath.questionFor(id) : null;
      const r = learningPath.complete(id, q ? lessonAnswer === q.correctIndex : false);
      const next = learningPath.nextId();
      lessonSelected = next; lessonAnswer = null; lessonChecked = false;
      renderPath(); renderLesson();
      toast(`گام ثبت شد: ${faNum(r.completed || 0)} از ${faNum(r.total || 0)} · پاداش توکنها اعمال شد`);
      return;
    }
    if (act.startsWith('out:')) {
      const map = { 'out:html': () => outputKit.downloadHtml(), 'out:zip': () => outputKit.downloadZip(),
        'out:state': () => outputKit.downloadState(), 'out:csv': () => outputKit.downloadCsv(),
        'out:session': () => outputKit.downloadSession(), 'out:print': () => outputKit.printReport(),
        'out:install': () => outputKit.install(), 'out:link': () => outputKit.copyLink() };
      if (map[act]) map[act]();
    }
  }, true);

  renderPath(); renderLesson(); renderTokens(); renderOutput(); aiStudio.render();
  return { mounted: true, onNavigate: renderAll, renderAll, economy, learningPath, aiStudio, outputKit,
    starter: STARTER_SUMMARY, designTokens: DESIGN_TOKENS };
}
