# MISSION 07 — 09 OFFLINE EXECUTION RESULTS

**Isolation proof (`VERIFIED_RUNTIME`)**: `ANALYSIS/RUNTIME/MISSION_07/EXPERIMENTS/G_OFFLINE_ISOLATION.txt` (run `42019353340`) and `EXPERIMENTS/S4_OFFLINE_ISOLATION.txt` (stage 4). Before: `Active default network: 101` with connected `MOBILE[LTE]` and `WIFI` NetworkAgentInfo. After `svc wifi disable` + `svc data disable` + `cmd connectivity airplane-mode enable`:
```
Active default network: none
connect: Network is unreachable
settings get global airplane_mode_on -> 1
```
`am force-stop com.getmimo` then `am start -n com.getmimo/.ui.SplashActivity_default` succeeded with no default network. No reconnect was claimed (M05 showed `svc wifi enable` did not restore connectivity).

## Operations classified (M07 classes A–E)

| # | Operation | Class | Evidence / status |
|---|---|---|---|
| 1 | Cold start / splash / onboarding skip / path-map render | **A locally implemented** | `VERIFED_RUNTIME`: offline cold start produced UI hierarchies (`UI/H_OFFLINE_COLD_START.xml`, `UI/S4_H_*`) and shipped curriculum; `mimo.db` present with 672 `tutorial_completions` rows, `lesson_progress` 0 |
| 2 | Browse learning path, chapters, lesson text | **A locally implemented** | `VERIFIED_RUNTIME`: M05 runs `42002808217`/`42003884423` offline XMLs byte-identical for first 3 states; shipped `assets/lessons-en/tracks/` (M05: 10,298 curriculum files, v753) |
| 3 | Read/write `mimo.db` (`lesson_progress`, `chapter_completions`, `tutorial_completions`) | **A locally implemented** | `VERIFIED_RUNTIME`: root `.backup`, WAL/SHM captured, `PRAGMA journal_mode=wal`, exact CREATE TABLE SQL matches M05 `ROOM_SQL.txt` |
| 4 | Read SharedPreferences / DataStore / `no_backup` / analytics queues | **A locally implemented** | `VERIFIED_RUNTIME`: 47–95 private files per snapshot, `experiments.xml`, `mimo_prefs.xml`, `sp_lesson_view_properties.xml`, `user_preferences.preferences_pb`, Firebase/RevenueCat/Mixpanel files |
| 5 | Local answer normalisation, selection validation, `isSolvedCorrectly()` | **A locally implemented** | `VERIFIED_RUNTIME`: E1/E3 direct Frida invocations (`04_ANSWER_VALIDATION_RUNTIME.md`) require no network |
| 6 | `NetworkUtils` connectivity detection | **A locally implemented** | `VERIFIED_RUNTIME`: E4 `a()=true`, `b()=false` online; M06 `getActiveNetwork`/`hasTransport` |
| 7 | `postUnsyncedLessonProgress` | **B local + queued** | `VERIFIED_STATIC`: M06 showed an `in_queue=1` Room row plus `NoConnectionException` when offline; SQL `UPDATE lesson_progress SET in_queue = 0 WHERE in_queue = 1` (M05 `ROOM_SQL.txt`) exists. Live offline post not yet captured → `PARTIALLY VERIFIED` |
| 8 | Analytics / telemetry / crashlytics / RevenueCat / Firebase Remote Config | **B local + queued** | `VERIFIED_RUNTIME`: offline snapshots still show `mixpanel.events`, `people`, `com.google.android.datatransport.events` rows growing (e.g. stage-2 `mixpanel.events` 0→16→26 across G/H/I); 818 SQL events in stage 3 from analytics DBs |
| 9 | Account creation / sign-in / purchase / restore | **D remote required** | `VERIFIED_RUNTIME` (boundary only): offline sign-up screen shows `Skip`; no auth attempted by M07, no credentials, no server reconstruction. `SERVER CONFIRMED=0` |
| 10 | Keys / `CanOpenChapterWithKeys`, subscription tier, leaderboard, streak, XP | **D remote required / E unknown** | `VERIFIED_STATIC`: `keys/a` is a remote repository (`DefaultKeysRepository.fetchKeys/consumeUserKey`) and `GetPathMapState` consumes `SubscriptionTier`; RevenueCat `no_backup/remote_config/remote_config.json` present offline. Exact offline unlock rule not measured → `UNKNOWN` |
| 11 | Code exercise execution (WebView JS → native) | **C blocked by condition / E unknown** | M05 shipped `lesson-webview.js` only relays gesture/focus/height/ready; no scoring in JS. Stage-3 UI reached a JavaScript snippet lesson (`let`/`const`) with a WebView. Whether execution is local or remote was not measured → `UNKNOWN` |
| 12 | Absolute XP / streak / score formulas | **E unknown / externally sourced** | No XP column in `mimo.db`; no local arithmetic found in `LessonProgress`/`d0()`/`V()`/`W()`; `core/model/streak/*`, `data/model/reward/*`, `leaderboard/*` are remote DTOs. `UNKNOWN` |
| 13 | Force-stop state restoration | **A locally implemented** | `VERIFIED_RUNTIME`: after offline force-stop + cold start, `mimo.db` still had the same 672 `tutorial_completions` rows and `lesson_progress` 0 (`SNAPSHOT_G/H/I`); UI returned to path map. Row-level restoration after an *answered* lesson is still targeted by stage 4 |

## Important negative result
Across all stage-2/3 snapshots `lesson_progress` had **0 rows** and
`chapter_completions` **0 rows**, while `tutorial_completions` had 672 rows all
with `is_completed=0`, `updated_at=1793878535878`, `track_id∈{50 (492), 226
(180)}`. These are **seeded content rows**, not user progress. Therefore no
claim is made that an answer was persisted until a measured before/after diff
shows one. `room_master_table` identity hash measured =
`2b8ab6d303d9a501bd8c8fb78d8352fc` (matches M05 `ROOM_SQL.txt` literal
`INSERT OR REPLACE INTO room_master_table (id,identity_hash) VALUES(42, …)`).

## Instrumentation note
Offline Frida sessions re-attached to the new PID after force-stop
(`FRIDA/STAGE2_OFFLINE_DRIVER.log`, `FRIDA/STAGE4_OFFLINE_DRIVER.log`); the
Java bridge is loaded in both. SQL hooks recorded 818 events in stage 3, all
from `mixpanel`, `com.google.android.datatransport.events` and
`google_app_measurement_local.db` — i.e. **no `lesson_progress` write occurred
during that run**, consistent with 0 rows.
