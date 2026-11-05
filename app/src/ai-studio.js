/**
 * «بخش هوش مصنوعی» — complete LOCAL LearnHarness studio.
 *
 * FOUR working phases (measure / plan / teach / practice), a knowledge graph,
 * token accounting, a local content-package importer and session export.
 * HONESTY CONTRACT: there is no LLM, no endpoint, no network call and NO
 * generated text. All displayed text is read verbatim from the content package
 * (the approved v12.5-fa prototype fixtures by default).
 */
import { esc, faNum, saveText, stamp } from './util.js';

const PHASES = [
  { key: 'measure', fa: 'سنجش' }, { key: 'plan', fa: 'برنامه' },
  { key: 'teach', fa: 'آموزش' }, { key: 'practice', fa: 'تمرین' },
];
const DEFAULTS = {
  phase: 'measure', goal: '', reasoning: '', confidence: 60,
  measureStarted: false, measureAnswers: {}, measureChecked: false, measureScore: null,
  teachStep: 0, practiceIndex: 0, practiceSelected: null, practiceChecked: false,
  contextUnits: 0, completedPhases: [], sessions: [], imported: null, tokenTab: 'model',
};

export function createAiStudio({ doc, store, economy, harnessRef, mountPackage, toast, starterPackage }) {
  let pkg = starterPackage;
  let screen = null;
  let l = { ...DEFAULTS, ...(store.get('ai.studio') || {}) };
  const save = (patch) => { l = { ...l, ...patch }; store.set('ai.studio', l); return l; };
  const questions = () => (pkg?.questions || []).filter((q) => q.correctIndex !== null && q.correctIndex >= 0);

  function tutorialsLesson(id) {
    for (const t of pkg?.tutorials || []) for (const c of t.chapters || []) for (const ls of c.lessons || []) {
      if (String(ls.id) === String(id)) return { lesson: ls, tutorial: t };
    }
    return null;
  }
  function bump(n = 1) { save({ contextUnits: l.contextUnits + n }); }
  function markPhase(p) {
    const done = l.completedPhases.includes(p) ? l.completedPhases : [...l.completedPhases, p];
    save({ completedPhases: done, phase: p });
    const h = harnessRef();
    if (h) h.setPhase(p);
  }

  function mount(tabs) {
    screen = doc.createElement('section');
    screen.className = 'screen mimo plus-screen';
    screen.dataset.screen = 'ai-studio';
    screen.innerHTML = `
      <div class="sp-top"><button type="button" class="x" data-nav="ai"><span data-icon="ic_arrow_back_24" data-size="24" data-mono="1"></span></button><b>استودیو یادگیری محلی</b></div>
      <div class="sd-hero plus-hero">
        <span class="kick">LearnHarness · موتور محلی</span>
        <h2>چهار فاز، بدون مدل زبانی</h2>
        <p>سنجش ← برنامه ← آموزش ← تمرین. هیچ متنی تولید نمیشود؛ هر چه میبینید عیناً از بستهٔ محتوای موجود خوانده شده است.</p>
        <span class="sp-scope" id="aiStudioSource">منبع: بستهٔ آغازین پروتوتایپ</span>
      </div>
      <div class="banner warn plus-note" id="aiStudioHonest">بدون LLM · بدون اینترنت · بدون کلید API · تولید متن: خیر · ارائهدهندهٔ خارجی: not-configured</div>
      <div class="chips" id="aiStudioTokenChips"></div>
      <div class="plus-card" id="aiStudioTokenDetail"></div>
      <div class="chips" id="aiStudioPhases"></div>
      <div id="aiStudioBody"></div>
      <div class="plus-card" id="aiStudioGraph"></div>
      <div class="plus-card">
        <b>وارد کردن بستهٔ محتوا (محلی، بدون آپلود)</b>
        <p class="plus-note">فایل JSON سازگار با «فرم اطلاعاتی» را انتخاب کنید. بستههای بازبینینشده برچسب میخورند و جایگزین درسنامهٔ نهایی نیستند.</p>
        <input type="file" id="aiPackageFile" accept=".json,application/json" class="plus-file">
        <button type="button" class="plus-entry" data-ai="import">بارگذاری بسته از فایل</button>
        <input type="file" id="aiNotesFile" accept=".txt,.md,text/plain" class="plus-file">
        <button type="button" class="plus-entry" data-ai="notes">پیوستکردن یادداشت (فقط متن)</button>
        <div id="aiStudioImportNote" class="plus-note"></div>
      </div>
      <div class="chips" style="padding-bottom:20px">
        <button type="button" class="chip" data-ai="export-session">خروجی جلسه (JSON)</button>
        <button type="button" class="chip" data-ai="reset">شروع دوباره</button>
      </div>`;
    const parent = tabs ? tabs.parentNode : doc.getElementById('phone');
    parent.insertBefore(screen, tabs || null);
    screen.addEventListener('click', onClick);
    screen.addEventListener('change', onChange);
    return screen;
  }

  function tokenStructure() {
    return [
      { key: 'model', fa: 'Model', value: 'local-content (بدون LLM)', detail: 'ارائهدهندهٔ محلی فقط درس/سؤال موجود را انتخاب میکند. قرارداد ارائهدهندهٔ خارجی: not-configured؛ نیازمند endpoint، پروکسی سروری و کلید کاربر است که در این نسخه وجود ندارد.' },
      { key: 'context', fa: 'Context', value: `${faNum(l.contextUnits)} واحد منبع محلی`, detail: `واحدهای زمینه = گزارههای ثبتشده + پاسخهای سنجش + جلسههای تمرین. بودجهٔ توکن خارجی: ۰ (هیچ درخواستی به مدل زبانی ارسال نشد). منابع موجود: ${faNum(questions().length)} سؤال.` },
      { key: 'cost', fa: 'Cost', value: '۰٫۰۰ دلار', detail: 'هزینهٔ واقعی صفر است چون هیچ فراخوانی شبکهای، توکن ورودی/خروجی یا سرویس ابری وجود ندارد. نمایش «۰٫۰۱ دلار» در پروتوتایپ صرفاً یک برچسب رابط بود.' },
      { key: 'steps', fa: 'Steps', value: `${faNum(l.completedPhases.length)}/۴ فاز`, detail: 'فازها: سنجش، برنامهریزی، آموزش، تمرین. وابستگی گامها از نقشهٔ پیشنیاز ساخته میشود؛ حلقهٔ practice بر اساس پاسخ و اطمینان ادامه مییابد.' },
      { key: 'settings', fa: 'Settings', value: 'تولید متن: خیر · شبکه: خیر', detail: 'تنظیمات ثابت نسخهٔ آفلاین: بدون fetch/XHR/WebSocket، بدون کلید، بدون ذخیرهٔ گفتگو در سرور. همهٔ وضعیتها در حافظهٔ محلی مرورگر نگهداری میشوند.' },
    ];
  }

  function render() {
    if (!screen) return;
    const src = doc.getElementById('aiStudioSource');
    if (src) src.textContent = l.imported
      ? `منبع: ${l.imported.name} (${faNum(l.imported.questions)} سؤال · ${l.imported.status})`
      : `منبع: بستهٔ آغازین پروتوتایپ (${faNum(questions().length)} سؤال)`;
    doc.getElementById('aiStudioTokenChips').innerHTML = tokenStructure().map((t) =>
      `<button type="button" class="chip ${l.tokenTab === t.key ? 'on' : ''}" data-ai="token:${t.key}">${esc(t.fa)}</button>`).join('');
    const tok = tokenStructure().find((t) => t.key === l.tokenTab) || tokenStructure()[0];
    doc.getElementById('aiStudioTokenDetail').innerHTML =
      `<b>${esc(tok.fa)} · ${esc(tok.value)}</b><p class="plus-note">${esc(tok.detail)}</p>`;
    doc.getElementById('aiStudioPhases').innerHTML = PHASES.map((p) =>
      `<button type="button" class="chip ${l.phase === p.key ? 'on' : ''}" data-ai="phase:${p.key}">${esc(p.fa)}${l.completedPhases.includes(p.key) ? ' ✓' : ''}</button>`).join('');
    const body = doc.getElementById('aiStudioBody');
    body.innerHTML = l.phase === 'measure' ? renderMeasure()
      : l.phase === 'plan' ? renderPlan()
        : l.phase === 'teach' ? renderTeach() : renderPractice();
    renderGraph();
  }

  function renderMeasure() {
    const qs = questions().slice(0, 5);
    const started = l.measureStarted;
    return `<div class="plus-card">
      <b>فاز ۱ · سنجش نقطهٔ شروع</b>
      <p class="plus-note">هدف یادگیری و استدلال خود را بنویسید؛ سپس ${faNum(qs.length)} سؤال موجود در بسته پاسخ دهید. نمره فقط محلی است.</p>
      <input class="plus-input" id="aiGoal" placeholder="مثلاً: ژنتیک مولکولی" value="${esc(l.goal)}">
      <label class="plus-note">میزان اطمینان: <span id="aiConfFa">${faNum(l.confidence)}</span>٪</label>
      <input type="range" min="0" max="100" value="${l.confidence}" id="aiConfidence" class="plus-range">
      <textarea class="plus-input" id="aiReasoning" rows="3" placeholder="استدلال / thinking aloud (متن شما، بدون پاسخ ساختگی)">${esc(l.reasoning)}</textarea>
      <button type="button" class="plus-entry primary" data-ai="start">شروع سنجش و ساخت برنامه</button>
    </div>` + (!started ? '' : `<div class="plus-card"><b>پرسشهای سنجش (از بستهٔ موجود)</b>
      ${qs.map((q, i) => `<div class="plus-q"><p>${faNum(i + 1)}. ${esc(q.stemFa)}</p>
        ${(q.options || []).map((o, oi) => `<button type="button" class="plus-opt ${l.measureAnswers[i] === oi ? 'sel' : ''}" data-ai="mopt" data-qi="${i}" data-oi="${oi}">${esc(o)}</button>`).join('')}
        ${l.measureChecked ? `<p class="plus-note">پاسخ صحیح: ${esc(q.options[q.correctIndex])} · ${esc(q.explanationFa || '')}</p>` : ''}
      </div>`).join('')}
      ${!l.measureChecked ? '<button type="button" class="plus-entry primary" data-ai="measure-submit">ثبت ارزیابی</button>'
        : `<div class="banner plus-ok">نتیجه: ${faNum(l.measureScore || 0)} از ${faNum(qs.length)} · سطح ${esc(levelOf(l.measureScore || 0, qs.length))}. برنامهٔ ۶ گام ساخته شد.</div>
           <button type="button" class="plus-entry" data-ai="phase:plan">نمایش برنامه</button>`}
    </div>`);
  }
  const levelOf = (score, total) => !total ? 'نامشخص' : score / total >= 0.7 ? 'پیشرفته' : score / total >= 0.4 ? 'متوسط' : 'نیازمند تمرین';

  function renderPlan() {
    const h = harnessRef(); const steps = (h && h.state && h.state.plan) || [];
    return `<div class="plus-card"><b>فاز ۲ · برنامهٔ وابسته (dependency map)</b>
      <p class="plus-note">گامها از درسهای موجود در بسته ساخته میشوند؛ هیچ عنوان یا متن جدیدی تولید نشده است.</p>
      ${steps.length ? `<ol class="plus-steps">${steps.map((s, i) => `<li><b>${faNum(i + 1)}. ${esc(s.title)}</b>
        <span class="plus-note">نقش: ${esc(s.pedagogicalRole)} · پیشنیاز: ${esc(s.dependsOn === null ? 'ندارد' : String(s.dependsOn))}</span></li>`).join('')}</ol>`
        : '<p class="plus-note">برنامهای نساخته شده؛ ابتدا فاز سنجش را اجرا کنید.</p>'}
      <button type="button" class="plus-entry primary" data-ai="phase:teach">رفتن به آموزش</button>
      ${!steps.length ? '<button type="button" class="plus-entry" data-ai="start">ساخت برنامه از بستهٔ موجود</button>' : ''}
    </div>`;
  }

  function renderTeach() {
    const h = harnessRef(); const steps = (h && h.state && h.state.plan) || [];
    const step = steps[Math.min(l.teachStep, Math.max(0, steps.length - 1))];
    const found = step ? tutorialsLesson(step.lessonId) : null;
    const blocks = found?.lesson?.blocks || [];
    const props = (h && h.state && h.state.graph && h.state.graph.propositions) || [];
    return `<div class="plus-card"><b>فاز ۳ · آموزش از متن موجود</b>
      <p class="plus-note">${step ? `گام ${faNum(l.teachStep + 1)} از ${faNum(steps.length)} · ${esc(step.title)}` : 'ابتدا برنامه بسازید.'}</p>
      ${blocks.length ? `<div class="plus-q"><p>${esc(blocks[0].contentFa)}</p>
        ${(blocks[0].options || []).map((o, i) => `<button type="button" class="plus-opt" data-ai="noop">${esc(o)}</button>`).join('')}</div>
        <div class="banner plus-ok">${esc(blocks[1]?.contentFa || blocks[0].explanationFa || '')}</div>`
        : '<p class="plus-note">این گام بلوک متنی ندارد؛ عنوان درس از سرفصل پروتوتایپ نمایش داده میشود.</p>'}
      <p class="plus-note">منبع: ${esc(found?.lesson?.trace?.sourceRef || step?.lessonId || '—')} · وضعیت: ${esc(found?.lesson?.trace?.contentStatus || 'placeholder')}</p>
      <div class="chips">
        <button type="button" class="chip" data-ai="teach-record">ثبت گزاره در گراف</button>
        <button type="button" class="chip" data-ai="teach-next">گام بعدی</button>
        <button type="button" class="chip" data-ai="phase:practice">بلد هستم → تمرین</button>
      </div>
      <p class="plus-note">گزارههای ثبتشده: ${faNum(props.length)} · تولید متن: خیر</p>
    </div>`;
  }

  function renderPractice() {
    const qs = questions();
    const q = qs[l.practiceIndex % Math.max(1, qs.length)];
    if (!q) return '<div class="plus-card plus-note">بستهٔ محتوا سؤالی با پاسخ مشخص ندارد.</div>';
    const checked = l.practiceChecked, sel = l.practiceSelected;
    return `<div class="plus-card"><b>فاز ۴ · تمرین با پاسخ و توضیح واقعی</b>
      <p class="plus-note">سؤال ${faNum((l.practiceIndex % qs.length) + 1)} از ${faNum(qs.length)} · ${esc(q.trace?.sourceRef || '')}</p>
      <div class="plus-q"><p>${esc(q.stemFa)}</p>
        ${(q.options || []).map((o, i) => {
          let cls = 'plus-opt';
          if (sel === i) cls += ' sel';
          if (checked && i === q.correctIndex) cls += ' ok';
          if (checked && sel === i && i !== q.correctIndex) cls += ' bad';
          return `<button type="button" class="${cls}" data-ai="popt" data-oi="${i}">${esc(o)}</button>`;
        }).join('')}
      </div>
      ${!checked ? '<button type="button" class="plus-entry primary" data-ai="practice-check">بررسی پاسخ</button>'
        : `<div class="banner ${sel === q.correctIndex ? 'plus-ok' : 'plus-bad'}">${sel === q.correctIndex ? 'درست' : 'نادرست'} · ${esc(q.explanationFa || '')}</div>
           <div class="chips"><button type="button" class="chip" data-ai="practice-next">سؤال بعدی</button>
           <button type="button" class="chip" data-ai="practice-retry">تکرار خطاها</button>
           <button type="button" class="chip" data-ai="phase:measure">سنجش دوباره</button></div>`}
      <p class="plus-note">جلسههای ثبتشده: ${faNum(l.sessions.length)} · تلاش مجدد آزاد · زمانبندی: خیر</p>
    </div>`;
  }

  function renderGraph() {
    const box = doc.getElementById('aiStudioGraph'); if (!box) return;
    const h = harnessRef(); const st = h ? h.getStatus() : null;
    const props = (h && h.state && h.state.graph && h.state.graph.propositions) || [];
    box.innerHTML = `<b>گراف دانش و وضعیت موتور</b>
      <div class="plus-grid">
        <span>فاز</span><b>${esc(st?.phaseFa || '—')}</b>
        <span>درس / سؤال موجود</span><b>${faNum(st?.availableLessons || 0)} / ${faNum(st?.availableQuestions || 0)}</b>
        <span>گزارهها</span><b>${faNum(st?.propositions || props.length)}</b>
        <span>تولید متن</span><b>خیر</b>
        <span>ارائهدهندهٔ خارجی</span><b>${esc(st?.externalProvider || 'not-configured')}</b>
      </div>
      ${props.length ? `<ol class="plus-steps">${props.slice(-4).map((p) => `<li>${esc(String(p.text).slice(0, 90))}
        <span class="plus-note">${esc(p.sourceRef || '')} · generated=${String(p.generated)}</span></li>`).join('')}</ol>` : ''}`;
  }

  function onClick(e) {
    const el = e.target.closest('[data-ai]'); if (!el || !screen.contains(el)) return;
    const act = el.dataset.ai; e.preventDefault(); e.stopPropagation();
    if (act.startsWith('token:')) { save({ tokenTab: act.slice(6) }); render(); return; }
    if (act.startsWith('phase:')) { markPhase(act.slice(6)); if (act.slice(6) === 'practice') { const h = harnessRef(); if (h) h.practice('prototype-fixture'); } render(); return; }
    if (act === 'start') {
      const g = doc.getElementById('aiGoal'), r = doc.getElementById('aiReasoning'), c = doc.getElementById('aiConfidence');
      const goal = (g?.value || l.goal || 'یادگیری').trim();
      const reasoning = r?.value || l.reasoning || '';
      const confidence = Number(c?.value || l.confidence);
      const h = harnessRef();
      if (h) { h.start(goal, reasoning); h.plan(confidence); }
      save({ goal, reasoning, confidence, measureStarted: true, measureChecked: false,
        measureAnswers: {}, measureScore: null, teachStep: 0 });
      if (reasoning.trim().length >= 12) economy.apply('lh-reasoning', { reason: 'thinking-aloud' });
      bump(1); markPhase('measure'); toast('سنجش آغاز شد؛ برنامهٔ ۶ گام از منابع موجود ساخته شد'); render(); return;
    }
    if (act === 'mopt') {
      const answers = { ...l.measureAnswers, [Number(el.dataset.qi)]: Number(el.dataset.oi) };
      save({ measureAnswers: answers }); render(); return;
    }
    if (act === 'measure-submit') {
      const qs = questions().slice(0, 5);
      let score = 0;
      for (let i = 0; i < qs.length; i += 1) {
        const pick = l.measureAnswers[i], ok = qs[i].correctIndex;
        const right = pick === ok;
        if (right) score += 1;
        economy.apply(right ? 'answer-correct' : 'answer-wrong',
          { difficulty: 2, firstTry: true, reason: `measure-${i}` });
      }
      bump(Object.keys(l.measureAnswers).length + 1);
      save({ measureChecked: true, measureScore: score });
      markPhase('plan'); toast(`ارزیابی ثبت شد: ${faNum(score)} از ${faNum(qs.length)}`); render(); return;
    }
    if (act === 'teach-record') {
      const h = harnessRef(); const r = h && h.teach(l.teachStep);
      if (r && r.ok) { bump(1); toast('گزاره از متن موجود در گراف ثبت شد (تولید متن: خیر)'); }
      else toast('ابتدا برنامه بسازید');
      render(); return;
    }
    if (act === 'teach-next') {
      const steps = (harnessRef()?.state?.plan || []).length;
      save({ teachStep: Math.min(steps - 1, l.teachStep + 1) }); render(); return;
    }
    if (act === 'popt') { save({ practiceSelected: Number(el.dataset.oi), practiceChecked: l.practiceChecked }); render(); return; }
    if (act === 'practice-check') {
      if (l.practiceSelected === null) { toast('یک گزینه انتخاب کنید'); return; }
      const qs = questions(), q = qs[l.practiceIndex % Math.max(1, qs.length)];
      const right = l.practiceSelected === q.correctIndex;
      const session = { id: `ps-${Date.now()}`, qid: q.id, selected: l.practiceSelected,
        correct: right, at: stamp(), sourceRef: q.trace?.sourceRef || null };
      save({ practiceChecked: true, sessions: [...l.sessions, session].slice(-100) });
      economy.apply(right ? 'answer-correct' : 'answer-wrong',
        { difficulty: 2, firstTry: true, reason: q.id });
      if (l.reasoning.trim().length >= 12) economy.apply('lh-reasoning', { reason: 'thinking-aloud' });
      const h = harnessRef(); if (h) h.practice('prototype-fixture');
      bump(2); toast(right ? 'پاسخ درست؛ توضیح از بسته نمایش داده شد' : 'پاسخ نادرست؛ توضیح موجود نمایش داده شد');
      render(); return;
    }
    if (act === 'practice-next') {
      save({ practiceIndex: l.practiceIndex + 1, practiceSelected: null, practiceChecked: false }); render(); return;
    }
    if (act === 'practice-retry') {
      const wrong = new Set(l.sessions.filter((s) => !s.correct).map((s) => s.qid));
      const qs = questions(); const idx = qs.findIndex((q) => wrong.has(q.id));
      save({ practiceIndex: idx >= 0 ? idx : l.practiceIndex, practiceSelected: null, practiceChecked: false,
        sessions: [...l.sessions.filter((s) => s.correct), ...l.sessions.filter((s) => !s.correct).slice(0, 1)] });
      toast('حلقهٔ تمرین خطاها تشکیل شد'); render(); return;
    }
    if (act === 'import') { const f = doc.getElementById('aiPackageFile'); if (f) f.click(); return; }
    if (act === 'notes') { const f = doc.getElementById('aiNotesFile'); if (f) f.click(); return; }
    if (act === 'export-session') { exportSession(); return; }
    if (act === 'reset') {
      save({ ...DEFAULTS }); const h = harnessRef(); if (h) { h.start('یادگیری', ''); h.plan(60); }
      toast('جلسهٔ محلی بازنشانی شد'); render(); return;
    }
  }

  function onChange(e) {
    const id = e.target.id;
    if (id === 'aiConfidence') { const v = Number(e.target.value); save({ confidence: v });
      const out = doc.getElementById('aiConfFa'); if (out) out.textContent = faNum(v); return; }
    if (id === 'aiGoal' || id === 'aiReasoning') {
      save({ [id === 'aiGoal' ? 'goal' : 'reasoning']: e.target.value }); return;
    }
    if (id === 'aiPackageFile' && e.target.files && e.target.files[0]) {
      const file = e.target.files[0], reader = new FileReader();
      reader.onload = () => {
        try {
          const data = JSON.parse(String(reader.result));
          if (!data || !Array.isArray(data.questions)) throw new Error('questions_missing');
          pkg = data;
          const status = data.source?.contentStatus || 'unknown';
          save({ imported: { name: file.name, questions: data.questions.length,
            tutorials: (data.tutorials || []).length, status, at: stamp() },
            measureStarted: false, measureChecked: false, measureAnswers: {}, teachStep: 0 });
          if (mountPackage) mountPackage(data);
          doc.getElementById('aiStudioImportNote').textContent =
            `بسته «${file.name}» بارگذاری شد: ${faNum(data.questions.length)} سؤال · وضعیت ${status} · ${status === 'approved' || status === 'reviewed' ? 'بازبینیشده' : 'بازبینینشده'}.`;
          bump(1); toast('بستهٔ محتوا بهصورت محلی بارگذاری شد (بدون آپلود)'); render();
        } catch (err) { toast('فایل با فرم اطلاعاتی سازگار نیست'); }
      };
      try { reader.readAsText(file); } catch (_) { toast('خواندن فایل ممکن نشد'); }
      return;
    }
    if (id === 'aiNotesFile' && e.target.files && e.target.files[0]) {
      const file = e.target.files[0], reader = new FileReader();
      reader.onload = () => {
        store.set('ai.studioNotes', String(reader.result).slice(0, 20000));
        doc.getElementById('aiStudioImportNote').textContent =
          `یادداشت «${file.name}» فقط بهعنوان متن پیوست شد؛ منبع درسی محسوب نمیشود.`;
        toast('یادداشت محلی پیوست شد'); render();
      };
      try { reader.readAsText(file); } catch (_) { toast('خواندن فایل ممکن نشد'); }
    }
  }

  function exportSession() {
    const h = harnessRef();
    const payload = {
      kind: 'mimo-local-ai-session', exportedAt: new Date().toISOString(),
      honest: 'no LLM, no network, no generated text',
      package: { packageId: pkg?.packageId, contentStatus: pkg?.source?.contentStatus,
        questions: questions().length, imported: l.imported },
      harness: h ? h.getStatus() : null,
      graph: h?.state?.graph || { propositions: [] },
      studio: { ...l, tokens: tokenStructure() },
      economy: economy.snapshot(),
    };
    const ok = saveText('mimo-ai-session.json', JSON.stringify(payload, null, 2), 'application/json');
    toast(ok ? 'خروجی جلسه ساخته شد' : 'خروجی در این محیط پشتیبانی نمیشود');
  }

  return { mount, render, tokenStructure, state: () => l, package: () => pkg,
    renderGraph, bump, exportSession };
}
