# Spec 108 — AI Tutor

## MUST
1. Start: `POST /v1/aiTutor/conversations` with `{systemMessage, userMessage}`.
2. Continue: `POST /v1/aiTutor/conversations/{id}`.
3. Send `Accept: text/event-stream` and consume SSE; append `content` per event.
4. Take `conversationId` from the streamed payload; terminate on `finishReason ∈ {Length, Stop}`.
5. Quota: `GET …/messages/count` → `{userMessageCount}`; display only.
6. Keep no local transcript.

## MUST NOT
- Include lesson/code context in the request (no such field exists).
- Implement client-side quota enforcement.
- Retry automatically on failure (none found).

## GIVEN EVIDENCE
`08_AI_TUTOR/56..62`.
