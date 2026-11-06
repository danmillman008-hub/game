"use client";

import { useEffect, useMemo, useRef, useState } from "react";
import { Bot, Brain, RefreshCw, Send, Sparkles, WifiOff } from "lucide-react";
import { chaptersOfSubject, lessonsOfChapter } from "@/core/content";
import {
  PHASE_LABELS,
  PHASE_ORDER,
  advanceHarness,
  createHarnessSession,
  harnessSuggestions,
  type HarnessSession,
} from "@/core/harness/engine";
import type { SubjectId } from "@/core/types";
import { useLearner } from "@/state/LearnerProvider";
import { Button, Card, Chip, Progress, SectionTitle, cx } from "@/components/ui/kit";

export function HarnessTab() {
  const { state, curriculum } = useLearner();
  const [subjectId, setSubjectId] = useState<SubjectId>("bio12");
  const chapters = chaptersOfSubject(subjectId);
  const [lessonsList] = useState(() => chapters.flatMap((chapter) => lessonsOfChapter(chapter.id)));

  const defaultLessonId =
    state.lastLessonId && curriculum.lessonById.has(state.lastLessonId)
      ? state.lastLessonId
      : lessonsList[0]?.id ?? curriculum.lessons[0].id;

  const [lessonId, setLessonId] = useState(defaultLessonId);
  const lesson = curriculum.lessonById.get(lessonId) ?? curriculum.lessons[0];
  const [session, setSession] = useState<HarnessSession>(() => createHarnessSession(lesson));
  const [input, setInput] = useState("");

  const openLesson = (nextId: string) => {
    const nextLesson = curriculum.lessonById.get(nextId);
    if (!nextLesson) return;
    setSubjectId(nextLesson.subjectId);
    setLessonId(nextLesson.id);
    setSession(createHarnessSession(nextLesson));
    setInput("");
  };
  const bottomRef = useRef<HTMLDivElement | null>(null);

  useEffect(() => {
    bottomRef.current?.scrollIntoView?.({ behavior: "smooth", block: "end" });
  }, [session.messages.length]);

  const phaseIndex = PHASE_ORDER.indexOf(session.phase);
  const suggestions = useMemo(() => harnessSuggestions(lesson), [lesson]);

  const send = (text: string) => {
    if (!text.trim()) return;
    setSession((prev) => advanceHarness(prev, text, lesson));
    setInput("");
  };

  return (
    <div className="space-y-4">
      <Card className="p-4">
        <div className="flex items-start gap-3">
          <div className="rounded-2xl bg-[var(--mimo-soft)] p-2.5 text-[var(--mimo-button)]">
            <Bot size={20} />
          </div>
          <div className="min-w-0 flex-1">
            <div className="flex flex-wrap items-center gap-1.5">
              <h2 className="text-[15px] font-extrabold">مربی لرن‌هارنس</h2>
              <Chip tone="success" icon={<Sparkles size={10} />}>
                LocalContentProvider
              </Chip>
              <Chip tone="neutral" icon={<WifiOff size={10} />}>
                آفلاین
              </Chip>
            </div>
            <p className="mt-1 text-[11.5px] leading-5 text-[var(--ink-soft)]">
              چهار فاز Measure → Plan → Teach → Practice روی گراف گزاره‌های کتاب. هر جملهٔ مربی به یک گزارهٔ
              دارای منبع گره خورده است؛ بنابراین متن ساختگی تولید نمی‌شود.
            </p>
          </div>
        </div>

        <div className="mt-4 flex items-center gap-1">
          {PHASE_ORDER.map((phase, index) => (
            <div key={phase} className="flex flex-1 items-center gap-1">
              <div
                className={cx(
                  "flex w-full flex-col items-center gap-1 rounded-xl px-1 py-1.5 text-[10px] font-bold",
                  index < phaseIndex
                    ? "bg-[var(--success-soft)] text-[var(--success)]"
                    : index === phaseIndex
                      ? "bg-[var(--mimo-soft)] text-[var(--mimo-button)]"
                      : "bg-[var(--surface-2)] text-[var(--ink-faint)]",
                )}
              >
                <span className="tabular text-[9px] opacity-70">{index + 1}</span>
                {PHASE_LABELS[phase]}
              </div>
            </div>
          ))}
        </div>
        <div className="mt-2">
          <Progress value={((phaseIndex + 1) / PHASE_ORDER.length) * 100} height={4} />
        </div>
      </Card>

      <div className="grid grid-cols-2 gap-2">
        <label className="block">
          <span className="mb-1 block text-[10px] font-bold text-[var(--ink-faint)]">درس</span>
          <select
            value={lessonId}
            onChange={(event) => openLesson(event.target.value)}
            className="w-full rounded-xl border border-[var(--line)] bg-[var(--surface)] px-2 py-2 text-[11px]"
          >
            {curriculum.chapters.map((chapter) => (
              <optgroup key={chapter.id} label={chapter.titleFa}>
                {lessonsOfChapter(chapter.id).map((item) => (
                  <option key={item.id} value={item.id}>
                    {item.titleFa}
                  </option>
                ))}
              </optgroup>
            ))}
          </select>
        </label>
        <div className="flex items-end">
          <Button
            variant="outline"
            full
            onClick={() => setSession(createHarnessSession(lesson))}
            className="h-[38px]"
          >
            <RefreshCw size={13} /> جلسهٔ جدید
          </Button>
        </div>
      </div>

      <Card className="flex max-h-[420px] flex-col overflow-hidden">
        <div className="scrollbar-thin flex-1 space-y-2 overflow-y-auto p-3">
          {session.messages.map((message) => (
            <div
              key={message.id}
              className={cx("flex", message.role === "learner" ? "justify-end" : "justify-start")}
            >
              <div
                className={cx(
                  "max-w-[86%] rounded-2xl px-3 py-2 text-[12px] leading-6",
                  message.role === "learner"
                    ? "bg-[var(--mimo-button)] text-white"
                    : message.role === "system"
                      ? "bg-[var(--surface-2)] text-[10.5px] text-[var(--ink-faint)]"
                      : "bg-[var(--surface-2)] text-[var(--ink)]",
                )}
              >
                {message.role === "coach" && (
                  <div className="mb-1 flex items-center gap-1 text-[9px] font-bold text-[var(--mimo-button)]">
                    <Brain size={10} /> {PHASE_LABELS[message.phase]}
                  </div>
                )}
                {message.textFa}
                {message.chips && message.chips.length > 0 && (
                  <div className="mt-2 flex flex-wrap gap-1">
                    {message.chips.map((chip) => (
                      <button
                        key={chip}
                        onClick={() => send(chip)}
                        className="rounded-full bg-[var(--surface)] px-2 py-1 text-[10px] font-semibold text-[var(--mimo-button)] shadow-sm"
                      >
                        {chip}
                      </button>
                    ))}
                  </div>
                )}
              </div>
            </div>
          ))}
          <div ref={bottomRef} />
        </div>

        <div className="border-t border-[var(--line)] p-2.5">
          <div className="mb-2 flex gap-1 overflow-x-auto scrollbar-thin">
            {suggestions.map((suggestion) => (
              <button
                key={suggestion}
                onClick={() => send(suggestion)}
                className="shrink-0 rounded-full border border-[var(--line)] px-2.5 py-1 text-[10px] font-semibold text-[var(--ink-soft)] hover:border-[var(--mimo-progress)] hover:text-[var(--mimo-button)]"
              >
                {suggestion}
              </button>
            ))}
          </div>
          <div className="flex gap-2">
            <input
              value={input}
              onChange={(event) => setInput(event.target.value)}
              onKeyDown={(event) => event.key === "Enter" && send(input)}
              placeholder="پاسخ یا سؤالت را بنویس…"
              className="flex-1 rounded-xl border border-[var(--line)] bg-[var(--surface-2)] px-3 py-2 text-[12px] outline-none focus:border-[var(--mimo-progress)]"
            />
            <Button onClick={() => send(input)} disabled={!input.trim()}>
              <Send size={15} className="rotate-180" />
            </Button>
          </div>
        </div>
      </Card>

      <div>
        <SectionTitle eyebrow="گراف گزاره‌ها" title="گزاره‌های کتاب و وضعیت تسلط" />
        <div className="space-y-1.5">
          {lesson.propositions.map((proposition) => {
            const concept = state.skills[`${lesson.id}.concept`]?.pKnown ?? 0;
            return (
              <Card key={proposition.id} className="flex items-start gap-2 p-2.5">
                <span className="mt-1 h-2 w-2 shrink-0 rounded-full bg-[var(--mimo-progress)] opacity-60" />
                <div className="min-w-0 flex-1">
                  <p className="text-[11.5px] leading-6">{proposition.textFa}</p>
                  <div className="mt-1 flex items-center gap-2">
                    <div className="w-20">
                      <Progress value={concept * 100} height={3} />
                    </div>
                    <span className="tabular text-[9px] text-[var(--ink-faint)]">{Math.round(concept * 100)}٪</span>
                    <span className="font-mono-code text-[8.5px] text-[var(--ink-faint)]">{proposition.id}</span>
                  </div>
                </div>
              </Card>
            );
          })}
        </div>
        <Card className="mt-2 p-3 text-[10.5px] leading-5 text-[var(--ink-soft)]">
          در استقرار سروری، همین جلسه از مسیر <span className="font-mono-code">POST /api/harness</span> با استریم SSE و
          کلید LLM سمت سرور اجرا می‌شود؛ در نسخهٔ آفلاین، Provider محلی بدون هیچ درخواست شبکه‌ای پاسخ می‌دهد.
        </Card>
      </div>
    </div>
  );
}
