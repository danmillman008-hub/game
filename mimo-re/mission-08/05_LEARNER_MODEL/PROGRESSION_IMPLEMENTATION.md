# Phase 5F — Progression: each effect traced independently

The brief asks not to assume these fire together. Each row below states what the code actually does.

| Effect | Trigger in code | Mechanism | Status |
|---|---|---|---|
| **Lesson advancement** | `base.c.U lessonSolvedAndProceedToNextLesson` | increments `d`, builds progress, `e0` stores it, emits `bundle.b` (int) into a flow and the lesson id into another flow | `VERIFIED_STATIC` |
| **Chapter finishing** | `GetChapterEndSuccessState` / `ChapterFinishedViewModel` | `storeAndPostAllLessonProgress()` → move (1→0) → POST → `fetchTrackCompletion(trackId)`; the screen reads completion *after* the round-trip | `VERIFIED_STATIC` |
| **Chapter completion** | server response → `chapter_completions` rows | `attachTutorialAndChapterCompletionToTrack` copies `isCompleted` into `Chapter` | `VERIFIED_STATIC` (client side) / `BACKEND_ONLY` (rule) |
| **Section progress** | `Section.hasProgress` lazy delegate | computed from tutorials' completion at access time; no write | `VERIFIED_STATIC` |
| **Track completion** | no client predicate | only `Track`'s tutorials/chapters carry flags; nothing computes a track-level boolean | `NOT_RECOVERED` |
| **Unlock conditions** | — | no lock/unlock field or rule in the client learner model; no `isLocked`, no dependency graph | `NOT_RECOVERED` |
| **XP** | `PostProgressResponse.dailyGoalCoinReward` → `cg.e` | the server returns a coin reward with the progress acknowledgement; the client stores it in the sync result object | `BACKEND_ONLY` (the value) / `VERIFIED_STATIC` (the transport) |
| **Streak** | `LessonProgressQueue.updateLessonStreakDetector(progress, flag)` → `gg.e.a(Z,Z)` | progress is pushed into an event sink; no streak value is computed or persisted in the tables we can see | `PARTIAL` |
| **League / leaderboard** | `base.c.H shouldShowLeaderboardBadge` (recovered in Stage 1, `ui.main.d`) | UI badge only; no league state in the learner tables | `PARTIAL` |
| **Daily goal** | `PostProgressResponse.reachedGoal` | server tells the client whether the goal was reached; client forwards it in the sync result | `BACKEND_ONLY` |

## The one ordering fact that matters

```text
store progress  →  move (in_queue 1→0)  →  POST  →  server  →  getTrackCompletion  →  UI completion
```

Everything downstream of the POST (chapter completion, next-chapter availability, daily goal, coins) is decided by the
backend. The client contributes exactly one input to that chain: the list of solved lessons with `tries`, `attempts`,
`tutorialVersion` and `publishSetVersion`.

## What the client *does* decide

* whether a lesson is solved (grading, Phase 4) — a client verdict that becomes `tries = 1`;
* how many submissions happened in the session (`attempts`);
* when to flush and when to clear the queue;
* nothing about completion, unlock, XP, coins or league.

## Open ends

* track-level completion has no client representation (question **B-4**);
* the streak sink `gg.e` emits into a channel we did not read (question **B-5**);
* whether `ChapterViewModel.clearOnExit` can delete unsynced progress before the flush (question **B-6**) — the code
  allows it, but whether both paths run in the same session was not traced.
