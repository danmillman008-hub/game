# Mission 7 — Network Stack (complete)

## Construction (VERIFIED_STATIC)
`ae.m` case 20 builds `OkHttpClient` with `connectTimeout 20 s`, read/write `30 s`, interceptors in order:
1. `hg.e` — connectivity gate, throws `NoConnectionException` before any socket work;
2. `fh.b` — `User-Agent: Mimo/9.35 Android/<Build.VERSION.RELEASE> (<manufacturer/model/device>)`;
3. `fh.a` — `Authorization: Bearer <token>` (authenticated client only).

Retrofit interfaces (29) are built on top; every call returns `d70.b<T>` (success/failure envelope).
Serialization: kotlinx.serialization (`$$serializer` on models); no Gson/Moshi in the recovered paths.

## Not present (VERSIFIED negative)
No retry/backoff interceptor, no logging interceptor, no `CertificatePinner`, no cache configuration, no
`Authenticator` (401 handling), no refresh-token flow.

## Where requests originate
Repositories in `com.getmimo.data.source.remote.*` and `data.repository.*`; ViewModels never call Retrofit
directly in recovered code (exception: analytics singleton and WebSocket listener).
