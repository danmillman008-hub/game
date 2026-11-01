# 10 — Network clients and endpoint catalogue

## 1. Clients (6 objects)

| ID | Object | Case | Config | Consumers |
|---|---|---|---|---|
| C1 | OkHttp authenticated | 20 | `hg.e`→`fh.b`→`fh.a`; 20 s / 30 s; retryOnConnectionFailure=1 | C2, C4, C5, C6, C7, C8 |
| C2 | Retrofit shared | 19 | base `w` (case 22), kotlinx converter, client C1 | 52 endpoints / 25 interfaces |
| C3 | OkHttp long-timeout | 108 | `fh.b`+`fh.a` only; 10 s / 120 s | `eh.a` (1 endpoint) |
| C4 | Retrofit Customer.io | 53 | `https://track.customer.io` | `hg.d` |
| C5 | Retrofit mimo-auth | 87 | `https://mimoauth.getmimo.com/` | `hg.b` |
| C6 | Retrofit e-mail | 117 | `https://email.getmimo.com` | `ph.b` |
| C7 | AI tutor transport | 81 | C1 + host `w` + `ku.a`; manual header | SSE |
| C8 | Execution socket | 113 | C1 + `hb0.b` + `ku.a`; subprotocol | `wss://…/v1/run/socket` |

Absences: no `Authenticator`, no cache, no pinning, no logging interceptor, no DNS/proxy override, no compression
config, no per-host retry.

## 2. Endpoint totals

**62 endpoints / 29 interfaces / 5 hosts**; verbs GET 28, POST 24, PATCH 4, PUT 2, DELETE 4. Distribution by client:
shared Retrofit 52, third-party SDK 6, C4/C5/C6/C3 one each. Full table with request/response types, headers,
annotations and provenance: `07_NETWORKING/02_ENDPOINT_CATALOG.json` + `.md`.

## 3. Host selection

```text
case 22 → dev-menu preference (sk.a array index 2) → https://api-testing.mimo.org | https://api.mimo.org
```

Not `BuildConfig`, not a build flavour (`C-17`, `Q-76` closed).

## 4. Authentication per endpoint — the one honest gap

The mechanism is proven (annotation on the Retrofit method, checked at call time). The **per-row annotation table is
not recoverable here** (`A-01`/`A7`, `BLOCKED_BY_ENVIRONMENT`); mission-06 recorded the aggregate 53 authenticated / 9
not at scan time. Treat per-row auth as unknown and consult the server contract; absence of a token on a call is not
evidence the endpoint is public.

## 5. Error and retry

No HTTP retry, no backoff, no 401 handling, no idempotency key. Offline → `java.io.IOException` from `hg.e` (C1 paths)
or an OkHttp `IOException` on C3. The progress POST has its own repository-level guard (`NoConnectionException`).

## 6. Manual calls that bypass the interceptor

AI tutor SSE, certificate download, Pusher channel auth, execution socket. Each is a place where a change to `fh.a`
silently does not apply.

## 7. Server contract boundary

Client-proven: paths, verbs, DTO shapes, headers, the progress payload and the completion response fields. **Not**
proven: status-code semantics per endpoint, pagination, rate limits, deduplication, completion/unlock rules, ETA
formula, quota threshold. Those remain `BACKEND_ONLY` (5 questions).
