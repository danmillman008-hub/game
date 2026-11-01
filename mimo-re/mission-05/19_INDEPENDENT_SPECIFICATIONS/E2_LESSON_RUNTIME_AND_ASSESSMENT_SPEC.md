# E2 — Lesson Runtime and Assessment Specification (independent)

## Scope
Normative behaviour for executing an interactive lesson: state, submission, verdict, feedback timing,
attempt accounting and visibility-driven feedback selection.

## Method
Reduced from `05_LESSON_RUNTIME/RUNTIME_SPEC.md` and `06_ASSESSMENT_AND_EVALUATION/ASSESSMENT_SPEC.md`
to testable requirements.

## Sources
`05_LESSON_RUNTIME/RUNTIME_SPEC.md`, `06_ASSESSMENT_AND_EVALUATION/ASSESSMENT_SPEC.md`.

## Findings (normative requirements)
- **E2-R-1** The runtime keeps, per lesson: `attempts` (monotonic within a session), `lastVerdict`
  (correct | partial | incorrect), and the current raw input.
- **E2-R-2** `attempts` increments on **every** submission, including correct ones.
- **E2-R-3** The recorded *solved* flag is **1 if and only if the most recent verdict before leaving
  the lesson was correct or partial**; otherwise 0. It is a flag, not a counter.
- **E2-R-4** *First-try success* is `solved && attempts == 1`.
- **E2-R-5** Validated-input grading is three-way:
  `exact` → correct; `normalised-equal but not exact` → correct-with-correction; else incorrect.
- **E2-R-6** Normalisation is: lowercase (locale-independent, US rules), then keep only
  letters, digits, `<` and `.`; discard everything else. Whitespace, punctuation and case are therefore
  insignificant, while `<` and `.` remain significant.
- **E2-R-7** A corrected match must overwrite the learner's input with the expected text and be
  recorded as solved.
- **E2-R-8** Option-bearing interactions grade solely on the authored correctness flag; no string
  comparison, no synonyms.
- **E2-R-9** Validated-input verdicts are applied after a 300 ms delay; option-bearing verdicts apply
  immediately.
- **E2-R-10** Feedback text is selected from paragraph modules by visibility: the `correct`-visible
  paragraph for correct verdicts and the `wrong`-visible paragraph for incorrect ones; the first such
  paragraph wins.
- **E2-R-11** The verdict type set is closed: an implementation must not invent a fourth outcome.

## Test vectors (synthetic, no Mimo content)
| expected | input | verdict |
|---|---|---|
| `print("hi")` | `print("hi")` | correct |
| `print("hi")` | `print ("hi")` | corrected (normalisation strips the space and quotes) |
| `print("hi")` | `print('hi')` | corrected (quote characters are discarded by E2-R-6) |
| `a.b` | `a . b` | corrected |
| `a<b` | `a<b` vs `ab` | **not** equal — `<` is retained |
| `[1,2]` | `[1, 3]` | incorrect |

## Evidence labels
E2-R-1…R-11: **VERIFIED_STATIC**. The test vectors are **synthetic fixtures** derived from the
normaliser definition, not captured app behaviour.

## Limitations
Executable (code-run) lessons grade remotely; no requirement can be stated for them beyond "the verdict
arrives with the execution response" (**UNKNOWN**).

## Unresolved
`U-05` skip path, `U-06` retry semantics, `U-07` spell dictionary, `U-08` whether `attempts` resets on
restart.

## Reproduction
Implement E2-R-5/R-6 and run the vectors above; every row must match.
