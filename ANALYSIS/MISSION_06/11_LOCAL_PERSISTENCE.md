# MISSION 06 — DEEP CLIENT REVERSE ENGINEERING

**APK:** `48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a` (unchanged) · **branch** `arena/aebb90b7-game` · `SERVER CONFIRMED = 0`  
Evidence: `EVIDENCE/DISASM/*.smali.txt`, `SCHEMAS/METHOD_CATALOG_MIMO.json`,
`CALL_GRAPHS/*.json`, `METHOD_DOSSIERS/*.md`. Classification on every finding.

---

## VERIFIED_STATIC — Room schema (M05 SQL reused, M06 verified callers)
`ANALYSIS/MISSION_05/EVIDENCE/ROOM_SQL.txt`:
- `lesson_progress` 11 columns, PK(`lesson_id`,`tutorial_id`) @`classes.dex 2183344`.
- `chapter_completions` PK(`chapter_id`,`track_id`) @2183130.
- `tutorial_completions` PK(`tutorial_id`,`track_id`) @2183790.
- DAO strings: `SELECT * FROM lesson_progress WHERE in_queue = 1`,
  `UPDATE lesson_progress SET in_queue = 0 WHERE in_queue = 1`,
  `DELETE FROM lesson_progress WHERE in_queue = 1`,
  `SELECT COUNT(DISTINCT chapter_id) FROM chapter_completions`.
- Identity hashes `08b926448d86528e697981ddd30459f7`,
  `2b8ab6d303d9a501bd8c8fb78d8352fc`.
- 269 database tables in the APK (M05).

M06 verified the exact `LessonProgress` field order from
`LessonProgressRepository.createLessonProgress` @10063916 and the entity constructor
`(J Instant Instant I J I J J I Z Z)V`:
`lessonId, completedAt, startedAt, tries, tutorialId, tutorialVersion, trackId,
publishSetVersion, attempts, isPracticeProgress, inQueue`.

## VERIFIED_STATIC — write path
```
V()/X()/U()/W()
 → base/c.H(tries,attempts)
 → LessonProgressRepository.createLessonProgress(bundle, startedAt, tries, attempts)
 → base/c.e0()  (guard field M)
 → LessonProgressQueue.storeLessonProgress(progress, bool, bool, cont)
     ├─ if devMenuStorage.e() → return (dev override)
     ├─ LessonProgressRepository.addOrUpdateLessonProgressInQueue(listOf(progress), …)
     │    → Room lesson_progress (in_queue = 1)
     ├─ updateCorrectAnswersCount() → _answersInChapter StateFlow
     └─ if attempts == 1 → updateLessonStreakDetector
```
Diagram `DIAGRAMS/07_persistence_flow.mmd`; call graph `CALL_GRAPHS/07_progress_persistence.json`.

## VERIFIED_STATIC — queue drain / sync boundary
`LessonProgressQueue.storeAndPostAllLessonProgress` →
`LessonProgressRepository.moveLessonProgressFromQueue()` (clears `in_queue`) →
`postUnsyncedLessonProgress()`:
```
if (!networkUtils.a()) {
    log("No internet connection, not posting unsynced lesson progress")
    throw NoConnectionException
}
launch { POST via LessonProgressApi }
```
`SERVER CONFIRMED = 0`: no response bodies or server logic reconstructed.

## VERIFIED_STATIC — other stores
- `data/local/a; DataStoreUserPreferences`: `completed_hard_mode_chapters`,
  `KEY_HARD_MODE_COMPLETED_LESSON_IDS`, onboarding/first-run/path-overview flags,
  `dailyGoal`; `f(cont):Boolean`, `p()` reset used by `base/c.d0()`.
- SharedPreferences strings: `onboarding_user_daily_goal`, `networkUtils`,
  `KEY_HARD_MODE_COMPLETED_LESSON_IDS` (M05 `STORAGE_AND_ONBOARDING_STRINGS.txt`).
- In-memory: `m0` LiveData (`e,f,i,j,k,m,n,q,w,A,R`), `kotlinx.coroutines.flow.i`
  shared flow (`h`), `_answersInChapter` StateFlow, `LessonProgressQueue` unsynced rows.
- `Lye/d` reads/writes under `Context.getFilesDir()` (updated content);
  `base/c.D()` deletes `File(filesDir, lessonId.toString())` after a solve.
- `libdatastore_shared_counter.so` native counter (M04/M05) = `INFERRED` DataStore
  multi-process support.

## Lifecycle / force-stop — `UNKNOWN`
Room rows with `in_queue=1` survive process death by design of SQLite, but M06 has **no
runtime test** of force-stop → relaunch → queue restoration. No root/private DB extraction
was performed (forbidden). This is an explicit `UNKNOWN` with pointer
`LessonProgressRepository.getAllLessonProgressInQueue` / `LessonProgressDao` (`Lcg/a;`).

## Migrations — `UNKNOWN`
Room identity hashes are known; the full migration class list and SQL was not decoded in M06.
