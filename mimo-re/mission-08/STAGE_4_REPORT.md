# Mission 8 — Stage 4 Report (interaction engine and grading)

**Status:** `substantially_complete` (15/15 deliverables + 15 semantic tests) · **Base:** Stage 3 `7e75056` · **2026-11-01**

## What was actually read

Method bodies, not names: `V` (162 insns), `W` (202), `X` (113), `Y` (31), `Z` (31), `d0` (148), `M` (60), `h0` (14),
`H`, `I`, `c0`, `K`, `f0`; `qm.i.<clinit>` + `qm.i.a`; `qm.d.E` (207); `qm.d.j0`;
`InteractiveLessonValidatedInputFragment$setupViews$2` (75); `InteractiveLessonBaseViewModel$onValidatedInputExecuted$1`
(144); the six per-type graders `im.d.E0` (200), `nm.b.E0` (177), `pm.b.E0` (148), `km.c.E0`/`om.d.E0` (97 each),
`mm.b.E0` (15); plus `selection.a` in full.

## The five results that matter

1. **The normaliser is decrypted.** `qm.i.a` = lowercase(`Locale.US`) + keep `isLetterOrDigit` + keep only
   `< > ( ) : { } , .`. Nine characters, no regex, no locale table.
2. **The validated-input verdict is a three-way rule**: normalise both sides → unequal = incorrect (`qm.g`);
   equal-normalised but unequal-raw = **partial** (`qm.f`, the only partial site in the app); equal both = correct
   (`qm.e`). Dispatch is a `when` over exactly those three types (`else` throws `NoWhenBranchMatchedException`).
3. **Every other interaction is boolean**: selection (count equality + flag-wise), fill-the-gap and spell
   (size equality + index-wise text), multiple/single choice (`km.f.b`). So **partial feedback is reachable only from
   validated input** — a structural fact of the code, not a policy.
4. **Grading is client-side everywhere** in the interactive lesson. No network call exists in any grading path.
5. **`ModuleVisibility` is `{ALWAYS, CORRECT, WRONG}`** — verdict-dependent rendering. `Selection` cannot be gated
   because its model has no visibility field and `te.e`'s vocabulary has no `visible-if`; the graded module is
   structurally always visible.

## Feedback engine

Three state types (`jm.m` correct, `jm.n` partial, `jm.o` wrong with six flags), each on its own flow, reset by `M()`.
The wrong path (`d0`) reads `data.local.a.f()` (`hasSeenHardModeTutorIntro`) and writes back through `data.local.a.p()`
and resolves `isAiTutorUnlimited()` inline — the wrong answer is the AI-tutor trigger.

## Completion semantics

`LessonProgress.isSolvedCorrectly()` is `tries >= 1` (body read). `tries` is the success counter, `attempts` the total;
completion is decided by `tries`.

## Corrections and new technique

* **C-14** — `solutionFeedbackCorrect` / `solutionFeedbackWrong` are **Kotlin null-check property names**, not
  analytics events (Stage 3 had recorded them as event names). The one real analytics event in this area is
  `validated_input_execution_correct_partial_match` with `user_input` and `expected_user_input`.
* New recovery channel documented in `PROPERTY_NAME_RECOVERY.md`: `checkNotNullExpressionValue` literals leak original
  property names (`lessonBundle`, `browserOutputDeferred`, `interactiveLessonContent`, `codePlaygroundController`, …).

## Limits

Eight items remain open (A21–A28) with named blockers: `jm.o` flag order, partial-vs-`WRONG` visibility, the verdict
delay, `mm.b` pass-through reachability, `Output` runtime producers, the `browserOutputDeferred` consumer, the
multiple-vs-single-choice trigger, and `qm.f` reachability from executable lessons. Nothing here is claimed as runtime.
