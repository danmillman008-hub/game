# Phase 1 — Network client inventory

Method: each client is read from its **DI provider case body** (`mission-06/evidence/DI_GRAPH.json`, DAD pseudo-Java).
No client is inferred from imports or naming. The full machine-readable table is
`01_NETWORK_CLIENT_INVENTORY.json`.

## 1. `C1` — the authenticated OkHttp client (DI case 20)

```text
OkHttpClient.Builder
  .interceptors += hg.e(ri.d)      // connectivity gate
  .interceptors += fh.b()          // User-Agent
  .interceptors += fh.a(ku.a)      // Bearer authorization
  connectTimeout    = 20 s
  readTimeout       = 30 s
  retryOnConnectionFailure = 1
```

`hg.e` receives the provider `u` typed `ri.d`; `fh.a` receives the component method `b()` typed `ku.a`. There is no
`authenticator`, no cache, no certificate pinner, no logging interceptor in this body.

## 2. `C2` — the shared Retrofit (DI case 19)

```text
new Retrofit.Builder()
   .baseUrl(String provider w)          // case 22 -> api.mimo.org | api-testing.mimo.org
   .addConverterFactory(he0.a.c(jx.d))  // kotlinx.serialization
   .client(OkHttpClient provider v)     // = C1
   .build()
```

`v` is C1 by elimination: only two cases construct an `OkHttpClient` (20 and 108), and 108 builds it **inline**
without storing it, so the stored provider that every other case reads is case 20's result. `w` is case 22 by the
same argument (it is the only provider returning one of the two hosts).

## 3. `C3` — the long-timeout client (DI case 108)

```text
OkHttpClient.Builder
  .interceptors += fh.b()   // UA
  .interceptors += fh.a()   // Bearer
  connectTimeout = 10 s
  readTimeout    = 120 s
  retryOnConnectionFailure = 1
→ Retrofit(baseUrl w, converter e, client)
→ create(eh.a)
```

Distinguishing property: **no connectivity gate**. An offline device therefore fails at the socket layer for whatever
`eh.a` does, and the failure surfaces as an `IOException` from OkHttp rather than the app's own message.

## 4. `C4`–`C6` — single-host Retrofit instances

| Client | Case | Base URL literal | Client used | Service |
|---|---|---|---|---|
| C4 | 53 | `https://track.customer.io` | C1 | `hg.d` |
| C5 | 87 | `https://mimoauth.getmimo.com/` | C1 | `hg.b` |
| C6 | 117 | `https://email.getmimo.com` | C1 | `ph.b` |

Because all three reuse C1, they inherit the Bearer interceptor **conditionally** (only for annotated methods) and the
connectivity gate.

## 5. `C7` — AI tutor transport (case 81)

`com.getmimo.data.source.local.aitutor.a` is constructed with `(jx.d, OkHttpClient = C1, String = w, ku.a)`. It is
not a Retrofit client: it builds the streaming request itself and therefore carries a **manual** `Authorization`
header. Its constructor taking the token provider directly is the structural reason this path bypasses `fh.a`.

## 6. `C8` — execution socket (case 113)

`pg.a` receives `(OkHttpClient = C1, hb0.b, ku.a)` and wraps a WebSocket to `wss://api.mimo.org/v1/run/socket`,
authenticating through the **subprotocol** header rather than `Authorization`.

## 7. Negative findings (all VERIFIED_STATIC as absences in the recovered bodies)

No `okhttp3.Authenticator`, no HTTP-logging interceptor, no `CertificatePinner`, no `Cache`, no DNS override, no proxy
configuration, no per-host retry policy, no request-id or deduplication tag, no compression configuration.

## 8. Third-party clients (not app-owned, listed to avoid double counting)

Retrofit/OkHttp instances also exist inside Customer.io's in-app SDK (`io.customer.*`, its own host
`https://track.customer.io` API paths under `/api/…`), Pusher, Firebase, RevenueCat, Adjust, Sentry. Their 6 endpoints
are in the catalogue but are marked `third_party_sdk`; they are not part of the app's client graph.
