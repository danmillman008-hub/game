# MISSION 06 — DEEP CLIENT REVERSE ENGINEERING

**APK:** `48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a` (unchanged) · **branch** `arena/aebb90b7-game` · `SERVER CONFIRMED = 0`  
Evidence: `EVIDENCE/DISASM/*.smali.txt`, `SCHEMAS/METHOD_CATALOG_MIMO.json`,
`CALL_GRAPHS/*.json`, `METHOD_DOSSIERS/*.md`. Classification on every finding.

---

## VERIFIED_STATIC — editor architecture
`Lcom/getmimo/ui/codeeditor/view/b;` = `CodeEditViewModel` (7 votes),
`Lam/o;` = `CodeDiffViewModel`, `Lep/t0;` emits `Lep/b0` events (`Lep/v` code pair,
`Lep/y` highlight list), `Lcom/getmimo/ui/codeeditor/highlight/a;` syntax highlighter,
`Lcom/getmimo/ui/inputconsole/a;` input console,
`Lcom/getmimo/ui/codeplayground/CodePlaygroundActivity;`,
`CodePlaygroundBundle$FromLesson` (referenced by `base/c.Q()`),
`Ldg/a;<clinit>` shipped HTML template:
```
<!doctype html>\n<html>\n<head>\n  <title></title>\n
  <link rel="stylesheet" href="style.css">\n</head>\n<body>\n
  <script src="script.js"></script>\n</body>
```
`assets/lesson-webview.js` / `lesson-webview-fonts.js` injected into `EmbeddedLessonWebView`.
`CodeLanguage` enum covers `BASH, CPP, CSHARP, CSS, CSV, …` with default file names
(`program.cpp`, `program.cs`, `style.css`, `data.csv`, `script.js`, `script.py`).

## VERIFIED_STATIC — file model & selection
`LessonContent$Executable{instructions, preselectedFileIndex, files,
getHasBrowserOutput(), getHasInputConsole()}`;
`File{name, codeLanguage, content, solvedContent}`; runtime `CodeFile{name, content}`.
`preselectedFileIndex` chooses the initially open tab; `q.G/H` handle tab selection.
M05: all 4,024 `executableContent` objects have
`instructions, preselectedFileIndex, hasVisualOutput, files, hints`.

## VERIFIED_STATIC — offline correctness decision
`ExecutableLessonViewModel.I()` @10912932 compares
`codeFiles.map{getContent()}` with `executable.files.map{getSolvedContent()}` using
`ArrayList.equals`. Equal → correct; otherwise `Ldm/h` error state and
`IncorrectSolutionException`. `E()` @10913380 then calls
`createLessonProgress(bundle, startedAt, tries, attempts)`.
⇒ **Shipped `solvedContent` is sufficient for the offline correctness check.**
`VERIFIED_STATIC`, resolving M05's open question.

## VERIFIED_STATIC — hints & browser preview
`q.F(Lym/h, Lzl/z)` (248 insns) handles guided-project hints: for file names
`style.css`, `index.html`, `script.py`, `script.js` it looks up static maps `Lcm/b.a..d`
keyed by lessonId, extracts identifiers, emits `Lep/v` and `Lep/y`.
`q.J(...)` builds `Lbe/n0` analytics with `ExecutableLessonRunResult`, duration from
`Seconds.secondsBetween(startedAt, now)`, attempts and either a dump of all files or
`"Lesson passed"`.
`q.K(...)` = `updateCodeExecutionState` (Orbit MVI intent).
`CreateBrowserOutput$invoke$2` logs `"Can't create WebView output"`.

## Client-side boundary (NOT reconstructed)
Retrofit endpoints `POST /v1/code/runfiles`, `POST /v1/tutorials/{id}/runFiles` exist in
M02 `HTTP_VERBS_RESOLVED.json` (53 endpoints). M06 records only the boundary:
no request/response bodies, no server execution engine, no server-side test harness.
`SERVER CONFIRMED = 0`.

## SQL / HTML / CSS / JS exercises
`LessonModule$Database` + `DatabaseView` render SQL exercises;
`WebviewType` + embedded WebView render HTML/CSS/JS; `hasVisualOutput` controls browser
preview. Which languages go through a local WebView vs a remote runner is `INFERRED` from
`hasVisualOutput`/`getHasBrowserOutput()`; exact routing = `UNKNOWN`.

## Remaining uncertainty
- Whether `q.I()` applies to every executable lesson or only guided-project variants
  (`callers=1`, reducer not fully decoded) = `UNKNOWN`.
- Result/test feedback from any remote runner = `UNKNOWN` (server-owned).
- `Interaction$ValidatedInput.e/f` and hint-test semantics = `UNKNOWN`.
