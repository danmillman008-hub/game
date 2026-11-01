# Mission 5 — Progress Model (local, queued, remote)

## Scope
The three-layer progress model: the Room row that the app writes locally, the in-memory queue that
decides what is posted, and the network DTO that leaves the device. Includes the derived predicates
(completion, first-try, streak) and the sync/delete behaviour.

## Method
Read the Room entity, its generated writers (`cg.b`, `cg.c` — INSERT/UPDATE SQL literals), the
repository (`LessonProgressRepository`), the queue (`LessonProgressQueue`), and the wire DTO
(`Progress`, `PostProgressRequestBody`, `PostProgressResponse`). Joined them with the API catalogue
rows for the progress endpoints.

## Sources
| Layer | Symbol |
|---|---|
| Entity | `com.getmimo.data.model.room.LessonProgress` |
| Generated SQL | `cg.b` (INSERT), `cg.c` (UPDATE), `LessonProgressRepository$postUnsyncedLessonProgress$2` (DELETE) |
| Queue | `com.getmimo.data.source.remote.progress.LessonProgressQueue` |
| Wire DTO | `com.getmimo.data.model.progress.Progress`, `PostProgressRequestBody`, `PostProgressResponse` |
| Endpoint | `POST /v1/tutorials/{tutorialId}/progress` (`evidence/API_CATALOG_V2.csv`) |

## Findings — the local row (VERIFIED_STATIC)
`lesson_progress` — 11 columns, from the generated INSERT literal:
```
lesson_id, completed_at, started_at, tries, tutorial_id, tutorial_version,
track_id, publish_set_version, attempts, is_practice_progress, in_queue
PRIMARY KEY (lesson_id, tutorial_id)        -- from the generated UPDATE ... WHERE clause
```
`completed_at`/`started_at` are stored through `Converters.fromInstant` (Joda `Instant` → INTEGER
epoch millis), confirmed by the binder code in `cg.b`.

Related tables (same generated-SQL method):
| Table | Columns | Key |
|---|---|---|
| `chapter_completions` | `chapter_id, created_at, track_id, tutorial_id` | `(chapter_id, track_id)` |
| `tutorial_completions` | `tutorial_id, is_completed, updated_at, track_id` | `(tutorial_id, track_id)` |

## Findings — field semantics (VERIFIED_STATIC, corrected)
| Column | Type | Real meaning |
|---|---|---|
| `tries` | int | **0/1 correctness flag** — `isSolvedCorrectly()` is `return tries >= 1;` |
| `attempts` | int | number of submissions in this lesson session |
| `in_queue` | int | 1 while the row is not yet acknowledged by the server; set to 1 on insert |
| `is_practice_progress` | boolean | distinguishes practice-tab attempts from track attempts |
| `publish_set_version` | long | content-pack version, read from the tracks repository at write time |

This corrects mission-04's model of "two counters" (`tries` = restarts, `attempts` = checks). `tries`
was never a counter.

## Findings — derived predicates (VERIFIED_STATIC)
```
isSolvedCorrectly()        = tries >= 1
isFirstTrySuccess()        = isSolvedCorrectly() && attempts == 1     -- LessonProgressQueue:196
```
`getCorrectLessonProgressCount()` and `getCorrectLessonsFirstTryCount()` are the two aggregates the UI
and analytics consume; both are computed by filtering the queue contents in memory, not by SQL.

## Findings — queue and sync (VERIFIED_STATIC)
```
storeLessonProgress(p, postToServer, moveFromQueue, ...) :
    write row (in_queue = 1)
    [if postToServer] → addOrUpdateLessonProgressInQueue → postProgress(tutorialId, PostProgressRequestBody(list))
    on success      → moveLessonProgressFromQueue → DELETE FROM lesson_progress WHERE lesson_id IN (...)
postUnsyncedLessonProgress() :
    batches of unsynced rows → POST → delete the batch on success
```
The delete is a **batched IN-list** built by string concatenation at the call site (see
`evidence/ROOM_SQL_LITERALS.csv`), i.e. the app deletes local progress once the server acknowledges
it — local history is *not* retained as an archive.

## Findings — wire shape (VERIFIED_STATIC)
`Progress` (Serializable, 9 fields, all boxed):
```
lessonId, completedAt, startedAt, tries, tutorialVersion,
trackId, publishSetVersion, attempts, isPracticeProgress
```
`PostProgressRequestBody` wraps a `List<Progress>`. The mapping is a straight 1:1 copy including
`tries` and `attempts` (`LessonProgressRepository:64`). Endpoint:
`POST /v1/tutorials/{tutorialId}/progress` → `PostProgressResponse`.

## Findings — gamification surfaces (partially verified)
- `GET /v1/user/activity` → `UserActivityResponse` (`from`/`to` query bounds) feeds the streak view.
- `GET /v1/user/coins` → `Coins`; `GET /v1/user/keys` → `UserKeys` (`Time-Zone` header);
  `POST /v1/user/keys/consume`; `GET /v1/user/rewards/next` → `Rewards`;
  `POST /v1/user/rewards/{rewardId}/confirm`.
- `LessonProgressQueue.updateLessonStreakDetector(LessonProgress, boolean)` exists and reacts to a
  stored row, i.e. **streak advancement is driven by local success**, but the detector's internals
  were not read this mission.

## Evidence labels
- Columns, key, SQL, DTO shape, predicates, queue flow: **VERIFIED_STATIC**.
- Streak *algorithm* (window length, repair rules, timezone handling): **UNKNOWN** for the client;
  the server owns the authoritative value (`/v1/user/activity`).
- Coin/key/reward *earning formulas*: **UNKNOWN** (server-side; `Coins`/`Rewards` are response DTOs).

## Limitations
- No `CREATE TABLE` DDL was recoverable: the app's `Database_Impl` declares only table names and
  delegates creation to a base class whose body DAD did not emit. Column order and keys are taken
  from generated INSERT/UPDATE statements, which is reliable, but column *affinity* for
  `publish_set_version`/`tutorial_version` is inferred from the Java types.
- Nothing here is runtime-verified; `in_queue` transitions are read, not observed.

## Unresolved
`U-09` streak algorithm; `U-10` whether the server recomputes `tries`; `U-11` offline conflict policy
when the same lesson is completed on two devices.

## Reproduction
```bash
grep -n 'INSERT INTO `lesson_progress`' -r /tmp/dad/cg.b.java
grep -n 'isSolvedCorrectly' /tmp/dad/com.getmimo.data.model.room.LessonProgress.java
grep -n 'getAttempts() == 1' /tmp/dad/com.getmimo.data.source.remote.progress.LessonProgressQueue.java
```
