# MIMO 9.35 — CORE ARCHITECTURE (MISSION 08)

**Target:** original APK `com.getmimo` 9.35, `versionCode=1792759685`, 142,353,499 B,
SHA-256 `48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a` — unchanged.
**Branch:** `arena/aebb90b7-game`. **SERVER CONFIRMED = 0.**

This is an **implementation-level reconstruction of the connected client system**, not a
class catalogue. Every major claim below carries an evidence reference `E##` resolved in
`MIMO_SYSTEM_MAP.json -> evidence_index`, and a classification
`VERIFIED_STATIC` / `VERIFIED_RUNTIME` / `VERIFIED_BOTH` / `INFERRED` / `UNKNOWN`.
No backend, no credentials, no fabricated server responses, and no replacement application.

**Evidence base:** M01–M07 (APK/DEX, Androguard, curriculum decoder, Room SQL, Frida 17 Java
bridge, stage-6 runtime traces, 202-entry evidence DB) plus four M08 controlled runs:
`42042312640` (broad navigation/DB, 275 events), `42046336206` (Frida/DI/onboarding,
485 events), `42049141553` (natural-state restore, 176 events) and `42050715150`
(final targeted main-screen attempt, 274 events). Per-run counts above are the raw
timeline lengths; the unified stream below deduplicates repeated machine events.
The single unified stream `MIMO_RUNTIME_TIMELINE.jsonl` contains 1034 correlated events
(176 repetitive machine events collapsed). Classification mix: VERIFIED_RUNTIME=767, INSTRUMENTATION=250, UNKNOWN=17.
`MIMO_NAVIGATION_GRAPH.json` holds 46 measured screens and 45 transitions.
All four runs used the SAME orchestrator, the SAME curated 63-hook agent and the SAME
experiment/action ID scheme; the timeline carries `run_id`, `phase`, `experiment_id` and
`action_id` on every event so cross-run correlation is explicit rather than implicit.

---

## 1. Process entry, startup and dependency injection

The launcher is `.ui.SplashActivity_default`; the first measured Activity after a cold start
is `.ui.onboarding.intro.IntroSlidesActivity`, then `.ui.onboarding.OnboardingActivity` →
`.ui.authentication.AuthenticationActivity` → `.ui.main.MainActivity` →
`.ui.chapter.ChapterActivity` [E11, E14, E19]. `Lcom/getmimo/App;` has 6 methods and 13
collaborator fields typed by obfuscated interfaces (`Lx30/g;`, `Ldf/c;`, `Lbe/d;`, …);
`App$onCreate$1` and `App$onCreate$2$1` are the coroutine bodies started from `onCreate`
[E01, E02]. `MainActivity.B()` returns `Lcom/getmimo/ui/main/d;` (`MainViewModel`);
`ChapterActivity.B()` returns `ChapterViewModel` [E01].

**DI mechanism.** There is no decoded Hilt/Dagger/Koin metadata. What *is* verified is a
hand-rolled 13-slot `Ljava/lang/Object;` container `Lhm/b;` (`a`..`m`) passed into
`InteractiveLessonBaseViewModel(Lhm/b;)V` and cast at each use site: `b` →
`Lcom/getmimo/analytics/a;`, `d` → `LessonProgressRepository`, `g` →
`Lcom/getmimo/data/local/a;`, `h` → `Lmf/a;` (filesDir), `i` →
`Lcom/getmimo/ui/lesson/sound/a;` [E02]. Larger graphs use constructor injection, e.g.
`ExecutableLessonViewModel` (32 parameters), `GetPathMapState` (15 collaborators),
`LessonProgressRepository(LessonProgressApi, Lye/g, Lye/c, Lnp/d, Lri/d, completion/a, Lcg/a)`
and `LessonProgressQueue_Factory` / `LessonProgressRepository_Factory` [E01, E02].
`LessonProgressQueue_Factory` is the only decoded generated factory, so compile-time
constructor injection is `INFERRED`; **the exact framework, scopes and singleton graph remain
`UNKNOWN`**. Phase 2 additionally hooks the *live* `App` instance with `Java.choose` (30 DI events)
because an attach happens after `Application.onCreate`; this yields real field values instead
of inferred ones. The measured `com.getmimo.App` object held `A=0`, `a=true` and 13
collaborators including `com.getmimo.analytics.a`, `com.getmimo.data.source.remote.authentication.a`,
`x30.g`, `df.c`, `be.d`, `q9.f`, `i9.h`, `lf.a`, `ke.a`, `kf.c`, `be.a4`
[E12 `env application`, `di live_instance`]. `Java.choose` found 0 live instances of
`MainViewModel`, `PathMapViewModel` and `LessonProgressQueue` at attach time (they are created
later), so their field values remain `UNKNOWN`. The loaded-class inventory measured 36,498
classes: `okhttp3` 235, `com.getmimo` 104, `app.rive` 84–100, `com.google.firebase` 112–114,
`androidx.datastore` 127, `androidx.room` 11, `androidx.fragment` 28, `androidx.work` 1,
`retrofit2` 0 (R8-obfuscated) [E12 `env class_inventory`].

## 2. Layered module map and communication

`APK assets → loader → kotlinx.serialization → content models → XmlPullParser DSL →
LessonModule → gm.h.a() interaction type → Fragment/ViewModel → repository → Room / queue →
Retrofit API` [E09, E10]. Modules are plain Kotlin classes with `invoke` / suspend
`a(…, Continuation)` use-cases, not a framework; UI is a **hybrid** of
Fragments + AndroidX `ViewModel`/`LiveData` (`androidx.lifecycle.m0` after R8) and
Jetpack Compose + Orbit MVI (`org.orbitmvi.orbit`) for the path map and executable lessons
[E02, E10]. Communication is: `LiveData` posts for feedback/input state, `StateFlow`
(`_answersInChapter`) for counters, `SharedFlow` for interaction events, `SavedStateHandle`
for navigation arguments, and coroutine `Continuation` across repositories [E05, E10].
See `MIMO_SYSTEM_MAP.json -> modules` for the ten modules with exact signatures.

## 3. Navigation and UI state machine

Measured graph: 46 screens / 45 transitions [E15]. Onboarding is a
26-transition decision chain (goal → motivation → employment → work field → coding
experience → interest → path result → daily goal → reminder → device); choosing **Web apps**
yields the Front-End Developer path and shipped tutorial 904 (HTML), while **Data science**
yields Python Developer and shipped selection lesson 123420 [E11, E19]. The `Skip` at
`AuthenticationActivity` creates a **guest** profile (`user_profile_created_at` in
`mimo_prefs.xml`) and enters `MainActivity` [E11, E13].

`MainActivity` owns a four-tab bottom bar with measured resource IDs
`bottom_navigation_item_track` (`Learn`), `_practice`, `_leaderboard`, `_profile` [E14
`UI/S231_resume_02.xml`]. The **Practice tab for a guest** does not show practice content:
it renders `Lock in your learning / Create a profile to access practice content` — a real
client-side auth gate, not an inference [E11, E14 `S234_resume_02_after.xml`]. The path map
shows `Python Developer / 1. Intro to Python`, toolbar counters `200` and `0`, and section
progress `0/20`, `0/11`, `0/9`, `0/15` in the `Select Path` sheet [E14
`S229_resume_01_after.xml`, `S221_resume_00_after.xml`]. Back from `ChapterActivity` requires
an explicit `Quit lesson / Choose a different path / Cancel` confirmation
[E14 `S213_back_from_lesson_after.xml`]. Activities are identified from `dumpsys activity
activities` (`topResumedActivity`) on every screen event; the attempted Frida
`ActivityLifecycleCallbacks` hook produced 0 nav events because the API-36 interface
has extra default methods [E11, E12].

**M08 discovery — real Fragment/ViewModel controller chain.** `androidx.lifecycle.m0.k`
LiveData posts during onboarding exposed the actual Jetpack Navigation controller objects:
`NavHostFragment{...}` with `SavedStateHandlesVM` and `NavControllerViewModel`, followed by
`IntroductionFragment`, `SetMotiveFragment`, `OnboardingMotiveReassuranceFragment`,
`SetOccupationFragment`, `SetWorkFunctionFragment`, `SetExperienceFragment`,
`OnboardingSelectPathContainerFragment` and the pick-a-path bottom sheet
`com.getmimo.ui.onboarding.selectpath.pickapath.b`. Their `ViewModelProvider.DefaultKey`
entries name per-step ViewModels (`m7.f.a`, `com.getmimo.ui.onboarding.step2.b`, `f7.e`,
`un.d`) [E12 `liveData` events]. This closes M06's "exact navigation graph UNKNOWN" gap for
the onboarding subgraph: it is a single `NavHostFragment` inside `OnboardingActivity`,
not a separate Activity per step. `ActivityLifecycleCallbacks` registration itself failed on
API 36 because `Java.registerClass` must also implement the extra `onActivityPre*/Post*`
and `onActivityConfigurationChanged` default methods; that is recorded as a `hook_error`,
not silently dropped [E12].

## 4. UI rendering

`gm.h.a(List)` selects one of nine `LessonInteractionType`s (`InteractiveWebView`,
`FillTheGap`, `Spell`, `Selection`, `ValidatedInput`, `SingleChoice`, `MultipleChoice`,
`Reveal`, `None`); `base/c.O(LessonContent$Interactive, LessonBundle)` maps ALWAYS-visible
modules to render items `jm/j` (Paragraph), `jm/i` (Image), `jm/k` (Webview) and posts them
to LiveData `m`; CORRECT/WRONG modules are revealed by `c0()`/`d0()` after a run [E09].
`RunButton$State` (`RUN_ENABLED, RUN_DISABLED, SUBMIT_ENABLED, SUBMIT_DISABLED, PROCESSING,
CONTINUE_BIG, CONTINUE_DISABLED, NOT_SHOWN`) and `InteractionKeyboardButtonState`
(`ENABLED/DISABLED/HIDDEN`) gate input [E05, E10]. Observed `androidx.lifecycle.m0.k`
LiveData posts in M08 phase 2 (fragment instance -> ViewModelStore keys):
- `NavHostFragment{253de5a} (c89705ce-3c7f-4373-9eca-462d439fa614 id=0x7f0a01cf)` -> `k1@4f86d68(keys=[androidx.lifecycle.internal.SavedStateHandlesVM, androidx.navigation.NavControllerViewModel])`
- `IntroductionFragment{a10920a} (90166d43-7fd2-430e-a440-bdd758bcf0d8 id=0x7f0a01cf tag=f1e0b8c5-5746-48df-b34a-` -> `k1@3496a7b(keys=[androidx.lifecycle.ViewModelProvider.DefaultKey:m7.f.a, androidx.lifecycle.internal.SavedStat`
- `SetMotiveFragment{966822d} (63dfbeb5-e92e-4e76-8d79-082f973f00ae id=0x7f0a01cf tag=09a9453e-eab0-4615-9bad-4c9` -> `k1@599509d(keys=[androidx.lifecycle.ViewModelProvider.DefaultKey:m7.f.a, androidx.lifecycle.internal.SavedStat`
- `null` -> `null`
- `OnboardingMotiveReassuranceFragment{472c97f} (411855ab-10d9-438f-91ce-78c2c3e4d62b id=0x7f0a01cf tag=1159c762-` -> `k1@ede074e(keys=[androidx.lifecycle.ViewModelProvider.DefaultKey:m7.f.a, androidx.lifecycle.internal.SavedStat`
- `SetOccupationFragment{cb6cfe1} (3f6e05f9-e751-4653-8971-0dd49f7c8b5f id=0x7f0a01cf tag=92ee2b75-19fe-4b8e-ae8c` -> `k1@6e70745(keys=[androidx.lifecycle.ViewModelProvider.DefaultKey:m7.f.a, androidx.lifecycle.internal.SavedStat`
- `SetWorkFunctionFragment{39fe7d4} (868a83cd-6231-46a4-8c70-e0ce579320ee id=0x7f0a01cf tag=3b42b52f-a52f-4e1f-87` -> `k1@444f121(keys=[androidx.lifecycle.ViewModelProvider.DefaultKey:m7.f.a, androidx.lifecycle.internal.SavedStat`
- `SetExperienceFragment{fa99db9} (93a4be14-3804-4404-bac5-0942d1472c81 id=0x7f0a01cf tag=6c621e4f-03a3-4795-8168` -> `k1@fcb2836(keys=[androidx.lifecycle.ViewModelProvider.DefaultKey:m7.f.a, androidx.lifecycle.internal.SavedStat`

## 5. Content pipeline and lesson DSL

Shipped English curriculum `publishSetVersion=753`: 19 tracks / 144 sections / 1,029
tutorials / 1,947 chapters / 18,272 lessons, with 2,855 decoded selection answers [E09, E18].
`Lye/b.b(J)` opens `lessons-<lang>/tracks/tutorial-<id>.json` via `AssetManager.open`;
`DefaultTrackLoader.a(J,I,I)` decodes with `kotlinx.serialization`; the lesson `content` is
XML-like text parsed by `XmlPullParserFactory` (`p`, `code`, `selection`, `img`, `webview`,
`database`), with unknown tags dropped and `xml_parse_error_module` analytics [E09]. Runtime
verification: `te.c.b(String)` returned Paragraph/Code/FillTheGap/Option(correct=true)/
Paragraph(WRONG) for a shipped lesson; `gm.h.a(nonEmpty)` = `FillTheGap` [E05, E08].
`LessonContent$Executable` carries `instructions, preselectedFileIndex, files,
getHasBrowserOutput(), getHasInputConsole()`; each `File` has
`name, codeLanguage, content, solvedContent` [E09].

## 6. Lesson engine, execution path and validators

The **central chain** (the mission's priority) is runtime-verified at the answer moment
in M07 stage 6 [E05, E06, E07]:

```
NonInteractiveLessonFragment$goToNextPage$1 / WebView Continue
  -> base/c.U()                       lessonSolvedAndProceed  (N=true)
  -> base/c.H(1, 1)                  createLessonProgress
  -> LessonProgressRepository.createLessonProgress(
       LessonBundle(lessonId=151403, lessonIndex=1, chapterId=17742,
                    tutorialId=904, trackId=219, tutorialVersion=161,
                    tutorialTitle="Discovering HTML and Tags", publishSetVersion=753))
  -> LessonProgress(... tries=1, attempts=1, isPracticeProgress=false, inQueue=true)
  -> base/c.e0(progress)             storeProgressInMemory
  -> LessonProgressQueue.storeLessonProgress(progress, false, true, cont)
  -> LessonProgress.isSolvedCorrectly() = true   (151410, 151403)
  -> base/c.f0(false, true)          trackLessonResult   [FIRST ARG IS FALSE]
  -> base/c.N()                      resetInputState
  -> e = chapterIndex -> next lesson
```

`Y(Z)` sets `f=TRUE` to prevent double submission; `onLessonRun$1.invokeSuspend` dispatches
`V()` (exact), `W()` (normalised partial match), `X()`/`d0()` (wrong), then resets `f`
[E09, E10]. Validators, all local: `qm/i.a` lowercases with `Locale.US` and keeps letters,
digits and `< > ( ) : { } , .`; `setupViews$2` produces CORRECT / PARTIAL / INCORRECT
[E08]; `km/f.b(List)` = all `selected == correct` [E08]; `im/d.E0()` ordered case-sensitive
token equality [E09]; `q.I()` compares user file contents with shipped `solvedContent` via
`ArrayList.equals` [E09]; `isSolvedCorrectly() = tries >= 1` [E08]. The shipped WebView
letter exercise 151403 uses `correctLetter='D'` in `lesson-webview.js`: wrong `Q` →
`Try again` and disables Q, correct `D` → `Correct! / D O G / dog_yawn.png`; **no native
`V()/W()/X()` or WebView JS-interface event fired** — M07's negative result is preserved
[E06, E07, E08].

## 7. Learner state and persistence

`mimo.db` is Room/SQLite in WAL mode (`mimo.db-wal`, `mimo.db-shm`), with three app tables
and identity hashes `08b92644…` / `2b8ab6d3…` [E03, E13]. `lesson_progress` has exactly 11
columns, PK(`lesson_id`,`tutorial_id`); the measured row after lesson 151403 is
`151403 | 1793883744787 | 1793883713744 | 1 | 904 | 161 | 219 | 753 | 1 | 0 | 1`
[E07, E13]. Phase 1 measured the natural transition `lesson_progress 0 → 2` during
onboarding (slide 151410 + WebView 151403) and `2 → 0` after a cold start, with
`tutorial_completions` holding 868 seeded `is_completed=0` rows and
`chapter_completions` 0 rows [E11, E13]. Phase 2 hooked `SQLiteDatabase` and captured the
**actual Room bootstrap SQL executed at runtime** against
`/data/user/0/com.getmimo/databases/mimo.db`: `PRAGMA user_version;`, the three
`CREATE TABLE IF NOT EXISTS` statements, `INSERT OR REPLACE INTO room_master_table
(id,identity_hash) VALUES(42, '2b8ab6d303d9a501bd8c8fb78d8352fc')` and
`PRAGMA user_version = 2`, plus `SELECT identity_hash FROM room_master_table WHERE id = 42`
[E12 `sql`]. This runtime-confirms the M05 static schema and establishes the shipped
Room migration version (`user_version = 2`); the complete migration class list remains
`UNKNOWN`.

**M08 discovery:** the persisted economy is in `mimo_prefs.xml` —
`local_coins = {"coins":200}` (matching the toolbar `200`), `user_settings =
{"hasProgrammingExperience":false}`, `favorite_tracks = {"favoriteTrackIds":[50,219]}`,
`user_profile_created_at`, `favorite_tracks_to_sync/remove` sets [E11, E13].
`sp_lesson_view_properties.xml` holds per-interaction hint booleans and
`code_editor_line_length=-1` [E13]. Jetpack DataStore `user_preferences.preferences_pb`
plus Firebase/RevenueCat/Mixpanel/Facebook stores were present; protobuf contents were **not**
decoded (`UNKNOWN`) [E13, E10]. Full schema in `MIMO_LEARNER_STATE_SCHEMA.json`.

## 8. Progression and unlock

`GetPathMapState$invoke$3` (659 instructions) builds
`Completed / Locked / Unlocked / UnlockedButNoKeys` states from `Tutorial.isCompleted()`,
`TutorialType.isRequired()`, subscription tier, `CanOpenChapterWithKeys`, keys count and dev
overrides; a reverse `listIterator` enforces the **sequential required-tutorial prerequisite**;
`Challenge` tutorials are excluded; `cc/b.y` classifies sections by completion floats
against `1.0f` [E10]. The unlock key is `ds/w.c(Set<String>,J,J,J)`: join the three longs
with `":"` and test `Set.contains("<trackId>:<tutorialId>:<chapterId>")`, consumed by
`CanOpenChapterWithKeys$invoke$1`; the key set comes from the remote
`DefaultKeysRepository.fetchKeys/consumeUserKey` (`/v1/user/keys`,
`/v1/user/keys/consume`) [E04, E20]. Section/classification state was observed as `0/20`,
`0/11`, `0/9`, `0/15` [E14]. **The exact live boolean combining tier / keys / progress is
`UNKNOWN`** — 659 decoded instructions with suspension labels; no runtime unlock decision
was forced with a seeded key [E10, E20].

## 9. Scoring, XP, coins, streak, goals and rewards

What is **verified**: `lesson_progress` has no XP/score/streak/key column [E03, E20];
`d0()` and `f0()` contain no XP arithmetic [E07]. Local answer counting is an exact
algorithm: `AnswersInChapter(correct = queued.count{isSolvedCorrectly()}, total =
queued.size)`, `getCorrectLessonProgressCount` = same count, and
`getCorrectLessonsFirstTryCount = queued.count{isSolvedCorrectly() && attempts == 1}`;
`updateCorrectAnswersCount` publishes the StateFlow and `updateLessonStreakDetector` runs
when `attempts == 1` [E10]. Phase 2 captured two real learner-state writes during onboarding:
`SharedPreferencesImpl$EditorImpl.putString("onboarding_goal", "build_something_useful")`
and `putString("user_settings", "{\"hasProgrammingExperience\":false}")`, and a real
`com.getmimo.data.settings.a.l(Settings)` call with
`Settings(dailySparksGoal=null, hasProgrammingExperience=false, dailyReminderTime=null,
notificationSettings=null, name=null, biography=null, userId=null, hadFreeProTrial=null,
hadFreeMaxTrial=null)`; `a()` returned `null` before that write [E12 `prefs_write`,
`entry settings_write`, `entry settings_get`]. This is a measured **onboarding decision →
repository → SharedPreferences** path; note the goal field is `dailySparksGoal`, not a
minute count. Phase 2 hooks the coin layer
(`com.getmimo.core.model.coins.Coins.getCoins()I`,
`com.getmimo.data.source.remote.coins.a.a()/b()`,
`LessonProgressQueue.getCorrectLessonProgressCount/getCorrectLessonsFirstTryCount/
updateCorrectAnswersCount/updateLessonStreakDetector`, `MainViewModel E/F/G/H/I`,
`data.settings.a` daily-goal, reward/keys repositories) so a scoring claim would need
input → calculation → output → storage [E12].

What is **not** verified: absolute XP per lesson, streak length, leaderboard rank, key
balance, coin award formula or daily-goal award thresholds. These live in remote DTOs
(`Reward/Rewards`, `UserActivityResponse`, `Leaderboard*`, `PostProgressResponse`,
`TrackEtaResponse`) and caches (`RevenueCat remote_config.json`) [E20]. The measured guest
`local_coins` stayed `200` across 14 natural snapshots, so **no per-lesson coin
increment was demonstrated** [E11, E13]. `SERVER CONFIRMED = 0`.

## 10. Learning and review

`CompletionRepository.b(Track, cont)` attaches `TutorialCompletion.isCompleted` and
`completedChapters` from Room; `ChapterFinishedViewModel.R` is the offline fallback
`handleChapterAlreadyCompletedState`; `ChapterFinishedSuccessType` distinguishes
`DAILY_GOAL_NOT_REACHED / REACHED / ALREADY_REACHED_EARLIER_TODAY` [E10]. Practice/review
content exists as `PRACTICE_LEVEL_1..3`, `PracticeRequired`, `PracticeOptional` chapter
types, but for a guest the Practice tab is gated behind profile creation [E10, E11].
No chapter-end screen, no `is_completed=1` row and no review session was reached — those
transitions are `UNKNOWN` [E11, E20].

## 11. Media / WebView / Rive / code editor / native

`assets/lesson-webview.js` relays gesture/activity/focus/height/ready and
`mimo.activity.correct|wrong|completed`; shipped `solvedContent` makes executable lessons
decidable offline [E09]. The code editor is `CodeEditViewModel` + `CodeDiffViewModel` +
syntax highlighter + input console + `CodePlaygroundActivity`; a shipped HTML template uses
`style.css` / `script.js` [E09]. Phase 1 reached the fill-the-gap code-editor lesson
("Click on `<button>Like</button>`") and measured its clickable snippet and
`tv_ftg_hint` [E14 `S151_onboard_23_after.xml`]. Twelve arm64 `.so` libraries ship,
including `librive-android.so` (Rive), `libsqlcipher.so`, `libdatastore_shared_counter.so`,
`libsigner.so` and ML Kit/CameraX/Bugsnag libraries [E10]. `System.loadLibrary` is hooked
(deduplicated), but JNI method tables, request signing and the native↔Kotlin surface
remain `UNKNOWN` [E12, E10]. `WebView.addJavascriptInterface` was hooked in M07 stage 6 and
produced **no** event for lesson 151403 [E06].

## 12. API, network, sync and offline boundary

53 Retrofit-annotated endpoints were decoded; the relevant ones are listed in
`MIMO_SYSTEM_MAP.json -> modules[network_sync].endpoints` [E04]:
`POST /v1/tutorials/{tutorialId}/progress`, `GET /v1/tracks/{trackId}/completion`,
`GET /v1/user/coins`, `GET /v1/user/keys`, `POST /v1/user/keys/consume`,
`GET /v1/user/rewards/next`, `POST /v1/user/rewards/{rewardId}/confirm`,
`GET /v1/leaderboards/latest`, `GET|PUT /v1/user/settings`,
`POST /v1/code/runfiles`, `POST /v1/user/visits`, `GET /v1/user/activity`.

`java.net.URL.openConnection` was hooked and produced the only observed outbound
connections: `https://graph.facebook.com/v16.0/app/model_asset?...`,
`https://api.mixpanel.com/track/?ip=1`, `https://api.mixpanel.com/engage/?ip=1`,
`https://app.adjust.com/event`, `https://api.revenuecat.com/v1/subscribers/<id>` and
`https://firebaselogging-pa.googleapis.com/v1/firelog/legacy/batchlog` — i.e. third-party
analytics, subscription and model-asset endpoints [E12, E22 `net`]. The subscriber ID is
redacted; no credentials are reproduced. `okhttp3.OkHttpClient.newCall` could not be
hooked (`net_probe okhttp_missing`: R8 removed that symbol), and **no Mimo backend
`/v1/...` request was observed in the window**, so the decoded endpoints below remain
`VERIFIED_STATIC` only. `SERVER CONFIRMED = 0`.

`com.getmimo.network.a.a()` is the exact connectivity gate:
`ConnectivityManager.getActiveNetwork()` + `hasTransport(WIFI) || hasTransport(CELLULAR)`;
`b() = !a()` [E10]. Offline, `postUnsyncedLessonProgress()` logs
"No internet connection, not posting unsynced lesson progress" and throws
`NoConnectionException`; this was runtime-verified [E08]. M07 stage 6 and M08 phase 1 both
measured `in_queue=1` rows being deleted at a cold start (2 → 0), including once while
`Active default network: 102` was online [E07, E11]. Whether deletion followed a successful
POST or a local `DELETE FROM lesson_progress WHERE in_queue = 1` was **not isolated**;
no server response was observed. The final M08 run is a counter-observation: the restored
natural state kept `lesson_progress=2` across a force-stop and cold start with all
`db_diff` deltas empty, so the deletion is **not universal** [E22]. `SERVER CONFIRMED = 0`.

## 13. Background jobs

`PostVisitWorker`, `StreakWidgetRefreshWorker`, `AccountDeleteWork`,
`AsyncRequestWorker`, `MimoFirebaseMessagingService`, `AutoSaveCodeService` and
`NotPremiumNotificationService` are decoded WorkManager `CoroutineWorker` / service classes
[E02, E10]. Phase 2 hooks `PostVisitWorker.a` and `StreakWidgetRefreshWorker.a`; their
**triggers and periodicity remain `UNKNOWN`** because no worker fired in the observed window
[E12].

## 14. The central decision graph (data flow, not class names)

1. **Navigation** chooses a route (bottom-nav tab / path-map icon / ChapterActivity page).
2. The **ViewModel** (`MainViewModel`, `PathMapViewModel`, `ChapterViewModel`,
   `InteractiveLessonBaseViewModel`) loads a `LessonBundle` from **shipped** content.
3. The **DSL + interaction selector** determine the renderer and validator.
4. User input → **validator** → `Y(boolean)` → `V/W/X/U` (`U()`/`H()` runtime-verified
   in M07 stage 6; `V/W/X` and `onLessonRun$1` are `VERIFIED_STATIC` only).
5. `H(tries,attempts)` → **Repository** `createLessonProgress` → 11-field
   `LessonProgress`.
6. `e0()` → **Queue** → Room `lesson_progress(in_queue=1)` + `AnswersInChapter`
   counters + streak detector.
7. `f0(false, isSolvedCorrectly())` analytics; `N()` resets input; `e = chapterIndex`
   posts the **next page**; `GetPathMapState` recomputes **unlock state** for the next
   Activity.
8. On reconnect/startup, `postUnsyncedLessonProgress` applies the **network gate** and
   either POSTs or throws `NoConnectionException`.
9. Remote **reward/streak/leaderboard/goal** objects are consumed by `MainViewModel`
   (static call graph); their award formulas are server-owned (`UNKNOWN`).

`MIMO_CORE_FLOW.mmd` draws exactly this graph; decisions D1–D7 with inputs, logic and
outputs are in `MIMO_SYSTEM_MAP.json -> decision_logic`.

## 15. Dependencies and client/server responsibilities

Kotlin + coroutines + kotlinx.serialization; AndroidX ViewModel/LiveData; Jetpack Compose +
Orbit MVI; Room/SQLite WAL; Jetpack DataStore; SharedPreferences; Retrofit-style APIs over
OkHttp; WorkManager; Firebase (Remote Config, Crashlytics, Analytics, Messaging); RevenueCat
IAP; Mixpanel; Adjust; Customer.io; WebView; Rive; ML Kit/CameraX [E01, E02, E04, E13].
**Client-owned:** curriculum, DSL, validation, progress rows, counters, guest coins,
offline correctness, unlock *state shape*, connectivity gate. **Server-owned / UNKNOWN:**
absolute XP, streak length, daily-goal awards, keys/rewards balances, leaderboard ranks,
`PostProgressResponse`, remote code-runner results, subscription tier, completion
acknowledgement [E07, E10, E20]. No server was reconstructed or contacted by design.

## 16. Honest verdict

M08 establishes the connected architecture, the real navigation state machine, the
answer → ViewModel → Repository → Room → queue → next-lesson execution path, the exact
learner-state stores (including the previously unknown `local_coins`), the unlock *shape*,
local answer counters, the network gate and the client/server boundary. 578 Frida
events (408 hook installs, 2 method entries, 28 SQL,
12 LiveData, 0 lifecycle, 30 DI, 2 preference writes,
12 network) were correlated into the one timeline [E12]. All 63 curated hooks
installed successfully in each attached process (the only `hook_error` was the API-36
lifecycle interface), so the absence of `V()/W()/X()` or `LessonProgressApi.postProgress`
events is a **negative runtime result**, not a hook failure. Phases 3 and 4 switched
technique — restoring the naturally generated post-onboarding snapshot instead of replaying
the Compose onboarding that stalled phase 2 — to put hooks on the main screens. The restore
was verified (`restored_files=82`, `lesson_progress=2`, `tutorial_completions=868`,
`local_coins={"coins":200}`, `favorite_tracks={"favoriteTrackIds":[50,219]}`), but the app
**still opened `IntroSlidesActivity`** on every cold start; a bounded, state-aware attempt to
tap the measured "Get started" node never reached `MainActivity`
(`main_activity_reached=false`, `route_tour_skipped`). Consequently
`MainViewModel`, `PathMapViewModel` and `LessonProgressQueue` had **0 live instances** at
every attach and no main-screen method entry was observed. This is reported as a measured
negative result, not silently filled in: the higher-level chain from a bottom-nav tap through
ViewModel → Repository → Room remains `VERIFIED_STATIC`/`UNKNOWN`, and no coordinates were
guessed [E21, E22]. It does **not** establish
absolute XP/streak/reward formulas, native validator dispatch for a submitted native answer,
chapter-completion transitions, JNI internals, or any server response. No complete
reconstruction is claimed. `SERVER CONFIRMED = 0`.
