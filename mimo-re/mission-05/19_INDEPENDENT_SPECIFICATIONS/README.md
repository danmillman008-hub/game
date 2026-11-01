# Mission 5 — Independent Specifications (E1 / E2 / E5)

Three specifications written so that a third party can implement the behaviour **without access to
Mimo's code, class names or assets**. They are derived from, and cite, the evidence documents of this
mission; they contain no Mimo content, no decompiled code and no branding (RULE 6, RULE 7).

| Spec | Subject | Inputs |
|---|---|---|
| `E1_CONTENT_FORMAT_SPEC.md` | the lesson content format and its parse contract | `04_CONTENT_AND_DSL/*` |
| `E2_LESSON_RUNTIME_AND_ASSESSMENT_SPEC.md` | lesson execution, submission, grading, feedback timing | `05_LESSON_RUNTIME/*`, `06_ASSESSMENT_AND_EVALUATION/*` |
| `E5_PROGRESS_AND_SYNC_SPEC.md` | progress recording, first-try semantics, offline queue and sync | `09_PROGRESS_AND_GAMIFICATION/*`, `11_LOCAL_DATA_AND_SYNC/*` |

The E-numbering follows the enumeration requested by the mission brief. Each file is self-contained and
states its own assumptions, so the content stands even if the numbering convention differs.
