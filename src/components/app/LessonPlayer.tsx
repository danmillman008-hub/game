"use client";

import { useEffect as useEffectSafe, useMemo, useRef, useState } from "react";
import {
  ArrowLeft,
  Check,
  ChevronLeft,
  CircleX,
  Flame,
  Info,
  Lightbulb,
  Play,
  RotateCcw,
  Sparkles,
  Target,
  X,
} from "lucide-react";
import { gradeAnswer, type GradeResult } from "@/core/text/grade";
import type { Lesson, LessonBlock } from "@/core/types";
import { useLearner } from "@/state/LearnerProvider";
import { Button, Card, Chip, Progress, Stars, cx } from "@/components/ui/kit";

export type BlockOutcome = {
  verdict: "correct" | "partial" | "incorrect" | "seen";
  aided: boolean;
  attempts: number;
  value?: string;
  grade?: GradeResult;
};

const ROLE_FA: Record<LessonBlock["role"], string> = {
  hook: "قلاب",
  check: "سنجش",
  feedback: "دیباگ",
  explain: "چیدمان",
  practice: "تست",
  recap: "مرور",
};

export function LessonPlayer({
  lessonId,
  onClose,
  onNextLesson,
}: {
  lessonId: string;
  onClose: () => void;
  onNextLesson: (lessonId: string) => void;
}) {
  const { curriculum, actions, state } = useLearner();
  const lesson = curriculum.lessonById.get(lessonId);
  const [index, setIndex] = useState(0);
  const [outcomes, setOutcomes] = useState<Record<string, BlockOutcome>>({});
  const [finished, setFinished] = useState(false);
  const [completed, setCompleted] = useState(false);
  const startedAt = useRef(0);

  useEffectSafe(() => {
    if (startedAt.current === 0) startedAt.current = Date.now();
  }, []);

  if (!lesson) return null;
  const block = lesson.blocks[index];
  const outcome = outcomes[block.id];
  const progressPct = ((index + (outcome ? 1 : 0)) / lesson.blocks.length) * 100;

  const gradedCount = lesson.blocks.filter((b) => outcomes[b.id]).length;
  const correctCount = lesson.blocks.filter((b) => {
    const value = outcomes[b.id]?.verdict;
    return value === "correct" || value === "seen";
  }).length;

  const grade = (result: BlockOutcome) => {
    setOutcomes((prev) => ({ ...prev, [block.id]: result }));

    if (block.renderer !== "reveal" && block.mechanic !== "summary_recap") {
      actions.recordAttempt({
        lessonId: lesson.id,
        blockId: block.id,
        skillId: block.skillId,
        correct: result.verdict === "correct" || result.verdict === "partial",
        aided: result.aided,
        verdict: result.grade?.verdict,
        seconds: startedAt.current ? Math.max(4, Math.round((Date.now() - startedAt.current) / 1000)) : 4,
        context: "lesson",
        difficulty: block.mcq?.difficulty ?? 2,
        promptFa:
          block.renderer === "cloze" ? block.cloze?.sentenceFa : block.renderer === "mcq" ? block.mcq?.stemFa : block.promptFa,
        answerFa:
          block.renderer === "cloze"
            ? block.cloze?.answer
            : block.renderer === "mcq"
              ? block.mcq?.options.find((option) => option.correct)?.textFa
              : block.assembly?.answerFa,
      });
    }
  };

  const finish = () => {
    const accuracy = gradedCount === 0 ? 0 : correctCount / lesson.blocks.length;
    actions.completeLesson(lesson.id, accuracy);
    setCompleted(true);
    setFinished(true);
  };

  const next = () => {
    if (index < lesson.blocks.length - 1) {
      setIndex(index + 1);
      return;
    }
    finish();
  };

  const nextLessonId =
    curriculum.lessons
      .filter((item) => item.chapterId === lesson.chapterId)
      .sort((a, b) => a.order - b.order)
      .find((item) => item.order === lesson.order + 1)?.id ?? null;

  const stars = completed
    ? correctCount / lesson.blocks.length >= 0.95
      ? 3
      : correctCount / lesson.blocks.length >= 0.8
        ? 2
        : correctCount / lesson.blocks.length >= 0.6
          ? 1
          : 0
    : 0;

  return (
    <div className="fixed inset-0 z-40 flex justify-center bg-[var(--bg-app)]">
      <div className="flex h-full w-full max-w-[640px] flex-col bg-[var(--bg-app)]">
        <div className="shrink-0 px-4 pt-4">
          <div className="mb-3 flex items-center gap-3">
            <button
              onClick={onClose}
              className="rounded-full bg-[var(--surface-2)] p-2 text-[var(--ink-soft)]"
              aria-label="بستن درس"
            >
              <X size={17} />
            </button>
            <div className="min-w-0 flex-1">
              <div className="truncate text-[13.5px] font-extrabold">{lesson.titleFa}</div>
              <div className="truncate text-[10.5px] text-[var(--ink-faint)]">{lesson.sourceRef}</div>
            </div>
            <span className="tabular rounded-full bg-[var(--surface-2)] px-2.5 py-1 text-[11px] font-bold text-[var(--ink-soft)]">
              {index + 1} / {lesson.blocks.length}
            </span>
          </div>
          <Progress value={progressPct} height={6} />
          <div className="mt-3 flex items-center gap-1.5 overflow-x-auto pb-1 scrollbar-thin">
            {lesson.blocks.map((item, itemIndex) => {
              const done = Boolean(outcomes[item.id]);
              const active = itemIndex === index;
              return (
                <div
                  key={item.id}
                  className={cx(
                    "flex shrink-0 items-center gap-1 rounded-full px-2 py-1 text-[9.5px] font-bold transition",
                    active
                      ? "bg-[var(--mimo-soft)] text-[var(--mimo-button)]"
                      : done
                        ? "bg-[var(--success-soft)] text-[var(--success)]"
                        : "bg-[var(--surface-2)] text-[var(--ink-faint)]",
                  )}
                >
                  {done ? <Check size={9} /> : <span className="h-1 w-1 rounded-full bg-current" />}
                  {ROLE_FA[item.role]}
                </div>
              );
            })}
          </div>
        </div>

        <div className="scrollbar-thin flex-1 overflow-y-auto px-4 py-4">
          <div key={block.id} className="animate-rise space-y-3">
            <div className="flex items-center justify-between gap-2">
              <div>
                <div className="text-[10px] font-bold tracking-wide text-[var(--mimo-button)]">
                  نقش {ROLE_FA[block.role]} · {block.mechanic}
                </div>
                <h2 className="text-[15px] font-extrabold">{block.titleFa}</h2>
              </div>
              <Chip tone="neutral" icon={<Target size={10} />}>
                {block.skillId.endsWith("application") ? "کاربرد" : "مفهوم"}
              </Chip>
            </div>

            <p className="text-[12.5px] leading-6 text-[var(--ink-soft)]">{block.promptFa}</p>

            {block.renderer === "reveal" && (
              <RevealBlock block={block} outcome={outcome} onGrade={grade} />
            )}
            {block.renderer === "cloze" && (
              <ClozeBlock block={block} outcome={outcome} onGrade={grade} />
            )}
            {block.renderer === "assembly" && (
              <AssemblyBlock block={block} outcome={outcome} onGrade={grade} />
            )}
            {block.renderer === "trap" && <TrapBlock block={block} outcome={outcome} onGrade={grade} />}
            {block.renderer === "mcq" && (
              <McqBlock block={block} outcome={outcome} onGrade={grade} />
            )}
          </div>
        </div>

        <div className="shrink-0 border-t border-[var(--line)] bg-[var(--surface)] px-4 py-3">
          {!outcome && block.renderer === "reveal" ? (
            <Button
              full
              onClick={() => {
                grade({ verdict: "seen", aided: false, attempts: 1 });
                next();
              }}
            >
              {index === lesson.blocks.length - 1 ? "پایان درس و ثبت پیشرفت" : "فهمیدم، ادامه بده"}
              <ArrowLeft size={16} />
            </Button>
          ) : outcome ? (
            <div className="flex items-center gap-2">
              {(outcome.verdict === "correct" || outcome.verdict === "partial" || outcome.verdict === "seen") && (
                <div className="flex items-center gap-1 text-[11.5px] font-bold text-[var(--success)]">
                  <Check size={14} /> ثبت شد
                </div>
              )}
              <Button full onClick={next}>
                {index === lesson.blocks.length - 1 ? "پایان درس" : "ادامه"}
                <ArrowLeft size={16} />
              </Button>
            </div>
          ) : (
            <div className="text-center text-[11px] text-[var(--ink-faint)]">
              پاسخ را کامل کن؛ سپس «ادامه» فعال می‌شود.
            </div>
          )}
        </div>
      </div>

      {finished && completed && (
        <Celebration
          lesson={lesson}
          stars={stars}
          correct={correctCount}
          total={lesson.blocks.length}
          nextLessonId={nextLessonId}
          dueCards={state.reviewCards.length}
          onClose={onClose}
          onNext={(id) => {
            setIndex(0);
            setOutcomes({});
            setFinished(false);
            setCompleted(false);
            onNextLesson(id);
          }}
        />
      )}
    </div>
  );
}

function FeedbackBanner({ outcome, block }: { outcome: BlockOutcome; block: LessonBlock }) {
  const good = outcome.verdict === "correct" || outcome.verdict === "seen";
  const partial = outcome.verdict === "partial";
  const message = good
    ? block.feedback.correctFa
    : partial
      ? (block.feedback.partialFa ?? block.feedback.correctFa)
      : block.feedback.wrongFa;

  return (
    <div
      className={cx(
        "flex items-start gap-2 rounded-2xl border p-3 text-[12px] leading-6",
        good
          ? "border-[var(--success)]/30 bg-[var(--success-soft)] text-[var(--success)]"
          : partial
            ? "border-[var(--warning)]/30 bg-[var(--warning-soft)] text-[var(--warning)]"
            : "border-[var(--danger)]/30 bg-[var(--danger-soft)] text-[var(--danger)]",
      )}
    >
      {good ? <Check size={15} className="mt-1 shrink-0" /> : partial ? <Info size={15} className="mt-1 shrink-0" /> : <CircleX size={15} className="mt-1 shrink-0" />}
      <div className="space-y-1">
        <div className="font-bold">{outcome.grade?.messageFa ?? (good ? "درست" : "دوباره تلاش کن")}</div>
        {message && <div className="text-[var(--ink-soft)]">{message}</div>}
      </div>
    </div>
  );
}

function HintToggle({
  hint,
  used,
  onUse,
}: {
  hint?: string;
  used: boolean;
  onUse: () => void;
}) {
  if (!hint) return null;
  return (
    <div>
      {!used ? (
        <button
          onClick={onUse}
          className="inline-flex items-center gap-1.5 rounded-full bg-[var(--warning-soft)] px-3 py-1.5 text-[11px] font-bold text-[var(--warning)]"
        >
          <Lightbulb size={12} /> راهنما (پاسخ با کمک ثبت می‌شود)
        </button>
      ) : (
        <div className="flex items-start gap-2 rounded-xl bg-[var(--warning-soft)] p-2.5 text-[11.5px] leading-5 text-[var(--warning)]">
          <Lightbulb size={13} className="mt-0.5 shrink-0" />
          {hint}
        </div>
      )}
    </div>
  );
}

function RevealBlock({
  block,
  outcome,
  onGrade,
}: {
  block: LessonBlock;
  outcome?: BlockOutcome;
  onGrade: (result: BlockOutcome) => void;
}) {
  const isRecap = block.mechanic === "summary_recap";
  return (
    <div className="space-y-3">
      <div className="space-y-2">
        {block.bodyFa.map((text, index) => (
          <div
            key={index}
            className={cx(
              "rounded-2xl border p-3 text-[12.5px] leading-7",
              index === 0 && !isRecap
                ? "border-[var(--mimo-progress)]/30 bg-[var(--mimo-soft)] text-[var(--ink)]"
                : "border-[var(--line)] bg-[var(--surface)] text-[var(--ink-soft)]",
            )}
          >
            {isRecap && (
              <span className="mr-1.5 inline-flex h-5 w-5 items-center justify-center rounded-full bg-[var(--mimo-soft)] text-[10px] font-bold text-[var(--mimo-button)]">
                {index + 1}
              </span>
            )}
            {text}
          </div>
        ))}
      </div>
      {isRecap && (
        <div className="rounded-2xl bg-[var(--surface-2)] p-3 text-[11px] leading-5 text-[var(--ink-soft)]">
          <div className="mb-1 flex items-center gap-1.5 font-bold text-[var(--mimo-button)]">
            <Sparkles size={12} /> ثبت در LessonProgress و صف FSRS-5
          </div>
          با پایان این درس، کارت‌های مرور زمان‌بندی می‌شوند و تلاش‌ها در لاگ افزودنی ثبت می‌گردند.
        </div>
      )}
      {outcome && <FeedbackBanner outcome={outcome} block={block} />}
    </div>
  );
}

function ClozeBlock({
  block,
  outcome,
  onGrade,
}: {
  block: LessonBlock;
  outcome?: BlockOutcome;
  onGrade: (result: BlockOutcome) => void;
}) {
  const [value, setValue] = useState(outcome?.value ?? "");
  const [aided, setAided] = useState(outcome?.aided ?? false);
  const cloze = block.cloze!;
  const parts = cloze.sentenceFa.split(/_{2,}/);

  const submit = () => {
    if (!value.trim()) return;
    const grade = gradeAnswer(value, cloze.answer);
    onGrade({
      verdict: grade.verdict === "CORRECT" ? "correct" : grade.verdict === "PARTIAL" ? "partial" : "incorrect",
      aided,
      attempts: 1,
      value,
      grade,
    });
  };

  return (
    <div className="space-y-3">
      <Card className="p-4">
        <div className="flex flex-wrap items-center gap-1.5 text-[13.5px] leading-8">
          {parts.map((part, index) => (
            <span key={index} className="contents">
              <span>{part}</span>
              {index < parts.length - 1 && (
                <input
                  value={value}
                  disabled={Boolean(outcome)}
                  onChange={(event) => setValue(event.target.value)}
                  onKeyDown={(event) => event.key === "Enter" && !outcome && submit()}
                  placeholder="…"
                  className={cx(
                    "w-36 rounded-xl border-2 border-dashed px-2 py-1 text-center text-[13px] font-bold outline-none transition",
                    outcome
                      ? outcome.verdict === "incorrect"
                        ? "border-[var(--danger)] bg-[var(--danger-soft)] text-[var(--danger)]"
                        : "border-[var(--success)] bg-[var(--success-soft)] text-[var(--success)]"
                      : "border-[var(--mimo-progress)]/60 bg-[var(--surface-2)] focus:border-[var(--mimo-progress)]",
                  )}
                />
              )}
            </span>
          ))}
        </div>
      </Card>

      {!outcome && (
        <>
          <div className="flex flex-wrap gap-1.5">
            {cloze.distractors.map((option) => (
              <button
                key={option}
                onClick={() => setValue(option)}
                className="rounded-full border border-[var(--line)] bg-[var(--surface)] px-3 py-1.5 text-[11.5px] font-semibold text-[var(--ink-soft)] transition hover:border-[var(--mimo-progress)] hover:text-[var(--mimo-button)]"
              >
                {option}
              </button>
            ))}
          </div>
          <HintToggle hint={block.hintFa} used={aided} onUse={() => setAided(true)} />
          <Button full disabled={!value.trim()} onClick={submit}>
            بررسی پاسخ
          </Button>
        </>
      )}

      {outcome && (
        <div className="space-y-2">
          <FeedbackBanner outcome={outcome} block={block} />
          {outcome.verdict !== "correct" && (
            <div className="rounded-xl bg-[var(--surface-2)] p-3 text-[12px]">
              <span className="text-[var(--ink-faint)]">پاسخ کتاب: </span>
              <span className="font-extrabold text-[var(--mimo-button)]">{cloze.answer}</span>
            </div>
          )}
        </div>
      )}
    </div>
  );
}

function AssemblyBlock({
  block,
  outcome,
  onGrade,
}: {
  block: LessonBlock;
  outcome?: BlockOutcome;
  onGrade: (result: BlockOutcome) => void;
}) {
  const [picked, setPicked] = useState<string[]>(outcome?.value ? outcome.value.split("|") : []);
  const [aided, setAided] = useState(false);
  const tokens = block.tokens ?? [];
  const solution = block.assembly?.solution ?? [];
  const usedTraps = picked.filter((id) => tokens.find((token) => token.id === id)?.kind === "trap");

  const submit = () => {
    const correct = picked.length === solution.length && picked.every((id, index) => id === solution[index]);
    onGrade({
      verdict: correct ? "correct" : "incorrect",
      aided,
      attempts: 1,
      value: picked.join("|"),
      grade: {
        verdict: correct ? "CORRECT" : "INCORRECT",
        normalizedInput: picked.join(","),
        normalizedExpected: solution.join(","),
        feedbackState: correct ? "jm.m" : "jm.o",
        nearMiss: !correct && picked.length === solution.length,
        distance: Math.abs(picked.length - solution.length),
        messageFa: correct
          ? "زنجیرهٔ مفهومی با متن کتاب منطبق است."
          : usedTraps.length > 0
            ? "یکی از بلوک‌های انتخابی، تلهٔ طراح است؛ توضیح آن را در پایین ببین."
            : "ترتیب بلوک‌ها با جملهٔ کتاب نمی‌خواند.",
      },
    });
  };

  return (
    <div className="space-y-3">
      <Card className="min-h-[92px] p-3">
        <div className="mb-1.5 text-[10px] font-bold text-[var(--ink-faint)]">زنجیرهٔ تو</div>
        <div className="flex flex-wrap gap-1.5">
          {picked.length === 0 && <span className="text-[12px] text-[var(--ink-faint)]">از بلوک‌های پایین انتخاب کن…</span>}
          {picked.map((id, index) => {
            const token = tokens.find((item) => item.id === id);
            return (
              <button
                key={`${id}-${index}`}
                disabled={Boolean(outcome)}
                onClick={() => setPicked(picked.filter((_, itemIndex) => itemIndex !== index))}
                className="rounded-xl border border-[var(--mimo-progress)]/30 bg-[var(--mimo-soft)] px-2.5 py-1.5 text-[11.5px] font-semibold text-[var(--mimo-button)]"
              >
                {token?.text}
              </button>
            );
          })}
        </div>
      </Card>

      <div className="flex flex-wrap gap-1.5">
        {tokens.map((token) => {
          const used = picked.includes(token.id);
          return (
            <button
              key={token.id}
              disabled={used || Boolean(outcome)}
              onClick={() => setPicked([...picked, token.id])}
              className={cx(
                "rounded-xl border px-2.5 py-1.5 text-[11.5px] font-semibold transition",
                used
                  ? "border-dashed border-[var(--line)] bg-transparent text-[var(--ink-faint)] opacity-40"
                  : "border-[var(--line)] bg-[var(--surface)] text-[var(--ink)] hover:border-[var(--mimo-progress)]",
              )}
            >
              {token.text}
            </button>
          );
        })}
      </div>

      {!outcome && (
        <>
          <HintToggle hint={block.hintFa} used={aided} onUse={() => setAided(true)} />
          <div className="flex gap-2">
            <Button variant="outline" size="md" onClick={() => setPicked([])}>
              <RotateCcw size={14} /> پاک کردن
            </Button>
            <Button full disabled={picked.length === 0} onClick={submit}>
              بررسی چیدمان
            </Button>
          </div>
        </>
      )}

      {outcome && (
        <div className="space-y-2">
          <FeedbackBanner outcome={outcome} block={block} />
          <div className="rounded-xl bg-[var(--surface-2)] p-3 text-[12px] leading-6">
            <div className="mb-1 text-[10px] font-bold text-[var(--ink-faint)]">ترتیب کتاب</div>
            {block.assembly?.answerFa}
          </div>
          {usedTraps.length > 0 && (
            <div className="rounded-xl bg-[var(--danger-soft)] p-3 text-[11.5px] leading-5 text-[var(--danger)]">
              {tokens.find((token) => token.id === usedTraps[0])?.trapHintFa}
            </div>
          )}
        </div>
      )}
    </div>
  );
}

function TrapBlock({
  block,
  outcome,
  onGrade,
}: {
  block: LessonBlock;
  outcome?: BlockOutcome;
  onGrade: (result: BlockOutcome) => void;
}) {
  const [selected, setSelected] = useState<string | null>(null);
  const [aided, setAided] = useState(false);
  const options = block.trapOptions ?? [];

  return (
    <div className="space-y-3">
      <div className="space-y-2">
        {options.map((option, index) => {
          const isChosen = selected === option.id;
          const revealed = Boolean(outcome);
          return (
            <button
              key={option.id}
              disabled={revealed}
              onClick={() => setSelected(option.id)}
              className={cx(
                "flex w-full items-start gap-2.5 rounded-2xl border p-3 text-right text-[12.5px] leading-6 transition",
                revealed && option.isTrap
                  ? "border-[var(--success)] bg-[var(--success-soft)]"
                  : revealed && isChosen
                    ? "border-[var(--danger)] bg-[var(--danger-soft)]"
                    : isChosen
                      ? "border-[var(--mimo-progress)] bg-[var(--mimo-soft)]"
                      : "border-[var(--line)] bg-[var(--surface)] hover:border-[var(--mimo-progress)]/50",
              )}
            >
              <span className="mt-0.5 flex h-5 w-5 shrink-0 items-center justify-center rounded-full bg-[var(--surface-2)] text-[10px] font-bold text-[var(--ink-soft)]">
                {["۱", "۲", "۳"][index] ?? index + 1}
              </span>
              <span className="text-[var(--ink)]">{option.textFa}</span>
            </button>
          );
        })}
      </div>

      {!outcome && (
        <>
          <HintToggle hint={block.hintFa} used={aided} onUse={() => setAided(true)} />
          <Button
            full
            disabled={!selected}
            onClick={() => {
              const chosen = options.find((option) => option.id === selected);
              onGrade({
                verdict: chosen?.isTrap ? "correct" : "incorrect",
                aided,
                attempts: 1,
                value: selected ?? undefined,
                grade: {
                  verdict: chosen?.isTrap ? "CORRECT" : "INCORRECT",
                  normalizedInput: selected ?? "",
                  normalizedExpected: options.find((o) => o.isTrap)?.id ?? "",
                  feedbackState: chosen?.isTrap ? "jm.m" : "jm.o",
                  nearMiss: false,
                  distance: 0,
                  messageFa: chosen?.isTrap
                    ? "تله را دقیقاً شکار کردی."
                    : "این گزاره تلهٔ طراح نبود؛ تله بخشی است که با متن کتاب نمی‌خواند.",
                },
              });
            }}
          >
            شکار تله
          </Button>
        </>
      )}

      {outcome && (
        <div className="space-y-2">
          <FeedbackBanner outcome={outcome} block={block} />
          <div className="space-y-1.5">
            {options.map((option) => (
              <div
                key={option.id}
                className={cx(
                  "rounded-xl p-2.5 text-[11.5px] leading-5",
                  option.isTrap
                    ? "bg-[var(--success-soft)] text-[var(--success)]"
                    : "bg-[var(--surface-2)] text-[var(--ink-soft)]",
                )}
              >
                <span className="font-bold">{option.isTrap ? "تله: " : "سالم: "}</span>
                {option.analysisFa}
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  );
}

function McqBlock({
  block,
  outcome,
  onGrade,
}: {
  block: LessonBlock;
  outcome?: BlockOutcome;
  onGrade: (result: BlockOutcome) => void;
}) {
  const mcq = block.mcq!;
  const [selected, setSelected] = useState<number | null>(null);
  const [aided, setAided] = useState(false);
  const correctIndex = useMemo(() => mcq.options.findIndex((option) => option.correct), [mcq]);

  return (
    <div className="space-y-3">
      <Card className="p-3.5">
        <p className="text-[13px] font-semibold leading-7">{mcq.stemFa}</p>
      </Card>

      <div className="space-y-2">
        {mcq.options.map((option, index) => {
          const revealed = Boolean(outcome);
          const isChosen = selected === index;
          return (
            <button
              key={option.id}
              disabled={revealed}
              onClick={() => setSelected(index)}
              className={cx(
                "flex w-full items-start gap-2.5 rounded-2xl border p-3 text-right text-[12.5px] leading-6 transition",
                revealed && index === correctIndex
                  ? "border-[var(--success)] bg-[var(--success-soft)]"
                  : revealed && isChosen
                    ? "border-[var(--danger)] bg-[var(--danger-soft)]"
                    : isChosen
                      ? "border-[var(--mimo-progress)] bg-[var(--mimo-soft)]"
                      : "border-[var(--line)] bg-[var(--surface)] hover:border-[var(--mimo-progress)]/50",
              )}
            >
              <span className="mt-0.5 flex h-5 w-5 shrink-0 items-center justify-center rounded-full bg-[var(--surface-2)] text-[10px] font-bold text-[var(--ink-soft)]">
                {["الف", "ب", "ج", "د"][index]}
              </span>
              <span>{option.textFa}</span>
            </button>
          );
        })}
      </div>

      {!outcome && (
        <>
          <HintToggle hint={mcq.hintFa} used={aided} onUse={() => setAided(true)} />
          <div className="flex items-center justify-between text-[10.5px] text-[var(--ink-faint)]">
            <span>سطح دشواری: {"★".repeat(mcq.difficulty)}</span>
            <span className="font-mono-code">{mcq.id}</span>
          </div>
          <Button
            full
            disabled={selected === null}
            onClick={() => {
              const correct = selected === correctIndex;
              onGrade({
                verdict: correct ? "correct" : "incorrect",
                aided,
                attempts: 1,
                value: String(selected),
                grade: {
                  verdict: correct ? "CORRECT" : "INCORRECT",
                  normalizedInput: String(selected),
                  normalizedExpected: String(correctIndex),
                  feedbackState: correct ? "jm.m" : "jm.o",
                  nearMiss: false,
                  distance: 0,
                  messageFa: correct ? "پاسخ صحیح. تحلیل سه گزینهٔ دیگر را ببین." : "پاسخ درست و تحلیل تله‌ها را در پایین ببین.",
                },
              });
            }}
          >
            ثبت پاسخ
          </Button>
        </>
      )}

      {outcome && (
        <div className="space-y-2">
          <FeedbackBanner outcome={outcome} block={block} />
          <div className="space-y-1.5">
            {mcq.options.map((option, index) => (
              <div
                key={option.id}
                className={cx(
                  "rounded-xl p-2.5 text-[11.5px] leading-5",
                  index === correctIndex
                    ? "bg-[var(--success-soft)] text-[var(--success)]"
                    : selected === index
                      ? "bg-[var(--danger-soft)] text-[var(--danger)]"
                      : "bg-[var(--surface-2)] text-[var(--ink-soft)]",
                )}
              >
                <span className="font-bold">{["الف", "ب", "ج", "د"][index]}: </span>
                {option.analysisFa}
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  );
}

function Celebration({
  lesson,
  stars,
  correct,
  total,
  nextLessonId,
  dueCards,
  onClose,
  onNext,
}: {
  lesson: Lesson;
  stars: number;
  correct: number;
  total: number;
  nextLessonId: string | null;
  dueCards: number;
  onClose: () => void;
  onNext: (lessonId: string) => void;
}) {
  return (
    <div className="absolute inset-0 z-10 flex items-center justify-center bg-[rgba(18,19,38,0.55)] p-4 backdrop-blur-sm">
      <div className="animate-pop surface w-full max-w-sm rounded-[26px] p-5 text-center">
        <div className="mx-auto mb-3 flex h-16 w-16 items-center justify-center rounded-full bg-[var(--mimo-soft)]">
          <Flame size={30} className="text-[var(--mimo-button)]" />
        </div>
        <h3 className="text-[17px] font-extrabold">درس تکمیل شد!</h3>
        <p className="mt-1 text-[12px] text-[var(--ink-faint)]">{lesson.titleFa}</p>

        <div className="mt-3 flex items-center justify-center">
          <Stars count={stars} size={26} />
        </div>

        <div className="mt-4 grid grid-cols-3 gap-2">
          <div className="rounded-xl bg-[var(--surface-2)] p-2">
            <div className="text-[9.5px] text-[var(--ink-faint)]">پاسخ درست</div>
            <div className="tabular text-[15px] font-extrabold">
              {correct}/{total}
            </div>
          </div>
          <div className="rounded-xl bg-[var(--surface-2)] p-2">
            <div className="text-[9.5px] text-[var(--ink-faint)]">XP</div>
            <div className="tabular text-[15px] font-extrabold">+۴۰</div>
          </div>
          <div className="rounded-xl bg-[var(--surface-2)] p-2">
            <div className="text-[9.5px] text-[var(--ink-faint)]">کارت مرور</div>
            <div className="tabular text-[15px] font-extrabold">{dueCards}</div>
          </div>
        </div>

        <div className="mt-4 space-y-2">
          {nextLessonId ? (
            <Button full onClick={() => onNext(nextLessonId)}>
              <Play size={15} /> درس بعدی
            </Button>
          ) : (
            <Button full onClick={onClose}>
              <Check size={15} /> بازگشت به نقشهٔ مسیر
            </Button>
          )}
          {nextLessonId && (
            <Button variant="ghost" full onClick={onClose}>
              بازگشت به نقشه
            </Button>
          )}
        </div>
      </div>
    </div>
  );
}
