# Mission 6 — UI State Management

## Scope
How screen state is produced and shared (MVVM shape, flows, one-shot events).

## Method
ViewModel field patterns, `StateFlow/Flow/LiveData` usage, fragment `collect` sites.

## Findings (VERIFIED_STATIC)
1. **MVVM with Kotlin coroutines**: view models expose flows; fragments collect and bind to views.
2. Lesson VMs are **stateful and imperative**: fields plus explicit setter methods (`H`, `U`, `V`, `W`,
   `X`) and null checks; the design is closer to a controller than to a reducer.
3. Navigation/one-shot effects are propagated as booleans/events the fragment observes (e.g. the
   validated-input fragment's `setupViews$2` lambda).
4. Compose screens use their own state hoisting in `ui.compose.*`; the two paradigms coexist (Fragment+View
   for lessons, Compose for newer surfaces).

## Evidence labels
**VERIFIED_STATIC**.

## Open questions
`Q-110` whether a shared session flow drives coins/keys across screens.

## Reproduction
`grep -c 'StateFlow' -r /tmp/dad/com.getmimo.ui.leaderboard*.java | head -3`
