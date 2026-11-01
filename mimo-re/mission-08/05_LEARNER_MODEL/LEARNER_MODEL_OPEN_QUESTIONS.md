# Phase 5 — open questions

| ID | Question | Evidence so far | Blocker |
|---|---|---|---|
| B-1 | exact id→SQL assignment for the 29 DAO lambdas | ids 18–21 map to the four `lesson_progress` statements by name/semantics; the other 25 belong to other tables | the switch payload has no symbol names; id assignment of the four is inferred from correspondence |
| B-2 | is progress intentionally not partitioned by account? | no account column in `lesson_progress`, `tutorial_completions`, `chapter_completions`, nor in the `Progress` DTO | design intent is not in the code; needs product context |
| B-3 | what happens when the progress POST fails with a non-network error | no try/catch in `postUnsyncedLessonProgress`; the exception leaves the coroutine | caller scopes not exhaustively read |
| B-4 | is there any track-level completion predicate? | no field, no method; only tutorial/chapter flags | could live in the server or in a screen we did not read |
| B-5 | what consumes `gg.e` (streak sink)? | `updateLessonStreakDetector` calls `gg.e.a(Z,Z)` which enqueues boolean pairs into a channel | channel consumer not traced (Phase 9/13 territory) |
| B-6 | can `ChapterViewModel.clearOnExit` delete unsynced progress before the flush? | it calls `LessonProgressQueue.clear()` → `DELETE WHERE in_queue = 1` | ordering of exit vs flush not traced |
| B-7 | does the POST send one request per tutorial or batches? | grouping by `tutorialId` then one `postProgress` call per group in the loop we read | whether the loop is sequential or parallel was not resolved from the state machine |
| B-8 | is `attempts` ever merged with a stored value server-side? | client always sends the session value | server behaviour is outside the client |

## Deliberate non-claims

* No backend completion rule is claimed. The client contract (endpoint + DTO) is all we have.
* No claim that `tries` accumulates across sessions: the code contradicts it.
* No claim that unlock/XP/league are absent from the app — only that they are not in this repository, and that the
  attributes we can read (`reachedGoal`, `dailyGoalCoinReward`) come from the server.
