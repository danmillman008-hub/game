import { describe, expect, it } from "vitest";
import { getCurriculum } from "@/core/content";
import { EXAM_MODES, buildExam, scoreExam, formatClock } from "@/core/exam/exam";
import {
  completeLesson,
  createInitialLearnerState,
  dueReviewCards,
  finishExam,
  lessonLock,
  recordAttempt,
  reviewCard,
  summarize,
} from "@/core/state/learner";

const curriculum = getCurriculum();
const bank = curriculum.questions;

describe("exam hub", () => {
  it("exposes the seven Konkur sections", () => {
    expect(EXAM_MODES.map((m) => m.id)).toEqual([
      "diagnostic",
      "chapter",
      "targeted",
      "timed",
      "mistakes",
      "bank",
      "mock",
    ]);
    expect(EXAM_MODES.find((m) => m.id === "mock")?.minutes).toBe(270);
  });

  it("builds a deterministic session for a given seed", () => {
    const a = buildExam(bank, { mode: "chapter", chapterId: "BIO12-C1", seed: "s1", now: 1 });
    const b = buildExam(bank, { mode: "chapter", chapterId: "BIO12-C1", seed: "s1", now: 1 });
    expect(a.items.map((i) => i.questionId)).toEqual(b.items.map((i) => i.questionId));
    expect(a.items.length).toBeGreaterThan(0);
    expect(a.items.every((i) => i.lessonId.startsWith("BIO12-C1"))).toBe(true);
  });

  it("applies one-third negative marking and never goes below zero", () => {
    const session = buildExam(bank, { mode: "timed", count: 3, seed: "neg", now: 1 });
    const [first, second, third] = session.items;
    const q1 = bank.find((q) => q.id === first.questionId)!;
    const q2 = bank.find((q) => q.id === second.questionId)!;
    const q3 = bank.find((q) => q.id === third.questionId)!;

    session.answers[first.questionId] = q1.options.findIndex((o) => o.correct);
    session.answers[second.questionId] = q2.options.findIndex((o) => !o.correct);
    session.answers[third.questionId] = q3.options.findIndex((o) => !o.correct);

    const result = scoreExam(session, bank, 1000);
    expect(result.correct).toBe(1);
    expect(result.wrong).toBe(2);
    expect(result.blank).toBe(0);
    // 3 correct points − 2 penalty points = 1
    expect(result.score).toBe(1);
    expect(result.maxScore).toBe(9);
    expect(result.percent).toBe(11);
  });

  it("ignores penalties in no-negative modes", () => {
    const session = buildExam(bank, { mode: "bank", count: 2, seed: "nn", now: 1 });
    const first = session.items[0];
    const q1 = bank.find((q) => q.id === first.questionId)!;
    session.answers[first.questionId] = q1.options.findIndex((o) => !o.correct);
    const result = scoreExam(session, bank, 1000);
    expect(result.negativeMarking).toBe(false);
    expect(result.score).toBe(0);
    expect(result.blank).toBe(1);
  });

  it("formats the countdown clock", () => {
    expect(formatClock(270 * 60)).toBe("04:30:00");
    expect(formatClock(59)).toBe("00:59");
  });
});

describe("learner state machine", () => {
  it("starts with the first lesson unlocked and later ones locked", () => {
    const state = createInitialLearnerState(1_700_000_000_000);
    const first = curriculum.lessonById.get("BIO12-C1-L1")!;
    const second = curriculum.lessonById.get("BIO12-C1-L2")!;
    expect(lessonLock(state, first)).toBe("available");
    expect(lessonLock(state, second)).toBe("locked");
  });

  it("unlocks the next lesson after one try (ADD-04)", () => {
    let state = createInitialLearnerState(1_700_000_000_000);
    state = recordAttempt(state, {
      lessonId: "BIO12-C1-L1",
      skillId: "BIO12-C1-L1.concept",
      correct: false,
      aided: false,
      now: 1_700_000_000_000,
    });
    expect(lessonLock(state, curriculum.lessonById.get("BIO12-C1-L2")!)).toBe("available");
  });

  it("creates an FSRS card only when the answer is wrong or scaffolded", () => {
    let state = createInitialLearnerState(1_700_000_000_000);
    state = recordAttempt(state, {
      lessonId: "BIO12-C1-L1",
      skillId: "BIO12-C1-L1.concept",
      correct: true,
      aided: false,
      blockId: "b1",
      promptFa: "پیوند؟",
      answerFa: "فسفودی‌استر",
      now: 1_700_000_000_000,
    });
    expect(state.reviewCards).toHaveLength(0);

    state = recordAttempt(state, {
      lessonId: "BIO12-C1-L1",
      skillId: "BIO12-C1-L1.concept",
      correct: false,
      aided: false,
      blockId: "b1",
      promptFa: "پیوند؟",
      answerFa: "فسفودی‌استر",
      now: 1_700_000_100_000,
    });
    expect(state.reviewCards).toHaveLength(1);
    expect(state.reviewCards[0].scheduledDays).toBe(1);
    expect(dueReviewCards(state, 1_700_000_100_000)).toHaveLength(0);
    expect(dueReviewCards(state, 1_700_000_100_000 + 2 * 24 * 3600 * 1000)).toHaveLength(1);
  });

  it("never deletes attempts (append-only log)", () => {
    let state = createInitialLearnerState(1_700_000_000_000);
    for (let i = 0; i < 3; i++) {
      state = recordAttempt(state, {
        lessonId: "BIO12-C1-L1",
        skillId: "BIO12-C1-L1.concept",
        correct: i === 0,
        aided: false,
        now: 1_700_000_000_000 + i,
      });
    }
    expect(state.attempts).toHaveLength(3);
  });

  it("awards stars and coins on completion and keeps the best result", () => {
    let state = createInitialLearnerState(1_700_000_000_000);
    state = completeLesson(state, "BIO12-C1-L1", 0.85, 1_700_000_000_000);
    expect(state.lessons["BIO12-C1-L1"].stars).toBe(2);
    const xpAfterFirst = state.wallet.xp;
    state = completeLesson(state, "BIO12-C1-L1", 0.5, 1_700_000_100_000);
    expect(state.lessons["BIO12-C1-L1"].stars).toBe(2);
    expect(state.wallet.xp).toBeGreaterThan(xpAfterFirst);
  });

  it("moves a reviewed card into the future", () => {
    let state = createInitialLearnerState(1_700_000_000_000);
    state = recordAttempt(state, {
      lessonId: "BIO12-C1-L1",
      skillId: "BIO12-C1-L1.concept",
      correct: false,
      aided: false,
      blockId: "b",
      promptFa: "q",
      answerFa: "a",
      now: 1_700_000_000_000,
    });
    const cardId = state.reviewCards[0].id;
    const reviewed = reviewCard(state, cardId, 3, 1_700_000_000_000);
    expect(reviewed.reviewCards[0].due).toBeGreaterThan(1_700_000_000_000);
    expect(dueReviewCards(reviewed, 1_700_000_000_000)).toHaveLength(0);
  });

  it("schedules mistakes from a finished exam and updates BKT", () => {
    let state = createInitialLearnerState(1_700_000_000_000);
    const session = buildExam(bank, { mode: "timed", count: 4, seed: "exam", now: 1 });
    for (const [index, item] of session.items.entries()) {
      const question = bank.find((q) => q.id === item.questionId)!;
      session.answers[item.questionId] =
        index % 2 === 0 ? question.options.findIndex((o) => o.correct) : question.options.findIndex((o) => !o.correct);
    }
    const result = scoreExam(session, bank, 1_000_000);
    state = finishExam(state, session, result, bank, 1_000_000);
    expect(state.examResults).toHaveLength(1);
    expect(state.reviewCards.length).toBe(result.wrong);
    expect(Object.keys(state.skills).length).toBeGreaterThan(0);
  });

  it("summarises mastery, accuracy and the due queue", () => {
    let state = createInitialLearnerState(1_700_000_000_000);
    state = recordAttempt(state, {
      lessonId: "BIO12-C1-L1",
      skillId: "BIO12-C1-L1.concept",
      correct: true,
      aided: false,
      now: 1_700_000_000_000,
    });
    state = recordAttempt(state, {
      lessonId: "BIO12-C1-L1",
      skillId: "BIO12-C1-L1.concept",
      correct: true,
      aided: true,
      now: 1_700_000_100_000,
    });
    const summary = summarize(state, curriculum, 1_700_000_100_000);
    expect(summary.totalAttempts).toBe(2);
    expect(summary.accuracy).toBe(1);
    expect(summary.unaidedAccuracy).toBe(1);
    expect(summary.aidedShare).toBe(0.5);
    expect(summary.totalLessons).toBe(18);
  });
});
