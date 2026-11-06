"use client";

import { useMemo, useState } from "react";
import {
  BookOpen,
  Check,
  ChevronLeft,
  Clock,
  Flame,
  Lock,
  Play,
  Sparkles,
  Target,
  Timer,
} from "lucide-react";
import { chaptersOfSubject, lessonsOfChapter } from "@/core/content";
import { lessonLock, type LessonLock } from "@/core/state/learner";
import type { Lesson, SubjectId } from "@/core/types";
import { useLearner } from "@/state/LearnerProvider";
import { Button, Card, Chip, Modal, Progress, Ring, SectionTitle, Stars, cx } from "@/components/ui/kit";

const SUBJECT_ICONS: Record<SubjectId, string> = {
  bio12: "🧬",
  chem12: "⚗️",
  phys12: "📐",
};

export function PathTab({ onStartLesson }: { onStartLesson: (lessonId: string) => void }) {
  const { state, curriculum } = useLearner();
  const [subjectId, setSubjectId] = useState<SubjectId>("bio12");
  const [previewLessonId, setPreviewLessonId] = useState<string | null>(null);

  const subject = curriculum.subjectById.get(subjectId)!;
  const chapters = useMemo(() => chaptersOfSubject(subjectId), [subjectId]);
  const subjectLessons = useMemo(
    () => chapters.flatMap((chapter) => lessonsOfChapter(chapter.id)),
    [chapters],
  );

  const completed = subjectLessons.filter((l) => (state.lessons[l.id]?.completions ?? 0) > 0).length;
  const nextLesson =
    subjectLessons.find((lesson) => lessonLock(state, lesson) === "available") ??
    subjectLessons.find((lesson) => lessonLock(state, lesson) === "in_progress") ??
    subjectLessons[0];

  const preview = previewLessonId ? curriculum.lessonById.get(previewLessonId) : null;
  const previewProgress = preview ? state.lessons[preview.id] : undefined;
  const previewLock = preview ? lessonLock(state, preview) : "locked";

  return (
    <div className="space-y-4 pb-2">
      <div className="flex gap-2 overflow-x-auto pb-1 scrollbar-thin">
        {curriculum.subjects.map((item) => (
          <button
            key={item.id}
            onClick={() => setSubjectId(item.id)}
            className={cx(
              "flex min-w-[112px] flex-1 items-center justify-center gap-2 rounded-2xl border px-3 py-2.5 text-[12.5px] font-bold transition",
              item.id === subjectId
                ? "border-transparent text-white shadow-[0_8px_20px_rgba(126,75,222,0.25)]"
                : "border-[var(--line)] bg-[var(--surface)] text-[var(--ink-soft)] hover:bg-[var(--surface-2)]",
            )}
            style={item.id === subjectId ? { background: item.accent } : undefined}
          >
            <span aria-hidden>{SUBJECT_ICONS[item.id]}</span>
            {item.shortFa}
          </button>
        ))}
      </div>

      <Card className="relative overflow-hidden p-4">
        <div className="mimo-dot-grid pointer-events-none absolute inset-0 opacity-60" />
        <div className="relative flex items-center gap-4">
          <Ring value={subjectLessons.length ? (completed / subjectLessons.length) * 100 : 0} size={82} stroke={7}>
            <span className="tabular text-[17px] font-extrabold">{completed}</span>
            <span className="text-[9.5px] text-[var(--ink-faint)]">از {subjectLessons.length}</span>
          </Ring>
          <div className="min-w-0 flex-1">
            <div className="text-[11px] font-bold" style={{ color: subject.accent }}>
              {subject.grade}
            </div>
            <h2 className="truncate text-[16px] font-extrabold">{subject.titleFa}</h2>
            <p className="mt-1 line-clamp-2 text-[11.5px] leading-5 text-[var(--ink-soft)]">
              شش نقش میمو، قید تصمیم‌ساز و تلهٔ طراح — هر درس یک زنجیرهٔ کامل از کتاب.
            </p>
            <div className="mt-2 flex flex-wrap gap-1.5">
              <Chip tone="purple" icon={<Sparkles size={11} />}>
                {chapters.length} فصل
              </Chip>
              <Chip tone="success" icon={<Check size={11} />}>
                {subjectLessons.reduce((sum, l) => sum + l.questions.length, 0)} تست تحلیل‌شده
              </Chip>
            </div>
          </div>
        </div>
        {nextLesson && (
          <Button full className="relative mt-4" onClick={() => setPreviewLessonId(nextLesson.id)}>
            <Play size={15} />
            ادامهٔ مسیر: {nextLesson.titleFa}
          </Button>
        )}
      </Card>

      <div className="space-y-5">
        {chapters.map((chapter) => {
          const lessons = lessonsOfChapter(chapter.id);
          const done = lessons.filter((l) => (state.lessons[l.id]?.completions ?? 0) > 0).length;
          const chapterMastery = Math.round(
            (lessons.reduce((sum, lesson) => {
              const concept = state.skills[`${lesson.id}.concept`]?.pKnown ?? 0;
              const application = state.skills[`${lesson.id}.application`]?.pKnown ?? 0;
              return sum + (concept + application) / 2;
            }, 0) /
              lessons.length) *
              100,
          );

          return (
            <section key={chapter.id}>
              <div className="mb-2 flex items-center justify-between gap-2 px-1">
                <div className="min-w-0">
                  <h3 className="truncate text-[13px] font-extrabold">{chapter.titleFa}</h3>
                  <p className="truncate text-[10.5px] text-[var(--ink-faint)]">{chapter.subtitleFa}</p>
                </div>
                <div className="flex shrink-0 items-center gap-2">
                  <span className="tabular text-[10.5px] font-bold text-[var(--ink-soft)]">{chapterMastery}٪</span>
                  <div className="w-16">
                    <Progress value={(done / lessons.length) * 100} height={5} color={subject.accent} />
                  </div>
                </div>
              </div>
              <LessonPath
                lessons={lessons}
                onSelect={setPreviewLessonId}
                accent={subject.accent}
                state={state}
              />
            </section>
          );
        })}
      </div>

      <Card className="flex items-start gap-2 p-3 text-[11px] leading-5 text-[var(--ink-soft)]">
        <Target size={15} className="mt-0.5 shrink-0 text-[var(--mimo-button)]" />
        <p>
          قفل هر درس با قانون محلی <span className="font-mono-code text-[10px]">ADD-04</span>{" "}
          باز می‌شود: تکمیل درس قبلی (tries ≥ ۱) یا تسلط BKT روی مهارت پیش‌نیاز.
        </p>
      </Card>

      <Modal
        open={Boolean(preview)}
        onClose={() => setPreviewLessonId(null)}
        title={preview?.titleFa ?? ""}
        subtitle={preview?.subtitleFa}
        footer={
          <div className="flex gap-2">
            {previewLock === "locked" ? (
              <Button variant="outline" full disabled>
                <Lock size={15} /> ابتدا درس قبلی را کامل کن
              </Button>
            ) : (
              <Button
                full
                onClick={() => {
                  if (preview) {
                    setPreviewLessonId(null);
                    onStartLesson(preview.id);
                  }
                }}
              >
                <Play size={15} />
                {previewLock === "in_progress" ? "ادامهٔ درس" : "شروع درس"}
              </Button>
            )}
          </div>
        }
      >
        {preview && (
          <div className="space-y-3">
            <div className="flex flex-wrap items-center gap-2">
              <Chip tone="purple" icon={<Clock size={11} />}>
                {preview.minutes} دقیقه
              </Chip>
              <Chip tone="neutral" icon={<Timer size={11} />}>
                ۶ نقش میمو
              </Chip>
              <Chip tone="success" icon={<Check size={11} />}>
                گاردریل {Math.round((preview.guardrails.filter((g) => g.passed).length / preview.guardrails.length) * 100)}٪
              </Chip>
              {previewProgress?.stars ? <Stars count={previewProgress.stars} /> : null}
            </div>

            <div className="rounded-2xl bg-[var(--surface-2)] p-3">
              <div className="mb-1 text-[10.5px] font-bold text-[var(--mimo-button)]">اصل بدیهی (Principle i)</div>
              <p className="text-[12px] leading-6 text-[var(--ink)]">{preview.axiomFa}</p>
            </div>

            <div className="rounded-2xl border border-[var(--line)] p-3">
              <div className="mb-1 text-[10.5px] font-bold text-[var(--warning)]">کشف باانگیزه (Principle ii)</div>
              <p className="text-[12px] leading-6 text-[var(--ink-soft)]">{preview.hookFa}</p>
            </div>

            <div>
              <div className="mb-1.5 text-[11px] font-bold text-[var(--ink-soft)]">شش نقش این درس</div>
              <div className="grid grid-cols-3 gap-1.5">
                {preview.blocks.map((block) => (
                  <div
                    key={block.id}
                    className="rounded-xl bg-[var(--surface-2)] px-2 py-2 text-center text-[10px] font-semibold text-[var(--ink-soft)]"
                  >
                    <div className="mb-0.5 text-[9px] text-[var(--mimo-button)]">{block.role}</div>
                    {block.mechanic}
                  </div>
                ))}
              </div>
            </div>

            <p className="text-[10.5px] leading-5 text-[var(--ink-faint)]">منبع: {preview.sourceRef}</p>
          </div>
        )}
      </Modal>
    </div>
  );
}

function LessonPath({
  lessons,
  onSelect,
  accent,
  state,
}: {
  lessons: Lesson[];
  onSelect: (lessonId: string) => void;
  accent: string;
  state: ReturnType<typeof useLearner>["state"];
}) {
  const rowHeight = 116;
  const nodeSize = 82;
  const totalHeight = lessons.length * rowHeight;
  const xFor = (index: number) => (index % 2 === 0 ? 21 : 79);
  const yFor = (index: number) => index * rowHeight + rowHeight / 2;

  const segments = lessons.slice(0, -1).map((_, index) => {
    const x1 = xFor(index);
    const y1 = yFor(index);
    const x2 = xFor(index + 1);
    const y2 = yFor(index + 1);
    const mid = (y1 + y2) / 2;
    return {
      d: `M ${x1} ${y1} C ${x1} ${mid - 6}, ${x2} ${mid + 6}, ${x2} ${y2}`,
      done: (state.lessons[lessons[index].id]?.completions ?? 0) > 0,
    };
  });

  return (
    <div className="relative" style={{ height: totalHeight }}>
      <svg
        className="pointer-events-none absolute inset-0 h-full w-full"
        viewBox={`0 0 100 ${totalHeight}`}
        preserveAspectRatio="none"
        aria-hidden
      >
        {segments.map((segment, index) => (
          <g key={index}>
            <path d={segment.d} fill="none" stroke="var(--surface-3)" strokeWidth={7} strokeLinecap="round" />
            {segment.done && (
              <path
                d={segment.d}
                fill="none"
                stroke={accent}
                strokeWidth={4}
                strokeLinecap="round"
                strokeDasharray="1 9"
              />
            )}
          </g>
        ))}
      </svg>

      {lessons.map((lesson, index) => {
        const lock: LessonLock = lessonLock(state, lesson);
        const progress = state.lessons[lesson.id];
        const isLeft = index % 2 === 0;
        const labelStyle = isLeft
          ? { left: "34%", right: "0%" }
          : { left: "0%", right: "34%" };
        const concept = state.skills[`${lesson.id}.concept`]?.pKnown ?? 0;

        return (
          <div key={lesson.id} className="absolute inset-x-0" style={{ top: index * rowHeight, height: rowHeight }}>
            <button
              onClick={() => onSelect(lesson.id)}
              aria-label={lesson.titleFa}
              className={cx(
                "absolute top-1/2 -translate-y-1/2 rounded-full transition-transform hover:scale-[1.04] active:scale-95",
                lock === "available" && "animate-breathe",
              )}
              style={{
                width: nodeSize,
                height: nodeSize,
                left: `calc(${xFor(index)}% - ${nodeSize / 2}px)`,
              }}
            >
              <span
                className={cx(
                  "absolute inset-0 rounded-full",
                  lock === "locked" ? "bg-[var(--surface-2)]" : "bg-[var(--surface)]",
                )}
                style={{
                  border: `3px solid ${lock === "locked" ? "var(--surface-3)" : accent}`,
                  boxShadow: lock === "available" ? `0 12px 26px ${accent}33` : "var(--shadow-card)",
                }}
              />
              <span
                className="absolute inset-[6px] rounded-full"
                style={{
                  background:
                    lock === "locked"
                      ? "var(--surface-3)"
                      : lock === "mastered"
                        ? `${accent}22`
                        : "var(--surface-2)",
                }}
              />
              <span className="absolute inset-0 flex flex-col items-center justify-center gap-0.5">
                {lock === "locked" ? (
                  <Lock size={20} className="text-[var(--ink-faint)]" />
                ) : lock === "mastered" ? (
                  <Check size={26} strokeWidth={3} style={{ color: accent }} />
                ) : (
                  <Play size={22} style={{ color: accent }} fill={`${accent}33`} />
                )}
                <span className="text-[9px] font-bold text-[var(--ink-faint)]">
                  درس {lesson.order}
                </span>
              </span>
              {progress?.stars ? (
                <span className="absolute -bottom-1 left-1/2 -translate-x-1/2 rounded-full bg-[var(--surface)] px-1 py-0.5 shadow">
                  <Stars count={progress.stars} size={9} />
                </span>
              ) : null}
              {lock === "available" && (
                <span
                  className="absolute -top-1 right-0 rounded-full px-1.5 py-0.5 text-[8.5px] font-bold text-white"
                  style={{ background: accent }}
                >
                  جدید
                </span>
              )}
            </button>

            <div className="absolute top-1/2 flex -translate-y-1/2 flex-col gap-1" style={labelStyle}>
              <div className="flex items-center gap-1.5">
                {isLeft ? <ChevronLeft size={13} className="shrink-0 text-[var(--ink-faint)]" /> : null}
                <h4
                  className={cx(
                    "truncate text-[12.5px] font-extrabold",
                    lock === "locked" ? "text-[var(--ink-faint)]" : "text-[var(--ink)]",
                  )}
                >
                  {lesson.titleFa}
                </h4>
                {!isLeft ? <ChevronLeft size={13} className="shrink-0 text-[var(--ink-faint)]" /> : null}
              </div>
              <p className="line-clamp-1 text-[10.5px] text-[var(--ink-faint)]">{lesson.subtitleFa}</p>
              <div className="flex items-center gap-2">
                <div className="w-16">
                  <Progress value={concept * 100} height={4} color={accent} />
                </div>
                <span className="tabular text-[9.5px] text-[var(--ink-faint)]">
                  تسلط {Math.round(concept * 100)}٪
                </span>
              </div>
            </div>
          </div>
        );
      })}
    </div>
  );
}
