import { describe, expect, it } from "vitest";
import { initialSkillState, updateSkillState } from "@/core/algorithms/bkt";
import {
  DAY_MS,
  createCard,
  dueCards,
  forecast,
  intervalDays,
  ratingForOutcome,
  retrievability,
  scheduleCard,
} from "@/core/algorithms/fsrs";
import { flowStatus, difficultyWeight } from "@/core/algorithms/flow";

describe("Calibrated BKT", () => {
  it("rises on a correct answer and falls on a wrong one", () => {
    const start = initialSkillState();
    const correct = updateSkillState(start, true, Date.now(), { aided: false });
    const wrong = updateSkillState(start, false, Date.now(), { aided: false });
    expect(correct.pKnown).toBeGreaterThan(start.pKnown);
    expect(wrong.pKnown).toBeLessThan(start.pKnown);
  });

  it("gives less credit to an aided correct answer than an unaided one", () => {
    const start = initialSkillState();
    const unaided = updateSkillState(start, true, Date.now(), { aided: false });
    const aided = updateSkillState(start, true, Date.now(), { aided: true });
    expect(unaided.pKnown).toBeGreaterThan(aided.pKnown);
    expect(unaided.unaidedCorrect).toBe(1);
    expect(aided.aidedCorrect).toBe(1);
  });

  it("counts attempts and resets the streak on a mistake", () => {
    let state = initialSkillState();
    state = updateSkillState(state, true, Date.now(), { aided: false });
    state = updateSkillState(state, true, Date.now(), { aided: false });
    expect(state.streak).toBe(2);
    state = updateSkillState(state, false, Date.now(), { aided: false });
    expect(state.streak).toBe(0);
    expect(state.attempts).toBe(3);
  });
});

describe("FSRS-5 scheduler", () => {
  const now = Date.UTC(2026, 0, 1);

  it("schedules a new card further out for Good than for Hard", () => {
    const base = createCard({
      id: "c1",
      lessonId: "BIO12-C1-L1",
      skillId: "BIO12-C1-L1.concept",
      promptFa: "پیوند چیست؟",
      answerFa: "فسفودی‌استر",
      now,
    });
    const hard = scheduleCard(base, 2, now);
    const good = scheduleCard(base, 3, now);
    expect(good.stability).toBeGreaterThan(hard.stability);
    expect(good.due).toBeGreaterThan(hard.due);
  });

  it("sends an Again card back to tomorrow and counts a lapse", () => {
    const base = createCard({
      id: "c2",
      lessonId: "BIO12-C1-L1",
      skillId: "BIO12-C1-L1.concept",
      promptFa: "q",
      answerFa: "a",
      now,
    });
    const learned = scheduleCard(base, 3, now);
    const forgotten = scheduleCard(learned, 1, now + 5 * DAY_MS);
    expect(forgotten.lapses).toBe(1);
    expect(forgotten.scheduledDays).toBe(1);
    expect(forgotten.state).toBe("relearning");
  });

  it("computes a decreasing retrievability over time", () => {
    const card = scheduleCard(
      createCard({ id: "c3", lessonId: "l", skillId: "s", promptFa: "q", answerFa: "a", now }),
      3,
      now,
    );
    const fresh = retrievability(card, now);
    const later = retrievability(card, now + 30 * DAY_MS);
    expect(fresh).toBeGreaterThan(later);
    expect(fresh).toBeLessThanOrEqual(1);
  });

  it("forecasts the review queue into seven day buckets", () => {
    const card = scheduleCard(
      createCard({ id: "c4", lessonId: "l", skillId: "s", promptFa: "q", answerFa: "a", now }),
      3,
      now,
    );
    const buckets = forecast([card], now);
    expect(buckets).toHaveLength(7);
    expect(buckets.reduce((sum, b) => sum + b.count, 0)).toBe(1);
  });

  it("puts overdue cards at the head of the queue", () => {
    const overdue = { ...createCard({ id: "x", lessonId: "l", skillId: "s", promptFa: "q", answerFa: "a" }), due: now - DAY_MS };
    const future = { ...createCard({ id: "y", lessonId: "l", skillId: "s", promptFa: "q", answerFa: "a" }), due: now + DAY_MS };
    expect(dueCards([future, overdue], now).map((c) => c.id)).toEqual(["x"]);
  });

  it("maps outcomes to ratings", () => {
    expect(ratingForOutcome({ correct: false, aided: false })).toBe(1);
    expect(ratingForOutcome({ correct: true, aided: true })).toBe(2);
    expect(ratingForOutcome({ correct: true, aided: false })).toBe(3);
    expect(ratingForOutcome({ correct: true, aided: false, secondsSpent: 5 })).toBe(4);
  });

  it("keeps intervals within one year", () => {
    expect(intervalDays(0.02)).toBeGreaterThanOrEqual(1);
    expect(intervalDays(10000)).toBeLessThanOrEqual(365);
  });
});

describe("flow band controller", () => {
  it("asks for easier items when accuracy is under 70%", () => {
    const status = flowStatus([false, false, true, false, false]);
    expect(status.band).toBe("too_hard");
    expect(status.difficultyBias).toBe(-1);
    expect(status.showHints).toBe(true);
  });

  it("raises difficulty above 85% accuracy", () => {
    const status = flowStatus([true, true, true, true, true, true]);
    expect(status.band).toBe("too_easy");
    expect(status.difficultyBias).toBe(1);
    expect(status.showHints).toBe(false);
  });

  it("holds steady inside the band", () => {
    const status = flowStatus([true, true, true, false, true]);
    expect(status.band).toBe("in_band");
    expect(difficultyWeight(2, status)).toBeGreaterThan(difficultyWeight(1, status));
  });
});
