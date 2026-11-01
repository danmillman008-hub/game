# Spec 102 — Content System (independent, evidence-bound)

## MUST
1. Model four entity levels: Section, Chapter, Lesson, LessonContent; tutorials exist as ids/ranges only.
2. Key every lesson by `{trackId, trackVersion, tutorialId, chapterId, lessonId}`.
3. Carry a `publishSetVersion` on the pack and persist it on every progress record.
4. Support `ChapterType ∈ {NONE, QUIZ, PRACTICE_LEVEL_1..3, CHALLENGE_DIFFICULTY_0..4}`.
5. Support `LessonContentType ∈ {INTERACTIVE, EXECUTABLE_FILES}` and both payloads as in Spec 103/114.
6. Ship the English corpus in-app; deliver other locales as separate content packs.
7. Support `section.hasProgress` as a derived flag.

## MUST NOT
- Invent a `Track`/`Tutorial` field set (not recovered).
- Treat `ContentLocale`'s 5 constants as the locale inventory.
- Add a content cache table to the progress DB (no such table exists).

## GIVEN EVIDENCE
`02_CONTENT_SYSTEM/*`, `evidence/CONTENT_MODEL_FIELDS.json`.

## UNSPECIFIED — do not invent
Update-detection policy, ordering guarantees, chapter↔tutorial persistence on the wire.
