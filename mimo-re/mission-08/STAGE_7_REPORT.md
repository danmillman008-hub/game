# Mission 8 — Stage 7 Report (networking and authentication)

**Status:** `substantially_complete` · **Base:** Stage 6 `8049767` · **2026-11-01**
**Deliverables:** 12 files + 3 JSON companions + 26 semantic tests in `07_NETWORKING/`.

## 0. Environment (read this before the findings)

The sandbox was rebuilt between sessions: the APK, the 12 DEX files, `/tmp/dad` and the Python venv were gone, and the
local git history had been re-initialised to the mission base commit while the working tree survived as untracked
files. Both were reconciled before any analysis:

* `git fetch` + tree comparison showed the working tree byte-identical to remote `8049767`;
* `git reset --mixed FETCH_HEAD` restored HEAD to `8049767` with **no** file changes and **no** remote rewrite.

Because the host allow-list (`github.com`, `pypi.org`, `registry.npmjs.org`) excludes every APK mirror, the target could
not be re-acquired. **Stage 7 therefore performed no new DEX reads**; every claim is re-derived from committed evidence
(`mission-06/evidence/DI_GRAPH.json`, mission-08 phase-5 dumps, `API_CATALOG_V2.csv`, the obfuscation map). Claims that
would need a fresh read are marked `BLOCKED_BY_ENVIRONMENT` rather than filled in.

## 1. What is now established

* **Six client objects** with per-client configuration read from their DI case bodies: the authenticated client
  (20 s/30 s, three interceptors), the shared Retrofit (case 22 host + kotlinx converter), a long-timeout client
  (10 s/120 s, **no** connectivity gate), and three single-host Retrofit instances (Customer.io, mimo-auth, e-mail).
* **Interceptor order proven** (`hg.e` → `fh.b` → `fh.a`) from the `add(…)` sequence — this closes the ordering
  question mission-08 phase 5 left open.
* **62 endpoints in 29 interfaces**, each attributed to a client and an origin; five distinct hosts, no single-backend
  assumption.
* **Authentication is method-annotation driven** (`Method.getAnnotation` on the Retrofit tag) with the token from
  `ku.a.d(false)`; four transports authenticate by four different channels (interceptor header, manual header,
  WebSocket subprotocol, Pusher channel auth).
* **No retry, no 401 handling, no idempotency key, no cache, no pinning** — established as absences in the recovered
  bodies, not as assumptions.
* The progress POST's place in the architecture: an **outbox flush** at chapter end and app start, grouped per
  tutorial, acknowledged by row deletion.

## 2. Corrections

C-17 (dev-menu host switch, Q-76 closed) · C-18 (`fh.a` conditional, `ku.a` token, `ri.b` is an annotation) ·
C-19 (offline gate throws `java.io.IOException`) · C-20 (`d70.b` = `Continuation`, no `Result` envelope).

## 3. B-1 … B-13

Closed: B-4, B-10, B-13 (and B-2 structurally). Partially: B-3, B-5, B-6, B-7. Backend-only: B-8.
Blocked by the missing APK: B-1, B-9, B-11, B-12.

## 4. Limits

No runtime evidence. No traffic. The per-endpoint annotation list, the WebSocket frame schema, the SSE resume
semantics and the `Json` strictness remain open (A-01 … A-10). Nothing in this stage asserts server behaviour.
