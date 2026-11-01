# 01 — Complete component inventory

All counts below are produced by `tools/export_manifest_resources.py`,
`tools/screen_inventory.py` and `tools/dex_evidence.py`; raw data in
`evidence/components.json`, `evidence/screens.json`, `evidence/dex-inventory.json`.

## 1. Package and build identity

| Property | Value | Class |
|---|---|---|
| Package | `com.getmimo` | VERIFIED STATIC |
| Version name / code | 9.35 / 1792759685 | VERIFIED STATIC |
| minSdk / targetSdk | 28 / 36 | VERIFIED STATIC |
| Application class | `com.getmimo.App` | VERIFIED STATIC |
| APK size / DEX files | 142,353,499 B / 12 (`classes.dex` … `classes12.dex`) | VERIFIED STATIC |
| Classes (total / `com.getmimo`) | 29,454 / 3,133 | VERIFIED STATIC |
| Unique DEX string literals | 105,611 | VERIFIED STATIC |
| `assets/` payload | ~623 MB (10 language packs, webview assets, test fixtures) | VERIFIED STATIC |
| Signing | self-signed, CN `youarefinished`, 2021-11-20 → 2046-11-14 | VERIFIED STATIC |
| Obfuscator | Smob v4.6 watermark string in DEX (`Smob - Mod obfuscation tool v4.6 by Kirlif'`) | VERIFIED STATIC |
| `allowBackup` | `false` | VERIFIED STATIC |
| `debuggable` | absent | VERIFIED STATIC |
| `networkSecurityConfig` | absent (platform defaults, cleartext blocked at targetSdk 36) | VERIFIED STATIC |
| Native libs | none observed for course logic; sandbox execution is remote | VERIFIED STATIC |

## 2. Manifest components

| Kind | Count | Notes |
|---|---|---|
| Activities | 61 (36 `com.getmimo`) | 8 exported, all justified by deep links or Firebase flows |
| Services | 19 | Firebase Messaging, WorkManager, RevenueCat, Adjust, Customer.io, widget refresh |
| Providers | 8 | FileProvider, FirebaseInit, WorkManager/Startup, `androidx` initialisers |
| Broadcast receivers | 20 | attribution, boot/refresh, in-app messaging |

Exported components (VERIFIED STATIC, from `evidence/components.json`):

| Component | Filters | Exposure |
|---|---|---|
| `com.getmimo.ui.SplashActivity` | 3 | `https|mimo://getmimo.com/login`, `/register`, `/deeplink/continuelearning`, `/deeplink/support` |
| `com.getmimo.ui.MainActivity` | 3 | `https|mimo://getmimo.com/profile`, `/learn/.*` (pathPattern) |
| `com.facebook.CustomTabActivity` | 2 | `fbconnect://cct.com.getmimo` |
| `com.canhub.cropper.CropImageActivity` | 1 | third-party crop flow (profile image) |
| `firebase.auth.internal.GenericIdpActivity` | 0 | `genericidp://firebase.auth/`, `singleTask` |
| `firebase.auth.internal.RecaptchaActivity` | 0 | `recaptcha://firebase.auth/`, `singleTask` |
| `saschpe.android.customtabs.WebViewActivity` | 0 | in-app browser |
| `androidx.compose.ui.tooling.PreviewActivity` | 0 | **QA tooling shipped to production** (see §17) |

The last row is a real finding: `PreviewActivity` exists in release builds only when
`ui-tooling` is packaged as a runtime dependency. It is exported and unfiltered, i.e. any
app on the device can launch it, but it renders a `@Preview` composable by name and holds no
course state. Its presence is an audit smell, not an exploit.

## 3. Screen-bearing classes

| Surface | Count | Source |
|---|---|---|
| Activities | 61 | manifest |
| Fragments (`*Fragment`) | 22 | class names |
| `ModalData` modal variants | 22 | `ui.introduction.ModalData$*` |
| Bottom sheets (`*BottomSheet*`) | 87 | class names |
| Dialogs (`*Dialog*`) | 44 | class names |
| ViewModels matching `*ViewModel` | 9 (named) + many obfuscated | class names — **undercount by design**, R8 renames most |
| Widget classes | 19 | `ui.widget.*` (Glance) |
| XML layouts | 809 | `res/layout/` |
| Compose screens | 4 name-visible + many obfuscated | `*Screen`/`*Kt` literals |
| Navigation graph resources | 1 (`nav_onboarding_graph.xml`) | `res/navigation/` |
| App string resources | 1,721 (116 locales) | `evidence/resources.json` |
| Locales (content packs) | 10: en, de, fr, es, it, pt, pl, ru, tr, id | `assets/lessons-*` |

The **22 onboarding fragments** are the single biggest concentration of UI surface in the app
(12 of the 22 fragments below are onboarding steps):

`OnboardingSelectPathContainerFragment`, `OnboardingDevicePreferenceFragment`,
`OnboardingDeviceReassuranceFragment`, `OnboardingMotiveReassuranceFragment`,
`OnboardingPathReassuranceFragment`, `OnboardingPreparingCurriculumFragment`,
`OnboardingSetDailyGoalFragment`, `OnboardingSkillPreferenceFragment`,
`SetExperienceFragment`, `SetMotiveFragment`, `SetOccupationFragment`,
`SetWorkFunctionFragment` (plus `AskForNameFragment`, `HonestFreeTrialFragment`,
`TrialReminderChoiceFragment`, `SetReminderTimeFragment`, `PathCompletionEstimationFragment`,
`IntroductionFragment`, `NameCodePlaygroundFragment`, `ProfileFragment`,
`SettingsFragment`, `DeveloperMenuFragment`).

## 4. Third-party SDK weight (class counts under `com.*`)

| Vendor | Classes | Function observed |
|---|---|---|
| Google (Firebase, Play, GMS, material) | 5,718 | auth, messaging, remote config, in-app messaging, billing, crash |
| RevenueCat | 2,436 | entitlements / paywall |
| Rive | 983 | vector animations (streak, chapter end) |
| AndroidX Compose | 786 | AI tutor sheet, coding keyboard, some lesson chrome |
| Customer.io | 351 | lifecycle messaging |
| Adjust | 315 | install attribution |
| AndroidX Glance | 196 | streak widget |
| Retrofit/OkHttp/kotlinx | bundled | transport |
| Smob | obfuscation | whole DEX |

## 5. Subsystem map (package → responsibility)

| Package | Responsibility |
|---|---|
| `ui.lesson.interactive.*` | markup lesson player (interactions, hints, module visibility) |
| `ui.lesson.executable.*` | code lesson player (editor, console, tests, see-solution) |
| `ui.projects.*` | playground/projects, coding keyboard, autosave |
| `ui.aitutor.*` | AI tutor bottom sheet, chat, prompt suggestions |
| `ui.practice.*` | practice hub, filters, stats |
| `ui.developermenu.*` | 55 classes of QA/ops tooling |
| `data.content.*` | track/tutorial/chapter/lesson models + **lessonparser** |
| `data.source.local.*` | Room DB, prefs, repositories (per domain) |
| `core.model.*` | streak, coins, keys, lesson executables |
| `interactors.*` | use-cases (freemium quota, progress writers) |
| `analytics.*` | 305 typed `Property` classes + Mixpanel/Segment-style pipeline |

## 6. Deliberately not in this inventory

* Firebase project IDs, API keys and client secrets were found in the manifest/AXML and are
  **not reproduced** — they are public-in-APK by design but out of scope per the mission rules
  (no credential disclosure). All are shaped as standard Firebase/Google keys and carry no
  server access beyond what a normal install has.
* Anything that would require a runtime session (actual endpoint responses, prompt outputs,
  paywall prices). See §21.
