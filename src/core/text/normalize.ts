/**
 * LAYER 1 — Pure domain core (no DOM, no React, no server deps).
 * Persian-aware normalisation that closes `Q-44` from the Mimo 9.35 reverse-engineering.
 */

const ZERO_WIDTH = /[\u200b\u200d\u200e\u200f\u202a-\u202e\u2060\ufeff]/g;
const ZWNJ = /\u200c/g;
const DIACRITICS = /[\u064b-\u065f\u0670\u06d6-\u06ed]/g;
const TATWEEL = /\u0640/g;

const PERSIAN_DIGITS = "۰۱۲۳۴۵۶۷۸۹";
const ARABIC_DIGITS = "٠١٢٣٤٥٦٧٨٩";

/** Canonical surface form of Persian text: one glyph per phoneme, ZWNJ preserved. */
export function canonicalizeFa(input: string): string {
  let out = input
    .replace(ZERO_WIDTH, "")
    .replace(DIACRITICS, "")
    .replace(TATWEEL, "")
    .replace(/ي/g, "ی")
    .replace(/ك/g, "ک")
    .replace(/ة/g, "ه")
    .replace(/ۀ/g, "ه")
    .replace(/[أإآ]/g, "ا")
    .replace(/[۰-۹]/g, (d) => String(PERSIAN_DIGITS.indexOf(d)))
    .replace(/[٠-٩]/g, (d) => String(ARABIC_DIGITS.indexOf(d)));

  out = out
    .replace(/[ \t\u00a0]+/g, " ")
    .replace(/\s*\n\s*/g, "\n")
    .trim();

  return out;
}

/**
 * The exact key used by the grader (`qm.i.a` + Persian layer):
 * lowercase, ZWNJ dropped, digits unified, only letters/numbers kept.
 */
export function normalizeAnswer(input: string): string {
  const canonical = canonicalizeFa(input).toLowerCase().replace(ZWNJ, "");

  let out = "";
  for (const ch of canonical) {
    if (/[\p{L}\p{N}]/u.test(ch)) out += ch;
  }
  return out;
}

export function stripZwnj(input: string): string {
  return input.replace(ZWNJ, "");
}

/** Levenshtein distance on code points (small strings only). */
export function levenshtein(a: string, b: string): number {
  const s = Array.from(a);
  const t = Array.from(b);
  if (s.length === 0) return t.length;
  if (t.length === 0) return s.length;

  let prev = Array.from({ length: t.length + 1 }, (_, i) => i);
  for (let i = 1; i <= s.length; i++) {
    const curr = [i];
    for (let j = 1; j <= t.length; j++) {
      const cost = s[i - 1] === t[j - 1] ? 0 : 1;
      curr[j] = Math.min(prev[j] + 1, curr[j - 1] + 1, prev[j - 1] + cost);
    }
    prev = curr;
  }
  return prev[t.length];
}

export function similarity(a: string, b: string): number {
  const na = normalizeAnswer(a);
  const nb = normalizeAnswer(b);
  if (!na.length && !nb.length) return 1;
  const distance = levenshtein(na, nb);
  return Math.max(0, 1 - distance / Math.max(na.length, nb.length));
}
