# Mission 7 — Content Identity and Versioning

## Three identity systems
| System | Shape | Versioned? | Evidence |
|---|---|---|---|
| lesson identity | `LessonIdentifier{trackId,trackVersion,tutorialId,chapterId,lessonId}` | **yes** (trackVersion inside the key) | field extraction |
| progress identity | Room key `(lesson_id,tutorial_id)` + columns `publish_set_version`, `tutorial_version` | **no** (stored, not keyed) | entity + SQL |
| pack identity | `TracksJson.publishSetVersion` (single long) | per pack | field extraction |

## Resolved relationships
- A lesson is addressed with its track version but stored without it → **one row per lesson per tutorial,
  regardless of version** (VERIFIED_STATIC from schema).
- `solvedContent` lives in the lesson payload, so it versions with the pack.
- Locale is not part of any identity: the same `LessonIdentifier` resolves to different documents per module.

## Still unresolved
`Q-21` (update detection), `Q-22` (stale pack handling), `Q-23` (who increments `trackVersion`) — no comparison
or increment code exists in the inspected subset.
