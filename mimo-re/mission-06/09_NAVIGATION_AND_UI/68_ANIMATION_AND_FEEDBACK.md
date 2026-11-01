# Mission 6 — Animation and Feedback

## Scope
Motion and haptic/visual feedback tied to learning actions.

## Method
Asset census (59 `.riv` files, Rive runtime), view/lottie usage, haptics search, lesson VM side effects.

## Findings (VERIFIED_STATIC)
1. **Rive** is the animation system: 59 `.riv` assets + `librive-android.so`. No Lottie was found.
2. No lesson-VM code path references a specific `.riv`; animation is triggered from UI layers outside the
   recovered batch (`Q-34`).
3. `ui.sonar` (59 classes) contains UI-effect classes — the name suggests a feedback "sonar" pulse used for
   correct/incorrect affordances; **INFERRED_HIGH**, not proven.
4. Haptic feedback calls (`performHapticFeedback`) were not found in the lesson VM; if present they are in
   the fragments (`UNKNOWN`).
5. Sound: no audio assets found for lesson feedback (`VERIFIED_STATIC` for absence in `res/raw`).

## Evidence labels
As marked.

## Open questions
`Q-34` Rive trigger points; `Q-113` haptics; `Q-108` what `sonar` is.

## Reproduction
`find /tmp/x -name '*.riv' | wc -l`
