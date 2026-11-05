/* ===========================================================================
   Mimo 9.35 CONTENT ENGINE — independent implementation of the measured
   lesson/content structure. No network, no LLM, no generated text.

   Evidence (all local, SERVER CONFIRMED=0):
   - ANALYSIS/MISSION_09/COMPLETE_LESSON_ENGINE_SPEC.md  (asset schema, DSL
     parser, 9 renderer families, validators A6..A11, V/W/X feedback,
     LessonProgress 11-field row, isSolvedCorrectly == tries>=1)
   - app/content/PEDAGOGY.md  (1,029 tutorials / 1,947 chapters / 18,272
     micro-lessons; mean 21.2 words; chapter.type difficulty ramp; 4.5:1
     "do" vs "explain" ratio; HOOK→DO→CHECK→FEEDBACK→REPEAT→CHALLENGE)
   - app/content/MIMO_INFORMATION_FORM.json  (native-shaped form)
   =========================================================================== */
import { STRUCTURED_PACKAGE } from './content-package.js';

export const RENDERER_FAMILIES = ['InteractiveWebView', 'FillTheGap', 'Spell',
  'Selection', 'ValidatedInput', 'SingleChoice', 'MultipleChoice', 'Reveal',
  'None', 'fillTheGap', 'executableFiles', 'noninteractiveSlide', 'text',
  'strong', 'feedback', 'image'];

/* ---------------------------------------------------------------------------
   1. DSL parser — mirrors Lte/c.b(String) @14378108: known tags become
   modules, html/body/unknown are dropped, malformed input yields a slide ([]).
   --------------------------------------------------------------------------- */
export function parseDSL(html) {
  if (typeof html !== 'string' || !html.trim()) return [];
  try {
    const doc = new DOMParser().parseFromString(html, 'text/html');
    const root = doc.body || doc.documentElement;
    if (!root) return [];
    const modules = [];
    const walk = (node) => {
      for (const el of node.children || []) {
        const tag = (el.tagName || '').toLowerCase();
        if (tag === 'p') {
          modules.push({ kind: 'Paragraph', html: el.innerHTML, text: el.textContent,
            visibleIf: el.getAttribute('visible-if') || 'always' });
        } else if (tag === 'code') {
          modules.push({ kind: 'Code', name: el.getAttribute('name') || '',
            lang: el.getAttribute('codelang') || '',
            text: el.textContent, visibleIf: el.getAttribute('visible-if') || 'always' });
        } else if (tag === 'selection') {
          const items = [...el.querySelectorAll('item')].map((it) => ({
            text: it.textContent, correct: it.getAttribute('correct') === 'true',
          }));
          modules.push({ kind: 'Selection', multiple: el.getAttribute('multiple') === 'multiple',
            items, visibleIf: el.getAttribute('visible-if') || 'always' });
        } else if (tag === 'img') {
          modules.push({ kind: 'Image', src: el.getAttribute('src') || '',
            visibleIf: el.getAttribute('visible-if') || 'always' });
        } else if (tag === 'webview') {
          modules.push({ kind: 'Webview', content: el.getAttribute('content') || '',
            visibleIf: el.getAttribute('visible-if') || 'always' });
        } else if (tag === 'interaction') {
          modules.push({ kind: 'Interaction', type: el.getAttribute('type') || '',
            text: el.textContent, visibleIf: el.getAttribute('visible-if') || 'always' });
        } else if (tag === 'database' || tag === 'output') {
          modules.push({ kind: tag === 'database' ? 'Database' : 'Output',
            text: el.textContent });
        } else {
          /* html/body/unknown -> SKIP (measured); keep descending into wrappers */
          walk(el);
        }
      }
    };
    walk(root);
    return modules;
  } catch (_) {
    return []; /* malformed DSL -> empty module list -> noninteractive slide */
  }
}

/* gm.h.a(List): classify the interaction family from the parsed modules. */
export function interactionType(modules) {
  if (!Array.isArray(modules) || !modules.length) return 'None';
  const kindSet = new Set(modules.map((m) => m.kind));
  if (kindSet.has('Interaction')) {
    const it = modules.find((m) => m.kind === 'Interaction');
    if (it.type === 'fillTheGap') return 'FillTheGap';
    if (it.type === 'validatedInput') return 'ValidatedInput';
  }
  if (kindSet.has('Selection')) {
    const sel = modules.find((m) => m.kind === 'Selection');
    if (sel.multiple) return 'MultipleChoice';
    return 'SingleChoice';
  }
  if (kindSet.has('Webview')) return 'InteractiveWebView';
  if (kindSet.has('Code')) return 'executableFiles';
  return 'None';
}

/* A9 normalizer: lowercase, keep letters/digits and exactly these punctuation. */
const KEEP = new Set(['<', '>', '(', ')', ':', '{', '}', ',', '.']);
export function normalizeValidatedInput(s) {
  let out = '';
  for (const c of String(s).toLowerCase()) {
    if (/[a-z0-9]/.test(c) || KEEP.has(c) || /[\u0600-\u06ff]/.test(c)) out += c;
  }
  return out;
}

/* ---------------------------------------------------------------------------
   2. Validators — verbatim logic from COMPLETE_LESSON_ENGINE_SPEC.md §4
   A6 ordered equality (case/order sensitive), A7 all{selected==isCorrect},
   A8 ordered typed tokens, A9/A10 normalized comparison, A11 solvedContent.
   --------------------------------------------------------------------------- */
export function validateAnswer(family, input, module) {
  const m = module || {};
  switch (family) {
    case 'FillTheGap': {                    /* A6 */
      const chosen = (input && input.tokens) || [];
      const correct = (m.correctTokens) || (m.options ? [m.options[m.correctIndex]] : []);
      return chosen.length === correct.length
        && chosen.every((t, i) => String(t) === String(correct[i]));
    }
    case 'Selection':                       /* A7 */
    case 'SingleChoice':
    case 'MultipleChoice': {
      const selected = (input && input.selected) || [];
      const items = (m.items) || (m.options || []).map((o, i) => ({ correct: i === m.correctIndex }));
      if (typeof m.correctIndex === 'number' && !m.items) {
        return selected.length === 1 && selected[0] === m.correctIndex;
      }
      return items.every((it, i) => Boolean(selected.includes(i)) === Boolean(it.correct));
    }
    case 'Spell': {                         /* A8 */
      const typed = (input && input.tokens) || [];
      const expected = m.correctTokens || [];
      return typed.length === expected.length && typed.every((t, i) => t === expected[i]);
    }
    case 'ValidatedInput': {                /* A9 + A10 */
      const expected = m.expectedText != null ? m.expectedText : (m.options || [])[m.correctIndex];
      if (expected == null) return false;
      return normalizeValidatedInput(input && input.text) === normalizeValidatedInput(expected);
    }
    case 'executableFiles': {               /* A11 */
      const files = (input && input.files) || [];
      const solved = m.solvedContent || [];
      return files.length === solved.length && files.every((f, i) => f === solved[i]);
    }
    case 'Reveal':
    case 'None':
    case 'noninteractiveSlide':
      return true;                          /* no validation, Continue advances */
    default:
      return false;
  }
}

/* ---------------------------------------------------------------------------
   3. Engine over the native-shaped content package
   --------------------------------------------------------------------------- */
export function createContentEngine({ store, now } = {}) {
  const pkg = STRUCTURED_PACKAGE;
  const clock = now || (() => Date.now());
  const persist = (key, value) => {
    try { if (store && store.set) store.set(key, value); } catch (_) { /* blocked */ }
    return value;
  };
  const read = (key, fallback) => {
    try {
      /* store.get() takes ONE argument and returns undefined for a missing path */
      const v = store && store.get ? store.get(key) : undefined;
      return (v === undefined || v === null) ? fallback : v;
    } catch (_) { return fallback; }
  };

  const tutorialIndex = new Map(pkg.tutorials.map((t) => [t.id, t]));
  const chapterIndex = new Map();
  const lessonIndex = new Map();
  for (const t of pkg.tutorials) {
    for (const c of t.chapters) {
      chapterIndex.set(`${t.id}:${c.id}`, c);
      for (const l of c.lessons) lessonIndex.set(`${t.id}:${c.id}:${l.id}`, l);
    }
  }
  const questionIndex = new Map(pkg.questions.map((q) => [q.id, q]));

  const api = {
    pkg,
    tracks: () => pkg.tracks,
    sections: (trackId) => {
      const t = pkg.tracks.find((x) => x.id === trackId) || pkg.tracks[0];
      return t ? t.sections : [];
    },
    tutorials: (sectionName) => {
      const secs = pkg.tracks[0].sections.filter((s) => !sectionName || s.name === sectionName);
      const ids = new Set(secs.flatMap((s) => s.tutorialIds));
      return pkg.tutorials.filter((t) => ids.has(t.id));
    },
    tutorial: (id) => tutorialIndex.get(Number(id)),
    chapter: (tutId, chId) => chapterIndex.get(`${Number(tutId)}:${Number(chId)}`),
    lesson: (tutId, chId, lessonId) => lessonIndex.get(`${Number(tutId)}:${Number(chId)}:${Number(lessonId)}`),
    lessonsOf: (tutId, chId) => {
      const c = chapterIndex.get(`${Number(tutId)}:${Number(chId)}`);
      return c ? c.lessons : [];
    },
    questions: () => pkg.questions,
    question: (id) => questionIndex.get(id),
    questionsForTopic: (topicId) => pkg.questions.filter((q) => q.topicId === topicId),
    parseDSL, interactionType, validateAnswer, normalizeValidatedInput,

    /* Measured lifecycle: V()/X() -> attempts++, tries, 11-field progress row,
       inQueue=true, publishSetVersion=753, isSolvedCorrectly === tries>=1. */
    submit({ lessonRef, block, answer }) {
      const family = api.familyOfBlock(block);
      const ok = validateAnswer(family, answer, block);
      const rows = read('content.lessonProgress', []);
      const prev = rows.find((r) => r.lessonId === lessonRef.lessonId);
      const attempts = (prev ? prev.attempts : 0) + 1;
      const row = {
        lessonId: lessonRef.lessonId,
        lessonIndex: lessonRef.lessonIndex == null ? 0 : lessonRef.lessonIndex,
        chapterId: lessonRef.chapterId,
        tutorialId: lessonRef.tutorialId,
        trackId: lessonRef.trackId || 1,
        tutorialTitle: lessonRef.tutorialTitle || '',
        tries: ok ? 1 : 0,
        attempts,
        isPracticeProgress: Boolean(lessonRef.isPracticeProgress),
        inQueue: true,
        publishSetVersion: 753,
        completedAt: clock(),
        startedAt: prev ? prev.startedAt : clock(),
      };
      const next = rows.filter((r) => r.lessonId !== lessonRef.lessonId).concat(row);
      persist('content.lessonProgress', next);
      if (!ok) {
        const mistakes = read('content.mistakes', []);
        mistakes.push({ questionKey: block.questionId || lessonRef.lessonId,
          answerKeyVersion: 1, topicId: lessonRef.topicId || '',
          difficulty: (api.question(block.questionId) || {}).difficulty || 'unknown',
          ts: clock(), resolved: false, consecutiveCorrect: 0 });
        persist('content.mistakes', mistakes);
      } else {
        const mistakes = read('content.mistakes', []);
        const open = mistakes.filter((m) => !m.resolved
          && m.questionKey === (block.questionId || lessonRef.lessonId));
        for (const m of open) {
          m.consecutiveCorrect = (m.consecutiveCorrect || 0) + 1;
          if (m.consecutiveCorrect >= 2) m.resolved = true; /* FSRS-lite rule */
        }
        persist('content.mistakes', mistakes);
      }
      return {
        ok, family, progress: row,
        isSolvedCorrectly: row.tries >= 1,
        feedback: ok ? (block.explanationFa || 'درست شد!')
          : (block.explanationFa || 'دوباره امتحان کن.'),
        wrongLatch: !ok,
      };
    },
    /* noninteractive slides still create progress with tries=1, attempts=1 */
    advance({ lessonRef }) {
      const rows = read('content.lessonProgress', []);
      if (rows.some((r) => r.lessonId === lessonRef.lessonId)) return;
      rows.push({
        lessonId: lessonRef.lessonId, lessonIndex: lessonRef.lessonIndex || 0,
        chapterId: lessonRef.chapterId, tutorialId: lessonRef.tutorialId,
        trackId: 1, tutorialTitle: lessonRef.tutorialTitle || '',
        tries: 1, attempts: 1, isPracticeProgress: false, inQueue: true,
        publishSetVersion: 753, completedAt: clock(), startedAt: clock(),
      });
      persist('content.lessonProgress', rows);
    },
    familyOfBlock(block) {
      const r = block && block.renderer;
      if (r === 'MultipleChoice') return 'MultipleChoice';
      if (r === 'fillTheGap') return 'FillTheGap';
      if (r === 'validatedInput') return 'ValidatedInput';
      if (r === 'executableFiles') return 'executableFiles';
      if (r === 'feedback') return 'Reveal';
      return 'None';
    },
    progress: () => read('content.lessonProgress', []),
    mistakes: () => read('content.mistakes', []),
    reviewQueue: () => api.mistakes().filter((m) => !m.resolved),
    stats: () => ({
      tracks: pkg.tracks.length,
      sections: pkg.tracks[0].sections.length,
      tutorials: pkg.tutorials.length,
      chapters: pkg.tutorials.reduce((n, t) => n + t.chapters.length, 0),
      microLessons: pkg.tutorials.reduce((n, t) => n + t.chapters.reduce((a, c) => a + c.lessons.length, 0), 0),
      blocks: pkg.tutorials.reduce((n, t) => n + t.chapters.reduce(
        (a, c) => a + c.lessons.reduce((b, l) => b + l.blocks.length, 0), 0), 0),
      questions: pkg.questions.length,
      knownAnswers: pkg.questions.filter((q) => q.correctIndex !== null).length,
      rendererFamilies: [...new Set(pkg.tutorials.flatMap((t) => t.chapters.flatMap(
        (c) => c.lessons.flatMap((l) => l.blocks.map((b) => b.renderer)))))].sort(),
      contentStatus: pkg.source.contentStatus,
      reviewStatus: pkg.provenance.reviewStatus,
      externalProvider: 'not-configured',
      generatesText: false,
      serverConfirmed: false,
    }),
  };
  return api;
}
