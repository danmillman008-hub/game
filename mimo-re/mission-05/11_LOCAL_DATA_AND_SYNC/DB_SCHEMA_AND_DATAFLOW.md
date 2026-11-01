# Mission 5 — Local Database Schema and Data Flow

## Scope
The complete on-device relational store: tables, columns, keys, the generated SQL, how rows are
written and deleted, and which read paths build SQL dynamically. Also states what is *not* stored
locally (content, credentials, analytics).

## Method
Enumerated every `const-string` SQL literal in the decompiled app tree
(`evidence/ROOM_SQL_LITERALS.csv`), then read the Room database implementation, the generated DAO
writers (`cg.b`/`cg.c`), the repository and the two interactors that build dynamic queries.
Room's own annotations (`@Query`, `@Entity`) are **CLASS-retention** and therefore absent from the
DEX — the DDL must be reconstructed from generated SQL instead, which is what this document does.

## Sources
| Evidence | Symbol |
|---|---|
| Database impl | `com.getmimo.data.source.local.room.Database_Impl` |
| Generated INSERT/UPDATE | `cg.b`, `cg.c` |
| Repository | `com.getmimo.data.source.remote.progress.LessonProgressRepository` |
| Dynamic queries | `com.getmimo.interactors.path.d`, `ObservePathSwitcherState$invoke$$inlined$flatMapLatest$2` |
| SQL literals of record | `evidence/ROOM_SQL_LITERALS.csv` |

## Findings — schema (VERIFIED_STATIC)
```
lesson_progress(
  lesson_id            INTEGER/INT,  \
  completed_at         INTEGER,       | epoch millis (Joda Instant via Converters.fromInstant)
  started_at           INTEGER,       |
  tries                INTEGER,       | 0/1 correctness flag
  tutorial_id          INTEGER,       |
  tutorial_version     INTEGER,       |
  track_id             INTEGER,       |
  publish_set_version  INTEGER,       |
  attempts             INTEGER,       |
  is_practice_progress INTEGER,       |
  in_queue             INTEGER        |
  PRIMARY KEY (lesson_id, tutorial_id)
)

chapter_completions(chapter_id, created_at, track_id, tutorial_id)
  PRIMARY KEY (chapter_id, track_id)

tutorial_completions(tutorial_id, is_completed, updated_at, track_id)
  PRIMARY KEY (tutorial_id, track_id)
```
That is the **entire** relational store: three tables, registered in `Database_Impl` as
`new String[]{"chapter_completions", "tutorial_completions", "lesson_progress"}`.
`Database_Impl` registers **no migrations at all** (`new LinkedHashMap()` twice, i.e. empty
auto-migration and callback maps), so schema evolution in this build is destroy-and-recreate.

Generated statements (verbatim, from `cg.b`/`cg.c`):
```sql
INSERT INTO `lesson_progress` (`lesson_id`,`completed_at`,`started_at`,`tries`,`tutorial_id`,
  `tutorial_version`,`track_id`,`publish_set_version`,`attempts`,`is_practice_progress`,`in_queue`)
  VALUES (?,?,?,?,?,?,?,?,?,?,?)
UPDATE `lesson_progress` SET ... WHERE `lesson_id` = ? AND `tutorial_id` = ?
INSERT INTO `chapter_completions` (`chapter_id`,`created_at`,`track_id`,`tutorial_id`) VALUES (?,?,?,?)
INSERT INTO `tutorial_completions` (`tutorial_id`,`is_completed`,`updated_at`,`track_id`) VALUES (?,?,?,?)
```

## Findings — dynamic read paths (VERIFIED_STATIC)
Two places build SQL by concatenation instead of using generated statements:
```
SELECT * FROM chapter_completions  WHERE track_id = ? AND tutorial_id in (v0, v1, ...)   -- interactors/path/d
SELECT * FROM tutorial_completions WHERE track_id = ? AND tutorial_id in (...)           -- ObservePathSwitcherState
```
The IN-list is string-built from in-memory ids (not user input), so this is a performance smell, not
an injection surface. It is recorded because a reimplementation must reproduce the *result set*, not
the query text.

## Findings — data flow (VERIFIED_STATIC)
```
lesson submission ──► base.c.H(tries, attempts)
                   ──► LessonProgressRepository.createLessonProgress(...)   (12-arg ctor)
                   ──► INSERT/UPSERT lesson_progress (in_queue = 1)
                   ──► LessonProgressQueue.storeLessonProgress(..., post=true)
                   ──► POST /v1/tutorials/{tutorialId}/progress  { List<Progress> }
                   ──► on 2xx: moveLessonProgressFromQueue → DELETE FROM lesson_progress WHERE lesson_id IN (...)
                   ──► off-line: rows stay with in_queue = 1 and are re-posted in batches by postUnsyncedLessonProgress
```
Consequence: the device keeps progress **only until the server acknowledges it**. A local-only
"history" or "completed lessons archive" does not exist in this schema.

## Findings — what is *not* local
- Lesson content: shipped as JSON assets and cached by the content layer, not in Room.
- Auth tokens: not in this database (separate secure/preferences storage; not located this mission).
- Analytics events: not in Room (SDKs queue internally).
- AI tutor conversations: the repository is called `data.source.local.aitutor` but no Room table was
  found for it — conversation state is in memory only (**INFERRED_HIGH**, register `U-12`).

## Evidence labels
- Tables, columns, keys, SQL text, absence of migrations, delete-after-sync: **VERIFIED_STATIC**.
- Column affinities: **INFERRED_HIGH** (derived from Java field types; no DDL available).
- Runtime sync behaviour (timing, retries, backoff): **BLOCKED** — never observed executing.

## Limitations
No `CREATE TABLE` DDL exists in the decompiled set (creation is delegated to a base class DAD did not
emit), so NOT NULL/affinity defaults cannot be proven. Register `U-13`.

## Unresolved
`U-12` AI tutor persistence, `U-13` DDL/affinity, `U-14` whether `in_queue` is ever reset to 0.

## Reproduction
```bash
# every SQL literal that survives in the decompiled tree, with file+line:
python3 - <<'P'
import glob,re
pat=re.compile(r'"(CREATE TABLE[^"]*|SELECT [^"]*|INSERT INTO[^"]*|UPDATE `[^"]*|DELETE FROM [^"]*)"')
for p in glob.glob('/tmp/dad/**/*.java',recursive=True):
    for i,l in enumerate(open(p,errors='replace'),1):
        for m in pat.finditer(l): print(p,i,m.group(1)[:120])
P
# or use the committed extract: evidence/ROOM_SQL_LITERALS.csv
```
