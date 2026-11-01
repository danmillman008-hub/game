# Phase 5B — `LessonProgressRepository` and `LessonProgressQueue`

Both classes kept their original method names (R8 did not rename them), so the repository is readable at the level of
names *and* bodies; this document cites the bodies.

## 1. Class shape

```text
LessonProgressRepository(lessonProgressApi, lessonProgressDao, networkUtils, dispatcherProvider,
                         tracksRepository, favoriteTracksRepository, completionRepository)
LessonProgressQueue(devMenuStorage, lessonProgressRepository)   // + answersInChapter StateFlow
```

## 2. Method-by-method

| Method | Insns | What it actually does |
|---|---|---|
| `createLessonProgress(bundle, startedAt, tries, attempts)` | 44 | builds the entity (no I/O), `completedAt = now`, `publishSetVersion = tracksRepository.getPublishSetVersion()`, `inQueue = 1`; reports the ordering anomaly (see 5A §4) |
| `addOrUpdateLessonProgressInQueue(list, flag, …)` | 62 | `copy$default` each row with `inQueue = true`, then a Room write on the IO dispatcher |
| `getAllLessonProgressInQueue()` | 22 | `DBUtil.performSuspending` with query id **20** → `SELECT * FROM lesson_progress WHERE in_queue = 1` |
| `moveLessonProgressFromQueue()` | 26 | query id **21** → `UPDATE lesson_progress SET in_queue = 0 WHERE in_queue = 1` |
| `clearLessonProgressQueue()` | 36 | query id **19** → `DELETE FROM lesson_progress WHERE in_queue = 1` |
| `postUnsyncedLessonProgress()` | 44 | network guard + launch; see §3 |
| `toProgressList(list)` | 76 | entity → DTO mapping for the POST body |
| `toLessonProgressSyncResult(response)` | 14 | `PostProgressResponse(reachedGoal, dailyGoalCoinReward)` → `cg.e(reachedGoal, dailyGoalCoinReward)` |
| `fetchTrackCompletionForFavoriteTracks()` | 239 | favourites → tracks → `CompletionRepository.fetchTrackCompletion(trackId, trackVersion)` per track, logs `"Successfully fetched track completions for …"` |

Query ids 18–21 were read from the `bb/j` switch (29 generated cases) and matched to the four SQL statements by
method-name correspondence; the mapping is internally consistent (see `INQUEUE_IMPLEMENTATION.md` §2 for why).

## 3. `postUnsyncedLessonProgress` — the only network path

```text
if (!networkUtils.a()) {                       // com.getmimo.network.a.a() = isConnected
    log "No internet connection, not posting unsynced lesson progress"
    throw NoConnectionException
}
launch {
    rows = SELECT * FROM lesson_progress        // id 18 — ALL rows, not only in_queue = 1
    group rows by tutorialId
    for each group: POST /v1/tutorials/{tutorialId}/progress  body = PostProgressRequestBody(toProgressList(group))
    result = toLessonProgressSyncResult(response)
    DELETE FROM lesson_progress WHERE lesson_id IN (<posted ids>)
}
```

Two consequences worth stating explicitly:

1. the POST body is **per tutorial**, not global — the grouping happens in the client;
2. a successful POST **deletes the rows it posted**; the local table is an outbox, not an archive. Anything the UI
   shows after that comes from the completion tables (`tutorial_completions`, `chapter_completions`) and from the
   server.

## 4. Error handling

* offline → `NoConnectionException` (typed, so callers can distinguish "not now" from "failed");
* HTTP failure → no catch block was found in the body; the exception propagates to the caller's coroutine scope
  (callers: `MainViewModel`, `LessonProgressQueue`), which is recorded as an open question (B-3);
* ordering anomaly in `createLessonProgress` → reported, ignored;
* no retry counter, no backoff, no dead-letter: retry is implicit (the rows are still there next time).

## 5. Queue facade (`LessonProgressQueue`)

| Method | Behaviour |
|---|---|
| `storeLessonProgress(progress, flagA, flagB)` | if the dev-menu gate allows, `addOrUpdateLessonProgressInQueue([progress], …)`, then `updateCorrectAnswersCount()`, then `updateLessonStreakDetector(progress, flag)` |
| `storeSyntheticLessonProgress(list)` | batch insert (used by the hard-mode/synthetic path) |
| `storeAndPostAllLessonProgress()` | `moveLessonProgressFromQueue()` then `postUnsyncedLessonProgress()` |
| `clear()` | `clearLessonProgressQueue()` |
| `getLessonProgress()` | `getAllLessonProgressInQueue()` |
| `getCorrectLessonProgressCount()` | counts `isSolvedCorrectly()` over the in-queue rows |
| `getCorrectLessonsFirstTryCount()` | counts `isSolvedCorrectly() && attempts == 1` |
| `updateCorrectAnswersCount()` | emits `AnswersInChapter(correct, total)` into a flow |
| `getAnswersInChapter()` | exposes that flow |

## 6. Who calls what

```text
base.c.e0 (storeLessonProgressInMemory)         → LessonProgressQueue.storeLessonProgress
ExecutableLessonViewModel.doOnLessonCorrectlySolved / initialise → LessonProgressQueue.storeLessonProgress
MainViewModel.fetchLessonProgressAndPostUnsyncedToBackend
        → LessonProgressRepository.postUnsyncedLessonProgress
        → LessonProgressRepository.clearLessonProgressQueue
        → LessonProgressRepository.fetchTrackCompletionForFavoriteTracks
ChapterViewModel.initialize / clearOnExit         → LessonProgressQueue.clear
ChapterViewModel.getExitType                      → getCorrectLessonProgressCount
ChapterFinishedViewModel.onChapterFinishedScreenShown → getLessonProgress
ChapterFinishedViewModel / GetChapterEndSuccessState → storeAndPostAllLessonProgress
```

Full machine-readable version: `PROGRESS_REPOSITORY_CALL_GRAPH.json`.
