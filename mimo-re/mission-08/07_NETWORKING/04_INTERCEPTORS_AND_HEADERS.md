# Phase 4 — Interceptors, headers, propagation

## 1. The three interceptors (whole bodies)

| # | Class | Interface | Fields | Behaviour |
|---|---|---|---|---|
| 1 | `hg.e` | `okhttp3.Interceptor` | `ri.d a` | `if (com.getmimo.network.a.b()) throw new java.io.IOException("No network while trying to call " + url); else proceed` |
| 2 | `fh.b` | `okhttp3.Interceptor` | — | adds `User-Agent: Mimo/9.35 Android/<release> (<manufacturer>/<model>/<device>)` |
| 3 | `fh.a` | `okhttp3.Interceptor` | `ku.a a` | conditional `Authorization: Bearer <token>` (see §2) |

Order is proven by the `add` sequence in DI case 20 and by OkHttp's contract (application interceptors run in list
order). **This closes the ordering question left open in mission-08 phase 5** (was: "not proven whether the offline
gate runs before the token fetch"; now: it does).

## 2. `fh.a` in detail — the conditional, and why the older description was wrong

Instruction targets, in order (from `DEX_auth_interceptors_and_repository.json`):

```text
Headers.a("Authorization")                       // already set?
getOrCreateKotlinClass(...) → bc0.b.n(v70/d)     // KClass of the tag type
Tags.a(v70/d) → Class.cast(...)                  // pull the tag: a java.lang.reflect.Method
Method.getAnnotation(Class)                      // the per-endpoint marker
ku.a.d(Z) → String.concat(...)                   // token, then "Bearer " + token
Request.b() → Request.Builder.a(String,String)   // header(...)
RealInterceptorChain.b(Request)                  // proceed (two call sites: success + catch)
new java.io.IOException(Throwable)               // wraps interceptor exceptions
```

Mission-07 recorded "`fh.a` has no path check, so **every** request on the client carries the header". That is
contradicted by the `getAnnotation` branch (a `null` annotation skips the header). The corrected statement is:
*the header is added iff the invoked Retrofit method carries the marker annotation, and iff no Authorization header is
already present.*

Two more consequences of the same body:

* the interceptor **cannot** add the header to a request that did not come from Retrofit (no `Method` tag) — which is
  exactly why the AI tutor, certificate download, Pusher call and WebSocket each carry their own header;
* the interceptor wraps thrown exceptions into `IOException`, so even a `RuntimeException` from the token provider
  surfaces to the caller as an `IOException` (the app's `AccessTokenUnavailableException` path is preserved only
  through `cause`).

## 3. Header inventory

| Header | Where | Value source | Notes |
|---|---|---|---|
| `Authorization` | `fh.a` (conditional), 4 manual sites | `ku.a.d(false)` | manual sites: `AiTutorRepository$sendMessage$2`, `RemoteCertificateRepository$downloadCertificate$2`, `remote.pusher.a`, `pg.a` (via subprotocol) |
| `User-Agent` | `fh.b` | `Mimo/9.35 Android/…` | only on C1 and C3 |
| `Content-Type` | Retrofit `@Body` (47 rows `application/json`, 1 `application/zip`) | per endpoint | from the catalogue |
| `Accept: text/event-stream` | AI tutor request | literal | SSE only |
| `Sec-WebSocket-Protocol` | `pg.a` | `authorization.bearer.<token>` | WebSocket auth channel |
| static per-endpoint headers | catalogue column `static_headers` | — | 14 rows have none |

## 4. What is absent

No `okhttp3.Authenticator`, no 401 interceptor, no token-refresh-on-401, no request signing, no HMAC, no `Cookie`
handling, no `X-Request-Id`, no client version header beyond `User-Agent`, no idempotency key. Given that the progress
POST has no idempotency key (Stage 5), a retried POST depends entirely on server-side deduplication — which is outside
client evidence.
