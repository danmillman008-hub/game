# Interactive WebView lesson & activity-result messages

**Mission:** MISSION 06 — deep client reverse engineering, Mimo Android 9.35  
**APK:** `48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a` (unchanged)  
**Method:** Androguard 4.1.4 disassembler over all 12 original `ANALYSIS/_INPUT/classes*.dex`;
real `invoke-*` xrefs; Kotlin inner-class names used to recover R8-renamed class names.  
**Primary bytecode evidence:** `ANALYSIS/MISSION_06/EVIDENCE/DISASM/WebViewLessonViewModel.smali.txt`  
**Corpus:** `SCHEMAS/METHOD_CATALOG_MIMO.json`, `SCHEMAS/OBFUSCATION_MAP.json`,
`SCHEMAS/METHOD_NAME_MAP.json`, `CALL_GRAPHS/`.  
`SERVER CONFIRMED = 0`. No backend reconstruction.

> Classification legend: `VERIFIED_STATIC` = read directly from DEX instructions;
> `INFERRED` = named/behavioural interpretation of verified bytecode; `UNKNOWN` = not recovered.

---

## VERIFIED_STATIC
- `Lcom/getmimo/ui/lesson/interactive/webview/c;` = `InteractiveWebViewLessonViewModel`
  (9 methods: `E()` 57 insns, `Q/S/T()` booleans, `a0()`, `j0(cont)` 75 insns).
- `Lcom/getmimo/ui/lesson/interactive/webview/b;` = `InteractiveWebViewLessonFragment`.
- `WebViewActivityResult` enum constants (from `<clinit>`): `mimo.activity.correct`,
  `mimo.activity.wrong`, `mimo.activity.completed` (M05 counted 217/217/90).
- `assets/lesson-webview.js` + `lesson-webview-fonts.js` are injected into
  `Lcom/getmimo/ui/lesson/interactive/webview/a;` and `EmbeddedLessonWebView`.
- `WebViewType` enum has an `UNLOCK` constant; `Lte/g;->a(XmlPullParser)` maps the
  `<webview ...>` tag attributes `visible-if`, `version`, `style`, `interaction`, `content`.
  It resolves `unlock` / `embedded` / other to `WebviewType.e/d/c/b` and HTML-escapes `#`→`%23`.

### Client-side completion path — VERIFIED_STATIC
`base/c;->U()` (lessonSolvedAndProceedToNextLesson) is called from
`webview/c;->j0(cont)` and
`InteractiveWebViewLessonFragment$goToNextPage$1` (error string
`"Error storing unlock activity lesson progress"`).
`webview/c;->j0` also calls `Lgm/h` interaction-type logic.

## Boundary
`mimo.activity.*` messages are WebView→native events (`lesson-webview.js` `postMessage`
JSON `{documentID, ...}`), **not** server responses. M05 already established the JS only
relays gesture/activity/focus/height/ready. No answer evaluation is performed in JS.

## Remaining uncertainty
- Exact mapping from `mimo.activity.correct|wrong|completed` payload to `Y(true/false)`/`U()`
  = `INFERRED` (call sites exist, full argument decoding incomplete).
- `WebviewType` version/style semantics = `UNKNOWN`.
