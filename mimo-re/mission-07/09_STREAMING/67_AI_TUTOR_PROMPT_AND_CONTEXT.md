# Mission 7 — AI Tutor Prompt and Context

## Structure (VERIFIED_STATIC, types only)
```
SystemMessage : { Interactive(a,b) | Executable(a,b,c) }
UserMessage   : { Executable | InstantPrompt{ ExplainError(String, List) | ExplainInteractiveMistake(List, String) } }
```
Interpretation (INFERRED_HIGH from arity and call sites):
- `Interactive(a,b)` = exercise prompt + learner answer;
- `Executable(a,b,c)` = task + code + observed error/output;
- `ExplainError(String, List)` = error string + stack/output lines;
- `ExplainInteractiveMistake(List, String)` = option/interaction list + learner choice.

## Exact prompt text
`UserMessage$InstantPrompt.q(android.content.res.Resources)` returns a **resource-derived string**, i.e. the prompt
copy lives in `res/values*/strings`. Mission 7 decoded the ARSC (Phase 11) but the specific resource ids are
resolved at runtime from `Resources`, so the literal id is not embedded in the class — exact text is
**NOT_RECOVERED** without a call-site read (`Q-95` stays open).

## What is *not* sent
No course id, lesson id, exercise id, correct answer, attempt history, or conversation history as separate
fields. Any context must be folded into those strings.

## Verified absence
No `lessonId`/`code`/`context` field exists in the request DTO (`StartConversation{systemMessage,userMessage}`).
