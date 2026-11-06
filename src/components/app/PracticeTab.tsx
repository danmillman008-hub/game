"use client";

import { useEffect, useMemo, useRef, useState } from "react";
import {
  AlertTriangle,
  ArrowLeft,
  BarChart3,
  Brain,
  CalendarClock,
  Check,
  ChevronLeft,
  CircleX,
  Clock,
  Flag,
  Layers,
  ListChecks,
  RotateCcw,
  Target,
  Timer,
  Trophy,
  X,
  Zap,
} from "lucide-react";
import { chaptersOfSubject, lessonsOfChapter } from "@/core/content";
import {
  EXAM_MODES,
  buildExam,
  formatClock,
  scoreExam,
  type ExamModeId,
  type ExamResult,
  type ExamSession,
} from "@/core/exam/exam";
import { DAY_MS, forecast, retrievability } from "@/core/algorithms/fsrs";
import type { Rating } from "@/core/algorithms/fsrs";
import { flowStatus } from "@/core/algorithms/flow";
import { recentAccuracy, summarize } from "@/core/state/learner";
import type { MCQ, SubjectId } from "@/core/types";
import { useLearner } from "@/state/LearnerProvider";
import { Button, Card, Chip, EmptyState, Modal, Progress, Ring, SectionTitle, cx } from "@/components/ui/kit";

const MODE_ICONS: Record<ExamModeId, React.ReactNode> = {
  diagnostic: <Target size={17} />,
  chapter: <Layers size={17} />,
  targeted: <Zap size={17} />,
  timed: <Timer size={17} />,
  mistakes: <RotateCcw size={17} />,
  bank: <ListChecks size={17} />,
  mock: <Trophy size={17} />,
};

export function PracticeTab() {
  const [section, setSection] = useState<"exam" | "review">("exam");
  const { state } = useLearner();
  const pending = state.reviewCards.filter((card) => card.due <= Date.now()).length;

  return (
    <div className="space-y-4">
      <div className="grid grid-cols-2 gap-1 rounded-2xl bg-[var(--surface-2)] p-1">
        <button
          onClick={() => setSection("exam")}
          className={cx(
            "rounded-xl py-2 text-[12.5px] font-bold transition",
            section === "exam" ? "bg-[var(--surface)] text-[var(--mimo-button)] shadow-sm" : "text-[var(--ink-soft)]",
          )}
        >
          هاب آزمون
        </button>
        <button
          onClick={() => setSection("review")}
          className={cx(
            "flex items-center justify-center gap-1.5 rounded-xl py-2 text-[12.5px] font-bold transition",
            section === "review" ? "bg-[var(--surface)] text-[var(--mimo-button)] shadow-sm" : "text-[var(--ink-soft)]",
          )}
        >
          صف مرور FSRS
          {pending > 0 && (
            <span className="rounded-full bg-[var(--danger)] px-1.5 text-[10px] font-bold text-white">{pending}</span>
          )}
        </button>
      </div>

      {section === "exam" ? <ExamHub /> : <ReviewQueue />}
    </div>
  );
}

function ExamHub() {
  const { state, curriculum, actions } = useLearner();
  const [modeId, setModeId] = useState<ExamModeId>("chapter");
  const [subjectId, setSubjectId] = useState<SubjectId>("bio12");
  const [chapterId, setChapterId] = useState("BIO12-C1");
  const [session, setSession] = useState<ExamSession | null>(null);
  const [result, setResult] = useState<ExamResult | null>(null);
  const mode = EXAM_MODES.find((item) => item.id === modeId)!;
  const chapters = chaptersOfSubject(subjectId);
  const chapterQuestions = curriculum.questions.filter((q) => q.chapterId === chapterId);
  const mistakeIds = state.reviewCards.map((card) => card.questionId).filter(Boolean) as string[];

  const pickSubject = (id: SubjectId) => {
    setSubjectId(id);
    setChapterId(chaptersOfSubject(id)[0]?.id ?? "");
  };

  const start = () => {
    const built = buildExam(curriculum.questions as MCQ[], {
      mode: modeId,
      subjectId: modeId === "mock" || modeId === "targeted" ? undefined : subjectId,
      chapterId: modeId === "chapter" ? chapterId : undefined,
      weakSkillIds: modeId === "targeted" ? state.reviewCards.map((c) => c.skillId) : undefined,
      mistakeQuestionIds: modeId === "mistakes" ? mistakeIds : undefined,
    });
    setSession(built);
    setResult(null);
  };

  const finish = (current: ExamSession) => {
    const scored = scoreExam(current, curriculum.questions as MCQ[], Date.now());
    actions.finishExam(current, scored);
    setSession(current);
    setResult(scored);
  };

  if (session && !result) {
    return (
      <ExamRunner
        session={session}
        bank={curriculum.questions as MCQ[]}
        onQuit={() => setSession(null)}
        onFinish={finish}
      />
    );
  }

  if (result) {
    return (
      <ExamResultView
        session={session!}
        result={result}
        bank={curriculum.questions as MCQ[]}
        onDone={() => {
          setSession(null);
          setResult(null);
        }}
      />
    );
  }

  const questionCount =
    modeId === "chapter"
      ? chapterQuestions.length
      : modeId === "mistakes"
        ? Math.max(mistakeIds.length, 4)
        : modeId === "mock"
          ? 30
          : Math.min(mode.count, curriculum.questions.length);

  return (
    <div className="space-y-4">
      <Card className="p-4">
        <div className="flex items-start justify-between">
          <div>
            <div className="text-[10.5px] font-bold text-[var(--mimo-button)]">هاب ۷ بخشی آزمون کنکور</div>
            <h2 className="text-[15px] font-extrabold">آزمون و تمرین تطبیقی</h2>
            <p className="mt-1 text-[11.5px] leading-5 text-[var(--ink-soft)]">
              نمرهٔ منفی یک‌سوم، پاسخ‌برگ مستقل از پاسخنامهٔ تشریحی، و زمان‌سنج واقعی جلسهٔ آزمون.
            </p>
          </div>
          <Ring value={Math.round(summarize(state, curriculum).accuracy * 100)} size={62} stroke={6}>
            <span className="tabular text-[13px] font-extrabold">
              {Math.round(summarize(state, curriculum).accuracy * 100)}٪
            </span>
            <span className="text-[8px] text-[var(--ink-faint)]">دقت کل</span>
          </Ring>
        </div>
      </Card>

      <div className="grid grid-cols-2 gap-2">
        {EXAM_MODES.map((item) => (
          <button
            key={item.id}
            onClick={() => setModeId(item.id)}
            className={cx(
              "rounded-2xl border p-3 text-right transition",
              item.id === modeId
                ? "border-[var(--mimo-progress)] bg-[var(--mimo-soft)]"
                : "border-[var(--line)] bg-[var(--surface)] hover:border-[var(--mimo-progress)]/40",
            )}
          >
            <div
              className={cx(
                "mb-2 inline-flex rounded-xl p-1.5",
                item.id === modeId
                  ? "bg-[var(--mimo-button)] text-white"
                  : "bg-[var(--surface-2)] text-[var(--ink-soft)]",
              )}
            >
              {MODE_ICONS[item.id]}
            </div>
            <div className="text-[12.5px] font-extrabold">{item.titleFa}</div>
            <div className="mt-0.5 text-[10px] text-[var(--ink-faint)]">{item.subtitleFa}</div>
          </button>
        ))}
      </div>

      <Card className="space-y-3 p-4">
        <p className="text-[11.5px] leading-5 text-[var(--ink-soft)]">{mode.descriptionFa}</p>

        {mode.id !== "targeted" && mode.id !== "mistakes" && mode.id !== "mock" && (
          <div className="grid grid-cols-2 gap-2">
            <label className="block">
              <span className="mb-1 block text-[10.5px] font-bold text-[var(--ink-faint)]">درس</span>
              <select
                value={subjectId}
                onChange={(event) => pickSubject(event.target.value as SubjectId)}
                className="w-full rounded-xl border border-[var(--line)] bg-[var(--surface-2)] px-2.5 py-2 text-[12px]"
              >
                {curriculum.subjects.map((subject) => (
                  <option key={subject.id} value={subject.id}>
                    {subject.titleFa}
                  </option>
                ))}
              </select>
            </label>
            <label className="block">
              <span className="mb-1 block text-[10.5px] font-bold text-[var(--ink-faint)]">فصل</span>
              <select
                value={chapterId}
                onChange={(event) => setChapterId(event.target.value)}
                className="w-full rounded-xl border border-[var(--line)] bg-[var(--surface-2)] px-2.5 py-2 text-[12px]"
              >
                {chapters.map((chapter) => (
                  <option key={chapter.id} value={chapter.id}>
                    {chapter.titleFa}
                  </option>
                ))}
              </select>
            </label>
          </div>
        )}

        <div className="flex flex-wrap gap-1.5">
          <Chip tone="purple" icon={<ListChecks size={11} />}>
            {questionCount} سؤال
          </Chip>
          <Chip tone="neutral" icon={<Clock size={11} />}>
            {mode.minutes === 0 ? "بدون تایمر" : `${mode.minutes} دقیقه`}
          </Chip>
          <Chip tone={mode.negativeMarking ? "danger" : "success"} icon={<AlertTriangle size={11} />}>
            {mode.negativeMarking ? "نمرهٔ منفی ⅓" : "بدون نمرهٔ منفی"}
          </Chip>
          {mode.id === "mistakes" && (
            <Chip tone="warning">{mistakeIds.length} اشتباه ثبت‌شده</Chip>
          )}
        </div>

        <Button full onClick={start} disabled={questionCount === 0}>
          <ArrowLeft size={16} /> شروع {mode.titleFa}
        </Button>
      </Card>

      {state.examResults.length > 0 && (
        <div>
          <SectionTitle eyebrow="تاریخچه" title="آزمون‌های اخیر" />
          <div className="space-y-2">
            {state.examResults.slice(0, 4).map((item) => (
              <Card key={item.id} className="flex items-center gap-3 p-3">
                <Ring value={item.percent} size={46} stroke={5}>
                  <span className="tabular text-[10px] font-extrabold">{item.percent}٪</span>
                </Ring>
                <div className="min-w-0 flex-1">
                  <div className="truncate text-[12px] font-bold">{item.titleFa}</div>
                  <div className="text-[10px] text-[var(--ink-faint)]">
                    {item.correct} درست · {item.wrong} غلط · {item.blank} نزده
                  </div>
                </div>
                <Chip tone={item.percent >= 70 ? "success" : item.percent >= 40 ? "warning" : "danger"}>
                  {item.score}/{item.maxScore}
                </Chip>
              </Card>
            ))}
          </div>
        </div>
      )}
    </div>
  );
}

function ExamRunner({
  session,
  bank,
  onFinish,
  onQuit,
}: {
  session: ExamSession;
  bank: MCQ[];
  onFinish: (session: ExamSession) => void;
  onQuit: () => void;
}) {
  const [current, setCurrent] = useState(0);
  const [answers, setAnswers] = useState<Record<string, number | null>>(session.answers);
  const [flagged, setFlagged] = useState<string[]>([]);
  const [confirmEnd, setConfirmEnd] = useState(false);
  const [remaining, setRemaining] = useState(session.minutes * 60);
  const byId = useMemo(() => new Map(bank.map((q) => [q.id, q])), [bank]);
  const answersRef = useRef(answers);
  const flaggedRef = useRef(flagged);
  const finishRef = useRef(onFinish);

  useEffect(() => {
    answersRef.current = answers;
    flaggedRef.current = flagged;
    finishRef.current = onFinish;
  }, [answers, flagged, onFinish]);
  const item = session.items[current];
  const question = byId.get(item.questionId);

  const activeSession = useMemo<ExamSession>(
    () => ({ ...session, answers, flagged }),
    [session, answers, flagged],
  );

  useEffect(() => {
    if (session.minutes === 0) return;
    const timer = window.setInterval(() => {
      setRemaining((value) => {
        if (value <= 1) {
          window.clearInterval(timer);
          finishRef.current({
            ...session,
            answers: answersRef.current,
            flagged: flaggedRef.current,
            finishedAt: Date.now(),
          });
          return 0;
        }
        return value - 1;
      });
    }, 1000);
    return () => window.clearInterval(timer);
  }, [session]);

  const answeredCount = Object.values(answers).filter((value) => value !== null).length;

  return (
    <div className="space-y-3">
      <Card className="flex items-center justify-between gap-2 p-3">
        <button onClick={() => setConfirmEnd(true)} className="rounded-xl bg-[var(--surface-2)] p-2 text-[var(--ink-soft)]">
          <X size={16} />
        </button>
        <div className="text-center">
          <div className="text-[11.5px] font-bold">{session.titleFa}</div>
          <div className="text-[10px] text-[var(--ink-faint)]">
            {answeredCount} از {session.items.length} پاسخ داده شده
          </div>
        </div>
        {session.minutes > 0 ? (
          <div
            className={cx(
              "tabular rounded-xl px-2.5 py-1.5 text-[12px] font-extrabold",
              remaining < 60
                ? "bg-[var(--danger-soft)] text-[var(--danger)]"
                : "bg-[var(--mimo-soft)] text-[var(--mimo-button)]",
            )}
          >
            {formatClock(remaining)}
          </div>
        ) : (
          <Chip tone="neutral">حالت مطالعه</Chip>
        )}
      </Card>

      <Progress value={(answeredCount / session.items.length) * 100} height={5} />

      <Card className="p-4">
        <div className="mb-2 flex items-center justify-between">
          <Chip tone="purple">
            سؤال {current + 1} از {session.items.length}
          </Chip>
          <button
            onClick={() =>
              setFlagged((prev) => (prev.includes(item.questionId) ? prev.filter((id) => id !== item.questionId) : [...prev, item.questionId]))
            }
            className={cx(
              "flex items-center gap-1 rounded-full px-2 py-1 text-[10.5px] font-bold",
              flagged.includes(item.questionId)
                ? "bg-[var(--warning-soft)] text-[var(--warning)]"
                : "bg-[var(--surface-2)] text-[var(--ink-faint)]",
            )}
          >
            <Flag size={11} /> علامت
          </button>
        </div>
        <p className="text-[13.5px] font-semibold leading-7">{question?.stemFa}</p>

        <div className="mt-3 space-y-2">
          {question?.options.map((option, index) => {
            const selected = answers[item.questionId] === index;
            return (
              <button
                key={option.id}
                onClick={() => setAnswers((prev) => ({ ...prev, [item.questionId]: selected ? null : index }))}
                className={cx(
                  "flex w-full items-start gap-2.5 rounded-2xl border p-3 text-right text-[12.5px] leading-6 transition",
                  selected
                    ? "border-[var(--mimo-progress)] bg-[var(--mimo-soft)]"
                    : "border-[var(--line)] bg-[var(--surface)] hover:border-[var(--mimo-progress)]/40",
                )}
              >
                <span className="mt-0.5 flex h-5 w-5 shrink-0 items-center justify-center rounded-full bg-[var(--surface-2)] text-[10px] font-bold">
                  {["الف", "ب", "ج", "د"][index]}
                </span>
                {option.textFa}
              </button>
            );
          })}
        </div>
      </Card>

      <div className="flex items-center gap-2">
        <Button variant="outline" disabled={current === 0} onClick={() => setCurrent((value) => value - 1)}>
          <ChevronLeft size={15} className="rotate-180" /> قبلی
        </Button>
        {current === session.items.length - 1 ? (
          <Button full onClick={() => setConfirmEnd(true)}>
            <Check size={16} /> پایان و تصحیح
          </Button>
        ) : (
          <Button full onClick={() => setCurrent((value) => value + 1)}>
            بعدی <ChevronLeft size={15} />
          </Button>
        )}
      </div>

      <Button variant="outline" full onClick={() => setConfirmEnd(true)}>
        <Check size={15} /> پایان آزمون و تصحیح
      </Button>

      <Card className="p-3">
        <div className="mb-2 text-[10.5px] font-bold text-[var(--ink-faint)]">پاسخ‌برگ</div>
        <div className="grid grid-cols-10 gap-1">
          {session.items.map((entry, index) => {
            const isAnswered = answers[entry.questionId] !== null;
            const isFlagged = flagged.includes(entry.questionId);
            return (
              <button
                key={entry.questionId}
                onClick={() => setCurrent(index)}
                className={cx(
                  "tabular aspect-square rounded-lg text-[10px] font-bold transition",
                  index === current
                    ? "bg-[var(--mimo-button)] text-white"
                    : isFlagged
                      ? "bg-[var(--warning-soft)] text-[var(--warning)]"
                      : isAnswered
                        ? "bg-[var(--success-soft)] text-[var(--success)]"
                        : "bg-[var(--surface-2)] text-[var(--ink-faint)]",
                )}
              >
                {index + 1}
              </button>
            );
          })}
        </div>
      </Card>

      <Modal
        open={confirmEnd}
        onClose={() => setConfirmEnd(false)}
        title="پایان آزمون؟"
        subtitle={`${answeredCount} پاسخ ثبت شده و ${session.items.length - answeredCount} سؤال بی‌پاسخ است.`}
        footer={
          <div className="flex gap-2">
            <Button variant="outline" onClick={() => setConfirmEnd(false)}>
              ادامهٔ آزمون
            </Button>
            <Button
              full
              onClick={() => {
                setConfirmEnd(false);
                onFinish({ ...activeSession, finishedAt: Date.now() });
              }}
            >
              تصحیح و مشاهدهٔ کارنامه
            </Button>
          </div>
        }
      >
        <div className="space-y-2 text-[12px] leading-6 text-[var(--ink-soft)]">
          <p>پس از تصحیح، پاسخ‌برگ و پاسخنامهٔ تشریحی جدا نمایش داده می‌شوند (F39–F43).</p>
          <p>همهٔ سؤالات اشتباه به‌صورت خودکار در صف مرور FSRS-5 زمان‌بندی می‌شوند.</p>
          <button
            onClick={() => {
              setConfirmEnd(false);
              onQuit();
            }}
            className="text-[11px] font-bold text-[var(--danger)]"
          >
            خروج بدون ذخیره
          </button>
        </div>
      </Modal>
    </div>
  );
}

function ExamResultView({
  session,
  result,
  bank,
  onDone,
}: {
  session: ExamSession;
  result: ExamResult;
  bank: MCQ[];
  onDone: () => void;
}) {
  const [tab, setTab] = useState<"sheet" | "key">("sheet");
  const byId = useMemo(() => new Map(bank.map((q) => [q.id, q])), [bank]);

  return (
    <div className="space-y-4">
      <Card className="p-4 text-center">
        <div className="mx-auto mb-2 w-fit">
          <Ring value={result.percent} size={104} stroke={9}>
            <span className="tabular text-[24px] font-extrabold">{result.percent}٪</span>
            <span className="text-[9px] text-[var(--ink-faint)]">درصد</span>
          </Ring>
        </div>
        <h2 className="text-[15px] font-extrabold">{result.titleFa}</h2>
        <p className="mt-1 text-[11px] text-[var(--ink-faint)]">
          {result.negativeMarking ? "نمرهٔ منفی یک‌سوم اعمال شد" : "بدون نمرهٔ منفی"} · {result.minutesSpent} دقیقه
        </p>
        <div className="mt-3 grid grid-cols-4 gap-1.5 text-center">
          <div className="rounded-xl bg-[var(--success-soft)] p-2">
            <div className="tabular text-[15px] font-extrabold text-[var(--success)]">{result.correct}</div>
            <div className="text-[9px] text-[var(--ink-faint)]">درست</div>
          </div>
          <div className="rounded-xl bg-[var(--danger-soft)] p-2">
            <div className="tabular text-[15px] font-extrabold text-[var(--danger)]">{result.wrong}</div>
            <div className="text-[9px] text-[var(--ink-faint)]">غلط</div>
          </div>
          <div className="rounded-xl bg-[var(--surface-2)] p-2">
            <div className="tabular text-[15px] font-extrabold">{result.blank}</div>
            <div className="text-[9px] text-[var(--ink-faint)]">نزده</div>
          </div>
          <div className="rounded-xl bg-[var(--mimo-soft)] p-2">
            <div className="tabular text-[15px] font-extrabold text-[var(--mimo-button)]">
              {result.score}/{result.maxScore}
            </div>
            <div className="text-[9px] text-[var(--ink-faint)]">نمره</div>
          </div>
        </div>
      </Card>

      {Object.keys(result.perSubject).length > 1 && (
        <Card className="p-3">
          <div className="mb-2 text-[11px] font-bold text-[var(--ink-soft)]">تفکیک دروس</div>
          <div className="space-y-1.5">
            {Object.entries(result.perSubject).map(([subject, bucket]) => {
              if (!bucket) return null;
              const percent = Math.round(((bucket.correct - (result.negativeMarking ? bucket.wrong / 3 : 0)) / bucket.total) * 100);
              return (
                <div key={subject} className="flex items-center gap-2">
                  <span className="w-16 text-[10.5px] text-[var(--ink-faint)]">{subject}</span>
                  <div className="flex-1">
                    <Progress value={Math.max(0, percent)} height={5} />
                  </div>
                  <span className="tabular w-9 text-left text-[10px] font-bold">{percent}٪</span>
                </div>
              );
            })}
          </div>
        </Card>
      )}

      <div className="grid grid-cols-2 gap-1 rounded-2xl bg-[var(--surface-2)] p-1">
        <button
          onClick={() => setTab("sheet")}
          className={cx(
            "rounded-xl py-2 text-[12px] font-bold",
            tab === "sheet" ? "bg-[var(--surface)] text-[var(--mimo-button)] shadow-sm" : "text-[var(--ink-soft)]",
          )}
        >
          پاسخ‌برگ
        </button>
        <button
          onClick={() => setTab("key")}
          className={cx(
            "rounded-xl py-2 text-[12px] font-bold",
            tab === "key" ? "bg-[var(--surface)] text-[var(--mimo-button)] shadow-sm" : "text-[var(--ink-soft)]",
          )}
        >
          پاسخنامهٔ تشریحی
        </button>
      </div>

      {tab === "sheet" ? (
        <Card className="p-3">
          <div className="grid grid-cols-8 gap-1.5">
            {session.items.map((item, index) => {
              const chosen = session.answers[item.questionId];
              const question = byId.get(item.questionId);
              const correct = chosen !== null && chosen !== undefined && Boolean(question?.options[chosen]?.correct);
              return (
                <div
                  key={item.questionId}
                  className={cx(
                    "tabular flex aspect-square items-center justify-center rounded-lg text-[10.5px] font-bold",
                    chosen === null || chosen === undefined
                      ? "bg-[var(--surface-2)] text-[var(--ink-faint)]"
                      : correct
                        ? "bg-[var(--success-soft)] text-[var(--success)]"
                        : "bg-[var(--danger-soft)] text-[var(--danger)]",
                  )}
                >
                  {index + 1}
                </div>
              );
            })}
          </div>
          <div className="mt-3 flex justify-center gap-3 text-[9.5px] text-[var(--ink-faint)]">
            <span className="flex items-center gap-1"><span className="h-2 w-2 rounded-full bg-[var(--success)]" /> درست</span>
            <span className="flex items-center gap-1"><span className="h-2 w-2 rounded-full bg-[var(--danger)]" /> غلط</span>
            <span className="flex items-center gap-1"><span className="h-2 w-2 rounded-full bg-[var(--surface-3)]" /> نزده</span>
          </div>
        </Card>
      ) : (
        <div className="space-y-2">
          {session.items.map((item, index) => {
            const question = byId.get(item.questionId);
            if (!question) return null;
            const chosen = session.answers[item.questionId];
            return (
              <Card key={item.questionId} className="p-3">
                <div className="mb-1.5 flex items-center gap-2 text-[10px] text-[var(--ink-faint)]">
                  <span className="rounded-full bg-[var(--surface-2)] px-1.5 py-0.5 font-bold">سؤال {index + 1}</span>
                  <span className="font-mono-code">{question.id}</span>
                </div>
                <p className="text-[12px] font-semibold leading-6">{question.stemFa}</p>
                <div className="mt-2 space-y-1">
                  {question.options.map((option, optionIndex) => {
                    const isChosen = chosen === optionIndex;
                    return (
                      <div
                        key={option.id}
                        className={cx(
                          "rounded-lg px-2 py-1.5 text-[11px] leading-5",
                          option.correct
                            ? "bg-[var(--success-soft)] text-[var(--success)]"
                            : isChosen
                              ? "bg-[var(--danger-soft)] text-[var(--danger)]"
                              : "bg-[var(--surface-2)] text-[var(--ink-soft)]",
                        )}
                      >
                        <span className="font-bold">{["الف", "ب", "ج", "د"][optionIndex]}) </span>
                        {option.textFa}
                        <div className="mt-0.5 text-[10px] opacity-80">{option.analysisFa}</div>
                      </div>
                    );
                  })}
                </div>
              </Card>
            );
          })}
        </div>
      )}

      <Button full onClick={onDone}>
        <Check size={16} /> پایان و بازگشت به هاب آزمون
      </Button>
      <Card className="flex items-start gap-2 p-3 text-[11px] leading-5 text-[var(--ink-soft)]">
        <CalendarClock size={14} className="mt-0.5 shrink-0 text-[var(--mimo-button)]" />
        {result.wrong} سؤال اشتباه به صف مرور FSRS-5 اضافه شد؛ فردا در بخش «صف مرور» می‌بینی.
      </Card>
    </div>
  );
}

function ReviewQueue() {
  const { state, curriculum, actions } = useLearner();
  const [reviewing, setReviewing] = useState(false);
  const [cardIndex, setCardIndex] = useState(0);
  const [revealed, setRevealed] = useState(false);
  const [earlyBird, setEarlyBird] = useState(false);
  const [sessionIds, setSessionIds] = useState<string[]>([]);
  const now = Date.now();
  const due = state.reviewCards.filter((card) => card.due <= now);
  const queue = earlyBird ? state.reviewCards : due;
  const reviewQueue = sessionIds
    .map((id) => state.reviewCards.find((entry) => entry.id === id))
    .filter((entry): entry is (typeof state.reviewCards)[number] => Boolean(entry));
  const buckets = forecast(state.reviewCards, now);
  const maxBucket = Math.max(1, ...buckets.map((bucket) => bucket.count));
  const stats = summarize(state, curriculum, now);

  const card = reviewQueue[cardIndex];
  const lesson = card ? curriculum.lessonById.get(card.lessonId) : null;

  const rate = (rating: Rating) => {
    if (!card) return;
    actions.reviewCard(card.id, rating);
    if (cardIndex + 1 >= reviewQueue.length) {
      setReviewing(false);
      setCardIndex(0);
      setRevealed(false);
    } else {
      setCardIndex(cardIndex + 1);
      setRevealed(false);
    }
  };

  if (reviewing && card) {
    const retention = Math.round(retrievability(card, now) * 100);
    return (
      <div className="space-y-3">
        <div className="flex items-center justify-between">
          <Chip tone="purple">
            کارت {cardIndex + 1} از {reviewQueue.length}
          </Chip>
          <button onClick={() => setReviewing(false)} className="text-[11px] font-bold text-[var(--ink-faint)]">
            خروج
          </button>
        </div>
        <Progress value={(cardIndex / Math.max(1, reviewQueue.length)) * 100} height={5} />

        <Card className="p-5">
          <div className="mb-2 flex items-center gap-1.5 text-[10px] text-[var(--ink-faint)]">
            <Brain size={11} /> {lesson?.titleFa ?? card.lessonId}
          </div>
          <p className="text-[13.5px] font-semibold leading-7">{card.promptFa}</p>

          {revealed ? (
            <div className="animate-rise mt-4 rounded-2xl bg-[var(--success-soft)] p-3">
              <div className="text-[10px] font-bold text-[var(--success)]">پاسخ کتاب</div>
              <div className="mt-1 text-[12.5px] leading-6 text-[var(--ink)]">{card.answerFa}</div>
            </div>
          ) : (
            <Button variant="soft" full className="mt-4" onClick={() => setRevealed(true)}>
              نمایش پاسخ
            </Button>
          )}

          <div className="mt-3 flex items-center justify-between text-[10px] text-[var(--ink-faint)]">
            <span>قابلیت یادآوری: {retention}٪</span>
            <span className="tabular">S={card.stability.toFixed(1)} · D={card.difficulty.toFixed(1)}</span>
          </div>
        </Card>

        {revealed && (
          <div className="grid grid-cols-4 gap-1.5">
            {[
              { rating: 1 as Rating, label: "دوباره", tone: "danger" as const },
              { rating: 2 as Rating, label: "سخت", tone: "warning" as const },
              { rating: 3 as Rating, label: "خوب", tone: "success" as const },
              { rating: 4 as Rating, label: "آسان", tone: "purple" as const },
            ].map((option) => (
              <button
                key={option.rating}
                onClick={() => rate(option.rating)}
                className={cx(
                  "rounded-xl px-1 py-2.5 text-[11px] font-bold transition active:scale-95",
                  option.tone === "danger"
                    ? "bg-[var(--danger-soft)] text-[var(--danger)]"
                    : option.tone === "warning"
                      ? "bg-[var(--warning-soft)] text-[var(--warning)]"
                      : option.tone === "success"
                        ? "bg-[var(--success-soft)] text-[var(--success)]"
                        : "bg-[var(--mimo-soft)] text-[var(--mimo-button)]",
                )}
              >
                {option.label}
              </button>
            ))}
          </div>
        )}
      </div>
    );
  }

  return (
    <div className="space-y-4">
      <Card className="p-4">
        <div className="flex items-start justify-between gap-3">
          <div>
            <div className="text-[10.5px] font-bold text-[var(--mimo-button)]">زمان‌بندی FSRS-5</div>
            <h2 className="text-[15px] font-extrabold">صف مرور فاصله‌دار</h2>
            <p className="mt-1 text-[11px] leading-5 text-[var(--ink-soft)]">
              هر پاسخ غلط یا همراه با راهنما، یک کارت می‌سازد. هدف: نگه‌داشتن قابلیت یادآوری روی ۹۰٪ تا روز کنکور.
            </p>
          </div>
          <Ring value={Math.min(100, state.reviewCards.length * 4)} size={64} stroke={6}>
            <span className="tabular text-[14px] font-extrabold">{stats.dueReviews}</span>
            <span className="text-[8px] text-[var(--ink-faint)]">سررسید</span>
          </Ring>
        </div>

        <div className="mt-4 flex items-end justify-between gap-1">
          {buckets.map((bucket) => (
            <div key={bucket.dayOffset} className="flex flex-1 flex-col items-center gap-1">
              <div className="flex h-16 w-full items-end">
                <div
                  className="w-full rounded-t-md bg-[var(--mimo-progress)] transition-all"
                  style={{ height: `${Math.max(4, (bucket.count / maxBucket) * 100)}%`, opacity: bucket.count ? 1 : 0.25 }}
                />
              </div>
              <span className="text-[8.5px] text-[var(--ink-faint)]">{bucket.label}</span>
            </div>
          ))}
        </div>

        <div className="mt-3 flex gap-2">
          <Button
            full
            disabled={queue.length === 0}
            onClick={() => {
              setSessionIds(queue.map((entry) => entry.id));
              setReviewing(true);
              setCardIndex(0);
              setRevealed(false);
            }}
          >
            <Brain size={15} /> شروع مرور ({queue.length})
          </Button>
          <Button
            variant="outline"
            onClick={() => {
              setEarlyBird((value) => !value);
            }}
          >
            {earlyBird ? "فقط سررسید" : "مرور زودهنگام"}
          </Button>
        </div>
      </Card>

      {state.reviewCards.length === 0 ? (
        <EmptyState
          icon={<Check size={20} />}
          title="صف مرور خالی است"
          hint="با یک درس یا آزمون شروع کن؛ اشتباه‌ها و پاسخ‌های همراه با راهنما خودکار به این صف می‌آیند."
        />
      ) : (
        <div className="space-y-2">
          <SectionTitle eyebrow="همهٔ کارت‌ها" title="بانک مرور" />
          {queue.length === 0 && <p className="text-[11.5px] text-[var(--ink-faint)]">هیچ کارتی سررسید نشده است؛ «مرور زودهنگام» را روشن کن.</p>}
          {queue.slice(0, 12).map((entry) => {
            const cardLesson = curriculum.lessonById.get(entry.lessonId);
            const days = Math.ceil((entry.due - now) / DAY_MS);
            return (
              <Card key={entry.id} className="flex items-center gap-3 p-3">
                <div
                  className={cx(
                    "flex h-9 w-9 shrink-0 items-center justify-center rounded-xl",
                    entry.due <= now ? "bg-[var(--danger-soft)] text-[var(--danger)]" : "bg-[var(--surface-2)] text-[var(--ink-faint)]",
                  )}
                >
                  <CalendarClock size={15} />
                </div>
                <div className="min-w-0 flex-1">
                  <div className="truncate text-[11.5px] font-bold">{cardLesson?.titleFa ?? entry.lessonId}</div>
                  <div className="truncate text-[10px] text-[var(--ink-faint)]">{entry.promptFa}</div>
                </div>
                <Chip tone={entry.due <= now ? "danger" : "neutral"}>
                  {entry.due <= now ? "سررسید" : `${days} روز`}
                </Chip>
              </Card>
            );
          })}
        </div>
      )}

      <Card className="flex items-start gap-2 p-3 text-[11px] leading-5 text-[var(--ink-soft)]">
        <BarChart3 size={14} className="mt-0.5 shrink-0 text-[var(--mimo-button)]" />
        کنترلر باند جریان:{" "}
        {flowStatus(recentAccuracy(state)).labelFa} — {flowStatus(recentAccuracy(state)).recommendationFa}
      </Card>
    </div>
  );
}
