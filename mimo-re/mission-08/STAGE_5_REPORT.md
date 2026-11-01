# Mission 8 — Stage 5 Report (learner model, progress, completion)

**Status:** `substantially_complete` (12/12 deliverables + 16 semantic tests) · **Base:** Stage 4 `df259d7` · **2026-11-01**

## The three findings that change the picture

**1. `tries` is a flag, not a counter.** All four writers go through `base.c.H(tries, attempts)`. `V` passes
`!(C == TRUE)`, `X` passes `0`, `U` passes `(C == TRUE)`. So `tries ∈ {0,1}` and `isSolvedCorrectly()` (`tries >= 1`)
is a boolean. Nothing accumulates.

**2. `attempts` is session-scoped.** It comes from view-model field `d`, incremented before every `H(...)`, with no
initialiser and no reader of stored progress. Therefore `getCorrectLessonsFirstTryCount()` measures "first attempt of
this session", not first attempt ever.

**3. Progress is keyed `(lesson_id, tutorial_id)`.** The five-part `LessonIdentifier` is navigation-only; `chapterId`
is never persisted. The Room schema, the INSERT column list and the UPDATE's `WHERE lesson_id = ? AND tutorial_id = ?`
all agree.

## Repository and queue

* `createLessonProgress` builds the entity locally (`completedAt = now`, `publishSetVersion` from `tracks.json` = 753,
  `inQueue = 1`) and reports-but-ignores a clock-skew anomaly.
* `in_queue` is a **local outbox flag** with exactly three statements: `SELECT … WHERE in_queue = 1`, `UPDATE … SET
  in_queue = 0 WHERE in_queue = 1`, `DELETE … WHERE in_queue = 1`, plus `postUnsyncedLessonProgress` which does
  `SELECT *` → group by `tutorialId` → `POST /v1/tutorials/{tutorialId}/progress` → `DELETE` the posted ids.
* Offline → `NoConnectionException`; the rows survive for the next start (`MainViewModel` startup path).
* `ChapterViewModel.clearOnExit` deletes pending rows — unsynced progress can be discarded (B-6).

## Completion is server-derived

`CompletionRepository.fetchTrackCompletion(trackId, trackVersion)` calls `GET /v1/tracks/{trackId}/completion`, then
writes `tutorial_completions` and `chapter_completions` rows and a `last_interacted_tutorial_id_<trackId>` preference.
`attachTutorialAndChapterCompletionToTrack` copies those flags into immutable content copies. **Solving a lesson never
creates a completion row** — only the server response does.

## Progression, effect by effect

Lesson advancement, chapter-end refresh and the completion attach are `VERIFIED_STATIC`. Unlock, XP and league have
**no client implementation** in the learner model; `reachedGoal` and `dailyGoalCoinReward` arrive from the server in
`PostProgressResponse` and are only forwarded. The ordering `store → move → POST → getTrackCompletion → UI` is proven
and is the whole client-side progression loop.

## Corrections

* **C-15** — `base.c.e0` is `storeLessonProgressInMemory` (its continuation class is
  `InteractiveLessonBaseViewModel$storeLessonProgressInMemory$1/$2`), not `initialiseViewModel` as the Stage-1 mapping
  claimed. This resolves open question **A18** and leaves `initialiseViewModel` unidentified.
* **C-16** — the progress key recorded in Stages 3/4 as `(trackId, lessonId)` is `(lesson_id, tutorial_id)`; `trackId`
  is a payload column, not part of the key.

## Limits

No backend rule is claimed. Eight questions registered (B-1 … B-8), including the exact DAO id→SQL assignment for the
25 remaining generated queries, the account-partitioning question (no account column anywhere) and the streak sink.
Nothing here is `VERIFIED_RUNTIME`.
