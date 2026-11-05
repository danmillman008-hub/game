# LOCAL_STORAGE_MODEL — Mimo 9.35 client persistence

`VERIFIED_STATIC` = DEX literal / JADX class / APK asset byte ·
`VERIFIED_RUNTIME` = emulator observation · `VERIFIED_BOTH` ·
`INFERRED` · `UNKNOWN`.
APK `48ce1740…7c7a` · `com.getmimo` 9.35 / 1792759685 ·
branch `arena/aebb90b7-game`.

> **Design principle honoured:** this document describes the **original** storage
> implementation. No new database architecture is proposed; the client already
> contains a suitable one.

## 1. Storage stack — `VERIFIED_STATIC`

| Layer | Implementation | Evidence |
|---|---|---|
| Structured progress DB | **AndroidX Room / SQLite**, database name literal `mimo.db` (`classes.dex @3,432,719`) | `EVIDENCE/ROOM_SQL.txt`, `EVIDENCE/DEX_STRING_OFFSETS.txt` |
| Key/value prefs | **androidx DataStore Preferences**, file `user_preferences` (`@3,550,076`), `.preferences_pb` (`@1,994,520`), `preferences_pb` suffix | DEX strings, `EVIDENCE/STORAGE_AND_ONBOARDING_STRINGS.txt` |
| Legacy prefs | `SharedPreferencesMigration` + `SharedPrefsBackedUserProperties`, `registerOnSharedPreferenceChangeListener` | JADX `data/settings/*`, DEX strings |
| Shipped content | read-only JSON **APK assets**, never written to DB | `CONTENT_MODEL.md`, `EVIDENCE/ASSET_MANIFEST.txt` |
| Work scheduling | WorkManager (`androidx.work.workdb`, `WorkSpec`, `Preference`) | DEX strings |
| Native counter | `libdatastore_shared_counter.so` (JNI `NativeSharedCounter`) | `NATIVE_LIBRARIES.md` |
| Network cache | Room tables + `LessonProgress.in_queue` queue | SQL below |

Room identity hashes present in DEX (`VERIFIED_STATIC`):
`08b926448d86528e697981ddd30459f7` and `2b8ab6d303d9a501bd8c8fb78d8352fc`
(two schema versions / migrations).

## 2. Exact Room schema — `VERIFIED_STATIC` (byte-level SQL literals)

All statements extracted verbatim from `classes.dex`; offsets in
`EVIDENCE/ROOM_SQL.txt`.

```sql
CREATE TABLE IF NOT EXISTS `lesson_progress` (
  `lesson_id` INTEGER NOT NULL, `completed_at` INTEGER NOT NULL,
  `started_at` INTEGER NOT NULL, `tries` INTEGER NOT NULL,
  `tutorial_id` INTEGER NOT NULL, `tutorial_version` INTEGER NOT NULL,
  `track_id` INTEGER NOT NULL, `publish_set_version` INTEGER NOT NULL,
  `attempts` INTEGER NOT NULL, `is_practice_progress` INTEGER NOT NULL,
  `in_queue` INTEGER NOT NULL,
  PRIMARY KEY(`lesson_id`, `tutorial_id`))                    -- @2,183,344

CREATE TABLE IF NOT EXISTS `chapter_completions` (
  `chapter_id` INTEGER NOT NULL, `created_at` INTEGER NOT NULL,
  `track_id` INTEGER NOT NULL, `tutorial_id` INTEGER NOT NULL,
  PRIMARY KEY(`chapter_id`, `track_id`))                      -- @2,183,130

CREATE TABLE IF NOT EXISTS `tutorial_completions` (
  `tutorial_id` INTEGER NOT NULL, `is_completed` INTEGER NOT NULL,
  `updated_at` INTEGER NOT NULL, `track_id` INTEGER NOT NULL,
  PRIMARY KEY(`tutorial_id`, `track_id`))                     -- @2,183,790
```

**Entities (JADX field declarations, `SCHEMAS/JADX_MODEL_FIELDS.json`):**

| Entity | Fields (type) |
|---|---|
| `…data/model/room/LessonProgress` | `int attempts`, `Instant completedAt`, `boolean inQueue`, `boolean isPracticeProgress`, `long lessonId`, `long publishSetVersion`, `Instant startedAt`, `long trackId`, `int tries`, `long tutorialId`, `int tutorialVersion`; `isSolvedCorrectly()` |
| `ChapterCompletion` | `long chapterId`, `Instant createdAt`, `long trackId`, `long tutorialId` |
| `TutorialCompletion` | `boolean isCompleted`, `long trackId`, `long tutorialId`, `Instant updatedAt` |
| `Converters` | `Long fromInstant(Instant)`, `Instant toInstant(Long)` ⇒ timestamps stored as INTEGER epoch millis |

**DAO operations (`VERIFIED_STATIC`, SQL literals):**

| Operation | SQL |
|---|---|
| insert | `INSERT INTO lesson_progress (…11 cols…) VALUES (?,?,?,?,?,?,?,?,?,?,?)` |
| update | `UPDATE lesson_progress SET … WHERE lesson_id = ? AND tutorial_id = ?` |
| read all | `SELECT * FROM lesson_progress` |
| read unsynced | `SELECT * FROM lesson_progress WHERE in_queue = 1` |
| mark synced | `UPDATE lesson_progress SET in_queue = 0 WHERE in_queue = 1` |
| delete synced | `DELETE FROM lesson_progress WHERE in_queue = 1` |
| delete subset | `DELETE FROM lesson_progress WHERE lesson_id IN (…)` |
| chapter query | `SELECT * FROM chapter_completions WHERE track_id = ?` / `… AND tutorial_id in (…)` |
| tutorial query | `SELECT * FROM tutorial_completions WHERE track_id = ?` / `… AND tutorial_id in (…)` |
| aggregate | `SELECT COUNT(DISTINCT chapter_id) FROM chapter_completions` |
| migration | `DROP TABLE IF EXISTS lesson_progress` / `chapter_completions` / `tutorial_completions` |

`chapter_completions` and `tutorial_completions` have full INSERT/UPDATE
statements with their primary keys. `in_queue` on `lesson_progress` is the
**offline outbox**: progress is written locally first, then posted.

## 3. Offline outbox / sync — `VERIFIED_STATIC` (symbols) + `INFERRED` (order)

Classes/methods found in DEX/JADX:
`LessonProgressQueue` (`storeLessonProgress`, `addOrUpdateLessonProgressInQueue`,
`getCorrectLessonProgressCount`, `getCorrectLessonsFirstTryCount`,
`getRewardMultiplier`, `updateCorrectAnswersCount`,
`clearLessonProgressQueue`, `storeAndPostAllLessonProgress`),
`LessonProgressRepository` (`postUnsyncedLessonProgress`,
`moveLessonProgressFromQueue`, `fetchTrackCompletionForFavoriteTracks`),
`LessonProgressApi` (`POST /v1/tutorials/{tutorialId}/progress`),
`MainViewModel$fetchLessonProgressAndPostUnsyncedToBackend`,
`GetChapterEndSuccessState$storeAndPostAllLessonProgress`,
`ChapterFinishedViewModel$storeAndPostAllLessonProgress`,
`toLessonProgressSyncResult`, `LessonProgressSyncResult(reachedDailyGoal=…`.

`ChapterFinishedViewModel` has explicit `handleOfflineState$1`,
`handleOnlineState$1`, `getChapterEndSuccessStateWithRetry$1` and
`ChapterFinishedSynchronizationException` ⇒ **offline is an anticipated state
of the chapter-end flow**, not an afterthought. `VERIFIED_STATIC` (class names).

`INFERRED` flow (never observed end-to-end): answer → `storeLessonProgress`
(Room, `in_queue=1`) → `storeAndPostAllLessonProgress` at chapter end →
`POST /v1/tutorials/{id}/progress` → `in_queue=0`. Exact retry/backoff policy
`UNKNOWN`.

## 4. DataStore / preferences — `VERIFIED_STATIC`

`DataStoreUserPreferences` is a large class (18 `b`-typed `Preferences.Key`
fields in `com.getmimo.data.local.a`). Named accessors recovered from JADX
inner-class names (`VERIFIED_STATIC` for names; exact key strings `UNKNOWN`
unless listed):

| Area | Accessors |
|---|---|
| User id | `getCurrentUserId`, `setCurrentUserId`, `clear` |
| Hard mode | `observeHardModeEnabled`, `setHardModeEnabled`, `setHardModeEnabledFromChapterDialog`, `hasSeenHardModeIntro`, `hasSeenHardModeTutorIntro`, `consumeHardModeIntro`, `hasPendingHardModeIntro`, `setHardModeIntroPending`, `observeCompletedHardModeChapters`, `markChapterCompletedInHardMode`, `resetUserMessagesSent` |
| First-run / feature intros | `hasSeenPracticeOptionalFeatureIntro`, `hasSeenMaxUpsellFlow`, `hasSeenGuidedProjectProUpsellFlow`, `hasSeenResubscribeMascotOverlay`, `shouldSeeFirstChapterIntro`, `getHasSeenQuizIntroductionToolTip`, `getHasSeenPythonInputIntroduction`, `getHasSeenSmartPracticeIntroduction`, `getHasSeenLeaderboardFeatureIntroduction`, `getHasSeenPublishPlaygroundsIntro`, `getHasSeenRemixPlaygroundIntro`, `hasSeenLocalDiscountAfterSecondChapter` |
| Path overview | `hasSeenPathOverviewEta`, `shouldShowPathOverviewIntro`, `setShowPathOverviewIntro`, `setShowPathOverviewEta`, `shouldQueuePathOverviewEta`, `shouldShowPathOverviewEta` |

DEX literals (`VERIFIED_STATIC`, examples): `user_preferences`, `.preferences_pb`,
`selected_appearance`, `onboarding_daily_notifications_enabled`,
`onboarding_daily_notifications_reminder_time`,
`onboarding_skill_preference_picked`, `resume_onboarding_from_select_path`,
`show_learning_preference_reassurance`, `user_messages_sent`,
`experiment_daily_goal_companions_android`,
`experiment_adapted_onboarding_android_local`,
`trigger_paywall_onboarding_exit_offer`.

`SharedPrefsBackedUserProperties` + `SharedPreferencesMigration` prove a
**migration from legacy SharedPreferences into DataStore** (`VERIFIED_STATIC`).
`ripgrep`-able list: `EVIDENCE/STORAGE_AND_ONBOARDING_STRINGS.txt`.

## 5. Serialization — `VERIFIED_STATIC`

- Curriculum: **kotlinx.serialization JSON** (`@Serializable`,
  `*$$serializer.java` classes for `TracksJson`, `TrackJson`, `SectionJson`,
  `TutorialJson`, `Tutorial`, `Chapter`, `Lesson`, `LessonContent$Executable`,
  `LessonImage`). `JsonNames(names = …)` present for alias handling.
- Lesson body: **HTML-like XML/DSL string** parsed by
  `data/content/lessonparser/interactive/ParserModule` into `LessonModule`s
  (`Content → LessonModule`, `Interaction`, `Option`, `SelectionItem`,
  `Output`, `Table`, `WebviewType`, `ModuleVisibility`).
- Runtime models are `Parcelable` (`LessonContent`, `LessonModule`,
  `Interaction`, `Option`, `SelectionItem`, `Lesson`, `LessonIdentifier`,
  `ChapterIdentifier`, `TrackIdentifier`) ⇒ screen state is passed as Parcelable,
  not re-fetched.
- Timestamps: `org.joda.time.Instant`, converted to epoch `Long` by `Converters`.
- WebView bridge: JSON string via `MimoLesson.postMessage(JSON.stringify(...))`.

## 6. Resume behaviour after restart — `VERIFIED_STATIC` + `INFERRED` + `UNKNOWN`

- `VERIFIED_STATIC`: `MainViewModel$fetchLessonProgressAndPostUnsyncedToBackend`,
  `resume_onboarding_from_select_path`, `GET /v1/tracks/completion/lastInteracted`,
  `GET /v1/tracks/{trackId}/completion`, `GET /v1/tutorials/{id}/progress`-like
  endpoints, `LessonProgress` local rows.
- `INFERRED`: on cold start the client reads `user_preferences` for onboarding
  stage, reads the three Room tables for progress, and optionally refreshes
  completion state from the server for a signed-in user.
- `UNKNOWN` (`VERIFIED_RUNTIME` not yet obtained): exact screen shown on restart
  without an account, whether progress written while offline survives a
  force-stop, and whether the intro slides reappear. M05 runtime run 2 probes a
  **cold start with network disabled**; see `../RUNTIME/MISSION_05/`.

## 7. What is NOT stored locally — `VERIFIED_STATIC` (endpoint evidence)

| State | Owner |
|---|---|
| XP total, sparks/coins/keys balances, streak, daily goal result | server (`/v1/user/*`, `/v2/client-config`) |
| Leaderboard rank / league | server (`/v1/leaderboards/*`) |
| Track ETA / estimated completion | server (`/v1/tracks/{id}/eta`) |
| Favourite tracks (remote copy) | server (`/v1/user/favorites/tracks`) |
| Saved code / executable lesson files | server (`/v1/code`, `…/savefiles`, `…/savedFiles`) |
| Code execution result & test pass/fail | server (`…/runFiles`) |
| Account / auth token / profile / social | server + secure storage (`UNKNOWN` exact location) |

Local `user_preferences` holds **flags and UI state**, not the authoritative
economy. This is the core offline boundary — see `OFFLINE_DEPENDENCY_MATRIX.md`.

## 8. Integrity note

`allowBackup=false` in the manifest (M02) and a non-debuggable release build mean
the actual `mimo.db` and `user_preferences` files of the running app were **not
extracted** in M05. Everything here comes from the APK's own SQL/schema strings
and decompiled classes. Direct file contents = `UNKNOWN`; no values were invented.
No root, no `run-as`, no private DB extraction was used.

**Evidence:** `EVIDENCE/ROOM_SQL.txt`, `EVIDENCE/DEX_STRING_OFFSETS.txt`,
`EVIDENCE/STORAGE_AND_ONBOARDING_STRINGS.txt`, `SCHEMAS/JADX_MODEL_FIELDS.json`,
`ANALYSIS/MIMO_COMPLETION_ENGINE.json`, `ANALYSIS/DATA_AND_API_MAP.fa.md`,
`ANALYSIS/MIMO_RETROFIT_ENDPOINTS.json`.
