# 06 — Interaction and grading (definitive specification)

## 1. Interaction types

9 UI interaction types map onto 4 content types (`04_INTERACTION_ENGINE/INTERACTION_CLASS_MAP.csv`):

Selection · FillTheGap · Spell · ValidatedInput · MultipleChoice · SingleChoice · Reveal · WebView · Table.

## 2. Normalisation — `qm.i.a(String)`

```text
s.toLowerCase(Locale.US)
keep: letters (isLetterOrDigit), digits, and the characters  < > ( ) : { } , .
drop: whitespace, " ' ; = [ ]  and every other symbol
```

Consequences (documented as behaviour, not as a defect):

* `=` and `;` inside code answers are stripped, so `a = 1;` and `a 1` normalise identically;
* non-Latin answers normalise to the empty string (`Q-44` closed) — the app is Latin-answer based;
* the kept punctuation is exactly what code-ish answers need: `<>` (generics/compare), `()` (calls), `{}` (blocks),
  `:` `,` `.` (syntax).

## 3. Verdicts

| Content type | Predicate | Partial? |
|---|---|---|
| ValidatedInput | `norm(input) != norm(expected)` → INCORRECT; raw equality → CORRECT; else `qm.f` PARTIAL | **yes** |
| Selection | boolean set/choice equality | no |
| FillTheGap | per-gap equality, all-or-nothing | no |
| Spell | exact equality after normalisation | no |
| MultipleChoice | criteria over the chosen set (`pm.b.E0`) | no |
| SingleChoice | single-item predicate (`km.c.E0`) | no |
| Reveal / Table / WebView | none (informational) | no |

`qm.f` has one construction site, on the validated-input path (`A25`).

## 4. Feedback

| State | Constructor | Consumed by |
|---|---|---|
| correct | `jm.m` | CORRECT-gated modules, ALWAYS modules |
| partial | `jm.n` | partial affordances only (not WRONG-gated) |
| wrong | `jm.o` | WRONG-gated modules, ALWAYS modules |

`jm.o` takes six booleans (hint/solution/retry/tutor candidates); argument order is not recoverable, so two of six are
attributed with confidence (`A22`, partially closed). `solutionFeedbackCorrect/Wrong` are **property names**, not
analytics events (correction C-14).

## 5. Attempt accounting

`d` (session attempts) increments on **every** submission path (`V/W/X/U`) before the entity is built; `tries` records
only the solved flag. Nothing resets `d` except a new view-model instance. A reset does not touch the persisted row
(`Q-08`, closed).

## 6. Edge cases that are decided

* answering correctly twice: second submission writes `tries = 0` because `C` is already false-negative — the row keeps
  "solved" only via the earlier write (`tries >= 1` already true);
* empty answer after normalisation (e.g. only symbols): compares equal to an empty expected value → CORRECT;
* wrong-then-correct in one session: `tries = 1` on the correcting submission, `attempts = 2`.

## 7. Evidence and tests

`04_INTERACTION_ENGINE/` (16 files) plus `tests/test_interaction_semantics.py` (15 tests) pin the normaliser character
set, the three-way verdict and the feedback routing. Those tests are re-run in this mission and pass.
