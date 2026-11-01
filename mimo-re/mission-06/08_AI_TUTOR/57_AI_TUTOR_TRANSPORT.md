# Mission 6 — AI Tutor Transport

## Scope
Exact request/stream wire behaviour.

## Method
Read of `AiTutorRepository$sendMessage$2` and the SSE event source consumer.

## Findings (VERIFIED_STATIC)
```
first message   POST /v1/aiTutor/conversations           JSON StartConversation{systemMessage,userMessage}
later messages  POST /v1/aiTutor/conversations/{id}      JSON (same envelope)
headers         Content-Type: application/json
                Accept: text/event-stream
stream          okhttp3.sse.RealEventSource → EventSourceListener.onEvent(id,type,data)
                 ← AiTutorConversationMessage{content, conversationId, finishReason}
termination     finishReason == Stop  (or Length = truncated by token limit)
error path      onFailure → envelope d70.b failure; no retry found
```
- JSON body even on the SSE call (POST-with-stream), not EventSource/GET.
- The conversation id comes back **inside the streamed payload**, not in a header, so the client must
  capture it from the first event to continue the thread.

## Evidence labels
**VERIFIED_STATIC**.

## Open questions
`Q-93` event `type` vocabulary (only data payload recovered); `Q-94` keep-alive/retry semantics of the
SSE client.

## Reproduction
`sed -n '1,200p' /tmp/dad/com.getmimo.data.repository.aitutor.AiTutorRepository\$sendMessage\$2.java`
