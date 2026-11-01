# Mission 6 — AI Tutor State and Streaming

## Scope
Client-side state machine while a reply streams.

## Method
`AiTutorViewModel` fields and the five `ui.aitutor.*` helper classes.

## Findings (VERIFIED_STATIC)
```
IDLE → SENDING (user message appended locally) → STREAMING (content appended per event)
     → DONE (finishReason Stop) | TRUNCATED (finishReason Length) | FAILED (onFailure)
FAILED → IDLE on retry (manual only)
```
- Rendering is incremental: each event's `content` is appended to the last assistant message.
- `finishReason` is the only terminator; there is no token counter on the client.
- Quota display is refreshed by the count endpoint, not by the stream.

## Evidence labels
**VERIFIED_STATIC** for states/transitions present in code; the labels are descriptive names for
behaviour, not Mimo identifiers.

## Open questions
`Q-97` whether a stopped stream leaves a partial message rendered.

## Reproduction
`grep -n 'finishReason\|isStreaming' /tmp/dad/com.getmimo.ui.aitutor.AiTutorViewModel.java | head`
