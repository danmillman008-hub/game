# Phase 4.1 — The interaction modules, complete

## 1. Two layers, one model

| Layer | Type | Members |
|---|---|---|
| content model (what the lesson file declares) | `Interaction` (abstract `Parcelable`, one `boolean a`) | `Selection`, `ValidatedInput`, `FillTheGap`, `Spell` |
| UI model (what the screen can present) | `LessonInteractionType` (abstract `Parcelable`, `a(): String`) | `FillTheGap`, `InteractiveWebView`, `MultipleChoice`, `None`, `Reveal`, `Selection`, `SingleChoice`, `Spell`, `ValidatedInput` |

The UI layer has **nine** members; the content layer has **four**. Three UI members exist without a content
counterpart (`MultipleChoice`, `SingleChoice`, `Reveal`), and `InteractiveWebView` maps to a *module* (`Webview`)
rather than to an `Interaction`. This is why the interaction count differs between missions: both numbers are right,
for different layers.

## 2. Fields per interaction model (machine-extracted)

```text
Interaction(boolean a)                                  // shared flag, inherited by all four
Interaction$Selection(boolean, int, int, List)          // two ints: selection bounds; List: items
Interaction$ValidatedInput(boolean, int, int, String, String[])   // String: correct answer; String[]: alternates
Interaction$FillTheGap(List, boolean)                   // List<Option(correct,text,int,int)>
Interaction$Spell(int, int, boolean)                    // two ints: word/gap geometry
```

`Option` carries `(correct: Boolean, text: CharSequence, c: Int, d: Int)`; `SelectionItem` carries
`(correct: Boolean, text: CharSequence)`. **Neither stores the user's answer** — the answer lives in UI state
(`cn/d`), so grading state is not part of the parsed content model.

## 3. Per-type rendering and state owner

| Type | Parser | ViewModel | State | Grader |
|---|---|---|---|---|
| Selection | `te.e` | `selection.a` | `nm.e(viewItems, textCodeItems, textCodeItemsUnmodified)` | `nm.b.E0` |
| FillTheGap | `te.a` (`interactions`) | `fillthegap.a` | `im.a` | `im.d.E0` |
| Spell | `te.a` | `spell.a` | `pm.f` | `pm.b.E0` |
| ValidatedInput | `te.a` | `validatedinput.b` → `qm.d` | `qm.h` + `qm.d.S` | `InteractiveLessonValidatedInputFragment.setupViews` |
| MultipleChoice | `gm.h` mapping | `km.a`/`km.c` | `km.e` | `km.f.b(List)` |
| SingleChoice | `gm.h` mapping | `om.a`/`om.d` | `om.f` | `km.f.b(List)` |
| InteractiveWebView | `te.g` | `webview.a–d` | `jm.k(String, WebviewType)` | `mm.b.E0` (pass-through) |

`gm.h.a(List)` is the mapper that converts parsed modules into UI items and carries the four literal type names
`interactive_webview`, `fill_the_gap`, `spell`, `selection` — direct evidence for the mapping.

## 4. Item identity

`cn/d` (the UI option item) is `(a: String text, b: boolean selected, c: boolean correct, d, e)` and is constructed
with a **random UUID** (`java.util.UUID.randomUUID()` in its `(int,String,boolean)` constructor). Answer identity is
therefore per-render, not content-derived — an item index cannot be used as a stable key across renders.
