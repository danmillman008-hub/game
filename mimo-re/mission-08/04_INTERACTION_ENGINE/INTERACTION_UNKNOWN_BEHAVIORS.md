# Phase 4.15 — Unknown and partially-known interaction behaviour

| ID | Item | What is known | What is missing | Status |
|---|---|---|---|---|
| A21 | `WRONG`-gated modules after a partial verdict | partial emits `jm.n`, not `jm.o`; no "wrong" block is shown | whether `ModuleVisibility.WRONG` also triggers on partial | open |
| A22 | semantics of the six `jm.o` booleans | the type is `(CharSequence, Z×6)` and is built in `d0` | which flag is hint / solution / retry / AI-tutor | open |
| A23 | `mm.b.E0` pass-through | returns a stored boolean from state flow `E0` | which interaction types use it at runtime | open |
| A24 | delay before verdict | `kotlinx.coroutines.a.g` delays before `when(result)` | duration and its source | open |
| A25 | `qm.f` reachability | `qm.f` is built at exactly one site (validated input) | whether executable lessons can also produce partial verdicts | open |
| A26 | `Output` at runtime | `ConsoleOutput`/`TableOutput` exist, `te.f` builds tables | any producer of `ConsoleOutput` inside the interactive branch | open |
| A27 | `browserOutputDeferred` consumer | the literal exists in `base.c.i0`; browser output is a deferred flow value | which composable collects it | open |
| A28 | MultipleChoice vs SingleChoice trigger | both graders delegate to `km.f.b`; state holders differ | the condition that selects one over the other | open |

## Deliberate non-claims

* No interaction type is claimed to be **server-graded**. No network call exists in any grading path that was read.
  The executable lesson (Phase 10) may still be hybrid — `postCodeExecutionResult` implies a result arriving from
  outside — but that is not an interactive-lesson grader.
* The visibility *evaluator* is claimed to be the renderer by elimination (parser cannot know the verdict, module has
  no evaluation method, view-model holds the verdict). No composable body was read, so the exact gate is `INFERRED`.
* `jm.o` flag order is not guessed. A wrong guess here would silently corrupt every feedback reconstruction, so it is
  left open rather than filled in.
