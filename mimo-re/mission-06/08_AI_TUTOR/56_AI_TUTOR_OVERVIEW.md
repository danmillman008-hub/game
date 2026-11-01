# Mission 6 — AI Tutor Overview

## Scope
What the AI Tutor is in this build: entry points, transports, message model and limits — closing
mission-05 U-15.

## Method
Read of `AiTutorRepository`, `ui.aitutor.*` view models, SSE plumbing, quota endpoint, analytics source
enum.

## Findings (VERIFIED_STATIC)
- **Entry point**: lesson-scoped. `AiTutorInteractionSource` is an analytics property carrying where the
  tutor was opened from (lesson/project context), and `ui.lesson.executable.*` references tutor classes —
  so the tutor is reachable from code lessons, not from a global chat tab.
- **Transport**: HTTP POST for starting/continuing a conversation, **SSE for the reply stream**
  (`okhttp3.sse.RealEventSource`, `Accept: text/event-stream`).
- **Conversation model**: `StartConversation{systemMessage, userMessage}`; streamed items are
  `AiTutorConversationMessage{content, conversationId, finishReason}` with
  `FinishReason ∈ {Length, Stop}`.
- **Quota**: `GET …/messages/count` → `AiTutorialConversationMessageCount{userMessageCount}`. The client
  renders the count; no client-side quota enforcement beyond display was recovered.
- The tutor has its **own** repository, not a generic chat service.

## Evidence labels
**VERIFIED_STATIC**. "Not a global tab" is **INFERRED_HIGH** (navigation graph traversal, Phase 10).

## Open questions
`Q-91` which screen hosts it exactly; `Q-92` whether the tutor sees lesson content as context.

## Reproduction
`grep -rn 'text/event-stream' /tmp/dad | head`
