# 04 — Content and track delivery

## 1. Corpus (from the shipped APK)

| Property | Value |
|---|---|
| Content root | `assets/lessons-<locale>/` |
| Locale packs | **10** (`en` base + `ru`, `pt`, `fr`, `es`, `id`, `it`, `pl`, `tr`, one more) |
| Documents | **10,317** JSON (1,030 per pack; `id`, `it`, `pl`, `tr` carry 1,032) |
| Tracks | **19** |
| Tutorials | **1,029** |
| Chapters | **1,947** |
| Lessons | **18,272** |
| Publish-set version | **753** (`tracks.json`) |
| Delivery | APK assets — **no network content download** |

## 2. Hierarchy and identity

```text
TracksJson { publishSetVersion: Long, tracks: [Track] }
  Track   { id, version, name, sections[] , … }
    Section { index, name, description, hasProgress(lazy), tutorials[] }
      Tutorial { id, version, type(course|practice …), chapters[] }
        Chapter { id, type, lessons[] }
          Lesson { id, contentType: interactive|executableFiles, interactiveContent | executableContent }
LessonIdentifier = (trackId, trackVersion, tutorialId, chapterId, lessonId)   // five-part, navigation only
```

Field sets: `mission-06/evidence/CONTENT_MODEL_FIELDS.json`;
schema: `mission-08/02_CONTENT_DELIVERY/CONTENT_MODEL_COMPLETE.json`.
Note the split identities: the five-part `LessonIdentifier` is never persisted; the Room row keys on
`(lesson_id, tutorial_id)` only (Stage 5, C-16).

## 3. Load path

```text
lesson navigation → ContentRepository (ye.g/ye.b) → asset path "lessons-<locale>/tracks/tutorial-<id>.json"
→ kotlinx deserialisation → Track/Tutorial model → parser dispatch (te.c) → renderer → custom elements
```

`ye.b` derives the pack from `"lessons-" + locale`; no fallback branch to `en` was observed (A12).

## 4. Versioning

`publishSetVersion` is (a) read from `tracks.json`, (b) copied into every `LessonProgress` row as
`publish_set_version`, (c) sent in the progress POST. **Nothing compares it** with a stored value anywhere (A11
closed negative). A content update therefore never invalidates local progress or the completion cache.

## 5. Localisation

Ten packs ship in the APK while the `ContentLocale` enum has five values — the enum is a subset, not the inventory
(Q-14 closed). Dynamic feature modules for locales are **stubs** in the DEX (1,096-byte `BuildConfig`/`R` classes), yet
their assets are present, so the stub does not prevent content from loading (Q-05 stays blocked only for the module
*code*, not for the content).

## 6. Caching and invalidation

No content cache in Room, no ETag/If-None-Match logic, no download manager. The only content-adjacent network calls are
`GET /v1/tracks/{id}/eta` and the `eh.a` long-timeout service (A-03 open). Practically: content is immutable for the
life of the install.

## 7. Feeding new content into an independent engine (informational)

The engine-facing contract is the three JSON shapes above plus the DSL grammar of `te.a`–`te.g`. A replacement corpus
must supply: `tracks.json` with a version, per-tutorial documents with chapter/lesson arrays, and lesson bodies in the
tag grammar. Nothing in the client hard-codes Mimo lesson text; localisation is directory-based, so additional locales
require only a new `lessons-<locale>` tree.
