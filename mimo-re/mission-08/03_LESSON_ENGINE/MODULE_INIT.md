# Phase 3.10 — Module initialisation

## Sequence

```
initialiseViewModel(LessonProgress)      base.c.e0   39 insns
   → module list handed to the engine    base.c.O   616 insns  (LessonContent → state)
   → code blocks prepared                base.c.K   39 insns   (also stores progress in memory)
   → AI tutor context built              base.c.G   283 insns
```

## Code blocks

`LessonModule.Code` carries a `CharSequence` (the code) and a `List` (secondary). `initialiseCodeBlocks` therefore
has to decide *which* of the parsed code modules become editable panes. The class
`com.getmimo.ui.lesson.interactive.base.InteractiveLessonBaseViewModel$initialiseCodeBlocks$1$1` exists in the
decompiled tree, confirming the suspended inner step.

## Ordering constraint (proven by data, not by code reading)

`Selection` is the only variant **without** `ModuleVisibility`, and `visible-if` is absent from `te.e`'s vocabulary.
So the answer-bearing module cannot be hidden. This is a structural constraint on initialisation: visibility is
applied to content modules, never to the selection being graded.

## What is missing

* the assignment of the five boolean flags during initialisation (needs `f0` + `O` read line by line);
* whether `initialiseCodeBlocks` or `storeLessonProgressInMemory` is which behaviour (ambiguous mapping);
* the `hardModeLessonModules` selection rule (Phase 5).
