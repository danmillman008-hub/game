# Mission 5 — Assessment and Evaluation Specification

## Scope
Exactly how each interaction type decides "correct", what tolerance is applied, how partial credit is
represented, and what is recorded per attempt. This is the domain where Mimo's behaviour is most
commonly mis-described, so every rule below is traced to a specific comparison site.

## Method
Located the comparison sites by following the sealed verdict family (`iq.w` → `qm.e`/`qm.f`/`qm.g`)
from its producers. Read the producer lambdas instruction by instruction, then read the normaliser
they call. Cross-checked the three-way verdict against the base VM dispatch table.

## Sources
| Rule | Symbol |
|---|---|
| Validated-input grading | `InteractiveLessonValidatedInputFragment$setupViews$2.invokeSuspend` |
| Normaliser | `qm.i.a(String)` + `qm.i.<clinit>` |
| Verdict types | `qm.e` (Correct), `qm.f` (CorrectPartialMatch(userInput, expectedUserInput)), `qm.g` (Incorrect) |
| Dispatch | `InteractiveLessonBaseViewModel$onValidatedInputExecuted$1` → `V()/W()/X()` |
| Option correctness | `Option.a` (boolean), read by `fillthegap.a`, `selection.a`, `spell.a` |

## Findings

### 1. Validated input — the exact algorithm (VERIFIED_STATIC)
```
userInput = vm.S                       // raw text typed by the learner
expected  = state.a                    // source slice [max(0,start), min(end,len)) of <content>
normalizedEqual = normalize(userInput) == normalize(expected)
exactEqual      = userInput == expected
verdict = when {
    normalizedEqual &&  exactEqual -> Correct                    (qm.e)
    normalizedEqual && !exactEqual -> CorrectPartialMatch(...)   (qm.f)
    else                           -> Incorrect                  (qm.g)
}
```
### 2. The normaliser (VERIFIED_STATIC — full body read)
```
normalize(s) = s.toLowerCase(Locale.US).filter { c -> Character.isLetterOrDigit(c) || c == '<' || c == '.' }
```
The kept punctuation set is `{'<', '.'}` exactly (the `Character` values `> ( ) : { } ,` are
constructed in `<clinit>` but **not** placed in the retained list). Effects:
- case-insensitive;
- every space, newline, tab, comma, colon, bracket, quote, `+`, `-`, `=` is **discarded**;
- `<` and `.` are preserved, so `a<b` and `a < b` normalise differently from `ab`, while
  `foo.bar` vs `foo . bar` compare equal.

### 3. Partial credit semantics (VERIFIED_STATIC)
`CorrectPartialMatch` carries both strings and is routed to `W()` — the *success-with-correction*
terminal: the VM first overwrites the answer field with the expected text (`b0(expected)`) and then
records a success with `tries = 1`. So a normalised-only match:
- counts as **solved** (progress row gets `tries = 1`),
- is **not** counted as first-try-perfect if `attempts > 1`, and
- is visible to the learner as "this is the exact form we expected".
Labelled VERIFIED_STATIC for the control flow; the *product intent* ("accept sloppy spacing") is
INFERRED_HIGH.

### 4. Option-based types (VERIFIED_STATIC)
`FillTheGap`, `Selection` and `Spell` all grade on `Option.a` — a boolean carried in the parsed
content. There is no string comparison, no fuzzy matching and no synonym list for these types.
Correctness therefore depends entirely on the authored `correct` flag; a lesson whose option text
differs from the source slice is still graded correct (the flag wins).

### 5. Attempt accounting (VERIFIED_STATIC)
- `attempts` (`d`) increments on every submission, on success **and** failure.
- `tries` is **not** a counter: it is written as 1/0 depending on the last submission's verdict
  (`isSolvedCorrectly() { return this.tries >= 1; }`).
- "First try" is therefore defined as `isSolvedCorrectly() && attempts == 1`, which is exactly how
  `LessonProgressQueue.getCorrectLessonsFirstTryCount` filters
  (`if (p.isSolvedCorrectly() && p.getAttempts() == 1)`).

### 6. Timing (VERIFIED_STATIC)
Validated input defers the verdict by `delay(300)` ms; option-based types grade immediately on tap.
No other artificial latency was found in the grading path.

### 7. What is *not* assessment
No spaced-repetition scheduler, no mastery estimation, no item difficulty weighting and no
distractor-level analytics were found in the grading path. Mission-04's "mastery" language is not
supported by these code paths; see `22_FINAL_AUDIT/`.

## Evidence labels
- Normaliser body, comparison order, verdict routing, `Option.a` reliance, counters: **VERIFIED_STATIC**.
- "Partial match is intended as tolerance for formatting sloppiness": **INFERRED_HIGH**.
- Any claim about how the *server* scores progress: **UNKNOWN** (backend not observable).

## Limitations
- Only the interactive lesson path was traced. Executable (code-run) grading depends on the remote
  code executor (`/v1/code/runfiles` → `CodePlaygroundExecutionResponse`) and is out of scope here;
  its correctness semantics live server-side → **UNKNOWN**.
- Spell-type grading may additionally consult a dictionary in a path not reached from the traced
  lambdas; no dictionary resource was found, so this is recorded as a *negative* finding, not proof.

## Unresolved
- Spell: is `Option.a` really the only signal (no spell-check)? Registering as `U-07` with the
  evidence we have (no dictionary, no edit-distance code in the traced path).
- Whether `attempts` resets when a lesson is restarted via `lesson_reset`. Register `U-08`.

## Reproduction
```bash
sed -n '1,60p'  /tmp/dad/com.getmimo.ui.lesson.interactive.validatedinput.InteractiveLessonValidatedInputFragment\$setupViews\$2.java
sed -n '1,40p'  /tmp/dad/qm.i.java
sed -n '20,90p' /tmp/dad/com.getmimo.ui.lesson.interactive.base.InteractiveLessonBaseViewModel\$onValidatedInputExecuted\$1.java
```
