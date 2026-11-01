# 07 — Learner model and completion

## 1. Data dictionary — `lesson_progress` (11 columns)

| Column | Type | Meaning | Written by |
|---|---|---|---|
| `lesson_id` | long | **PK part 1** | `createLessonProgress` from `LessonBundle.a` |
| `tutorial_id` | long | **PK part 2** | from `LessonBundle.e` |
| `tutorial_version` | int | content version | from `LessonBundle.v` |
| `track_id` | long | attribution (not key) | from `LessonBundle.f` |
| `publish_set_version` | long | content baseline | `TracksRepository.getPublishSetVersion()` (753) |
| `tries` | int | **solved flag (0/1)** | `V` = `!(C==TRUE)`, `X` = 0, `U` = `(C==TRUE)` |
| `attempts` | int | **session counter** | view-model `d` after `+1` |
| `started_at` | Instant | lesson opened | view-model `I` |
| `completed_at` | Instant | row creation | `new Instant()` |
| `is_practice_progress` | boolean | practice run | `LessonBundle.B` |
| `in_queue` | boolean | outbox marker | `1` at creation, `0` after move |

## 2. What the model is and is not

* **is**: a per-session, per-lesson outcome record used as a transport payload;
* **is not**: a history. `attempts` never accumulates across sessions, `tries` never exceeds 1, and rows are deleted
  after a successful upload.

## 3. Outbox lifecycle

```text
store (in_queue=1) → move (1→0) → POST /v1/tutorials/{id}/progress → 2xx → DELETE WHERE lesson_id IN (…)
                        ↑ triggers: chapter end · app start
clear (DELETE WHERE in_queue=1) ← chapter exit  (pending rows lost, B-6 closed as mechanism)
```

## 4. Completion

| Fact | Where | Origin |
|---|---|---|
| lesson solved | `lesson_progress.tries` | client |
| tutorial completed | `tutorial_completions.is_completed` | **server** (`GET /v1/tracks/{id}/completion`) |
| chapter completed | presence of a `chapter_completions` row | **server** |
| track completed | no client representation | server |

Order: post progress → fetch completion → attach flags to immutable content copies → UI. Solving a lesson therefore
never creates a completion row by itself (`B-4`/`Q-49`).

## 5. Statistics the client can compute

`AnswersInChapter(correct, total)` over **pending** rows; `getCorrectLessonProgressCount` (solved count);
`getCorrectLessonsFirstTryCount` (solved **and** `attempts == 1` — i.e. first attempt *of the session*).

## 6. Reuse note (informational)

For a standalone offline engine the durable model must be redesigned: keep `LessonProgress`-style outcome records but
add (a) a per-user key, (b) a monotonic attempt history, (c) a local completion rule, and (d) an idempotent upload id.
None of those exist in Mimo; the *shape* of the entity and the store/move/post/delete lifecycle are still a usable
template.

**Evidence anchors:** `05_LEARNER_MODEL/LESSON_PROGRESS_FIELD_MAP.json`, `05_LEARNER_MODEL/PROGRESS_REPOSITORY_IMPLEMENTATION.md`, `05_LEARNER_MODEL/COMPLETION_REPOSITORY_IMPLEMENTATION.md`, `06_PERSISTENCE/ROOM_SCHEMA.json`, records E-P01…E-P04 in `16_CONSOLIDATED_EVIDENCE_REGISTER.json`.
