# Phase 3.11 — Lesson navigation

## Proven

* `LessonIdentifier` is `Parcelable` and carries all five ids → navigation arguments can identify a lesson without a
  lookup by position.
* `lessonSolvedAndProceedToNextLesson` (`base.c.U`, 130 insns) is the "advance" exit; `lessonSolvedCorrectly`
  (`base.c.V`) is the "stay/confirm" exit.
* `lesson_reset` (`base.c.a0`, 104 insns) resets the current lesson in place.
* `DefaultTracksRepository.getTrackWithChapters` (86 insns) and `loadTrackWithChapters` (409 insns) are what a
  navigation target needs in order to show the next lesson inside its chapter context.

## Not proven (handed to Phase 11)

* which navigation route/composable consumes `LessonIdentifier` (Compose route strings were not traced here);
* deep-link handling for lessons;
* back-stack behaviour after `lessonSolvedAndProceedToNextLesson` when the next lesson is in a different chapter.

These are UI-layer facts and belong to the navigation phase; stating them now would be inference from names.
