# Mission 6 — Progress Model

## Scope
The exact progress record and its five-level aggregation.

## Method
Room entity fields (mission-05, re-verified by table list), progress DTOs, endpoint inventory.

## Findings — record (VERIFIED_STATIC)
`lesson_progress` (11 columns, see Phase 6.40) stores: lesson/tutorial identity, `publish_set_version`,
`tutorial_version`, `tries`, `attempts`, `in_queue`, timestamps. **There is no score column.**

## Findings — aggregation
```
lesson  row(s)                       → chapter completion flag
chapter                              → chapter_completions row
tutorial                             → tutorial_completions row + POST /v1/tutorials/{id}/progress
track                                → GET /v1/tracks/{trackId}/completion { lastInteractedTutorialId, tutorials[] }
                                     → GET /v1/tracks/{trackId}/eta { currentPaceMinutesPerDay, trackEstimatedCompletionAt, sections[] }
```
`TrackEtaResponse` is the only *predictive* field in the system: the server estimates completion from the
learner's pace (minutes/day). No client-side estimator was found.

## Findings — queue semantics
Every write happens twice: locally (`in_queue=1`) and, when online, in a batch push
(`PostProgressRequestBody { progressList: List }`), after which pushed rows are deleted. Progress is
therefore **write-through with an offline outbox**, not a merge engine.

## Evidence labels
**VERIFIED_STATIC** for schema and endpoints; server aggregation rules **UNKNOWN**.

## Open questions
`Q-49` server-side recomputation; `Q-50` `eta` formula; `Q-54` whether deletes happen per-batch or per-row.

## Reproduction
`grep -n 'in_queue\|publish_set_version' -r /tmp/dad/com.getmimo.data.model.room.LessonProgress.java`
