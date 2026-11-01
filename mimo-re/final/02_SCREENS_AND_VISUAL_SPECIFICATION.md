# 02 — Screens and their states

36 app activities, 22 fragments, 22 `ModalData` modals, 87 bottom-sheet classes, 44 dialog
classes, 19 Glance widget classes and 809 XML layouts (VERIFIED STATIC). This document walks
the app the way a user does, and for each surface records: entry point, structural elements,
and the **state set**. State names are grounded in the strings that the app actually renders
(`evidence/resources-strings.xml`), not invented.

Notation: **V** = VERIFIED STATIC, **I** = INFERRED, **U** = UNKNOWN.

---

## 1. Cold start

| | |
|---|---|
| Activity | `com.getmimo.ui.SplashActivity` (V), 3 intent filters, exported |
| Purpose | deep-link router + session bootstrap + remote-config prefetch |
| States | `launch` → `authenticated` / `unauthenticated`; deep-link `login`, `register`, `deeplink/continuelearning`, `deeplink/support` (V) |
| Transition | authenticated + onboarding complete → `MainActivity`; incomplete → `OnboardingActivity` (I, from `nav_onboarding_graph.xml` + `OnboardingActivity`) |

Deep links (V): `https://getmimo.com/login`, `mimo://getmimo.com/register`,
`https://getmimo.com/deeplink/continuelearning`, `…/deeplink/support`,
`https://getmimo.com/profile`, `https://getmimo.com/learn/*`.

## 2. Authentication

`AuthenticationActivity` (V) with email, Google, Apple and Facebook providers
(`AuthenticationActivity`, `authentication_error_*` strings: invalid credentials, email in use,
generic login error, social provider mismatch). Also `ChangeEmailActivity`.
State set (V by strings): `idle`, `submitting`, `error_invalid_credentials`,
`error_email_in_use`, `error_generic`, `error_provider_conflict`.
`delayed_account_creation_offline_error` and `signup_prompt_headline_continue_learning`
indicate **deferred account creation**: the user can learn before signing up and is asked to
convert later (V string, I flow).

## 3. Onboarding — the largest UI surface (12 steps + 3 branches)

`OnboardingActivity` + `nav_onboarding_graph.xml` (the app's only navigation resource, V).
Step fragments in shipping order (I: order derived from fragment names + `onboarding_*`
string families; the graph itself was not decompiled):

1. `IntroductionFragment` — value proposition slides (`IntroSlidesActivity` also exists for the
   pre-onboarding slide show).
2. `SetMotiveFragment` — *why are you learning* (`onboarding_adapted_motive_*`).
3. `SetOccupationFragment` — occupation/role.
4. `SetWorkFunctionFragment` — only for certain occupations (branch, I).
5. `SetExperienceFragment` — `beginner` / `intermediate` / `advanced` (V strings).
6. `OnboardingSelectPathContainerFragment` — path choice with `onboarding_adapted_all_courses_title`.
7. `OnboardingPathReassuranceFragment` — reassurance after path choice.
8. `OnboardingDevicePreferenceFragment` — `phone` / `desktop` / `both` (V strings): drives the
   promised device split of the curriculum.
9. `OnboardingDeviceReassuranceFragment`.
10. `OnboardingMotiveReassuranceFragment`.
11. `OnboardingSkillPreferenceFragment` — skill goals.
12. `OnboardingSetDailyGoalFragment` + `SetDailyGoalActivity` — daily goal in minutes
    (`reactivation_set_goal_current`, `onboarding_adapted_daily_goal_title`).
13. `OnboardingPreparingCurriculumFragment` — server-side plan generation with
    `onboarding_curriculum_loading` (V) → this is the step where the *adapted* curriculum is
    materialised (`experiment_adapted_onboarding_android` gates the variant, V: remote-config key).
14. `PathCompletionEstimationFragment` — projected finish date (`chapter_end_progress_eta_*`
    strings mirror this vocabulary).
15. `SetReminderTimeFragment` + `NotificationsSettings` modal — reminder opt-in.
16. `AskForNameFragment` → `NameCodePlaygroundFragment` (first-run mini playground).

States per step: `default`, `selected`, `disabled CTAs` (`continue_cta`, `onboarding_continue`
strings), `loading` (only step 13), `offline` (`delayed_account_creation_offline_error`).
Back-navigation is a `SavedStateHandle`-backed ViewModel per step (I: `NavigationBar$…SavedState`
and fragment-local ViewModels; per-step state restoration not directly observable).

## 4. Home / path screen

Host: `MainActivity` (V) with `NavigationBar` (V: `ui.navigation.NavigationBar` with
`listenToTabChanges`, `listenToTabNotifications`, `listenToTabVisibilityChanges` — i.e. the tab
set is **server/policy driven**, and a tab can be hidden or badge-highlighted at runtime).
Tab labels are not present as app strings (U / icon-only).

Content blocks visible from class + string evidence:
* current path card with progress and `continue_learning` CTA (V string);
* streak strip (`Streak`, `ui.streak.ArcProgressView`, Glance widget shares the same state
  provider — V);
* daily-goal ring (`daily_goal_progress_view_current_sparks_text_size_42sp` dimen proves a
  dedicated goal view, V);
* chapters list with lock/`keys_left_today` gating (V strings);
* re-activation banner after absence (`reactivation_*`, 22 strings, V);
* Pro upsell banners (`track_content_upgrade_pro_*`, V).

States: `loaded`, `loading` (`loading`), `empty` (no path yet → onboarding), `offline`
(`activity_offline_description`, `offline_view_refresh`), `error` (`generic_error_retry`),
`paywalled` (`track_content_upgrade_pro_action_button`).

## 5. Chapter screen

`ChapterActivity` (V) is the lesson container. It hosts `WrapperFragmentActivity` (V) and the
three lesson players; `ChapterActivity` also owns the chapter-completion flow
(`chapter_end_*`, 52 strings, V) and native-ad fallbacks (`chapter_end_native_ads_*`).

States: `lesson_in_progress`, `chapter_finished` (`chapter_end_free_streak_goal_*`),
`chapter_finished_offline_state_description` (V!), `chapter_finished_loading` (V),
`streak_challenge_prompt` (V), `certificate_progress` (`certificate_upselling_closer_to_certificate`).

## 6. Interactive (markup) lesson player

`ui.lesson.interactive.*` (V). Layout is a scrolling document; each module is either
informational or assessed. Assessed modules: fill-the-gap, validated input, selection.
Feedback strings (V): `module_*` family, `validated_input_partial_match_feedback_text_the_correct_answer_is`,
`interaction_hint_ftg` ("Tap the snippets below"), `interaction_hint_multiple_choice`,
`interaction_hint_single_choice`, `interaction_hint_validated_input`, `see_solution*` (7 strings).
A "check" produces a per-module `wrong`/`correct` state which then toggles
`visible-if="wrong"` / `visible-if="correct"` blocks — the mechanism behind 13,043
"shown only when wrong" blocks in the corpus (§6).

State set per module: `unanswered` → `selected` → `checked_correct` | `checked_wrong`
→ (`hint_shown`) → `solution_shown` (`see_solution_confirm_dialog_*`).
Lesson-level: `in_progress`, `passed` (client-side for markup lessons), `failed_attempts_n`.

## 7. Executable lesson player

`ui.lesson.executable.*` (`ExecutableLessonViewModel`, V). Surfaces: instructions tab
(`executable_lesson_instructions`, "Tap Instructions anytime"), code editor
(`codeeditor_*` dimens, `code_editor_text_size 15sp`), coding keyboard
(`coding_keyboard_height 64dp`, `CodingKeyboardKt` with an AI-tutor pulse button, V),
console (`input_console_*`, `InputConsoleActivity`), test list
(`%d/%d checks passed`, `Condition %d`), run button, see-solution
(`see_solution_user_code` / `see_solution_our_solution` diff view), AI tutor entry points.

Feedback strings (V): `executable_lesson_feedback_success_0..5` (6 rotating encouragements),
`…_almost_there`, `…_somethings_off`, `…_get_help`, `…_ask_ai_tutor`,
`executable_lessons_code_execution_general_error`, `executable_lessons_connection_warning`.

States: `editing` → `running` (`code_header_console_loading`) → `all_tests_passed` |
`some_tests_failed` | `execution_error` | `compile_error` | `offline_blocked`
(`executable_lessons_connection_warning` — **code execution requires network**, V).
Autosave runs continuously (`AutoSaveCodeService`, V class).

## 8. Chapter end / reward moment

`ModalData` variants (V): `CertificateCompletionInfo`, `CertificateNotFinishedYetModalData`,
`CertificateProfessionalInfo`, `SmartPracticeChargedModal`, `SmartPracticeMasteredModal`,
`StreakChallengeSuccess`, `StreakChallengeFailure`, `StreakRepairModal`, `TrialStartedEnableNotification`,
`PendingPurchase`, `JoinedAnInvite`, `InviteFriendsPro/NoPro`, `FriendsAcceptedInvitePro/NoPro`,
`NotificationsSettings`, `AppIconChangeNeedsRestart`, `InputConsoleIntroduction`,
`ContentRearrange`, `FirebaseInAppMessages`, `DeveloperMenuDownloadLiveContent`,
`DeveloperMenuLiveDeploymentError`.
Reward ritual strings (V): `reward_choose_box`, `reward_tap_to_open`, `reward_header_with_name`,
`reward_drag_to_dismiss` + Rive animation (`Rive` 983 classes).

States: `chapter_complete` → `reward_available` → `box_opening` → `reward_granted`
(`sparks_goal_reached_coins`), or `streak_challenge_prompt` → accepted/declined.

## 9. Practice hub

`ui.practice` (V) + 37 `practice_*` strings: three value props
(`practice_benefit_title_1..3`), filters `Completion status` / `Paths` / `Content type`,
`Hide completed`, search placeholder, empty state
(`practice_filter_no_results_description`). Smart practice is a **paid** feature
(`SmartPracticeChargedModal`, `SmartPracticeMasteredModal`, V).
States: `loading`, `results`, `filtered_empty`, `offline` (`practice_offline_*`).

## 10. AI tutor

`AiTutorBottomSheetKt` (Compose, V) — a bottom sheet with chat, writing indicator, suggestion
chips (`PromptSuggestions`: `FirstHint`, `SecondHint`), upgrade path
(`ai_tutor_upgrade_title`, `ai_tutor_upgrade_message_count`, `ai_tutor_upgrade_button`).
States (V, from `AiTutorViewModel$State`): `loading`, `messages[]`, `usedMessages`,
`nextHint`, `isMessageLoading`, `isPro`, `isFeatureDisabled`, `blockingError`, `offline`
(`ai_tutor_offline_description`). Full behaviour in §8.

## 11. Store, paywall, upgrade

`PaywallActivity`, `UpgradeModalActivity`, `AllPlansActivity`, `CertificateUpgradeActivity`,
`UpgradeCompletedActivity`, `ExtendedUpsellFlowActivity`, `ReactivationActivity`,
`store_*` (39 strings) + `upgrade_*` (39) + `ai_tutor_upgrade_*`.
Store sells **cosmetics and protections**, not just subscription: app icons
(`store_info_app_icons_*`), streak freezes (`store_product_streak_freeze_*`), coins→rewards.
States: `plans`, `trial_eligible`, `discount_active` (`keys_discount_drawer_*`: 50% off with
countdown; `DeveloperMenuDiscountActivity` can force it), `purchase_pending`
(`PendingPurchase` modal), `purchase_complete` (`UpgradeCompletedActivity`), `offline`
(`store_offline_message`), `restore` (`restore_purchases`).

## 12. Profile, certificates, settings

`ProfileFragment` + `PublicProfileActivity` (V): bio, certificates
(`profile_certificates_completion_*`, `profile_certificates_professional_*`), friends
(`friends_*`, 30+ strings incl. `friends_offline_message`, `friends_profile_empty`),
report user (`public_profile_report_user_dialog_*`).
`SettingsActivity` (68 `settings_*` strings): account, email, appearance
(`settings_appearance_dark/light`), app icon (`settings_app_icon_*`, requires restart),
notifications, privacy, sign-out.
`CertificateActivity` / `ProfessionalCertificateActivity`: 50 `certificate*` strings, download
(`certificate_snackbar_download_message`), upsell gate (`certificate_upselling_likely_to_finish`).
States: `anonymous_profile_locked` (`profile_anonymous_lock_*`), `empty`, `offline`
(`profile_offline_description`).

## 13. Offline surface (cross-cutting)

Every network-bound surface has an offline variant with its own string
(V, 14 strings): `activity_offline_description`, `chapter_finished_offline_state_description`,
`leaderboard_offline_message`, `store_offline_message`, `profile_offline_description`,
`map_offline_description`, `report_lesson_offline_message`, `friends_offline_message`,
`integrated_webview_offline_view`, `ai_tutor_offline_description`, `offline_message`,
`offline_view_refresh`. This is the app's most consistent UX rule: **nothing fails with a raw
error; everything degrades to an offline view with a refresh affordance.**

## 14. Widgets

Glance widget sizes: small / medium / large / tiny (`MimoStreakSmallWidgetReceiver`,
`…MediumWidgetReceiver`, `…LargeWidgetReceiver`, `WidgetSizeBucket`), refreshed by
`StreakWidgetRefreshWorker`; strings `widget_message_time_to_code`, `widget_message_well_done`,
`widget_inactive_title` ("Mimo misses you!"), `widget_inactive_subtitle`.
States: `streak_active`, `no_streak`, `inactive/dormant`, `refreshing`.

## 15. Developer menu (production build)

`DeveloperMenuActivity` + `DeveloperMenuFragment` + sub-activities (§12). Not reachable from
any exported component (V: no exported activity with that name), typically gated by a hidden
gesture or a remote flag (U).

## 16. Screen-state coverage summary

| State family | Surfaces that implement it | Evidence |
|---|---|---|
| `loading` | onboarding plan, chapter end, console, AI chat, practice | `loading`, `chapter_finished_loading`, `onboarding_curriculum_loading`, `code_header_console_loading` |
| `offline` | 12 surfaces | 14 `*_offline_*` strings |
| `empty` | playgrounds, saved code, friends, practice filters, console | `empty`, `state_empty`, `playgrounds_empty_*`, `saved_code_empty_state_*`, `friends_profile_empty` |
| `error + retry` | global | `generic_error_retry`, 71 `*error*` strings |
| `paywall` | paths, chapters, practice, AI tutor, certificates, app icons | `*_upgrade_*`, `*_pro_*`, `keys_*` |
| `reward` | chapter end, streak challenge, daily goal | `reward_*`, `streak_challenge_*`, `sparks_*` |
