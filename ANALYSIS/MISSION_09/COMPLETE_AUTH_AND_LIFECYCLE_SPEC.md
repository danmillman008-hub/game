# MIMO 9.35 — COMPLETE AUTH & LIFECYCLE SPECIFICATION

**Document:** `COMPLETE_AUTH_AND_LIFECYCLE_SPEC.md` · **Mission:** MISSION 09 (final reconstruction) · **Branch:** `arena/aebb90b7-game`
**Target APK:** `com.getmimo` 9.35, `versionCode=1792759685`, 142,353,499 B, SHA-256 `48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a` — unchanged.
**SERVER CONFIRMED = 0.** Classification vocabulary: `VERIFIED_STATIC`, `VERIFIED_RUNTIME`, `VERIFIED_ASSET`, `VERIFIED_DATABASE`, `VERIFIED_NETWORK_OBSERVATION`, `INFERRED`, `UNKNOWN`, `SERVER_DEPENDENT`.
Evidence codes resolve in `COMPLETE_EVIDENCE_DATABASE.json` / `COMPLETE_SYSTEM_MAP.json -> evidence_index`.

---


## 1. Guest vs authenticated feature-access matrix

No real authentication was attempted or bypassed; no credentials, tokens or server state
were fabricated. All findings are the legitimate client-side guest behaviour.

| Feature | Guest (measured) | Auth gate layer | Classification |
|---|---|---|---|
| Splash / intro / onboarding | accessible | none | VERIFIED_RUNTIME |
| `Skip` on `AuthenticationActivity` | guest created locally | UI | VERIFIED_RUNTIME |
| Learn / path map / chapters / lessons | accessible | none | VERIFIED_RUNTIME |
| Answer validation / progress | accessible | none | VERIFIED_RUNTIME |
| Practice tab | **`Lock in your learning` / `Create a profile to access practice content` + `Log in` + `Sign up with Google` / `Sign up with email`** in Compose `anonymous_user_lock_view` | **UI-only gate** (no server call observed) | VERIFIED_RUNTIME [E14, E29] |
| Streak data | `DefaultStreakRepository.getStreakMonthData` -> `java.io.IOException: com.getmimo.data.source.remote.authentication.AccessTokenUnavailableException` | **repository-level**: an access token is required before the remote request | VERIFIED_RUNTIME (M09 run `42077425594`) [E29] |
| Coins / keys / rewards / leaderboard | refreshed from remote repositories; cached values rendered | repository-level + server | VERIFIED_RUNTIME + SERVER_DEPENDENT |
| Profile | destination exists in `NavigationBar` map; guest screen contents not cleanly measured | UNKNOWN | UNKNOWN |
| Purchases / subscription | RevenueCat cached config present; no purchase attempted | server | SERVER_DEPENDENT |

**Decisive correction:** the Practice gate is a **client UI gate**, not a server requirement —
the guest never reaches a server call. Streak data is a **repository-level auth gate**:
the exact exception `AccessTokenUnavailableException` was captured from a real method
`entry`/`throw` pair in M09. These are distinct layers and must not be conflated.

## 2. Lifecycle graph (VERIFIED_RUNTIME — M09 direct Activity hooks)

The M08 `Application$ActivityLifecycleCallbacks` hook failed on API 36 because
`onActivityPre*/Post*` default methods were missing. M09 replaced it with **direct**
`android.app.Activity.onCreate/onStart/onPostCreate/onResume/onPause/onStop/
onSaveInstanceState/onRestart/onDestroy` hooks plus `androidx.fragment.app.Fragment`
hooks. Result: 28 `nav` events in one run [E29].

```mermaid
flowchart LR
  Splash["SplashActivity"] -->|onCreate/onStart/onResume| Intro["IntroSlidesActivity"]
  Splash -->|onStop/onDestroy| Stopped["destroyed"]
  Intro -->|Get started| Onb["OnboardingActivity (NavHostFragment)"]
  Intro -->|onPause/onStop/onSaveInstanceState| Bg["background"]
  Onb -->|onCreate $2 coroutine| MainVM["MainViewModel.F()"]
  Onb -->|onPause| Main["MainActivity"]
  Main -->|onCreate| B["MainActivity.B() -> com.getmimo.ui.main.d"]
  Main -->|onStart/onPostCreate/onResume| Resume["MainViewModel.I(true), H(), onResume"]
  Main -->|bottom nav setActive| Nav["NavigationBar.setActive(Path/Practice/Leaderboard/Profile)"]
  Main -->|onPause/onStop/onDestroy (back)| Onb2["OnboardingActivity onRestart/onResume (incomplete onboarding stack)"]
  Main -->|force-stop + cold start offline| Intro2["IntroSlidesActivity (network none)"]
```

M09 evidence: `activity_onCreate/onStart/onPostCreate/onResume` for
`IntroSlidesActivity`, `OnboardingActivity` and `MainActivity`; `onStop/onDestroy` for
`SplashActivity`; `onRestart` for `OnboardingActivity` after back; and the offline cold
start returned to `IntroSlidesActivity` [E29].

## 3. Background / workers (VERIFIED_RUNTIME + VERIFIED_STATIC)

| Component | Evidence | Status of trigger |
|---|---|---|
| `com.getmimo.data.source.remote.authentication.PostVisitWorker.a()` | M09 `entry` with `this_fields {g: authentication.a, h: kf.c}` | executed once; periodicity/constraints UNKNOWN |
| `.data.notification.MimoFirebaseMessagingService` | M09 `activity_inventory` | VERIFIED_STATIC |
| `MimoStreak{Large,Medium,Small}WidgetReceiver` | M09 `activity_inventory` | VERIFIED_STATIC |
| `StreakWidgetRefreshWorker`, `AccountDeleteWork`, `AsyncRequestWorker` | M06 class census | UNKNOWN triggers |
| 6 `SplashActivity_*` aliases (`_default`, `_bat`, `_chemist`, `_ninja`, `_proud`, `_ukraine`) | M09 `activity_inventory` (12 entries) | VERIFIED_STATIC |

No Hilt/Dagger/Koin/WorkManager scheduling metadata was decoded; do not infer periodicity.

## 4. Startup / persistence / restart semantics

* Room bootstrap observed **online and offline**: `PRAGMA user_version;` ->
  `SELECT count(*) FROM sqlite_master ...` -> three `CREATE TABLE` -> `room_master_table`
  identity insert -> `PRAGMA user_version = 2` -> `PRAGMA query_only/temp_store/recursive_triggers`
  -> Room temp invalidation triggers [E29, E27].
* **`DELETE FROM lesson_progress WHERE in_queue = 1` executed at startup in M09**
  (SQL event seq 260, online), followed by `SELECT * FROM lesson_progress`,
  `DELETE FROM lesson_progress WHERE lesson_id IN ()`, and
  `SELECT COUNT(DISTINCT chapter_id) FROM chapter_completions` [E29]. This closes the
  M07/M08 queue anomaly: the cleanup is a **normal startup statement**, not a network
  acknowledgement; when it does not run (app never reaches the startup path) rows survive.
* Offline cold start (`Active default network: none`, `airplane_mode_on=1`) reopened
  `IntroSlidesActivity`; reconnect gave `Active default network: 102`. No server
  acknowledgement was observed. `SERVER CONFIRMED = 0`.

## 5. Interruption / restart matrix

| Interruption | Measured effect | Classification |
|---|---|---|
| Back from lesson | quit dialog (`Quit / Choose / Cancel`) then path map | VERIFIED_RUNTIME [E14] |
| Force-stop + cold start offline | `mimo.db` intact, UI back at intro | VERIFIED_RUNTIME [E26, E29] |
| Network loss mid-session | `NetworkUtils.a()` flips; learning continues from assets | VERIFIED_RUNTIME [E26] |
| `in_queue=1` rows at startup | deleted by DDL statement (M07/M09) or retained (M08 run4) | VERIFIED_RUNTIME (both paths) |
| Process death during `postUnsyncedLessonProgress` | coroutine returns `COROUTINE_SUSPENDED`; no result captured | UNKNOWN |
