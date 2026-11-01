# Phase 3.9 — Section and chapter completion

Scope note: the lesson engine *emits* completion signals; the *rules* live in the learner model (Phase 5) and the
persistence layer (Phase 6). This file records only what the engine side proves.

## 1. Model support

| Level | Field | Class |
|---|---|---|
| Tutorial | `isCompleted` | `Tutorial` |
| Chapter | `isCompleted` | `Chapter` |
| Section | `hasProgress` (lazy delegate) | `Section` |
| Track | — (no completion field) | `Track` |
| Lesson | — (completion lives in `Progress`) | `Lesson` |

`Section.hasProgress` being a **lazy delegate** rather than a stored boolean means section progress is *computed*
from its tutorials on access, while `Chapter.isCompleted` is a stored flag delivered by content.

## 2. Engine side

* `lessonSolvedCorrectly` (`base.c.V`) and `lessonSolvedAndProceedToNextLesson` (`base.c.U`) are the two exits from
  a solved lesson — one stays, one advances.
* `storeLessonProgressInMemory` (ambiguously `base.c.K`) shows the progress object is **kept in memory first**, then
  persisted elsewhere; the engine never writes storage directly.
* `markChapterCompletedInHardMode` (recovered in `data.local.a`, the DataStore preferences) proves chapter
  completion has a hard-mode-specific writer.

## 3. Consequence

Completion is a **three-layer property**: engine emits → in-memory `LessonProgress` → DataStore/Room. Phase 6 owns
the third layer; nothing in Phase 3 may claim a persisted completion.

## 4. Unknown

Whether finishing the last lesson of a chapter auto-completes the chapter, or only the hard-mode writer does, is
not established — question **A16**.
