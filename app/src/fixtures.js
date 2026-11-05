/**
 * PLACEHOLDER TEST DATA — deliberately isolated from the final content schema.
 *
 * No curriculum, lesson text, explanation or new questions are authored here.
 * The question bank is derived from the fixture questions that ALREADY EXIST
 * in the approved v12.5-fa prototype (window.PROTO.questions / QBANK).
 * The curriculum graph only contains IDs and neutral labels in the M09 shape
 * (track -> section -> tutorial/chapter -> lesson), so real content can be
 * dropped in later without touching the app logic.
 */

export const PLACEHOLDER = Object.freeze({
  tag: 'PLACEHOLDER',
  contentReady: false,
  serverConfirmed: false,
  source: 'v12.5-fa prototype fixture data + neutral labels',
});

/** Neutral path/program labels taken from the approved prototype's KONKUR data. */
export const PATHS = Object.freeze([
  { id: 'grade12', fa: 'یادگیری همگام با برنامه آزمون دوازدهم', icon: 'ic_cap_filled' },
  { id: 'grade11', fa: 'یادگیری همگام با برنامه آزمون یازدهم', icon: 'ic_cap' },
  { id: 'grade10', fa: 'یادگیری همگام با برنامه آزمون دهم', icon: 'ic_trophy' },
]);

export const SUBJECTS = Object.freeze(['زیست', 'شیمی', 'فیزیک', 'ریاضی']);

/** M09-shaped placeholder graph: 3 tracks, 9 sections, 3 chapters/section,
 *  4 lessons/chapter. IDs are stable so persisted state survives a rebuild. */
export function buildCurriculum() {
  const tracks = PATHS.map((p) => ({
    id: p.id, title: p.fa, icon: p.icon, locale: 'fa',
    publishSetVersion: 753, placeholder: true,
  }));
  const sections = [];
  const chapters = [];
  const lessons = [];
  for (const track of tracks) {
    for (let s = 1; s <= 3; s += 1) {
      const section = {
        id: `${track.id}-s${s}`, trackId: track.id, index: s,
        title: `فصل ${s}`, placeholder: true,
      };
      sections.push(section);
      for (let c = 1; c <= 3; c += 1) {
        const chapter = {
          id: `${section.id}-c${c}`, sectionId: section.id, trackId: track.id,
          index: c, title: `درس ${c}`, placeholder: true,
        };
        chapters.push(chapter);
        for (let l = 1; l <= 4; l += 1) {
          lessons.push({
            id: `${chapter.id}-l${l}`, chapterId: chapter.id,
            sectionId: section.id, trackId: track.id, index: l,
            title: `گام ${l}`, renderer: l === 4 ? 'MultipleChoice' : 'noninteractiveSlide',
            placeholder: true,
          });
        }
      }
    }
  }
  return {
    tracks, sections, chapters, lessons,
    lessonIds: lessons.map((l) => l.id),
    meta: { ...PLACEHOLDER, counts: {
      tracks: tracks.length, sections: sections.length,
      chapters: chapters.length, lessons: lessons.length,
    } },
  };
}

/** Reuse the prototype's existing fixture questions; do not author new ones. */
export function buildQuestionBank(protoQuestions = []) {
  return protoQuestions.map((q, i) => ({
    id: `q-${i + 1}`,
    subject: String(q.sub || '').split(' · ')[0] || '—',
    topic: String(q.sub || ''),
    stem: String(q.stem || ''),
    options: (q.opts || []).map((label, oi) => ({
      id: oi, label: String(label), isCorrect: oi === Number(q.ok),
    })),
    correctId: Number(q.ok),
    explanation: String(q.expl || ''),
    placeholder: true,
  }));
}

/** Placeholder leaderboard rows. No server ranking is simulated. */
export const LEADERBOARD_PLACEHOLDER = Object.freeze([
  { rank: 1, name: 'کاربر نمونه ۱', xp: 980, local: true },
  { rank: 2, name: 'کاربر نمونه ۲', xp: 840, local: true },
  { rank: 3, name: 'کاربر نمونه ۳', xp: 720, local: true },
  { rank: 4, name: 'کاربر نمونه ۴', xp: 610, local: true },
  { rank: 5, name: 'شما', xp: 480, self: true, local: true },
]);

/** Placeholder exam catalogue (7 labelled sections from the prototype). */
export const EXAM_KINDS = Object.freeze([
  { id: 'comprehensive', fa: 'جامع', minutes: 270 },
  { id: 'timed', fa: 'زماندار', minutes: 30 },
  { id: 'single', fa: 'تکدرسی', minutes: 30 },
  { id: 'topic', fa: 'مبحثی', minutes: 20 },
  { id: 'monthly', fa: 'این ماه', minutes: 60 },
  { id: 'analytical', fa: 'تحلیلی', minutes: 45 },
  { id: 'review', fa: 'جمع بندی', minutes: 45 },
]);
