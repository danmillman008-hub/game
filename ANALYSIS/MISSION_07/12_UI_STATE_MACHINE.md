# MISSION 07 — 12 UI / NAVIGATION STATE MACHINE (MEASURED)

**Status:** `VERIFIED_RUNTIME`. Every transition below comes from an
`adb shell uiautomator dump` XML in `ANALYSIS/RUNTIME/MISSION_07/UI/` and a
recorded `input tap x y` in `EXPERIMENTS/STAGE*_TRACE.txt` or
`EXPERIMENTS/S*_ANSWER_LOG.jsonl`. Tap coordinates are node centres computed
from `bounds`, never guessed. `SERVER CONFIRMED = 0`.

## Deterministic onboarding chain, stage 4 (`S4NAV-01..26`, run `42028049247`)
```
01 Get started                    (540,2049)
02 Let's go                       (540,2228)
03 Do better at work or school    (540,1365)
04 Build something useful         (540,1324)
05 Continue                       (540,2226)
06 Employed                       (540,1407)
07 Software, IT & data            (540,1376)
08 Continue                       (540,2228)
09 path container                 (540,1265)   [no visible change]
10 progress bar                   (540,186)    [no visible change]
11 action_bar_root                (540,1200)   [no visible change]
12 Web apps                       (540,1362)   <-- path choice
13 Continue                       (540,2068)
14 Continue                       (540,2226)
15 Continue                       (540,2228)
16 Casual (5 min)                 (540,1206)
17 path completion estimation     (540,1278)   [no visible change]
18 Continue                       (540,2228)
19 Yes, turn on (reminder)        (540,2070)
20 Allow (notifications)          (540,1316)
21 Mostly on the computer         (540,1362)
22 Continue                       (540,2226)
23 Skip (create account)          (971,199)
24 Welcome to your learning path  (607,1604)
25 Continue (slide 151410)        (540,2238)
26 LESSON 151403: Guess the letter / _ O G / Q R D / Continue  <-- experiment
```
Stage 2 (`NAV-08..31`) took the `Data science` branch and reached a different
first lesson chain: Python intro slides (`NAV-25..27`) then selection lesson
123420 (`NAV-28..30` "What do computers use variables for?" / two text options
/ `Submit`). Stage 3 with a `Web apps` preference reached a JavaScript
snippet lesson (`S3NAV-34`). This **adaptive onboarding** is why M07 replaced
M05's blind 24-tap replay with XML measurement plus shipped-answer
classification.

## Lesson state machine (measured states)
```
SLIDE (no interaction) --Continue--> U()/H()/e0() -> lesson_progress row
                                      -> next slide
WEBVIEW_LETTER --tap wrong Q--> "Try again", Q disabled, R/D enabled
               --tap correct D--> "Correct!", "D O G"   [shipped JS; stage 5]
               --Continue--> next lesson
SELECTION_TEXT --tap option--> bottom Submit container becomes enabled
               --Submit--> correct/wrong feedback        [UNKNOWN, not measured]
```
`UI/S4_D1_AFTER_WRONG_OPTION.xml` clickable node bounds:
`Q [343,963][454,1071] enabled=false`, `R [485,963][595,1071]`,
`D [630,963][737,1071]`, bottom CTA `[47,2178][1033,2299]`.

## Offline restart chain (stage 4, `S4OFFNAV-01..08`)
```
01 Skip (971,199)  02 Skip (540,1236)  03 Skip (971,199)
04 Practice optional, HTML Basics 1 (540,1923)
05 Start practicing (540,1381)
06 btn_lesson_close (73,204)      <-- generic chooser artefact, recorded
07 Start practicing (540,1381)
08 <html> WebView content (580,1508)
```
`m07_answer_driver.py` now forbids `btn_lesson_close` / `btn_lesson_report`
coordinates so an experiment cannot be aborted that way.

## Screens not reached by M07
chapter completion screen, "Correct!" native feedback screen after a
submitted selection, leaderboard, streak modal, purchase/paywall, account
creation. These are `UNKNOWN`, not inferred. M05 run `42005358012`
`LESSON-WRONG-01.xml` did show `Try again` after a wrong `Q` with `Q` disabled
and `R`/`D` enabled — consistent with the stage-4 measurement.
