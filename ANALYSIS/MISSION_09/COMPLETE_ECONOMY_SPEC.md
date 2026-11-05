# MIMO 9.35 — COMPLETE ECONOMY SPECIFICATION

**Document:** `COMPLETE_ECONOMY_SPEC.md` · **Mission:** MISSION 09 (final reconstruction) · **Branch:** `arena/aebb90b7-game`
**Target APK:** `com.getmimo` 9.35, `versionCode=1792759685`, 142,353,499 B, SHA-256 `48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a` — unchanged.
**SERVER CONFIRMED = 0.** Classification vocabulary: `VERIFIED_STATIC`, `VERIFIED_RUNTIME`, `VERIFIED_ASSET`, `VERIFIED_DATABASE`, `VERIFIED_NETWORK_OBSERVATION`, `INFERRED`, `UNKNOWN`, `SERVER_DEPENDENT`.
Evidence codes resolve in `COMPLETE_EVIDENCE_DATABASE.json` / `COMPLETE_SYSTEM_MAP.json -> evidence_index`.

---


## 0. Verdict

The client contains **no local award formula**. XP, streak length, key balance, reward
eligibility, daily-goal award thresholds and leaderboard rank are `SERVER_DEPENDENT` and
`UNKNOWN`. What IS client-side is display, cached values and local answer counters.
`SERVER CONFIRMED = 0`. No formula below is invented.

## 1. Formula inventory (every entry classified)

| # | Quantity | Formula / behaviour | Classification |
|---|---|---|---|
| F1 | `isSolvedCorrectly()` | `tries >= 1` | VERIFIED_RUNTIME |
| F2 | `AnswersInChapter.correct` | `queued.count{ isSolvedCorrectly() }` | VERIFIED_STATIC |
| F3 | `AnswersInChapter.total` | `queued.size` | VERIFIED_STATIC |
| F4 | `getCorrectLessonProgressCount` | same count as F2 | VERIFIED_STATIC |
| F5 | `getCorrectLessonsFirstTryCount` | `queued.count{ isSolvedCorrectly() && attempts == 1 }` | VERIFIED_STATIC |
| F6 | `updateCorrectAnswersCount` | emits `AnswersInChapter(correct,total)` to `_answersInChapter` StateFlow; runs `updateLessonStreakDetector` when `attempts==1` | VERIFIED_STATIC |
| F7 | `tries` write | `V/W/X` -> `H(tries,attempts)`; `tries = wrongLatch ? 0 : 1` | VERIFIED_STATIC + VERIFIED_RUNTIME |
| F8 | `attempts` write | `V()`/`X()` increment ViewModel field `d` | VERIFIED_STATIC |
| F9 | `f0(false,isSolvedCorrectly())` | analytics/tracking call; **contains no XP arithmetic** | VERIFIED_RUNTIME |
| F10 | `d0()` | wrong-feedback; **contains no XP arithmetic** | VERIFIED_RUNTIME |
| F11 | guest coin balance | `mimo_prefs.xml local_coins={"coins":200}`; constant across 14 snapshots | VERIFIED_DATABASE |
| F12 | coins display | toolbar `200` (x~238) and `0` (x~916, UNKNOWN counter) | VERIFIED_RUNTIME |
| F13 | XP per lesson | **no local formula; no XP column in mimo.db** | UNKNOWN + SERVER_DEPENDENT |
| F14 | streak length / daily streak | remote `core/model/streak/Streak`, `UserActivity`, `UserActivityResponse`, `DefaultStreakRepository` | UNKNOWN + SERVER_DEPENDENT |
| F15 | keys balance / consumption | remote `DefaultKeysRepository.fetchKeys/consumeUserKey` | UNKNOWN + SERVER_DEPENDENT |
| F16 | rewards | remote `Reward`, `Rewards`, `PostProgressResponse`; `MainViewModel$confirmRewardAndLookForNewRewards$1`, `fetchRewards$1` | UNKNOWN + SERVER_DEPENDENT |
| F17 | leaderboard rank | remote `Leaderboard`, `LeaderboardLeague`, `LeaderboardRank`, `LeaderboardUserResult`, `RemoteLeaderboardState{Active/Error/NotEnrolled/Result}` | UNKNOWN + SERVER_DEPENDENT |
| F18 | daily goal | `Settings.dailySparksGoal` (observed `null`); `SettingsRepository.getUserDailyGoal/setDailyGoal`; onboarding goal `build_something_useful` persisted | VERIFIED_RUNTIME (storage) / UNKNOWN (formula) |
| F19 | achievement / level / multiplier / cap | no local arithmetic found | UNKNOWN + SERVER_DEPENDENT |
| F20 | practice/challenge rewards | no local arithmetic found; practice tab auth-gated | UNKNOWN + SERVER_DEPENDENT |

## 2. Client-side vs server-authoritative separation

**Client-owned:** `lesson_progress` rows, `tries`/`attempts`, `AnswersInChapter` counters,
guest `local_coins` cached balance, `favorite_tracks`, `user_settings`, toolbar rendering,
`f0()` analytics event, `Settings` object write, `NetworkUtils` connectivity gate.
**Display-only:** `200` coin counter, `0` unknown counter, section `0/20 / 0/11 / 0/9 /
0/15` progress, `Path Icon` state.
**Server-owned:** XP, streak length, keys balance, reward eligibility, leaderboard rank,
subscription tier, `PostProgressResponse`, `Progress`, `TrackEtaResponse`,
RevenueCat `remote_config.json`, remote code-runner results, daily-goal awards.

## 3. Trace of the coin layer (VERIFIED_STATIC)

Classes/methods found in the DEX catalog [E31, E28]:
`com.getmimo.core.model.coins.Coins.getCoins()I` (model getter),
`com.getmimo.data.source.remote.coins.a.a()` / `b(...)` (remote source: flow + sync),
`com.getmimo.data.source.remote.reward.a.a()/c()` (reward confirm/retrieve),
`com.getmimo.data.source.remote.keys.a.a()/b()/c()` (keys fetch/consume/gate),
`com.getmimo.data.user.streak.a.d()/f()/h()` (mapResponse/getData/toModel),
`com.getmimo.data.settings.a.h()` (daily goal),
`com.getmimo.ui.main.d.E/F/G/H/I` (MainViewModel).
M08/M09 hooked all of these; **no `entry` event** carrying an award calculation was
observed. The only `entry` events were `settings_get a` -> `null` and
`settings_write l` with the null `Settings` [E12, E29].

## 4. Exact boundary evidence

* `mimo.db` has exactly 11 `lesson_progress` columns and 0 XP/score/streak/key columns [E27].
* `local_coins` was `200` in all 14 natural snapshots; a lesson completion did not change
  it [E11, E13].
* `f0(false,true)` and `d0()` have no arithmetic (M07 static decode `d0.smali.txt`) [E32].
* No Mimo `/v1/...` request or response was observed in any run; only third-party URLs
  (Mixpanel, Adjust, Facebook model_asset, RevenueCat subscribers, Firebase batchlog)
  [E12, E22, E29].
* `SERVER CONFIRMED = 0`.

## 5. Offline behaviour / idempotency

Offline, the economy is **display-only and constant**: coins render from the cached
`local_coins`, counters derive from local `lesson_progress` rows, analytics events still
accumulate in local databases (Mixpanel / datatransport rows grew offline in M07 stage 2),
but no award is computed. Retry/idempotency of reward confirmation is
`SERVER_DEPENDENT` / `UNKNOWN`: `POST /v1/user/rewards/{rewardId}/confirm` exists but
was never called. No coin/XP increment should be implemented as "original Mimo behaviour".

## 6. Independent implementation contract (design choice, clearly labelled)

```text
interface EconomyService {
    fun coinBalance(): Flow<Int>                 # local cache, default 200 for a new guest
    fun chapterCounters(chapterId): AnswersInChapter   # F2/F3/F5/F6, locally computed
    fun onLessonCompleted(progress): Unit        # emits local counters only; NO award
    // Optional: a pluggable award policy. Any XP/coin/streak formula here is an
    // INDEPENDENT DESIGN CHOICE, never presented as reconstructed Mimo behaviour.
}
```
Acceptance test: after a lesson completes offline, `coinBalance()` MUST be unchanged and
`chapterCounters()` MUST equal F2/F3/F5 values; no network call is required.


---

## MISSION 09 runtime addendum (`VERIFIED_RUNTIME`, run `42077425594`)

The MISSION 09 controlled run succeeded where M08 failed: the API-36 `Java.registerClass`
lifecycle hook was replaced with **direct** `android.app.Activity` / `Fragment` /
`WebView` hooks, giving `server_active=true`, `attach_ok=true` (pid 3348, process `Mimo`),
**181 hooks installed, 72 real `com.getmimo` method `entry` events**, 71 `exit`,
86 SQL, 17 DI, 19 LiveData and 28 lifecycle `nav` events. `real_target_method_executed=true`.
All three user-required instrumentation conditions are therefore met [E29, E30].

`SERVER CONFIRMED = 0`. Instrumentation success is not a claim that every screen was
reached: the fixed 20-tap onboarding chain stalled at step 4 on this build, so
`MainActivity` was reached with an explicit intent; the lesson answer matrix was
**not executed** (`lesson_matrix_not_executed`, `ChapterActivity` not reached) and the
resulting three route screens resumed an incomplete `OnboardingActivity` back stack.
See `FINAL_UNKNOWN_REGISTER.md` and `FINAL_TEST_MATRIX.json` for the honest limitations.

### M09 runtime economy evidence (boundary confirmed, no formula invented)

* `Coins.getCoins()` executed 3× with `this_fields.coins="0"` and `ret="0"` [E29].
* `com.getmimo.data.source.remote.coins.a.b()` executed from
  `RefreshPathToolbarState$refreshCoinsFlow$1`; `keys.a.b()` from `$refreshKeysFlow$1`;
  `reward.a.c()` executed with cached `[]`; `MainViewModel.H()` from
  `checkIfLeaderboardBadgeShouldBeShown` [E29].
* `com.getmimo.data.user.streak.a.f()` (`DefaultStreakRepository.getStreakMonthData`)
  **threw** `java.io.IOException: com.getmimo.data.source.remote.authentication.AccessTokenUnavailableException`
  with `StreakMonthRange(2026-10-26..2026-11-05)` — direct runtime proof that streak data
  is auth-gated at repository level [E29].
* Toolbar numeric values measured: `0` at x~201, `0` at x~238, `0` at x~540 — no coin
  counter increment was observed [E29].
* No award arithmetic appeared in any of the 72 method entries. F13–F20 remain
  `SERVER_DEPENDENT`/`UNKNOWN`; `SERVER CONFIRMED = 0`.
