# Mission 6 — Screen Inventory

## Scope
Screens derivable from code packages and manifest components.

## Method
Package census under `com.getmimo.ui.*` (activity/fragment/viewmodel classes) and manifest components.

## Findings (VERIFIED_STATIC — counts from file listing)
`ui.*` packages recovered in the decompile batch include: `sonar` (59 files), `lesson.buildtoolbar` (59),
`streak` (12), `codeeditor` (many), `lesson.interactive.*` (4 interaction packages),
`onboarding`, `upgrade`, `iap`, `paywall`, `projects`, `leaderboard`, `profile`, `settings`, `search`
(names as packages). The APK has 61 activities; the `ui` tree contains hundreds of classes.

Screens confirmed by behaviour (not just names):
- onboarding (17-fragment nav graph, Phase 9.63),
- track/tutorial/chapter list (content models + completion endpoints),
- lesson: interactive (4 kinds) and executable (files + console),
- code editor (highlighting, `PartlyEditableEditText`, run actions),
- AI tutor (SSE chat),
- leaderboard (friends/latest), streak/activity, upgrade/paywall, profile.

## Evidence labels
Package presence and behavioural confirmation: **VERIFIED_STATIC**. A full screen-by-screen spec with
layouts is **NOT_RECOVERED** (binary layouts need aapt2).

## Open questions
`Q-107` per-screen layout structure; `Q-108` what `sonar` is (59 classes — name suggests a debugging/QA
overlay, not a learner screen).

## Reproduction
`ls /tmp/dad | grep '^com.getmimo.ui.' | cut -d. -f4 | sort | uniq -c | sort -rn | head -20`
