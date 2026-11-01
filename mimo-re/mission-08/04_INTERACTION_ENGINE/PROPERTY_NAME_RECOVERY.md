# Property-name recovery (new channel, used by Stage 4)

## The technique

Kotlin compiles `Intrinsics.checkNotNullExpressionValue(field, "fieldName")` into
`invoke-static <field>, <const-string "fieldName">, Lkotlin/jvm/internal/h;->j(...)`. R8 removes the field name but
**cannot remove the string literal**, because it is an argument to a runtime check. The literal is therefore an
original **property name** preserved inside the dex.

## Recovered names in `InteractiveLessonBaseViewModel` (`base.c`)

| Field | Type (dex) | Recovered original name | Site |
|---|---|---|---|
| `D` | `LessonBundle` | `lessonBundle` | `K()` |
| `s` | `Long` (boxed) | `solutionFeedbackCorrect` | `V` |
| `t` | `jm.o` | `solutionFeedbackWrong` | `d0`, `X` |
| `i0` (flow) | — | `browserOutputDeferred` | `i0` |
| `O` (parameter) | `LessonContent.Interactive` | `interactiveLessonContent` | `G` |

## Cross-app counts (whole app tree, top hits)

| Recovered name | Occurrences |
|---|---|
| `binding` | 134 |
| `chapterBundle` | 26 |
| `codeHeaderTabLayout` | 20 |
| `codePlaygroundController` | 18 |
| `spell` | 14 |
| `fillTheGap` | 10 |
| `codeViewAdapter` | 9 |
| `mimoAnalytics` | 8 |
| `selection` | 6 |
| `lessonNavigator` | 3 |
| `reportLessonBundle` | 3 |

## Why this matters for Stage 4

The two feedback fields are now **named**: the correct path writes `solutionFeedbackCorrect` (a boxed `Long`, the
lesson id emitted to the flow) and the wrong path reads `solutionFeedbackWrong` (a `jm.o`). That turned two anonymous
fields into explained state and produced correction **C-14** (they are property names, not analytics event names).

## Limits

The channel yields a name only where the compiler inserted a null-check (`!!`, platform types, lateinit reads). It
does not name every field, and it never names local variables.
