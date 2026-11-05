# MISSION 06 — ORIGINAL SHIPPED SAMPLES

`MANIFEST.json` lists 11 **byte-exact copies of original APK members** with source APK path,
byte size and SHA-256. Nothing was authored, rewritten or reconstructed. The APK is unchanged.

| File | APK member | Why |
|---|---|---|
| `ORIGINAL_fillTheGap.json` | `assets/lessons-en/tracks/tutorial-4589.json` | `fillTheGap` + `validatedInput` lesson |
| `ORIGINAL_validatedInput.json` | same tutorial (second copy) | explicit validatedInput example |
| `ORIGINAL_selection.json` | `tutorial-2307.json` | `<selection>` and `correct="true/false"` |
| `ORIGINAL_webview.json` | `tutorial-3144.json` | `<webview version=…>` |
| `ORIGINAL_hardModeContent.json` | `tutorial-2346.json` | `hardModeContent` alternate modules |
| `ORIGINAL_executableContent.json` | `tutorial-3042.json` | full `executableContent` incl. `solvedContent` |
| `ORIGINAL_assets_lessons-en_tracks_tracks.json` | `tracks.json` (v753) | full shipped track index |
| `ORIGINAL_assets_lesson-webview.js` | `assets/lesson-webview.js` | WebView↔native bridge |
| `ORIGINAL_assets_lesson-webview-fonts.js` | `assets/lesson-webview-fonts.js` | injected font loader |
| `ORIGINAL_assets_testdata_127-0-1.html` | `assets/testdata/127-0-1.html` | shipped `spell` interaction fixture |

Smallest matching English v753 tutorial was chosen per interaction type. The v753 English
curriculum sample set contains no `spell` tag, so the shipped testdata fixture is used for
that interaction; it is still an original APK member. `assets/testdata/test-tracks.json`
is a `publishSetVersion=52` fixture, not the shipped v753 curriculum — it is not presented
as such here. See `../MISSION_05/SAMPLES/README.txt` for M05's additional samples.
