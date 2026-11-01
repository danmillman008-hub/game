# Mission 7 — Execution WebSocket Protocol

## Setup (VERIFIED_STATIC)
```
wss://api.mimo.org/v1/run/socket
Sec-WebSocket-Protocol: authorization.bearer.<token>
listener: pg.a (okhttp3.WebSocketListener)
```
Only one `WebSocketListener` exists in the decompiled subset, so this socket is the app's only raw WebSocket
(Pusher uses its own client internally).

## Message schema
**NOT_RECOVERED.** `pg.a`'s `onMessage` body was not decompiled in a readable form in this batch; the frames are
consumed elsewhere. What is known:
- the socket streams run output (pairs with `ExecuteFilesResponse.consoleOutput` semantics);
- the REST equivalent (`POST /v1/code/runfiles`) returns the final result synchronously.

## Lifecycle
No reconnection logic, no ping/pong handling, and no close-code handling was recovered; close conditions and
timeouts are therefore UNKNOWN (`Q-40`).
