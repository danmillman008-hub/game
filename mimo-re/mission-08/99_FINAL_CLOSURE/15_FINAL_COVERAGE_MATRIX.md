# 15 — Final coverage matrix

45 domains, each with a terminal status. Machine-readable: `15_FINAL_COVERAGE_MATRIX.csv` (status + evidence anchor +
note per domain). Status vocabulary: `COMPLETE`, `SUBSTANTIALLY_COMPLETE`, `PARTIALLY_COMPLETE`, `BACKEND_ONLY`,
`BLOCKED_BY_ENVIRONMENT`, `GENUINELY_UNKNOWN`.

## Summary

| Status | Domains |
|---|---|
| COMPLETE | **25** |
| SUBSTANTIALLY_COMPLETE | **15** |
| PARTIALLY_COMPLETE | **5** (D-04, D-23, D-24, D-25, D-44) |
| BACKEND_ONLY | 0 as a whole domain (server behaviour is carried *inside* D-15, D-16, D-36 as open questions) |
| BLOCKED_BY_ENVIRONMENT | 0 as a whole domain |
| GENUINELY_UNKNOWN | 0 as a whole domain |

No domain is unclassified and none is missing relative to the 45-domain register
(`00_BASELINE/CANONICAL_DOMAIN_REGISTER.json`).

## The 20 domains that carry the product

| ID | Domain | Status | Anchor |
|---|---|---|---|
| D-02 | startup/DI | COMPLETE | 127 provider cases |
| D-03 | content hierarchy | COMPLETE | 19/1,029/1,947/18,272 |
| D-05/06/07 | DSL, parser, AST | COMPLETE | `te.a`–`te.g` |
| D-09 | lesson runtime | COMPLETE | `base.c` K/e0/U/V/W/X |
| D-10/11/12 | interactions, grading, feedback | COMPLETE | Stage 4 (16 files) |
| D-14/15 | learner model, progression | COMPLETE | Stage 5 |
| D-17/18 | Room, sync/outbox | COMPLETE | Stages 5–6 |
| D-19/20 | network stack, endpoints | COMPLETE | Stage 7 (62/29/5) |
| D-22 | SSE | COMPLETE | Stage 7 §8 |
| D-28/29 | resources, design system | COMPLETE | mission-07 12 |
| D-35 | background jobs | COMPLETE | mission-07 86 |
| D-38/39 | SDKs, security posture | COMPLETE | mission-06 13/14 |
| D-40 | offline/failure | COMPLETE | `08_OFFLINE_CAPABILITY_MATRIX.csv` |
| D-43 | auth token lifecycle | COMPLETE | phase 5 + Stage 7 |

## The 5 partially complete domains (with the exact gap)

| ID | Domain | Gap |
|---|---|---|
| D-04 | dynamic modules | locale module *code* is a stub; assets present (Q-05) |
| D-23 | execution socket | frame schema not recovered (Q-40) |
| D-24 | Pusher | channel/event names are SDK-internal (Q-89) |
| D-25 | push notifications | receive path only; send is backend |
| D-44 | privacy/consent | SDK consent state only; no app consent screen (Q-134) |

## How to read this matrix

* `COMPLETE` means: entry point, classes, bodies, inputs/outputs, callees, control flow, persistence/network touchpoints,
  error paths and evidence links all exist for the domain, and no question about it is open.
* `SUBSTANTIALLY_COMPLETE` means the behaviour is reconstructed but a named sub-question is partial (listed in §14).
* A domain being complete does **not** mean runtime-verified. Zero domains are runtime-verified.
