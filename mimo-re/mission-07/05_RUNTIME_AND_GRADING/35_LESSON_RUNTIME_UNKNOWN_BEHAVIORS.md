# Mission 7 — Lesson Runtime Unknown Behaviours

| # | Behaviour | Status | Missing artifact |
|---|---|---|---|
| 1 | progress-row effect of `a0()` restart on an existing row | UNKNOWN | `ProgressRepository` signature/usage for reset |
| 2 | post-lesson navigation (which screen after `U()`) | NOT_RECOVERED | fragment/activity navigation code |
| 3 | webview interaction callback schema | NOT_RECOVERED | webview bridge class |
| 4 | Rive trigger points inside the lesson | NOT_RECOVERED | UI code referencing `.riv` names |
| 5 | hint mechanism | CLOSED_STATIC (absent) | — |
| 6 | animation timing of feedback | NOT_RECOVERED | UI effect classes (`sonar.*`) |
| 7 | keyboard/focus behaviour of validated input | PARTIALLY (custom view exists) | fragment code |
| 8 | process-death restoration of an in-progress exercise | INFERRED (instance state only) | runtime test |

## Rule applied
None of the above is asserted as behaviour anywhere in Mission 7; they are the honest frontier of static
analysis for the lesson surface.
