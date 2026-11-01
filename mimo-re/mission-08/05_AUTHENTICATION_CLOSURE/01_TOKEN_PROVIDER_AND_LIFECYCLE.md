# Phase 5.1 — Token provider and lifecycle

**Question this closes (Q-121):** where are Mimo's credentials stored and how are they refreshed?

## 1. Answer

There is **no application-owned token repository**. The only credential object in the app namespace is a
`FirebaseAuth` handle, and the only token-producing method is

```
ku.a.d(boolean forceRefresh) : String
```

which is present in **`classes2.dex`**, has **83 instructions**, and has **no decompiled Java** (DAD emits nothing
for `ku.a`). Its body was read at instruction level (`evidence/DEX_ku.a_access_token_provider.json`).

## 2. Lifecycle, reconstructed

| Step | Instruction evidence | Meaning |
|---|---|---|
| L1 | `iget-object … Lku/a;->a Ljava/lang/Object;` + `check-cast … FirebaseAuth` | the provider holds `FirebaseAuth` |
| L2 | `iget-object … FirebaseAuth;->f Lcom/google/firebase/auth/FirebaseUser;` | current user |
| L3 | `if-eqz v6` → `const-string "There is no Firebase user!"` → `invoke-static Lwc/f;->i` → `return-object v0` | **signed-out path**: logs, returns `null` |
| L4 | `FirebaseAuth;->c(FirebaseUser; Z)Task` with `const/4 v0, 0` | `getAccessToken(false)` — cached token |
| L5 | `Tasks.await(...)` | **blocking** bridge (one of only two in the app) |
| L6 | `const-string "exp"` → `vu/d;->b Ljava/util/Map;->get` → `Integer` | read JWT `exp` claim (Unix seconds) |
| L7 | `new-instance Lorg/joda/time/DateTime;` → `div-long 1000` → `cmp-long` | compare with now |
| L8 | `if-gez v0` → return `vu/d;->a` | **fresh**: return token unchanged |
| L9 | `FirebaseAuth;->c(FirebaseUser; Z=1)` → `Tasks.await` → `vu/d;->a` | **expired**: one forced refresh, then return |
| L10 | `const-string "Token doesn't exist!"` → `IllegalStateException` → `catch` → `new AccessTokenUnavailableException` | **failure**: typed exception |
| L11 | `zu.b;->a()` … `new-instance Lapp/rive/c;` `(Object,Object,B)` → `lev.b;->a(Runnable)` | schedules Firebase token-revocation bookkeeping (the `runnable` is reused helper code, not Rive rendering) |

## 3. Properties that follow from the body

* **Refresh is lazy and expiry-driven**, not timer-driven: there is no scheduler, no WorkManager, no AlarmManager
  involved in token refresh.
* **Exactly one refresh attempt** when expired; if that refresh throws, the caller gets
  `AccessTokenUnavailableException` and never a stale token.
* **No skew margin**: the comparison is `exp < now`; there is no grace period constant in the method.
* **Signed-out is not an error**: callers receive `null` and must decide. (The `null` then produces
  `"Bearer null"` if a caller concatenates blindly — the call sites guard, but this is a client-side hazard worth
  noting.)
* **Blocking by design**: the token fetch blocks the calling coroutine, because the interceptor
  (`fh.a.intercept`) is synchronous by OkHttp contract.

## 4. Where the credential actually lives

| Layer | Owner | Evidence |
|---|---|---|
| credential persistence | **Firebase Authentication SDK** (internal `SharedPreferences`/`DataStore` storage) | no app class writes a token; `ku.a` only reads `FirebaseAuth.currentUser` |
| in-memory token | Firebase SDK cache | `FirebaseAuth.c(user,false)` returns a cached `GetTokenResult` |
| token as a *value* copied by the app | **WorkManager input data** (`ARGS_ACCESS_TOKEN`) for deferred account deletion | `com.getmimo.data.source.remote.account.a.c()` |
| token in headers | `fh.a` (central, for annotated Retrofit methods) + 3 manual sites | see `02_INTERCEPTOR_CHAIN.md` |

Mission-08 records no token value, hash, length or prefix anywhere.

## 5. Status

`BEHAVIOUR_RECONSTRUCTED` for `ku.a.d(Z)`. The Firebase SDK's own storage format is **library behaviour** and out of
scope; that residual is recorded explicitly rather than as "unknown".

## 6. Evidence

* `evidence/DEX_ku.a_access_token_provider.json` (mission root `evidence/`)
* `evidence/DEX_auth_interceptors_and_repository.json`
* `02_METHOD_RELATIONSHIPS/02_EDGES_FOCUS_EXTRACT.csv` (the nine `ku.a.d` call sites)
