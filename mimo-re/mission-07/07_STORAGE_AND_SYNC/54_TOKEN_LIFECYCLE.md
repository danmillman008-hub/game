# Mission 7 — Token Lifecycle

## Recovered (VERIFIED_STATIC)
| Stage | Evidence | Status |
|---|---|---|
| storage | `ri.*` holder; `ri.b.d(0)` returns the token string | PARTIAL — implementation not decompiled |
| injection | `fh.a.intercept` sets `Authorization: Bearer <token>` on the authenticated client | VERIFIED_STATIC |
| WebSocket auth | `Sec-WebSocket-Protocol: authorization.bearer.<token>` in `pg.a` | VERIFIED_STATIC |
| Pusher auth | `f9.j` reads API host/token | PARTIAL |
| refresh | no refresh interceptor recovered | NOT_RECOVERED |
| expiry handling | no 401 branch in the interceptors | NOT_RECOVERED |
| deletion/logout | no logout code recovered | NOT_RECOVERED |

## What is certain
The token is a **plain string** injected by an interceptor; the app has no visible refresh mechanism, so expiry
is either long-lived or handled by the repositories (which would surface as a thrown failure through `d70.b`).

## Not attempted
No token values were read, logged or committed (RULE E).
