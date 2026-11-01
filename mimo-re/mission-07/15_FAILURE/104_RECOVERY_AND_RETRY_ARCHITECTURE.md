# Mission 7 — Recovery and Retry Architecture

## What the app retries
| Layer | Retry | Notes |
|---|---|---|
| HTTP | **no** | no retry interceptor, no backoff; user action required |
| outbox push | **implicit** | row remains `in_queue=1`; no counter, no backoff, no dead-letter |
| SSE | no | stream failure ends the message |
| WebSocket | no app-level reconnect | Pusher has SDK reconnect, the run socket does not |
| analytics | SDK | Firebase/Adjust buffer |
| remote config | next launch | log-and-continue |

## Design assessment (INFERRED)
The architecture assumes a **mostly-online, user-driven client**: nothing is scheduled, nothing is retried
automatically, and the only durable queue is the progress outbox. Recovery is therefore "open the app again".

## Where this bites
1. A rejected progress push is retried forever (no dead-letter).
2. A killed process loses in-progress lesson state (only the initial row survives).
3. No entitlement cache ⇒ offline premium checks are unreliable.
4. No content-cache integrity ⇒ a truncated pack fails at parse time with no fallback.

## Verification status
Static only. Every failure row in `103_FAILURE_HANDLING_MATRIX.csv` carries a label; nothing is runtime-observed.
