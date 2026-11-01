# Mission 6 — AI Tutor Context and Prompts

## Scope
What context the client sends to the tutor (system message, lesson context) and who composes the prompt.

## Method
Read of the tutor interactor (`interactors.aitutor.a`) and the view model's message assembly; search for
lesson/code inclusion in the request.

## Findings
1. The request contains exactly two authored strings: `systemMessage` and `userMessage`. There is **no**
   `lessonId`, `code`, `language`, or `context` field in the recovered body type. (VERIFIED_STATIC)
2. `systemMessage` is composed **client-side** by the interactor, so prompt engineering lives in the app,
   not the server (`INFERRED_HIGH` — the composition site was located, its literal text was not fully
   readable through DAD).
3. The tutor cannot, per this contract, see the learner's code unless the client inlines it into
   `userMessage`. Whether it does was not recovered (`Q-92`).
4. No conversation history is replayed as separate messages: continuation is by conversation id, so history
   lives server-side.

## Evidence labels
1, 4 **VERIFIED_STATIC**; 2, 3 **INFERRED_HIGH / UNKNOWN**.

## Open questions
`Q-92`, `Q-95` prompt text; `Q-96` moderation system prompt (none observed).

## Reproduction
`grep -n 'systemMessage' -r /tmp/dad/com.getmimo.interactors.aitutor.a.java`
