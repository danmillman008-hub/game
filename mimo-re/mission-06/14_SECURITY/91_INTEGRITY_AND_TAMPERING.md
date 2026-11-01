# Mission 6 — Integrity and Tampering

## Scope
Whether the app has integrity/tamper/root checks — and the fact that **this APK is itself tampered**.

## Findings (VERIFIED_STATIC)
1. Signer is **not** Mimo's: `META-INF/YOUAREFINISHED.RSA`/`.SF` (942 B, sha256 `c93e9a58…`).
2. A mod-tool watermark string appears in **11,543** constant strings
   (`"Smob - Mod obfuscation tool v4.6 by Kirlif'"`).
3. Injected application class `com.getmimo.App extends bin.ghost.yrf` (+ `libyrf.so`) is foreign.
4. Therefore: (a) no claim about Mimo's own integrity protection can be made from this artifact;
   (b) any behaviour of `bin.ghost`/`libyrf.so` must not be attributed to Mimo (mission-06 U-18 stays
   **BLOCKED** as a *Mimo* question — it is a repack question).
5. Play Integrity / SafetyNet classes: **not found** in the recovered batch (`Q-141`).

## Consequences for this mission
Every finding in mission 6 is scoped to *this modified 9.35 artifact*. Content, DSL, runtime and API
conclusions are unaffected (they live in Mimo's own code); code-integrity and injected-SDK conclusions are
not reproducible against a stock build.

## Evidence labels
1–3 **VERIFIED_STATIC**; 4–5 as marked.

## Reproduction
`unzip -l "/tmp/apk/Mimo_9.35 (1).apk" | grep META-INF`
