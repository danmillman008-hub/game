# MISSION 06 — DEEP CLIENT REVERSE ENGINEERING

**APK:** `48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a` (unchanged) · `SERVER CONFIRMED = 0` · classification on every finding.

---

All algorithms below are `VERIFIED_STATIC` from named DEX methods. Pseudocode is a faithful
restatement of bytecode, not invented specification. Raw disassembly:
`EVIDENCE/VALIDATION_RAW_DISASM.txt`, `EVIDENCE/ALGORITHM_DIGEST.txt`,
`EVIDENCE/PATH_STATE_DISASM.txt`, `EVIDENCE/DISASM/*.smali.txt`.

### A. `InteractiveLessonBaseViewModel.Y(Z)` @10954996
```
fun onLessonRun(isCorrect: Boolean) {
  if (runInProgress.value == TRUE) return
  runInProgress.value = TRUE
  viewModelScope.launch {
      if (isCorrect) lessonSolvedCorrectly() else lessonSolvedIncorrectly()
      nextPage.value = lessonBundle.chapterIndex
      runInProgress.value = FALSE
  }
}
```
### B. `V()` lessonSolvedCorrectly @10953356 (162 insns)
```
awaitBrowserOutput()
wrongLatch = FALSE; attempts++
updateSolutionFeedback()
val tries = if (wrongLatch == TRUE) 0 else 1
createLessonProgress(tries, attempts)
storeLessonProgressInMemory()
showSolutionFeedbackCorrect(); sound.playCorrect()
analytics.track(isSolvedCorrectly, …); emitLessonId(lessonId); cleanupFiles()
```
### C. `X()` lessonSolvedIncorrectly @10954596 (113 insns)
```
attempts++; wrongLatch = TRUE
createLessonProgress(0, attempts)
storeLessonProgressInMemory()
showWrongFeedbackBlock()
```
### D. `LessonProgressRepository.createLessonProgress` @10063916
```
completedAt = Instant.now()
if (completedAt < startedAt) log("CreateLessonProgress: completedAt date (…) is before startedAt date (…)")
LessonProgress(lessonId=bundle.a, completedAt, startedAt, tries, tutorialId=bundle.e,
   tutorialVersion=bundle.v, trackId=bundle.f,
   publishSetVersion = tracksRepository.currentPublishSetVersion(),
   attempts, isPracticeProgress=bundle.B, inQueue=true)
```
### E. `LessonProgress.isSolvedCorrectly()` @9913532
`return tries >= 1` — **M05 correction** (not `attempts >= 1`).
### F. fillTheGap `Lim/d.E0()` @12834200
```
selected = state.placedTokens.filter{ it.placed }
ok = selected.size == state.correctTokens.size &&
     selected.indices.all{ selected[it].text == state.correctTokens[it].text }
answer = selected.filter{ it.text.isNotBlank() }.joinToString(" ")
baseVM.b0(answer); baseVM.Y(ok)
```
### G. selection `Lkm/f.b(List)` @13243392
`return list.all { it.selected == it.isCorrect }`
### H. spell `Lpm/b.E0()`
```
typed = state.c; expected = state.b
ok = typed.size == expected.size && typed.indices.all{ typed[it].text == expected[it].text }
answer = typed.filter{ it.text.isNotBlank() }.joinToString("")
baseVM.b0(answer); baseVM.Y(ok)
```
### I. validatedInput normalizer `Lqm/i.a(String)` @14172860
```
lower = s.toLowerCase(Locale.US)
out = ""
for (c in lower) if (c.isLetterOrDigit() || c in KEEP) out += c
return out
KEEP = ['<','>','(',')',':','{','}',',','.']
```
### J. validatedInput result `setupViews$2.invokeSuspend` @10985684
```
user = vm.S; expected = vm.R.a
result = if (normalize(user) != normalize(expected)) Lqm/g
         else if (user == expected)                Lqm/e
         else                                      Lqm/f(user, expected)
vm.b0(user); vm.Z(result)
```
`onValidatedInputExecuted$1` @10939224: `delay(300)` then
`Lqm/e → V()`, `Lqm/f → b0(f.h) + W(f)`, `Lgm/g → X()`.
### K. executable `q.I()` @10912932
```
user   = codeFiles.map{ it.content }
answer = executable.files.map{ it.solvedContent }
return if (user == answer) state else errorState + IncorrectSolutionException
```
### L. `LessonProgressQueue.updateCorrectAnswersCount()` @10056956
```
queued = repo.getAllLessonProgressInQueue()
correct = queued.count{ it.isSolvedCorrectly() }
_answersInChapter.emit(AnswersInChapter(correct, queued.size))
```
### M. Offline gate `NetworkUtils.a()` @10174360 and
`LessonProgressRepository.postUnsyncedLessonProgress`
```
if (!androidNetworkUtils.a()) {
  log("No internet connection, not posting unsynced lesson progress")
  throw NoConnectionException
}
launch { POST unsyncedRows }
```
### N. DSL dispatch `Lte/c.b(String)` @14378108
```
parser = XmlPullParserFactory.newInstance().apply{ isNamespaceAware = true }.newPullParser()
parser.setInput(StringReader(html))
for each START_TAG:
  p→Lte/d.a | code→Lte/a.a | selection→Lte/e.a | img→Lte/c.a |
  webview→Lte/g.a | database→Lte/b.a | html/body/unknown→skip
```
### O. Path-map state `GetPathMapState$invoke$3` @10129608
```
for tutorial in sections (excluding Challenge):
  state = if (tutorial.isCompleted) Lvn/d0 Completed
          else if (no local progress && !sequential prerequisite met) Lvn/e0 Locked
          else if (pro/key gate fails) Lvn/h0 UnlockedButNoKeys
          else Lvn/g0 Unlocked
  chapterItem = Lvn/d(id,title,isCompleted,isCompletedInHardMode)
final Lvn/n(track, sectionStates, selectedIndex, dialogs, …)
```
The exact boolean combination in step `state` is `UNKNOWN` — shown here as the closest
faithful shape with explicit uncertainty, not a substitute rule.

## Algorithms explicitly NOT reconstructed
Scoring/XP/coins/keys/streak/daily-goal award formulas and thresholds; full unlock
predicate; `SingleChoice`/`MultipleChoice`/`Reveal` dispatch; `W()` partial-match feedback;
remote code execution; any server-side algorithm. `SERVER CONFIRMED = 0`.
