# 09 — SPEC: analytics, remote config, entitlements (context, not required for the engine)

Sources: `mimo-re/mission-07/10_ANALYTICS_CONFIG`, `mimo-re/mission-07/12_UI_RESOURCES`,
`mimo-re/mission-07/13_SUBSCRIPTION`, `mimo-re/mission-07/evidence/ANALYTICS_DISPATCH.json`,
`mimo-re/mission-07/evidence/EVENTS_WITH_CALLSITES.csv`. `VERIFIED_STATIC`.

## 1. Analytics

* 14 events are bound to call sites (`EVENTS_WITH_CALLSITES.csv`); dispatch goes through a single façade to the vendor SDK.
* Event names and parameter keys are recoverable; **server-side interpretation is BACKEND_ONLY**.
* No analytics events were found persisted locally, so offline events are simply lost (correction C-22).

For `mimo/`: an optional local event log is a **new** feature (`ADD`-class if you add it), never "Mimo's analytics".

## 2. Remote config / feature flags

A remote-config surface exists (keys category, 2 endpoints). Defaults are compiled in and were recoverable as
constants; the remote override values are **not** observable statically and were not fetched (no production access).

## 3. Entitlements / subscription

* Product ids and the entitlement gate are recoverable; the paywall gate is evaluated **client-side against a
  server-issued entitlement** (BACKEND_ONLY for the decision itself).
* Rule 6 applies: nothing in this repo bypasses, forges or emulates the entitlement check. `mimo/` must not contain a
  "premium unlock" workaround; if the engine needs a gate, it takes an explicit local capability flag with a documented
  source.

## 4. Code execution

4 endpoints exist for running user code remotely; the execution sandbox is server-side (BACKEND_ONLY). An offline engine
that wants executable lessons must define a **local, sandboxed** runner and label it as new work.

## 5. What this means for the build

| Feature | Offline engine |
|---|---|
| content + lessons | in scope, from assets |
| grading + feedback | in scope, fully specified (`04`) |
| progress | in scope, local rule `ADD-04` |
| analytics | out of scope (optional local log) |
| remote config | out of scope; compile-time constants |
| entitlements | out of scope; no bypass, no emulation |
| code execution, tutor, certificates | out of scope |
