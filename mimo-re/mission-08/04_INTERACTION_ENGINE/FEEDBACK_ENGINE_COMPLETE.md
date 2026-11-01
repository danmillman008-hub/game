# Phase 4.5 — Feedback engine

## 1. Three feedback states, three types

| State type | Shape | Emitted by | Meaning |
|---|---|---|---|
| `jm.m(CharSequence, Z, Z)` | text + 2 flags | `base.c.V` (`lessonSolvedCorrectly`) | correct feedback |
| `jm.n(String user, String expected, Z, Z)` | both inputs + 2 flags | `base.c.W` | partial-match feedback |
| `jm.o(CharSequence, Z×6)` | text + 6 flags | `base.c.d0` (`showWrongFeedbackBlock`) | wrong feedback (hint/solution/retry gates) |

Each is written to its own `MutableStateFlow` (`q`, `r`-family, `t`), so the three cannot be shown simultaneously by
accident: emitting one does not clear the others, which is why `base.c.M()` exists.

## 2. `M()` — the reset

`M()` resets all three states (`jm.m.b`, `jm.n.b`, `jm.o.b` defaults) and calls `jw.p.b()`. It is called by the
fragment's `onViewCreated$18`, by the selection/validated-input view-models (`a0`, `a.a`), and by `c.a0`. It is the
engine's "show no feedback" transition.

## 3. Wrong-feedback path (`d0`, 148 insns) — the most interesting one

```text
emit jm.o (copy with flags) to flow q
analytics name check "solutionFeedbackWrong"
read data.local.a.f()      // hasSeenHardModeTutorIntro  (Stage-1 HIGH mapping)
if (flag was absent && hard mode) data.local.a.p()      // write the intro-shown flag
P()                        // isAiTutorUnlimited (91 insns, error string for AI-tutor state)
build new jm.o(text, 6 booleans) and emit
```
So the **wrong answer is the trigger for the AI-tutor nudge** (the "tutor intro" preference is consumed exactly
here), and the AI-tutor availability is resolved inline. That is a behavioural coupling no name could have told us.

## 4. Correct path (`V`)

```text
C := false                       // boxed Boolean flag cleared
c0()                             // reset feedback UI (jm.q(list, flag))
progress = H(d, d)               // LessonProgress
e0(progress)                     // persist
emit jm.m(...)                   // correct feedback state
sound.a(false)                   // success sound, gated by "enable_sound_effects"
f0(false, progress.isSolvedCorrectly())   // analytics lesson-completed event
emit lesson id to flow h
I()                              // code-view action button state
```

## 5. Partial path (`W`)

Same as correct, except: `jm.n(userInput, expected)` is emitted, and an analytics event is recorded with
`validated_input_execution_correct_partial_match` and the two `StringProperty` entries `user_input` and
`expected_user_input`. That is a genuine analytics event (built through `analytics.a.o(be.x3)`), unlike the
`solutionFeedbackCorrect`/`Wrong` literals which are Kotlin null-check *names* (correction **C-14**).

## 6. Hints, solutions, retry

`jm.o`'s six booleans are the carriers; which one means "hint" cannot be decided from the constructor alone — the
argument order is not recoverable from the dex. Recorded as question **A22**. What *is* proven:

* retry does not create a new attempt object: `M()` only resets feedback state, so a retry keeps the same
  `LessonProgress` until the next `H()` call;
* "proceed to next lesson" is a separate method (`U`) from "correct" (`V`), so a correct answer can be confirmed
  without advancing.

## 7. Timing and animation

`jw.p.b()` is called on reset and in `M()`; `base.c.Z` delays before dispatching a verdict (`kotlinx.coroutines.a.g`).
The feedback block is therefore shown **after** a suspension point, not synchronously with the tap. The concrete
duration was not read.
