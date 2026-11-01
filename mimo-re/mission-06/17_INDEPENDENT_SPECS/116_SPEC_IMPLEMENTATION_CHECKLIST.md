# Spec 116 — Implementation Checklist (evidence-gated)

## MUST

A reconstruction effort should tick these in order; each line names the evidence that makes it safe.

### Ordered gates

| # | Item | Evidence | Gate |
|---|---|---|---|
| 1 | AST + DSL parser | 16–19 | can parse 20,306-doc corpus without new error classes |
| 2 | Grading (2-phase) | 26, 30 | unit vectors reproduce verdicts incl. false positives |
| 3 | Lesson state machine | 22, 38 | transitions match table exactly |
| 4 | Progress outbox | 40–44 | offline → push → delete sequence |
| 5 | Content hierarchy | 09–15 | section delta form supported |
| 6 | API client | 47–55 | UA/Bearer/timeout/verbs match catalogue |
| 7 | AI tutor SSE | 56–62 | finishReason handling |
| 8 | Gamification display | 32–37 | server-order rendering, no local computation |
| 9 | Navigation/deep links | 63–69 | 12 filters → one entry activity |
| 10 | Design system | 70–74 | fonts + two palettes; values pending |
| 11 | Auth/subscription | 75–81 | RevenueCat entitlement only |
| 12 | Analytics | 82–85 | only verified events claimed |

Unticked by design: anything requiring runtime (`15_RUNTIME/96_TEST_TO_SOURCE_MATRIX.csv`).
