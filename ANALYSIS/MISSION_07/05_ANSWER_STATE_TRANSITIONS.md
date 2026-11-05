# MISSION 07 — 05 STATE TRANSITIONS AFTER A WRONG / CORRECT ANSWER

**Status:** `VERIFIED_RUNTIME` for the WebView wrong-answer state and for the
non-interactive solved state; `PARTIALLY VERIFIED` for the native correct /
partial / wrong branches; `UNKNOWN` where not exercised.
`SERVER CONFIRMED = 0`.

## Experiment design (M07 requirement: one operation at a time)
`ANALYSIS/RUNTIME/MISSION_07/m07_answer_driver.py` + `m07_lesson_plan.py`:
tap targets are measured from `uiautomator` XML; correct/wrong labels come
verbatim from shipped `interactiveContent`; every single tap is bracketed by a
root SQLite snapshot (`m07_snapshot.sh`) and a UI dump. No APK modification,
no guessed answer, no server call.

## Measured transition 1 — WebView lesson 151403, WRONG letter `Q`
Fresh lesson UI (`UI/S4_C_BEFORE_ANSWER.xml`):
`["Hypertext Markup Language…", "On top of HTML…", "Guess the letter", "_ O G", "Q", "R", "D", "Continue"]`.
Shipped content (`assets/lessons-en/tracks/tutorial-904.json`, lesson 151403)
sets `correctLetter = 'D'`; on a wrong letter the WebView JS does
`button.disabled = true`, `result.innerHTML = 'Try again'`.

After `input tap 398 1017` (measured centre of the `Q` button):
`UI/S4_D1_AFTER_WRONG_OPTION.xml`:
`["Hypertext Markup Language…", "On top of HTML…", "Try again", "_ O G", "Q", "R", "D", "Continue"]`
with clickable nodes:
* `Q` — `clickable=true`, **`enabled=false`**, bounds `[343,963][454,1071]`
* `R` — enabled, `[485,963][595,1071]`
* `D` — enabled, `[630,963][737,1071]` (centre `683,1017`)
* bottom CTA container — enabled, `[47,2178][1033,2299]` (centre `540,2238`)

**Frida result (`TRACES/STAGE4_ONLINE.jsonl`):** zero entries for
`onLessonRun`, `lessonSolvedIncorrectly`, `wrongFeedback`, `d0()`, `partialMatch`
or `solutionFeedback`. No `jm/o` LiveData value was posted. `lesson_progress`
remained the single pre-existing row (lesson 151410). Therefore the wrong-letter
feedback of this WebView exercise is **entirely inside the WebView JavaScript**,
not the native `base/c.X()/d0()` path. This is a `VERIFIED_RUNTIME` boundary
finding and it corrects the naive assumption that every wrong answer calls
`d0()`.

## Measured transition 2 — non-interactive slide lesson 151410, "solved"
Continuing past a slide fired the full `base/c.U() → H() →
LessonProgressRepository.createLessonProgress → e0() →
LessonProgressQueue.storeLessonProgress → f0(false,true) → N()` chain with
`LessonProgress(… tries=1, attempts=1, inQueue=true)` and produced the first
`lesson_progress` row. See `03_INTERACTIVE_LESSON_VIEWMODEL_RUNTIME.md` and
`06_DATABASE_BEFORE_AFTER.md`. This is a **local, no-server** transition.

## Measured transition 3 — queued row at offline cold start
`UI/S4_G_BEFORE_FORCESTOP.xml` → `am force-stop` → offline `am start`.
`DELETE FROM lesson_progress WHERE in_queue = 1` was observed (offline trace,
4 occurrences at 12:44:04/31/38/44), `SELECT * FROM lesson_progress WHERE
in_queue = 1` at 12:44:37, and
`com.getmimo.network.NoConnectionException` thrown from
`postUnsyncedLessonProgress` at 12:44:04. The row disappeared from
`SNAPSHOT_S4_H_OFFLINE_COLD_START.json`. See `07_PERSISTENCE_RESTORATION_AND_QUEUE.md`.

## State table
| # | State | UI marker | DB | Native hook | Class |
|---|---|---|---|---|---|
| S0 | lesson opened, no answer | `Guess the letter`, `_ O G` | slide row 151410 only | `initialiseViewModel`, `getLessonBundle` | A local |
| S1 | wrong WebView letter | `Try again`, `Q disabled` | unchanged | **none** | A local (JS) |
| S2 | non-interactive slide solved | next slide / Continue | 1 `lesson_progress` row, `in_queue=1` | `U,H,e0,queue_store,f0,N` | A local + B queued |
| S3 | offline cold start | path map | `lesson_progress` 0 rows | `repo_postUnsynced` throws `NoConnectionException` | B queued, not durable |
| S4 | native correct / partial / wrong answer | `Correct!` / `D O G` / `jm/o` | not yet measured | `V()`/`W()`/`X()` | `UNKNOWN` (stage 5 targets this) |

## Feedback object catalogue (`VERIFIED_STATIC`)
`jm/m` correct (requires `solutionFeedbackCorrect`), `jm/n(userInput,
expectedInput, true, E)` partial match, `jm/o` wrong (7 booleans incl.
`solutionFeedbackWrong`, `solutionFeedbackTryAgain`). `q` LiveData carries
them. M06 `setupViews$2` @10985684 maps exact/normalised-only/mismatch to
`V/W/X`. No XP arithmetic in `d0()` (M07 static decode).

## STAGE 5 — full wrong → correct → persist chain (`VERIFIED_RUNTIME`, run `42030594857`)
`EXPERIMENTS/S5_ANSWER_LOG.jsonl` and `UI/S5_1_*.xml`:

| step | operation | measured UI | `lesson_progress` |
|---|---|---|---|
| `S5_1_C_BEFORE_ANSWER` | lesson 151403 opened (after 42 measured onboarding taps) | `Guess the letter`, `_ O G`, `Q R D`, `Continue` | 1 row (slide 151410) |
| `S5_1_D1_AFTER_WRONG_OPTION` | `input tap 398 1017` = wrong `Q` | `Try again`, `_ O G`, Q disabled, R/D enabled | 1 row (unchanged) |
| `S5_1_E1_AFTER_CORRECT_OPTION` | `input tap 683 1017` = correct `D` | **`Correct!`**, **`D O G`**, `dog_yawn` image loaded | 1 row (unchanged) |
| `S5_1_F_AFTER_CORRECT_SUBMIT` | `input tap 540 2238` = `Continue` | next lesson: `This is the code editor where we'll write code`, `Click on <button>Like</button>`, `index.html`, snippets | **2 rows** — new row for lesson 151403 |

New row (verbatim, 11 columns):
```
151403  1793883744787  1793883713744  1  904  161  219  753  1  0  1
```
i.e. `lesson_id=151403`, `completed_at=13:02:24Z`, `started_at=13:01:53Z`,
`tries=1`, `attempts=1`, `in_queue=1`, `publishSetVersion=753`,
`isPracticeProgress=0`. `tries=1` ⇒ `isSolvedCorrectly()=true` by E3.

**Interpretation (careful):** the correct-letter feedback is produced by the
shipped WebView JS, and the row is written when the lesson is *proceeded past*,
not at the instant of the `D` tap. The stage-5 Frida session attached at
12:55:18 went silent after 12:58:01 because onboarding restarted the app
process; therefore the `V()`/`W()` native dispatch for this WebView exercise is
**not** claimed. What is `VERIFIED_RUNTIME` is the full observable chain from a
shipped-correct answer to a persisted `LessonProgress` row. Stage 6 attaches
Frida at the answer moment and targets a native selection lesson to test the
`onLessonRun$1 → V()/X()` path.

`second_lesson_not_found` is recorded honestly: the post-answer search did not
reach a second classified lesson; no selection-answer claim is made from it.
