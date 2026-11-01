# 15 — Remote configuration and experimentation

## 1. Three separate configuration planes (V)

| Plane | Transport | What it controls | Evidence |
|---|---|---|---|
| **A. Firebase Remote Config + A/B Testing** | Firebase SDK | feature flags, experiment variants, server-side defaults | `FirebaseRemoteConfig refresh of A/B tests failed due to `, `abt_experiments_key`, `experiment_*` keys |
| **B. Mimo client-config service** | `GET /v2/client-config`, legacy `GET /v1/config/%s` | tabs, feature bundles, streak/pacing parameters | endpoint literals; `NavigationBar.listenToTabVisibilityChanges` |
| **C. Content experiments** | bundled config + `/v2/client-config`; editable in the dev menu | swapping a whole **track** for a variant with a rollout percentage | `ParsedContentExperiment$Experiment(originalTrackId, variantTrackId, visibilityPercentage)` |

Plane C is the interesting one: it is not a UI experiment, it is an **experiment on the product's
core content**, expressed as "serve track 80 instead of track 50 to N% of users".

## 2. Known keys (V literals)

| Key | Plane | Reading |
|---|---|---|
| `experiment_adapted_onboarding_android` | A | alternative onboarding that builds an "adapted" plan |
| `experiment_daily_goal_companions_android` | A | companion characters on the daily-goal UI |
| `experiment_hardmode_v2_android` | A | second-generation hard mode (42.5% of interactive lessons have variants) |
| `experiment_trial_reminder_choice_android` | A | trial-reminder variant with a choice (`TrialReminderChoiceFragment`) |
| `experiment_app_start_ttid` | A | time-to-initial-display instrumentation |
| `feature_flag_ai_tutor_android` | A | AI tutor availability (drives `State.isFeatureDisabled`) |
| `feature_flag_last_call_discount` | A | final-discount paywall |
| `abt_experiments_key` | A (prefs) | local cache of A/B assignment |

> Caution applied here: the DEX also contains `ff_*` keys (e.g. `ff_policy`, `ff_coppa`,
> `ff_google_adid_disabled`). Those are **Adjust SDK internals**, not Mimo feature flags, and
> are excluded from this table deliberately.

## 3. Remote discount engine (V) — the most complex remote-config object in the app

`RemoteConfigDiscount(start_date, days_running, rive_animation_url, image_url, image_url_dark,
title, body, activation_info, show_timer, call_to_action, skip_button_cta, banner_info)` with
sub-objects `RemoteConfigDiscountActivationInfo(title, body)`,
`RemoteConfigDiscountBannerInfo(title, cta)`, a mirrored `RemoteDiscountContent`, a local-theme
variant `LocalDiscountTheme(start_date, title, copy, image_url, image_url_dark,
path_banner_title)`, and pricing shapes `DiscountedSubscription(withoutFreeTrial,
with7DaysFreeTrial, with14DaysFreeTrial, discountPercent)` and
`PriceReduction$CurrentDiscount(reductionApplied, fullPriceAmount)`.

Interpretation: **the entire offer — animation, both illustrations (light/dark), copy, CTA,
skip CTA, banner, countdown — is server-configured**, so a discount campaign is a config change,
not a release. `days_running` + `show_timer` + `in_app_offer_countdown` give urgency; the dev
menu can force it (`setForceLastCallDiscountEnabled`, `setFakeRemoteDiscountEnabled`).

This is the single most transferable *commercial* mechanism in the app for an Iranian market:
campaign-driven pricing without app releases.

## 4. Consumption pattern (I, from class/state shapes)

```
app start
 ├─ FirebaseRemoteConfig.fetchAndActivate()            (plane A; A/B assignments arrive here)
 ├─ /v2/client-config                                   (plane B; tabs, bundles)
 ├─ parse content experiment (originalTrackId → variantTrackId if user in visibilityPercentage)
 └─ build UI state per feature; each gate reads a single boolean
failure: last-known values from prefs (abt_experiments_key); feature falls back to default (I)
```

## 5. Override surface

`DevMenuRemoteConfigActivity` (`addItem`/`removeItem`) lets an internal user inject any key/value
at runtime; `ABTestConfigActivity` inspects assignments;
`DevelopersMenuContentExperimentActivity` writes a content experiment from a JSON template
(`{"originalTrackId":50,"variantTrackId":80,"visibilityPercentage":100}`). All three are
client-local overrides (I), i.e. they do not affect the server's experiment accounting.

## 6. Governance observations

* Two config planes + a third content plane means **the same behaviour can be controlled from
  three places**; the risk is a flag set in Firebase being overridden by `/v2/client-config`
  (precedence is not statically discoverable — **UNKNOWN**, and this is the most important open
  question in this document).
* Every experiment is `*_android`-suffixed ⇒ independent iOS rollout; cross-platform consistency
  is a manual process.
* No expiry mechanism is visible for keys: stale experiment keys accumulate (V: keys with
  `_v2` and `_android` suffixes coexist).

## 7. Konkur transfer

| Mechanism | Verdict | Konkur form |
|---|---|---|
| Firebase A/B for UI experiments | **Exclude** | Firebase availability in Iran is unreliable; use self-hosted flags |
| `/v2/client-config` bundle | **Reuse** | Single source for tab set, feature bundles, exam-year content pointers |
| Content experiment with `visibilityPercentage` | **Reuse** | Perfect for piloting a new question bank or a new plan generator on 5% of students |
| Remote-configured discount object | **Reuse** | Iranian pricing campaigns change weekly; avoid app releases |
| Dev-menu overrides | **Reuse (internal builds only)** | — |
| Three config planes | **Exclude** | One flag service, one precedence rule, documented |
