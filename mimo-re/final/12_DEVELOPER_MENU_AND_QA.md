# 12 — Developer Menu: the production-shipped control room

**55 classes** under `com.getmimo.ui.developermenu` ship in the 9.35 production APK (measured:
`grep -c developermenu` over `data/all-classes.txt` = 55 named classes plus lambdas). This is the
single most revealing subsystem for anyone who wants to know how Mimo operates its product.

## 1. Class inventory (V)

| Group | Classes |
|---|---|
| Root | `DeveloperMenuActivity`, `DeveloperMenuFragment` (+ 9 lambdas), `DeveloperMenuViewModel` (+4 named coroutines) |
| A/B testing | `abtest/ABTestConfigActivity` |
| Remote config | `remoteconfig/DevMenuRemoteConfigActivity`, `DevMenuRemoteConfigViewModel` (`addItem`, `removeItem`, `map` flows) |
| Content experiments | `contentexperiment/DevelopersMenuContentExperimentActivity` |
| Discounts | `discount/DeveloperMenuDiscountActivity`, `DeveloperMenuDiscountViewModel` (`resetDiscountCountdown`, `setFakeRemoteDiscountEnabled`, `setFakeRemoteDiscountImageEnabled`, `setForceLastCallDiscountEnabled`) |
| Campaign / attribution | `campaign/DeveloperMenuCampaignActivity`, `DeveloperMenuCampaignViewModel` (`loadCampaignInfo`) |
| View galleries | `modaldialog/ModalDialogTestActivity`, `viewcomponents/customviews/CustomViewsActivity`, `view/FakeLeaderboardsResultBottomSheetDialogFragment`, `view/FakeStreakBottomSheetDialogFragment` |
| Modals | `ui.introduction.ModalData$DeveloperMenuDownloadLiveContent`, `…$DeveloperMenuLiveDeploymentError` |

## 2. Capabilities, with the literals that prove each one

| Capability | Evidence (V) |
|---|---|
| Show exact build identity | `9.35 (1792759685)` literal |
| Show auth identity | `Authenticated with: firebase`, `not supported` |
| Copy push registration id / in-app messaging token to clipboard | `push_notification_registration_id`, `In_app messaging token`, `Copied to clipboard` |
| Reset the push token | `Push notification token reset.`, `DeveloperMenuViewModel$resetPushToken` |
| Clear local cache | `Cleared the cache successfully.` / `Error while clearing the cache.` |
| Download & unzip an **unpublished** content package | `downloadAndUnzipUnpublishedPackage`, `ModalData$DeveloperMenuDownloadLiveContent` |
| Surface live-deploy errors | `ModalData$DeveloperMenuLiveDeploymentError` |
| Open the "lesson variations" chapter (hard-mode/variant lessons) | `openLessonsVariationsChapter`, `Lesson Variations Chapter not found` |
| Override **any** remote-config key at runtime | `DevMenuRemoteConfigActivity` + `addItem`/`removeItem` |
| Inspect / force A/B test variants | `ABTestConfigActivity` |
| Author a **content experiment** inline | `DevelopersMenuContentExperimentActivity` with a JSON template `{"originalTrackId": 50, "variantTrackId": 80, "visibilityPercentage": 100}` |
| Force discount states | `setFakeRemoteDiscountEnabled`, `setForceLastCallDiscountEnabled`, `in_app_offer_countdown`, `reactivate_pro_discount_end_date` |
| Inspect entitlement state | `Tier: …`, `entitlement: …`, `expiration: …`, `cancelled: …` |
| Inspect attribution | `marketing_campaign`, `Organic user`, `Paid user`, `Undefined`, `Disabled`, `No campaign, user is organic` |
| Render any modal | `ModalDialogTestActivity` |
| Render any custom view | `CustomViewsActivity` |
| Fake leaderboards / fake streak for screenshots | `FakeLeaderboardsResultBottomSheetDialogFragment`, `FakeStreakBottomSheetDialogFragment` |

Live content delivery runs on **Pusher** (V): `AwesomeModePusherUseCase`, `PusherUpdates`,
`pusher/client/channel/ChannelState`, `PresenceSubscriptionData`, with app-specific error states
`pusher_quota_reached` and `pusher_connection_unauthorised`. The only event endpoint literal is
`/v1/user/events/subscribe` (V); the Pusher channel-authorisation path is not a string literal
(U — most likely composed at runtime from the base URL).

## 3. What this tells us about their process

1. **Content is deployed without an app release.** The combination of "download unpublished
   package", "Pusher update", "draft render endpoint" and "live deployment error" modal means
   authors push lesson changes to devices in seconds. Mimo's release train is not their content
   cadence.
2. **Every product decision is overridable.** Remote config, A/B assignment, experiments and
   discounts can all be forced from one screen — which is how they demo paywalls and test
   offer copy in-house.
3. **Screenshot/social production is a first-class need.** Dedicated fake-leaderboard and
   fake-streak sheets exist purely to generate marketing screenshots without touching real
   accounts. That is a mature content-marketing workflow.
4. **Attribution is debugged in-app**: `marketing_campaign` + organic/paid/undefined states.
5. **The variant system is content-aware**: the "lesson variations chapter" is a real chapter
   in the content that contains the alternative lessons, so QA can see all variants in one place.

## 4. Risk assessment (this is where the report should be blunt)

| Risk | Assessment |
|---|---|
| Reachability | **Low.** No exported component leads to `DeveloperMenuActivity` (V: manifest). It must be unlocked by an in-app gesture or remote flag (U). |
| Remote-config override | **High impact if reached** — an attacker on a rooted device with the menu open can force entitlements, discounts and experiments locally. But overrides are client-side only; server-side entitlement checks still apply (I, from `/v1/subscribers/*` and RevenueCat). |
| Live content download | Downloads an **unpublished** pack into app storage. Content is signed by TLS only; no asset signature check observed (U). A MITM with a trusted CA could inject arbitrary lesson markup. Markup is rendered in a WebView for `<webview>` blocks — so malformed/injected content could attempt WebView abuse. |
| Token display | Push token and in-app messaging token are copyable — normal for a debug menu, unacceptable for production. |
| Recommend | Strip the menu in release via a build flag; keep it in internal tracks. Mimo did not. |

## 5. Konkur transfer

Build a **smaller but similar** internal console, and keep it out of production:
* toggle any feature flag / quota locally;
* force plan states (free / trial / paid / expired) without touching billing;
* render any modal/sheet for design review;
* fake streak/leaderboard screenshots;
* generate a fake attempt history to test the weakness model;
* preview an unpublished question pack.

The two items with the highest return for Konkur are **flag overrides** (because you will ship
dozens of plan/paywall variants) and **fake attempt history** (because your whole adaptive value
depends on the weakness model, and QA needs to see it with realistic data).
