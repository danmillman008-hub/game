# Phase 7 — Error, retry, offline, cancellation

## 1. Error paths that exist (each with the code that produces it)

| # | Path | Mechanism | Label |
|---|---|---|---|
| E1 | offline, client C1/C2/C4/C5/C6/C7/C8 | `hg.e` throws `java.io.IOException("No network while trying to call <url>")` before any socket work | VERIFIED_STATIC |
| E2 | offline, client **C3** (long-timeout) | no gate → OkHttp's own `UnknownHostException`/`ConnectException` (`IOException` subclasses) | VERIFIED_STATIC (by absence of the interceptor) |
| E3 | signed out | `ku.a.d` returns `null` → header `Authorization: Bearer null` → server rejects; no client-side guard | VERIFIED_STATIC (mechanism), consequence is server-side |
| E4 | token acquisition failure | `AccessTokenUnavailableException` thrown inside `ku.a.d`, then **wrapped into `java.io.IOException`** by `fh.a` | VERIFIED_STATIC |
| E5 | HTTP 4xx/5xx, direct-body endpoints | Retrofit suspend integration throws `HttpException`; nothing in the client catches it at the transport layer | INFERRED_HIGH (no catch in interceptors; repository bodies not exhaustively read) |
| E6 | HTTP 4xx/5xx, `Response<T>` endpoints | no exception — the call site must check `isSuccessful`; whether it does was not recovered | UNKNOWN (A-07) |
| E7 | repository-level offline fallback (progress) | `postUnsyncedLessonProgress` guards with `networkUtils.a()` and throws its own `NoConnectionException` **before** the request; rows survive in Room | VERIFIED_STATIC (Stage 5) |

E1 and E7 are two independent offline signals for the same action — the repository checks connectivity, and the
interceptor checks it again. Both can be true at once; neither is deduplicated.

## 2. Retry

| Layer | Policy | Evidence |
|---|---|---|
| connection | `retryOnConnectionFailure = 1` (OkHttp default, set explicitly) | DI cases 20 and 108 |
| HTTP request | **none** — no `RetryInterceptor`, no `maxRetries`, no backoff constants | absence in both case bodies + interceptor census |
| token | exactly one forced refresh inside `ku.a.d`, and only when `exp < now` | phase-5 dump |
| progress POST | no retry loop; retry is implicit (rows remain until a 2xx deletes them) | Stage 5 |
| SSE | none recovered (no `retry:` handling, no `Last-Event-ID`) | mission-07 69 |
| WebSocket | none recovered (no reconnect, no ping/pong handler) | mission-07 70 |

## 3. Timeouts

| Client | connect | read/write | Effect |
|---|---|---|---|
| C1 | 20 s | 30 s | every REST call |
| C3 | 10 s | 120 s | download-style call (`eh.a`) |
| C1 default call timeout | not set (0 = no overall deadline) | | a slow stream is bounded only by read timeout |

## 4. Duplicate-request protection

None. No idempotency key, no request id, no dedup tag, no `If-Match`, and OkHttp's `retryOnConnectionFailure` can
silently repeat a POST on a connection failure. For the progress flush this means the same `lesson_id` set may reach
the server twice if the first response never arrives.

## 5. Cancellation

* coroutine cancellation propagates to OkHttp through `Call.cancel` (Retrofit's suspend adapter installs a
  cancellation handler — library behaviour, not app code);
* the SSE `EventSource` is closed when its coroutine is cancelled, but **whether the server aborts generation** is not
  observable from the client;
* no app-level `Dispatcher` tuning (OkHttp default limits: 64 total, 5 per host), so a burst of progress POSTs for many
  tutorials runs at most 5 in parallel.

## 6. Offline behaviour, end to end

```text
lesson solved offline → grading runs (local) → row written (in_queue = 1)
chapter end offline   → move (1→0) → POST → E7 NoConnectionException → rows remain, still in_queue = 0
next app start        → POST (all rows, not only pending) → success → DELETE
```

The `in_queue` flag therefore distinguishes "not yet acknowledged" from "not yet attempted" only *before* the first
attempt; after a failed flush every row is in the same state (`in_queue = 0`, present). This is a refinement of Stage
5's model and is recorded there as the operational semantics.

## 7. Server error propagation

Nothing maps a status code to a user-visible message at the transport layer. Any such mapping lives in repositories/view
models; the only recovered example is the progress sync result (`reachedGoal`, `dailyGoalCoinReward`), which is a
**success** payload.

## 8. Local fallback

`tracks.json` in assets means lessons, chapters and tutorial structure render with the network down. Only completion
flags, ETA, leaderboards, coins, keys, rewards, AI tutor and code execution require network — i.e. the *content* is
offline-first, the *progression* is not.
