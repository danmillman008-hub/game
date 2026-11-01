# Mission 7 — Authentication Interceptor (complete)

## Mechanism (VERIFIED_STATIC)
`fh.a` is an OkHttp application interceptor that adds exactly one header:
`Authorization: Bearer <token>` where token = `ri.b.d(0)` (holder field, index 0).

## Which requests get it
The interceptors are attached to the client built in `ae.m` case 20. Because `fh.a` has no path check in the
decompiled body, **every request on that client carries the header** (`VERIFIED_STATIC` for the body, INFERRED for
"no conditional"). Public endpoints therefore also send it — harmless, but it means the server, not the client,
decides what is public.

## Failure behaviour
| Case | Behaviour |
|---|---|
| no token | header value `Bearer ` with empty token (no guard recovered) |
| expired token | no refresh; the call fails and the envelope propagates |
| 401 | no `Authenticator`, no retry |

## WebSocket variant
`pg.a` authenticates by subprotocol: `Sec-WebSocket-Protocol: authorization.bearer.<token>` — same token, different
channel (Phase 10).
