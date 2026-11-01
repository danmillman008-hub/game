# Mission 7 — Dependency Lifecycle

## Graph shape (VERIFIED_STATIC)
`ae.m` contains **127 `when` arms**; **74** of them return a typed object, the rest are
utility/exception arms. Dependencies are wired by *field*: each arm reads fields already assigned by earlier arms
(`providers_used`), so the graph is **ordered and eager** — construction order is the case order.

Case 1 provides the analytics singleton `com.getmimo.analytics.a`; case 20 the `OkHttpClient`; case 22 the
`HttpUrl` (`api-testing.mimo.org` vs `https://api.mimo.org`).

## Scope (INFERRED_HIGH)
No annotation scoping exists. One graph per process; ViewModels receive repositories from it; activity-scoped
objects are built inside activities. Nothing is recreated on rotation; process death rebuilds everything.

## Lifecycle table
| Object | Created | Dies |
|---|---|---|
| graph (`ae.m`) | Application | process |
| OkHttp/Retrofit (case 20) | graph | process |
| Room DB + DAOs | graph | process |
| analytics singleton (case 1) | graph | process |
| lesson VM state | ViewModel | process death |
| progress rows | per lesson write | deleted after push |

## Failure path
An exception in any arm aborts graph construction; no defensive branch exists → startup failure, not degraded
startup (VERIFIED_STATIC for absence of try/catch around the switch).
