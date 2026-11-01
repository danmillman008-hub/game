# Phase 5A — `LessonProgress`, field by field

## 1. The entity

```text
com.getmimo.data.model.room.LessonProgress   (Room entity, table lesson_progress)
LessonProgress(lessonId: J, completedAt: Instant, startedAt: Instant, tries: I,
               tutorialId: J, tutorialVersion: I, trackId: J, publishSetVersion: J,
               attempts: I, isPracticeProgress: Z, inQueue: Z)
```

The constructor argument order is proven by the `iput` sequence of `<init>` and by the 11-column `INSERT` list in the
Room adapter (`cg/b`). It is **not** the field-declaration order.

| Field | Column | Role | Initial value (measured) |
|---|---|---|---|
| `lessonId` | `lesson_id` | **primary key part 1** | `LessonBundle.a` |
| `tutorialId` | `tutorial_id` | **primary key part 2** | `LessonBundle.e` |
| `tutorialVersion` | `tutorial_version` | payload | `LessonBundle.v` |
| `trackId` | `track_id` | payload (not a key) | `LessonBundle.f` |
| `publishSetVersion` | `publish_set_version` | payload | `DefaultTracksRepository.getPublishSetVersion()` → `tracks.json` value **753** |
| `tries` | `tries` | solved indicator | `!(C == TRUE)` on correct, `0` on incorrect |
| `attempts` | `attempts` | session counter | view-model field `d` after `+1` |
| `startedAt` | `started_at` | payload | view-model field `I`, set when the lesson opened |
| `completedAt` | `completed_at` | payload | `new Instant()` inside `createLessonProgress` |
| `isPracticeProgress` | `is_practice_progress` | payload | `LessonBundle.B` |
| `inQueue` | `in_queue` | local sync flag | literal `1` |

## 2. `tries` — resolved, and it is *not* a counter

The whole app has four writers of `tries` (all through `base.c.H`, which forwards its first `int` parameter):

| Caller | First argument to `H(tries, attempts)` |
|---|---|
| `V` `lessonSolvedCorrectly` | `!(field C == TRUE)` → **1 on the first correct answer, 0 afterwards** |
| `X` `lessonSolvedIncorrectly` | `const 0` |
| `U` `lessonSolvedAndProceedToNextLesson` | `(field C == TRUE)` |
| `W` partial match | same shape as `V` |

So `tries ∈ {0,1}` — it is a **solved flag**, not an attempt counter. This is why `isSolvedCorrectly()` is
`tries >= 1` (body: `if (this.tries < 1) return false; else return true;`) and why the value is stable: once a lesson
is correct, `C` becomes `TRUE` and subsequent submissions write `0`, i.e. the flag is **retained, never incremented**.

## 3. `attempts` — a session counter, not a lifetime counter

`V`, `W`, `X` and `U` all execute the same three instructions before building the entity:

```text
v = this.d ; v = v + 1 ; this.d = v      // field d is the only source of attempts
```

`field d` has **no initialiser other than 0** and **no reader of stored progress**: a scan of every `iput` to
`base.c.d` finds only those four methods, and no method copies `LessonProgress.getAttempts()` into `d`. Therefore:

* `attempts` counts submissions **inside one view-model instance** (one lesson session);
* it is not capped, not compared with a maximum, and not restored from the database;
* `getCorrectLessonsFirstTryCount()` (which counts rows with `isSolvedCorrectly() && attempts == 1`) therefore measures
  *first attempt of the session*, not first attempt ever.

## 4. Ordering guard

`createLessonProgress` compares `now` with `startedAt`:

```text
if (now.isBefore(startedAt))  le0.a.d(new RuntimeException("CreateLessonProgress: completedAt date (…) is before startedAt date (…)"))
```
The exception is **reported to the crash/telemetry sink and discarded** — the entity is still constructed. A clock skew
therefore produces a reported-but-ignored anomaly rather than a failed write.

## 5. Mutability

`LessonProgress` is an immutable Kotlin data class: the only "mutation" primitive is `copy(...)` / `copy$default(...)`.
Every write path in the app goes through `copy` — `addOrUpdateLessonProgressInQueue` flips `inQueue` this way, and the
synthetic hard-mode interactor (`interactors.chapter.f.a`) builds a modified copy with a decremented value and shifted
timestamps.

## 6. Serialisation

* Room: 11 columns, types `INTEGER`/`REAL`-as-long and `Instant` stored as epoch millis (adapter reads
  `org.joda.time.Instant`, error string `Expected NON-NULL 'org.joda.time.Instant', but it was NULL.`).
* Wire: **not** serialised directly. `toProgressList` converts entity → `Progress` DTO
  (`lessonId, completedAt: Date, startedAt: Date, tries, tutorialVersion, trackId, publishSetVersion, attempts,
  isPracticeProgress`) and that list becomes `PostProgressRequestBody(progressList)`.

## 7. What the entity does *not* carry

No account/user column, no device id, no `chapterId`, no `sectionId`, no score, no duration, no answer text. Learner
identity is therefore **not part of the row** (see `PROGRESS_KEY_AND_VERSIONING.md` §4).
