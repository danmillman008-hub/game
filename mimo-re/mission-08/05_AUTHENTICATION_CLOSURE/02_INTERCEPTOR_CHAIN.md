# Phase 5.2 — Interceptor chain and `Authorization` propagation

## 1. The central authorization interceptor: `fh.a`

```java
public final class fh.a implements okhttp3.Interceptor {
    public final ku.a a;                       // token provider
    public final Response intercept(Chain chain) {
        if (chain.request().headers("Authorization") == null) {           // 1
            Object tag = chain.request().tag(getOrCreateKotlinClass(ge0.s));  // 2
            if (tag != null && tag.getClass().getAnnotation(ri.b) != null) {   // 3
                request.newBuilder()
                       .header("Authorization", "Bearer ".concat(this.a.d(false)))  // 4
                       .build();
            }
        }
        … proceed …
    }
}
```

Instruction evidence (`evidence/DEX_auth_interceptors_and_repository.json`): `iface okhttp3.Interceptor`,
field `a: Lku/a;`, strings `"Authorization"`, `"Bearer "`, calls `Headers;->a(String)`,
`Tags;->a(v70/d)`, `Class;->getAnnotation`, `ku.a;->d(Z)String`.

Reading:

1. an existing `Authorization` header is **never overwritten** (idempotent interceptor),
2. the decision is made per **Retrofit service method**, via a tag carrying the method's Kotlin class,
3. the annotation `ri.b` is the `@RequiresAuthorization`-style marker: **only annotated endpoints get a token**,
4. the token is fetched with `forceRefresh = false` — the interceptor never forces a refresh.

### Correction of an intermediate mission-08 claim

Phase 2's data-flow note said headers are built "inside the request builders". That was derived from the three
manual `"Bearer "` sites and was **wrong as a general statement**: there *is* a central interceptor. Corrected in
`02_METHOD_RELATIONSHIPS/05_DATA_FLOW.md` (DF-01) and recorded as R-11 in
`00_BASELINE/HISTORICAL_FINDINGS_RECONCILIATION.md`.

## 2. The network-availability interceptor: `hg.e`

```java
public final class hg.e implements okhttp3.Interceptor {
    public final ri.d a;                        // network-state provider
    public final Response intercept(Chain chain) {
        if (((com.getmimo.network.a) this.a).b())               // is offline?
            throw new NoConnectionException("No network while trying to call " + url);
        return chain.proceed(chain.request());
    }
}
```

* `ri.d` is the **interface**; `com.getmimo.network.a` is the implementation (the cast is in the body).
* The exception type is `com.getmimo.network.NoConnectionException`, message
  `"No network while trying to call <url>"`.
* This confirms the Phase-1 mapping of the `ri.*` family: `ri.b` annotation, `ri.d` state-provider interface,
  `ri.a` platform callback, `ri.c` state value. (**Refinement of R-05**, not a new hypothesis.)

## 3. Manual header sites (bypass the interceptor)

Four app classes carry the `Authorization` literal themselves:

| Class | Why it bypasses the interceptor |
|---|---|
| `com.getmimo.data.source.local.aitutor.AiTutorRepository$sendMessage$2` | streaming (SSE) request built on a raw client, not a Retrofit interface method |
| `com.getmimo.data.source.remote.certificates.RemoteCertificateRepository$downloadCertificate$2` | certificate download (raw file response) |
| `com.getmimo.data.source.remote.pusher.a` | Pusher channel authentication call |
| `pg.a` (execution socket) | WebSocket handshake headers |

Each is a place where the token is used *outside* the annotation-driven path, and therefore a place where a future
change to `fh.a` would silently not apply.

## 4. Ordering inside the OkHttp chain

Mission-06 established the client construction (case 20 of the DI switch: timeouts 20 s / 30 s, interceptors
`hg.e`, `fh.b`, `fh.a`). Static evidence from that graph plus this phase gives the *set* of interceptors but not
their guaranteed order — OkHttp applies them in the order they were added, which was not read here. Therefore:

* **proven**: which interceptors exist and what each does,
* **not proven**: that `hg.e` (network guard) runs before `fh.a` (authorization), i.e. whether an offline request
  fails before or after a token fetch. This matters for the "blocking token fetch" hazard and is recorded as an
  open ordering question for Phase 11.

## 5. Evidence

* `05_AUTHENTICATION_CLOSURE/evidence/DEX_auth_interceptors_and_repository.json`
* `mission-06/evidence/DI_GRAPH.json` (OkHttp arm, case 20)
* `evidence/SCAN_AUTHORIZATION_HEADER.json` (33 classes contain an `Authorization` literal; only 4 are app classes,
  the rest are Adjust/Facebook/GMS/Mixpanel internals)
