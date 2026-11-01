# Mission 6 — Phase 0 Baseline Report

## Scope
Establish, before any new extraction, exactly what artifact is being analysed, in what environment,
with which tools, and which prior-mission outputs are intact — and record two integrity findings that
change how every conclusion in this mission must be read.

## Method
`git rev-parse`/`status`/`ls-tree`; SHA-256 and MD5 over the APK; per-DEX SHA-256; zip entry census;
APK signature block inspection; tool presence probe (`shutil.which` + `--version`); re-run of both
prior test suites; cross-check of the mission-05 decompilation manifests against the decompiled tree.

## Sources (all local, reproducible — see `tools/build_baseline.py`)
| Artifact | Value |
|---|---|
| Repository / branch | `danmillman008-hub/game` · `arena/ecb8af07-game` |
| Starting commit | `10a96006186e0a83d25cc0662db205d7e6fd3aac` (= expected) |
| Worktree | clean |
| APK | `Mimo_9.35 (1).apk`, 142,353,499 bytes |
| APK MD5 / SHA-256 | `f9cef2d8029e59da3668ec1c18e21566` / `48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a` |
| Zip entries | 14,398 (assets 10,564 · res 3,177 · org 489 · META-INF 65 · google 63 · lib 12) |
| DEX files | 12 (`classes.dex` 16.2 MB … 8 stubs of 1,096 bytes) |
| Package identity | `com.getmimo` · versionName `9.35` · versionCode `1792759685` · compileSdk 37 |
| Decompiled Java | 3,284 files, 8.5 MB, in `/tmp/dad` (outside Git) |
| Extracted resources | 3,179 files (`AndroidManifest.xml`, `resources.arsc`, `res/**`) in `/tmp/res` |
| Mission-04 files | 399 tracked · Mission-05 files | 61 tracked (both unmodified) |

## Findings — baseline

1. **Environment (see `ENVIRONMENT_INVENTORY.json`)**
   Present: python 3.11.2, androguard 4.1.4, pytest 9.2.0, lxml, `nm`, `readelf`, `objdump`, `strings`, `git`, `unzip`.
   Absent: `java`, `javac`, `jadx`, `apktool`, `baksmali`, `smali`, `aapt`, `aapt2`, `dot`, `mmdc`, `adb`, `emulator`.
   Consequence: no smali-grade verification, no aapt2 — **but** androguard's AXML/ARSC readers replace
   aapt2 for the manifest, XML configs and the resource table (demonstrated in Phase 9/14), and DAD
   replaces JADX for Java-level reading. Runtime remains impossible.
2. **Prior missions intact.** `git ls-tree HEAD` shows mission-04 (399 files) and mission-05 (61 files);
   `git status --porcelain` is empty at session start and no file under either directory was touched.
3. **Test baseline.** mission-04 suite **23 passed**; mission-05 artifact suite **44 passed**
   (`EXISTING_TEST_RESULTS.md`).
4. **Decompilation still matches the APK.** The 12 DEX SHA-256 values recomputed here are recorded in
   `DEX_HASHES.json`; the decompiled tree contains 3,284 `.java` files, consistent with mission-05's
   3,323-class run plus the mission-06 batches added during this mission.

## Findings — two integrity facts that reframe the mission

**I-1. The APK is a repackaged, re-signed build — not the official Play artifact.**
`META-INF/` contains `YOUAREFINISHED.RSA` / `.SF` (942-byte certificate, SHA-256
`c93e9a5885c9ca0426aebd2b7a783240…`), i.e. the archive was signed by a third party, not by Mimo.
Labelled **VERIFIED_STATIC**. Consequence: every finding in missions 4–6 describes *this artifact*.
Nothing in this mission may be presented as "what the Play Store build does" without that caveat.

**I-2. The DEX carries a post-build obfuscation/protection pass.**
The literal `"Smob - Mod obfuscation tool v4.6 by Kirlif'"` is embedded in **11,543 instruction sites**
across `classes.dex` (tool: instruction scan; see `tools/extract_parser_grammar.py` discussion and the
mission log). A protection layer that rewrites the app's superclass is also present:
`com.getmimo.App extends bin.ghost.yrf`, with `libyrf.so` backing `bin.ghost.YRF`
(`execute()`, `logo()`, `dpToPx()` native methods).
Interpretation: **the `bin.ghost` package and `libyrf.so` are most likely injected by the
modification/protection tool rather than authored by Mimo** — a repackager that adds a base
`Application` subclass to intercept lifecycle and can show a blocking dialog.
Label: **INFERRED_HIGH**. Counter-hypothesis (kept open, `Q-01`): Mimo could ship a third-party
anti-tamper SDK in the same package namespace.

## Evidence labels
Artifact identity, hashes, entry counts, tool availability, prior-mission integrity, test results:
**VERIFIED_STATIC**. The *purpose* of `bin.ghost`/`Smob`: **INFERRED_HIGH**. Official-vs-repackaged
provenance: **VERIFIED_STATIC** for "re-signed"; **UNKNOWN** for "who produced it and why".

## Limitations
No comparison against a Play-signed APK is possible here (only one APK exists in the workspace), so the
delta between official and repackaged code cannot be measured. This is the single most significant
caveat of the whole mission.

## Open questions
`Q-01` provenance of `bin.ghost`/`Smob`; `Q-02` whether the mod altered lesson/grading code (no
mechanism to diff without an official APK); `Q-03` whether the native dialog is dormant.

## Reproduction
```bash
/tmp/venv/bin/python tools/build_baseline.py            # writes all six JSON artifacts here
unzip -l "/tmp/apk/Mimo_9.35 (1).apk" | head            # signature + entry census
git -C /home/user/game rev-parse HEAD                    # 10a9600…
```
