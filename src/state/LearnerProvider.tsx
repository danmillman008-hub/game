"use client";

import { createContext, useCallback, useContext, useEffect, useMemo, useState, type ReactNode } from "react";
import { buildKnowledgeGraph, type KnowledgeGraph } from "@/core/algorithms/kst";
import type { Rating } from "@/core/algorithms/fsrs";
import { getCurriculum } from "@/core/content";
import type { ExamResult, ExamSession } from "@/core/exam/exam";
import {
  completeLesson as completeLessonState,
  createInitialLearnerState,
  finishExam as finishExamState,
  recordAttempt as recordAttemptState,
  resetLearner,
  reviewCard as reviewCardState,
  setProfile as setProfileState,
  setTheme as setThemeState,
  type LearnerProfile,
  type LearnerState,
  type RecordAttemptInput,
  type ThemeMode,
} from "@/core/state/learner";
import type { Curriculum, MCQ } from "@/core/types";

const STORAGE_KEY = "konkur-mimo:learner:v2";

interface LearnerContextValue {
  state: LearnerState;
  hydrated: boolean;
  curriculum: Curriculum;
  graph: KnowledgeGraph;
  actions: {
    recordAttempt: (input: RecordAttemptInput) => void;
    completeLesson: (lessonId: string, accuracy: number) => void;
    reviewCard: (cardId: string, rating: Rating) => void;
    finishExam: (session: ExamSession, result: ExamResult) => void;
    setProfile: (patch: Partial<LearnerProfile>) => void;
    setTheme: (theme: ThemeMode) => void;
    reset: () => void;
    importState: (raw: string) => { ok: boolean; messageFa: string };
  };
}

const LearnerContext = createContext<LearnerContextValue | null>(null);

function migrate(raw: unknown): LearnerState | null {
  if (!raw || typeof raw !== "object") return null;
  const candidate = raw as Partial<LearnerState>;
  if (candidate.version !== 2) return null;
  const base = createInitialLearnerState();
  return {
    ...base,
    ...candidate,
    profile: { ...base.profile, ...(candidate.profile ?? {}) },
    wallet: { ...base.wallet, ...(candidate.wallet ?? {}) },
    streak: { ...base.streak, ...(candidate.streak ?? {}) },
    skills: candidate.skills ?? {},
    lessons: candidate.lessons ?? {},
    reviewCards: candidate.reviewCards ?? [],
    attempts: candidate.attempts ?? [],
    examResults: candidate.examResults ?? [],
  };
}

export function LearnerProvider({ children }: { children: ReactNode }) {
  const curriculum = useMemo(() => getCurriculum(), []);
  const graph = useMemo(() => buildKnowledgeGraph(curriculum), [curriculum]);
  const [state, setState] = useState<LearnerState>(() => createInitialLearnerState());
  const [hydrated, setHydrated] = useState(false);

  useEffect(() => {
    try {
      const raw = window.localStorage.getItem(STORAGE_KEY);
      if (raw) {
        const migrated = migrate(JSON.parse(raw));
        if (migrated) setState(migrated);
      }
    } catch {
      // corrupt storage is ignored: the learner keeps a fresh local profile
    } finally {
      setHydrated(true);
    }
  }, []);

  useEffect(() => {
    if (!hydrated) return;
    try {
      window.localStorage.setItem(STORAGE_KEY, JSON.stringify(state));
    } catch {
      // quota errors must never break a lesson
    }
  }, [state, hydrated]);

  useEffect(() => {
    if (!hydrated) return;
    document.documentElement.dataset.theme = state.profile.theme;
  }, [state.profile.theme, hydrated]);

  const actions = useMemo<LearnerContextValue["actions"]>(
    () => ({
      recordAttempt: (input) => setState((prev) => recordAttemptState(prev, input)),
      completeLesson: (lessonId, accuracy) => setState((prev) => completeLessonState(prev, lessonId, accuracy)),
      reviewCard: (cardId, rating) => setState((prev) => reviewCardState(prev, cardId, rating)),
      finishExam: (session, result) =>
        setState((prev) => finishExamState(prev, session, result, curriculum.questions as MCQ[])),
      setProfile: (patch) => setState((prev) => setProfileState(prev, patch)),
      setTheme: (theme) => setState((prev) => setThemeState(prev, theme)),
      reset: () => setState((prev) => resetLearner(prev.profile)),
      importState: (raw) => {
        try {
          const parsed = migrate(JSON.parse(raw));
          if (!parsed) return { ok: false, messageFa: "نسخهٔ فایل پشتیبان با این نسخهٔ اپ سازگار نیست." };
          setState(parsed);
          return { ok: true, messageFa: "دادهٔ یادگیری با موفقیت بازیابی شد." };
        } catch {
          return { ok: false, messageFa: "فایل پشتیبان قابل خواندن نیست." };
        }
      },
    }),
    [curriculum],
  );

  const value = useMemo<LearnerContextValue>(
    () => ({ state, hydrated, curriculum, graph, actions }),
    [state, hydrated, curriculum, graph, actions],
  );

  return <LearnerContext.Provider value={value}>{children}</LearnerContext.Provider>;
}

export function useLearner(): LearnerContextValue {
  const context = useContext(LearnerContext);
  if (!context) throw new Error("useLearner must be used inside <LearnerProvider>");
  return context;
}

export { useCallback };
