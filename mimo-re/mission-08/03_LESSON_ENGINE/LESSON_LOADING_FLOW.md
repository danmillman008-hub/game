# Phase 3.5 — Lesson loading flow

1. **Request.** A lesson is identified by `LessonIdentifier(trackId, trackVersion, tutorialId, chapterId, lessonId)`
   (`Parcelable`, so it survives navigation).
2. **Content acquisition.** `DefaultTracksRepository.getTrackWithChapters` / `getTutorial` → provider `ye.f` →
   `assets/lessons-<locale>/tracks/tutorial-<tutorialId>.json` (or the live-preview equivalent).
3. **Deserialisation.** `DefaultTrackLoader.c(InputStream)` → String → kotlinx JSON → `Tutorial`/`Chapter`/`Lesson`.
4. **Lesson extraction.** `DefaultTrackLoader.a(trackId, tutorialId, lessonId)` returns a `JsonObject` whose string
   pool names the three levels `tutorial`, `chapters`, `lessons` — i.e. the same method serves both interactive and
   executable retrieval (`getInteractiveLesson`/`getExecutableLesson` share `b.a`).
5. **Module parsing.** The `interactiveContent` string crosses into `te.c`, which delegates to the element parsers
   and produces `List<LessonModule>` inside `LessonContent.Interactive`.
6. **View-model initialisation.** `InteractiveLessonBaseViewModel.initialiseViewModel` (`base.c.e0`) receives the
   in-memory `LessonProgress` and restores prior state; `initialiseCodeBlocks` / `storeLessonProgressInMemory`
   (`base.c.K`) prepares the code panes; `createInteractiveAiTutorInfo` (`base.c.G`, 283 insns) builds AI-tutor
   context from the parsed modules.
7. **Render.** The fragment (`base.b`, `onViewCreated` → `b.K0`, MEDIUM) binds the module list to the Compose tree.

## Observable timing structure

`base.c.i0` (`updateTabbedCodeViewWithBrowserOutput`, 215 insns) contains the literal
**`browserOutputDeferred`**, which proves the engine treats browser output as a *deferred* value rather than a
synchronous return: code execution and rendering are decoupled. Phase 10 owns the actual scheduling.
