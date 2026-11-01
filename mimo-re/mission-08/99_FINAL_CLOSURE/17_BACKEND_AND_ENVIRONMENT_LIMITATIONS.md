# 17 — Backend and environment limitations

Two distinct kinds of limitation, kept apart deliberately.

## 1. BACKEND_ONLY — unanswerable from any client artifact

| # | Behaviour | Why it is out of reach |
|---|---|---|
| 1 | chapter/tutorial completion rule (Q-49) | client stores the server's verdict; no computation exists |
| 2 | ETA formula (Q-50) | only `currentPaceMinutesPerDay` is returned |
| 3 | whether duplicate progress re-awards coins | no client idempotency key exists to reason from |
| 4 | server merge of session `attempts` (B-8) | client always sends the session value |
| 5 | whether `null` timestamps can be sent (A-06) | client rejects them at the Room boundary |
| 6 | whether closing SSE aborts generation (A-08) | transport-level server behaviour |
| 7 | quota threshold for the tutor | count endpoint returns no limit |
| 8 | 4xx semantics per endpoint, rate limits, pagination | server contract |
| 9 | entitlement grant authority | RevenueCat/server, not the client |
| 10 | Push send path | FCM server side |

None of these is estimated anywhere in the dossier.

## 2. BLOCKED_BY_ENVIRONMENT — answerable in principle, impossible here

| # | Item | What is missing |
|---|---|---|
| 1 | per-endpoint auth annotation table (A-01, A7) | DEX read of the 29 interfaces |
| 2 | remaining 25 DAO lambda id→SQL (B-1) | DEX read of `cg/a`, `leg/c`, `leg/f` |
| 3 | Room builder destructive-fallback flag values (B-9) | control-flow walk of a 1,643-instruction provider |
| 4 | `mimo_prefs` / DataStore key set (B-11, B-12) | data-flow over a generic preference helper |
| 5 | WebSocket frame schema (Q-40) | DEX read of `pg.a.onMessage` |
| 6 | dynamic-module locale code (Q-05) | split APK bundles |
| 7 | unread bodies: logout classes, `AccountDeleteWork`, `base.c.O`, webivew JS asset | DEX/assets |

Cause: the APK (`sha256 48ce1740…`) and its 12 DEX files are absent, and the sandbox reaches only
`github.com`, `api.github.com`, `pypi.org`, `registry.npmjs.org`. `apkpure.com`, `ghproxy.net` and
`raw.githubusercontent.com` all return 000. The repository itself has no LFS objects and its only release asset is an
unrelated APK.

## 3. NOT_RECOVERED — bodies that never decompiled well

The decompiler produced 431 invalid Java files and 1,059 queued classes have no body. Items 7 above and the
`app.rive.c` Runnable (A3), `f9.j` tag-17 branch (A10) and the `kind` vocabulary (A9) sit here. They are *known*
unrecovered, not unknown-unknown.

## 4. What is explicitly **not** a limitation

* Class inventory, call graph, content corpus, endpoint catalogue, schema, grading rules, learner model and auth
  lifecycle are complete at the static level; they are limited only by the absence of runtime confirmation.
* No part of the mission was skipped for convenience; every deferred item appears in `14`.

**Evidence anchors:** `14_ALL_OPEN_QUESTIONS_CLOSURE.json` (per-status reasoning), `01_TARGET_AND_REPOSITORY_BASELINE.md` §4 (host reachability tests), `07_NETWORKING/12_OPEN_QUESTIONS.md` (part 3), `mission-07/08_NETWORK/64_BACKEND_CONTRACT_BOUNDARIES.md`.
