# MISSION 07 — 10 CODE EDITOR / WEBVIEW / DSL / EXECUTABLE LESSON BOUNDARY

**Status:** `VERIFIED_RUNTIME` for shipped content, UI and the DSL parser;
`UNKNOWN` for code evaluation and native/JNI boundary. `SERVER CONFIRMED = 0`.

## Shipped executable content (M05 + M07 recheck)
`assets/lessons-en/tracks/tutorial-904.json` lesson 151403 (`HTML`,
`contentType=interactive`) embeds a WebView v2 with:
```js
let correctLetter = 'D';
let letterButtons = document.querySelectorAll('#letterButtons button');
letterButtons.forEach(button => button.addEventListener('click', function() {
  let letter = this.textContent;
  if (letter !== correctLetter) { button.disabled = true; }
  if (letter === correctLetter) {
    result.innerHTML = 'Correct!'; result.style.color = '#046865';
    image.src = 'https://mimo.app/i/dog_yawn.png';
    word.textContent = 'D O G'; …
  } else { result.innerHTML = 'Try again'; … }
}));
```
UI text measured in `UI/S4_C_BEFORE_ANSWER.xml`: `Guess the letter`, `_ O G`,
`Q`, `R`, `D`, `Continue`. After a wrong `Q`: `Try again`, `Q` disabled, `R`/`D`
still enabled (`UI/S4_D1_AFTER_WRONG_OPTION.xml`). **This is a pure WebView JS
state transition** — no native `d0()`/`X()` hook fired, no DB change.

`tutorial-1103.json` lesson 123420 uses
`<selection multiple="multiple"><item value="1" correct="true">To store
information for later use</item><item value="2" correct="false">To display
information on the screen</item></selection>`; `UI/NAV-28.xml` shows both texts
and a text-less bottom `Submit` container `[42,2179][1038,2305]` that is
`enabled=false` until an option is selected.

A generated index of **2,855 shipped selection questions** with their exact
correct/wrong item texts is
`ANALYSIS/MISSION_07/RUNTIME_TRACE/SHIPPED_CONTENT/SELECTION_ANSWERS.json`
(source: ORIGINAL APK `assets/lessons-en/tracks/*.json`, APK SHA recorded in
that file). This index is used by `m07_lesson_plan.py` so the automation never
guesses an answer.

## DSL parser `te.c.b(String)` — `VERIFIED_RUNTIME` (offline session, stage 4)
`Java.choose('te.c')` found a live DI-created parser after app restart; calling
`b()` on it with controlled XML produced:

| input | returned `List<LessonModule>` |
|---|---|
| `<html><body><p>Hello <strong>world</strong></p></body></html>` | `[Paragraph(texts=[Hello , world], visibilty=ALWAYS)]` (size 1) |
| `<p>Intro</p><code version="2" codelang="html" name="index.html" visible-if="always"><content><text value="&lt;h1&gt;Hi&lt;/h1&gt;" /></content></code>` | `[Paragraph(texts=[Intro], visibilty=ALWAYS), Code(content=<h1>Hi</h1>, interactions=[], output=null, visibilty=ALWAYS, language=HTML, name=index.html, collapsibleLines=[])]` (size 2) |
| `<p>Pick</p><selection multiple="multiple"><item value="1" correct="true">Yes</item><item value="2" correct="false">No</item></selection>` | `[Paragraph(texts=[Pick], visibilty=ALWAYS), Selection(selectionItems=[SelectionItem(correct=true, text=Yes), SelectionItem(correct=false, text=No)])]` (size 2) |
| `<foo>a</foo><p>ok</p>` | `[Paragraph(texts=[ok], visibilty=ALWAYS)]` (unknown tags dropped) |
| `<p>unclosed` | `[]` (size 0) |

Runtime module names confirm M06's static module taxonomy: `Paragraph`, `Code`
(with `language`, `name`, `content`, `interactions`, `output`, `visibilty`,
`collapsibleLines`), `Selection`/`SelectionItem`, `Image`. Note the shipped
spelling `visibilty` (sic) in the app's `toString()`.

## Executable / code-editor lesson UI (measured)
Stage 3 (`S3NAV-34.xml`) reached a JavaScript snippet lesson:
`We use let and const to create variables…`, `Tap the snippets below`,
`script.js`, `let&#10;W`, `const`, `constant`; tapping a snippet changed the
editor text to `let&#10;const`. Stage-4 offline `S4OFFNAV-08` tapped
`<html>` inside a WebView. M05 shipped `runtime_matched_executable_lesson_63259.json`
and `ANALYSIS/MISSION_05/SAMPLES/lesson-webview.js` shows the shipped JS only
relays `gesture`, `activity`, `focus`, `height`, `ready` messages — no code
evaluation and no scoring.

## Boundary classification
| Question | Class | Status |
|---|---|---|
| WebView wrong-letter feedback (`Try again`, disable button) | A local (JS) | `VERIFIED_RUNTIME` |
| WebView correct-letter feedback (`Correct!`, `D O G`) | A local (JS) | `VERIFIED_STATIC` (shipped JS); live tap targeted by stage 5 |
| DSL/HTML → module parsing | A local | `VERIFIED_RUNTIME` |
| native `q.I()` equality with `solvedContent` | A local | `VERIFIED_STATIC` (M06); not exercised |
| code execution / output evaluation | **C blocked by condition / E unknown** | `UNKNOWN` — no native or remote evaluation path was instrumented |
| external URL substitution offline (M05 Q-25) | B/D | `UNKNOWN` |
| WebView `addJavascriptInterface` / JS→Kotlin bridge | A or E | `UNKNOWN` (hook not installed) |

A future stage should hook `android.webkit.WebView.addJavascriptInterface`,
`System.loadLibrary`, and the app's JS bridge object before claiming where code
is evaluated. Nothing here asserts a server-side executor.

## Stage 5 — correct WebView letter measured (`VERIFIED_RUNTIME`)
`UI/S5_1_E1_AFTER_CORRECT_OPTION.xml` after `input tap 683 1017`:
`["Hypertext Markup Language…", "On top of HTML…", "Correct!", "D O G",
"dog_yawn", "Q", "R", "D", "Continue"]`. The shipped JS's `Correct!` branch,
the `D O G` word replacement and the `dog_yawn` image are therefore confirmed
on device. `UI/S5_1_F_AFTER_CORRECT_SUBMIT.xml` then shows the next lesson — a
**code editor**: `This is the code editor where we'll write code. Let's jump in
and start coding.`, `Click on <button>Like</button> to add the HTML code …`,
`Tap the snippets below`, `index.html`, `W`, `<button>Like</button>`.
This is a real code-editor boundary UI; whether its snippets are evaluated
locally or remotely remains `UNKNOWN` (no JS-interface/native hook evidence).
Stage 6 installs `android.webkit.WebView.addJavascriptInterface` hooks to
record the bridge object class if one is registered.

## Stage 6 — real fill-the-gap module and RunButton state (`VERIFIED_RUNTIME`)
`TRACES/STAGE6_ONLINE.jsonl` at 13:20:09 shows the lesson **after** the correct
WebView answer being initialised with real shipped HTML:
```
te.c.b(...) -> [Paragraph(..., visibilty=ALWAYS),
  Code(content=<button>, interactions=[FillTheGap(isDefault=true,
       options=[Option(correct=true, text=, startIndex=0, endIndex=8),
                Option(correct=false, text=</button>, startIndex=0, endIndex=0),
                Option(correct=false, text=button, ..., ...)])],
       output=null, visibilty=ALWAYS, language=HTML, name=index.html,
       collapsibleLines=[]),
  Paragraph(texts=[Make sure to pick , <button>, .], visibilty=WRONG)]
gm.h.a(...) -> FillTheGap(interactionTypeName=fill_the_gap)
LiveData: RunButton$State.RUN_DISABLED, InteractionKeyboardButtonState.DISABLED,
          jm.q = LessonOutput(outputItems=[], isVisible=false), jm.g
```
This is a verified local code-editor/fill-the-gap state: options carry
`correct` flags and `startIndex/endIndex` spans, and wrong-only paragraphs are
tagged `visibilty=WRONG`. `WebView.addJavascriptInterface` emitted no event in
the attach window, so the JS→native interface object remains `UNKNOWN`.
