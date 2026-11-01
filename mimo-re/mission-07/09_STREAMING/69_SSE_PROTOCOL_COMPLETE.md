# Mission 7 — SSE Protocol

```
POST /v1/aiTutor/conversations            (or /{conversationId})
Content-Type: application/json
Accept: text/event-stream
body: StartConversation{systemMessage, userMessage}

< HTTP/1.1 200, text/event-stream
  event frames → data: AiTutorConversationMessage{content, conversationId, finishReason}
  …
  terminal: finishReason == "Stop" | "Length"
```

## Behaviour recovered from code
- reader = `okhttp3.sse.RealEventSource` + `EventSourceListener`; each frame's `content` is appended to the last
  assistant message;
- `conversationId` arrives in the payload (not a header) and must be captured for the next call;
- `Length` means truncated-by-limit, `Stop` means natural end;
- no `retry:` handling, no `Last-Event-ID` resume, no keep-alive logic of the app's own.

## Unknowns
Event `type` field vocabulary, cancellation semantics (does closing the call abort generation?), and behaviour on
mid-stream disconnect (`Q-97`).
