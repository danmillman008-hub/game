# Mission 6 — Local State

## Scope
Everything the app keeps across process death.

## Method
Room schema + DataStore/SharedPreferences search + `savedInstanceState` usage in lesson VMs.

## Findings (VERIFIED_STATIC)
1. **Room**: progress + completion markers only (40).
2. **Preferences/DataStore**: session token, onboarding flags and remote-config overrides are the
   categories found by name; no lesson-level state is written there (no lesson id key appears in
   preference usage).
3. **In-memory only**: parsed lesson AST, verdict state, attempt counters, code-block lists. `base.c` keeps
   these in fields; a process death loses the in-progress exercise (only the initial `H(0,0)` row
   survives, which is why an abandoned lesson still appears).
4. **Instance state**: the four lesson fragments restore view state (e.g. typed text), not the AST.

## Evidence labels
1–2 **VERIFIED_STATIC** for the categories; exact preference keys **NOT_RECOVERED** (obfuscated strings
inside `SharedPreferences` calls were not enumerated).

## Open questions
`Q-67` preference key inventory; `Q-68` whether a mid-lesson rotation loses answers.

## Reproduction
`grep -rn 'getSharedPreferences\|dataStore' /tmp/dad/com.getmimo.core.session*.java | head`
