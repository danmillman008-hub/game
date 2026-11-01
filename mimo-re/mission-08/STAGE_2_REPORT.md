# Mission 8 — Stage 2 Report (content delivery)

**Status:** complete (12/12 deliverable files) · **Base:** Stage 1 commit `752add7` · **Date:** 2026-11-01

## Delivered

`02_CONTENT_DELIVERY/`: `CONTENT_ENTRY_POINTS.md`, `CONTENT_LOADING_CALL_GRAPH.json`,
`CONTENT_SOURCE_MATRIX.csv`, `CONTENT_MODEL_COMPLETE.json`, `CONTENT_IDENTITY_AND_VERSIONING.md`,
`DYNAMIC_MODULE_IMPLEMENTATION.md`, `DYNAMIC_MODULE_CONSUMER_GRAPH.json`, `CONTENT_CACHE_IMPLEMENTATION.md`,
`CONTENT_INVALIDATION_AND_RETRY.md`, `CONTENT_AVAILABILITY_STATE_MACHINE.json`, `CONTENT_TO_LESSON_HANDOFF.md`,
`CONTENT_PIPELINE_EVIDENCE.csv` (+ `evidence/CONTENT_CORPUS_STATS.json`).

## The pipeline, end to end

`ye.f` (provider) ← `ye.b` (assets, base `lessons-<locale>/tracks`, icons `lessons-common/icons`) | `ye.d`
(live preview, `/live_preview`) → `DefaultTrackLoader` (`tracks.b`: stream → String → JSON, holds the DSL parser
`te.c`) → `DefaultTracksRepository` (`tracks.c`: `TracksJson` + `HashMap`, `getTrackById`, `getTrackWithChapters`,
`loadTrackWithChapters`) → models → `LessonContent.Interactive(lessonModules)` → lesson engine.

## Numbers measured this stage

* **10,317** content JSON documents; **10 locales** at 1,030–1,032 each; `publishSetVersion **753**`; **19** tracks.
* Lesson identity is **five** longs (`trackId, trackVersion, tutorialId, chapterId, lessonId`); progress keys on
  **two** (`trackId, lessonId`) plus `publishSetVersion`, and carries **two distinct counters** (`attempts`, `tries`).
* Content is **bundled**, not fetched: no HTTP, no WorkManager, no content Room table, no runtime invalidation.

## Correction carried into the registers

**C-13** — the eight locale *code* modules are stubs, but all ten locale **content sets are present as assets**;
"non-English packs absent" is therefore wrong as stated and Q-05 is refined (see
`00_BASELINE/HISTORICAL_FINDINGS_RECONCILIATION.md`).

## Limits

Three seams remain `INFERRED` and are handed to Phase 3: the `te.c` call site, the base view-model's
`initialiseViewModel`, and the UI caller that first requests tracks. Four new questions: A11 (publish-set compare),
A12 (locale fallback), A13 (parse-error handling), A14 (what the four locales' extra two documents are).
