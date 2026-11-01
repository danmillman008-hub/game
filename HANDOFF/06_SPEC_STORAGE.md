# 06 — SPEC: storage (normative)

Sources: `data/room_schema.json`, `mimo-re/mission-08/06_PERSISTENCE/`. `VERIFIED_STATIC`.

## 1. Database identity

| Property | Value |
|---|---|
| file | `mimo.db` |
| version | **2** |
| tables | 3, **no indices**, **0 migrations** |
| identity hash | `2b8ab6d303d9a501bd8c8fb78d8352fc` |
| delegate | `leg/e` (also hosts a WorkManager database at version 24 — separate concern) |
| `clearAllTables` | `Database_Impl.d` — clears all three tables in one transaction |

## 2. Tables

```sql
CREATE TABLE lesson_progress (
  lesson_id INTEGER NOT NULL, tutorial_id INTEGER NOT NULL,
  tutorial_version INTEGER NOT NULL, track_id INTEGER NOT NULL,
  publish_set_version INTEGER NOT NULL, tries INTEGER NOT NULL,
  attempts INTEGER NOT NULL, started_at INTEGER NOT NULL, completed_at INTEGER NOT NULL,
  is_practice_progress INTEGER NOT NULL, in_queue INTEGER NOT NULL,
  PRIMARY KEY(lesson_id, tutorial_id));

CREATE TABLE tutorial_completions (
  tutorial_id INTEGER NOT NULL, track_id INTEGER NOT NULL,
  is_completed INTEGER NOT NULL, updated_at INTEGER NOT NULL,
  PRIMARY KEY(tutorial_id, track_id));

CREATE TABLE chapter_completions (
  chapter_id INTEGER NOT NULL, track_id INTEGER NOT NULL,
  tutorial_id INTEGER NOT NULL, created_at INTEGER NOT NULL,
  PRIMARY KEY(chapter_id, track_id));
```

Type mapping: `Instant` → INTEGER epoch, `boolean` → INTEGER 0/1, `long`/`int` → INTEGER.

## 3. DAO statement counts (evidence of completeness)

| DAO | Subject | Statements |
|---|---|---|
| `cg/a` | lesson progress | 4 |
| — | tutorial completions | 5 |
| — | chapter completions | 6 |

Total 15 — every one recovered as a statement string. Your schema must satisfy the same queries (see
`mission-08/06_PERSISTENCE/` for the statement texts).

## 4. What is **not** in the database

There is **no** table for users, credentials, lesson content, settings, analytics events, streaks or coins. Anything the
app shows about those comes from memory or the network. A Mimo clone that adds tables is diverging; record it.

## 5. Migration policy

Mimo has version 2 with **zero** migrations and no `Migration` object. Behaviour on an unexpected version is a
destructive `fallbackToDestructiveMigration`-style path (inferred from the absence of migrations; `INFERRED`).
→ `ADD-06` requires an explicit, non-destructive migration policy for your engine.

## 6. Storage acceptance

1. `PRAGMA user_version` = the version you declare.
2. `SELECT * FROM lesson_progress WHERE in_queue = 1` returns exactly the pending set.
3. Deleting posted ids leaves other rows untouched.
4. `clearAllTables` empties all three tables atomically.
