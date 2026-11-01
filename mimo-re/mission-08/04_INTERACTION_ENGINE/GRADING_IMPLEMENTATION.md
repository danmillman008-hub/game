# Phase 4.4 — Grading, reconstructed from bodies

Every claim below is anchored to an instruction sequence read out of the dex, not to a name.

## 1. The single client-side normaliser: `qm.i.a(String)`

```text
s = input.toLowerCase(Locale.US)
out = for each c in s: if Character.isLetterOrDigit(c) or c in {'<','>','(','),':','{','}',',','.'} keep c
return out
```
The keep-set is literally pushed onto a static `List<Character>` in `qm.i.<clinit>` (char codes 60, 62, 40, 41, 58,
123, 125, 44, 46). Whitespace, quotes, semicolons, `=`, brackets `[ ]` and exclamation marks are dropped.

This is the same `qm.i` recorded in mission-07 as "normaliser" — now its algorithm is known, not just its role.

## 2. ValidatedInput — three-way verdict (`InteractiveLessonValidatedInputFragment.setupViews`)

```text
user      = viewModel.S                 // qm.d.S : String, updated by j0(String)
expected  = validatedInput.a            // qm.h.a : String (correct answer)
nUser     = qm.i.a(user);  nExp = qm.i.a(expected)
if  nUser != nExp           -> qm.g   (INCORRECT)
elif user == expected       -> qm.e   (CORRECT)
else                        -> new qm.f(user, expected)   (PARTIAL)  + viewModel.b0(user)
viewModel.Z(result)         // iq.w
```

`qm.f`'s own `toString` names its two fields: `CorrectPartialMatch(userInput=…, expectedUserInput=…)`.

### Dispatch (`InteractiveLessonBaseViewModel$onValidatedInputExecuted$1`)

```text
delay(...)
when (result) {
  is qm.e -> V()                  // lessonSolvedCorrectly
  is qm.f -> { b0(result.userInput); W(result) }   // …WithPartialMatch
  is qm.g -> X()                  // lessonSolvedIncorrectly
  else    -> NoWhenBranchMatchedException()
}
```
The `else` throw proves `iq.w` has exactly three subtypes at this call site, which matches the three subclasses found
by scanning the dex (`qm.e`, `qm.f`, `qm.g`).

## 3. Selection — boolean verdict (`nm.b.E0`, 177 insns)

```text
state = selectionViewModel.Q (nm.e)
if state.viewItems.isEmpty() -> return
index of first selected item -> count of selected
if selectedCount != correctCount -> false
iterate items: item.selected must equal item.correct
answerText = join(selected item texts, ", ")   -> b0(answerText)
base.c.Y(correct)                              // onLessonRun(boolean)
```
`cn/d.a` is the item text, `.b` is selected, `.c` is correct. Unreachable guards use `Intrinsics.W()` (a
"should never happen" throw), so the loop and the count check are the only real branches.

## 4. FillTheGap (`im.d.E0`, 200 insns) and Spell (`pm.b.E0`, 148 insns)

```text
selected = state.options where cn/d.b == true
if selected.size != expected.size -> false
for i: selected[i].a must equal expected[i].a
answerText = join(selected texts, " ")    // fill-the-gap
answerText = join(selected texts, "")     // spell  (same code, empty separator)
b0(answerText); base.c.Y(correct)
```

## 5. MultipleChoice / SingleChoice (`km.c.E0` and `om.d.E0`, 97 insns each)

Both delegate to `km.f.b(List)` (a pure predicate over `sm.a` items: `selected` vs `correct` flags) and both join the
selected texts with `", "`. `km.f.d(List)` rebuilds the list with an updated flag for display. The two classes differ
only in their state holder (`km.e` vs `om.f`), i.e. single-choice is a constraint on the same engine.

## 6. Reveal / None / InteractiveWebView (`mm.b.E0`, 15 insns)

`Y(state.E0.value)` — the verdict is already a boolean in the state flow; the interaction does not grade, it forwards
a stored result. This is the weakest reconstruction of the six and is marked `MEDIUM` in the ownership matrix.

## 7. What the numbers do to a lesson

`H(int,int) → LessonProgress` calls `LessonProgressRepository.createLessonProgress(bundle, I: Instant, int, int)`.
`I` is the only `Instant` field of the view-model (set when the lesson opened), so the two ints are the counters that
become `attempts` and `tries`. `LessonProgress.isSolvedCorrectly()` is `tries >= 1` — proven by reading its body, so
**`tries` is the success counter and `attempts` the total**; completion is decided by `tries`, not by `attempts`.

## 8. Ownership summary

Client-side for every type examined: no network call appears in any grading path. The only hybrid is the executable
lesson (Phase 10), where the run result is produced outside the view-model.
