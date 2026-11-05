/**
 * «مسیر آموزشی» — a COMPLETE, clickable learning path built ONLY from the
 * approved v12.5-fa prototype payload (var KONKUR in proto-data.js).
 *
 * No new lesson text, answer or curriculum is authored here: the 12 courses /
 * 60 chapters / 180 lesson titles are the ones already approved in the
 * prototype, and the interactive step uses the 20 existing QBANK questions
 * with their real answers and explanations. Final textbook content is loaded
 * later through the content form / package importer.
 */
import { faNum } from './util.js';

export const PATH_DISCLAIMER = 'عنوان درسها از سرفصلهای پروتوتایپ تأییدشده و تمرینها از همان '
  + 'بانک سؤال پروتوتایپاند؛ درسنامهٔ نهایی پس از تحویل منابع وارد میشود. '
  + 'هیچ فرمول یا رفتار سروری تأیید نشده است.';

export function buildRealCurriculum() {
  const src = (typeof KONKUR !== 'undefined' && KONKUR) ? KONKUR : null;
  const courses = (src?.courses || []).map((c) => ({
    key: c.key, name: c.name, subject: c.subject, grade: c.grade, icon: c.icon,
    chapters: (c.chapters || []).map((ch, ci) => ({
      id: `${c.key}:c${ci + 1}`, ordinal: ch.ordinal, name: ch.name,
      lessons: (ch.lessons || []).map((title, li) => ({
        id: `${c.key}:c${ci + 1}:l${li + 1}`, title, chapterId: `${c.key}:c${ci + 1}`,
        courseKey: c.key, index: ci * 3 + li + 1,
      })),
    })),
  }));
  return {
    programs: src?.programs || [], note: src?.note || '',
    subjects: src?.subjects || [], courses,
    totalChapters: courses.reduce((n, c) => n + c.chapters.length, 0),
    totalLessons: courses.reduce((n, c) => n + c.chapters.reduce((m, ch) => m + ch.lessons.length, 0), 0),
  };
}

const DEFAULTS = {
  programKey: 'grade12', courseKey: 'bio12', completed: [], currentId: null,
  answers: {}, attempts: 0, correct: 0, sessions: [],
};

export function createLearningPath(store, economy, proto, starterQuestions = []) {
  const curriculum = buildRealCurriculum();
  let s = store.get('progress.learningPath');
  if (!s || typeof s !== 'object') { s = { ...DEFAULTS }; store.set('progress.learningPath', s); }
  s = { ...DEFAULTS, ...s };

  const save = (patch) => { s = { ...s, ...patch }; store.set('progress.learningPath', s); return s; };
  const course = () => curriculum.courses.find((c) => c.key === s.courseKey) || curriculum.courses[0] || null;
  const flat = () => (course() ? course().chapters.flatMap((ch) => ch.lessons) : []);
  const byId = (id) => flat().find((l) => l.id === id) || null;

  function statusOf(id) {
    if (s.completed.includes(id)) return 'done';
    const list = flat(), i = list.findIndex((l) => l.id === id);
    if (i < 0) return 'locked';
    if (i === 0 || s.completed.includes(list[i - 1].id)) return i === s.currentId ? 'current' : 'open';
    return 'locked';
  }
  function nextId() {
    const list = flat();
    return (list.find((l) => !s.completed.includes(l.id) && (statusOf(l.id) !== 'locked')) || list[0])?.id || null;
  }
  function open(id) {
    if (statusOf(id) === 'locked') return { ok: false, reason: 'locked' };
    save({ currentId: id }); return { ok: true, lesson: byId(id) };
  }
  function questionFor(id) {
    const pool = (proto && proto.questions && proto.questions.length) ? proto.questions : [];
    let h = 0; for (const c of String(id)) h = (h * 31 + c.charCodeAt(0)) >>> 0;
    if (pool.length) {
      const q = pool[h % pool.length];
      return { stem: q.stem, options: q.opts, correctIndex: q.ok, explanation: q.expl,
        ref: `prototype:v12.5-fa:qbank-${(h % pool.length) + 1}` };
    }
    if (starterQuestions.length) {
      const q = starterQuestions[h % starterQuestions.length];
      return { stem: q.stemFa, options: q.options, correctIndex: q.correctIndex,
        explanation: q.explanationFa, ref: q.trace?.sourceRef || 'starter' };
    }
    return null;
  }
  function complete(id, correct, difficulty = 2) {
    if (s.completed.includes(id)) return { ok: false, reason: 'already-done' };
    const done = [...s.completed, id];
    save({ completed: done, attempts: s.attempts + 1, correct: s.correct + (correct ? 1 : 0),
      currentId: nextId() === id ? null : s.currentId });
    economy.apply('lesson-complete', { reason: id });
    economy.apply(correct ? 'answer-correct' : 'answer-wrong',
      { difficulty, subjectFactor: 1, firstTry: correct, reason: id });
    const list = flat(), i = list.findIndex((l) => l.id === id);
    if (i >= 0 && (i + 1) % 3 === 0) economy.apply('chapter-complete', { reason: id });
    return { ok: true, completed: done.length, total: list.length };
  }
  function progress() {
    const total = flat().length, done = s.completed.filter((id) => flat().some((l) => l.id === id)).length;
    return { done, total, percent: total ? Math.round((done / total) * 100) : 0,
      doneFa: faNum(done), totalFa: faNum(total), percentFa: faNum(total ? Math.round(done / total * 100) : 0) };
  }
  return {
    curriculum, state: () => s, course, flat, byId, statusOf, nextId, open, questionFor, complete, progress,
    setProgram(k) { return save({ programKey: k }); },
    setCourse(k) {
      const c = curriculum.courses.find((x) => x.key === k); if (!c) return false;
      return save({ courseKey: k, currentId: null });
    },
    reset() { return save({ ...DEFAULTS }); },
  };
}
