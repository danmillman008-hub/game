# Mission 6 — Dirty Tracking

## Scope
How the app knows a progress row still needs pushing.

## Method
`in_queue` flag usage; push repository flow; delete-after-2xx behaviour.

## Findings (VERIFIED_STATIC)
- Each row is born dirty: `in_queue = 1` is set at insert.
- The push flow selects `WHERE in_queue=1`, posts, and on success deletes those rows.
- There is **no separate dirty-set, generation counter, or retry counter**. A failing push leaves the row
  untouched, so it is retried on the next push trigger with no backoff and no timestamp change.
- Consequence: a permanently rejected row (e.g. 4xx) would be retried forever — no dead-letter path was
  recovered (`Q-69`).

## Evidence labels
**VERIFIED_STATIC**. The "forever retry" consequence is **INFERRED_HIGH**.

## Open questions
`Q-69` failure handling for 4xx; `Q-70` push trigger points (login, app foreground, lesson end).

## Reproduction
`grep -rn 'in_queue' /tmp/dad | head -20`
