# 14 — All open questions, closed

**91 questions** across five families. Machine-readable: `14_ALL_OPEN_QUESTIONS_CLOSURE.json` (verbatim question text,
prior status, final status, final answer, evidence, and what would still close the remainder).

## 1. Distribution

| Final status | Count |
|---|---|
| CLOSED_STATIC | 36 |
| PARTIALLY_CLOSED | 24 |
| NOT_RECOVERED | 11 |
| BLOCKED_BY_ENVIRONMENT | 8 |
| GENUINELY_UNKNOWN | 6 |
| BACKEND_ONLY | 5 |
| OUT_OF_SCOPE | 1 |
| **total** | **91** |

By family: canonical 39 · mission-8 A (A1–A28) 28 · Stage-7 A (A-01…A-10) 10 · B 13 · out-of-register 1 (`Q-76`).

## 2. Closed in this mission (newly, or upgraded)

| ID | Final | What changed |
|---|---|---|
| Q-08 | CLOSED_STATIC | no reset writer exists; the row is immutable, counters are per-session |
| Q-14 | CLOSED_STATIC | ten locale packs vs a five-value enum — enum is a subset |
| Q-15 | CLOSED_STATIC | field sets recovered (`CONTENT_MODEL_FIELDS.json`) |
| Q-27 | CLOSED_STATIC | client renders document order; `index` is carried, not re-sorted |
| Q-54 | CLOSED_STATIC | deletion is a batch statement with an id list |
| Q-69 | CLOSED_STATIC | no 4xx branch; rows survive and are retried by the next trigger |
| Q-70 | CLOSED_STATIC | two triggers: chapter end, app start |
| Q-80 | CLOSED_STATIC | no app login endpoint; Firebase-mediated |
| Q-121 | CLOSED_STATIC | no app-owned token storage |
| A4 | CLOSED_STATIC | interceptor order proven (DI case 20) |
| A5 | CLOSED_STATIC | no token cached outside Firebase |
| A11 | CLOSED_STATIC | `publishSetVersion` never compared |
| A16 | CLOSED_STATIC | chapter completion is server-owned; no client auto-complete |
| A21 | CLOSED_STATIC | partial verdict does not trigger WRONG-gated modules |
| A25 | CLOSED_STATIC | no partial verdict on the executable path |
| B-6 | CLOSED_STATIC | `clearOnExit` can delete pending rows (mechanism proven) |
| B-2 | CLOSED_STATIC | no account column anywhere |
| Q-76 | CLOSED_STATIC | host switch is a dev-menu preference |

## 3. Deliberately still open (and why)

| Reason | IDs |
|---|---|
| needs the APK/DEX (unavailable) | Q-05, Q-40, A7, A-01, B-1, B-9, B-11, B-12 |
| needs a decompiled body that was never readable | A2/A-02, A3, A6, A8, A9, A19, Q-17, A-05, A-07, A-10, Q-30, Q-34, Q-39/A-04, A-03 |
| server-side by definition | Q-49, Q-50, B-8, A-06, A-08 |
| partially answerable but not fully | Q-115, Q-118, Q-57, Q-89, U-20, A11–A13 (Stage 2), A15, A17, A20, A22–A24, A27, A28, B-3, B-5, B-7, A-09 |

## 4. Rule applied

A question is `CLOSED_STATIC` only when application-side evidence answers it fully. `PARTIALLY_CLOSED` is used where one
side of the answer is proven and the other is not. Nothing is closed by plausibility, and no backend question is closed
by inference from a client method name.
