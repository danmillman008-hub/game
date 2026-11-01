# Mission 6 — Conflict Resolution

## Scope
What happens when local and server disagree about progress (two devices, reinstall, pack change).

## Method
Search for merge/last-write-wins/timestamp comparison in the progress repositories; read of the push
response handling.

## Findings
1. **No conflict resolution exists.** The client never downloads raw progress rows; it posts rows and
   deletes them. There is no `GET` that returns per-lesson rows in the recovered catalogue
   (`TrackCompletionResponse` returns *tutorial list + lastInteractedTutorialId*, not counters).
2. Therefore the effective policy is **server-accumulates, client-asserts**: the client's post is an
   assertion, and what the server does with duplicates is invisible to the client (**UNKNOWN**).
3. On a second device, the same lesson produces a second assertion; whether that re-awards coins is
   server-side (`Q-72`).
4. Pack version changes do not trigger any local reconciliation (Phase 2.12).

## Evidence labels
1–2 **VERIFIED_STATIC / INFERRED** as marked; 3–4 **UNKNOWN**.

## Open questions
`Q-49`, `Q-72`, `Q-73` whether the server deduplicates by `(lesson_id, tutorial_id)` or timestamp.

## Reproduction
`grep -c GET ../mission-05/evidence/API_CATALOG_V2.csv`
