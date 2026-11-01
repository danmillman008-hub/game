# Phase 4.3 — `ModuleVisibility`, implemented

## 1. It is an enum of three states, not a boolean

```java
enum ModuleVisibility { ALWAYS("always"), CORRECT("correct"), WRONG("wrong") }
```

(The `static` initialiser in `ModuleVisibility` builds exactly these three constants with these payload strings.)

## 2. What that means

Visibility is **verdict-dependent**, not static:

| Value | Rendered when |
|---|---|
| `ALWAYS` | always |
| `CORRECT` | only after the lesson's answer was judged correct |
| `WRONG` | only after the answer was judged incorrect |

So a module can be a *feedback* module: the "well done" paragraph and the "try again" paragraph can both exist in the
parsed list and only one becomes visible. This also explains `visible-if="always"` in the DSL, and why the parser
vocabulary only ever mentions `always` (the other two values are engine state, not authoring state — see §4).

## 3. Why `Selection` has no `ModuleVisibility` (answer, not guess)

Three independent facts agree:

1. `LessonModule$Selection` declares only one field (`ArrayList c` of `SelectionItem`) — no visibility field.
2. `te.e`'s entire string pool contains no `visible-if` token, while `te.a`, `te.b`, `te.c`, `te.d`, `te.g` all do.
3. `Interaction$Selection` (the content-side interaction) also carries no visibility.

The structural consequence is an invariant: **the graded module cannot be hidden by content**, because there is no
mechanism to hide it. Every other module type can be gated; the selection cannot.

## 4. Who evaluates visibility — evidenced boundaries

| Candidate owner | Finding |
|---|---|
| the module itself | it *stores* the value and exposes no evaluation method (no method on `ModuleVisibility` other than `values`/`valueOf`) |
| the renderer | consumes the value; the Compose layer decides to draw or not — no `if (visibility)` was found inside the parser or the repositories |
| the view-model state | the verdict is a view-model fact (`base.c.C` boxed Boolean, `jm.*` feedback states), and `CORRECT`/`WRONG` can only be known there |
| the parser | only produces `ALWAYS`-style values from `visible-if`; it cannot know a verdict at parse time |

Therefore: **parse time resolves `always`; render time resolves `correct`/`wrong` against the view-model verdict.**
The renderer is the evaluator, the view-model is the source of truth, and the module is a passive carrier. This is
`VERIFIED_STATIC` for the data model and the vocabulary, `INFERRED` for the exact composable that applies the gate
(no composable body was read in this phase).

## 5. Open

* whether `WRONG`-gated modules appear for a *partial* verdict (the partial path never renders a "wrong" block — it
  emits `jm.n`), question **A21**;
* whether the hard-mode module list (`hardModeLessonModules`) uses visibility differently — question **A20** (Phase 3).
