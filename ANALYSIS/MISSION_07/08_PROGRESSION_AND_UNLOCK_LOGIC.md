# MISSION 07 — 08 PROGRESSION, CHAPTER COMPLETION AND UNLOCK CONDITION

**Status:** `PARTIALLY VERIFIED` (client objects) / `UNKNOWN` (exact unlock
boolean at runtime). `SERVER CONFIRMED = 0`.

## Measured progression objects
`LessonBundle` returned by `base/c.K()` (stage-4 hook, verbatim prefix):
```
lessonId=151410 lessonIndex=0 chapterIndex=0 chapterId=17742
tutorialId=904 trackId=219 trackVersion=82 tutorialVersion=161
tutorialIndex=0 tutorialType=Learn chapterType=PRACTICE_LEVEL_1
isChapterAlreadyCompleted=false isLastLesson=false
isPracticeRedo=false isChallengeRedo=false sectionIndex=0
```
`chapter_completions` remained **0 rows** in every snapshot; no chapter-end
screen was reached by M07. `tutorial_completions` held 672 (stage 2) / 868
(stage 4) seeded rows, all `is_completed=0`. No `is_completed=1` row was
measured. Therefore chapter/tutorial completion transitions are `UNKNOWN`
at runtime; their SQL and DAO signatures are `VERIFIED_STATIC` (M05 `ROOM_SQL.txt`,
M06 `LessonProgressDao` interface).

## Unlock key shape (`VERIFIED_STATIC`, M07 bytecode decode)
`ds/w.c(Set<String>, long, long, long)` @5303868 joins the three longs with
`":"` and returns `Set<String>.contains("<long>:<long>:<long>")`.
`CanOpenChapterWithKeys$invoke$1` consumes that boolean. The **origin of the
three longs and the key set is unknown**: `keys/a` is a remote repository
(`DefaultKeysRepository.fetchKeys`, `consumeUserKey`), and
`com.getmimo.data.model.reward.Reward`/`Rewards` are remote DTOs. No live key
value was observed.

## Path-map state (`VERIFIED_STATIC`, M07 static decode)
`GetPathMapState$invoke$3` @10129608 reads
`sk/a.d() = MainActivity.h` and
`sk/a.e() = mimo_dev_prefs.USE_UNPUBLISHED_TRACKS_PACKAGE`;
`v19 = !e()`, `v21 = (SubscriptionTier.f)`, `v22 = (tier.a >= 4 || v19)`.
`cc/b.y` classifies sections by completion floats compared to `1.0f`.
`sk/a` dev-prefs file is `mimo_dev_prefs` with keys `DISABLE_PREMIUM`,
`preload_images`, `USE_TEST_SERVER`, `CREATE_LESSON_PROGRESS_WHEN_SWIPING`,
`USE_UNPUBLISHED_TRACKS_PACKAGE`, `override_content_experiment`, etc.
**`mimo_dev_prefs.xml` was NOT present** in the measured private-data
snapshots, so these switches were at their defaults and no runtime value of
`v19/v21/v22` is claimed.

## Adaptive onboarding (measured, `VERIFIED_RUNTIME`)
Run `42019353340` UI `NAV-08..20.xml` and run `42028049247` `S4NAV-*`:
coding experience (`NONE / A LITTLE / A LOT`), goal
(`Do better at work or school / Build something useful`), employment
(`Employed`), interests (`Software, IT & data`), topic (`Web apps`,
`Data science`, `Games`, `AI / Machine learning`), path result
(`Python Developer` / `JavaScript` / `HTML`), daily goal
(`Casual 5 min / Regular 10 min / Serious 20 min`), reminders,
notifications, device choice. M05's exact run-003 24-tap chain used the older
onboarding; M07 therefore uses measured XML tap targets rather than replaying
blind coordinates. Choosing `Web apps` in stage 4 produced tutorial 904
(HTML/`Discovering HTML`) with WebView lesson 151403; the generic chooser's
`Data science` in stage 2 produced the Python Developer path whose 4th lesson
was shipped selection lesson 123420.

## Classification
| Rule | Class | Status |
|---|---|---|
| lesson index / chapter index / `LessonBundle` construction | A local | `VERIFIED_RUNTIME` |
| `lesson_progress.tries`, `attempts`, `in_queue` | A local | `VERIFIED_RUNTIME` |
| `isSolvedCorrectly()` | A local | `VERIFIED_RUNTIME` |
| section classification by completion float | A local | `VERIFIED_STATIC` |
| key-set membership unlock | B/D | `VERIFIED_STATIC` for shape, `UNKNOWN` for live values |
| subscription tier / premium gate | D remote / E unknown | `UNKNOWN` |
