# MISSION 07 — 07 OFFLINE PERSISTENCE, RESTORATION AND QUEUE

**Status:** `VERIFIED_RUNTIME`. This is a correction/nuance to M06's static
statement that `postUnsyncedLessonProgress` "throws `NoConnectionException`
offline and leaves Room rows": the throw is real, but the queued rows are also
**deleted** at cold start on this build.

## Measured sequence (run `42028049247`, stage 4)
1. `EXPERIMENTS/S4_OFFLINE_ISOLATION.txt`: `Active default network: none`,
   `connect: Network is unreachable`, `airplane_mode_on=1`.
2. `am force-stop com.getmimo` → `am start -n com.getmimo/.ui.SplashActivity_default`.
3. Offline Frida trace `TRACES/STAGE4_OFFLINE.jsonl`:
```
12:44:04  entry  LessonProgressRepository.postUnsyncedLessonProgress
12:44:04  throw  com.getmimo.network.NoConnectionException
12:44:04  sql    DELETE FROM lesson_progress WHERE in_queue = 1   (mimo.db)
12:44:31  sql    DELETE FROM lesson_progress WHERE in_queue = 1
12:44:37  sql    SELECT * FROM lesson_progress WHERE in_queue = 1
12:44:38  sql    DELETE FROM lesson_progress WHERE in_queue = 1
12:44:44  sql    DELETE FROM lesson_progress WHERE in_queue = 1
```
   `this_fields` of `LessonProgressRepository` at throw:
   `completionRepository=com.getmimo.data.source.local.completion.a`,
   `lessonProgressDao=cg.d`, `lessonProgressApi=fd.l`,
   `networkUtils=com.getmimo.network.a`, `tracksRepository=…`,
   `dispatcherProvider=np.b`, `favoriteTracksRepository=…`.
4. `E4_network_gate` offline: `a() = false`, `b() = true` (online:
   `a() = true`, `b() = false`). So `b()` behaves as a "no connection" flag.
5. Snapshot diff: `S4_G` `lesson_progress=1` (`in_queue=1`) →
   `S4_H_OFFLINE_COLD_START` `lesson_progress=0` → `S4_I_OFFLINE_RESTORED` `0`.
   `tutorial_completions=868` and `room_master_table` identity hash
   `2b8ab6d303d9a501bd8c8fb78d8352fc` are unchanged, so the DB was not wiped.

## Classification
| Behaviour | Class | Evidence |
|---|---|---|
| `in_queue=1` Room row written locally on lesson completion | A local, B queued | `createLessonProgress`/`e0`/`queue_store` hooks + `S4_C` row |
| offline `postUnsyncedLessonProgress` throws `com.getmimo.network.NoConnectionException` | B local + queued, D remote required to flush | `throw` record |
| queued row removed on offline cold start | A local (destructive) — `DELETE FROM lesson_progress WHERE in_queue = 1` | SQL hooks + snapshot diff |
| UI/path map restored offline | A local | `UI/S4_H_OFFLINE_COLD_START.xml`, `UI/S4_I_OFFLINE_RESTORED.xml`, `S4OFFNAV-01..08.xml` |
| analytics rows continue to accumulate offline | B local + queued | mixpanel / datatransport row counts |
| server acknowledgement of progress | **NOT OBSERVED** (`SERVER CONFIRMED=0`) | no response body, no auth, no server reconstruction |

**Conclusion:** on this build the client-side "offline queue" is not a durable
restore mechanism for `lesson_progress` across a cold start — the `in_queue=1`
row is deleted during startup. M06's static reading is `VERIFIED_BOTH` for the
exception but `PARTIALLY VERIFIED` for "leaves Room rows". M05's suggestion
that an unsynced row would persist after force-stop is therefore **not
confirmed** by M07 runtime evidence.

## DataStore / SharedPreferences
47–95 private files per snapshot. `files/datastore/user_preferences.preferences_pb`
and `shared_prefs/*.xml` are captured byte-for-byte in
`DB/SNAPSHOT_*/private/`. No `mimo_dev_prefs.xml` was present. Exact key/value
semantics of the protobuf DataStore were not decoded (`UNKNOWN`); its presence,
size and hash are `VERIFIED_RUNTIME`.

## Stage 5 repetition (run `42030594857`)
`EXPERIMENTS/S5_OFFLINE_ISOLATION.txt` again proves `Active default network:
none` / `Network is unreachable` / `airplane_mode_on=1`.
`S5_G` had **2** `lesson_progress` rows (151410 and 151403, both `in_queue=1`);
`S5_H_OFFLINE_COLD_START` and `S5_I_OFFLINE_RESTORED` had **0**.
`tutorial_completions=868` and the Room identity hash were unchanged. This
reproduces the stage-4 queue-deletion result with the row created by a real
correct answer, and strengthens the conclusion that `in_queue=1` rows are not
restored after an offline cold start on this build. Offline Frida trace
`TRACES/STAGE5_OFFLINE.jsonl` records 24 `net_isOnline` / 24 `net_isOnline_b`
calls and 903 SQL events.
