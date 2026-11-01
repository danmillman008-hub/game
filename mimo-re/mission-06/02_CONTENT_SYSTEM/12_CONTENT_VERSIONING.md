# Mission 6 — Content Versioning

## Scope
Version identity for content: pack version, track version, lesson identity, update detection and
compatibility behaviour.

## Method
Field extraction (`TracksJson`, `LessonIdentifier`), progress-model reads, API catalogue review.

## Sources
`evidence/CONTENT_MODEL_FIELDS.json`, mission-05 `09_PROGRESS_AND_GAMIFICATION/PROGRESS_MODEL.md`,
`evidence/API_CATALOG_V2.csv`.

## Findings (VERIFIED_STATIC)
1. **`publishSetVersion`** is a `long` carried by `TracksJson` and persisted into every progress row
   (`lesson_progress.publish_set_version`). It is captured at *write* time from the content layer, so a
   progress record states which content pack it was produced against.
2. **`trackVersion`** is part of `LessonIdentifier`; the same lesson id may exist at multiple track
   versions. Remote endpoints that return lesson content take `trackId` (and, for drafts/previews,
   `tutorialId`/`chapterId`/`lessonId`) in the path.
3. **Progress is version-agnostic**: the Room key is `(lesson_id, tutorial_id)` — no version component —
   while the *payload* records `publish_set_version` and `tutorial_version`. Consequence: re-completing
   a lesson in a newer pack **overwrites** the row rather than creating a second one.
4. **Update detection**: no local content-version comparison class was recovered; the app receives
   `publishSetVersion` with the pack and stores it. Whether a mismatch triggers a refresh is **UNKNOWN**
   (no code path found in the traced repositories).

## Evidence labels
Field-level statements: **VERIFIED_STATIC**. Update behaviour: **UNKNOWN** (explicitly not inferred).

## Limitations
The content repository that would compare local vs remote versions was **not recovered** as source
(obfuscated), so this document describes *data*, not *policy*.

## Open questions
`Q-21` update-detection policy; `Q-22` whether stale progress is discarded on pack change; `Q-23` how
`tutorial_version` is incremented (client or server).

## Reproduction
`python3 -c "import json;print(json.load(open('evidence/CONTENT_MODEL_FIELDS.json'))['com.getmimo.data.content.model.track.LessonIdentifier'])"`
