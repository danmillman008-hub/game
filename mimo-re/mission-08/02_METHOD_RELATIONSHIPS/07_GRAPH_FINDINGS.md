# Phase 2.7 — What the call graph establishes (and what it refuses to)

## Established (each with an edge artefact)

1. **The app-related graph is 85,724 edges / 138,025 call sites**, of which 56,012 are app→app, 24,186 go to
   platform classes, and exactly **1** is unresolved.
2. **No app class is called but absent from the dex.** The "missing" classes of Phase 1 (AccountRepository,
   AuthenticationFragment, RiveAnimationKt, PusherConnectionManager) are never the target of a static `invoke`.
   They are reached through interfaces and inheritance — which is precisely why renaming them left their lambdas
   intact.
3. **The token provider has nine app-side entry points**, all through `ku.a.d(Z)`; no reflection and no callback
   participates. This is the backbone of Phase 5 (authentication closure).
4. **Blocking is exceptional: two `Tasks.await` sites in the entire app namespace** (`ku.a`, `oq.n`), against 246
   `Flow.collect` registrations and 379 flow-helper edges. Asynchronous composition is Flow-first.
5. **Account deletion is a WorkManager deferral with the token copied into the job's input data** and a
   "network connected" constraint (`account.a.c()`).
6. **The executable-lesson bridge is a real JS↔Kotlin channel**: `addJavascriptInterface`, `evaluateJavascript`,
   `loadDataWithBaseURL`, four inbound JSON keys and one injected `CustomEvent`.
7. **Reflection is absent from the app namespace** — 20,599 reflection sites, all library-internal.

## Refused (deliberately not claimed)

| Tempting statement | Why it is refused |
|---|---|
| "`ku.a` is a heavily used core class" | `ku.a` is a **merged** class; its fan-in mixes Firebase, GMS, Coil, Facebook, RevenueCat and gRPC call sites. Only per-method statements are valid. |
| "the app uses 85k method relationships, so it is well understood" | edge count ≠ understanding; 561 of 637 registered methods are still `BODY_PRESENT_NOT_READ` |
| "`ra0.z` is the coroutine dispatcher" | 379 edges prove it is the flow/coroutine helper *used* by these callers; its own body and semantics were not read in this phase |
| "the notification service posts notifications after FCM" | the service's `d(RemoteMessage)` body was read to the point of `title`/`body` extraction only; the notification-building tail is not traced |
| "the WebView bridge dispatches gestures synchronously" | registration and injection order is proven; runtime hand-off is not |
| "`i9.t`/`q9.r`/`r9.c` are the WorkManager builder chain" | they are consistent with it and referenced by `account.a.c()`, but their own bodies were not read |

## Effect on the method-status register

Phase 2 raises the *ceiling* for call-graph work but does not promote methods by itself: `CALL_GRAPH_TRACED`
requires enumerated callers **and** callees with evidence for that specific method. The 61-class register stays at
`BEHAVIOUR_RECONSTRUCTED 9 · DEX_INSPECTED 44 · JAVA_INSPECTED 2` until Phase 3 traces complete per-subsystem
chains; the graph file is the artefact those promotions will cite.

## Immediately actionable for later phases

| Phase | Uses |
|---|---|
| 3 (subsystems) | `02_TYPED_GRAPH_EDGES.csv.gz` filtered by subsystem package |
| 5 (auth closure) | the nine `ku.a.d` call sites + `AccessTokenUnavailableException` |
| 6 (AI/realtime) | `AiTutorRepository$sendMessage$2 → ku.a.d`, `pg.a → ku.a.d`, callback edges into `Flow.collect` |
| 7 (learner/progress) | 246 collect edges as the observation surface of learner state |
| 11 (E2E) | framework-entry table in `06_…` as the set of legitimate flow starts |
| 16 (final audit) | edge counts + confidence split as the *relationship* dimension (never as a percentage of truth) |
