# Mission 6 — Mastery and Spaced Repetition

## Scope
Whether the client implements mastery scoring, spacing, or review scheduling — asked because the product
markets "personalised" learning.

## Method
Search for memory/scheduling vocabulary in the recovered sources and DTOs; review of chapter kinds and
progress fields; endpoint inventory.

## Findings
1. **No spaced-repetition engine was found**: no interval/ease/next-review field, no SM-2-like algorithm,
   no review queue table. (VERIFIED_STATIC — negative; the three Room tables are progress-only.)
2. **No mastery score**: no float/percentage mastery field in any recovered DTO; the closest signals are
   `tries`/`attempts` per lesson and `ChapterType.PRACTICE_LEVEL_1..3`, which are *authored difficulty
   tiers*, not computed mastery. (VERIFIED_STATIC)
3. `hardModeSelected` and `LessonContent$Interactive.hardModeLessonModules` show **hard mode** exists —
   a per-lesson second variant of exercises, chosen by the learner, not by an algorithm.
   (VERIFIED_STATIC)
4. `TrackEtaResponse.currentPaceMinutesPerDay` is a pace signal the *server* holds — the only
   personalisation input visible in the client contract.

## Interpretation (INFERRED)
"Personalisation" in this build is realised as (a) choice of practice level/challenge difficulty per
chapter, (b) hard mode per lesson, (c) server-side pacing for ETA and daily goals. That is a
**rule-based/templated** personalisation, not an adaptive model.

## Evidence labels
1–3 **VERIFIED_STATIC**; interpretation **INFERRED_HIGH**; any server-side adaptive model **UNKNOWN**
(RULE 4: client-side absence ≠ backend absence).

## Open questions
`Q-55` whether the server schedules review; `Q-56` who selects `hardModeSelected` by default.

## Reproduction
`grep -rilE 'spaced|interval|next_?review|ease' /tmp/dad | head`
