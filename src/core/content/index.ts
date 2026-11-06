import { compileLesson } from "@/core/pedagogy/compiler";
import type { LessonSeed, SeedChapter, SeedSubject } from "@/core/pedagogy/seed-types";
import type { Chapter, Curriculum, Lesson, MCQ, Skill, Subject, SubjectId } from "@/core/types";
import { BIO_LESSONS } from "./lessons-bio";
import { CHEM_LESSONS } from "./lessons-chem";
import { PHYS_LESSONS } from "./lessons-phys";

export const SEED_SUBJECTS: SeedSubject[] = [
  {
    id: "bio12",
    titleFa: "زیست‌شناسی ۳",
    shortFa: "زیست",
    grade: "دوازدهم تجربی",
    accent: "#2F9E7A",
  },
  {
    id: "chem12",
    titleFa: "شیمی ۳",
    shortFa: "شیمی",
    grade: "دوازدهم تجربی و ریاضی",
    accent: "#D9772F",
  },
  {
    id: "phys12",
    titleFa: "فیزیک ۳",
    shortFa: "فیزیک",
    grade: "دوازدهم تجربی و ریاضی",
    accent: "#3B6FD4",
  },
];

export const SEED_CHAPTERS: SeedChapter[] = [
  {
    id: "BIO12-C1",
    subjectId: "bio12",
    order: 1,
    titleFa: "فصل ۱ · مولکول‌های اطلاعاتی",
    subtitleFa: "دنا، رنا، همانندسازی و سه‌گانهٔ ساختار",
  },
  {
    id: "BIO12-C2",
    subjectId: "bio12",
    order: 2,
    titleFa: "فصل ۲ · جریان اطلاعات در یاخته",
    subtitleFa: "رونویسی، پیرایش و ترجمه",
  },
  {
    id: "BIO12-C3",
    subjectId: "bio12",
    order: 3,
    titleFa: "فصل ۳ · انتقال اطلاعات در نسل‌ها",
    subtitleFa: "جهش، وراثت و احتمال",
  },
  {
    id: "CHEM12-C1",
    subjectId: "chem12",
    order: 1,
    titleFa: "فصل ۱ · مولکول‌ها در خدمت تندرستی",
    subtitleFa: "اسید، باز، pH و قدرت اسید",
  },
  {
    id: "CHEM12-C2",
    subjectId: "chem12",
    order: 2,
    titleFa: "فصل ۲ · آسایش و رفاه در سایهٔ شیمی",
    subtitleFa: "صابون، شوینده و پلیمرها",
  },
  {
    id: "PHYS12-C1",
    subjectId: "phys12",
    order: 1,
    titleFa: "فصل ۱ · حرکت بر خط راست",
    subtitleFa: "سرعت، شتاب و نمودارهای حرکت",
  },
  {
    id: "PHYS12-C2",
    subjectId: "phys12",
    order: 2,
    titleFa: "فصل ۲ · دینامیک",
    subtitleFa: "قوانین نیوتون، اصطکاک و حرکت دایره‌ای",
  },
];

export const SEED_LESSONS: LessonSeed[] = [...BIO_LESSONS, ...CHEM_LESSONS, ...PHYS_LESSONS];

/** Chapters → lessons prerequisite chain, derived from curriculum order (no hash mapping!). */
function withPrerequisiteChain(seeds: LessonSeed[]): LessonSeed[] {
  const bySubjectChapter = new Map<string, LessonSeed[]>();
  for (const seed of seeds) {
    const list = bySubjectChapter.get(seed.chapterId) ?? [];
    list.push(seed);
    bySubjectChapter.set(seed.chapterId, list);
  }

  const result: LessonSeed[] = [];
  for (const subject of SEED_SUBJECTS) {
    const chapters = SEED_CHAPTERS.filter((c) => c.subjectId === subject.id).sort((a, b) => a.order - b.order);
    let previousChapterLastLessonId: string | undefined;

    for (const chapter of chapters) {
      const lessons = (bySubjectChapter.get(chapter.id) ?? []).sort((a, b) => a.order - b.order);
      lessons.forEach((lesson, index) => {
        const dependency =
          index === 0 ? previousChapterLastLessonId : lessons[index - 1]?.id;
        result.push({
          ...lesson,
          dependsOnLessonIds: lesson.dependsOnLessonIds ?? (dependency ? [dependency] : []),
        });
      });
      previousChapterLastLessonId = lessons[lessons.length - 1]?.id;
    }
  }
  return result;
}

let cached: Curriculum | null = null;

export function getCurriculum(): Curriculum {
  if (cached) return cached;

  const seeds = withPrerequisiteChain(SEED_LESSONS);
  const lessons: Lesson[] = seeds.map(compileLesson);

  const subjects: Subject[] = SEED_SUBJECTS.map((s) => ({
    id: s.id,
    titleFa: s.titleFa,
    shortFa: s.shortFa,
    grade: s.grade,
    accent: s.accent,
    chapterIds: SEED_CHAPTERS.filter((c) => c.subjectId === s.id)
      .sort((a, b) => a.order - b.order)
      .map((c) => c.id),
  }));

  const chapters: Chapter[] = SEED_CHAPTERS.map((c) => ({
    id: c.id,
    subjectId: c.subjectId,
    order: c.order,
    titleFa: c.titleFa,
    subtitleFa: c.subtitleFa,
    lessonIds: lessons
      .filter((l) => l.chapterId === c.id)
      .sort((a, b) => a.order - b.order)
      .map((l) => l.id),
  }));

  const questions: MCQ[] = lessons.flatMap((l) => l.questions);
  const skills: Skill[] = lessons.flatMap((l) => l.skills);

  cached = {
    subjects,
    chapters,
    lessons,
    questions,
    lessonById: new Map(lessons.map((l) => [l.id, l])),
    chapterById: new Map(chapters.map((c) => [c.id, c])),
    subjectById: new Map(subjects.map((s) => [s.id, s])),
    skillById: new Map(skills.map((s) => [s.id, s])),
  };
  return cached;
}

export function lessonsOfChapter(chapterId: string): Lesson[] {
  return getCurriculum()
    .lessons.filter((l) => l.chapterId === chapterId)
    .sort((a, b) => a.order - b.order);
}

export function chaptersOfSubject(subjectId: SubjectId): Chapter[] {
  return getCurriculum()
    .chapters.filter((c) => c.subjectId === subjectId)
    .sort((a, b) => a.order - b.order);
}

export function curriculumStats() {
  const curriculum = getCurriculum();
  const guardrailPassed = curriculum.lessons.flatMap((l) => l.guardrails).filter((g) => g.passed).length;
  const guardrailTotal = curriculum.lessons.flatMap((l) => l.guardrails).length;
  return {
    subjects: curriculum.subjects.length,
    chapters: curriculum.chapters.length,
    lessons: curriculum.lessons.length,
    questions: curriculum.questions.length,
    skills: curriculum.lessons.flatMap((l) => l.skills).length,
    blocks: curriculum.lessons.reduce((sum, l) => sum + l.blocks.length, 0),
    guardrailPassed,
    guardrailTotal,
  };
}
