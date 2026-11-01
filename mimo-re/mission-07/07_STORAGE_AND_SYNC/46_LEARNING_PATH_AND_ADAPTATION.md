# Mission 7 — Learning Path and Adaptation

## Path model (VERIFIED_STATIC)
```
Track (19 in English corpus) → Section (index-ordered) → Tutorial(ids) → Chapter{type} → Lessons
```
Ordering is **authored**: `Section.index`, `SectionJson.startIndex/endIndex`, and chapter order inside the
tutorial. No client-side reordering, no recommendation engine, no personalised selection.

## Adaptation mechanisms that exist
| Mechanism | Where | Who decides |
|---|---|---|
| chapter kind | `ChapterType{QUIZ, PRACTICE_LEVEL_1..3, CHALLENGE_DIFFICULTY_0..4}` | author |
| hard mode | `Lesson.hardModeSelected` + `hardModeLessonModules` | learner |
| daily goal / pace | `PostProgressResponse.reachedGoal`, `TrackEtaResponse.currentPaceMinutesPerDay` | server |
| AB-test user groups | `com.getmimo.analytics.a` (Remote Config) | server, feature-level |

## Adaptation mechanisms that do **not** exist
Spaced repetition, skill mastery, difficulty adjustment from performance, AI-generated content selection,
review scheduling. (Negative evidence: no fields/tables/algorithms; `qm.*` never reads history.)

## Verdict
Progression is **fixed-sequence with authored difficulty tiers and server-side pacing**, not adaptive learning.
