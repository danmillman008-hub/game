# Phase 5.6 — Storage map (no token values) and remaining unknowns

## 1. Where authentication-related state can be written

| Store | Content | Evidence | Sensitivity handling |
|---|---|---|---|
| **Firebase Authentication SDK storage** | refresh token, user record | no app class writes a token; `ku.a` reads `FirebaseAuth.currentUser` and calls `getAccessToken` | library-owned; format not inspected |
| `androidx.datastore` (Preferences/Proto) | app preferences produced by app classes | `com.getmimo.data.firebase.a` builds a `DataStore`; the literal scan finds 40 classes with DataStore/EncryptedSharedPreferences strings, all library except that one | no secret reading attempted |
| `SharedPreferences` | — | no app class was observed writing a token literal near `SharedPreferences` | — |
| **WorkManager input Data** | `ARGS_ACCESS_TOKEN` | `com.getmimo.data.source.remote.account.a.c()` | value never read; only the key is recorded |
| Room | learner/progress tables (mission-5/6) | mission-06 evidence | not auth |

**No credential value was read at any point.** The mission records only keys, types and transport shapes.

## 2. Header propagation map

```
Retrofit call to an @ri.b-annotated method
    └── OkHttp chain
          ├── hg.e  (network guard)            → NoConnectionException("No network while trying to call <url>")
          ├── fh.b  (mission-06 arm; not read here)
          └── fh.a  (authorization)
                 └── if no Authorization header and method annotated @ri.b
                        → "Bearer " + ku.a.d(false)
Manual sites (no annotation path):
    AiTutorRepository$sendMessage$2        (SSE)
    RemoteCertificateRepository$downloadCertificate$2
    data.source.remote.pusher.a            (Pusher auth)
    pg.a                                   (WebSocket handshake)
```

## 3. Open questions this phase leaves (with what would close them)

| # | Question | Current status | What closes it |
|---|---|---|---|
| A1 | Is `mimo-auth-production` a tenant id, an emulator project id, or a preference key? | `GENUINELY_UNKNOWN` | read the constructor's immediate use of the string (next phase: string-argument tracing) |
| A2 | Where is sign-out implemented? | `PARTIALLY_CLOSED` | read `com.getmimo.ui.authentication.logout.{a,b}` |
| A3 | Does the scheduled `Runnable` in `ku.a.d` revoke tokens or merely log? | `NOT_RECOVERED` | read `app.rive.c` constructor `(Object,Object,B)` branch used at that call site |
| A4 | Interceptor order (`hg.e` before/after `fh.a`)? | `GENUINELY_UNKNOWN` | read the OkHttp builder arm in `ae.m` (mission-06 case 20) |
| A5 | Are tokens cached beyond Firebase's own cache (e.g. in DataStore)? | `PARTIALLY_CLOSED` (negative evidence only) | a targeted write-site scan for `putString(<*\*token\*>)` in app classes |
| A6 | Does account deletion clear the local Firebase user? | `NOT_RECOVERED` | read `AccountDeleteWork.doWork` |

None of these is upgraded by assumption. Each is carried into Phase 12 with the transition rules of that phase.

## 4. Why this phase can be called "closure" at all

Because the two questions that mattered — *what holds the credential* (Q-121) and *how it reaches a request* —
are answered with instruction-level evidence, and the answers are falsifiable:

* no app-owned token store exists (a negative claim backed by a positive mechanism),
* the token has exactly one producer (`ku.a.d(Z)`),
* there is exactly one central consumer (`fh.a`) plus four manual consumers,
* refresh is expiry-driven with a single forced retry.

What remains open is scoped, enumerated and small.

## 5. Evidence index

* `05_AUTHENTICATION_CLOSURE/evidence/DEX_auth_interceptors_and_repository.json`
* `05_AUTHENTICATION_CLOSURE/evidence/METHOD_NAME_RECOVERY.json`
* `evidence/DEX_ku.a_access_token_provider.json`
* `evidence/SCAN_TOKEN_LITERALS.json`, `evidence/SCAN_LOCAL_STORAGE_LITERALS.json`,
  `evidence/SCAN_METHODS_TOKEN.json`, `evidence/SCAN_AUTHORIZATION_HEADER.json`
* `02_METHOD_RELATIONSHIPS/02_EDGES_FOCUS_EXTRACT.csv`
