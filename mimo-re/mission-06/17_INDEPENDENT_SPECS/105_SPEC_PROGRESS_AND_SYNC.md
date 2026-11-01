# Spec 105 — Progress and Sync

## MUST
1. Persist rows with key `(lesson_id, tutorial_id)`; `in_queue=1` at insert.
2. Store: versions (`publish_set_version`, `tutorial_version`), `tries`, `attempts`, timestamps.
3. Record an abandoned lesson as `tries=0, attempts=0`.
4. Push per tutorial: `POST /v1/tutorials/{tutorialId}/progress {progressList}`.
5. Delete pushed rows only on success; retain on any failure (no dead-letter).
6. Honour `{reachedGoal, dailyGoalCoinReward}` from the push response as display only.
7. Two completion marker tables (chapter, tutorial).

## MUST NOT
- Implement a merge engine, watermark, retry counter or backoff: none exists.
- Download raw progress rows: no such endpoint was recovered.

## GIVEN EVIDENCE
`06_PERSISTENCE_AND_SYNC/40..46`.
