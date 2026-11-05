# MISSION 07 — 06 ROOM / SQLite DATABASE BEFORE–AFTER

**Status:** `VERIFIED_RUNTIME`. All values below are read from consistent on-device
`sqlite3 .backup` copies inside `ANALYSIS/RUNTIME/MISSION_07/DB/SNAPSHOT_*/consistent_mimo.db`
and their JSON descriptors (`SNAPSHOT_*.json`). `SERVER CONFIRMED = 0`.

## Schema (identical to M05 `ANALYSIS/MISSION_05/EVIDENCE/ROOM_SQL.txt`)
```sql
CREATE TABLE `lesson_progress` (
 `lesson_id` INTEGER NOT NULL, `completed_at` INTEGER NOT NULL,
 `started_at` INTEGER NOT NULL, `tries` INTEGER NOT NULL,
 `tutorial_id` INTEGER NOT NULL, `tutorial_version` INTEGER NOT NULL,
 `track_id` INTEGER NOT NULL, `publish_set_version` INTEGER NOT NULL,
 `attempts` INTEGER NOT NULL, `is_practice_progress` INTEGER NOT NULL,
 `in_queue` INTEGER NOT NULL, PRIMARY KEY(`lesson_id`, `tutorial_id`))
CREATE TABLE `chapter_completions` (
 `chapter_id` INTEGER NOT NULL, `created_at` INTEGER NOT NULL,
 `track_id` INTEGER NOT NULL, `tutorial_id` INTEGER NOT NULL,
 PRIMARY KEY(`chapter_id`, `track_id`))
CREATE TABLE `tutorial_completions` (
 `tutorial_id` INTEGER NOT NULL, `is_completed` INTEGER NOT NULL,
 `updated_at` INTEGER NOT NULL, `track_id` INTEGER NOT NULL,
 PRIMARY KEY(`tutorial_id`, `track_id`))
CREATE TABLE android_metadata (locale TEXT)          -- 'en_US'
CREATE TABLE room_master_table (id INTEGER PRIMARY KEY, identity_hash TEXT)
       -- (42, '2b8ab6d303d9a501bd8c8fb78d8352fc')
PRAGMA journal_mode = wal
```
`mimo.db`, `mimo.db-wal`, `mimo.db-shm` are all captured. `consistent_mimo.db`
is a checkpointed WAL backup; `private/databases/mimo.db` is the raw file. Both
were read successfully.

## Stage 2 (run `42019353340`) — no answer reached
| Snapshot | files | `lesson_progress` | `chapter_completions` | `tutorial_completions` |
|---|---|---|---|---|
| `A_BEFORE_ONBOARDING` | 0 | n/a (no `mimo.db` yet) | – | – |
| `C_LESSON_BEFORE_ANSWER` | 91 | 0 | 0 | 672 |
| `D_AFTER_WRONG_ANSWER_SKIPPED` | 91 | 0 | 0 | 672 |
| `E_AFTER_CORRECT_ANSWER_SKIPPED` | 91 | 0 | 0 | 672 |
| `F_AFTER_LESSON_FINISHED_SKIPPED` | 91 | 0 | 0 | 672 |
| `G_BEFORE_FORCESTOP` / `H_OFFLINE_COLD_START` / `I_OFFLINE_RESTORED` | 91 | 0 | 0 | 672 |

The 672 rows are all `is_completed=0`, `updated_at=1793878535878`,
`track_id ∈ {50: 492 rows, 226: 180 rows}` — seeded content rows, not progress.

## Stage 4 (run `42028049247`) — first real `lesson_progress` row
| Snapshot | files | `lesson_progress` | `chapter_completions` | `tutorial_completions` |
|---|---|---|---|---|
| `S4_A_BEFORE_ONBOARDING` | 47 | no `mimo.db` yet | – | – |
| `S4_C_BEFORE_ANSWER` | 88 | **1** | 0 | 868 |
| `S4_D1_AFTER_WRONG_OPTION` | 88 | **1** (unchanged) | 0 | 868 |
| `S4_G_BEFORE_FORCESTOP` | 88 | **1** | 0 | 868 |
| `S4_H_OFFLINE_COLD_START` | 88 | **0** | 0 | 868 |
| `S4_I_OFFLINE_RESTORED` | 88 | **0** | 0 | 868 |

The row, verbatim (column order as in the CREATE TABLE):
```
lesson_id=151410  completed_at=1793882404495  started_at=1793882398890
tries=1           tutorial_id=904            tutorial_version=161
track_id=219      publish_set_version=753    attempts=1
is_practice_progress=0  in_queue=1
```
Group counts: `tries {1:1}`, `attempts {1:1}`, `track_id {219:1}`,
`is_practice_progress {0:1}`, `in_queue {1:1}`.
`tutorial_completions` 868 rows: `is_completed {0:868}`,
`track_id {50:492, 219:376}`, all `updated_at=1793882380548`.

Interpretation: the row is for the **non-interactive slide lesson 151410**,
created when the user continued past it, not for the WebView answer. The wrong
`Q` tap produced no row change. This is the exact before/after diff M07 asked
for; it is reported without over-claiming.

## Observed SQL against `mimo.db` (Frida SQL hooks, stage 4)
1,067 `mimo.db` SQL events online plus `SQLiteStatement` executions. Distinct
statements of interest (verbatim):
```
CREATE TABLE IF NOT EXISTS `lesson_progress` (…)
DELETE FROM `lesson_progress`
DELETE FROM lesson_progress WHERE in_queue = 1
DELETE FROM lesson_progress WHERE lesson_id IN ()
SELECT * FROM lesson_progress
SELECT * FROM lesson_progress WHERE in_queue = 1
```
`DELETE FROM lesson_progress WHERE in_queue = 1` appears repeatedly online and
offline (offline: 12:44:04, 12:44:31, 12:44:38, 12:44:44). M05 `ROOM_SQL.txt`
also lists `UPDATE lesson_progress SET in_queue = 0 WHERE in_queue = 1`.
This explains the row disappearing at cold start.

## Other private databases (measured, unchanged APK)
`com.google.android.datatransport.events`, `google_app_measurement_local.db`,
`mixpanel`, plus `no_backup/` and `files/datastore/user_preferences.preferences_pb`.
Stage-2 offline snapshots: `mixpanel.events` H=16 → I=26, `people` H/I=11,
datatransport `event_metadata` H=90 → I=105, `events` H=6 → I=7. Analytics
rows grow offline (local queue); no server response was observed.

## SharedPreferences / DataStore
`mimo_prefs.xml`, `mimo_prefs_global.xml`, `sp_lesson_view_properties.xml`,
`experiments.xml`, `content_experiment.xml`, Firebase / RevenueCat / Mixpanel
files. `mimo_dev_prefs.xml` was **not** observed in these runs (M07 static decode
shows `sk/a` would create it for developer switches). No `mimo_dev_prefs` value
is therefore claimed.
