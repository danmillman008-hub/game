# Phase 2.5 — Data flow

Data flow is traced only where the instructions or the decompiled body show the *hand-off* of a value between
producer and consumer. Each flow below names its evidence.

## DF-01 Credential → HTTP header

| Step | Evidence |
|---|---|
| producer: `FirebaseAuth.c(user, forceRefresh)` → `GetTokenResult.a: String` | `ku.a.d(Z)` instruction stream |
| transform: `"Bearer ".concat(token)` | `com.getmimo.data.source.remote.account.a.c()` decompiled line 45; the same literal appears in `RemoteCertificateRepository$downloadCertificate$2`, `PusherConnectionManager$initializePusher$1`, `AiTutorRepository$sendMessage$2`, `AccountRepository$deleteAccount$2` |
| consumer: request header / WorkManager input / socket auth | header construction is inside the request builders; socket auth via `pg.a → ku.a.d` edge |

**Sensitivity.** The token *value* is never printed, stored or copied by mission-08. Only the transport shape is
recorded. The token is additionally written into WorkManager `Data` (see DF-02), which persists it via the
WorkManager database — a design observation, not a credential exposure.

## DF-02 Account deletion request → deferred worker

```
account.a.c()
  token ──► "ARGS_ACCESS_TOKEN" ──► Data ──► OneTimeWorkRequest(AccountDeleteWork)
                                                   │  constraint: NETWORK_TYPE_CONNECTED
                                                   ▼
                                          WorkManager.enqueue
```
Evidence: the four-step basic block in `account.a.c()`; `AccountDeleteWork` is the worker class literal.
Downstream (inside `doWork`) is `NOT_RECOVERED` in this phase.

## DF-03 Connectivity → state flow

```
ConnectivityManager callback (ri.a)
  onAvailable(net): set.add(n);   emit ri.c(previous, current)
  onLost(net):      set.remove(n); set.isEmpty(); emit ri.c(previous, current)
                                  └── ta0.j.k(value)  (flow emission)
consumer side: com.getmimo.network.* (NetworkState enum type carried inside ri.c)
```
Evidence: `evidence/DEX_ri_network_callback.json`. The *identity* of the emitted flow's consumers is not proven —
the emission goes through a `ta0.j` handle, and no app call site collecting that specific handle was matched.

## DF-04 Lesson HTML → WebView → Kotlin

```
assets/lesson-webview.js ─┐
HTML template ────────────┴─► loadDataWithBaseURL(base, html, "text/html; charset=UTF-8")
   substitutions: __MIMO_DOCUMENT_ID__, __MIMO_TOUCH_SLOP_CSS_PX__
   injection: window.dispatchEvent(new CustomEvent('mimo-visibility', {detail: …}))
   inbound JSON: { documentID, kind, gesture, decision } → org.json.JSONObject → Kotlin
   touch: MotionEvent → dispatchToWeb(MotionEvent) → page
   id: UUID.randomUUID().toString() used as documentID
```
Evidence: `evidence/DEX_rive_webview.json`, class `com.getmimo.ui.lesson.interactive.webview.a`.
Unknown: field names inside `detail`, the set of `kind` values, and what Kotlin does with `decision`.

## DF-05 Rive content model

```
ImageContent$Rive( int resourceId, Float ?, Map<String,?> inputs, String stateMachineName? )
      │
      └──► RiveAnimationProperties(autoplay, Fit, Alignment, Loop)  [Compose, Parcelable]
                │
                └──► RiveAnimationKt (BODY NOT RECOVERED — class absent from dex)
```
Evidence: field tables from `evidence/DEX_rive_webview.json`. The field *order* is proven; the semantic names are
inferred from type and from the `toString` of `RiveAnimationProperties` (`autoplay/fit/alignment/loop`), which is
printed in the DEX string constants. The final render call is `NOT_RECOVERED`.

## DF-06 FCM message → notification

```
RemoteMessage → MimoFirebaseMessagingService.d(RemoteMessage)   [270 insns]
   strings observed: "Notification received.", "Handle push notification", "title", "body", "crashKeysHelper"
   reads: message data keys "title"/"body"
   then: notification construction/notification-manager path — NOT traced in this phase
RemoteMessage token refresh → e(String)  [25 insns]  "Refreshed token: "
```
Evidence: `evidence/DEX_auth_push_pusher.json`. The downstream notification builder must be read before any claim
about channels, icons, or deep-link actions.

## DF-07 Lesson progress (existing mission-5/6 knowledge, re-confirmed as an edge)

Mission-6 established the Room tables and the outbox (`in_queue=1`); the graph adds the *call shape*: 379 flow
helper edges and 246 `collect` registrations mean learner state is published as flows and observed by UI. No new
persistence claim is made in this phase.

## What is deliberately absent

* No flow diagram claims a value's *runtime* path through dispatchers.
* No flow crosses the JavaScript boundary in both directions with named fields (only the four proven keys).
* No data-flow claim is made for the 1,148 renamed classes beyond the ones traced above.
