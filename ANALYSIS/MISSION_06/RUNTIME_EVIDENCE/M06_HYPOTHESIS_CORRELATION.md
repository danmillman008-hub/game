# M06 static methods ↔ M05 runtime observations

Classification: `VERIFIED_BOTH` only where a M05 observation and M06 bytecode both exist.
No M06 screenshot/log is presented as newly captured.

| # | M06 `VERIFIED_STATIC` method | M05 `VERIFIED_RUNTIME` observation | Classification | Reproduction |
|---|---|---|---|---|
| 1 | `Lye/b.b(J)` opens `lessons-<lang>/tracks/tutorial-<id>.json` | `42003884423` STEP-24 rendered tutorial-904 lesson 151403 ("Guess the letter"); `42006697783` rendered offline track 274 AI/ChatGPT lessons | `VERIFIED_BOTH` | M05 `RUNTIME/RUN_42003884423_FINDINGS.md`, `RUN_42006697783_FINDINGS.md`, `EVIDENCE/RUNTIME_STATIC_MATCH.json` MATCH-1/3/4/5 |
| 2 | `LessonContent$Executable` + `solvedContent` shipped in APK | `42003884423` OFFLINE-03 rendered tutorial-2199 lesson 63259 executable lesson | `VERIFIED_BOTH` | MATCH-2, `SAMPLES/runtime_matched_executable_lesson_63259.json` |
| 3 | `base/c.X()` → `d0()` wrong-feedback block | `42005358012` wrong answer → red "Try again", Q disabled/grey, `Continue` → code editor | `VERIFIED_BOTH` | M05 `RUNTIME/RUN_42003884423_FINDINGS.md` / run-004 archive notes; STEP screenshots in M05 |
| 4 | `NetworkUtils.a()` `hasTransport(WIFI|CELLULAR)` gate; `postUnsyncedLessonProgress` offline guard | `42002808217` cold start with `Active default network: none`, `NetworkUnknown`/`UnknownHostException` for analytics, no FATAL/ANR; first three offline XMLs byte-identical to online | `VERIFIED_BOTH` | M05 `RUNTIME/RUN_42002808217_FINDINGS.md` |
| 5 | `ChapterFinishedViewModel$handleOfflineState$1` → local already-completed state | M05 run-002/003 path screen "Connect to the internet to progress further" while local lesson content remained visible | `VERIFIED_BOTH` | M05 `RUNTIME/RUN_42002808217_FINDINGS.md` |
| 6 | `Lqm/i.a` normalizer / `lim/d.E0` / `Lkm/f.b` / `Lpm/b.E0` / `q.I` answer validators | **No correct answer or offline answer was ever submitted** in M05 runs 001–005 | `VERIFIED_STATIC` only | `UNKNOWN` for correct-answer runtime state |
| 7 | `LessonProgressQueue.storeLessonProgress` → Room `lesson_progress` `in_queue=1` | **No private DB read** was permitted; no persisted-progress-after-answer observation | `VERIFIED_STATIC` only | `UNKNOWN` for persisted row |

## Explicitly NOT claimed
- No M06 emulator screenshots, XML dumps, logcat, `dumpsys` or device state were collected.
- No server response body was observed. `SERVER CONFIRMED = 0`.
- No offline reconnect was demonstrated (`svc wifi enable`/`svc data enable` did not
  restore connectivity in M05 runs 002/003).
