# Spec 109 — Navigation

## MUST
1. Single entry activity handling deep links for `https://getmimo.com/*` and `mimo://`.
2. Onboarding as a multi-step graph (17 fragments observed) before the main surface.
3. Lesson flow reachable from track/tutorial/chapter list; interactive lessons in a shared host with one
   fragment per interaction kind.
4. AI tutor reachable from lesson/code context.

## MUST NOT
- Invent route names or a bottom-bar structure (not recovered).
- Assume a nav library — part of the app is Compose-driven.

## GIVEN EVIDENCE
`09_NAVIGATION_AND_UI/63..69`.
