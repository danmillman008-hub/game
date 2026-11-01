# Mission 7 — UI Architecture (complete)

## Two rendering technologies coexist (VERIFIED_STATIC)
- **View/Fragment**: the lesson flow (4 interaction fragments + base VM), onboarding pager, code editor
  (`PartiallyEditableEditText`, `CodingKeyboardView`), WebView modules.
- **Compose**: newer surfaces use `ui.compose.*` (components, `SpanCopier` for styled text), which is why no XML
  layout exists for some screens.

## State
MVVM + coroutines. Lesson VMs are imperative controllers (`H/U/V/W/X/Z/a0`), the rest use `StateFlow`/`Flow`.

## Rendering pipeline for a lesson
```
lesson document → te.* parsers → LessonModule models → base.c state (blocks, slots, visibility)
      → fragment binds → SpannableStringBuilder / PartiallyEditableEditText / WebView
      → user event → Z(verdict) → state → re-bind
```

## Why this architecture matters
Because blocks are plain span-composed text rather than a view per node, the lesson UI has **one scrollable page
per lesson** and no adapter-based recycling: cheap to implement, but it caps lesson size and makes per-block
animations manual.
