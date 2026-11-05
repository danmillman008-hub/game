# MIMO 9.35 — COMPLETE CLIENT-SIDE ARCHITECTURE

**Document:** `COMPLETE_CLIENT_ARCHITECTURE.md` · **Mission:** MISSION 09 (final reconstruction) · **Branch:** `arena/aebb90b7-game`
**Target APK:** `com.getmimo` 9.35, `versionCode=1792759685`, 142,353,499 B, SHA-256 `48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a` — unchanged.
**SERVER CONFIRMED = 0.** Classification vocabulary: `VERIFIED_STATIC`, `VERIFIED_RUNTIME`, `VERIFIED_ASSET`, `VERIFIED_DATABASE`, `VERIFIED_NETWORK_OBSERVATION`, `INFERRED`, `UNKNOWN`, `SERVER_DEPENDENT`.
Evidence codes resolve in `COMPLETE_EVIDENCE_DATABASE.json` / `COMPLETE_SYSTEM_MAP.json -> evidence_index`.

---


## 0. What this document is

An implementation-level description of the **client** only. It answers all 22 questions in
the MISSION 09 primary objective by resolving them to a component, an algorithm, a data store
and an evidence class. Server-owned behaviour is explicitly fenced off; no backend is
reconstructed. `SERVER CONFIRMED = 0`.

MISSION 09 runtime run `42077425594`: 691 timeline events. Instrumentation proof: `{"seq": 689, "ts_mono_ms": 284854.774, "ts_utc": "2026-11-05T17:52:13.776Z", "experiment_id": "EXP-M09-005", "action_id": "ACT-0031", "source": "orchestrator", "event": "instrumentation_proof", "server_active": true, "attach_ok": true, "hook_installed_events":`. MainActivity reached: `{"seq": 395, "ts_mono_ms": 186334.805, "ts_utc": "2026-11-05T17:50:35.256Z", "experiment_id": "EXP-M09-001", "action_id": "ACT-0021", "source": "orchestrator", "event": "main_activity_reached", "reached": true, "activity`. Lesson matrix executed: `{"seq": 526, "ts_mono_ms": 258667.306, "ts_utc": "2026-11-05T17:51:47.589Z", "experiment_id": "EXP-M09-003", "action_id": "ACT-0031", "source": "orchestrator", "event": "lesson_entry_result", "reached_chapter": false, "r`.

## 1. Startup (VERIFIED_RUNTIME + VERIFIED_STATIC)

1. Launcher activity `.ui.SplashActivity_default` (alias) starts the process.
2. `com.getmimo.App.onCreate()` (`Lcom/getmimo/App;`, 6 methods, 13 collaborator fields)
   builds the object graph. `App$onCreate$1` / `App$onCreate$2$1` are the coroutine bodies
   launched from `onCreate` [E02, E31].
3. `androidx.room` / `androidx.datastore` initialise; `mimo.db` is opened in WAL mode.
   Runtime bootstrap SQL captured in M08 phase 2: `PRAGMA user_version;` -> three
   `CREATE TABLE IF NOT EXISTS` -> `INSERT OR REPLACE INTO room_master_table
   (id,identity_hash) VALUES(42,'2b8ab6d303d9a501bd8c8fb78d8352fc')` ->
   `PRAGMA user_version = 2` [E12, E27].
4. First measured Activity after cold start is `.ui.onboarding.intro.IntroSlidesActivity`
   (3-slide carousel with `Get started` / `I already have an account`) [E11, E14].
5. For a fresh install: `OnboardingActivity` (single `NavHostFragment`) -> 
   `AuthenticationActivity` (`Skip` = guest) -> `MainActivity` -> `ChapterActivity` [E11, E12].

**Startup side effects measured:** `experiments.xml` selects the original onboarding
variant; `mimo_prefs.xml` gains `user_profile_created_at`, `user_settings`,
`favorite_tracks`, `local_coins={"coins":200}`; `tutorial_completions` is seeded with 868
`is_completed=0` rows for the selected tracks; `lesson_progress` starts at 0 rows [E11, E13, E26].

## 2. Application-state initialisation and dependency injection

`Lcom/getmimo/App;` holds 13 collaborators (`x30.g`, `df.c`, `com.getmimo.analytics.a`,
`be.d`, `q9.f`, `i9.h`, `lf.a`, `ke.a`, `kf.c`, `be.a4`,
`com.getmimo.data.source.remote.authentication.a`, plus `A=0`, `a=true`). These were read
from the **live** instance with `Java.choose` in M08 phase 2 (30 DI events) [E12].

There is **no decoded Hilt/Dagger/Koin metadata** (CLASS_CATALOG has 0 Hilt/Dagger/Koin/
`javax.inject` entries, 2 `_Factory` classes). The verified mechanism is:

* a hand-rolled 13-slot `Ljava/lang/Object;` container `Lhm/b;` (`a`..`m`) passed to
  `InteractiveLessonBaseViewModel(Lhm/b;)V` and cast at each use site: `b` -> analytics,
  `d` -> `LessonProgressRepository`, `g` -> local source, `h` -> filesDir, `i` -> sound [E02];
* constructor injection for large graphs: `ExecutableLessonViewModel` (32 parameters),
  `GetPathMapState` (15 collaborators), `LessonProgressRepository` (7 collaborators),
  `LessonProgressQueue_Factory` / `LessonProgressRepository_Factory` [E02, E31].

**Classification:** `VERIFIED_STATIC` for the container and signatures, `VERIFIED_RUNTIME`
for the live `App` fields, `INFERRED` for compile-time DI, `UNKNOWN` for exact framework,
scopes and singleton graph. This gap does **not** block an independent implementation: a
plain service locator / manual constructor graph reproduces the observed behaviour.

## 3. Learner representation

The learner is **not** a Room entity. It is a union of:
`mimo_prefs.xml` (SharedPreferences: `local_coins`, `favorite_tracks`, `user_settings`,
`favorite_tracks_to_sync/remove`, `user_profile_created_at`, `marketing_network/campaign`),
`files/datastore/user_preferences.preferences_pb` (Jetpack DataStore, protobuf **not decoded**),
`no_backup/` (Firebase / RevenueCat / Mixpanel caches), and the three Room progress tables.
`Settings(dailySparksGoal, hasProgrammingExperience, dailyReminderTime, notificationSettings,
name, biography, userId, hadFreeProTrial, hadFreeMaxTrial)` was observed written through
`com.getmimo.data.settings.a.l(Settings)` with only `hasProgrammingExperience=false` set [E12].
No user id / auth token was read or stored by the analysis; all token keys are redacted [E13].

Full field-level spec: `COMPLETE_LEARNER_STATE_SPEC.md` and
`ANALYSIS/MISSION_08/MIMO_LEARNER_STATE_SCHEMA.json`.

## 4. Curriculum loading and next-lesson selection

`tracks.json` (v753, 357,063 B in the APK) is the root index: 19 tracks, each with ordered
`sections` carrying `startIndex`/`endIndex`/`tutorialIds`. Each `tutorial-<id>.json` has a
single root key `{"tutorial": {...}}` with `id, version, type, codeLanguage, title, chapters`.
Each chapter carries `id, title, type, lessons`; each lesson carries
`title, id, contentType, images, interactiveContent, hardModeSelected, hardModeContent,
executableContent` [E23, E24].

Loader chain (static): `Lye/b.b(J)` opens `lessons-<lang>/tracks/tutorial-<id>.json` through
`AssetManager.open`; `DefaultTrackLoader.a(J,I,I)` decodes with `kotlinx.serialization`;
`Lte/c.b(String)` parses the lesson HTML/XML DSL with `XmlPullParserFactory` [E09, E25 §N].

**Ordering rule (VERIFIED_ASSET):** lessons are strictly ordered by
`chapter.lessons[]` index, chapters by `tutorial.chapters[]`, tutorials by
`section.tutorialIds[]`, sections by `startIndex`. There is **no randomization** in the
shipped index; the `COMPLETE_CURRICULUM_GRAPH.json` `prerequisiteLessonId` /
`prerequisiteChapterId` fields encode the deterministic chain [E23].
`LessonBundle` measured at runtime: `lessonId=151410 lessonIndex=0 chapterIndex=0
chapterId=17742 tutorialId=904 trackId=219 trackVersion=82 tutorialVersion=161
tutorialIndex=0 tutorialType=Learn chapterType=PRACTICE_LEVEL_1
isChapterAlreadyCompleted=false isLastLesson=false isPracticeRedo=false
isChallengeRedo=false sectionIndex=0` [E28].

Next-lesson selection at runtime is `nextPage.value = lessonBundle.chapterIndex` after
`Y(Z)` completes (static), and `e = chapterIndex` after `f0()/N()` (M07 stage 6) [E25 §A, E06].

## 5. UI execution technologies (VERIFIED_RUNTIME + VERIFIED_STATIC)

Hybrid: Android Views + Fragments + AndroidX `ViewModel`/`LiveData`
(`androidx.lifecycle.m0` after R8), plus Jetpack Compose + Orbit MVI for the path map and
executable lessons. `MainActivity` hosts `main_activity_root`, `contentFrame`,
`bottom_navigation_view` and swaps in `anonymous_user_lock_view` (Compose) for guests on the
Practice tab [E14]. `ChapterActivity` hosts `vp_lessons` (ViewPager) and
`container_lesson_interactive` [E14]. WebView hosts embedded HTML activities; Rive,
highlight.js/Prettier and 12 arm64 `.so` libraries provide media/editor support [E10, E33].

`uiautomator dump` does not expose Compose nodes reliably (three identical blank hierarchies
in M08 phase 2); M09 uses the **measured** phase-1 tap chain and direct Activity/Fragment
hooks instead [E12, E29].

## 6. Runtime / storage / network / lifecycle summary

| Concern | Implementation | Evidence class |
|---|---|---|
| State propagation | `LiveData` posts, `StateFlow` (`_answersInChapter`), `SharedFlow`, `SavedStateHandle`, coroutine `Continuation` | VERIFIED_STATIC + VERIFIED_RUNTIME |
| Local persistence | Room `mimo.db` (WAL), SharedPreferences, Jetpack DataStore, `no_backup/` caches | VERIFIED_DATABASE |
| Sync | `LessonProgressQueue` -> `LessonProgressRepository.postUnsyncedLessonProgress` -> `LessonProgressApi.postProgress`; `NetworkUtils.a()` gate | VERIFIED_STATIC + VERIFIED_RUNTIME |
| Background | WorkManager `CoroutineWorker`s, Firebase Messaging, services; triggers UNKNOWN | VERIFIED_STATIC / UNKNOWN |
| Network contract | 53 Retrofit-annotated endpoints; verbs from DEX `RequestFactory$Builder` | VERIFIED_STATIC |
| Lifecycle | startup cleanup of `in_queue=1` rows; state restored from Room/prefs; UI returns to path map after offline cold start | VERIFIED_RUNTIME |

See `COMPLETE_NETWORK_API_CONTRACT.md`, `COMPLETE_AUTH_AND_LIFECYCLE_SPEC.md` and
`COMPLETE_UI_RENDERER_CATALOG.md` for the full expansions.

## 7. Answer to the 22 primary-objective questions

| # | Question | Resolution | Class |
|---|---|---|---|
| 1 | How does the app start? | §1 | VERIFIED_RUNTIME |
| 2 | How is state initialised? | §2, §3 | VERIFIED_RUNTIME + STATIC |
| 3 | How is a learner represented? | §3, `COMPLETE_LEARNER_STATE_SPEC.md` | VERIFIED_DATABASE |
| 4 | How is curriculum loaded? | §4, `COMPLETE_CURRICULUM_GRAPH.json` | VERIFIED_ASSET |
| 5 | How is the next lesson selected? | §4 + `COMPLETE_PROGRESSION_ENGINE_SPEC.md` | VERIFIED_RUNTIME + ASSET |
| 6 | How are modules parsed? | `Lte/c.b` §N, `COMPLETE_LESSON_ENGINE_SPEC.md` | VERIFIED_RUNTIME |
| 7 | How does each renderer behave? | `COMPLETE_UI_RENDERER_CATALOG.md` | VERIFIED_RUNTIME + STATIC |
| 8 | How is every answer validated? | A6–A11, `COMPLETE_LESSON_ENGINE_SPEC.md` | VERIFIED_RUNTIME + STATIC |
| 9 | Correct/incorrect handling | A2/A3 + M07 stage5 WebView feedback | VERIFIED_RUNTIME |
| 10 | Attempts/completion recording | A4/A5 + M07 stage6 row | VERIFIED_RUNTIME |
| 11 | XP/coins/keys/streaks/rewards | `COMPLETE_ECONOMY_SPEC.md` | SERVER_DEPENDENT + UNKNOWN |
| 12 | Chapter completion | `COMPLETE_PROGRESSION_ENGINE_SPEC.md` | UNKNOWN (never observed) |
| 13 | Next chapter unlock | A17/A18 | VERIFIED_STATIC + UNKNOWN |
| 14 | Track progression | §4 + A17 | VERIFIED_ASSET + STATIC |
| 15 | Practice/redo/challenge/review | `COMPLETE_PROGRESSION_ENGINE_SPEC.md` | VERIFIED_ASSET + STATIC |
| 16 | Recovery after interruption/restart | §6, `COMPLETE_LEARNER_STATE_SPEC.md` | VERIFIED_RUNTIME |
| 17 | Local persistence | §6 | VERIFIED_DATABASE |
| 18 | Sync queue | A14/A19/A20 + `COMPLETE_LEARNER_STATE_SPEC.md` | VERIFIED_RUNTIME + UNKNOWN |
| 19 | Offline behaviours | `COMPLETE_NETWORK_API_CONTRACT.md` | VERIFIED_RUNTIME |
| 20 | Backend-required behaviours | `COMPLETE_NETWORK_API_CONTRACT.md` | SERVER_DEPENDENT |
| 21 | Auth-gated screens | `COMPLETE_AUTH_AND_LIFECYCLE_SPEC.md` | VERIFIED_RUNTIME |
| 22 | Components/algorithms to implement | `COMPLETE_IMPLEMENTATION_BLUEPRINT.md` | — |

## 8. Honest boundary

Everything client-side needed for an **independent offline learning client** is specified.
What remains outside that boundary: absolute award formulas, remote code-runner results,
subscription tier, authenticated practice/leaderboard, live unlock keys, DataStore protobuf
semantics, JNI internals and any server response. These are enumerated with closure
conditions in `FINAL_UNKNOWN_REGISTER.md`. `SERVER CONFIRMED = 0`.


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

### M09-closed architecture facts

* `MainActivity.B()` -> `com.getmimo.ui.main.d` (`MainViewModel`) with live fields
  `A=network.a`, `B/E=remote iap.b`, `G=remote keys.a`, `I=practice.c`,
  `J/K/L/M=capacity-64 channels`, `N=StateFlow`. `MainActivity` field `b="Max"`,
  `C=container_bottombar`, `h=true`, `x=true` [E29].
* `NavigationBar.setActive("Path(showStore=false, showDiscountDrawer=false,
  shouldSkipDialogRefresh=false)")` with destination map
  `2131361976=Path, 2131361974=Practice, 2131361973=Leaderboard,
  2131361975=Profile(scrollToPlayground=false)` [E29].
* `com.getmimo.interactors.path.d` (`GetPathMapState`) live collaborators:
  `tracks.c`, `local completion.a`, `remote iap purchase.a`, `sk.a` (dev prefs),
  `cc.b` (section classifier), `network.a`, `remote keys.a`, `local.a`; called from
  `PathMapViewModel$init$$inlined$flatMapLatest$1` as `b(50, 0, null, ...)` [E29].
* `RefreshPathToolbarState$refreshCoinsFlow$1` -> `remote coins.a.b()`;
  `$refreshKeysFlow$1` -> `remote keys.a.b()`; `sections.a` (unlock state) holds
  `coins.a`, `streak.a`, `keys.a`, `np.b` [E29].
* Startup SQL: `PRAGMA user_version=2`, 3 `CREATE TABLE`, `room_master_table`
  identity insert, Room temp invalidation triggers, then
  **`DELETE FROM lesson_progress WHERE in_queue = 1`** [E29].
