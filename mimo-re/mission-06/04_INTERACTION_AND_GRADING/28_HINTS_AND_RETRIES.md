# Mission 6 — Hints and Retries

## Scope
Whether the client offers hints, how retries are counted, and how either affects progress.

## Method
Search for hint-like state in the lesson VMs; read of the attempt counter and reset path; API catalogue
review for hint/help endpoints.

## Sources
`base.c` (`d`, `C`, `a0`), `evidence/API_CATALOG_V2.csv`, Phase 5.

## Findings
1. **No hint UI/state was recovered** in the lesson view models. There is no `hint` field, no hint
   counter, and no hint event. (VERIFIED_STATIC — negative evidence across the four VMs and the base VM.)
2. **Retries are unbounded**: `attempts` increments on every submission and nothing caps it; no
   "out of lives" branch exists in the grading path (VERIFIED_STATIC).
3. **Lesson reset** (`a0`) exists and emits `lesson_reset`; it clears the exercise but its effect on the
   persisted progress row is **UNKNOWN** (`Q-08`), because the progress writer is called from `H` and the
   reset path's arguments were not fully recovered.
4. The only "reveal" mechanism is the phase-2 input overwrite (near-miss), see 26.

## Evidence labels
Points 1–2: **VERIFIED_STATIC**. Point 3: **UNKNOWN**.

## Open questions
`Q-08`, `Q-37`, `Q-47`.

## Reproduction
`grep -rn 'hint' /tmp/dad/com.getmimo.ui.lesson*.java | head`
