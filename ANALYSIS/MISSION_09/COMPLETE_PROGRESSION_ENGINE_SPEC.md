# MIMO 9.35 — COMPLETE PROGRESSION ENGINE SPECIFICATION

**Document:** `COMPLETE_PROGRESSION_ENGINE_SPEC.md` · **Mission:** MISSION 09 (final reconstruction) · **Branch:** `arena/aebb90b7-game`
**Target APK:** `com.getmimo` 9.35, `versionCode=1792759685`, 142,353,499 B, SHA-256 `48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a` — unchanged.
**SERVER CONFIRMED = 0.** Classification vocabulary: `VERIFIED_STATIC`, `VERIFIED_RUNTIME`, `VERIFIED_ASSET`, `VERIFIED_DATABASE`, `VERIFIED_NETWORK_OBSERVATION`, `INFERRED`, `UNKNOWN`, `SERVER_DEPENDENT`.
Evidence codes resolve in `COMPLETE_EVIDENCE_DATABASE.json` / `COMPLETE_SYSTEM_MAP.json -> evidence_index`.

---


## 1. Content hierarchy (VERIFIED_ASSET)

`COMPLETE_CURRICULUM_GRAPH.json` is the deterministic index:
`Track -> Section -> Tutorial -> Chapter -> Lesson -> Asset -> Renderer -> Prerequisite`.
19 tracks, 144 sections, 1,029 unique tutorials, 1,947 chapters, 18,272 unique lessons,
2,002 tutorial references across tracks, 37,183 lesson placements. `section.startIndex`/
`endIndex` are consistent with `tutorialIds` in all 144 sections (0 violations) [E23].

Tutorial types (`tutorial.type`): `course` 507, `practiceRequired` 157,
`practiceOptional` 134, `guidedProjectOptional` 117, `guidedProject` 74, `challenges` 40.
Chapter types: `practiceLevel1` 810, `practiceLevel3` 522, `challengeLevel2` 382,
`practiceLevel2` 174, `challengeLevel0` 45, `challengeLevel1` 14 [E24].

## 2. Ordering and next-item selection (VERIFIED_ASSET + VERIFIED_RUNTIME)

```
nextLesson(bundle):
    lessons = tutorial(bundle.tutorialId).chapters[bundle.chapterIndex].lessons
    if bundle.lessonIndex + 1 < lessons.size:
        return lessons[bundle.lessonIndex + 1]
    else:
        return firstLesson(nextChapter(bundle))

nextChapter(bundle):
    chapters = tutorial(bundle.tutorialId).chapters
    return chapters[bundle.chapterIndex + 1]  # VERIFIED_ASSET ordering

nextTutorial(section, currentId):
    ids = section.tutorialIds
    return ids[ids.indexOf(currentId) + 1]    # VERIFIED_ASSET ordering
```
Runtime: `nextPage.value = lessonBundle.chapterIndex` after `Y(Z)`; M07 stage 6 observed
`e = chapterIndex -> next lesson` after `f0()/N()` [E25 §A, E06].
`LessonBundle.isLastLesson` and `isChapterAlreadyCompleted` are runtime flags on the bundle
[E28]. **No randomization** exists in the shipped index.

## 3. Path-map state (VERIFIED_STATIC, exact boolean UNKNOWN)

`GetPathMapState$invoke$3` @10129608 (659 instructions) [E25 §O, E28, E32]:

```
for tutorial in sections (excluding Challenge):
    state = if (tutorial.isCompleted)                              -> Completed (vn/d0)
            else if (no local progress && !sequential prerequisite met) -> Locked (vn/e0)
            else if (pro/key gate fails)                          -> UnlockedButNoKeys (vn/h0)
            else                                                   -> Unlocked (vn/g0)
    chapterItem = vn/d(id, title, isCompleted, isCompletedInHardMode)
result = vn/n(track, sectionStates, selectedIndex, dialogs, ...)
```
Known inputs: `Tutorial.isCompleted()`, `TutorialType.isRequired()`, `SubscriptionTier.f`,
`CanOpenChapterWithKeys`, keys count, and dev overrides read from
`sk/a.d() = MainActivity.h`, `sk/a.e() = mimo_dev_prefs.USE_UNPUBLISHED_TRACKS_PACKAGE`;
`v19 = !e()`, `v21 = SubscriptionTier.f`, `v22 = (tier.a >= 4 || v19)`.
`cc/b.y` classifies sections by completion floats compared against `1.0f`.
A **reverse `listIterator`** enforces the sequential required-tutorial prerequisite
(M06 10_LEARNING_PROGRESSION.md). Branch PCs `0x04aa`, `0x4f0`, `0x51a`, `0x608`.

**The exact live boolean combining tier / keys / progress is UNKNOWN.** `mimo_dev_prefs.xml`
was absent in every snapshot, so dev switches were at defaults; no key value and no live
`Locked`/`UnlockedButNoKeys` decision was observed. Do NOT implement a guessed predicate:
define an interface (§7) with an explicit offline fallback.

## 4. Unlock key (VERIFIED_STATIC + SERVER_DEPENDENT)

`ds/w.c(Set<String>, long, long, long)` @5303868:
```
return set.contains("<trackId>:<tutorialId>:<chapterId>")
```
consumed by `CanOpenChapterWithKeys$invoke$1` @10104004. The key set originates from remote
`DefaultKeysRepository.fetchKeys` / `consumeUserKey` (`GET /v1/user/keys`,
`POST /v1/user/keys/consume`) [E28]. No live key was observed; no key was seeded.

## 5. Chapter / tutorial completion (UNKNOWN at runtime)

`chapter_completions` stayed **0 rows** and `tutorial_completions` held **868 rows all
`is_completed=0`** in every M07/M08 snapshot; no chapter-end screen, no `is_completed=1`
row, no `ChapterFinishedSuccessType` transition was reached [E28, E13].
Static only: `CompletionRepository.b(Track, cont)` attaches `TutorialCompletion.isCompleted`
and `completedChapters` from Room; `ChapterFinishedViewModel.R` handles
`handleChapterAlreadyCompletedState`; `ChapterFinishedSuccessType` distinguishes
`DAILY_GOAL_NOT_REACHED / REACHED / ALREADY_REACHED_EARLIER_TODAY`.
SQL exists for `INSERT INTO chapter_completions` and
`SELECT COUNT(DISTINCT chapter_id) FROM chapter_completions` [E27].
**Closure condition:** `U-PROG-002`.

## 6. Practice / redo / challenge / review (VERIFIED_ASSET + STATIC)

Shipped content types prove the *existence* of these modes: `practiceRequired` (157),
`practiceOptional` (134), `challenges` (40), `guidedProject` (74),
`guidedProjectOptional` (117); chapter types `practiceLevel1/2/3`, `challengeLevel0/1/2`.
`LessonBundle` carries `isPracticeRedo` and `isChallengeRedo` flags (both `false` in the
measured bundle) and `tutorialType=Learn`, `chapterType=PRACTICE_LEVEL_1` [E28].
`lesson_progress.is_practice_progress` distinguishes practice rows from learn rows.

**Runtime gate:** the Practice tab for a guest renders `Lock in your learning / Create a
profile to access practice content` in a Compose `anonymous_user_lock_view`; no practice
lesson was entered, no redo/challenge session was observed [E14].
Therefore: mode *assets* are `VERIFIED_ASSET`, mode *behaviour* is `UNKNOWN` / requires
authentication. Closure: `U-PROG-003`.

## 7. Deterministic progression algorithm (implementation contract)

```text
# Locally authoritative (implement verbatim)
function resolveTrack(trackId): return curriculum.tracks[trackId]
function resolveSection(track, index): return track.sections[index]
function resolveTutorial(track, section, tutorialId):
    assert tutorialId in section.tutorialIds
    return curriculum.tutorials[tutorialId]
function nextLesson(bundle): ... (§2)
function localCompletionState(tutorialId, trackId):
    return { lessonProgress: rowsFor(tutorialId),
             chapterCompletions: rowsFor(tutorialId),
             tutorialCompletion: tutorialCompletionsRow(tutorialId, trackId) }
function localSectionProgress(section):
    done = count(distinct completed chapterIds in section)
    total = count(all chapterIds in section)
    return done / total                     # compared to 1.0f by cc/b.y

# Interface only — ORIGINAL predicate UNKNOWN
interface UnlockPolicy {
    enum Status { COMPLETED, LOCKED, UNLOCKED, UNLOCKED_BUT_NO_KEYS }
    Status evaluate(Tutorial t, Chapter c, LocalProgress p, SubscriptionTier tier,
                    Set<String> keys, DevOverrides dev);
}
# Key-membership sub-rule IS verified:
function hasKey(keys, trackId, tutorialId, chapterId):
    return keys.contains("<trackId>:<tutorialId>:<chapterId>")

# Independent offline fallback (EXPLICIT DESIGN CHOICE, not Mimo behaviour):
#   treat every required tutorial whose sequential prerequisites are locally
#   complete as UNLOCKED; ignore tier and remote keys; never invent a key value.
```

## 8. Decision table

| Condition | Status (verified shape) | Evidence class |
|---|---|---|
| `tutorial.isCompleted()` true | `Completed` | VERIFIED_STATIC |
| no local progress AND sequential required-tutorial prerequisite unmet | `Locked` | VERIFIED_STATIC |
| pro/key gate fails | `UnlockedButNoKeys` | VERIFIED_STATIC |
| otherwise | `Unlocked` | VERIFIED_STATIC |
| exact boolean combination / tier / live keys | UNKNOWN | UNKNOWN + SERVER_DEPENDENT |
| chapter completion event | never observed | UNKNOWN |
| section unlock threshold | `cc/b.y` compares completion float to `1.0f` | VERIFIED_STATIC |

## 9. Failure / success paths

* **Failure (wrong answer):** `attempts++`, `tries=0`, wrong-feedback block, no advance;
  no chapter unlock change [E25 §C].
* **Success (correct answer):** `tries=1`, progress row with `in_queue=1`, `nextPage`
  advanced, analytics `f0(false,true)`, `N()` reset input [E06].
* **Offline:** learning continues from shipped assets; `postUnsyncedLessonProgress`
  throws `NoConnectionException`; queued rows may be deleted at cold start [E26].
* **Restart:** Room `tutorial_completions` / `room_master_table` persist; UI returns to
  path map [E26].
* **Different selected track:** `favorite_tracks` / `favorite_tracks_to_sync` preferences
  change; `GetPathMapState` recomputes from the new track id [E11, E13, E28].


---

## MISSION 09 runtime addendum (`VERIFIED_RUNTIME`, run `42077425594`)

The MISSION 09 controlled run succeeded where M08 failed: the API-36 `Java.registerClass`
lifecycle hook was replaced with **direct** `android.app.Activity` / `Fragment` /
`WebView` hooks, giving `server_active=true`, `attach_ok=true` (pid 3348, process `Mimo`),
**181 hooks installed, 72 real `com.getmimo` method `entry` events**, 71 `exit`,
86 SQL, 17 DI, 19 LiveData and 28 lifecycle `nav` events. `real_target_method_executed=true`.
All three user-required instrumentation conditions are therefore met [E29, E30].

`SERVER CONFIRMED = 0`. Instrumentation success is not a claim that every screen was
reached: the fixed 20-tap onboarding chain stalled at step 4 on this build, so
`MainActivity` was reached with an explicit intent; the lesson answer matrix was
**not executed** (`lesson_matrix_not_executed`, `ChapterActivity` not reached) and the
resulting three route screens resumed an incomplete `OnboardingActivity` back stack.
See `FINAL_UNKNOWN_REGISTER.md` and `FINAL_TEST_MATRIX.json` for the honest limitations.

### M09 runtime progression evidence

`com.getmimo.interactors.path.d` (`GetPathMapState`) was observed **live** with its full
collaborator set: `a=com.getmimo.data.content.tracks.c`, `b=local completion.a`,
`c=remote iap purchase.a`, `d=sk.a` (dev prefs), `e=cc.b` (section classifier),
`f=interactors.path.b`, `g=upgrade inventory.a`, `h=network.a`, `i=remote keys.a`,
`l=local.a`. Calls: `b(50, 0, null, continuation)` from
`PathMapViewModel$init$$inlined$flatMapLatest$1` and `a(0, true, continuation)` from
`GetPathMapState$invoke$3` [E29]. `com.getmimo.interactors.path.sections.a.a()` was invoked
from `MainViewModel$updateData$1`. `keys.a.b()`/`c()` and `path.f.a()` also executed.
`SELECT COUNT(DISTINCT chapter_id) FROM chapter_completions` was captured. This **closes
the collaborator graph** of gap D; the exact live status boolean remains `UNKNOWN`
(`U-PROG-001`) and chapter completion remains unobserved (`U-PROG-002`).
