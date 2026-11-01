# Mission 6 — Correctness Model

## Scope
What "correct" means for each interaction and how correctness aggregates upward to a lesson, chapter,
tutorial and track.

## Method
Verdict visitor + progress writers + completion endpoints.

## Sources
`qm.d/e/f/g`, `LessonProgress` schema, `evidence/API_CATALOG_V2.csv`.

## Findings
```
interaction   → verdict ∈ {CORRECT, CORRECT_NORMALISED, INCORRECT}
exercise      → solved if verdict ∈ {CORRECT, CORRECT_NORMALISED}      (base.c U())
lesson        → tries ∈ {0,1}; attempts = submissions; completed when the learner proceeds
chapter       → isCompleted (boolean on Chapter) + chapter_completions row
tutorial      → tutorial_completions row; POST /v1/tutorials/{tutorialId}/progress
track         → /v1/tracks/{trackId}/completion; /v1/tracks/{trackId}/eta for remaining time
```
- **First-try correctness** is `solved && attempts == 1` — derived, not stored (`LessonProgress` has no
  first-try column).
- A learner who is wrong once and proceeds still produces a completed lesson with `tries=0`; the system
  therefore separates *completion* from *correctness* everywhere.
- No score/threshold exists: there is no "pass mark" and no partial credit at any level.

## Evidence labels
**VERIFIED_STATIC** for all five levels' representations. Server-side aggregation rules: **UNKNOWN**
(client only sends rows).

## Open questions
`Q-49` whether the server recomputes chapter completion from lesson rows; `Q-50` `eta` formula.

## Reproduction
`grep -n 'createLessonProgress\|completion' -r /tmp/dad/com.getmimo.data.model.progress.*.java | head`
