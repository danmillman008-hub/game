# Mission 5 — AI Tutor Architecture

## Scope
What is statically knowable about the in-app AI tutor: the message model, how prompts are assembled
from lesson context, the quota check, the endpoints, and the paywall gate.

## Method
Enumerated `com.getmimo.data.model.aitutor.*`, `com.getmimo.data.source.local.aitutor.*` and every
`*AiTutor*` analytics property class; joined them with the API catalogue rows whose path contains
`aiTutor`; read `AiTutorRepository$sendMessage$2` for the transport shape.

## Sources
| Evidence | Symbol |
|---|---|
| Message model | `data.model.aitutor.{AiTutorConversationMessage, FollowupMessage, FinishReason, StartConversation, AiTutorialConversationMessageCount}` |
| Prompt types | `data.source.local.aitutor.{SystemMessage$Interactive, SystemMessage$Executable, UserMessage$InstantPrompt$ExplainError, ...$ExplainInteractiveMistake}` |
| Transport | `data.source.local.aitutor.AiTutorRepository$sendMessage$2` |
| Endpoints | `POST /v1/aiTutor/conversations`, `GET /v1/aiTutor/conversations/messages/count` (`evidence/API_CATALOG_V2.csv`) |
| Gate | `analytics.properties.upgrade.ShowUpgradeDialogType$AiTutor`, `UpgradeSource$AiTutor` |

## Findings
1. **Prompt construction is typed, not templated at the call site** (VERIFIED_STATIC). A conversation
   start is `StartConversation(systemMessage, userMessage)`; the system message has two specialisations
   corresponding to the two lesson engines — `SystemMessage$Interactive` and `SystemMessage$Executable`.
   The user message has *instant prompts*: `ExplainError(errors, code)` and
   `ExplainInteractiveMistake(...)`, i.e. the "explain my error" affordance is a distinct, structured
   prompt rather than free text.
2. **Quota is server-side** (VERIFIED_STATIC). The client only reads a counter:
   `GET /v1/aiTutor/conversations/messages/count` → `AiTutorialConversationMessageCount`. No local
   quota arithmetic was found, so the free/paid message allowance is authoritative on the server
   (**INFERRED_HIGH**; the numeric allowance is **UNKNOWN** — mission-04's "5 free messages" is not
   reproduced by any constant in this build's decompiled code).
3. **Streaming**: `sendMessage` is a suspend function whose continuation generic is the response type
   (a conversation-message model). Whether the transport is SSE/chunked could not be established from
   the traced path; `okhttp3` `ResponseBody` streaming helpers appear elsewhere in the app but not in
   the traced AI path. Labelled **UNKNOWN**, not "SSE".
4. **Finish reason** is modelled (`FinishReason`), so the client distinguishes normal completion from
   truncation/refusal — evidence that the backend returns an explicit terminal reason.
5. **Gate**: two dedicated analytics property families (`ShowUpgradeDialogType$AiTutor`,
   `UpgradeSource$AiTutor`) prove the AI tutor is a **paywall surface** integrated with the
   subscription model, and that entering it from different origins is tracked separately.
6. **Analytics**: `Analytics$AiTutorInteraction$PromptType` enumerates prompt kinds;
   `AiTutorInteractionSource$InteractiveLesson` / `$ExecutableLesson` record where the tutor was
   opened; the literal `ask_ai_tutor` exists among the app's snake_case event/property strings.

## Evidence labels
- Model inventory, typed prompts, quota endpoint, finish reason, paywall properties: **VERIFIED_STATIC**.
- "Quota enforced server-side": **INFERRED_HIGH**.
- Streaming protocol, model name, prompt text, token limits, retention: **UNKNOWN**.

## Limitations
The repository's main class was not emitted by DAD (only its `sendMessage` lambda was recovered), so
request/response field mapping is incomplete. Deliberately **not** attacked: no attempt to observe
live conversations, no account use, no prompt-extraction (RULE 5).

## Unresolved
`U-15` streaming protocol; `U-16` free-message allowance; `U-17` whether conversations persist across
app restarts (no Room table found — see `11_LOCAL_DATA_AND_SYNC/`).

## Reproduction
```bash
ls /tmp/dad | grep -i aitutor
grep -n 'aiTutor' evidence/API_CATALOG_V2.csv
grep -n 'private final' /tmp/dad/com.getmimo.data.model.aitutor.StartConversation.java
```
