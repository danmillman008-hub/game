# 05 — Lesson engine and rendering

## 1. From document to pixels

```text
tutorial-<id>.json → ContentRepository → Tutorial/Chapter/Lesson model
   → LessonViewModel(InteractiveLessonBaseViewModel subtype)
   → te.c (dispatcher) → te.a..te.g (7 parsers) → AST
   → renderer → HTML custom elements in a WebView host + native composables
   → interaction surfaces (Stage 4)
```

## 2. Parsers

| Parser | Role |
|---|---|
| `te.a`–`te.g` | seven tag-family parsers sharing one grammar; each accepts a fixed tag set |
| `te.c` | dispatcher choosing the parser per tag/block |

`NUMBER` is declared in the tag enum and accepted by no parser (`Q-31`, closed as a dead tag in this build). Unknown-tag
behaviour is only partly established (`Q-30`, partially closed). Grammar: `mission-07/04_DSL_PARSER_RENDERER`.

## 3. Module variants (6)

Recovered from `04_INTERACTION_ENGINE/SIX_MODULE_VARIANTS.json`. Each variant carries its own grading guard (`E0`):
`nm.b.E0`, `im.d.E0`, `pm.b.E0`, `km.c.E0`, `om.d.E0`, `mm.b.E0` (pass-through). Visibility is governed by
`ModuleVisibility {ALWAYS, CORRECT, WRONG}`; `Selection` has no equivalent field (Stage 4 finding).

## 4. Lesson state machine (recovered methods)

| Transition | Method | Effect |
|---|---|---|
| open | `initialiseCodeBlocks` (`K`) | code blocks initialised for the lesson |
| answer correct | `V` | `d += 1`, progress built with `tries = !(C==TRUE)`, feedback `jm.m` |
| answer partial | `W` | `d += 1`, same shape; feedback `jm.n` (partial) |
| answer wrong | `X` | `d += 1`, `tries = 0`, feedback `jm.o` |
| proceed | `U` | `d += 1`, `tries = (C==TRUE)`, emits next lesson id, stores progress |
| store | `e0` (`storeLessonProgressInMemory`) | outbox write (correction C-15) |

Inner state: `C` = last verdict sane/incorrect flag, `M` = one-shot store guard, `d` = session attempt counter,
`I` = `startedAt`. Three further booleans in the base view-model remain unassigned (`A17`, partially closed).

## 5. Rendering surfaces

* HTML custom elements inside a WebView host for prose/code/markup blocks (not Markdown);
* native composables for interaction surfaces and feedback;
* `Output` renders per variant; `ConsoleOutput` has **no recovered producer** in the interactive branch (`A26`), and
  `browserOutputDeferred` exists in state without an isolated consumer (`A27`).

## 6. Lesson completion and next lesson

Completion of a *lesson* is local: `U` emits the next lesson identifier and stores the progress row. Completion of a
*chapter* is not local (see `07`): the client posts progress and then asks the server. Auto-completing the last lesson
therefore does **not** complete the chapter client-side (`A16`, closed negative).

## 7. Executable lessons

A parallel view-model (`ExecutableLessonViewModel`) uses REST (`POST /v1/code/runfiles`) and/or the socket. Which channel
a lesson uses was not recovered (`Q-39`, genuinely unknown). Grading for executable-type modules is pass-through
(`mm.b.E0`), so a partial verdict is not produced on that path (`A25`, closed negative).
