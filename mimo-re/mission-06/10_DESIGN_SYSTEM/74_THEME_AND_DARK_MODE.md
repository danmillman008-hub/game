# Mission 6 — Theme and Dark Mode

## Scope
Whether a dark theme exists and how theming is applied.

## Findings
1. The ARSC contains `values-night`-class configurations only if such variants exist; **the config list
   could not be enumerated** (Phase 9.71 Method), so dark-mode resource presence is **NOT_RECOVERED**
   (`Q-103`).
2. Firebase Remote Config's 3 defaults include no theme flag by name (Phase 11.77).
3. No programmatic theme switch class (e.g. `AppCompatDelegate.setDefaultNightMode`) was found in the
   recovered batch (`VERIFIED_STATIC` for the batch).
4. The code editor has **its own** theme mechanism independent of app theming (71).

## Evidence labels
As marked. This is a genuine gap: a reconstruction should **assume light-only** only after checking with a
proper resource dump.

## Open questions
`Q-103`, `Q-130` system-dark behaviour.
