# Phase 3.1 — From content structure to parsed model

```
tutorial-<id>.json
  └─ "tutorial": { id, version, type, isNew, codeLanguage, title, …, chapters[] }
        └─ chapter { id, title, type, lessons[] }
              └─ lesson { id, title, contentType, images[], hardModeSelected,
                          interactiveContent: String  ← the HTML-with-custom-elements document }
                            │
                            ▼  DefaultTrackLoader (tracks.b) reads the file, parses JSON
                     LessonContent.Interactive(lessonModules, hardModeLessonModules)
                            │   ← at this point the document is still a string
                            ▼  parser dispatcher te.c + six element parsers
                     List<LessonModule>   (Code | Database | Image | Paragraph | Selection | Webview)
                            ▼
                     InteractiveLessonBaseViewModel (base.c) → rendered screen
```

## Structural match (proof that the model mirrors the JSON)

| JSON key | Model field | Class |
|---|---|---|
| `id`, `version`, `title`, `isNew`, `codeLanguage`, `showInTrack`, `iconBanner` | same names | `Tutorial` |
| `chapters[]` | `chapters` | `Tutorial` |
| `id`, `title`, `type`, `lessons[]` | same names | `Chapter` |
| `title`, `id`, `contentType`, `images[]`, `hardModeSelected` | same names | `Lesson` |
| `interactiveContent` (string) | not stored as a field — it is *parsed* into `lessonModules` | `LessonContent.Interactive` |
| `publishSetVersion`, `tracks[]` | same names | `TracksJson` |

The one asymmetry is the important one: **`interactiveContent` has no model field**. The string is consumed by the
parser at load time, and what survives into the view-model is the module list. The DSL is therefore never stored
parsed on disk — re-parsing is unavoidable per lesson open (and explains why `DefaultTrackLoader` holds the parser).

## Hard mode

`hardModeLessonModules` sits next to `lessonModules` in `LessonContent.Interactive`. A lesson carries **two module
lists**, selected by the hard-mode flag (`Lesson.hardModeSelected`, and the preference keys recovered in
`data.local.a`: `hasSeenHardModeIntro`, `setHardModeEnabled`, `hasPendingHardModeIntro`). Phase 3 records the
structure; Phase 5 owns the selection rules.
