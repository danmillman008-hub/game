# Mission 7 — Light and Dark Theme

## Result (VERIFIED_STATIC — **Q-103 closed**)
The resource table contains **configuration variants**, and the decoder reports per-entry configs. Colour tokens
with a `night` configuration: **116**.

Example night-overridden tokens: `$ic_badge_backend__0`, `$ic_badge_backend_professional__0`, `$ic_badge_css__2`, `$ic_badge_frontend__0`, `$ic_badge_frontend_professional__0`, `$ic_badge_frontend_professional__1`, `$ic_badge_fullstack__0`, `$ic_badge_python__1`, `$ic_badge_python__2`, `$ic_badge_python_dev__0`, `$ic_badge_python_dev__2`, `$ic_badge_python_dev_professional__0`

## Interpretation
- If night variants exist for tokens, the app supports a dark theme via resource qualification (`values-night`),
  not via a runtime switch class (no `AppCompatDelegate.setDefaultNightMode` was found).
- The editor theme is separate (Phase 12.77), so a dark app theme does not imply a dark editor.

## Limit
Layout-level theme attribution (which screens opt into which theme) is not recovered; it needs layout decoding.
