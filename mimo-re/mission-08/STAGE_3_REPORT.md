# Mission 8 — Stage 3 Report (lesson engine)

**Status:** `substantially_complete` (13/13 deliverable files) · **Base:** Stage 2 commit `fc11272` · **2026-11-01**

## The discovered fact that changes the picture

Lesson content is **not Markdown and not a bespoke DSL**: it is an HTML document with custom elements, carried as the
`interactiveContent` string of a lesson. Walking 18,272 English lessons gives a closed tag census
(`text` 235,973 · `code` 58,806 · `p` 29,193 · `content` 22,810 · `option` 22,465 · `selection` 4,751 · `webview` 841 ·
`img` 139 …), and the seven parsers' string pools name exactly the tags and attributes in that census.

## Parsers

| Parser | Own vocabulary | Emits |
|---|---|---|
| `te.a` | `code`, `content`, `interactions`, `codelang`, `name`, `version`, `visible-if` | `LessonModule.Code` |
| `te.b` | `database`, `tables`, `table` | `Database` |
| `te.c` | `p`, `img`, `code`, `selection`, `src`, **`xml_parse_error_module`** | dispatcher + `Image` |
| `te.d` | `p`, `span`, `strong`, `br` | `Paragraph` |
| `te.e` | `selection`, `item`, `iscode`, `correct` | `Selection` |
| `te.f` | `table`, `row`, `header`, `content`, `data` | table structure |
| `te.g` | `webview`, `style`, `unlock`, `embedded`, `interaction` | `Webview` |

The **parse-error module** is the error path Phase 2 could not find: malformed markup becomes a module, not an
exception.

## Model

`LessonModule` (abstract, `Parcelable`) has exactly **six** variants — `Code`, `Database`, `Image`, `Paragraph`,
`Selection`, `Webview`. Five carry `ModuleVisibility`; **`Selection` does not**, and `visible-if` is absent from
`te.e`'s vocabulary, which is a structural guarantee that the graded module cannot be hidden by content. A lesson
carries **two** module lists (`lessonModules`, `hardModeLessonModules`).

## View-model

`InteractiveLessonBaseViewModel` (`base.c`): 33 methods. Recovered: `initialiseViewModel` (39 insns),
`lessonSolvedCorrectly` (162, `solutionFeedbackCorrect`), `lessonSolvedCorrectlyWithPartialMatch` (202,
`validated_input_execution_correct_partial_match`, `user_input`), `lessonSolvedIncorrectly` (130),
`showWrongFeedbackBlock` (148, `solutionFeedbackWrong`), `lessonSolvedAndProceedToNextLesson` (130),
`updateTabbedCodeViewWithBrowserOutput` (215, **`browserOutputDeferred`**), `isAiTutorUnlimited` (91),
`createInteractiveAiTutorInfo` (283); plus two unnamed analytics emitters (`lesson_reset`,
`lesson_interaction_delete`). The largest method (`O`, 616 insns, takes `LessonContent`) has **no recovered name**.

## Handed to Phase 4

Grading inputs are `qm.f` (first parameter of `W`), `user_input` and `validated_input_execution_correct_partial_match`
are the property keys, and `Selection` items carry `correct`. Phase 4 must read `W`/`V`/`X` bodies and the
`ModuleVisibility`/`Output` types.

## Limits

Six items stay open (A15–A20) with named blockers. Nothing in this stage claims a rendered lesson or a graded answer:
all labels are `VERIFIED_STATIC`.
