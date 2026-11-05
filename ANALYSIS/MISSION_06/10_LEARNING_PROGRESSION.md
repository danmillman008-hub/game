# MISSION 06 — DEEP CLIENT REVERSE ENGINEERING

**APK:** `48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a` (unchanged) · **branch** `arena/aebb90b7-game` · `SERVER CONFIRMED = 0`  
Evidence: `EVIDENCE/DISASM/*.smali.txt`, `SCHEMAS/METHOD_CATALOG_MIMO.json`,
`CALL_GRAPHS/*.json`, `METHOD_DOSSIERS/*.md`. Classification on every finding.

---

## VERIFIED_STATIC — content hierarchy (M05 reused)
19 tracks → 144 sections → 1,029 tutorials → 1,947 chapters → 18,272 lessons (English v753).
Tutorial types: `Learn, MobileProject, Challenge, Quiz, GuidedProject,
GuidedProjectOptional, RecreateProject, PracticeRequired, PracticeOptional`
(enum `<clinit>` verified). M05 counts: course 507, guidedProjectOptional 117,
guidedProject 74, challenges 40, practiceRequired 157, practiceOptional 134.
Chapter types: `NONE, PRACTICE_LEVEL_1..3, QUIZ, CHALLENGE_DIFFICULTY_0..4`.
All 144 sections satisfy `endIndex-startIndex+1 == len(tutorialIds)` (M05).

## VERIFIED_STATIC — path-map state machine
`GetPathMapState$invoke$3.invokeSuspend` @10129608, 659 insns
(`EVIDENCE/PATH_STATE_DISASM.txt`, dossier 15):
- states `Lvn/d0 Completed`, `Lvn/e0 Locked`, `Lvn/g0 Unlocked`,
  `Lvn/h0 UnlockedButNoKeys`, `Lvn/d chapter item`,
  `Lvn/y Locked(index)` / `Lvn/a0 Unlocked(index)` section states,
  `Lvn/a Locked(trackId)` / `Lvn/b Unlocked(trackId)` track states.
- `Challenge` tutorials are excluded from path items.
- Sequential prerequisite: a reverse `listIterator` over already-built items checks
  `TutorialType.isRequired()` and `Lvn/i0.d()`; the next item unlocks after the previous
  **required** predecessor is completed.
- `Tutorial.isCompleted()` → `Completed`; chapter items carry `isCompleted` and
  `isCompletedInHardMode` (from `Lds/w.c(Set, trackId, tutorialId, chapterId)`).
- `Tutorial.getHasProgress()`, `TutorialType.PracticeOptional`, Pro subscription tier
  (`Lyg/c.c`), `CanOpenChapterWithKeys`, keys count and dev-menu overrides
  (`Lsk/a.d()/e()`) choose `Locked` / `UnlockedButNoKeys` / `Unlocked`.
- Section states from `Lcc/b.y(List, Z, Integer?, Z, Z)`.
- Final `Lvn/n(track, sectionStates, selectedSectionIndex, dialogs, nextSectionState, …)`.

## VERIFIED_STATIC — completion records
`LessonProgressQueue.updateCorrectAnswersCount`:
`AnswersInChapter(correct = queued.count{isSolvedCorrectly()}, total = queued.size)`.
`getCorrectLessonProgressCount` = same correct count.
`getCorrectLessonsFirstTryCount` = `queued.count{isSolvedCorrectly() && attempts == 1}`.
`CompletionRepository.b(Track, cont)` attaches `TutorialCompletion.isCompleted` and
`completedChapters` from Room. `ChapterFinishedViewModel.R` =
`handleChapterAlreadyCompletedState` is the offline fallback.

## Economy / rewards — client-side boundary only
`VERIFIED_STATIC` strings and classes: `MainViewModel$fetchKeys$1`, `fetchRewards$1`,
`confirmRewardAndLookForNewRewards`, `daily_goal`, `streak_challenge_7d`,
`ChapterFinishedSuccessType{DAILY_GOAL_NOT_REACHED, DAILY_GOAL_REACHED,
DAILY_GOAL_ALREADY_REACHED_EARLIER_TODAY}`, `streakChallengeCoinPrice`, `userCoins`,
`local_coins`, `DefaultKeysRepository`, `DefaultStreakRepository`, `DefaultRewardRepository`,
`OnboardingSetDailyGoalViewModel`, `SetDailyGoalViewModel`, `GetUserStreakMonth`,
`ObserveUserStreakInfoCache`, `GetTrackEta`, `QueuePathOverviewEtaIfNeeded`.
**No XP/keys/coins/streak award formulas or thresholds were recovered** — they depend on
`Progress`/`PostProgressResponse`/`TrackEtaResponse` server bodies that M06 deliberately did
not reconstruct. `SERVER CONFIRMED = 0`.

## Unlock rule — EXPLICIT UNKNOWN
The exact boolean combination selecting `Locked` vs `UnlockedButNoKeys` vs `Unlocked` in
`GetPathMapState$invoke$3` is `UNKNOWN`: 659 instructions, 3 suspension labels, junk
`const/4` decoys. Precise pointer:
`Lcom/getmimo/interactors/path/GetPathMapState$invoke$3;->invokeSuspend`,
`classes.dex` @10129608, branches at PC `0x04aa`, `0x4f0`, `0x51a`, `0x608`.
`CanOpenChapterWithKeys$invoke$1` @10104004 second branch also `UNKNOWN`.

## Resume / restoration — `UNKNOWN`
M05 showed offline cold start rendering the same first three screens byte-for-byte and
offline AI/ChatGPT track content (`VERIFIED_RUNTIME`), but no persisted-progress-after-answer
or resume-after-force-stop evidence exists. `LessonBundle` and DataStore
`path_overview`/`first_run` keys indicate local state, but the exact restore algorithm is
`UNKNOWN`.
