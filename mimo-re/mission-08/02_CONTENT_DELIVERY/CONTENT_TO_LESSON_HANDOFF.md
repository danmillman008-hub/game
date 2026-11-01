# Phase 2.11 — Content → lesson-engine handoff

This is the join the brief requires: a *representative* lesson traced from its content source to the lesson-engine
entry point.

## 1. The representative lesson

`assets/lessons-en/tracks/tutorial-1001.json` → `tutorial.id = 1001`, `version = 31`, `type = course`,
`codeLanguage = html`, one chapter, whose first lesson carries
`contentType`, `images[]`, and **`interactiveContent` — a single String**.

Structural keys only; no lesson text is reproduced here.

## 2. The path (each step evidenced)

```
UI request (caller not yet traced)
   → DefaultTracksRepository.getTrackWithChapters / getTutorial        [tracks.c.e / tracks.b.c]
   → provider interface ye.f
        ├── ye.b (AssetManager): base "lessons-<locale>/tracks", file "/tutorial-1001.json"
        └── ye.d (live preview): "/live_preview/tracks/tutorial-1001.json"
   → tracks.b.c(InputStream) → BufferedReader(8192) → String          [tracks.b.c, 29 insns]
   → kotlinx.serialization JSON (hb0.b)                                [tracks.b.a, sget hb0/k]
   → model construction: Tutorial / Chapter / Lesson / LessonContent
   → LessonContent.Interactive(lessonModules, hardModeLessonModules)   [fields proven]
   → DSL text is handed to the parser dispatcher te.c                  [ctor injection into tracks.b]
   → InteractiveLessonBaseViewModel.initialiseViewModel                 [base.c.e0, Stage-1 mapping]
```

## 3. What is proven vs inferred

| Claim | Status |
|---|---|
| content is read from `assets/lessons-<locale>/tracks/tutorial-<id>.json` | **VERIFIED_STATIC** (strings + path join + asset tree) |
| the file is parsed as JSON into `Tutorial`/`Chapter`/`Lesson` | **VERIFIED_STATIC** (model fields match JSON keys exactly) |
| the DSL text is the `interactiveContent` string of a lesson | **VERIFIED_STATIC** (JSON key present; `LessonContent.Interactive` carries `lessonModules`) |
| the parser dispatcher receives that text | **INFERRED** — the loader holds `te.c`, but the call site that passes the string was not read in Phase 2 |
| the base view-model opens the lesson | **INFERRED** — method name recovered with HIGH confidence, body not yet read |

## 4. Why this is enough to start Phase 3, and not enough to claim it

The handoff point is now a single, named seam: **`LessonContent.Interactive.lessonModules` → `te.c` →
`InteractiveLessonBaseViewModel.initialiseViewModel`**. Phase 3 must read those three bodies and turn the three
`INFERRED` rows into `VERIFIED_STATIC` (or report why not).
