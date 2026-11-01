# Mission 7 — Final Domain Audit

**Four notions kept separate** (the brief demands it): complete *inventory* ≠ complete *static reconstruction* ≠
complete *behavioural understanding* ≠ *runtime confirmation* (which is zero for every domain).

| Domain | Class | Inventory | Static reconstruction | Runtime |
|---|---|---|---|---|
| APK/packaging | FULLY RECONSTRUCTED | complete | complete | n/a |
| startup/DI | FULLY RECONSTRUCTED | complete | complete | complete |
| content hierarchy | FULLY RECONSTRUCTED | complete | complete | substantial |
| dynamic modules | PARTIALLY RECONSTRUCTED | partial (names only) | none | none |
| DSL grammar | FULLY RECONSTRUCTED | complete | complete | complete |
| parser | FULLY RECONSTRUCTED | complete | complete | complete |
| AST | FULLY RECONSTRUCTED | complete | complete | complete |
| rendering | PARTIALLY RECONSTRUCTED | partial | partial | partial |
| lesson runtime | FULLY RECONSTRUCTED | complete | complete | complete |
| interactions | FULLY RECONSTRUCTED | complete | complete | complete |
| grading | FULLY RECONSTRUCTED | complete | complete | complete |
| feedback/retry | FULLY RECONSTRUCTED | complete | complete | complete |
| executable lessons | SUBSTANTIALLY RECONSTRUCTED | complete | substantial | partial |
| learner model | FULLY RECONSTRUCTED | complete | complete | substantial |
| progression | FULLY RECONSTRUCTED | complete | complete | complete |
| gamification | FULLY RECONSTRUCTED | complete | complete | partial |
| room/persistence | FULLY RECONSTRUCTED | complete | complete | complete |
| sync/outbox | FULLY RECONSTRUCTED | complete | complete | substantial |
| network stack | FULLY RECONSTRUCTED | complete | complete | substantial |
| endpoints | FULLY RECONSTRUCTED | complete | complete | partial |
| AI tutor | SUBSTANTIALLY RECONSTRUCTED | complete | substantial | substantial |
| SSE | FULLY RECONSTRUCTED | complete | complete | complete |
| execution socket | SUBSTANTIALLY RECONSTRUCTED | complete | partial | none |
| Pusher | PARTIALLY RECONSTRUCTED | partial | partial | none |
| push notifications | PARTIALLY RECONSTRUCTED | partial | partial | partial |
| navigation | PARTIALLY RECONSTRUCTED | partial | partial | partial |
| screens | PARTIALLY RECONSTRUCTED | partial | partial | partial |
| resources | FULLY RECONSTRUCTED | complete | complete | n/a |
| design system | FULLY RECONSTRUCTED | complete | complete | n/a |
| Rive | SUBSTANTIALLY RECONSTRUCTED | complete (assets) | none | none |
| localization | SUBSTANTIALLY RECONSTRUCTED | complete | substantial | substantial |
| accessibility | PARTIALLY RECONSTRUCTED | partial | partial | none |
| analytics | SUBSTANTIALLY RECONSTRUCTED | partial | substantial | partial |
| remote config | SUBSTANTIALLY RECONSTRUCTED | complete | substantial | partial |
| background jobs | FULLY RECONSTRUCTED | complete (absence) | complete | complete |
| subscriptions | SUBSTANTIALLY RECONSTRUCTED | complete | substantial | partial |
| native | SUBSTANTIALLY RECONSTRUCTED | complete | minimal | none |
| SDKs | FULLY RECONSTRUCTED | complete | complete | partial |
| security posture | FULLY RECONSTRUCTED | complete | complete | n/a |
| offline/failure | FULLY RECONSTRUCTED | complete | complete | substantial |

## Distribution
| Classification | Count |
|---|---|
| FULLY RECONSTRUCTED | 24 |
| PARTIALLY RECONSTRUCTED | 7 |
| SUBSTANTIALLY RECONSTRUCTED | 9 |

## Not represented here
Backend-only behaviour (completion aggregation, ETA, quota, league promotion) and out-of-scope items (server
implementation) have no row because no client artefact can confirm them.
