# Phase 4.9 — End-to-end interaction traces (real content, real methods)

Each trace starts from a real lesson document in the shipped asset set and ends at a state mutation. Method names
without a recovered original are shown as `class.method`.

## Trace 1 — ValidatedInput (code block with a blank)

1. **Content** — `assets/lessons-en/tracks/tutorial-1001.json`, chapter 0, lesson 0: `contentType=interactive`,
   `interactiveContent` contains a `<code version="2" codelang="html" …>` element whose `<interactions>` carries a
   validated-input interaction with a correct-answer string.
2. **Parsed module** — `te.a` → `LessonModule.Code(c, d, Output, ModuleVisibility, CodeLanguage, name)` with the
   interaction attached.
3. **Rendered** — validated-input screen (`InteractiveLessonValidatedInputFragment`), text edited in an EditText.
4. **User input** — `qm.d.j0(String)` on every change; empty text disables `RunButton.State`, non-empty enables it.
5. **Answer** — `qm.d.S` holds the raw text; `qm.h(correctAnswer, prefix, suffix)` holds the expected answer and the
   uneditable text around the gap (built in `qm.d.E` with `Math.max/min` on the gap indices).
6. **Grade** — `setupViews`: normalise both sides with `qm.i.a`; `qm.g`/`qm.e`/`qm.f` as in `GRADING_IMPLEMENTATION.md`.
7. **Verdict** — `base.c.Z(iq.w)` → `onValidatedInputExecuted` → `V`, `W` (with `b0`), or `X`.
8. **Feedback** — `jm.m` / `jm.n` / `jm.o` emitted; wrong path consults `data.local.a.f()` (hard-mode tutor intro).
9. **State** — `H()` builds `LessonProgress`, `e0()` persists it, `f0()` records the completion event, lesson id is
   emitted on the correct/partial paths only.
10. **Next action** — `U()` advances; `M()` resets; retry leaves the attempt counters to the next `H()`.

## Trace 2 — Selection (multiple choice)

1. **Content** — a `<selection iscode="…">` block with `<item correct="…">` children counts 4,751 in the en corpus.
2. **Parsed module** — `te.e` → `LessonModule.Selection(List<SelectionItem(correct, text)>)`, no visibility field.
3. **Rendered** — `selection.a` builds `nm.e(viewItems, textCodeItems, textCodeItemsUnmodified)`; items are `cn/d`
   with a random UUID each.
4. **User input** — tapping an item toggles `cn/d.b`, `j0(nm.e)` recomputes `RunButton.State` and
   `InteractionKeyboardButtonState` and publishes the state.
5. **Grade** — `nm.b.E0`: count equality, then per-item `selected == correct`; joined texts are recorded with `b0`.
6. **Verdict** — `base.c.Y(correct)` → `onLessonRun`.
7. **Feedback / state** — identical to Trace 1 from step 8.
8. **Why no partial** — the selection grader returns a boolean; there is no third value to express "partially right".

## Trace 3 — FillTheGap

1. **Content** — `<code>` with `<interactions>` of fill-the-gap kind; `<option correct="…">` texts.
2. **Parsed** — `Interaction$FillTheGap(List<Option(correct,text,int,int)>, isDefault)`.
3. **Rendered** — `fillthegap.a`, state `im.a`.
4. **Grade** — `im.d.E0`: size equality then index-wise text equality.
5. **Verdict** — `Y(correct)`.
6. **Difference from Selection** — the answer is positional (index-wise), the selection answer is set-like
   (flag-wise), and only fill-the-gap joins with a space.

## Trace 4 — Spell

Same as Trace 3 with `spell.a` / `pm.f` / `pm.b.E0` and an **empty** join separator, i.e. the answer text is the
concatenation of the letters, which is what a spelling check needs.

## Trace 5 — MultipleChoice / SingleChoice

`km.c.E0` and `om.d.E0` both delegate to `km.f.b(List)` over `sm.a(selected, correct)` items; single-choice differs
only by its state holder. Join separator `", "`.

## What these traces are not

They are static reconstructions. No lesson was executed, no tap was simulated, and no verdict was observed at
runtime. Every step is labelled in `INTERACTION_METHOD_MAP.csv` with the instruction-level evidence behind it.
