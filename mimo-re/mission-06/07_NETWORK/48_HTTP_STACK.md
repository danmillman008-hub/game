# Mission 6 — HTTP Stack

## Scope
Client library, configuration, interceptors and timeouts.

## Method
Read of `ae.m` case 20 (OkHttp builder) and the interceptor classes `fh.a`, `fh.b`, `hg.e`.

## Findings (VERIFIED_STATIC)
```
OkHttpClient.Builder
  .connectTimeout(20s)  .readTimeout/…(30s)
  .addInterceptor(hg.e)   // connectivity gate → NoConnectionException
  .addInterceptor(fh.b)   // User-Agent: "Mimo/9.35 Android/<Build.VERSION.RELEASE> (<manufacturer/model/…>)"
  .addInterceptor(fh.a)   // Authorization: "Bearer " + tokenStore.d(0)   (only for the auth retrofit)
```
- Retrofit sits on top (interfaces annotated with `@GET/@POST/@PATCH/@PUT/@DELETE`); responses are wrapped
  in `d70.b<T>` (a `Result`-like envelope with success/failure + error).
- SSE is `okhttp3.sse.RealEventSource` (Phase 8); WebSocket is `okhttp3.WebSocket` with a bearer
  subprotocol (Phase 3.23).
- Marshalling: kotlinx.serialization (models carry `$$serializer`), Moshi/Moshi-like adapters present for
  a few legacy DTOs.

## Evidence labels
**VERIFIED_STATIC**. The claim that *only* the auth client gets the Bearer interceptor is
**INFERRED_HIGH** (the two clients are built separately and only one is fed `fh.a`).

## Open questions
`Q-78` write timeout value; `Q-79` whether a logging interceptor exists in release builds (none found).

## Reproduction
`sed -n '1,120p' /tmp/dad/ae.m.java | grep -n 'Interceptor\|Timeout'`
