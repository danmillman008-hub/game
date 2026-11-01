# Phase 5C — `CompletionRepository`

Recovered class: `com.getmimo.data.source.local.completion.a`; every method name below comes from the continuation
classes it instantiates (`CompletionRepository$<name>$1`), so the names are evidence, not guesses.

| Method | Insns | Recovered name |
|---|---|---|
| `a` | 302 | `attachTutorialAndChapterCompletionToTrack` |
| `b` | 178 | `attachTutorialCompletionToTrack` |
| `c` | 70 | `fetchLastInteractedTrackId` |
| `d` | 210 | `fetchTrackCompletion(trackId, trackVersion)` |
| `e` | 100 | `fetchTrackCompletion(trackId)` (loads the current track version, then calls `d`) |
| `f` | 83 | `getChapterCompletionCount(trackId)` |
| `g` | 272 | `getRecentlyCompletedTutorialTitles(track)` |

## 1. What completion *is*

Completion is **not computed on the client**. `fetchTrackCompletion` calls
`CompletionApi.getTrackCompletion(trackId, trackVersion)` (`GET /v1/tracks/{trackId}/completion`) and then stores what
the server returned:

```text
response = getTrackCompletion(trackId, trackVersion)
now = Instant()
for each tutorial in response.tutorials:
    for each chapterId in tutorial.completedChapters:
        ChapterCompletion(chapterId, now, trackId, tutorialId)
    TutorialCompletion(tutorialId, tutorial.isCompleted, now, trackId)
insert both lists into the DAO
SharedPreferences.putLong("last_interacted_tutorial_id_" + trackId, response.lastInteractedTutorialId)
```

So there are **three different completion facts**, and they come from three different places:

| Fact | Stored in | Origin |
|---|---|---|
| "this lesson is solved" | `lesson_progress.tries` | client (grading) |
| "this tutorial is completed" | `tutorial_completions.is_completed` | server response |
| "this chapter is completed" | presence of a `chapter_completions` row | server response |

A lesson being solved therefore **does not by itself create a completion row**; the row appears after the server
answers `getTrackCompletion`. That is the single most important boundary in the learner model.

## 2. How completion reaches the UI

`attachTutorialAndChapterCompletionToTrack(track)`:
1. reads `tutorial_completions` (by `track_id`) and `chapter_completions` (by `track_id`) from Room;
2. builds `tutorialId → TutorialCompletion` and `tutorialId → List<ChapterCompletion>` maps;
3. walks `Track.sections → Section.tutorials → Tutorial.chapters` and rebuilds **copies** with `isCompleted` set from
   the maps (`Tutorial.copy`, `Chapter.copy`, `Section.copy`, `Track.copy`);
4. returns the new immutable track.

The content model therefore stays immutable and completion is a *view* over the database. Consumers of the attach
functions: `GetPathMapState`, `GetPracticeTopics`, `b.a`, `e.e`, `e.g`, `f.a`, `ReactivationViewModel.fetchTrackProgress`.

## 3. Navigation and progression effects

| Consumer | Uses | Effect |
|---|---|---|
| `GetPathMapState` | `attachTutorialAndChapterCompletionToTrack` | path map shows completed tutorials/chapters |
| `GetPracticeTopics` | same attach | practice topics exclude/included by completion |
| `ReactivationViewModel.fetchTrackProgress` | `attachTutorialCompletionToTrack` + `getRecentlyCompletedTutorialTitles` | re-engagement copy |
| `GetSignupPrompt.getFinishedChaptersCount` | `getChapterCompletionCount` | signup prompt threshold |
| `GetChapterEndSuccessState` | `fetchTrackCompletion(trackId)` then `storeAndPostAllLessonProgress` | chapter-end screen refreshes completion **after** posting progress |
| `t.M` | `fetchLastInteractedTrackId` | "continue where you left off" |

The order in `GetChapterEndSuccessState` is the progression loop: **post progress → fetch completion**, i.e. the client
only knows a chapter is finished after the server has processed the posted progress. This is also why the client can
show a chapter-end screen and still not have the completion row for a moment.

## 4. What is *not* implemented client-side

* no unlock rule, no `isLocked` computation, no dependency graph — nothing in the client decides that chapter *n+1*
  becomes available;
* no XP, streak or league computation in this repository (the only adjacent code is
  `LessonProgressQueue.updateLessonStreakDetector` → `gg.e.a(boolean, boolean)`, an event sink);
* no client-side "did the user finish the chapter" predicate: `getChapterCompletionCount` just counts rows.

## 5. Persistence of completion

`tutorial_completions (tutorial_id, track_id, is_completed, updated_at)` and
`chapter_completions (chapter_id, track_id, created_at, tutorial_id)`, both with composite primary keys, written only
by `fetchTrackCompletion`. They are never deleted by any code path found in this mission (no DELETE statement exists
for either table), so completion is cumulative on the device.

## 6. Backend contract vs behaviour

The client proves only: *the server, given (trackId, trackVersion), returns a list of tutorials with `isCompleted` and
`completedChapters`, plus a `lastInteractedTutorialId`*. It does **not** prove the rules that produce those values
(thresholds, per-lesson requirements, retro-completion on version bumps). Those remain `BACKEND_ONLY`.
