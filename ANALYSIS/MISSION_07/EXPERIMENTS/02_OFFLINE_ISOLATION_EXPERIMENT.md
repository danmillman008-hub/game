# M07 — offline isolation and restoration experiment (distilled)

Commands (stage 4/5/6, `ANALYSIS/RUNTIME/MISSION_07/EXPERIMENTS/*OFFLINE_ISOLATION.txt`):
```
adb shell svc wifi disable
adb shell svc data disable
adb shell cmd connectivity airplane-mode enable
adb shell dumpsys connectivity | grep 'Active default network'   # -> none
adb shell ping -c 1 -W 2 8.8.8.8                                 # -> Network is unreachable
adb shell settings get global airplane_mode_on                   # -> 1
adb shell am force-stop com.getmimo
adb shell am start -n com.getmimo/.ui.SplashActivity_default
```
Before: `Active default network: 101/102` with connected LTE and WIFI agents.
After: `Active default network: none`. No reconnect was claimed (M05 showed
`svc wifi enable` did not restore connectivity).

Measured offline behaviour in `TRACES/STAGE4_OFFLINE.jsonl`:
`postUnsyncedLessonProgress` throws `com.getmimo.network.NoConnectionException`;
`DELETE FROM lesson_progress WHERE in_queue = 1` executes repeatedly;
`S4_G` 1 row → `S4_H/I` 0 rows; stage 5/6 reproduce with 2 rows → 0.
`tutorial_completions` (672/868 rows) and `room_master_table` identity hash
`2b8ab6d303d9a501bd8c8fb78d8352fc` are unchanged, so the DB was not wiped.
Analytics DBs continue to accumulate rows offline.

**Verdict:** `VERIFIED_RUNTIME`. The `in_queue=1` queue is **not durable** across
an offline cold start on this build — a correction to the M05/M06 expectation.
`SERVER CONFIRMED = 0`.
