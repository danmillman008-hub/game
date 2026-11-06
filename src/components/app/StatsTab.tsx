"use client";

import {
  Activity,
  BarChart3,
  Brain,
  Flame,
  Gauge,
  Lightbulb,
  Play,
  Sparkles,
  Target,
  TrendingUp,
  Trophy,
} from "lucide-react";
import { masteryBand, MASTERY_BAND_FA } from "@/core/algorithms/bkt";
import { outerFringe, selectNextSkill } from "@/core/algorithms/kst";
import { flowStatus } from "@/core/algorithms/flow";
import { DAY_MS } from "@/core/algorithms/fsrs";
import {
  lessonLock,
  masteryMap,
  recentAccuracy,
  summarize,
} from "@/core/state/learner";
import { useLearner } from "@/state/LearnerProvider";
import { Button, Card, Chip, Progress, Ring, SectionTitle, Sparkline } from "@/components/ui/kit";

export function StatsTab({ onStartLesson }: { onStartLesson: (lessonId: string) => void }) {
  const { state, curriculum, graph } = useLearner();
  const summary = summarize(state, curriculum);
  const mastery = masteryMap(state);
  const flow = flowStatus(recentAccuracy(state));
  const next = selectNextSkill(graph, mastery, flow.accuracy);
  const fringe = outerFringe(graph, mastery);

  const nextSkill = next.skillId ? curriculum.skillById.get(next.skillId) : undefined;
  const nextLesson = nextSkill
    ? (() => {
        const lesson = curriculum.lessonById.get(nextSkill.lessonId);
        return lesson ? { lesson, skill: nextSkill, lock: lessonLock(state, lesson) } : null;
      })()
    : null;

  const chapterStats = curriculum.chapters.map((chapter) => {
    const lessons = curriculum.lessons.filter((lesson) => lesson.chapterId === chapter.id);
    const value =
      lessons.reduce((sum, lesson) => {
        const concept = state.skills[`${lesson.id}.concept`]?.pKnown ?? 0;
        const application = state.skills[`${lesson.id}.application`]?.pKnown ?? 0;
        return sum + (concept + application) / 2;
      }, 0) / Math.max(1, lessons.length);
    return {
      chapter,
      value,
      subject: curriculum.subjectById.get(chapter.subjectId)!,
      completed: lessons.filter((lesson) => (state.lessons[lesson.id]?.completions ?? 0) > 0).length,
      total: lessons.length,
    };
  });

  const activityDays = 14;
  const activityNow = Date.now();
  const dailyActivity = Array.from({ length: activityDays }, () => 0);
  for (const attempt of state.attempts) {
    const offset = Math.floor((activityNow - attempt.at) / DAY_MS);
    if (offset >= 0 && offset < activityDays) dailyActivity[activityDays - 1 - offset] += 1;
  }

  const examCountdown = Math.max(
    0,
    Math.ceil((new Date(state.profile.examDate).getTime() - Date.now()) / DAY_MS),
  );

  return (
    <div className="space-y-4">
      <div className="grid grid-cols-2 gap-2">
        <Card className="p-3.5">
          <div className="flex items-center justify-between">
            <span className="text-[11px] font-semibold text-[var(--ink-faint)]">تسلط کل</span>
            <span className="rounded-lg bg-[var(--mimo-soft)] p-1.5 text-[var(--mimo-button)]">
              <Brain size={13} />
            </span>
          </div>
          <div className="mt-1 flex items-baseline gap-1">
            <span className="tabular text-[24px] font-extrabold">{summary.masteredSkills}</span>
            <span className="text-[10.5px] text-[var(--ink-faint)]">از {summary.totalSkills} مهارت</span>
          </div>
          <Progress className="mt-2" value={(summary.masteredSkills / summary.totalSkills) * 100} height={5} />
        </Card>

        <Card className="p-3.5">
          <div className="flex items-center justify-between">
            <span className="text-[11px] font-semibold text-[var(--ink-faint)]">استریک</span>
            <span className="rounded-lg bg-[var(--warning-soft)] p-1.5 text-[var(--warning)]">
              <Flame size={13} />
            </span>
          </div>
          <div className="mt-1 flex items-baseline gap-1">
            <span className="tabular text-[24px] font-extrabold">{state.streak.count}</span>
            <span className="text-[10.5px] text-[var(--ink-faint)]">روز پیوسته</span>
          </div>
          <div className="mt-2 flex items-center justify-between text-[10px] text-[var(--ink-faint)]">
            <span>تا کنکور: {examCountdown} روز</span>
            <span className="tabular">{summary.minutesPracticed} دقیقه تمرین</span>
          </div>
        </Card>
      </div>

      <Card className="p-4">
        <div className="flex items-center gap-4">
          <Ring value={Math.round(summary.accuracy * 100)} size={92} stroke={8}>
            <span className="tabular text-[19px] font-extrabold">{Math.round(summary.accuracy * 100)}٪</span>
            <span className="text-[8.5px] text-[var(--ink-faint)]">دقت کل</span>
          </Ring>
          <div className="flex-1 space-y-2">
            <div>
              <div className="mb-1 flex items-center justify-between text-[10.5px]">
                <span className="text-[var(--ink-soft)]">پاسخ مستقل (unaided)</span>
                <span className="tabular font-bold">{Math.round(summary.unaidedAccuracy * 100)}٪</span>
              </div>
              <Progress value={summary.unaidedAccuracy * 100} height={5} color="var(--success)" />
            </div>
            <div>
              <div className="mb-1 flex items-center justify-between text-[10.5px]">
                <span className="text-[var(--ink-soft)]">سهم پاسخ با راهنما</span>
                <span className="tabular font-bold">{Math.round(summary.aidedShare * 100)}٪</span>
              </div>
              <Progress value={summary.aidedShare * 100} height={5} color="var(--warning)" />
            </div>
            <div className="text-[10px] text-[var(--ink-faint)]">
              BKT کالیبره، پاسخ با راهنما را شاهد ضعیف‌تری می‌داند تا تسلط واقعی مخدوش نشود.
            </div>
          </div>
        </div>
      </Card>

      <Card className="p-4">
        <div className="mb-2 flex items-center justify-between">
          <div className="flex items-center gap-1.5 text-[12px] font-bold">
            <Gauge size={14} className="text-[var(--mimo-button)]" /> کنترلر باند جریان ۷۰–۸۵٪
          </div>
          <Chip
            tone={flow.band === "in_band" ? "success" : flow.band === "too_hard" ? "warning" : flow.band === "too_easy" ? "purple" : "neutral"}
          >
            {flow.labelFa}
          </Chip>
        </div>
        <div className="relative h-3 overflow-hidden rounded-full bg-[var(--surface-2)]">
          <div className="absolute inset-y-0 bg-[var(--success-soft)]" style={{ left: "70%", right: "15%" }} />
          <div
            className="absolute top-1/2 h-4 w-4 -translate-x-1/2 -translate-y-1/2 rounded-full border-2 border-[var(--surface)] bg-[var(--mimo-button)] transition-all"
            style={{ left: `${Math.round(summary.accuracy * 100)}%` }}
          />
        </div>
        <div className="mt-1 flex justify-between text-[9px] text-[var(--ink-faint)]">
          <span>۰٪</span>
          <span>۷۰٪</span>
          <span>۸۵٪</span>
          <span>۱۰۰٪</span>
        </div>
        <p className="mt-2 text-[11px] leading-5 text-[var(--ink-soft)]">{flow.recommendationFa}</p>
      </Card>

      {nextLesson && (
        <Card className="relative overflow-hidden p-4">
          <div className="mimo-dot-grid pointer-events-none absolute inset-0 opacity-50" />
          <div className="relative">
            <div className="flex items-center gap-1.5 text-[10.5px] font-bold text-[var(--mimo-button)]">
              <Target size={12} /> قدم بعدی بر اساس KST Outer Fringe
            </div>
            <h3 className="mt-1 text-[14px] font-extrabold">{nextLesson.lesson.titleFa}</h3>
            <p className="mt-1 text-[11px] leading-5 text-[var(--ink-soft)]">{next.reasonFa}</p>
            <div className="mt-2 flex flex-wrap gap-1.5">
              <Chip tone="purple">{nextLesson.skill.labelFa}</Chip>
              <Chip tone="neutral">{MASTERY_BAND_FA[masteryBand(mastery[nextLesson.skill.id] ?? 0)]}</Chip>
              <Chip tone="neutral">{fringe.length} مهارت در حاشیهٔ بیرونی</Chip>
            </div>
            <Button
              className="mt-3"
              full
              disabled={nextLesson.lock === "locked"}
              onClick={() => onStartLesson(nextLesson.lesson.id)}
            >
              <Play size={14} />
              {nextLesson.lock === "locked" ? "پیش‌نیاز هنوز قفل است" : "شروع این درس"}
            </Button>
          </div>
        </Card>
      )}

      <div>
        <SectionTitle eyebrow="نقشهٔ تسلط" title="وضعیت فصل‌ها" />
        <div className="space-y-2">
          {chapterStats.map(({ chapter, value, subject, completed, total }) => (
            <Card key={chapter.id} className="p-3">
              <div className="flex items-center justify-between gap-2">
                <div className="min-w-0">
                  <div className="truncate text-[12px] font-bold">{chapter.titleFa}</div>
                  <div className="text-[10px] text-[var(--ink-faint)]">
                    {subject.shortFa} · {completed}/{total} درس
                  </div>
                </div>
                <span className="tabular text-[11px] font-extrabold" style={{ color: subject.accent }}>
                  {Math.round(value * 100)}٪
                </span>
              </div>
              <Progress className="mt-2" value={value * 100} height={5} color={subject.accent} />
            </Card>
          ))}
        </div>
      </div>

      <Card className="p-4">
        <div className="mb-2 flex items-center justify-between">
          <div className="flex items-center gap-1.5 text-[12px] font-bold">
            <Activity size={14} className="text-[var(--mimo-button)]" /> فعالیت ۱۴ روز گذشته
          </div>
          <span className="tabular text-[10.5px] text-[var(--ink-faint)]">{state.attempts.length} تلاش</span>
        </div>
        <Sparkline values={dailyActivity} />
        <div className="mt-1 flex justify-between text-[8.5px] text-[var(--ink-faint)]">
          <span>۱۴ روز پیش</span>
          <span>امروز</span>
        </div>
      </Card>

      <div>
        <SectionTitle eyebrow="امتیازها" title="پاداش‌ها و کارنامه" />
        <div className="grid grid-cols-3 gap-2">
          <Card className="p-3 text-center">
            <Trophy size={17} className="mx-auto mb-1 text-[var(--warning)]" />
            <div className="tabular text-[16px] font-extrabold">{state.wallet.xp}</div>
            <div className="text-[9px] text-[var(--ink-faint)]">XP</div>
          </Card>
          <Card className="p-3 text-center">
            <Sparkles size={17} className="mx-auto mb-1 text-[#C79A22]" />
            <div className="tabular text-[16px] font-extrabold">{state.wallet.coins}</div>
            <div className="text-[9px] text-[var(--ink-faint)]">سکه</div>
          </Card>
          <Card className="p-3 text-center">
            <TrendingUp size={17} className="mx-auto mb-1 text-[var(--success)]" />
            <div className="tabular text-[16px] font-extrabold">{state.examResults.length}</div>
            <div className="text-[9px] text-[var(--ink-faint)]">آزمون</div>
          </Card>
        </div>

        {state.examResults.length > 0 ? (
          <div className="mt-2 space-y-1.5">
            {state.examResults.slice(0, 5).map((result) => (
              <Card key={result.id} className="flex items-center gap-2 p-2.5">
                <BarChart3 size={14} className="text-[var(--ink-faint)]" />
                <div className="min-w-0 flex-1">
                  <div className="truncate text-[11.5px] font-bold">{result.titleFa}</div>
                  <div className="text-[9.5px] text-[var(--ink-faint)]">
                    {result.correct} درست · {result.wrong} غلط · {result.blank} نزده
                  </div>
                </div>
                <Chip tone={result.percent >= 70 ? "success" : result.percent >= 40 ? "warning" : "danger"}>
                  {result.percent}٪
                </Chip>
              </Card>
            ))}
          </div>
        ) : (
          <Card className="mt-2 p-3 text-center text-[11px] text-[var(--ink-faint)]">
            هنوز آزمونی ثبت نشده است.
          </Card>
        )}
      </div>

      <Card className="flex items-start gap-2 p-3 text-[10.5px] leading-5 text-[var(--ink-soft)]">
        <Lightbulb size={14} className="mt-0.5 shrink-0 text-[var(--warning)]" />
        هر پاسخ در یک لاگ افزودنی (append-only) ذخیره می‌شود؛ هیچ رکوردی پس از آپلود حذف نمی‌شود
        (تصمیم‌های <span className="font-mono-code">ADD-03</span> و <span className="font-mono-code">ADD-04</span>).
      </Card>
    </div>
  );
}
