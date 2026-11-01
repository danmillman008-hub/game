# Mission 5 — Lesson Runtime Specification (interactive lessons)

## Scope
The behaviour of an interactive lesson at runtime: the state machine, the submission pipeline, the
timing, what is persisted when, what is emitted as analytics, and how per-interaction-type view
models plug into one shared base. Executable (code) lessons are covered only where they share the
base class.

## Method
Read the shared base view model `com.getmimo.ui.lesson.interactive.base.c` (1,231 lines of DAD
pseudo-Java) in full at the instruction level, then every per-type view model
(`fillthegap.a`, `validatedinput.a/b`, `selection.a`, `spell.a`, `qm.d`), then the two fragments that
own the verdict lambdas. Method bodies were cross-checked against string literals, field types and
second call sites; no claim below rests on a single decompiled line.

## Sources
| Evidence | Symbol |
|---|---|
| Shared base VM | `com.getmimo.ui.lesson.interactive.base.c` |
| Per-type VMs | `fillthegap.a`, `selection.a`, `spell.a`, `validatedinput.a/b`, `qm.d` |
| Verdict lambdas | `InteractiveLessonBaseViewModel$onValidatedInputExecuted$1`, `InteractiveLessonValidatedInputFragment$setupViews$2` |
| Progress sink | `com.getmimo.data.source.remote.progress.LessonProgressRepository` |
| Analytics sink | `th.b.a`, `com.getmimo.analytics.*` |

## Findings

### 1. State machine (VERIFIED_STATIC)
The base VM holds the whole lesson state in five load-bearing fields:
| Field | Meaning | Evidence |
|---|---|---|
| `d` (int) | **attempts**: incremented on *every* submission | `d++` in all three terminals |
| `C` (Boolean) | "the previous attempt was incorrect" | set `FALSE` in success path, `TRUE` in failure path |
| `E` | redundant-reset guard gating `c0()` | read before reset |
| `h` | one-shot "solved" event stream | emitted on success |
| `S` (subclass) | current raw user input (`qm.d.S`) | assigned before grading |

Terminals:
```
success      U():  tries = (C != true) ; d++ ; H(tries, d) ; repo.markSolved(lessonId) ; f0(0, 1) ; emit solved
success-part W():  b0(expectedInput)   ; d++ ; c0() ; H(1, d)
success(v2)  V():  C = false          ; d++ ; c0() ; H(1, d)
failure      X():  d++ ; C = true ; H(0, d) ; c0() ; d0()
```
`U()` is the "proceed / next" terminal and is the only one that derives `tries` from `C`; the three
`V/W/X` terminals fire *at verdict time*. Consequence: **`tries` is 0 whenever the learner's most
recent submission before proceeding was wrong, and 1 only if the last submission was right.**

### 2. Submission pipeline (VERIFIED_STATIC)
1. A user gesture produces a typed event (`iq.w` sealed family).
2. `Z(result)` dispatches the verdict. For validated input the dispatch is wrapped in
   `delay(300)` — a deliberate 300 ms pause between submission and feedback
   (`kotlinx.coroutines.delay(300)` in `onValidatedInputExecuted`).
3. Dispatch table: `qm.e` → `V()` (correct), `qm.f` → `b0(h)` + `W()` (partial), `qm.g` → `X()`
   (incorrect). Any other subtype throws `NoWhenBranchMatchedException` — the sealed set is closed.
4. After the terminal, the VM pushes the attempt counter into the tracking field
   (`this.e.l(Integer.valueOf(this.K().b))`) and clears the "in-flight" flag (`v2.k(FALSE)`).

### 3. Progress persistence (VERIFIED_STATIC)
`H(tries, attempts)` → `LessonProgressRepository.createLessonProgress(bundle, startedAt, tries, attempts)`
→ 12-argument `LessonProgress` constructor:
```
(lessonId, completedAt=now, startedAt, tries, tutorialId, tutorialVersion,
 trackId, publishSetVersion, attempts, isPracticeProgress, inQueue=1)
```
Call sites of `H(...)`: `base.c:557, 661, 710, 773, 834` and `interactive/d:141, 151`.
On first entry into a lesson the VM writes an initial row `H(0, 0)` when the first-visit flag holds —
so a lesson that is opened and abandoned is recorded with `tries = 0, attempts = 0`.
`publishSetVersion` comes from the tracks repository at write time, not from the lesson payload.
A guard warns when `completedAt < startedAt` (clock-skew defence).

### 4. Analytics emitted by the runtime (VERIFIED_STATIC)
| Trigger | Emitter | Properties |
|---|---|---|
| every submission | `f0(interactionType, isSolvedCorrectly)` → `th.b.a(bundle, lessonType, d, I, c, p14, p15, trackingField, E)` | attempts count, interaction type, solved flag, tracking field |
| lesson restart | `a0()` → `lesson_reset` | `lesson_id, attempt, tutorial_id, tutorial_version, track_id, attempts, duration` |
| interaction deleted | `g0()` → `lesson_interaction_delete` | interaction identity |

The property *names* above come from `a0()`'s map construction (string literals read at the call
site); the event names `lesson_reset` / `lesson_interaction_delete` are literals in the same method.

### 5. Per-type behaviour differences (VERIFIED_STATIC)
| Type | Verdict source | Notable detail |
|---|---|---|
| `ValidatedInput` | `qm.d.E()` builds `qm.h(answer, prefix, suffix)` with `max(0,start)`/`min(end,len)` clamping; fragment compares | 300 ms delay; three-way verdict |
| `FillTheGap` | `fillthegap.a` builds slot list from `option.c/.d`; correct option gets `SpannableStringBuilder(source, c, d)` | distractor labels render plain |
| `Selection` | `selection.a` slices `source` around the interaction offsets into `qc.a` segments, wraps in `nm.e` | selection state keeps two parallel lists (`v0_1.a`, `v0_1.c`) |
| `Spell` | `spell.a` mirrors fill-the-gap but with `Interaction$Spell` and `pm.f` state | same slot slicing |
| `NoInteraction` | `nointeraction.a` | degrades to a plain code block |

### 6. Module visibility drives feedback text (VERIFIED_STATIC)
`initialiseViewModel` picks the **first `Paragraph` module** as the feedback candidate and stores it
in `s`/`t`. The wrong-answer feedback is built from the `WRONG`-visible paragraph
(`ModuleVisibility.e`), and correct feedback from `CORRECT`. `jm.o` carries the wrong-answer feedback
object, `jm.m` the paragraph feedback `(text, 0, 0, …)`. Therefore a lesson without a
`visible-if="wrong"` paragraph has no targeted wrong-answer explanation — this is a *content*
contract, not a runtime fallback.

## Evidence labels
- State machine, terminals, persistence call shape, 300 ms delay, sealed verdict set, analytics
  properties: **VERIFIED_STATIC**.
- "300 ms is user-perceptible feedback pacing": **INFERRED_HIGH** (intent not stated in code).
- Nothing in this document is **VERIFIED_RUNTIME**: the app was never executed (no device/emulator).

## Limitations
- DAD collapses some locals; the *ordering* of `d++` relative to `H(...)` was confirmed by reading
  both the increment and the constructor-argument load in the same basic block, but a smali-level
  confirmation is impossible here (no baksmali). Register `U-04`.
- Interstitial/ad surfaces between lessons were not traced.

## Unresolved
- Whether `U()` is reachable without any prior `V/W/X` (i.e. "skip" path) — one call site suggests a
  skip exists but its guard was not resolved. Register `U-05`.
- The exact retry policy (does a wrong answer replay the same interaction instance?) is
  content-driven and was not traced end-to-end. Register `U-06`.

## Reproduction
Read in this order: `base.c` → `validatedinput/…Fragment$setupViews$2` → `qm.d.E()` →
`qm.i.a()` → `LessonProgressRepository.createLessonProgress`. All under `/tmp/dad` after running
`tools/decompile_apk.py` (see `01_TOOLCHAIN_AND_ENVIRONMENT/`).
