# MIMO 9.35 — FINAL UNKNOWN REGISTER

**Document:** `FINAL_UNKNOWN_REGISTER.md` · **Mission:** MISSION 09 (final reconstruction) · **Branch:** `arena/aebb90b7-game`
**Target APK:** `com.getmimo` 9.35, `versionCode=1792759685`, 142,353,499 B, SHA-256 `48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a` — unchanged.
**SERVER CONFIRMED = 0.** Classification vocabulary: `VERIFIED_STATIC`, `VERIFIED_RUNTIME`, `VERIFIED_ASSET`, `VERIFIED_DATABASE`, `VERIFIED_NETWORK_OBSERVATION`, `INFERRED`, `UNKNOWN`, `SERVER_DEPENDENT`.
Evidence codes resolve in `COMPLETE_EVIDENCE_DATABASE.json` / `COMPLETE_SYSTEM_MAP.json -> evidence_index`.

---


## 0. How to read this register

Everything **technically resolvable from the client** has been resolved and is in the 19
deliverables. What remains is either (a) server-owned, (b) requires legitimate
authentication, (c) was not reachable in a controlled emulator run, or (d) explicitly
out of scope. Each entry states the exact missing evidence and its closure condition.
`SERVER CONFIRMED = 0`. **No further broad discovery mission is recommended.**

## 1. Gaps CLOSED in MISSION 09

| Gap | Closure |
|---|---|
| A — navigation / MainActivity state machine | M09 captured 23 `MainActivity.B()` entries returning `com.getmimo.ui.main.d` with its live field graph, `NavigationBar.setActive` with the exact 4-route destination map, `MainViewModel.F/I/H`, 28 direct Activity lifecycle events. |
| C — queue anomaly | M09 SQL hook captured `DELETE FROM lesson_progress WHERE in_queue = 1` at startup; explains M07 2->0 and M08 run4 2->2 (MainActivity never reached). |
| D — progression collaborators | M09 captured live `com.getmimo.interactors.path.d` `this_fields` (tracks, local completion, IAP purchase, dev prefs, section classifier, keys) and `PathMapViewModel` call `b(50,0,null,...)`. |
| E — economy boundary | M09 captured `Coins.getCoins()=0`, `RefreshPathToolbarState` remote coin/key flows, `reward_retrieve.c`, and `streak_getData` -> `AccessTokenUnavailableException`. No local award formula exists. |
| F — network contract | 53 endpoints with DEX-resolved verbs (M05 heuristic `n`/`p`/`b` labels corrected); 17 third-party-only `net` events; zero Mimo `/v1/` observations. |
| G — auth layers | Practice = UI-only gate; streak = repository-level `AccessTokenUnavailableException`. |
| H — lifecycle | API-36-safe direct Activity hooks worked (181 hooks, 28 nav events); `PostVisitWorker.a()` observed. |
| J — curriculum integrity | 10,298 tutorial JSON files validated; 0 parse failures / missing refs / duplicates / orphans; 4 locale discrepancies reported; normalized graph built. |
| K — algorithms | A1–A20 with signature, inputs, outputs, state, side effects, pseudocode, evidence, confidence, edge cases. |
| L — instrumentation | `real_target_method_executed=true` (72 `entry` events, 71 `exit`, 86 SQL, 17 DI, 19 LiveData). |
| Instrumentation success criterion | `server_active=true`, `attach_ok=true` (pid 3348 / `Mimo`), 72 real `com.getmimo` method entries. |

## 2. Remaining unknowns

| ID | Unknown | Classification | Why it remains (evidence) | Exact closure condition | Where handled |
|---|---|---|---|---|---|
| `U-ECON-001` | Absolute XP / streak / keys / reward / daily-goal award formulas and thresholds | SERVER_DEPENDENT + UNKNOWN | No XP/score/streak/key column in mimo.db; d0()/f0()/V()/W() have no arithmetic; Coins.getCoins() returned 0 on fresh install while M08 had local_coins=200; RefreshPathToolbarState pulls from remote coins/keys repositories; streak_getData threw AccessTokenUnavailableException in M09. | Capture a real authenticated `PostProgressResponse` and the exact int arithmetic in MainViewModel/reward repositories, with an input->output table. No legitimate auth was available. | COMPLETE_ECONOMY_SPEC.md §1 F13-F20; interface `AwardPolicy` (design choice) |
| `U-PROG-001` | Exact live unlock boolean in GetPathMapState (tier, keys, progress combination) | VERIFIED_STATIC (shape) + UNKNOWN (boolean) | 659-instruction method decoded; collaborators measured live in M09 (tracks.c, local completion.a, remote iap purchase.a, sk.a dev prefs, cc.b classifier, keys.a); no live Locked/UnlockedButNoKeys decision and no key value observed. | Reach a chapter that requires keys/premium with a real account and capture the branch PCs 0x04aa/0x4f0/0x51a/0x608 with inputs and resulting vn/d0|e0|h0|g0. | COMPLETE_PROGRESSION_ENGINE_SPEC.md §7 UnlockPolicy interface + offline fallback |
| `U-PROG-002` | Chapter/tutorial completion transition and next-chapter unlock at runtime | UNKNOWN | chapter_completions stayed 0 rows; 868 tutorial_completions rows all is_completed=0 in every M07/M08/M09 snapshot; no chapter-end screen reached. SQL and DAO signatures are known. | Finish every lesson of one chapter under instrumentation and capture the INSERT into chapter_completions plus the path-map state change. | COMPLETE_PROGRESSION_ENGINE_SPEC.md §5; blueprint deterministic next-chapter rule |
| `U-PROG-003` | Practice / redo / challenge / review behaviour | VERIFIED_ASSET (content) + UNKNOWN (behaviour) | Content types and LessonBundle flags exist; guest Practice is UI-gated; no practice lesson entered. | With a legitimate account, enter a practiceLevel1/2/3 and a challengeLevel0/1/2 chapter. | Blueprint treats modes as content variants; no invented scoring |
| `U-LESSON-001` | Runtime dispatch of V()/W()/X(), jm/m|n|o feedback objects and native validator selection | VERIFIED_STATIC (bodies) + UNKNOWN (dispatch) | M07 stage 6 and M09 observed U()->H() instead; no onLessonRun$1, V/W/X, d0, jm/m|n|o or native selection-submit event fired. | Trigger each of the 9 interaction families to a wrong/correct submission with hooks on Y(Z), V/W/X and the feedback LiveData. | COMPLETE_LESSON_ENGINE_SPEC.md §4/§5 pseudocode (static, faithful) |
| `U-WEB-001` | Native WebView bridge object, method names, payload schema, callbacks | VERIFIED_ASSET (JS side) + UNKNOWN (native side) | lesson-webview.js posts 5 message kinds; M07 stage 6 had 0 addJavascriptInterface events; M09 added 5 WebView hooks but recorded 0 webview events because no lesson was reached. | Enter an InteractiveWebView lesson with the M09 agent attached and capture loadDataWithBaseURL/evaluateJavascript/addJavascriptInterface plus the JS payload. | COMPLETE_UI_RENDERER_CATALOG.md §3; blueprint defines an independent bridge |
| `U-NATIVE-001` | JNI / native library internals and remote code-runner boundary | UNKNOWN (explicit scope) | 12 arm64 .so shipped; M09 observed loadLibrary("conscrypt_gmscore_jni"); POST /v1/code/runfiles exists; q.I() provides an offline comparison. | Out of scope by user direction; only needed if code execution must be reproduced. | Blueprint `CodeSandbox` interface + offline `q.I()` validator |
| `U-STATE-001` | Jetpack DataStore user_preferences.preferences_pb protobuf semantics | VERIFIED_RUNTIME (file present) + UNKNOWN (schema) | File captured byte-for-byte in M07/M08/M09 snapshots; key names only from static strings. | Decode the protobuf schema and map each key to its reader/writer. | COMPLETE_LEARNER_STATE_SPEC.md §4; Settings object fields are known |
| `U-LIFE-001` | Worker triggers / periodicity / constraints | VERIFIED_STATIC (classes) + UNKNOWN (schedule) | PostVisitWorker.a() executed once in M09; widget receivers and Firebase service listed; no WorkManager scheduling metadata decoded; no DI framework metadata. | Decode WorkRequest constraints/intervals or observe a full work cycle. | COMPLETE_AUTH_AND_LIFECYCLE_SPEC.md §3 |
| `U-NAV-001` | Clean Leaderboard / Profile destination screens for a guest | VERIFIED_RUNTIME (dispatch) + UNKNOWN (screen contents) | NavigationBar.setActive destination map measured; M09 route tour taps resumed an incomplete OnboardingActivity back stack after the explicit-intent MainActivity; M08 route tours recorded 7 route_not_found on ChapterActivity/intro. | Complete onboarding naturally on this build, then tour all four tabs with the back stack clean. | COMPLETE_NAVIGATION_STATE_MACHINE.json; COMPLETE_UI_RENDERER_CATALOG.md §1 |
| `U-NET-001` | Real Mimo backend request/response bodies, status codes, auth and retry | SERVER_DEPENDENT | 53 endpoints and DEX-resolved verbs are client-side only; 0 Mimo /v1/ URLs observed; only third-party SDK URLs captured; SERVER CONFIRMED=0. | Legitimate authenticated capture with server cooperation. Explicitly not attempted. | COMPLETE_NETWORK_API_CONTRACT.md §2/§6 |
| `U-QUEUE-001` | Which startup path chooses DELETE vs UPDATE for in_queue rows | CLOSED (behaviour) / UNKNOWN (precise caller ordering) | M09 captured `DELETE FROM lesson_progress WHERE in_queue = 1` executing at startup online (SQL seq 260) plus `repo_postUnsyncedLessonProgress` entry returning COROUTINE_SUSPENDED. M07 stage4/5 saw the same DELETE offline; M08 run4 retained rows because it never reached MainActivity (main_activity_reached=false), so cleanup never ran. | Only the caller ordering between the two DAO statements remains; behaviour is explained. | COMPLETE_LEARNER_STATE_SPEC.md §5; blueprint [D] durable queue |

## 3. What is definitively NOT unknown

* Shipped curriculum graph, asset schema, DSL tags, renderer families, all validator bodies.
* Room schema, SQL statements, identity hash, migrations shape, SharedPreferences keys,
  `Settings` object fields, progress row construction, `isSolvedCorrectly()`.
* Startup chain, Activity lifecycle, bottom-nav destination dispatch, `MainViewModel` field graph,
  `GetPathMapState` collaborators, `NavigationBar.setActive` map.
* Offline matrix, connectivity gate, queue cleanup SQL, `NoConnectionException`.
* 53 client endpoints, DEX-backed HTTP verb mapping, third-party endpoint separation.
* Guest Practice UI gate and repository-level streak auth gate.
* The fact that no server response was ever observed.

## 4. Verdict

**An independent offline learning client CAN be implemented** to behavioural fidelity for
everything client-side. The remaining unknowns are server-authoritative or require a real
account; they are fenced by explicit interfaces and deterministic offline fallbacks that are
clearly labelled as independent design choices. This is not 100% reverse engineering of the
whole product, and no claim to that effect is made.
