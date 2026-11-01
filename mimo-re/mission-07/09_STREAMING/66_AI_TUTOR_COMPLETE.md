# Mission 7 — AI Tutor (complete)

## Components (VERIFIED_STATIC)
| Layer | Class | Role |
|---|---|---|
| context model | `SystemMessage$Interactive(a,b)`, `SystemMessage$Executable(a,b,c)`, `UserMessage$Executable`, `UserMessage$InstantPrompt{ExplainError(String,List),ExplainInteractiveMistake(List,String)}` | typed request context; prompt text resolved via `Resources` (`q(Resources)`) |
| transport | `AiTutorRepository.sendMessage$2` | POST + `Accept: text/event-stream` |
| stream parse | `okhttp3.sse.RealEventSource` | append `content` per event |
| state | `AiTutorViewModel` + 5 helpers | IDLE→SENDING→STREAMING→DONE/TRUNCATED/FAILED |
| quota | `AiTutorialConversationMessageCount{userMessageCount}` | display only |
| analytics | `Analytics$AiTutorInteraction$PromptType`, `AiTutorInteractionSource` | typed properties |

## Two prompt families
- **Interactive**: explain a mistake inside an interactive exercise (strings supplied from resources).
- **Executable**: explain an error from a code run (three strings: code/output/error context).

## Persistence
None locally: `data.source.local.aitutor.a` holds no DAO; the conversation lives server-side keyed by
`conversationId` returned inside the stream.

## Correction to Mission 6
Mission 6 said the request contains "exactly two authored strings" and no context. Mission 7 shows the context is
modelled as **typed message objects** (`SystemMessage.*`, `UserMessage.*`) whose text comes from string resources —
so context *is* assembled client-side, but it is not serialised as free text in the DTO we had inspected.
