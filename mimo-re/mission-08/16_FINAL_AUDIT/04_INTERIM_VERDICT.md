# Phase 16.4 — Interim verdict

## What is established about Mimo 9.35 by this mission so far

1. **Credential handling** — Firebase ID tokens, one producer, one central interceptor, four manual sites, lazy
   expiry-driven refresh, typed failure. (`05_AUTHENTICATION_CLOSURE/`)
2. **Session model** — anonymous-first accounts that can be linked to a real credential; auth state is observed as
   a flow, not owned as a mutable object. (`05_…/04_SESSION_STATE_MACHINE.md`)
3. **Account deletion** — deferred through WorkManager with the access token copied into the job's input data and a
   network constraint. (`02_…/05_DATA_FLOW.md` DF-02)
4. **Connectivity** — a `ConnectivityManager` callback + value class + interface (`ri.*`), consumed by an OkHttp
   interceptor that throws `NoConnectionException`. (`05_…/02_INTERCEPTOR_CHAIN.md`)
5. **Executable lessons** — a real JS↔Kotlin bridge with four proven inbound keys and two proven template
   placeholders. (`01_…/04_DEEP_CLASS_INVESTIGATION.md` C-04)
6. **Push** — FCM receive and token-refresh overrides are recovered; notification construction is not.
7. **Code structure** — the build's obfuscation merges classes (47), renames app logic out of the `com.getmimo`
   namespace (1,148), and leaves 1,379 orphan lambdas; half the investigation queue is DEX-only and 13 % of the
   decompiled Java is invalid. Every later claim must respect these three properties.

## What is definitively **not** established

* any runtime behaviour whatsoever (`runtime_verified = 0`),
* the learner/progress state machine, mastery/adaptation, `TrackEtaResponse`,
* AI tutor prompt construction and SSE state machine,
* WebSocket/Pusher/FCM lifecycles as *sequences*,
* UI composition (Compose screens, Rive per-asset binding, accessibility),
* analytics dispatch to endpoints,
* billing/subscription lifecycle beyond catalogues,
* the 1,059 DEX-only queue classes as a body of code,
* 35 of 39 inherited questions.

## The one number that matters

Of 2,178 queue classes, **9 methods in 6 classes** reached `BEHAVIOUR_RECONSTRUCTED` (0.3 % of queue classes).
Everything else is inventoried, source-mapped, edge-mapped or explicitly untouched. Stating that plainly is the
audit's job; inflating it is what the brief forbids.
