# Mission 7 — Conflict and Retry Rules

## Conflict
| Case | Behaviour | Evidence |
|---|---|---|
| two devices, same lesson | two independent assertions; server merges invisibly | no client merge code |
| local newer than server | no comparison exists | no `updated_at` usage on read |
| server newer than local | local rows are not reconciled | no GET of per-lesson rows |
| duplicate insert for same key | upsert (REPLACE) | repository insert |

## Retry
- HTTP: no retry interceptor, no backoff (only the connectivity gate `hg.e`).
- Outbox: implicit retry on next push cycle; a permanently rejected row is retried forever (no dead-letter).
- SSE/WebSocket: no automatic reconnect recovered for the tutor; Pusher owns its own reconnect logic.

## Verdict
The sync design is **assert-only with server-side deduplication responsibilities**. The client cannot detect or
resolve divergence, which is a deliberate simplification given that completion is monotonic.
