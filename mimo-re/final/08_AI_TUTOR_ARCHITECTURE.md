# 08 — AI tutor: prompt, context, transport, quota

## 1. What it is
A chat assistant embedded in the lesson player as a bottom sheet (Compose:
`AiTutorBottomSheetKt`, `AiTutorViewsKt$ChatView`, `ChatWritingIndicator`). It is opened from
the lesson chrome (interactive lessons and the coding keyboard's `AiTutorButton`), and it is
gated by remote config `feature_flag_ai_tutor_android` (V) and by Pro entitlement with a
freemium allowance (V).

## 2. Transport (V)
| Property | Value |
|---|---|
| Path | `POST /v1/aiTutor/conversations` (also `/v1/aiTutor/conversations/…` for follow-ups) |
| Headers | `Authorization: Bearer …`, `Content-Type: application/json`, **`Accept: text/event-stream`** |
| Streaming | SSE — responses arrive token-by-token into `AiTutorConversationMessage(conversationId, content, finishReason)` |
| Finish reason | `FinishReason` enum = `Stop` \| `Length` (V: the only two values) |
| Model | **UNKNOWN** (server-side; nothing in the APK names a provider or model) |

Two `FinishReason` values are an important detail: the client must handle a **truncated**
answer (`Length`) as a normal outcome — that is why `ChatMessage` has an `id` and the UI has a
"writing" indicator with an error template (`ai_tutor_error_message_template`).

## 3. Prompt architecture (V structure, I ordering)

Two system-message shapes (V: class names + prompt fragments in
`com.getmimo.data.source.local.aitutor`):

```
Interactive(pathName, lessonContext)      # markup lesson: injects what the learner SEES
Executable(pathName, instructions, expectedAnswer)
                                          # code lesson: injects the file name, the authored
                                          # instructions and the EXPECTED SOLUTION
```

Both wrap their payload in **`{{{ … }}}` fences** (V literal), and both share one behavioural
preamble whose sentences are about acting as a tutor, giving hints and concise explanations,
and staying encouraging (V fragments). The user side has three shapes:

```
UserMessage(codeFiles)                        # the learner's current code
UserMessage$InstantPrompt$ExplainError(codeFiles, error)
UserMessage$InstantPrompt$ExplainInteractiveMistake(codeFiles, wrongAnswer)
```

So the "instant prompts" are **pre-composed user messages**, not system instructions: tapping
"Explain this error" sends a normal user turn that contains the console error and the code.
That is the cleanest idea in this subsystem and it is directly portable.

```
StartConversation(systemMessage, userMessage)
AiTutorConversationMessage(conversationId, content, finishReason)
AiTutorialConversationMessageCount(userMessageCount)
```

### Inferred wire format
```json
{ "systemMessage": {"type":"interactive","pathName":"…","lessonContext":"…"},
  "userMessage":  {"type":"executable","codeFiles":[{"name":"index.html","content":"…"}]} }
```
(I: field names come from the Kotlin `toString` templates; the actual JSON envelope uses the
same field names because kotlinx.serialization is configured on the same classes — not
independently provable.)

## 4. Context engineering — what the model gets and what it does not

| Context | Interactive | Executable |
|---|---|---|
| Lesson prose / markup | ✅ `lessonContext` (whole visible lesson) | ➖ only `instructions` |
| File names | ✅ `pathName` | ✅ `pathName` |
| Learner code | ➖ (interactive has no editor) | ✅ `codeFiles` |
| Expected solution | ❌ | ✅ `expectedAnswer` |
| Console error | via `InstantPrompt$ExplainError` | via same |
| Wrong answer | via `ExplainInteractiveMistake(wrongAnswer)` | ❌ |
| Learner profile / level / streak / language | ❌ not in these messages | ❌ |
| Prior conversation | conversation-scoped on the server (`conversationId`) | same |

Consequences worth noting:
* **The tutor can see the answer** in executable lessons. Its instructions therefore have to
  enforce "hints, not solutions" in the prompt layer, not by withholding data (V: preamble
  asks for hints; the expected answer is present — so a prompt-injection attempt
  ("ignore previous instructions") is the obvious attack, mitigated only server-side).
* **No personalisation**: the model does not receive the learner's track, level, streak or
  locale. Mimo chose lesson-context-only, which keeps prompts cacheable and privacy-cheap but
  produces generic tutoring.

## 5. Quota & monetisation (V)
```
GetAiTutorFreemiumUsage  (interactor `interactors.aitutor.*`)
State.usedMessages / State.isPro / State.nextHint
UpgradeModalPageData$UnlimitedAiTutor ; ai_tutor_upgrade_title / _message_count / _button
hard_mode_ai_tutor_intro_free_bubble: "This is a Pro feature, but your first 5 questions are
                                       on the house."
hard_mode_ai_tutor_intro_pro_bubble : "Enjoy unlimited tutor access thanks to your Pro plan!"
```
⇒ free tier = 5 messages, counted **server-side per user** (the count is returned by the
usage endpoint, not stored in Room — V: no ai-tutor table in the schema), Pro = unlimited.
`State.nextHint` implies a **hint ladder** (first hint, second hint — matching
`PromptSuggestions.FirstHint/SecondHint`), i.e. progressive disclosure instead of a raw chat.

## 6. Failure and degraded states (V)
`State = { loading, messages, usedMessages, isPro, isFeatureDisabled, blockingError,
           isMessageLoading, offline, nextHint }`
* `isFeatureDisabled` ← remote config flag off;
* `offline` ← network observer (`Error observing network state: ` literal) → the sheet shows
  `ai_tutor_offline_description`;
* `blockingError` ← hard failure with `ai_tutor_error_message_template`;
* `isMessageLoading` ← distinct from `loading`: per-message streaming state.

## 7. Analytics (V)
`AiTutorInteraction$PromptType = AskInChat | GiveMeAHint | Custom`,
`AiTutorInteractionSource = InteractiveLesson | ExecutableLesson`, plus open/close events
(`trackAiTutorOpened` / `trackAiTutorClosed` in `ExecutableLessonViewModel`).
So the product measures which entry point converts to an upgrade, per lesson type.

## 8. Hard-mode tutor variant (V)
`HardModeAiTutorIntroBottomSheetKt$HardModeAiTutorAnimatedSpeechBubble` + copy
`hard_mode_ai_tutor_intro_header` ("Almost there! Let's work through this together."),
`…_body` ("I'll help you think it through, not think for you: …"), `…_cta` ("Let's chat"),
`hard_mode_intro_do_not_ask`. Hard-mode lessons surface the tutor **at the moment of failure**,
with a "do not ask again" suppression — a pattern that increases perceived support without
increasing free-text usage.

## 9. Transfer decision for Konkur (summary; full matrix in §19)

| Element | Verdict |
|---|---|
| SSE streaming chat + per-message streaming state | **Reuse** (cheap, familiar) |
| Instant prompts as pre-composed user messages (`ExplainError`, `ExplainInteractiveMistake`) | **Reuse** — highest value, lowest cost |
| System-message context injection with `{{{ }}}` fences | **Reuse** |
| Passing `expectedAnswer` into the prompt | **Exclude** — Konkur answers must never enter a prompt; use a solver + grader instead |
| Free-quota `5 messages + Pro unlimited` | **Adapt** — Iran: quota per *subject* + no hard paywall (payment friction) |
| Prompt suggestions ladder (FirstHint/SecondHint) | **Reuse** |
| Per-lesson-type analytics on tutor usage | **Reuse** |
| English-only prompt strategy | **Exclude** — Persian prompts must be authored and evaluated; expect 2–3× failure rate on formula notation and RTL code mixing |
