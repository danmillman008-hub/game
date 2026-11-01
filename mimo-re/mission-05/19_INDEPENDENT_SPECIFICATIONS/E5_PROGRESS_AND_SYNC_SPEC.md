# E5 — Progress and Sync Specification (independent)

## Scope
Normative behaviour for recording lesson progress locally, deciding what to transmit, and keeping the
local store and the server consistent.

## Method
Reduced from `09_PROGRESS_AND_GAMIFICATION/PROGRESS_MODEL.md` and
`11_LOCAL_DATA_AND_SYNC/DB_SCHEMA_AND_DATAFLOW.md`.

## Sources
`09_PROGRESS_AND_GAMIFICATION/PROGRESS_MODEL.md`, `11_LOCAL_DATA_AND_SYNC/DB_SCHEMA_AND_DATAFLOW.md`,
`evidence/ROOM_SQL_LITERALS.csv`, `evidence/API_CATALOG_V2.csv`.

## Findings (normative requirements)
- **E5-R-1** A progress record is keyed by `(lessonId, tutorialId)`; a second completion of the same
  lesson in the same tutorial replaces the record (upsert), it does not append.
- **E5-R-2** A record carries: start time, completion time, `tries` (0/1 flag), `attempts`, tutorial
  version, track id, content-pack version, practice flag, and a queued flag.
- **E5-R-3** Opening a lesson without submitting writes a record with `tries = 0, attempts = 0`
  (an "attempted" marker).
- **E5-R-4** The content-pack version is captured at write time from the content layer, not from the
  lesson payload.
- **E5-R-5** Records are written with the queued flag set, then transmitted as a **batch** (list) to the
  progress endpoint; on a successful response the transmitted records are deleted locally in a single
  batched delete.
- **E5-R-6** If transmission fails, records stay queued and are retried in batches later; the local
  store is therefore a *transmit buffer*, not an archive.
- **E5-R-7** Derived values (`solved`, `first-try`) are computed from `tries`/`attempts`, never stored
  twice.
- **E5-R-8** Chapter and tutorial completion are separate tables keyed by
  `(chapterId, trackId)` and `(tutorialId, trackId)`; they are not derived from lesson rows.

## Evidence labels
E5-R-1…R-8: **VERIFIED_STATIC** (schema + generated SQL + queue code).
E5-R-6 (retry cadence) is **INFERRED_HIGH**: the retry *mechanism* is verified, the schedule is not.

## Limitations
Column affinities and NULL constraints cannot be stated (no DDL recovered). Server-side recomputation
of `tries`/`attempts` is **UNKNOWN**.

## Unresolved
`U-11` multi-device conflict policy, `U-14` whether the queued flag is ever cleared without deletion.

## Reproduction
Recreate the schema from E5-R-1/R-2, feed the generated INSERT/UPDATE from
`evidence/ROOM_SQL_LITERALS.csv`, and verify a two-directional round trip of one record.
