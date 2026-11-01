# 05 — SPEC: learner model and progress (normative)

Sources: `data/learner_model.json`, `data/progress_vectors.json`, `mimo-re/mission-08/05_LEARNER_MODEL/`.
`VERIFIED_STATIC`.

## 1. The entity `LessonProgress` — 11 fields, constructor order fixed

| # | Field | Type | Role | Column | Meaning |
|---|---|---|---|---|---|
| 1 | `lessonId` | long | PK part 1 | `lesson_id` | lesson identity |
| 2 | `tutorialId` | long | PK part 2 | `tutorial_id` | content grouping / sync unit |
| 3 | `tutorialVersion` | int | payload | `tutorial_version` | tutorial content version |
| 4 | `trackId` | long | payload, **not** key | `track_id` | attribution |
| 5 | `publishSetVersion` | long | payload | `publish_set_version` | content baseline |
| 6 | `tries` | int | **solved flag 0/1** | `tries` | `isSolvedCorrectly() = tries >= 1` |
| 7 | `attempts` | int | session counter | `attempts` | submissions in this session |
| 8 | `startedAt` | Instant | open time | `started_at` | duration source |
| 9 | `completedAt` | Instant | creation time | `completed_at` | ordering guard |
| 10 | `isPracticeProgress` | boolean | practice marker | `is_practice_progress` | practise vs course |
| 11 | `inQueue` | boolean | `1` at creation | `in_queue` | outbox pending flag |

The primary key is **`(lessonId, tutorialId)`** — two columns, not five (see `02` §5, correction C-16).

## 2. Creation rule

```text
createLessonProgress(lesson):
    completedAt   = now()
    startedAt     = lessonOpenTime
    publishSetVersion = currentTracksBundleValue      // from the loaded pack
    tutorialVersion   = lesson.tutorialVersion
    tries = 0 ; attempts = 0 ; inQueue = true ; isPracticeProgress = lesson.isPractice
```

## 3. Ordering guard

```text
if now() < startedAt:  throw RuntimeException("...")   // reported to crash reporting, swallowed
```
The entity is still built afterwards, so the row is written. Reproduce the *outcome* (row written, error logged), not
the exception type.

## 4. Update on submit — three call sites, three rules

| Site | Trigger | `attempts` | `tries` |
|---|---|---|---|
| `V` | verdict CORRECT | +1 | `!(C == TRUE)` → **0** |
| `W` | verdict PARTIAL/other | +1 | `!(C == TRUE)` → **1** |
| `X` | verdict INCORRECT | +1 | `0` |
| `U` | practice/alternate path | +1 | `(C == TRUE)` → **1** |

Any of these leaves `tries >= 1` once the lesson has been solved, which is what `isSolvedCorrectly()` reads. **`tries`
is never incremented.**

## 5. Derived metrics (all computed from the rows above)

| Metric | Rule |
|---|---|
| `isSolvedCorrectly` | `tries >= 1` |
| `firstTryCount` | `solved && attempts == 1` |
| `AnswersInChapter(correct, total)` | aggregate over **pending** rows of the chapter |
| `duration` | `completedAt − startedAt` |
| queue | rows with `in_queue = 1` |

## 6. Sync protocol (this is where Mimo's server dependency lives)

```text
store  : insert row with in_queue = 1
move   : set in_queue = 0 (claimed for upload)
post   : POST all claimed rows  ──success──▶ DELETE the posted ids
clear  : DELETE rows with in_queue = 1 (needs reconnect / reset)
```

Consequences you must decide about:
* progress is **deleted after a successful upload** → no local history, no offline analytics (correction C-22);
* a failed POST keeps rows (they are still `in_queue = 0` after `move`, so the retry path is not fully recovered — A-04).

## 7. The completion boundary — the single most important design fact

```text
GET /v1/tracks/{id}/completion  →  tutorial_completions / chapter_completions tables  →  UI
```

The client **never** computes whether a tutorial or chapter is complete, and **never** decides unlocks. It caches the
server's answer (`is_completed`, `updated_at`). 5 DAO statements for `tutorial_completions`, 6 for `chapter_completions`,
all server-fed.

→ For the offline engine, `ADD-04` replaces this with a **local completion rule** (recommended: a chapter is complete
when every lesson in it has a row with `tries >= 1`; a tutorial likewise), and the rule must be documented as
`DIVERGES_FROM_MIMO` in `mimo/DELTAS.md`.

## 8. Wire payload

`toProgressList` maps **9** of the 11 fields into the `Progress` DTO:
`lessonId, completedAt, startedAt, tries, tutorialVersion, trackId, publishSetVersion, attempts, isPracticeProgress`.
`inQueue` and the DAO internals stay local.

## 9. Acceptance

`data/progress_vectors.json` pins: identity, creation, ordering guard, six counter updates, three completion-flag cases,
four queue transitions, retrieval, chapter answers, first-try, version-change, wire mapping. Reproduce them all.
