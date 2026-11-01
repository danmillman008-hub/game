# Phase 2.5 — Content identity and versioning

## 1. Five-part lesson identity (verified)

```json
LessonIdentifier { trackId: J, trackVersion: J, tutorialId: J, chapterId: J, lessonId: J }
```
Source: `com.getmimo.data.content.model.track.LessonIdentifier` — five `private final long` fields, parsed from the
decompiled class. The "five-part identifier" recorded in earlier missions is therefore exact, and it is a
`Parcelable` (it travels through navigation arguments).

## 2. Progress identity is different — and that is now proven, not assumed

```json
Progress { trackId: Long, lessonId: J, publishSetVersion: Long, attempts: Int, tries: Int?,
           startedAt: Date, completedAt: Date, isPracticeProgress: Boolean }
```

* Progress keys on **`(trackId, lessonId)`**, not on the five parts.
* It carries **`publishSetVersion`**, not `trackVersion`.
* It contains **two counters**, `attempts` and `tries`, whose semantics differ (see Phase 4; the brief's warning
  applies exactly here — they must not be treated as synonyms until both are read).

## 3. Version numbers that actually exist

| Version | Where | Value observed |
|---|---|---|
| `publishSetVersion` | `TracksJson.publishSetVersion`, and `Progress.publishSetVersion` | **753** in `assets/lessons-en/tracks/tracks.json` |
| `Track.version` | `Track.version: long` | per track (e.g. tutorial 1001 has `version: 31`) |
| `Tutorial.version` | `tutorial.version` | 31 for tutorial 1001 |
| module/APK version | `BuildConfig` in each locale module stub | not read |

## 4. Layer separation (answer to "are identity, version and progress resolved in different layers?")

Yes, and the three use **three different keys**:

| Layer | Key | Consequence |
|---|---|---|
| content selection (JSON) | `trackId` + `tutorialId` + `chapterId` + `lessonId` + `trackVersion` | a lesson file is looked up by tutorial id: `<base>/tutorial-<id>.json` |
| in-memory model | `LessonIdentifier` (5 parts) | survives process death through `Parcelable` navigation args |
| persisted progress | `(trackId, lessonId)` + `publishSetVersion` | a publish-set bump can invalidate progress without changing lesson identity |

That last row is the important architectural fact: **progress is versioned by publish set, not by track version**,
so a track can change version while stored progress remains comparable, and a publish-set change silently shifts
the baseline for every stored progress row.

## 5. Unknowns

* whether `getPublishSetVersion` is compared against a stored value anywhere (would imply cache invalidation) — not
  found in Phase 2, listed as question **A11**;
* what `Track.version` is used for beyond display: no consumer was read in Phase 2;
* whether `tries` and `attempts` are both persisted (only the DTO field list is proven).
