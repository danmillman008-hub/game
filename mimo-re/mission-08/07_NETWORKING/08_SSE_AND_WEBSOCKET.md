# Phase 8 — SSE and WebSocket

## 1. SSE — AI tutor

```text
POST {w}/v1/aiTutor/conversations            (new conversation)
POST {w}/v1/aiTutor/conversations/{id}       (continuation)
headers: Content-Type: application/json
         Accept: text/event-stream
         Authorization: Bearer <ku.a.d(false)>        ← manual, not fh.a
body:    StartConversation{ systemMessage, userMessage }
reader:  okhttp3.sse.RealEventSource + EventSourceListener
frames:  data: AiTutorConversationMessage{ content, conversationId, finishReason }
end:     finishReason == "Stop" (natural) | "Length" (truncated)
```

Properties that follow from the recovered reader:

* the append target is the **last assistant message**, so out-of-order or interleaved frames have no per-message key;
* `conversationId` arrives **in the payload**, not in a header or a redirect, and must be captured to continue;
* there is **no** `retry:` field handling, no `Last-Event-ID`, no resume token, no heartbeat expectation — a dropped
  connection ends the answer;
* on cancellation the `EventSource` closes; whether the server stops generating is unobservable (A-08).

Quota: `GET /v1/aiTutor/conversations/messages/count` on the shared Retrofit returns a count without a limit value, so
the client cannot predict when the quota ends.

## 2. WebSocket — code execution

```text
wss://api.mimo.org/v1/run/socket
Sec-WebSocket-Protocol: authorization.bearer.<token>      ← auth via subprotocol
listener: pg.a (okhttp3.WebSocketListener)                ← the only raw WebSocketListener in the app
wrapped by: com.getmimo.ui.inputconsole.a (DI case 113)
```

* **frame schema: NOT_RECOVERED** (`pg.a.onMessage` body was not readable in the recovered decompilation). What is
  known by construction: the socket streams run output and pairs with the synchronous
  `POST /v1/code/runfiles` result type (`ExecuteFilesResponse`).
* **lifecycle: NOT_RECOVERED** — no reconnect, no ping/pong, no close-code handling, no timeout on this socket (the
  underlying C1 read timeout does not apply to an established WS connection the same way).
* the token is read **once** at connect time; a token that expires mid-socket is not refreshed, because the socket never
  re-authenticates.

## 3. Pusher (third channel, SDK-owned)

`com.getmimo.data.source.remote.pusher.a` performs the Pusher channel-authorization call with a **manual**
`Authorization` header and uses `f9.j` as the client. The app does not implement the WSS protocol itself; the frames
and channel names remain `UNKNOWN` (mission-07 71).

## 4. Protocol comparison

| Property | REST | SSE | WS | Pusher |
|---|---|---|---|---|
| transport | OkHttp C1/C3 | OkHttp C1 (manual request) | OkHttp C1 (manual handshake) | SDK client |
| auth channel | `Authorization` via `fh.a` | `Authorization` manual | `Sec-WebSocket-Protocol` | manual `Authorization` for channel auth |
| reconnect | n/a | none | none | SDK |
| backpressure | n/a | none recovered | none recovered | n/a |
| schema recovered | yes (62 endpoints) | partial (`content`, `conversationId`, `finishReason`) | no | no |

## 5. Why three auth channels matter

A single change to `ku.a` (the token provider) reaches all three, but a change to `fh.a` (the annotation-driven
interceptor) reaches **only** REST-via-annotation. SSE, WS and the Pusher channel auth each read the token directly.
This is the practical consequence of the four manual `Authorization` sites recorded in phase 5 and is the structural
reason those sites exist.
