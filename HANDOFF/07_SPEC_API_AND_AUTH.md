# 07 — SPEC: API surface and auth lifecycle (normative)

Sources: `data/endpoint_catalog.json`, `data/client_inventory.json`,
`mimo-re/mission-08/07_NETWORKING/`. `VERIFIED_STATIC`; per-row auth is `INFERRED_HIGH` (correction C-24).

## 1. Shape

62 endpoints / 29 interfaces / 6 HTTP client objects / 5 hosts.

| Client | Endpoints | Notes |
|---|---|---|
| `shared_retrofit` | 52 | the product's own API |
| `third_party_sdk` | 6 | vendor SDK traffic |
| `mimo_auth` | 1 | auth-specific Retrofit |
| `email_click` | 1 | tracking |
| `customerio` | 1 | messaging |
| `preview_long_timeout` | 1 | code preview, long timeout |

By category: account 5, completion 2, favorites 3, invitations 3, code_execution 4, content 2, content_preview 1,
analytics_proxy 2, iap 2, keys 2, certificates 1, gamification 1, email_tracking 1, ai_tutor 1.

## 2. Endpoints an offline engine actually needs

| Purpose | Endpoint |
|---|---|
| upload progress | completions POST (payload = 9-field `Progress` list, §05 §8) |
| read completion | `GET /v1/tracks/{id}/completion` |
| track catalogue revision | content endpoint (category `content`) |
| identity | Firebase token supply |

Everything else (coins, certificates, invitations, IAP, tutor, code execution) belongs to the online product and is
**out of scope** for `mimo/`; say so explicitly rather than faking it.

## 3. Interceptor chain (order verified)

```text
hg.e  →  fh.b  →  fh.a
```

* `hg.e` — auth: fetches the Firebase ID token for the request and adds the `Authorization` header **only when the
  endpoint's annotation requires it**;
* `fh.b`, `fh.a` — shared logging/header interceptors.

Because injection is annotation-driven, REST, SSE and WebSocket authenticate differently; the per-endpoint annotation
table was **not** recovered (`A-05`, `Q-63`). The 53 authenticated / 9 unauthenticated split is `INFERRED_HIGH`.

## 4. Token lifecycle

```text
FirebaseAuth.currentUser → getIdToken(forceRefresh?) → header "Authorization: Bearer <jwt>"
401 → refresh path exists; the exact retry/backoff is in 07_ERROR_RETRY_OFFLINE.md (PARTIAL)
```

No token, refresh token, or credential material is recoverable from the APK, and none is in this repo.

## 5. Error / retry / offline (PARTIAL)

Recovered: the retry predicate and the offline short-circuit exist in the networking layer; the concrete retry counts
and backoff constants were only partially read (`mission-08/07_NETWORKING/07_ERROR_RETRY_OFFLINE.md`).
→ Your engine: implement a documented `RetryPolicy` and mark it `DECIDED_IN_MIMO_BUILD`.

## 6. For an offline-first engine

`mimo/` needs **no auth at all** unless it ships a sync adapter. If it does, the contract is: bearer token from a
provider interface, injected per endpoint, 401 → refresh once → then surface an error. Never store tokens on disk
unencrypted; the reference design keeps them in memory only.

## 7. Acceptance

1. The endpoint table you implement is a documented subset with every row traceable to `data/endpoint_catalog.json`.
2. Unauthenticated endpoints carry no `Authorization` header (assert in tests).
3. A 401 triggers exactly one refresh attempt, then a typed error.
