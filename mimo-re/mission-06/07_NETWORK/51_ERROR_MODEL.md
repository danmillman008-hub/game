# Mission 6 — Error Model

## Scope
How failures are represented and surfaced.

## Method
Response envelope `d70.b<T>`, `NoConnectionException`, HTTP error bodies in the catalogue, Sentry
presence.

## Findings (VERIFIED_STATIC)
1. Every call returns `d70.b<T>` — success/failure envelope; failures carry a throwable.
2. `NoConnectionException` (from `hg.e`) is the only *domain* exception class recovered in the network
   layer.
3. Error bodies: the catalogue shows no dedicated error DTO; repositories map status codes/`Throwable`
   directly (**INFERRED_HIGH** from the absence of an error type).
4. Crash/error reporting is Sentry (native lib present, `io.sentry` classes in the DEX).
5. Retry: no retry interceptor and no exponential backoff found; a failed progress push is retried only by
   the next push cycle (Phase 6.43).

## Evidence labels
1, 2, 4, 5 **VERIFIED_STATIC**; 3 **INFERRED_HIGH**.

## Open questions
`Q-85` user-facing message mapping; `Q-86` HTTP 4xx handling per endpoint.

## Reproduction
`grep -rn 'NoConnectionException' /tmp/dad | head`
