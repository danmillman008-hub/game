# Mission 6 — DAOs and Queries

## Scope
Which operations exist against the three tables.

## Method
`ROOM_SQL_LITERALS.csv` (mission-05) + repository call sites.

## Findings
| DAO | Operation | Query shape |
|---|---|---|
| lesson progress | insert/upsert | full row, `in_queue=1` |
| lesson progress | read by lesson | `WHERE lesson_id=? AND tutorial_id=?` |
| lesson progress | read pending | `WHERE in_queue=1` |
| lesson progress | delete after push | `WHERE …` (per row or per batch, `Q-54`) |
| chapter completions | insert | marker row |
| tutorial completions | insert | marker row |

No update-in-place of counters was found: the repository **inserts a new row** (upsert semantics) rather
than updating, which is why the table key matters more than the write path.

## Evidence labels
Query shapes: **VERIFIED_STATIC** for the literals; the mapping of each literal to a DAO method:
**INFERRED_HIGH** (literal ↔ method binding verified only where the annotation could be matched).

## Open questions
`Q-54`, `Q-66` conflict policy on duplicate insert (REPLACE vs IGNORE).

## Reproduction
`head -20 ../mission-05/evidence/ROOM_SQL_LITERALS.csv`
