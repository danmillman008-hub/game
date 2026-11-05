# M07 — controlled answer experiment (distilled)

**Hypothesis:** a real correct answer causes a distinct runtime path and a
`lesson_progress` Room row; a wrong answer does not.

**Prepared state:** fresh AVD, original APK installed, no prior answer, lesson
151403 opened via measured XML tap targets, Frida attached at the lesson moment
(stage 6). Correct/wrong labels come verbatim from shipped
`assets/lessons-en/tracks/tutorial-904.json` (`correctLetter='D'`), never from
guesswork. One operation at a time, each bracketed by a UI dump and a root
SQLite `.backup` snapshot.

| operation | measured result |
|---|---|
| `tap 398 1017` (`Q`, wrong) | `Try again`, Q disabled; no DB change; no native `V/W/X` hook |
| `tap 683 1017` (`D`, correct) | `Correct!`, `D O G`, `dog_yawn`; no DB change yet |
| `tap 540 2238` (`Continue`) | next lesson (code editor); **new row** `151403` with `tries=1, attempts=1, in_queue=1` |

Stage-6 hooks at 13:20:08: `c.U() → c.H(1,1) →
LessonProgressRepository.createLessonProgress(LessonBundle(lessonId=151403,
lessonIndex=1, tutorialTitle=Discovering HTML and Tags)) → c.e0() →
LessonProgressQueue.storeLessonProgress → isSolvedCorrectly()=true →
c.f0(false,true) → c.N()`.

**Verdict:** `VERIFIED_RUNTIME` for the persistence chain. Native validator
dispatch for validatedInput/selection/fillTheGap answers remains `UNKNOWN`.
`SERVER CONFIRMED = 0`.
