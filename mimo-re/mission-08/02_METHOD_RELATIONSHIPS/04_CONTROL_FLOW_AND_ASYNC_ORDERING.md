# Phase 2.4 — Control flow and asynchronous ordering

Static control flow is reconstructable from the instruction stream. **Ordering at runtime is not**, and this
document separates the two.

## 1. Synchronous control flow (recovered)

Per method the DEX gives `if-*`/`goto`/`packed-switch`/`sparse-switch` and catch handlers. Two recovered shapes
recur in the app namespace:

* **guard-then-work** — `ku.a.d(Z)`: three exits (null user → log + `return null`; fresh token → `return token`;
  expired → refresh → `return token`), with one exception handler that converts *any* throwable into
  `AccessTokenUnavailableException`.
* **switch-on-tag** — merged classes (`f9.j`, `ku.a`, `cc.b`, `di.a`) dispatch by constructor tag; the branch is
  part of the identity of the behaviour (see Phase 1.9).

## 2. Coroutine model (recovered, at the level of shape only)

| Signal | Measured |
|---|---|
| suspend lambdas (`*$…$1` implementing `invokeSuspend`) reached by a framework edge | 1,103 |
| calls into the coroutine/flow helper `ra0.z` | 379 edges (`p` 234, `z` 87, `c` 21, `d` 9) |
| blocking `Tasks.await(...)` sites in the whole app-related graph | **2** (`ku.a`, `oq.n`) |
| listener-style Google-Tasks composition (`forResult`, `forException`, `whenAll*`) | 20+ distinct app call sites (e.g. `com.getmimo.data.notification.CustomerIOPushNotificationRegistry$clearPushRegistrationId$2`, `AuthenticationFirebaseRepository$anonymousAuthentication$2`, `com.getmimo.data.firebase.RemoteConfigRepository$observeBoolean$1$2`) |

Reading: the codebase is **Flow/first-class-suspend first** (`ra0.z` + `invokeSuspend`), with listener-based Task
composition where it touches Firebase, and **exactly two blocking bridges** — one of which is the token provider.
A blocking token fetch inside a suspend chain is a deliberate design choice (or a deliberate simplification), and
it is the only place where a network call can block a coroutine without a listener.

## 3. Ordered chains that are *evidenced*

### 3.1 Account deletion (deferred path)

```
com.getmimo.data.source.remote.account.a.c()
  1  "Bearer ".concat(tokenProvider.d(false))          direct data dependency
  2  Data.Builder().putString("ARGS_ACCESS_TOKEN", …)
  3  new OneTimeWorkRequest.Builder(AccountDeleteWork)  → constraints: NetworkType.CONNECTED
  4  WorkManager.enqueue(request)                       → androidx.work.impl.b.a
```
Order is proven by the instruction sequence (no jumps between steps 1–4, single basic block).
What is *not* proven: when WorkManager runs the worker, whether it runs at all, and what the worker does with the
token (its `doWork` body was not read in Phase 2).

### 3.2 Token acquisition

```
ku.a.d(forceRefresh=false)
  ├── FirebaseAuth.currentUser == null → log "There is no Firebase user!" → return null
  └── GetTokenResult = FirebaseAuth.c(user, false) → Tasks.await(...)
        ├── exp (seconds) >= now (seconds)  → return result.a   (token)
        └── exp <  now                      → FirebaseAuth.c(user, true) → await → return result.a
  (any exception → AccessTokenUnavailableException)
```

### 3.3 Executable-lesson bridge handshake

```
WebView constructor
  → loadDataWithBaseURL(base, html, "text/html; charset=UTF-8", …)
  → HTML template substitution: __MIMO_DOCUMENT_ID__ = UUID.randomUUID().toString(),
                                __MIMO_TOUCH_SLOP_CSS_PX__ = displayMetrics-derived px
  → addJavascriptInterface(bridge, "dispatchToWeb")   (exposed name proven; see note below)
  → JS → evaluateJavascript("window.dispatchEvent(new CustomEvent('mimo-visibility', {…}))")
inbound: JSON {documentID, kind, gesture, decision} → Kotlin handling
```
Order (load → inject → evaluate) is proven. The exact `addJavascriptInterface` object name and the JS function
names inside `lesson-webview.js` are `NOT_RECOVERED` (the asset is not decoded yet, and the DEX only names the
Java-side method `dispatchToWeb`).

## 4. Ordering that cannot be established statically

| Question | Why not answerable here |
| --- | --- |
| does the outbox sync before or after the UI refresh? | ordering depends on coroutine dispatchers and Room transaction completion at runtime |
| does the SSE stream open before the lesson screen renders? | both are started from independent scopes; no static join point observed |
| does FCM delivery precede the Pusher event for the same lesson? | two independent transports, no ordering evidence in code |
| is `lesson-webview.js` evaluated before first paint? | `evaluateJavascript` is posted to the WebView message loop |
| does the deferred account deletion run before the next app start? | WorkManager scheduling is a platform decision |

These are recorded as `INFERRED`-free gaps: they are listed as ordered **unknowns**, not as claims. Phase 11 must
not build sequence diagrams that pretend to know them.

## 5. Threading

Static evidence does not fix threads. What is provable: 2 blocking `Tasks.await` sites, 246 `Flow.collect`
registrations, and no `Thread`/`Executor` construction inside the app namespace that the graph attributes to the
token path. The DI arms (mission-06) supply the OkHttp client with explicit 20 s/30 s timeouts, and `hg.e` /
`fh.b` / `fh.a` are the interceptor family — but which thread executes `ku.a.d` is a runtime property.
