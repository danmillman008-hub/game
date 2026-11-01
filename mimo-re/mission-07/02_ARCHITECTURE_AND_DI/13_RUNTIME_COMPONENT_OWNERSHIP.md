# Mission 7 — Runtime Component Ownership

| Concern | Owner | Class |
|---|---|---|
| process entry | target base Application | `bin.ghost.YRF` → `com.getmimo.App` |
| object graph | DI switch | `ae.m` |
| HTTP | OkHttp + Retrofit | case 20 clients, 29 interfaces |
| offline gate | interceptor | `hg.e` |
| auth header | interceptor | `fh.a` + token holder `ri.*` |
| UA | interceptor | `fh.b` |
| content parsing | 7 parsers | `te.a`–`te.g` |
| lesson state | lesson VM | `base.c` + 4 interaction VMs |
| verdicts | assessment | `qm.d/e/f/g/h/i` |
| progress | repository + Room | `...ProgressRepository`, 3 tables |
| analytics | singleton | `com.getmimo.analytics.a`, events `ge.j` |
| AI chat | repository (SSE) | `AiTutorRepository` |
| code run | REST + WebSocket | `POST /v1/code/runfiles`, `pg.a` |
| realtime events | Pusher | `f9.j` |
| purchases | SDK | RevenueCat |
| crashes | SDK | Sentry |
