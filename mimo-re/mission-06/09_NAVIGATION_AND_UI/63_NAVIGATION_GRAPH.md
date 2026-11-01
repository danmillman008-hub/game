# Mission 6 — Navigation Graph

## Scope
The real navigation structure: entry points, top-level destinations, and the lesson flow's place in it.

## Method
`res/navigation/*.xml` scan (17 fragments in the onboarding graph alone), `AndroidManifest.xml`
(61 activities, 6 splash aliases), deep-link filters, Compose `NavHost` findings.

## Findings (VERIFIED_STATIC)
1. `MainActivity` carries **12 deep-link intent filters for `https://getmimo.com/*`** plus a `mimo://`
   scheme — so the web→app surface is one activity with many routes, not one activity per feature.
2. Navigation XMLs exist (`res/navigation/…`); the largest recovered graph is onboarding-only:
   **17 fragments**. The main app graph was not recovered as a single XML (it is Compose-driven in part).
3. 61 activities: 6 are splash/alias variants (`…Alias…`), the rest are feature hosts (auth, upgrade,
   paywall, webview hosts, code editor, etc.).
4. Lesson flow: `ui.lesson.*` fragments are hosted by a lesson activity reached from the track/tutorial
   list; the interactive lesson uses 4 fragment classes (one per interaction kind) inside a shared host.
5. **The AI tutor is reached from lesson/code screens**, not from a bottom-bar destination (also Phase 8.56).

## Evidence labels
Deep links, counts, onboarding graph: **VERIFIED_STATIC**. "Main graph is partly Compose": 
**INFERRED_HIGH** (Compose present + absent XML graph).

## Open questions
`Q-105` full main-graph route names; `Q-106` bottom-bar destinations (none recovered by name).

## Reproduction
`grep -c 'BROWSABLE' /tmp/manifest.xml; ls /tmp/res/res/navigation | head`
