# Spec 104 — Grading and Feedback

## MUST
1. Four interaction kinds: FILL_THE_GAP, SELECTION, SPELL, VALIDATED_INPUT.
2. Expected answer = `content[startIndex, endIndex)`; no answer lists, no regex, no alternatives.
3. Two-phase compare: exact → CORRECT; normalised → CORRECT (+ overwrite input with expected); else INCORRECT.
4. Normalisation = lowercase, keep `[a-z0-9<.]` only.
5. Increment `attempts` on every submit; set `tries = 1` on proceed if the last verdict was correct else `0`.
6. Delay 300 ms before verdict for VALIDATED_INPUT only.
7. Feedback text comes from `visible-if="correct"/"wrong"` paragraphs of the same lesson.
8. Never reveal the expected answer on an incorrect verdict.

## MUST NOT
- Add scoring, partial credit, pass thresholds, hint counters, or lives consumption.
- Block retries.

## GIVEN EVIDENCE
`04_INTERACTION_AND_GRADING/25..31`, `qm.i`, `base.c`.

## UNSPECIFIED
Unicode/diacritic behaviour (filter drops them — a known hazard), trimming before phase 1.
