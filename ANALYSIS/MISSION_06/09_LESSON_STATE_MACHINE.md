# MISSION 06 — DEEP CLIENT REVERSE ENGINEERING

**APK:** `48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a` (unchanged) · **branch** `arena/aebb90b7-game` · `SERVER CONFIRMED = 0`  
Evidence: `EVIDENCE/DISASM/*.smali.txt`, `SCHEMAS/METHOD_CATALOG_MIMO.json`,
`CALL_GRAPHS/*.json`, `METHOD_DOSSIERS/*.md`. Classification on every finding.

---

## Verified states and transitions
Diagram `DIAGRAMS/04_lesson_execution.mmd` and `06_progression_state_machine.mmd`.

### Session lifecycle (`VERIFIED_STATIC`)
```
ChapterActivity
 → InteractiveLessonFragment (LessonBundle Parcelable)
 → InteractiveLessonViewModel.E(content,bundle)
 → Lgm/h.a(modules) : LessonInteractionType
 → base/c.O(content,bundle)  initialiseViewModel
 → N() reset RunButton + keyboard states
 → per-interaction ViewModel.E(content)  configure interaction state
 → user input (EditText / token taps / option taps / code editor)
 → Fragment.E0()  run handler
 → base/c.Y(isCorrect)
 → onLessonRun$1 → V() | X()
 → H(tries,attempts) → e0() → Room
 → e LiveData = lessonBundle.b → next lesson / chapter end
```

### Guard states (`VERIFIED_STATIC` field evidence)
| Field | Type | Meaning |
|---|---|---|
| `f` | `LiveData<Boolean>` | run-in-progress; `Y()` returns early if TRUE |
| `C` | `Boolean?` | wrong-answer latch; FALSE on correct, TRUE on incorrect |
| `d` | `int` | attempt counter (incremented in `V`, `X`, `U`) |
| `M` | `boolean` | `e0()` guard preventing duplicate progress writes |
| `E` | `boolean` | hard-mode / analytics flag |
| `I` | `Instant` | `startedAt` |
| `H` | `String` | last submitted answer text |
| `s`,`t` | `jm/m`,`jm/o` | correct / wrong feedback state |
| `n` | `LiveData<jm/q>` | module list + visibility flag |
| `e` | `LiveData<Integer>` | chapter/next-page index |
| `h` | `MutableSharedFlow<Long>` | emits `lessonId` on solve |

### Retry / reset — VERIFIED_STATIC
`a0()` emits `lesson_reset` analytics with
`lesson_id, tutorial_id, tutorial_version, track_id, attempts, duration`;
reposts `jm/q(list,false)`; calls `M()` and `Q()`; clears code-playground bundle `A`.
`g0()` emits `lesson_interaction_delete`.
`base/c.N()` resets `j`/`k` keyboard LiveData to `InteractionKeyboardButtonState.b`.

### Feedback state machine — VERIFIED_STATIC + VERIFIED_RUNTIME
`V()` → `i0()` browser output → `C=FALSE` → `d++` → `c0()` →
`solutionFeedbackCorrect` + success sound → `f0(isSolvedCorrectly, …)` → emit lessonId →
`I()` file cleanup.
`X()` → `d++` → `C=TRUE` → `H(0,d)` → `e0()` → `d0()` wrong feedback block.
`d0()` consults `S()`, DataStore `a.f()`/`a.p()`, `P()` (AI Tutor unlimited) and stores a
`jm/o` copy. M05 run-004 UI: red "Try again", Q disabled.

### Completion / advancement — VERIFIED_STATIC
`U()` and `onLessonRun$1` post `e = lessonBundle.b`;
`ChapterViewModel` drives chapter-end; `ChapterFinishedViewModel` branches online/offline;
`NonInteractiveLessonFragment` and WebView lessons use `U()` directly.

### Still `UNKNOWN`
- Correct-answer **runtime** screen (M05 never produced one); `UNKNOWN VERIFIED_RUNTIME`.
- `W()` partial-match feedback branch details.
- Full `d0()` boolean combination.
- How a wrong answer followed by a correct one affects `C` at the moment of the final
  submission (static `V()` sets `C=FALSE`; interaction = `INFERRED`).
