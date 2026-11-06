import { describe, expect, it } from "vitest";
import { gradeAnswer, gradeQuantifiedStatement } from "@/core/text/grade";
import { normalizeAnswer, similarity, canonicalizeFa } from "@/core/text/normalize";

describe("Persian normaliser (Q-44 closure)", () => {
  it("unifies Arabic yeh/kaf with Persian glyphs", () => {
    expect(normalizeAnswer("ياخته")).toBe(normalizeAnswer("یاخته"));
    expect(normalizeAnswer("كربن")).toBe(normalizeAnswer("کربن"));
  });

  it("drops ZWNJ and collapses whitespace", () => {
    expect(normalizeAnswer("پلی‌نوکلئوتید")).toBe("پلینوکلئوتید");
    expect(normalizeAnswer("پلی نوکلئوتید")).toBe("پلینوکلئوتید");
  });

  it("converts Persian and Arabic digits to ASCII", () => {
    expect(normalizeAnswer("۱۰⁻۳")).toBe("103");
    expect(normalizeAnswer("١٢٣")).toBe("123");
  });

  it("strips diacritics, tatweel and punctuation", () => {
    expect(normalizeAnswer("مُغزِ استخوان")).toBe("مغزاستخوان");
    expect(normalizeAnswer("دنا؛ «مولکول»")).toBe("دنامولکول");
  });

  it("canonical form keeps ZWNJ but removes zero-width garbage", () => {
    expect(canonicalizeFa("پلی\u200cنوکلئوتید")).toBe("پلی‌نوکلئوتید");
  });

  it("similarity is 1 for equal keys and lower for a one-character typo", () => {
    expect(similarity("هلیکاز", "هلیکاز")).toBe(1);
    expect(similarity("هلیکاز", "هلیکار")).toBeGreaterThan(0.6);
  });
});

describe("three-way verdict (jm.m / jm.n / jm.o)", () => {
  it("returns CORRECT when the canonical answer matches exactly", () => {
    const result = gradeAnswer("فسفودی‌استر", "فسفودی‌استر");
    expect(result.verdict).toBe("CORRECT");
    expect(result.feedbackState).toBe("jm.m");
  });

  it("returns PARTIAL for a ZWNJ difference and explains why", () => {
    const result = gradeAnswer("پلی نوکلئوتید", "پلی‌نوکلئوتید");
    expect(result.verdict).toBe("PARTIAL");
    expect(result.feedbackState).toBe("jm.n");
    expect(result.partialReason).toBe("ZWNJ");
    expect(result.messageFa).toContain("نیم‌فاصله");
  });

  it("returns PARTIAL for Arabic glyphs and keeps the same meaning", () => {
    const result = gradeAnswer("ياخته", "یاخته");
    expect(result.verdict).toBe("PARTIAL");
    expect(result.partialReason).toBe("ARABIC_GLYPH");
  });

  it("treats Persian digits as an equal value, only a surface difference", () => {
    const result = gradeAnswer("۳", "3");
    expect(result.verdict).toBe("PARTIAL");
    expect(result.normalizedInput).toBe("3");
  });

  it("returns INCORRECT for a different keyword", () => {
    const result = gradeAnswer("هلیکاز", "لیگاز");
    expect(result.verdict).toBe("INCORRECT");
    expect(result.feedbackState).toBe("jm.o");
  });

  it("flags a near miss for a one-letter typo", () => {
    const result = gradeAnswer("لیگاس", "لیگاز");
    expect(result.verdict).toBe("INCORRECT");
    expect(result.nearMiss).toBe(true);
    expect(result.distance).toBe(1);
  });
});

describe("quantifier trap detector", () => {
  const quantifiers = ["همه", "برخی", "اغلب", "هر"];

  it("rejects a correct body with a broken quantifier", () => {
    const result = gradeQuantifiedStatement(
      "در برخی یاخته‌های یوکاریوتی دنا با هیستون بسته می‌شود",
      "در همه یاخته‌های یوکاریوتی دنا با هیستون بسته می‌شود",
      quantifiers,
    );
    expect(result.quantifierBroken).toBe(true);
    expect(result.verdict).toBe("PARTIAL");
  });

  it("accepts the statement when the quantifier matches", () => {
    const result = gradeQuantifiedStatement(
      "در همه یاخته‌های یوکاریوتی دنا با هیستون بسته می‌شود",
      "در همه یاخته‌های یوکاریوتی دنا با هیستون بسته می‌شود",
      quantifiers,
    );
    expect(result.quantifierBroken).toBe(false);
    expect(result.verdict).toBe("CORRECT");
  });
});
