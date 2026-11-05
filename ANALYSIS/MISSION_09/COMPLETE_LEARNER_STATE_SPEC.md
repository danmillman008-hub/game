# MIMO 9.35 — COMPLETE LEARNER STATE SPECIFICATION

**Document:** `COMPLETE_LEARNER_STATE_SPEC.md` · **Mission:** MISSION 09 (final reconstruction) · **Branch:** `arena/aebb90b7-game`
**Target APK:** `com.getmimo` 9.35, `versionCode=1792759685`, 142,353,499 B, SHA-256 `48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a` — unchanged.
**SERVER CONFIRMED = 0.** Classification vocabulary: `VERIFIED_STATIC`, `VERIFIED_RUNTIME`, `VERIFIED_ASSET`, `VERIFIED_DATABASE`, `VERIFIED_NETWORK_OBSERVATION`, `INFERRED`, `UNKNOWN`, `SERVER_DEPENDENT`.
Evidence codes resolve in `COMPLETE_EVIDENCE_DATABASE.json` / `COMPLETE_SYSTEM_MAP.json -> evidence_index`.

---


## 1. Room database (VERIFIED_DATABASE + VERIFIED_RUNTIME)

Path `/data/data/com.getmimo/databases/mimo.db`; WAL mode (`mimo.db-wal`, `mimo.db-shm`);
`PRAGMA user_version = 2`; `room_master_table(42, '2b8ab6d303d9a501bd8c8fb78d8352fc')`.
Exact DDL [E27, E12]:

```sql
CREATE TABLE IF NOT EXISTS `lesson_progress` (
  `lesson_id` INTEGER NOT NULL, `completed_at` INTEGER NOT NULL,
  `started_at` INTEGER NOT NULL, `tries` INTEGER NOT NULL,
  `tutorial_id` INTEGER NOT NULL, `tutorial_version` INTEGER NOT NULL,
  `track_id` INTEGER NOT NULL, `publish_set_version` INTEGER NOT NULL,
  `attempts` INTEGER NOT NULL, `is_practice_progress` INTEGER NOT NULL,
  `in_queue` INTEGER NOT NULL, PRIMARY KEY(`lesson_id`,`tutorial_id`));
CREATE TABLE IF NOT EXISTS `chapter_completions` (
  `chapter_id` INTEGER NOT NULL, `created_at` INTEGER NOT NULL,
  `track_id` INTEGER NOT NULL, `tutorial_id` INTEGER NOT NULL,
  PRIMARY KEY(`chapter_id`,`track_id`));
CREATE TABLE IF NOT EXISTS `tutorial_completions` (
  `tutorial_id` INTEGER NOT NULL, `is_completed` INTEGER NOT NULL,
  `updated_at` INTEGER NOT NULL, `track_id` INTEGER NOT NULL,
  PRIMARY KEY(`tutorial_id`,`track_id`));
CREATE TABLE IF NOT EXISTS room_master_table (id INTEGER PRIMARY KEY, identity_hash TEXT);
```
Three `sqlite_autoindex_*` indexes exist on the composite primary keys. Dead-end note:
`LessonProgressDao` is an **interface**; its SQL is in the DEX string table [E27, E31].

## 2. Field semantics (every field)

| Field | Type | Default | Writer | Reader / trigger | Local authority | Survives process death | Survives restart |
|---|---|---|---|---|---|---|---|
| `lesson_id` | INTEGER PK | from `LessonBundle.a` | `createLessonProgress` | progress queries | YES | YES | YES |
| `tutorial_id` | INTEGER PK | `bundle.e` | same | `SELECT ... WHERE track_id=?` | YES | YES | YES |
| `completed_at` | INTEGER ms | `Instant.now()` | same | none observed | YES | YES | YES |
| `started_at` | INTEGER ms | `bundle` / fragment entry | same | logged if `completedAt<startedAt` | YES | YES | YES |
| `tries` | INTEGER | `1` on correct, `0` on wrong | `base/c.H(tries,attempts)` via `V/X/U` | `isSolvedCorrectly()` = `tries>=1` | YES | YES | YES |
| `attempts` | INTEGER | incremented in `V()/X()` | ViewModel field `d` | `getCorrectLessonsFirstTryCount` | YES | YES | YES |
| `tutorial_version` | INTEGER | `bundle.v` (161 measured) | `createLessonProgress` | version compatibility | YES | YES | YES |
| `track_id` | INTEGER | `bundle.f` (219 measured) | same | `SELECT ... WHERE track_id=?` | YES | YES | YES |
| `publish_set_version` | INTEGER | `tracksRepository.currentPublishSetVersion()` (753) | same | version compatibility | YES | YES | YES |
| `is_practice_progress` | INTEGER bool | `bundle.B` (`false` measured) | same | practice/redo counters | YES | YES | YES |
| `in_queue` | INTEGER bool | `true` | same | `SELECT * FROM lesson_progress WHERE in_queue=1` | YES | YES | **CONDITIONAL** (see §5) |
| `chapter_completions.*` | INTEGER | none (0 rows observed) | `CompletionRepository` (static) | path map | YES | YES | YES |
| `tutorial_completions.is_completed` | INTEGER | seeded `0` (868 rows) | `CompletionRepository.b(Track,cont)` (static) | path map | YES | YES | YES |

No XP / score / streak / keys / coins column exists [E28].

## 3. SharedPreferences (VERIFIED_DATABASE)

`mimo_prefs.xml`: `local_coins={"coins":200}`, `favorite_tracks={"favoriteTrackIds":[50,219]}`,
`user_settings={"hasProgrammingExperience":false}`, `user_profile_created_at` (ISO-8601),
`favorite_tracks_to_sync` / `favorite_tracks_to_remove` (string sets), `marketing_network=Organic`,
`marketing_campaign=""`. Third-party identifiers (`token_adjust`, `token_google_ads`,
`push_notification_registration_id`) are present and **redacted** in all deliverables [E11, E13].
`sp_lesson_view_properties.xml`: per-interaction hint booleans, `code_editor_line_length=-1`.
`experiments.xml`: `experiment_adapted_onboarding_android_local=original` selects the
original onboarding variant (harness-level, NOT learner progress).
`com_revenuecat_purchases_preferences.xml`, Firebase/Mixpanel prefs exist.

**Writes observed at runtime:** `SharedPreferencesImpl$EditorImpl.putString(
"onboarding_goal","build_something_useful")`, `putString("user_settings",
"{\"hasProgrammingExperience\":false}")`, and
`com.getmimo.data.settings.a.l(Settings(dailySparksGoal=null, hasProgrammingExperience=false,
dailyReminderTime=null, notificationSettings=null, name=null, biography=null, userId=null,
hadFreeProTrial=null, hadFreeMaxTrial=null))`; `a()` returned `null` before that write [E12].
Note the daily-goal field is `dailySparksGoal`, not a minute count.

## 4. Jetpack DataStore (VERIFIED_RUNTIME + UNKNOWN)

`files/datastore/user_preferences.preferences_pb` is present byte-for-byte in M07/M08
snapshots. Its protobuf schema was **not decoded**; key names come from M06 static strings
only. `mimo_dev_prefs` (`DISABLE_PREMIUM`, `preload_images`, `USE_TEST_SERVER`,
`CREATE_LESSON_PROGRESS_WHEN_SWIPING`, `USE_UNPUBLISHED_TRACKS_PACKAGE`,
`override_content_experiment`) was **absent** from measured snapshots, so dev switches were
at their defaults [E28, E13]. Closure: `U-STATE-001`.

## 5. Queue lifecycle and the cold-start anomaly (CLOSED to a precise boundary)

**Two competing DAO statements ship in the DEX** [E27]:
* `@2223460  DELETE FROM lesson_progress WHERE in_queue = 1` (destructive)
* `@2984647  UPDATE lesson_progress SET in_queue = 0 WHERE in_queue = 1` (non-destructive)
also `SELECT * FROM lesson_progress WHERE in_queue = 1`,
`DELETE FROM lesson_progress WHERE lesson_id IN (...)`, and
`DROP TABLE IF EXISTS ...` (destructive migration fallback).

**Measured behaviour:**
| Run | Condition | Before | After | SQL observed |
|---|---|---|---|---|
| M07 stage4 offline (`42028049247`) | `Active default network: none`, `Network is unreachable` | 1 queued row | 0 | `NoConnectionException` then 4× `DELETE ... WHERE in_queue=1` |
| M07 stage5 offline (`42030594857`) | same isolation proof | 2 queued rows | 0 | 24 `net_isOnline` calls, 903 SQL events |
| M08 phase1 (`42042312640`) | `Active default network: 102` (online) | 2 | 0 at `S8_AFTER_RESUME` | no SQL hook in that run |
| M08 run4 (`42050715150`) | restored natural state, cold start | 2 | 2 (all `db_diff` deltas empty) | no SQL hook in that run |
| M09 `42077425594` | offline transition + cold restart | see `COMPLETE_RUNTIME_TIMELINE.jsonl` | see timeline | SQL hooks live |

**Resolution:** the disappearance is a **local destructive DELETE**, not a proven server
acknowledgement (`SERVER CONFIRMED = 0`). M08 run4's retention is explained by the fact
that the app never reached the startup path that invokes `postUnsyncedLessonProgress` (it
stayed on `IntroSlidesActivity`), so the cleanup statement did not execute. Which of the two
shipped statements runs for a given startup ordering is **UNKNOWN** without an SQL hook in
that exact run; M09 hooks `SQLiteDatabase` and records the answer in the timeline.
The independent offline client should implement a **durable** queue (independent design
choice), while documenting that Mimo 9.35 is destructive on some cold starts.

## 6. Migrations (VERIFIED_STATIC)

`user_version = 2` with two identity hashes in DEX:
`08b926448d86528e697981ddd30459f7` (older) and `2b8ab6d303d9a501bd8c8fb78d8352fc` (current).
`DROP TABLE IF EXISTS` + `CREATE TABLE IF NOT EXISTS` literals indicate a destructive
fallback migration. Full migration class list / per-version SQL is **UNKNOWN** (M06 found
`androidx.room=11` loaded classes but no migration classes enumerated). Room's
`room_master_table` identity-hash validation is what triggers fallback [E12, E27, E31].

## 7. Snapshot inventory

14 natural (non-synthetic) Room/preferences snapshots in
`ANALYSIS/RUNTIME/MISSION_08/STATE/SNAPSHOT_*.json`, plus M07 `DB/SNAPSHOT_*/private/`
byte-for-byte directories. All are `synthetic=false` for learner rows. `local_coins` stayed
`200` across all 14 snapshots -> **no per-lesson coin increment demonstrated** [E11, E13].

## 8. Independent schema (implementation target)

Implement the three Room tables verbatim, add `settings` / `profile` / `coin_balance` stores
as plain local tables, and replace `in_queue` with a durable `sync_operation` table
(`id, lesson_id, payload_json, state, created_at, retry_count`). That replacement is an
**independent implementation choice**, clearly not original Mimo behaviour.


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

### M09 queue resolution (decisive)

M09 SQL hook captured `DELETE FROM lesson_progress WHERE in_queue = 1` executing at
startup **while online** (event seq 260), preceded by the Room bootstrap and followed by
`SELECT * FROM lesson_progress`, `DELETE FROM lesson_progress WHERE lesson_id IN ()` and
`SELECT COUNT(DISTINCT chapter_id) FROM chapter_completions`.
`LessonProgressRepository.postUnsyncedLessonProgress` also executed (`entry` seq 272,
`ret=COROUTINE_SUSPENDED`) with its 8 live collaborators. Therefore:

* the deletion is a **normal startup statement**, not a server acknowledgement;
* M07 stage4/5 (offline, 1–2 rows -> 0) and M08 phase1 (2 -> 0) are the same path;
* M08 run4 (2 -> 2) retained rows because `main_activity_reached=false` — the app stayed
  on `IntroSlidesActivity` and the cleanup path never ran;
* M09 itself had **0 queued rows** before/after, so no deletion of a row occurred, but the
  statement itself was observed.

`U-QUEUE-001` is closed for behaviour; only the caller ordering between the shipped
`DELETE` and `UPDATE lesson_progress SET in_queue = 0` remains UNKNOWN.
`SERVER CONFIRMED = 0` [E29, E26, E27].

### M09 preferences delta

The M09 fresh-install `mimo_prefs.xml` contained `marketing_campaign`, `marketing_network=Organic`,
`user_settings={"hasProgrammingExperience":false}`, `favorite_tracks_to_sync={50}`,
`favorite_tracks_to_remove={}` and **no `local_coins` key**; `Coins.getCoins()` returned
`0`. M08 snapshots had `local_coins={"coins":200}`. Coin balance is therefore state-dependent
and remote-sourced — not a fixed constant and never a per-lesson award [E29, E13].
