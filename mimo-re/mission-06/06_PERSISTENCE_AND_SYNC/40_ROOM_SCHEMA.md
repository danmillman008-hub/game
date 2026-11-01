# Mission 6 — Room Schema

## Scope
The complete local persistence schema, as compiled into the APK.

## Method
Entity classes (`com.getmimo.data.model.room.*`), DAO annotations, and the `CREATE TABLE` literals
recovered earlier (mission-05); re-verified here against field extraction.

## Findings (VERIFIED_STATIC)
Three tables only:

| Table | Purpose |
|---|---|
| `lesson_progress` | one row per (lesson_id, tutorial_id) — counters and queue flag (11 columns) |
| `chapter_completions` | chapter completion marker |
| `tutorial_completions` | tutorial completion marker |

No content, user, coin, streak or session table exists. **The database is an outbox + completion cache,
not an app state store.** There are no migrations registered (no `Migration` subclasses), so the schema is
recreated on version change — consistent with data being re-pushable.

## Findings — versioning
`@Database(version=…)` was recoverable only via the annotation table (`ANNOTATIONS_V2.csv.gz`), which
records the Room database class; a destructive-recreate strategy is **INFERRED** from the absence of
migrations combined with the outbox design.

## Evidence labels
Table list, columns of `lesson_progress`: **VERIFIED_STATIC**. Migration strategy: **INFERRED_HIGH**.

## Open questions
`Q-64` exact database version; `Q-65` whether `chapter_completions`/`tutorial_completions` are queued too.

## Reproduction
`grep -n 'CREATE TABLE' ../mission-05/evidence/ROOM_SQL_LITERALS.csv`
