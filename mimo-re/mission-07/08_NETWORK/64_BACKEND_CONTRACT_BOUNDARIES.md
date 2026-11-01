# Mission 7 — Backend Contract Boundaries

## Client-known (evidence: client code)
- endpoint paths/verbs and DTO shapes (62 endpoints, 50 DTOs);
- auth requirements on 53;
- that progress is pushed as a batch and deletions are the acknowledgement;
- that the server returns `reachedGoal`, `dailyGoalCoinReward`, ETA and completion data.

## Unknown by definition (no client evidence possible)
| Server behaviour | Why unknowable here |
|---|---|
| whether duplicate progress re-awards coins | server logic |
| how chapter/track completion is computed | no client computation exists |
| ETA formula | only `currentPaceMinutesPerDay` is returned |
| league promotion thresholds | server reports result only |
| AI tutor prompt handling/moderation | only the client envelope is visible |
| quota threshold value | count returned without limit |
| discount eligibility | server sends themes |
| deduplication of progress asserts | no client id/nonce |

## Rule honoured
No server behaviour is asserted anywhere in Mission 7; the boundary is explicit and testable
(`124_SEMANTIC_TEST_STRATEGY.md` includes a test that forbids server-behaviour phrasing in claim records).
