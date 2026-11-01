# Stage 7 — Networking and Authentication (executive summary)

**Date:** 2026-11-01 · **Base:** Stage 6 `8049767` · **Output dir note:** the brief names `mimo-re/mission-8/`;
this mission's convention (and Rule 2) is `mimo-re/mission-08/`, so artifacts live in `mimo-re/mission-08/07_NETWORKING/`.

## Environment constraint (stated up front, because it bounds every claim)

The APK, the 12 DEX files and the decompiled sources are **not present in this environment** (the sandbox was rebuilt
between sessions; only committed artifacts survived). Host allow-listing (`github.com`, `pypi.org`, `npmjs.org`)
excludes every APK mirror, so the target cannot be re-acquired here. Consequently:

* **no new DEX instruction reads were performed in Stage 7**;
* every claim below is re-derived from **committed evidence** (mission-04…08) — primarily
  `mission-06/evidence/DI_GRAPH.json` (DAD pseudo-Java of 127 DI provider cases),
  `mission-08/05_AUTHENTICATION_CLOSURE/evidence/DEX_auth_interceptors_and_repository.json` (class dumps),
  `mission-05/evidence/API_CATALOG_V2.csv` (62 endpoint rows) and
  `mission-06/01_APK_AND_ARCHITECTURE/05_OBFUSCATION_MAP.json`;
* claims that need a fresh read (e.g. the per-endpoint `@ri.b` annotation list) are marked
  `BLOCKED_BY_ENVIRONMENT`, not guessed.

## What is established

| Question | Answer | Label |
|---|---|---|
| How many HTTP clients does the app own? | **6 client objects**: main authenticated client, shared Retrofit, long-timeout client, and three single-host Retrofit instances (Customer.io, mimo-auth, email) | VERIFIED_STATIC |
| Interceptor chain | `hg.e` (connectivity) → `fh.b` (User-Agent) → `fh.a` (Bearer) — **the order is now proven** by the `add(…)` sequence in case 20 | VERIFIED_STATIC |
| Base URL | `https://api.mimo.org`, switched to `https://api-testing.mimo.org` by a **dev-menu preference** (`sk.a.r[2]`), not by BuildConfig | VERIFIED_STATIC (Q-76 closed) |
| Endpoints | 62 across **29 interfaces**; 52 on the shared Retrofit, 6 in third-party SDKs, 4 pinned to their own hosts | VERIFIED_STATIC (verbs: 56 HIGH / 6 MEDIUM) |
| Authorization | method-annotation driven (`Method.getAnnotation`) in `fh.a`; token from `ku.a.d(false)`; **no refresh in the interceptor** | VERIFIED_STATIC |
| Token lifecycle | FirebaseAuth → cached token → JWT `exp` check → one forced refresh → `AccessTokenUnavailableException` on failure | VERIFIED_STATIC (phase 5) |
| Retry | none at HTTP level; only `retryOnConnectionFailure = true` (connection-level) | VERIFIED_STATIC |
| 401 handling | none — no `Authenticator`, no re-login path | VERIFIED_STATIC (negative) |
| Streaming | SSE (AI tutor, `okhttp3.sse`) and one raw WebSocket (`wss://api.mimo.org/v1/run/socket`, bearer **subprotocol**) | VERIFIED_STATIC |
| Offline | connectivity gate throws `IOException` before socket work; the Room outbox (Stage 5) is the queue | VERIFIED_STATIC |

## Corrections issued (details in `00_BASELINE/HISTORICAL_FINDINGS_RECONCILIATION.md`)

* **C-17** — the API host switch is a **dev-menu preference**, not a build flag (mission-06 Q-76 left this open).
* **C-18** — `fh.a` is **conditional** (`Method.getAnnotation`) and the token comes from `ku.a.d(Z)`, not `ri.b.d(0)`;
  mission-07's "every request carries the header" is refuted by the interceptor body.
* **C-19** — the offline gate's throw target is `java.io.IOException`, not the app's `NoConnectionException`.
* **C-20** — `d70.b` is `kotlin.coroutines.Continuation`; there is **no** app-level `Result` envelope
  (mission-06/07 stated the opposite in their own words while their own obfuscation map says Continuation).

## What this stage does not claim

No runtime traffic was generated, `api.mimo.org` was never contacted, and no server behaviour is asserted.
The endpoint↔auth assignment per row, the WebSocket frame schema and the SSE resume semantics stay open
(`12_OPEN_QUESTIONS.md`).
