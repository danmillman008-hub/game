# 11 — AI tutor, SSE and code execution

## 1. AI tutor entry and eligibility

Entry points and eligibility are UI-level (mission-07 `09_STREAMING/66`, `68`): the tutor is offered from the lesson
surface and gated by plan/limit state; the quota endpoint `GET /v1/aiTutor/conversations/messages/count` returns a
count **without a limit**, so the client cannot predict exhaustion.

## 2. SSE protocol (client side complete)

```text
POST {api}/v1/aiTutor/conversations          (new)
POST {api}/v1/aiTutor/conversations/{id}     (continue)
Content-Type: application/json · Accept: text/event-stream
Authorization: Bearer <ku.a.d(false)>        (manual — bypasses fh.a)
body: StartConversation{systemMessage, userMessage}
reader: okhttp3.sse.RealEventSource + EventSourceListener
frame: data: AiTutorConversationMessage{content, conversationId, finishReason}
end: finishReason == "Stop" (natural) | "Length" (truncated)
```

Behavioural properties: content is appended to the **last** assistant message; `conversationId` arrives in the payload
and must be captured; there is no `retry:` handling, no `Last-Event-ID` resume and no heartbeat logic. Closing the
connection aborts client rendering; whether it aborts server generation is `BACKEND_ONLY` (`A-08`).

Lesson/code context is composed **client-side** into the two message strings (`Q-92` closed).

## 3. Code execution

| Channel | Endpoint | Auth | Status |
|---|---|---|---|
| REST sync | `POST /v1/code/runfiles`, `POST /v1/code/{id}/runfiles` | `fh.a` (if annotated) | proven |
| Socket stream | `wss://api.mimo.org/v1/run/socket` | `Sec-WebSocket-Protocol: authorization.bearer.<token>` | handshake proven, **frame schema not recovered** |

Socket facts: single `WebSocketListener` (`pg.a`), wrapper `com.getmimo.ui.inputconsole.a`; no reconnect, no ping/pong,
no close-code handling; the token is read once at connect time and never refreshed mid-socket (`Q-40` blocked, `A-04`
unknown).

## 4. Realtime third channel — Pusher

Channel authorization is app code (`remote.pusher.a`, manual Bearer); the WSS protocol and event names are SDK-internal
(`Q-89` partially closed). The app does not implement Pusher framing.

## 5. Output surfaces

`ConsoleOutput` / `browserOutputDeferred` exist in the interactive state model; no producer was found for the former in
the interactive branch (`A26` not recovered) and the latter's composable consumer was not isolated (`A27` partially
closed). Executable lessons consume the execution output through their own view-model.

## 6. What a rebuild would need that Mimo does not evidence

Frame schemas for both streaming channels, resume semantics, cancellation acknowledgement, quota limits, and the
server's prompt handling. All are outside client evidence and are recorded as such, not guessed.
