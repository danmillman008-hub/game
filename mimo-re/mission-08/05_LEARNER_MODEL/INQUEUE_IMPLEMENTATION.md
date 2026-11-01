# Phase 5 — the `inQueue` mechanism, established

## 1. What `in_queue` is

A boolean column on `lesson_progress` that marks a row as **pending local delivery to the backend**. It is the only
state machine in the local learner store, and it has exactly three transitions:

```text
INSERT (in_queue = 1)          createLessonProgress / addOrUpdateLessonProgressInQueue
UPDATE 1 -> 0                  moveLessonProgressFromQueue
DELETE WHERE in_queue = 1      clearLessonProgressQueue
```

## 2. The four statements (measured)

| Query id | SQL | Repository method |
|---|---|---|
| 18 | `SELECT * FROM lesson_progress` | `postUnsyncedLessonProgress` |
| 19 | `DELETE FROM lesson_progress WHERE in_queue = 1` | `clearLessonProgressQueue` |
| 20 | `SELECT * FROM lesson_progress WHERE in_queue = 1` | `getAllLessonProgressInQueue` |
| 21 | `UPDATE lesson_progress SET in_queue = 0 WHERE in_queue = 1` | `moveLessonProgressFromQueue` |

Ids were read from the `packed-switch` of the Room-generated `Function1` (`bb/j`, 29 cases); the four SQL literals are
the only `lesson_progress` statements in that class. The assignment above follows method semantics and is consistent
with every call site (a *move* cannot reasonably be a delete; the *clear* cannot be a select). Confidence **HIGH for
the SQL set, MEDIUM-HIGH for the id assignment** — recorded as such in `LEARNER_MODEL_OPEN_QUESTIONS.md` (B-1).

## 3. The full lifecycle

```text
1. lesson graded              base.c.V/W/X/U
2. entity built               LessonProgressRepository.createLessonProgress   (inQueue = 1)
3. stored                     LessonProgressQueue.storeLessonProgress
                                   → addOrUpdateLessonProgressInQueue([row], …)   (upsert, inQueue = true)
                                   → updateCorrectAnswersCount()                  (SELECT WHERE in_queue = 1)
                                   → updateLessonStreakDetector(row, flag)
4. two triggers flush the queue
   a) automatically after a chapter finishes:
        GetChapterEndSuccessState / ChapterFinishedViewModel → storeAndPostAllLessonProgress()
            moveLessonProgressFromQueue()      UPDATE 1 -> 0
            postUnsyncedLessonProgress()       SELECT *  → POST per tutorialId → DELETE posted ids
   b) at application start:
        MainViewModel.fetchLessonProgressAndPostUnsyncedToBackend()
            postUnsyncedLessonProgress(); clearLessonProgressQueue(); fetchTrackCompletionForFavoriteTracks()
5. chapter boundaries clear leftovers:
        ChapterViewModel.initialize / clearOnExit → LessonProgressQueue.clear() → DELETE WHERE in_queue = 1
```

## 4. Why "move" exists at all

Because the POST selects **all** rows, not only pending ones: `moveLessonProgressFromQueue` is the *acknowledgement*
step that says "these rows have left the pending queue" before the network call, while the POST is what actually
delivers and then removes them. The `in_queue = 1` subset is then exactly "stored but not yet acknowledged".

This answers two otherwise puzzling observations:
* why `getAllLessonProgressInQueue` is the source of the `AnswersInChapter` counter — the counter tracks *not yet
  acknowledged* answers, i.e. it is a progress meter for the local outbox, not for the server;
* why a successful POST deletes rows — the local table is a transport buffer.

## 5. Failure behaviour

| Situation | Behaviour | Evidence |
|---|---|---|
| offline | `NoConnectionException` thrown, rows untouched | `networkUtils.a()` guard + literal log line |
| HTTP error | no catch in the repository; propagates to the caller coroutine | absence of try/catch in the body |
| app killed after store, before flush | rows persist with `in_queue = 1`, flushed at next start | MainViewModel startup path |
| chapter finished | flush happens before the completion fetch, so the server sees the progress first | `GetChapterEndSuccessState` call order |
| chapter left | `clear()` deletes pending rows — **unsynced progress is discarded** | `ChapterViewModel.clearOnExit` → `clearLessonProgressQueue` |

The last row is a real risk and is stated as a finding rather than a bug claim: pending rows are deleted when the
chapter view model clears, and no retry buffer survives that path.

## 6. What `in_queue` is *not*

* not a user-visible "offline mode" flag (no UI reads it);
* not a retry counter (there is no counter);
* not per-account (no account column anywhere in the table).
