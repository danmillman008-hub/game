# MISSION 07 — 03 INTERACTIVE LESSON VIEWMODEL AT RUNTIME

**Status:** `VERIFIED_RUNTIME` for observed values, `VERIFIED_STATIC` for
branch structure. Evidence: `TRACES/STAGE4_ONLINE.jsonl` (`entry`/`exit` records
with `this_fields`, `ret_fields`), `ANALYSIS/MISSION_06/EVIDENCE/DISASM/`,
`ANALYSIS/MISSION_07/RUNTIME_TRACE/STATIC_DECODE/00_STATIC_DECODE_M07.md`.

## Real `LessonBundle` (`base/c.K()` exit, verbatim prefix)
```
LessonBundle(lessonId=151410, lessonIndex=0, chapterIndex=0, chapterId=17742,
tutorialId=904, trackId=219, trackVersion=82, tutorialVersion=161,
tutorialIndex=0, tutorialType=Learn, chapterType=PRACTICE_LEVEL_1,
isChapterAlreadyCompleted=false, isLastLesson=false, isPracticeRedo=false,
isChallengeRedo=false, sectionIndex=0, tutorialTitle=Discovering HTM…
```
This is the **first slide lesson** of shipped tutorial 904 (the same tutorial
that contains WebView lesson 151403). It proves the client builds a fully
local lesson bundle from shipped content, with no server response involved.

## Real `LessonProgress` (from `createLessonProgress` / `repo_createProgress`)
```
LessonProgress(lessonId=151410, completedAt=2026-11-05T12:40:04.495Z,
startedAt=2026-11-05T12:39:58.890Z, tries=1, tutorialId=904,
tutorialVersion=161, trackId=219, publishSetVersion=753, attempts=1,
isPracticeProgress=false, inQueue=true)
```
Mapped into the Room row (see `06_DATABASE_BEFORE_AFTER.md`):
`['151410','1793882404495','1793882398890','1','904','161','219','753','1','0','1']`.
`publishSetVersion=753` matches M05's shipped curriculum version. `tries=1`
and `attempts=1` for a **non-interactive slide** — i.e. `isSolvedCorrectly()`
returns `true` for a slide the user merely read and continued past.

## Measured call chain for a non-interactive slide lesson
```
NonInteractiveLessonFragment$goToNextPage$1.invokeSuspend
  -> base/c.U()                    [lessonSolvedAndProceed, this_fields {N: true}]
  -> base/c.H(tries, attempts)    [createLessonProgress]
  -> LessonProgressRepository.createLessonProgress(LessonBundle, …)
       [repo_createProgress, returns the 11-field LessonProgress]
  -> base/c.e0(progress, cont)    [storeProgressInMemory]
  -> LessonProgressQueue.storeLessonProgress(progress, false, true, cont)
  -> LessonProgressQueue.storeLessonProgress(null,    false, false, cont)  x2
  -> base/c.f0(false, true)       [trackLessonResult]  <-- FIRST ARG FALSE
  -> base/c.N()                   [resetInputState]
```
`f0(false, true)` is direct runtime confirmation of M07's bytecode correction:
M06 had reported `f0(true, isSolvedCorrectly())`; both `V()` and `W()` actually
pass `false`. The `true` second argument is `progress.isSolvedCorrectly()`
(`tries=1 >= 1`).

## ViewModel fields observed (`base/c`)
From `resetInputState#111` `this_fields`:
`N = im.b@…`, `O = com.getmimo.ui.lesson.interactive.base.d@…`, `P = true`,
`Q = null`, `R = androidx.lifecycle.m0@…`. From `lessonSolvedAndProceed#87`:
`N = true`. M06 static names these: `N` = `q`/`q1` input-state LiveData holder,
`O` = `P`/`Q` feedback state, `P` = boolean flag, `R` = `androidx.lifecycle.m0`
LiveData for UI feedback. Exact semantic labels remain `INFERRED`; field
existence and types are `VERIFIED_RUNTIME`.

## LiveData values (`androidx.lifecycle.m0.l / k`)
* `java.lang.Boolean` `true` (12:38:30) and `false` (12:38:48) — onboarding /
  lesson loading flags.
* `com.getmimo.ui.authentication.AuthenticationStep` `AuthOverview`,
  `SignupOverview` — auth navigation; the enum's full static field list was
  dumped (`a..x` incl. `LoginOverview`, `LoginSetEmail`, `LoginSetPassword`,
  `SignupSetEmail`, `SignupSetPassword`, `SignupSetUsername`, `Close`).
* No `jm/m`, `jm/n`, `jm/o` feedback object was posted during stage 4: no
  native correct/partial/wrong branch ran. That is a **negative runtime result**,
  recorded as `UNKNOWN` for those branches rather than assumed.

## Feedback branch structure (static, M06 + M07 recheck)
`setupViews$2` @10985684 dispatches exact → `c.V()`, normalised-only →
`c.W()`, mismatch → `c.X()`/`c.d0()`. `V()` and `W()` share the spine
`i0() → C=FALSE → d++ → c0() → tries=(C==TRUE)?0:1 → H(tries,d) → e0() →
sound.a(true) → f0(false, isSolvedCorrectly()) → emit Long(lessonBundle.a) →
I()`. `W()` additionally builds `jm/n(userInput, expectedInput, true, E)` and
logs `validated_input_execution_correct_partial_match`; `V()` builds `jm/m`
and requires `solutionFeedbackCorrect`. `d0()` builds `jm/o` (7 booleans) and
contains **no XP/scoring arithmetic**. Full smali in
`RUNTIME_TRACE/STATIC_DECODE/`.

## Stage 6 — the exact answer-moment hook chain (`VERIFIED_RUNTIME`)
All records below are `13:20:08` in `TRACES/STAGE6_ONLINE.jsonl` (run
`42033599909`, Frida attached at 13:19:50 right at the lesson).

```
entry lessonSolvedAndProceed#1  c.U()  args=[Continuation at
   NonInteractiveLessonFragment$goToNextPage$1.invokeSuspend]  N=true
exit  lessonSolvedAndProceed#1  ret=COROUTINE_SUSPENDED
entry createLessonProgress#2   c.H(1, 1)
entry repo_createProgress#4    LessonProgressRepository.createLessonProgress
   args[0]=LessonBundle(lessonId=151403, lessonIndex=1, chapterIndex=0,
        chapterId=17742, tutorialId=904, trackId=219, trackVersion=82,
        tutorialVersion=161, tutorialIndex=0, tutorialType=Learn,
        chapterType=PRACTICE_LEVEL_1, isChapterAlreadyCompleted=false,
        isLastLesson=false, isPracticeRedo=false, isChallengeRedo=false,
        sectionIndex=0, tutorialTitle=Discovering HTML and Tags, …)
exit  repo_createProgress#4    ret=LessonProgress(lessonId=151403,
        completedAt=2026-11-05T13:20:08.763Z,
        startedAt=2026-11-05T13:19:35.988Z, tries=1, tutorialId=904,
        tutorialVersion=161, trackId=219, publishSetVersion=753,
        attempts=1, isPracticeProgress=false, inQueue=true)
exit  createLessonProgress#2   same LessonProgress, ret_fields include
        $stable=8, inQueue=true, publishSetVersion=753, trackId=219
entry storeProgressInMemory#5 c.e0(progress, Continuation at
        InteractiveLessonBaseViewModel.lessonSolvedAndProceedToNextLesson)
entry queue_store#7  storeLessonProgress(progress, false, true, cont)
entry queue_store#8/#13  storeLessonProgress(null, false, false, cont)
entry isSolved#11  LessonProgress(lessonId=151410, tries=1) -> exit ret=true
entry isSolved#12  LessonProgress(lessonId=151403, tries=1) -> exit ret=true
entry isSolved#14  same row -> exit ret=true
entry lessonSolvedAndProceed#15 c.U() from
        InteractiveLessonBaseViewModel.lessonSolvedAndProceedToNextLesson
        -> exit ret=kotlin.Unit
entry trackLessonResult#17  c.f0(false, true) -> exit ret=undefined
entry resetInputState#26 c.N()  this_fields {N: im.b, O: d, P:false,
        Q:null, R:androidx.lifecycle.m0}
```

This is direct runtime proof that the WebView correct answer is persisted by
the **generic `U()/H(1,1)/e0()` proceed chain** with `tries=1, attempts=1`,
and that `f0` receives `(false, true)` — not by `V()`/`W()`.

### LiveData values at the next (fill-the-gap) lesson, 13:20:09
* `java.lang.Boolean` `true` → `false`
* `com.getmimo.ui.lesson.view.InteractionKeyboardButtonState` `DISABLED`
  (enum `ENABLED / DISABLED / HIDDEN`)
* `jm.g` (input-state holder object)
* `jm.q` = `LessonOutput(outputItems=[], isVisible=false)`
* `com.getmimo.ui.common.runbutton.RunButton$State` `RUN_DISABLED`
  (enum `RUN_ENABLED, RUN_DISABLED, SUBMIT_ENABLED, SUBMIT_DISABLED,
  PROCESSING, CONTINUE_BIG, CONTINUE_DISABLED, NOT_SHOWN`)

No `jm/m`, `jm/n` or `jm/o` value was posted: no native correct/partial/wrong
feedback object was created for the WebView exercise.
