import { levenshtein, normalizeAnswer, similarity } from "./normalize";

export type Verdict = "CORRECT" | "PARTIAL" | "INCORRECT";

export type PartialReason =
  | "ZWNJ"
  | "ARABIC_GLYPH"
  | "DIGITS"
  | "SPACING"
  | "PUNCTUATION"
  | "CASE"
  | "DIACRITICS";

export interface GradeResult {
  verdict: Verdict;
  normalizedInput: string;
  normalizedExpected: string;
  /** Machine feedback state, mirroring Mimo 9.35 resources jm.m / jm.n / jm.o */
  feedbackState: "jm.m" | "jm.n" | "jm.o";
  partialReason?: PartialReason;
  nearMiss: boolean;
  distance: number;
  /** Persian coaching message shown to the learner. */
  messageFa: string;
}

const PARTIAL_MESSAGES: Record<PartialReason, string> = {
  ZWNJ: "نزدیک بود! فقط نیم‌فاصله (ZWNJ) جابه‌جا شده است. شکل صحیح کتاب را ببین.",
  ARABIC_GLYPH: "درست است، اما «ی/ک» را با حرف عربی (ي/ك) تایپ کرده‌ای. در کنکور فقط شکل فارسی معیار است.",
  DIGITS:
    "پاسخ درست است ولی عددها با رقم فارسی/عربی نوشته شده‌اند. رقم لاتین همان مقدار است؛ همین را حفظ کن.",
  SPACING: "فقط فاصله‌گذاری فرق دارد. کلیدواژه درست انتخاب شده است.",
  PUNCTUATION: "پاسخ صحیح است؛ فقط نشانه‌گذاری اضافه یا کم شده است.",
  CASE: "پاسخ صحیح است؛ فقط بزرگی و کوچکی حروف لاتین متفاوت است.",
  DIACRITICS: "پاسخ صحیح است؛ اعراب اضافه شده است.",
};

function detectPartialReason(rawInput: string, rawExpected: string): PartialReason {
  if (/[يك]/.test(rawInput) && !/[يك]/.test(rawExpected)) return "ARABIC_GLYPH";
  if (/[۰-۹٠-٩]/.test(rawInput) !== /[۰-۹٠-٩]/.test(rawExpected)) return "DIGITS";
  if (/[\u064b-\u065f]/.test(rawInput)) return "DIACRITICS";
  const squeeze = (text: string) => text.replace(/[\s\u200c]+/g, "");
  if (rawExpected.includes("\u200c") && squeeze(rawInput) === squeeze(rawExpected)) return "ZWNJ";
  if (rawInput.replace(/\u200c/g, "") === rawExpected.replace(/\u200c/g, "")) return "ZWNJ";
  if (squeeze(rawInput) === squeeze(rawExpected)) return "SPACING";
  if (rawInput.toLowerCase() !== rawInput || rawExpected.toLowerCase() !== rawExpected) return "CASE";
  return "PUNCTUATION";
}

/**
 * Mimo 9.35 three-way verdict rule (`04_SPEC_INTERACTION_AND_GRADING.md` §3),
 * extended with Persian canonicalisation and actionable near-miss coaching.
 */
export function gradeAnswer(input: string, expected: string): GradeResult {
  const rawInput = input.trim();
  const rawExpected = expected.trim();

  const normalizedInput = normalizeAnswer(rawInput);
  const normalizedExpected = normalizeAnswer(rawExpected);
  const distance = levenshtein(normalizedInput, normalizedExpected);
  const nearMiss =
    normalizedInput !== normalizedExpected && similarity(normalizedInput, normalizedExpected) >= 0.7;

  if (normalizedInput !== normalizedExpected) {
    return {
      verdict: "INCORRECT",
      normalizedInput,
      normalizedExpected,
      feedbackState: "jm.o",
      nearMiss,
      distance,
      messageFa: nearMiss
        ? "خیلی نزدیک بود! یک یا دو حرف/کلمه جابه‌جا شده است؛ جملهٔ کتاب را دوباره بخوان و اصلاح کن."
        : "پاسخ با متن کتاب تطابق ندارد. کلیدواژهٔ دقیق کتاب را پیدا کن و دوباره تلاش کن.",
    };
  }

  if (rawInput === rawExpected) {
    return {
      verdict: "CORRECT",
      normalizedInput,
      normalizedExpected,
      feedbackState: "jm.m",
      nearMiss: false,
      distance: 0,
      messageFa: "کاملاً مطابق متن کتاب. آفرین!",
    };
  }

  const reason = detectPartialReason(rawInput, rawExpected);
  return {
    verdict: "PARTIAL",
    normalizedInput,
    normalizedExpected,
    feedbackState: "jm.n",
    partialReason: reason,
    nearMiss: false,
    distance: 0,
    messageFa: PARTIAL_MESSAGES[reason],
  };
}

/**
 * Quantifier-aware predicate grading: the Konkur trap is swapping «همه»
 * with «برخی» or «هرگز». A correct fact with a broken quantifier is a trap hit,
 * never a CORRECT answer.
 */
export function gradeQuantifiedStatement(
  input: string,
  expected: string,
  quantifiers: readonly string[],
): GradeResult & { quantifierBroken: boolean } {
  const base = gradeAnswer(input, expected);
  const found = quantifiers.filter((q) => normalizeAnswer(input).includes(normalizeAnswer(q)));
  const expectedQ = quantifiers.filter((q) => normalizeAnswer(expected).includes(normalizeAnswer(q)));

  const strip = (text: string) =>
    quantifiers
      .reduce((acc, q) => acc.split(q).join(" "), normalizeAnswer(text))
      .replace(/\s+/g, "");

  const bodiesMatch = strip(input) === strip(expected);
  const quantifierBroken =
    expectedQ.length > 0 &&
    !expectedQ.some((q) => found.includes(q)) &&
    (base.verdict === "CORRECT" || bodiesMatch);

  if (quantifierBroken) {
    return {
      ...base,
      verdict: "PARTIAL",
      feedbackState: "jm.n",
      quantifierBroken: true,
      messageFa:
        "بدنهٔ گزاره درست است اما قید آن با کتاب نمی‌خواند. طراح کنکور دقیقاً از همین قید (همه/برخی/اغلب) گزینهٔ تله می‌سازد.",
    };
  }

  return { ...base, quantifierBroken: false };
}

export function isPassVerdict(verdict: Verdict): boolean {
  return verdict === "CORRECT" || verdict === "PARTIAL";
}
