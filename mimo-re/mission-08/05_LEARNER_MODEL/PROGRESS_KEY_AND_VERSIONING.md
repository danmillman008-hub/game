# Phase 5D — Progress keys, identity and versioning

## 1. Four identities exist, and they are not interchangeable

| Identity | Shape | Used for | Evidence |
|---|---|---|---|
| `LessonIdentifier` | **5** longs: `trackId, trackVersion, tutorialId, chapterId, lessonId` | navigation payload (`Parcelable`) | field table of `model.track.LessonIdentifier` |
| `LessonProgress` row | **2** key columns: `(lesson_id, tutorial_id)` + payload | persistence, sync | `PRIMARY KEY(lesson_id, tutorial_id)` in the schema; `WHERE lesson_id = ? AND tutorial_id = ?` in the UPDATE |
| `TutorialCompletion` row | `(tutorial_id, track_id)` | completion cache | schema PK |
| `ChapterCompletion` row | `(chapter_id, track_id)` | completion cache | schema PK |

The five-part identifier never reaches the database. `chapterId` in particular is **not** part of the lesson's row —
a lesson does not record which chapter it belonged to, so a chapter reorganisation in a content update cannot be
reconciled locally.

## 2. Lookup keys

* lesson progress is looked up by `(lesson_id, tutorial_id)` (the UPDATE's WHERE clause proves both columns are used);
* tutorial completion by `(tutorial_id, track_id)`;
* chapter completion by `(chapter_id, track_id)`;
* completion attachment queries filter **by `track_id` only** (`SELECT * FROM tutorial_completions WHERE track_id = ?`).

## 3. Version fields

| Version | Where it lives | What reads it |
|---|---|---|
| `trackVersion` | `LessonIdentifier`, `Track.version`, `TrackJson.version` | passed to `CompletionApi.getTrackCompletion(trackId, trackVersion)`; stored per row as `tutorial_version` (different field, per tutorial) |
| `tutorialVersion` | `LessonProgress.tutorial_version` | POST body (`Progress.tutorialVersion`) |
| `publishSetVersion` | `LessonProgress.publish_set_version`, `TracksJson.publishSetVersion` (753), `Progress.publishSetVersion` | POST body; written at creation from `getPublishSetVersion()` |

**No comparison code exists.** No branch anywhere reads a stored `publishSetVersion` and compares it with the current
bundle's value; no migration, no invalidation, no "outdated progress" path. A publish-set bump therefore does **not**
rewrite, drop or invalidate local rows — the client keeps sending whatever value it wrote, alongside the new value
for new rows. This confirms Phase 2's open question **A11** in the negative: there is no comparison site.

## 4. Account identity

None of the three tables has a user/account column, and the DTO `Progress` carries no user field either. Progress is
therefore **device-local and not partitioned by account**: two accounts on the same install would share rows until
the server merges them. The account only participates through the authentication header on the POST (Phase 7), not
through the key. Recorded as question **B-2** because it may be intentional (single-account install) or a defect.

## 5. Version compatibility, as implemented

| Question | Answer from code |
|---|---|
| what happens to progress when a track's version changes? | nothing local; `tutorial_version` on the row is whatever was current at creation |
| what happens when the publish set changes? | nothing local; older rows keep their `publish_set_version` |
| is stale progress discarded? | never — no DELETE outside the sync outbox and `in_queue = 1` |
| is completion re-fetched on version change? | only when `fetchTrackCompletion` is called (favourite-track sync, chapter end); it passes the *current* `trackVersion` |

## 6. Summary

```text
navigation  → 5-part LessonIdentifier (never persisted)
grading     → view-model ints (tries, attempts) → LessonProgress
persistence → 2-part (lesson_id, tutorial_id) + versions as payload
sync        → per-tutorialId grouping of the same rows
completion  → server-derived, keyed (tutorial_id, track_id) / (chapter_id, track_id)
```
