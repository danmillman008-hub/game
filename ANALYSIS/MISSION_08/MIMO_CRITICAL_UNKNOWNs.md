# MIMO 9.35 — CRITICAL UNKNOWNS (MISSION 08)

**Target:** original APK `com.getmimo` 9.35, 142,353,499 B, SHA-256
`48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a` — unchanged.
**Scope:** only the material unknowns that block a complete implementation-level
reconstruction of the *central execution paths*. Anything below is deliberately `UNKNOWN`,
not guessed from bytecode. `SERVER CONFIRMED = 0`. Evidence codes resolve in
`MIMO_SYSTEM_MAP.json -> evidence_index`.

## Evidence status of this run

| Item | Value |
|---|---|
| Broad run | `42042312640`, 275 events, SUCCESS, no Frida method events (server binary not pushed); reached MainActivity, ChapterActivity, FTG code editor and quit dialog |
| Targeted run 2 | `42046336206`, 485 events, Frida attach OK (3 processes), 63 hooks per process, live DI / Fragments / Room SQL / Settings / network URLs; onboarding stalled on a Compose screen |
| Targeted run 3 | `42049141553`, 176 events; natural post-onboarding state restored (82 files, 2 `lesson_progress` rows, `local_coins=200`) but the app still opened the IntroSlides carousel; the route loop hit a keyword collision and aborted |
| Final run 4 | `42050715150`, 274 events; bounded, state-aware "Get started" navigation to reach MainActivity, keyword collision fixed |
| Unified stream | `MIMO_RUNTIME_TIMELINE.jsonl` — 1034 events, 176 repetitive events collapsed |
| Navigation | 46 screens / 45 edges in `MIMO_NAVIGATION_GRAPH.json` |
| State snapshots | 14 natural (non-synthetic) Room/preferences snapshots |

## 1. Absolute scoring / XP / streak / rewards — highest priority

`VERIFIED_STATIC` classes exist (`Coins.getCoins`, `LessonProgressQueue` counters,
`DefaultStreakRepository`, `DefaultRewardRepository`, `MainViewModel E/F/G/H/I`,
`SettingsRepository.getUserDailyGoal`), and `local_coins={"coins":200}` is a real persisted
value [E11, E13, E20]. **Missing:** a single observed event exposing input → calculation →
output → storage for an XP/coin/streak award. `local_coins` was constant across
14 snapshots, so a per-lesson increment was NOT demonstrated. No XP column exists in
`mimo.db`. The award formulas depend on `PostProgressResponse` / `Progress` /
`TrackEtaResponse` server bodies that were deliberately not reconstructed.
**Why it matters:** without it the "Scoring → Next Activity" half of the priority chain is
only structurally known. Precise pointer: `MainViewModel$confirmRewardAndLookForNewRewards$1`,
`MainViewModel$fetchRewards$1`, `/v1/user/rewards/next`.

## 2. Live unlock boolean and key values

`ds/w.c(Set,J,J,J)` = membership of `"<trackId>:<tutorialId>:<chapterId>"` in a key set from
`DefaultKeysRepository` is `VERIFIED_STATIC` [E20]; path-map states and the sequential
required-tutorial prerequisite are decoded [E10]. **Missing:** a runtime observation of
`GetPathMapState$invoke$3` (659 instructions, branches at PC `0x04aa`, `0x4f0`, `0x51a`,
`0x608`) or `CanOpenChapterWithKeys$invoke$1` @10104004 deciding `Locked` vs
`UnlockedButNoKeys` vs `Unlocked`, and any real key value. No key was seeded (that would be
synthetic state without exposing the algorithm).

## 3. Native validator dispatch and feedback objects

`V()`/`W()`/`X()`/`d0()` and `jm/m`, `jm/n`, `jm/o` are decoded statically [E09], and M07
stage 6 proved the WebView letter exercise uses `U()/H()` **instead** [E06]. **Missing:** a
submitted native `validatedInput` / `fillTheGap` / `selection` answer that actually reaches
`onLessonRun$1`, with the resulting LiveData feedback object and UI. Phase 1 reached the
fill-the-gap code-editor lesson and located the measured `<button>Like</button>` snippet
(`S151_onboard_23_after.xml`), but its exploration stalled on `btn_lesson_close`; phases 2–4
never reached a native lesson. If no `V/W/X` entry appears in the unified timeline, this
remains `UNKNOWN`.

## 4. Chapter / tutorial completion transitions

`chapter_completions` stayed 0 rows and `tutorial_completions` held 868 `is_completed=0`
rows in every snapshot [E13]. No chapter-end screen, no `is_completed=1` row, no
`ChapterFinishedSuccessType` transition was observed. `CompletionRepository.b(Track, cont)`
and `ChapterFinishedViewModel.R` are `VERIFIED_STATIC` only [E10, E20].

## 5. Code execution and WebView bridge

`q.I()` compares user files with shipped `solvedContent` offline, and `/v1/code/runfiles`
endpoints exist [E04, E09]. **Missing:** `WebView.addJavascriptInterface` payloads
(M07 stage 6 had zero events), the exact local-WebView vs remote-runner routing, the remote
runner's test/result feedback, and any JNI/native execution inside the 12 shipped `.so`
libraries (`libsigner.so`, `librive-android.so`, `libsqlcipher.so`, …). Native signing,
JNI method tables and the native↔Kotlin API are `UNKNOWN` by explicit scope [E10].

## 6. Sync / cold-start queue semantics

Both M07 stage 6 (offline) and M08 phase 1 (online, `Active default network: 102`) measured
`in_queue=1` rows disappearing at a cold start [E07, E11]. **Counter-observation:** in the
final M08 run the restored natural state kept `lesson_progress=2` across a force-stop and
cold start (`P3_S0_RESTORED` → `P3_S4_AFTER_RESTART`, all `db_diff` deltas empty,
`Active default network: 102`) [E22]. The deletion is therefore **not universal** and cannot
be attributed to a single trigger; it may depend on account/session state. **Missing:** isolation of whether
the DELETE was preceded by a successful `POST /v1/tutorials/{id}/progress` (and its
acknowledgement) or was a local `DELETE FROM lesson_progress WHERE in_queue = 1`. No server
response was observed or fabricated; `SERVER CONFIRMED = 0`. This is why earlier "queued-row
restore" expectations are not claimed.

## 7. DI framework, worker triggers and DataStore contents

No `@Inject`/Hilt/Koin metadata was decoded; only `Lhm/b;` 13-slot container and two
generated `_Factory` classes are known, so the framework/scopes are `UNKNOWN` [E02].
`PostVisitWorker`, `StreakWidgetRefreshWorker`, `AccountDeleteWork`, `AsyncRequestWorker`
names are `VERIFIED_STATIC` but no trigger/periodicity was observed [E10].
`user_preferences.preferences_pb` is present but its protobuf was not decoded in M08; the
DataStore key names come from M06 static strings only [E13].

## 8. Screens and states deliberately not reached

Leaderboard content, Profile/Settings screens, streak modal, purchase/paywall, account
creation, native correct/wrong feedback after a submitted selection, and the chapter-end
screen. `AuthenticationActivity` was passed with `Skip` (guest), so authenticated practice,
sync and leaderboard behaviour were not exercised — no credentials or auth bypass were used.

## 9. Instrumentation limitations (recorded, not hidden)

- Phase-1 run `42042312640` produced **no Frida method events**: the GitHub release asset
  download failed silently, `adb push` could not stat `frida-server`, and
  `dev.attach()` returned `unable to connect to remote frida-server: closed`
  [E16 `PHASE1_FRIDA_SETUP_42042312640.txt`]. All 275 phase-1 events are therefore UI /
  navigation / DB / orchestrator evidence, not method-level evidence.
- Phase 2 fixes this with three independent download paths, an `lzma` decompressor, a
  `pkill` + fresh device install, and an **actual attach preflight** before the orchestrator
  starts [E16 `PHASE2_FRIDA_SETUP_42046336206.txt`]. If the preflight is `attach_ok=false`, the phase-2
  timeline itself records the failure and method-level claims stay `UNKNOWN`.
- `dumpsys activity top` on this API-36 image exposed Launcher3 item dumps rather than
  Mimo fragments, so the `fragments` field of most screens is `UNKNOWN`. The onboarding
  subgraph's Fragment/ViewModel chain was recovered instead from Frida
  `androidx.lifecycle.m0.k` LiveData posts. Activities come from `dumpsys activity
  activities` (`topResumedActivity`); the attempted Frida `ActivityLifecycleCallbacks`
  hook never registered.
- `uiautomator2` was probed successfully but **not adopted**: adb hierarchy dumps +
  `dumpsys activity activities` + Frida LiveData posts already provided the required
  evidence [E11, E16].
- Phase 2's state-aware onboarding replay stalled at a Compose screen whose nodes are not
  exposed by `uiautomator dump` (three identical empty hierarchies). Rather than repeat it,
  phase 3 restored the naturally generated post-onboarding private state from run
  `42042312640` before launching. No synthetic learner rows were inserted; the restore is
  tagged `synthetic=false` in the timeline and in the learner-state schema.
- `Java.registerClass` for `Application$ActivityLifecycleCallbacks` failed on API 36
  ("Missing implementation for onActivityPostStarted …"), so Activity names come from
  `dumpsys activity activities` and Fragment names from `LiveData` posts instead.
- `okhttp3.OkHttpClient.newCall` is not present under that name after R8; only
  `java.net.URL.openConnection` produced network events. Hence the absence of a Mimo
  `/v1/...` request is an observation limit, not proof that no request occurred.
- A third-party launcher overlay ("This release is provided by …", with a countdown and
  "Do not show again.") appeared on cold start in phase 2. Its origin is `UNKNOWN` and no
  claim is made about it; it was waited out / dismissed as a UI obstacle only.
- The final run's first `uiautomator dump` returned no hierarchy (`restored_state_screen`
  activity `null`), so the bounded "Get started" loop stopped at step 0. Later dumps in the
  same run did show the intro carousel with two clickable nodes, but no further tapping was
  attempted: after four runs this was judged an ineffective path, and repeating it would add
  no architecture evidence. `main_activity_reached=false` is recorded explicitly.
- No `SERVER CONFIRMED = 1` result exists anywhere in M01–M08. All HTTP verb labels are
  static R8 annotation inferences, not observed requests.
- No snapshot contains synthetic learner rows. One harness-level experiment flag
  (`experiments.xml:experiment_adapted_onboarding_android_local=original`) was seeded to
  select the original onboarding variant; it is not learner progress and is tagged
  `synthetic=true` on that single key in `MIMO_LEARNER_STATE_SCHEMA.json`, while
  `synthetic_state_used` for the learner state is `false`. The phase-3/4 restore copied a
  naturally generated private tree (82 files, 2 `lesson_progress` rows) without inserting
  rows.

## Closure criterion

Investigation stops here: the main architecture, module communication, navigation state
machine, lesson engine, validators, learner state, offline/sync boundary, progression,
local scoring counters, media/code-execution boundaries and the central
`Navigation → ViewModel → Repository → Core Logic → Learner State → Scoring → Next Activity`
chain is established with real evidence **for the measured lesson-answer path**
(M07 stage 6: `U()` → `H()` → `LessonProgressRepository` → `LessonProgressQueue` →
`f0()`/`N()`), and the surrounding architecture, navigation graph and stores are measured.
The bottom-nav → ViewModel → Repository segment and the scoring/next-activity half remain
`VERIFIED_STATIC` / `UNKNOWN` at method level, because runs 2–4 never reached
`MainActivity`. The remaining items are server-owned or require authenticated/native
execution paths that were deliberately not fabricated. Closing M08 here is an explicit
scope decision after four runs, not a claim that those paths were observed.
