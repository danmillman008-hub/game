# Mission 6 — Lesson Rendering Architecture

## Scope
How parsed AST nodes become on-screen elements, using code-visible renderers (no layout inflation
possible without aapt2, so this is the *code* path, not a visual spec).

## Method
Read the four per-type view models and their fragment bindings; traced state objects (`jm.*`, `ym.*`,
`qc.a`, `nm.e`, `pm.f`, `qm.h`); identified span construction.

## Sources
`com.getmimo.ui.lesson.interactive.{fillthegap,selection,spell,validatedinput}.*`, `qm.*`, `jm.*`,
mission-05 `05_LESSON_RUNTIME/RUNTIME_SPEC.md`.

## Findings
1. **Rendering is ViewModel→state→View binding**, not per-node view inflation. The VM builds a list of
   *code blocks* (`ym.j` for plain code, `ym.n` for interactive), where each block carries the source
   text and an optional interaction.
2. **Fill-the-gap and spell** compose their display from `SpannableStringBuilder`: plain segments are
   `qc.a(subSequence)` wrappers, and the *correct* option renders with
   `SpannableStringBuilder(source, option.c, option.d)` — the option's span bounds. The input slot is
   the gap `[previousSlotEnd, option.c)`.
3. **Selection** slices the module source around the interaction offsets into `qc.a` segments and wraps
   them in `nm.e(state, slots, …)`; two parallel lists (options and slots) are kept in sync.
4. **Validated input** renders `qm.h(answer, prefix, suffix)` — the text is split into three pieces so
   the editable middle can be replaced without re-rendering the whole line.
5. **Paragraphs** are the feedback surface (see 29): the first paragraph module with visibility
   `CORRECT`/`WRONG` supplies the feedback text; paragraph inline elements (`a`, `br`, `span`, `em`,
   `strong`) are styling/inline concerns only, with no interaction.
6. **Rive** is present as 59 `.riv` assets plus `librive-android.so`; no code path ties a specific
   `.riv` to a lesson state in the recovered sources (`Q-34`) — animation is UI-level, not lesson-level,
   in everything that was read.
7. **Custom views**: `PartiallyEditableEditText` is the one lesson-specific custom view found; it exists
   to edit only the answer window inside a rendered line.

## Evidence labels
Points 1–5: **VERIFIED_STATIC**. Point 6: **VERIFIED_STATIC** for presence, **UNKNOWN** for usage.
Visual geometry (sizes, colours, spacing) is **NOT RECOVERED** at the lesson level.

## Limitations
No layout XML was inflated; Compose composables inside the lesson flow were not mapped 1:1 (the lesson
UI is largely Fragment+View, but `MainActivity` hosts Compose elsewhere).

## Open questions
`Q-34` Rive usage; `Q-35` whether code blocks are RecyclerView items (adapter not recovered).

## Reproduction
`grep -n 'SpannableStringBuilder' -r /tmp/dad/com.getmimo.ui.lesson.interactive.*.java | head`
