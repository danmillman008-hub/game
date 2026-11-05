# MISSION 07 — 11 SCORING, XP, KEYS, STREAK AND REWARD LOGIC

**Status:** `UNKNOWN` for absolute formulas / `VERIFIED_STATIC` for client
objects. Any externally sourced value is classified as such; no formula is
invented.

## Measured client-side arithmetic
* `LessonProgress.isSolvedCorrectly()` = `tries >= 1` (`VERIFIED_RUNTIME`,
  20-object truth table, `04_ANSWER_VALIDATION_RUNTIME.md`). `tries` is set by
  `base/c.H(tries, attempts)` from `C == Boolean.TRUE ? 0 : 1` after `d++`
  (M06 static, rechecked in `RUNTIME_TRACE/STATIC_DECODE/00_STATIC_DECODE_M07.md`).
* `base/c.V()` / `W()` increment the ViewModel field `d` (attempts) and pass it
  to `H()`; `f0(false, isSolvedCorrectly())` is an analytics/tracking call,
  not an XP computation.
* `LessonProgressQueue.updateCorrectAnswersCount` (M06) exists but its body and
  its consumer were not runtime-traced.
* `mimo.db` has **no XP/score/streak/key column**; its 11 `lesson_progress`
  columns are exactly `lesson_id, completed_at, started_at, tries,
  tutorial_id, tutorial_version, track_id, publish_set_version, attempts,
  is_practice_progress, in_queue` (`06_DATABASE_BEFORE_AFTER.md`).

## Externally sourced / remote objects (`VERIFIED_STATIC`)
Class census with the M06 corrected DEX cache finds:
`com.getmimo.core.model.streak.Streak`, `UserActivity`,
`UserActivityResponse`, `com.getmimo.data.model.leaderboard.*`
(`Leaderboard`, `LeaderboardLeague`, `LeaderboardRank`,
`LeaderboardUserResult`, `RemoteLeaderboardState` with `Active/Error/NotEnrolled/Result`),
`com.getmimo.data.model.reward.Reward`, `Rewards`,
`com.getmimo.data.model.publicprofile.ProfileLeaderboardInfo`,
`com.getmimo.analytics.properties.RewardScreenCloseState`,
`Analytics$LessonStreakChallenge$LessonStreakChallengeSource`,
`com.getmimo.data.source.remote.keys.a` (`DefaultKeysRepository.fetchKeys`
/ `consumeUserKey`), `SettingsRepository.getUserDailyGoal/setDailyGoal`.
RevenueCat `no_backup/RevenueCat/remote_config/remote_config.json` and
`com_revenuecat_purchases_preferences.xml` were present in the offline
private-data snapshots, i.e. cached remote state exists locally.

## Classification
| Quantity | Class | Status |
|---|---|---|
| `tries`, `attempts`, `in_queue` | A local | `VERIFIED_RUNTIME` (constructed rows) / `VERIFIED_STATIC` (H, createLessonProgress) |
| correct/wrong feedback objects `jm/m`, `jm/n`, `jm/o` | A local | `VERIFIED_STATIC` (V/W/d0), runtime pending |
| XP per lesson, streak length, daily goal minutes, leaderboard rank, keys balance | D remote / E unknown | `UNKNOWN` — no local formula found; values come from remote DTOs and caches |
| Chapter unlock boolean | mixed | `PARTIALLY VERIFIED`: `ds/w.c(Set<String>,J,J,J)` checks membership of `"long:long:long"` in a key set; the key set originates from the remote keys repository (`08_PROGRESSION_AND_UNLOCK_LOGIC.md`) |

No attempt was made to reconstruct server infrastructure (`SERVER CONFIRMED=0`).
