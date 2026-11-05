# MISSION 07 — 15 RECONSTRUCTION: FROM AN ANSWER TO PERSISTED STATE

**Scope statement:** this is a **partial, evidence-bounded** reconstruction.
Everything below marked `VERIFIED_RUNTIME` was measured on the original app;
`VERIFIED_STATIC` comes from M06/M07 DEX analysis; everything else is
`UNKNOWN`. No server logic is reconstructed. `SERVER CONFIRMED = 0`.

## Executable local specification (measured)
```
# 1. lesson content (shipped, offline)
lesson = shipped assets/lessons-en/tracks/tutorial-904.json
modules = te.c.b(lesson.interactiveContent)     # VERIFIED_RUNTIME (5 cases)
type    = gm.h.a(modules)                       # VERIFIED_RUNTIME for empty -> None(slide)

# 2. normalisation / validation (pure, offline)
normalise(s) = lowercase(s, Locale.US)
               keep Character.isLetterOrDigit(c) || c ∈ "<>() :{},."
               drop all other chars including all whitespace   # E1, 21 cases
selectionOK(items) = ∀i: items[i].selected == items[i].correct  # E2, 8 cases
isSolvedCorrectly(p) = p.tries >= 1                            # E3, 20 cases

# 3. WebView exercise 151403 (VERIFIED_RUNTIME stage 5)
tap Q  -> JS: button.disabled=true; result="Try again"  (no native hook, no DB)
tap D  -> JS: result="Correct!"; word="D O G"; image dog_yawn (no DB yet)
tap Continue -> proceed; write LessonProgress row         (DB diff measured)

# 4. progress object and Room row (VERIFIED_RUNTIME)
bundle = LessonBundle(lessonId=151403/151410, tutorialId=904, trackId=219,
                      tutorialVersion=161, publishSetVersion=753, …)
progress = LessonProgress(lessonId, completedAt, startedAt, tries=1,
                          tutorialId, tutorialVersion, trackId,
                          publishSetVersion, attempts=1,
                          isPracticeProgress=false, inQueue=true)
INSERT OR REPLACE INTO lesson_progress (11 cols)   # S5_1_F: row appears
chain: c.U() -> c.H(1,1) -> LessonProgressRepository.createLessonProgress
       -> c.e0() -> LessonProgressQueue.storeLessonProgress
       -> c.f0(false, true) -> c.N()

# 5. offline flush attempt (VERIFIED_RUNTIME)
network.a: online a()=true,b()=false ; offline a()=false,b()=true
postUnsyncedLessonProgress() offline -> throw com.getmimo.network.NoConnectionException
SQL: SELECT * FROM lesson_progress WHERE in_queue = 1
SQL: DELETE FROM lesson_progress WHERE in_queue = 1     # rows lost at cold start
```
The exact room row measured after the correct answer:
```
151403 | 1793883744787 | 1793883713744 | 1 | 904 | 161 | 219 | 753 | 1 | 0 | 1
```

## Answer → feedback branch table (static + measured)
| Condition | Static method | Runtime evidence |
|---|---|---|
| exact string match | `c.V()` → `jm/m` | branch structure `VERIFIED_STATIC`; live dispatch `UNKNOWN` |
| normalised-only match | `c.W()` → `jm/n(userInput,expectedInput,true,E)` + analytics `validated_input_execution_correct_partial_match` | `VERIFIED_STATIC`; live dispatch `UNKNOWN` |
| mismatch | `c.X()` / `c.d0()` → `jm/o` 7 booleans, `solutionFeedbackWrong` | `VERIFIED_STATIC`; wrong WebView letter did NOT use it |
| selection | `km.f.b(List)` all-match | `VERIFIED_RUNTIME` direct invocation; UI submit `UNKNOWN` |
| WebView JS | `correctLetter='D'` | `VERIFIED_RUNTIME` for both branches |
| non-interactive slide | `c.U()` | `VERIFIED_RUNTIME` |

## What is NOT reconstructed (`UNKNOWN`)
* Absolute XP / points / streak / daily-goal / leaderboard formulas. No XP
  column in `mimo.db`; no arithmetic in `V/W/d0`; remote DTOs only.
* Native `onLessonRun$1 → Y(true)/Y(false) → V/W/X` dispatch with a real
  validatedInput / fillTheGap / spell / executable answer. Stage 6 confirmed
  (negative) that the WebView letter exercise uses `U()/H()` instead; the
  fill-the-gap module, `FillTheGap` interaction type and `RUN_DISABLED` state
  were measured but not answered.
* `jm/m`, `jm/n`, `jm/o` LiveData instances and the resulting native feedback UI.
* Chapter completion / tutorial completion transitions and the chapter-end
  screen; `cc/b.y` section classification at runtime.
* Unlock key values (`"<long>:<long>:<long>"`) and `SubscriptionTier` gating.
* Code evaluation: WebView JS bridge object, JNI/native execution, or remote
  executor boundaries.
* `LessonProgressQueue.updateCorrectAnswersCount` semantics; analytics event
  payload contents beyond names.
* Offline external-URL substitution (M05 Q-25), Room migration history (Q-24).
* Force-stop restoration of *answered* progress: the opposite was measured —
  `in_queue=1` rows are deleted at offline cold start.

## Honest verdict
Stage 6 additionally verified the live `LessonBundle(lessonId=151403,
lessonIndex=1, tutorialTitle=Discovering HTML and Tags)`,
`gm.h.a(...) = FillTheGap(interactionTypeName=fill_the_gap)`, the real
`te.c.b()` output for a shipped fill-the-gap lesson, and the `RunButton$State`
/ `LessonOutput` LiveData objects.

MISSION 07 **reconstructs the local answer→Room persistence path** for the
shipped WebView exercise, including the exact row, the wrong/correct UI and the
offline queue behaviour, and it **verifies five pure validators/parsers at
runtime**. It does **not** reconstruct server-side scoring, native validator
dispatch, unlock rules or code execution. No claim of a complete app/server
reconstruction is made.
