# Mission 6 — Event Taxonomy

## Scope
Grouping of the 252 analytics-context literals into a taxonomy.

## Method
`evidence/EVENT_CANDIDATES.csv` (mission-06 tool) grouped by lexical family; **no emitter binding**.

## Findings (INFERRED — grouping only)
| Family | Examples of literals | Confidence |
|---|---|---|
| lesson interaction | `interaction_*`, `lesson_*` (`lesson_reset` verified in code) | HIGH for `lesson_reset` (read in `base.c`), INFERRED for the rest |
| onboarding | `onboarding_*` | INFERRED |
| paywall/upgrade | `paywall_*`, `upgrade_*`, `iap_*` | INFERRED |
| league/leaderboard | `leaderboard_*`, `league_*` | INFERRED |
| ai tutor | `ai_tutor_*` | INFERRED |
| streak | `streak_*` | INFERRED |

Only `lesson_reset` was **seen at a call site**; every other name is a string constant whose emission site
is unidentified. Treat this table as a *hypothesis list*, not an inventory.

## Evidence labels
`lesson_reset` **VERIFIED_STATIC**; the rest **INFERRED**.

## Open questions
`U-20`; `Q-132` whether some literals are property values rather than event names.

## Reproduction
`awk -F, 'NR>1{print $1}' evidence/EVENT_CANDIDATES.csv | cut -d_ -f1 | sort | uniq -c | sort -rn | head`
