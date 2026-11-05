# MISSION 07 — supplementary DEX decode (rechecked against M06 corrected xref cache)

All offsets/signatures from the ORIGINAL APK (`48ce1740…7c7a`) via Androguard 4.1.4
harness `m06_dex.M06`. Raw dumps are in this directory. `const/4 vN, <junk>` lines
are Smob no-op decoys; trailing `fill-array-data-payload` is a linear-decode artefact.
**Status:** `VERIFIED_STATIC` for instruction sequences; `INFERRED` for semantic names.
Runtime confirmation is being sought separately; no claim of execution here.

## Q-7 resolved: `c.W()` == correct answer WITH partial match
`Lcom/getmimo/ui/lesson/interactive/base/c;->W(Lqm/f; ContinuationImpl;)Object`
@`classes.dex 10953916` (202 instructions) is the state machine of
`InteractiveLessonBaseViewModel$lessonSolvedCorrectlyWithPartialMatch$1`.
Compare `c.V()` @10952900 (`…lessonSolvedCorrectly$1`), 165 instructions:

Identical spine in **both**:
1. suspend on `base/c.i0(cont)` (await browser/output),
2. `C = Boolean.FALSE`; `d++` (attempt counter); `c0()`,
3. `tries = (C == Boolean.TRUE) ? 0 : 1`  ← `Lkotlin/jvm/internal/h.c` + `xor-int/2addr …, 1`,
4. `H(tries, d)` → `LessonProgress` (M06: 11 columns, `inQueue=true`),
5. `e0(progress, cont)` → persist (suspends),
6. `sound/a.a(true)` (success sound), `f0(false, progress.isSolvedCorrectly())`,
7. emit `Long(lessonBundle.a)` to flow `h`, then `I()` cleanup.

**NOTE — M06 correction:** `c.V()` byte-code passes **false** as the first `f0`
argument (`const/4 v9, 0; move v12, v9` @0x180), not `true` as stated in M06
summary. `W()` also passes `false` (@0x19e). `f0(Z Z)` semantics remain `INFERRED`.

Differences:
* `V()` posts `jm/m.b(s, true, E, 1)` to LiveData `q`; throws
  `Intrinsics.throwUninitializedPropertyAccessException("solutionFeedbackCorrect")`
  if field `s` is null.
* `W()` constructs `jm/n(userInput, expectedInput, true, E)` from
  `qm/f.h` / `qm/f.i`, posts it to `q`, and records analytics event
  `validated_input_execution_correct_partial_match` with properties
  `user_input` and `expected_user_input`.
Therefore the three M06 outcomes (`Exact → Correct`, `Normalized-only →
PartialMatch`, `Mismatch → Incorrect`) map to `V / W / X+d0`.

## `c.d0()` — wrong-feedback coroutine (`showWrongFeedbackBlock$1`)
@`10956096`, 148 instructions. Inputs actually read:
* `base/c.S()Z` — a fast-path guard,
* field `E Z` (hard-mode flag), field `d I` (attempts),
* field `t Ljm/o;` — wrong-feedback state; null triggers
  `throwUninitializedPropertyAccessException("solutionFeedbackWrong")`,
* `Lhm/b;->g` cast `com.getmimo.data.local.a`: `f(cont) → Boolean` and `p()V`,
* `base/c.P(cont) → Boolean`,
* `jm/o.b(Ljm/o; Z Z I)Ljm/o` (fast path) and
  `new Ljm/o(CharSequence; Z Z Z Z Z Z)` (7-field feedback object) posted to `q`.
Boolean derived at 0x138–0x148: `v12 = (E && d == 1 && prefBoolean) ? 1 : 0`.
`jm/o` field mapping is `INFERRED`; runtime field dumps (Frida hook `d0`) are
needed to name the 6 booleans. No scoring/XP arithmetic appears in `d0()`.

## D path-map / unlock boolean chain (Q-5, Q-8 partially)
`GetPathMapState$invoke$3.invokeSuspend` @10129608 (659 instructions) reads:
* `Track y`, `ri/c z`, `Pair<yg/c,Integer> A`, `boolean B`, `Set<String> C`,
* `path/d` collaborators `a…l` (completions, purchase, `ze/a`, `cc/b`, keys, …).
Measured branch at 0x0e8–0x15c (constants `v15 = 1`):
```
d()  = sk/a.d()  = MainActivity.h            (static, measured to be a boolean)
e()  = sk/a.e()  = pref "USE_UNPUBLISHED_TRACKS_PACKAGE"
v19  = !e()                                  (1 unless that pref is set)
v21  = (subscriptionTier == SubscriptionTier.f)
v22  = (subscriptionTier.a >= 4) || v19
cc/b.y(sections, v19, Integer(sectionIndex), v21, v22)
```
`cc/b.y` @8683988 (86 instr) classifies each `Section` by
`completionPercentageOptional()` and `completionPercentageRequired()` vs `1.0f`
into `vn/v`, `vn/w`, `vn/y`, `vn/a0` path states, calling
`cc/b.v(Section, v21, v22)` for detail.

Chapter lock boolean comes from `Lds/w;->c(Ljava/util/Set; J J J)Z`
@5303868 (41 instr): it joins three `long` args with `":"` and returns
`Set<String>.contains(that key)`; result goes into `new Lvn/d(J, String, Z, Z)`
(chapter id, title, completed, locked) at 0x3aa–0x410.
So an unlock key is the string `"<long>:<long>:<long>"` — exact operand origins
(track/tutorial/chapter IDs) still need runtime values (`UNKNOWN` for now).

`sk/a` @14344240 uses SharedPreferences **`mimo_dev_prefs`** with boolean keys:
`DISABLE_PREMIUM`, `preload_images`(default true), `USE_TEST_SERVER`,
`CREATE_LESSON_PROGRESS_WHEN_SWIPING`, `USE_UNPUBLISHED_TRACKS_PACKAGE`,
`disable_leak_canary`, `FORCE_REACTIVATION_PROMPT_ON_APP_LAUNCH`,
`FAKE_REMOTE_DISCOUNT_ENABLED`, `FAKE_REMOTE_DISCOUNT_IMAGE_ENABLED`,
`FORCE_LAST_CALL_DISCOUNT_ENABLED`, `FORCE_PATH_OVERVIEW_ETA_ENABLED`,
`FORCE_CHAPTER_END_PROGRESS_ETA_ENABLED`, `USE_MOCKED_TRIAL_REMINDER_DATES`,
`override_content_experiment`, `overridden_subscription_for_ReactivateProDiscount`.

`CanOpenChapterWithKeys$invoke$1` @10100124 is a thin coroutine forwarding to
`com.getmimo.interactors.chapter.a.a(cont)`; the repository holds
`com.getmimo.data.source.remote.keys.a` (remote keys). Offline behaviour of this
path is `UNKNOWN` until measured.
