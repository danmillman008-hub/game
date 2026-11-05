# LEARNING_ENGINE — evaluation, scoring, progression, rewards

Every row is classified. **`VERIFIED_STATIC` does not mean "behaviour proven at
runtime"**; it means the literal/class/field exists in the original APK.
`VERIFIED_RUNTIME` requires an emulator observation.
APK `48ce1740…7c7a`, `com.getmimo` 9.35, `SERVER CONFIRMED = 0`.

## 1. Answer evaluation — `VERIFIED_STATIC`

| Exercise | Where correctness is decided | Evidence |
|---|---|---|
| Multiple choice (`<selection>` 7,356) | **on-device**, from `item correct="true"/"false"` in the shipped DSL | `CONTENT_MODEL.md` §4.3, `SAMPLES/selection_lesson.txt` |
| Fill the gap (`fillTheGap` 9,957) | **on-device**, from `<option startIndex/endIndex>` into shipped `<content>` and explicit distractor `correct="false"` | `SAMPLES/fillthegap_lesson.txt` |
| Validated input (`validatedInput` 1,772) | **on-device** via `onValidatedInputExecuted`; exact token-index rule `UNKNOWN` | `InteractiveLessonBaseViewModel$onValidatedInputExecuted$1`, `SAMPLES/validatedinput_lesson.txt` |
| Embedded webview (930 `<webview>`; 217 lessons emit `mimo.activity.correct/wrong`) | **on-device JS** → `MimoLesson.postMessage({kind:'activity',result})` | `SAMPLES/lesson-webview.js`, `classes.dex @3,432,650/675/698` |
| Executable files (`executableFiles` 4,024) | **mixed**: content + `solvedContent` + `hints` shipped locally, but `ExecuteFilesResponse.hasPassed/tests[]/consoleOutput` comes from `POST …/runFiles` | `CONTENT_MODEL.md` §4.3, `MIMO_RETROFIT_ENDPOINTS.json` |

`VERIFIED_STATIC` feedback: `visible-if="correct" (173)`, `"wrong" (19,101)`,
`"always" (18,869)` → the client selects which shipped paragraph/module to
display. No server response is required to render correct/wrong feedback for
interactive lessons.

**`VERIFIED_RUNTIME` incorrect-answer state (run `42005358012`):** in the real
"Guess the letter" lesson (`tutorial-904.json` lesson 151403), tapping the wrong
option `Q` produced a red **"Try again"** message, disabled the `Q` button and
kept `R`/`D` and `Continue` available for retry —
`ANALYSIS/RUNTIME/MISSION_05/RUN_42005358012/SCREENSHOTS/LESSON-WRONG-01.png`
and `…/UI_HIERARCHY/LESSON-WRONG-01.xml`. `Continue` then advanced to the next
lesson ("This is the code editor where we'll write code…") —
`LESSON-CONTINUE.*`. **Correct-answer state remains `UNKNOWN`**: the follow-up
run `42006697783` selected a different path with no quiz options, so no correct
answer was submitted. No claim is made about correct-state rewards or scoring.

`INFERRED`: `lessonSolvedCorrectlyWithPartialMatch$1` implies a
partial-credit/partial-match path; its condition is `UNKNOWN`.

## 2. Local state update chain — `VERIFIED_STATIC` (names) / `INFERRED` (order)

```
lessonSolvedCorrectly / lessonSolvedIncorrectly
  -> storeLessonProgressInMemory (InteractiveLessonBaseViewModel$…)
  -> storeLessonProgress(LessonBundle, Instant, tries, attempts)
       signature VERIFIED_STATIC (MIMO_COMPLETION_ENGINE.json):
       (Lcom/getmimo/ui/lesson/interactive/LessonBundle;
        Lorg/joda/time/Instant; I I)
       Lcom/getmimo/data/model/room/LessonProgress;
  -> addOrUpdateLessonProgressInQueue (Room lesson_progress, in_queue=1)
  -> storeAndPostAllLessonProgress (chapter end)
  -> postUnsyncedLessonProgress / POST /v1/tutorials/{tutorialId}/progress
  -> toLessonProgressSyncResult / LessonProgressSyncResult(reachedDailyGoal=…)
  -> in_queue = 0
```

`VERIFIED_STATIC`: `LessonProgress.isSolvedCorrectly()` is `attempts >= 1`
(M02 bytecode: `intField >= 1`). `tries`, `attempts`, `startedAt`,
`completedAt`, `publishSetVersion`, `tutorialVersion`, `isPracticeProgress`
are the recorded dimensions. `getCorrectLessonProgressCount`,
`getCorrectLessonsFirstTryCount`, `updateCorrectAnswersCount`,
`getRewardMultiplier` are local queue methods.

## 3. Scoring / economy — `VERIFIED_STATIC` (names, strings) / `UNKNOWN` (formulas)

| Concept | Verified artefacts | Formula |
|---|---|---|
| XP | `total_xp`, `XP Earned`, `UserXpInformation(xpFormatted=`, `DOUBLE_XP_GAIN`, `xpHelper`, `CurrentStatus(xp=`, `sparks_daily_goal=%1$d/%2$d XP` | `UNKNOWN` |
| Sparks | `rewardedSparksForCorrectAnswer`, `dailySparksGoal`, `earnedSparks`, `formattedSparks`, `sparksCount`, `sparksGoal`, `DailySparksProgress`, `double_sparks_24h` | `UNKNOWN` — `rewardMultiplier` is a named getter only |
| Coins | `GET /v1/user/coins`, `dailyGoalCoinReward`, `userCoins`, `Coins(coins=`, `coinPrice`, `You earned %1$d coins!` | `UNKNOWN`, server-owned (`VERIFIED_STATIC` endpoint) |
| Keys | `GET /v1/user/keys`, `POST /v1/user/keys/consume`, `consumeKeyIfNeeded`, `ACTIVE_COIN_COUNT` | `UNKNOWN`; unlock semantics `UNKNOWN` |
| Daily goal | levels `1 Casual / 2 Regular / 3 Serious`; **`VERIFIED_RUNTIME` (42003884423 STEP-13): Casual = 5 min, Regular = 10 min, Serious = 20 min**; states `DAILY_GOAL_REACHED`, `DAILY_GOAL_NOT_REACHED`, `DAILY_GOAL_ALREADY_REACHED_EARLIER_TODAY` | `UNKNOWN` — `getReachedGoal` / `getDailyGoalCoinReward` are inferred server-owned |
| Streak | `activeStreakLength`, `longestStreakLength`, `userCurrentStreak`, `userLongestStreak`, `GET /v1/user/activity`, `STREAK_FREEZE`, `WEEKEND_FREEZE`, `STREAK_REPAIR`, `FREE_STREAK_REPAIR`, streak challenges 3/5/7-day, widgets | `UNKNOWN` — break/repair/promotion rules not observed |
| Leaderboard | 5 leagues (Wooden→Golden), "Finish in the top 15 to advance", `/v1/leaderboards/*`, `hasActiveLeagueFreeze`, `hasActiveLeagueProtection` | rule is a **string**, not verified behaviour |
| Rewards | `GET /v1/user/rewards/next`, `POST /v1/user/rewards/{rewardId}/confirm`, `DefaultRewardRepository$retrieveOutstandingRewards`, `sendConfirmationRequestToBackend`, `Rewards`, `Reward` | server-owned (`VERIFIED_STATIC` endpoints) |

**`UNKNOWN` explicitly:** `rewardMultiplier` value,
`rewardedSparksForCorrectAnswer` value, XP per lesson,
first-try bonus, chapter-end ETA threshold, streak break/repair,
daily-goal coin amount, leaderboard promotion computation.
M02 `FINAL_KNOWN_GAPS.fa.md` lists these as gap #6/#8; M05 did **not** resolve
them. No formula is invented here.

## 4. Progress calculation — `VERIFIED_STATIC` (SQL) / `UNKNOWN` (threshold)

- `SELECT COUNT(DISTINCT chapter_id) FROM chapter_completions` — the only
  aggregate found; used for chapter-end progress (`VERIFIED_STATIC`).
- `SELECT * FROM chapter_completions WHERE track_id = ? [AND tutorial_id in (…)]`
  and `SELECT * FROM tutorial_completions WHERE track_id = ? [AND …]` —
  used to mark `Chapter.isCompleted` / `Tutorial.isCompleted` on the runtime
  content model (`INFERRED` merge, `VERIFIED_STATIC` SQL).
- `lesson_progress` primary key `(lesson_id, tutorial_id)` means **progress is
  shared across tracks** for a tutorial reused by multiple tracks
  (`INFERRED` from 2,002 refs vs 1,029 tutorial files).
- `publish_set_version` is stored per progress row ⇒ content versioning is
  part of progress identity (`VERIFIED_STATIC`).

## 5. Lesson completion / repetition / review — `VERIFIED_STATIC` + `UNKNOWN`

- Completion: `ChapterCompletion` row written; `TutorialCompletion.isCompleted`;
  `lessonSolvedAndProceedToNextLesson`; `NonInteractiveLessonFragment$goToNextPage`.
- Repetition/review: `practiceRequired` 157, `practiceOptional` 134,
  `challenges` 40, `practiceLevel1/2/3`, `challengeLevel0/1/2`,
  `SmartPractice`, `GetChapterToolbarType$listenForLessonStreak`,
  `spaced repetition`-like strings (`INFERRED` only — the algorithm is `UNKNOWN`).
- Hard mode: 6,058 alternate `hardModeContent` bodies, 4,054
  `hardModeSelected`, `StoreSyntheticHardModeProgress`,
  `markChapterCompletedInHardMode` ⇒ an independent local completion track.
- Retry: `showWrongFeedbackBlock`, `tries`/`attempts`, `getCorrectLessonsFirstTryCount`.

## 6. Ownership boundary (critical for offline)

| Logic | Owner | Classification |
|---|---|---|
| Answer key & feedback text | **APK assets** | `VERIFIED_STATIC` |
| Correct/wrong decision for interactive lessons | **client (Kotlin + WebView JS)** | `VERIFIED_STATIC` |
| Per-lesson progress record | **Room DB on device** | `VERIFIED_STATIC` |
| Chapter/tutorial completion rows | **Room DB on device** | `VERIFIED_STATIC` |
| XP/sparks/coins/keys balances, streak, daily goal result, leaderboard | **server** | `VERIFIED_STATIC` (endpoints) |
| Code execution & test pass/fail for executable lessons | **server** | `VERIFIED_STATIC` (endpoints) |
| Chapter-end "success state" | **server-assisted** (`handleOnlineState` / `handleOfflineState`) | `VERIFIED_STATIC` (class names), `UNKNOWN` fallback behaviour |

**Offline conclusion:** the *learning loop itself* (content → interaction →
correct/wrong → feedback → next lesson → local progress) is fully local.
The *economy and authoring/execution services* are not. See
`OFFLINE_DEPENDENCY_MATRIX.md`.

`VERIFIED_RUNTIME` status: run `42003884423` reached a **real lesson**
("Guess the letter", shipped `tutorial-904.json` lesson 151403) and an
**offline executable lesson** (`tutorial-2199.json` lesson 63259); run
`42005358012` probes answer states. The offline learning-path toolbar showed
coins **200**, keys **∞**, streak **`-`** (`OFFLINE-01.png`) — these are
`VERIFIED_RUNTIME` UI values, **not** scoring formulas. No answer was submitted
and no completion screen was observed in runs 1–3. Every behaviour in §2–§5
above remains static evidence or inference unless explicitly marked.
`SERVER CONFIRMED = 0`.

**Evidence:** `ANALYSIS/MIMO_SCORING_MODEL.json`,
`ANALYSIS/MIMO_COMPLETION_ENGINE.json`, `ANALYSIS/MIMO_SCORING_STRINGS.json`,
`ANALYSIS/LESSON_AND_SCORING_ENGINE.fa.md`,
`ANALYSIS/LESSON_SCORING_VERIFICATION.fa.md`, `EVIDENCE/ROOM_SQL.txt`,
`SCHEMAS/SHIPPED_CONTENT_STATS.json`.
