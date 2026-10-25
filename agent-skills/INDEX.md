# فهرست مهارت‌ها

> این فایل **خودکار** ساخته می‌شود: `python3 agent-skills/tools/build_index.py`
> دستی ویرایش نکنید.

قبل از هر کار، `agent-skills/PROJECT-RULES.md` را بخوانید. سپس فقط مهارت مرتبط
با کار جاری را باز کنید — نه همه را.

## نقشهٔ سریع فازها

| کار جاری | اول از کجا بخوانم |
|---|---|
| build، AGP، R8، اندازهٔ APK | `vendor/android-official-skills/` (جست‌وجوی نام مهارت) + `android/skills` R8 |
| ViewModel، UiState، Flow، side-effect | `vendor/chrisbanes-skills/skills/compose-state-and-effects/` و `kotlin-concurrency-and-flow/` |
| نوشتن/اصلاح صفحهٔ Compose | `vendor/compose-kotlin-agent-skills/SKILL.md` + `references/02-compose-ui.md` + `00-banned-antipatterns.md` |
| Room، DAO، migration | `vendor/android-agent-skills/skills/android-room-database/` |
| اسکنر CameraX + ML Kit | `vendor/android-official-skills/camera/camerax/` + `vendor/compose-kotlin-agent-skills/references/12-camera-mlkit.md` |
| اعلان محلی و WorkManager (فاز H) | `vendor/android-agent-skills/skills/android-workmanager-notifications/` |
| تست UI / instrumentation / ADB | `vendor/android-testing-skills/` |
| بازبینی معماری با شدت‌بندی | `vendor/android-review/skills/` (هفت حوزه) |
| بازبینی UX و جریان کاربر | `vendor/mobile-app-ux-auditor-skill/skills/mobile-app-ux-auditor/` |

---

## مهارت‌های رسمی اندروید — `android/skills`

- نقش: **core** · لایسنس: Apache-2.0 · commit: `4ebabf2b0f`
- کِی: هر تغییر در build، Compose، اسکنر، انتشار یا مهاجرت
- تعداد مهارت یافت‌شده: **33**

| مهارت | چه کاری می‌کند | مسیر |
|---|---|---|
| `agp-9-upgrade` | Upgrades, or migrates, an Android project to use Android Gradle Plugin (AGP) version 9. Do not use this skill for migrating Kotlin Multiplatform (KMP) projects. | `vendor/android-official-skills/build-system/agp/agp-9-upgrade` |
| `camerax` | Provide technical guidance for Android camera development with CameraX. Use when implementing camera features, handling asynchronous recording lifecycles, wiring low-lev… | `vendor/android-official-skills/camera/camerax` |
| `android-for-cars-parked-apps` | Adapt existing Android video streaming apps, games, and web browsers to run as parked apps on Android Auto and Android Automotive OS. Covers manifest configuration, Goog… | `vendor/android-official-skills/cars/android-for-cars-parked-apps` |
| `appfunctions` | Analyzes Android apps to identify key user workflows for AppFunctions such as creating a note, playing media, or sending an automated or AI agent triggered message, voic… | `vendor/android-official-skills/device-ai/appfunctions` |
| `litert-lm` | Builds an Android app that runs an open text LLM on the device, on the CPU or the GPU, with the LiteRT-LM Kotlin API (com.google.ai.edge.litertlm:litertlm-android). Use… | `vendor/android-official-skills/device-ai/litert/litert-lm` |
| `litert-runtime` | Configures and implements LiteRT (.tflite) on-device inference on Android in Kotlin using the CompiledModel API on CPU and GPU. Use this skill for any Android LiteRT or… | `vendor/android-official-skills/device-ai/litert/litert-runtime` |
| `ml-kit-genai-prompt-api` | Analyzes Android codebases to implement ML Kit GenAI Prompt API. Use this skill to send natural language requests on-device to Gemini Nano, use structured output with Pr… | `vendor/android-official-skills/device-ai/ml-kit-genai-prompt-api` |
| `android-cli` | Provides instructions for installing and using the `android` CLI. The `android` command-line tool is a critical tool for Android development and helps you create new And… | `vendor/android-official-skills/devtools/android-cli` |
| `restore-credentials` | Provides knowledge and workflows to implement Android's Restore Credentials feature using the androidx.credentials library. Use this skill to create, sign in with, and d… | `vendor/android-official-skills/identity/restore-credentials` |
| `verified-email` | Provides a complete workflow for implementing verified email retrieval on Android Credential Manager API. Use this skill to integrate a secure, OTP-less email verificati… | `vendor/android-official-skills/identity/verified-email` |
| `adaptive` | Instructions to make or update an app's UI so that it adapts to different Android devices including phones, tablets, foldables, laptops, desktop, TV, Auto, and XR. It in… | `vendor/android-official-skills/jetpack-compose/adaptive` |
| `jetpack-compose-performance` | Diagnose and optimize Android Jetpack Compose UI code. Use this skill when analyzing performance bottlenecks of existing code to minimize recomposition overhead and prev… | `vendor/android-official-skills/jetpack-compose/jetpack-compose-performance` |
| `migrate-xml-views-to-jetpack-compose` | Provides a structured workflow for migrating an Android XML View to Jetpack Compose. This skill details the step-by-step process, from planning and dependency setup, to… | `vendor/android-official-skills/jetpack-compose/migration/migrate-xml-views-to-jetpack-compose` |
| `styles` | Use this skill to integrate the Jetpack Compose Styles API into an Android project. This skill guides you through upgrading dependencies, setting up component themes, ma… | `vendor/android-official-skills/jetpack-compose/theming/styles` |
| `media3-cast-integration` | Implements Google Cast support in Android apps using Jetpack Media3. Handles adding build dependencies, updating manifest, configuring OptionsProvider, and managing Cast… | `vendor/android-official-skills/media/media3-cast-integration` |
| `navigation-3` | Learn how to install and migrate to Jetpack Navigation 3, and how to implement features and patterns such as deep links, multiple backstacks, scenes (dialogs, bottom she… | `vendor/android-official-skills/navigation/navigation-3` |
| `navigation-event` | Intercept back gestures and run Predictive Back animations using the NavigationEvent (androidx.navigationevent) library in Compose Android. Handles Activity setup, paren… | `vendor/android-official-skills/navigation/navigation-event` |
| `anr-audit-and-fix` | Audits Android codebases for ANR risks and diagnoses ANR stack dumps. Use this skill when scanning Android code for ANR risks or triaging ANR stack dumps. Don't use for… | `vendor/android-official-skills/performance/anr-audit-and-fix` |
| `r8-analyzer` | Analyzes Android build files and R8 keep rules to identify redundancies, broad package-wide rules, and rules that subsume library consumer keep rules. Use when developer… | `vendor/android-official-skills/performance/r8-analyzer` |
| `engage-sdk-integration` | Helps developers integrate, debug, and resolve Play Engage SDK implementation issues. Use when adding Engage SDK support, generating publishing code, mapping data classe… | `vendor/android-official-skills/play/engage-sdk-integration` |
| `play-billing-library-version-upgrade` | Use this skill when upgrading or migrating an Android project from any legacy Google Play Billing Library (PBL) version to the latest stable version of PBL. | `vendor/android-official-skills/play/play-billing-library-version-upgrade` |
| `play-policy-insights` | Automated auditor designed to verify Android applications against Google Play Policy domains. It cross-references static code analysis with Play Store declarations to ge… | `vendor/android-official-skills/play/play-policy-insights` |
| `android-profiler` | Records and analyzes Android performance data and diagnoses performance bottlenecks across user apps, system apps, and system services, even if the user does not explici… | `vendor/android-official-skills/profilers/android-profiler` |
| `android-intent-security` | Best practices for Android Intent security. Use this skill when auditing component configurations in AndroidManifest.xml activities, services, receivers) or source code… | `vendor/android-official-skills/security/android-intent-security` |
| `android-permissions-security` | Audits, detects gaps, and remediates Android permissions and IPC component security vulnerabilities. Use when reviewing AndroidManifest.xml, defining custom permissions,… | `vendor/android-official-skills/security/android-permissions-security` |
| `edge-to-edge` | Use this skill to migrate your Jetpack Compose app to add adaptive edge-to-edge support and troubleshoot common issues. Use this skill to fix UI components (like buttons… | `vendor/android-official-skills/system/edge-to-edge` |
| `glance-canonical-layouts` | Use this skill to create home screen widgets using Jetpack Glance Canonical Layouts from the Android Platform Samples project, or when asked to implement standard widget… | `vendor/android-official-skills/system/glance-canonical-layouts` |
| `testing-setup` | Analyze and create a testing strategy for Android apps - install testing libraries, set up test infrastructure, create harnesses for unit tests, UI tests, screenshot tes… | `vendor/android-official-skills/testing/testing-setup` |
| `leanback-to-compose-tv-migration` | Provides instructions and architectural patterns for migrating Android TV applications from legacy Leanback UI Toolkit, Android Views, or Support Fragments to Jetpack Co… | `vendor/android-official-skills/tv/leanback-to-compose-tv-migration` |
| `wear-compose-m3` | Guidance for Wear OS Compose Material3 (Wear Compose Material 3 / Wear Compose Material3) watch and wearable apps. Covers creating, updating, and migrating projects (Mat… | `vendor/android-official-skills/wear/wear-compose-m3` |
| `wear-widgets` | Create, migrate, update, and verify Wear OS widgets using Glance Wear and Remote Compose in an Android project. Use this skill when implementing GlanceWearWidget, Glance… | `vendor/android-official-skills/wear/wear-widgets` |
| `display-glasses-with-jetpack-compose-glimmer` | Provides guidelines for developing projected Android XR apps for display glasses using the Jetpack Compose Glimmer UI toolkit. Covers Glimmer design principles, workflow… | `vendor/android-official-skills/xr/display-glasses-with-jetpack-compose-glimmer` |
| `projected-hardware` | Provides instructions and workflows for accessing and managing hardware on Android XR projected devices, such as audio glasses and display glasses. Use this skill when b… | `vendor/android-official-skills/xr/projected-hardware` |

## بازبینی فنی عمیق (state، effect، concurrency، API) — `chrisbanes/skills`

- نقش: **core** · لایسنس: Apache-2.0 · commit: `6c30c500c3`
- کِی: طراحی ViewModel/UiState، Flow، side-effect و بازبینی کد Compose
- تعداد مهارت یافت‌شده: **19**

| مهارت | چه کاری می‌کند | مسیر |
|---|---|---|
| `android-benchmark-comparison` | Use when comparing physical Android benchmark configurations, investigating inconsistent rankings, or selecting an Android default from measured results. Do not use for… | `vendor/chrisbanes-skills/skills/android-benchmark-comparison` |
| `compose-animations` | Use when writing or reviewing Jetpack Compose motion: visibility enter/exit, animating one property toward a target, color or size transitions, multiple properties from… | `vendor/chrisbanes-skills/skills/compose-animations` |
| `compose-component-design` | Use when designing or reviewing reusable Jetpack Compose component APIs with modifier parameters, root layout placement, caller-provided variable content, primitive cont… | `vendor/chrisbanes-skills/skills/compose-component-design` |
| `compose-focus-navigation` | Use when writing or reviewing Jetpack Compose UI for TV, keyboard, desktop, accessibility focus, D-pad navigation, FocusRequester, focusProperties, key events, or initia… | `vendor/chrisbanes-skills/skills/compose-focus-navigation` |
| `compose-performance` | Use when investigating Jetpack Compose recomposition cost, compiler stability reports, skippability, unstable parameters, frame-rate State reads, cross-phase snapshot ba… | `vendor/chrisbanes-skills/skills/compose-performance` |
| `compose-state-and-effects` | Use when writing or reviewing Jetpack Compose state ownership, remember state, state hoisting, screen state holders, LaunchedEffect, DisposableEffect, SideEffect, Flow c… | `vendor/chrisbanes-skills/skills/compose-state-and-effects` |
| `compose-ui-testing-patterns` | Use when writing or reviewing Jetpack Compose UI tests, screenshot tests or baseline-recording evidence, previews, semantics assertions, fake image loading, keyboard inp… | `vendor/chrisbanes-skills/skills/compose-ui-testing-patterns` |
| `deliver-spec` | Use when explicitly asked to deliver an approved GitHub or local spec through a reviewed pull request, or when a Project controller delegates one claimed implementation… | `vendor/chrisbanes-skills/skills/deliver-spec` |
| `gradle-run` | Use when planning to execute Gradle through `gradle`, `./gradlew`, or a custom `gradlew*` wrapper script, or diagnosing a Gradle build, recovering a workflow's status, c… | `vendor/chrisbanes-skills/skills/gradle-run` |
| `grounded-writing` | Use when drafting or reviewing public developer documentation, other text the user will publish or send, or a user-owned draft under an explicit editorial review, includ… | `vendor/chrisbanes-skills/skills/grounded-writing` |
| `implement-with-subagents` | Use when implementing supplied tickets or plan tasks with solo or worker-owned implementation selected from the task graph, or when reviewing that orchestration. | `vendor/chrisbanes-skills/skills/implement-with-subagents` |
| `kotlin-api-design` | Use when designing or reviewing Kotlin function ownership, member or extension functions, factories, single-field domain types, value classes, data classes, Kotlin Multi… | `vendor/chrisbanes-skills/skills/kotlin-api-design` |
| `kotlin-concurrency-and-flow` | Use when writing or reviewing Kotlin coroutine scope ownership, raw Thread or Executor work, init launches, non-suspending launch APIs, runBlocking, cancellation, StateF… | `vendor/chrisbanes-skills/skills/kotlin-concurrency-and-flow` |
| `kotlin-control-flow` | Use when writing or reviewing Kotlin branching and control flow: when expressions, guard conditions, sealed type exhaustiveness, smart casts, nullable branching, early r… | `vendor/chrisbanes-skills/skills/kotlin-control-flow` |
| `release-kotlin-library` | Use when preparing, publishing, or checking readiness for a Kotlin library release, including verifying its gradle-maven-publish-plugin prerequisite, reconciling changel… | `vendor/chrisbanes-skills/skills/release-kotlin-library` |
| `run-github-project` | Use when asked to set up, review, or operate a repository's GitHub Project workflow, including ready claims, role-labelled human work, unknown remote mutation outcomes,… | `vendor/chrisbanes-skills/skills/run-github-project` |
| `shepherd` | Use when asked to shepherd, babysit, monitor, or poll open pull requests or merge requests, including triaging review feedback, CI failures, and routine follow-up. | `vendor/chrisbanes-skills/skills/shepherd` |
| `to-plan` | Use when asked for an implementation plan or execution contract for one or more GitHub issues or an in-chat task, including a read-only review of the next safe step, wit… | `vendor/chrisbanes-skills/skills/to-plan` |
| `using-chrisbanes-skills` | Use when routing Kotlin or Jetpack Compose work, or physical Android benchmark evidence that needs a configuration decision, especially when several Kotlin or Compose co… | `vendor/chrisbanes-skills/skills/using-chrisbanes-skills` |

## مکمل تخصصی Compose + Kotlin — `haidrrrry/compose-kotlin-agent-skills`

- نقش: **core** · لایسنس: MIT · commit: `3851303e27`
- کِی: نوشتن یا اصلاح هر صفحهٔ Compose
- تعداد مهارت یافت‌شده: **4**

| مهارت | چه کاری می‌کند | مسیر |
|---|---|---|
| `compose-kotlin-agent-skills` | Enterprise Android/Kotlin skill for 2026 — Kotlin 2.x K2 compiler, AGP 9, Navigation 3, edge-to-edge Compose, strict MVI with atomic _state.update, banned AI antipattern… | `vendor/compose-kotlin-agent-skills` |
| `android-kotlin-architecture` | Enforces Clean Architecture, MVVM/MVI, and unidirectional data flow for Android apps. Covers UiState, UiEvent, UiEffect, UseCase boundaries, module structure, and atomic… | `vendor/compose-kotlin-agent-skills/skills/android-kotlin-architecture` |
| `android-kotlin-compose` | Jetpack Compose UI engineering for 2026 — edge-to-edge, Material 3, recomposition stability, Modifier ordering, LazyColumn performance, and animations. Use when building… | `vendor/compose-kotlin-agent-skills/skills/android-kotlin-compose` |
| `android-kotlin-testing` | Android testing patterns — ViewModel unit tests with Turbine, Compose UI semantics, Hilt TestInstallIn fakes, coroutine test dispatchers, and release quality gates. Use… | `vendor/compose-kotlin-agent-skills/skills/android-kotlin-testing` |

## بازبینی ساختاری با شدت‌بندی — `liuyi0808/android-review`

- نقش: **core** · لایسنس: MIT · commit: `26fbdc8536`
- کِی: در پایان هر milestone و قبل از هر انتشار، نه بعد از هر تغییر کوچک
- تعداد مهارت یافت‌شده: **7**

| مهارت | چه کاری می‌کند | مسیر |
|---|---|---|
| `architecture` | Android application architecture standards using Clean Architecture, MVVM/MVI patterns, Hilt dependency injection, and modularization. Use when: designing app structure,… | `vendor/android-review/skills/architecture` |
| `compose-ui` | Jetpack Compose UI best practices and patterns for Material 3. Use when: writing or reviewing Compose UI code, implementing state hoisting, using side effects (LaunchedE… | `vendor/android-review/skills/compose-ui` |
| `kotlin-quality` | Kotlin code quality review for Android projects. Covers coroutine structured concurrency, Flow operators, null safety, type design (sealed classes, data classes, value o… | `vendor/android-review/skills/kotlin-quality` |
| `performance` | Audit Android (Kotlin/Compose) apps for performance issues and produce structured findings. Use when: app cold start exceeds 500ms, UI jank or dropped frames, memory lea… | `vendor/android-review/skills/performance` |
| `play-store` | Google Play Store submission and compliance checklist for Android apps, with special focus on financial/loan apps. Covers build config, permissions (including Contacts P… | `vendor/android-review/skills/play-store` |
| `privacy-audit` | Three-way privacy compliance audit for Android loan apps, verifying that the privacy policy, in-app disclosure dialogs, and code implementation are consistent. Use for p… | `vendor/android-review/skills/privacy-audit` |
| `security-audit` | Android application security audit based on OWASP MASVS v2.0 and Kotlin secure coding practices. Use when: writing or reviewing code involving sensitive data storage (Sh… | `vendor/android-review/skills/security-audit` |

## کتابخانهٔ ۳۴ مهارت پایه — `krutikJain/android-agent-skills`

- نقش: **phase** · لایسنس: MIT · commit: `c5bf6731b8`
- کِی: فقط مهارت مرتبط با کار جاری؛ کل مجموعهٔ ۳۴تایی به‌طور همزمان خوانده نمی‌شود
- تعداد مهارت یافت‌شده: **68**

| مهارت | چه کاری می‌کند | مسیر |
|---|---|---|
| `android-architecture-clean` | Apply clean architecture boundaries, use cases, repositories, and lifecycle-aware presentation models in Android projects. | `vendor/android-agent-skills/.github/skills/android-architecture-clean` |
| `android-ci-cd-release-playstore` | Automate Android CI, versioning, signing boundaries, release channels, and Play-ready delivery workflows. | `vendor/android-agent-skills/.github/skills/android-ci-cd-release-playstore` |
| `android-coil-compose` | Use Coil in Jetpack Compose with AsyncImage, painter variants, sizing, and accessible image loading patterns. | `vendor/android-agent-skills/.github/skills/android-coil-compose` |
| `android-compose-accessibility` | Make Compose interfaces accessible with semantics, announcements, contrast, focus order, and adaptive touch targets. | `vendor/android-agent-skills/.github/skills/android-compose-accessibility` |
| `android-compose-foundations` | Build Android UI with Jetpack Compose foundations, layouts, modifiers, theming, and stable component structure. | `vendor/android-agent-skills/.github/skills/android-compose-foundations` |
| `android-compose-performance` | Profile and improve Compose recomposition, layout, scrolling, startup, and rendering performance in Android apps. | `vendor/android-agent-skills/.github/skills/android-compose-performance` |
| `android-compose-state-effects` | Manage Compose state, remember APIs, side effects, snapshots, and lifecycle-aware collection without leaks or loops. | `vendor/android-agent-skills/.github/skills/android-compose-state-effects` |
| `android-compose-xml-interoperability` | Bridge Compose and the View system safely during incremental migrations, interoperability screens, and shared theming. | `vendor/android-agent-skills/.github/skills/android-compose-xml-interoperability` |
| `android-coroutines-flow` | Use coroutines, Flow, structured concurrency, dispatchers, and cancellation-safe Android async pipelines. | `vendor/android-agent-skills/.github/skills/android-coroutines-flow` |
| `android-di-hilt` | Wire Android dependency injection with Hilt, scopes, testing overrides, and module ownership boundaries. | `vendor/android-agent-skills/.github/skills/android-di-hilt` |
| `android-emulator-automation` | Use semantic ADB and UIAutomator workflows to inspect, launch, and interact with Android apps from agents. | `vendor/android-agent-skills/.github/skills/android-emulator-automation` |
| `android-gradle-build-logic` | Shape Android build logic with Gradle, version catalogs, plugins, convention patterns, and toolchain compatibility. | `vendor/android-agent-skills/.github/skills/android-gradle-build-logic` |
| `android-gradle-build-performance` | Diagnose and improve Android and Gradle build performance with scans, cache checks, and bottleneck audits. | `vendor/android-agent-skills/.github/skills/android-gradle-build-performance` |
| `android-kotlin-core` | Use Kotlin idioms safely in Android apps, including nullability, data classes, sealed types, extension functions, and collection pipelines. | `vendor/android-agent-skills/.github/skills/android-kotlin-core` |
| `android-local-persistence-datastore` | Persist lightweight user and app preferences with DataStore, schema-safe models, and migration-aware defaults. | `vendor/android-agent-skills/.github/skills/android-local-persistence-datastore` |
| `android-material3-design-system` | Apply Material 3 tokens, color, type, spacing, adaptive components, and theme ownership in Android apps. | `vendor/android-agent-skills/.github/skills/android-material3-design-system` |
| `android-media-files-sharing` | Use modern Android file, media, picker, FileProvider, and share-sheet APIs with minimal permissions. | `vendor/android-agent-skills/.github/skills/android-media-files-sharing` |
| `android-mobile-frontend-design` | Design Android mobile frontend experiences from scratch, improve existing screens, and fix UI issues with brand-forward, localization-safe, overflow-safe guidance across… | `vendor/android-agent-skills/.github/skills/android-mobile-frontend-design` |
| `android-modernization-upgrade` | Bring very old Android projects to a current supported baseline with staged upgrades, deprecated API replacement, 16 KB alignment checks, and explicit handoff to special… | `vendor/android-agent-skills/.github/skills/android-modernization-upgrade` |
| `android-modularization` | Design Android repositories with feature, core, and build-logic modules that scale without cyclic dependencies. | `vendor/android-agent-skills/.github/skills/android-modularization` |
| `android-navigation-deeplinks` | Handle navigation graphs, back stack behavior, app links, intents, and destination ownership for Android apps. | `vendor/android-agent-skills/.github/skills/android-navigation-deeplinks` |
| `android-networking-retrofit-okhttp` | Build Android networking stacks with Retrofit, OkHttp, interceptors, API contracts, and resilient error handling. | `vendor/android-agent-skills/.github/skills/android-networking-retrofit-okhttp` |
| `android-performance-observability` | Measure startup, rendering, memory, jank, vitals, logs, and crash signals for Android apps with actionable traces. | `vendor/android-agent-skills/.github/skills/android-performance-observability` |
| `android-permissions-activity-results` | Use modern permission requests, Activity Result APIs, and capability-gated UX in Android flows. | `vendor/android-agent-skills/.github/skills/android-permissions-activity-results` |
| `android-room-database` | Model Room entities, DAOs, transactions, migrations, schema exports, and test-safe local persistence. | `vendor/android-agent-skills/.github/skills/android-room-database` |
| `android-rxjava-to-coroutines-migration` | Migrate Android RxJava code to Kotlin coroutines and Flow with safe lifecycle-aware replacements. | `vendor/android-agent-skills/.github/skills/android-rxjava-to-coroutines-migration` |
| `android-security-best-practices` | Apply Android app security guidance around secrets, storage, network trust, exported components, and least privilege. | `vendor/android-agent-skills/.github/skills/android-security-best-practices` |
| `android-serialization-offline-sync` | Coordinate serialization, caching, conflict handling, and offline-first sync flows in Android apps. | `vendor/android-agent-skills/.github/skills/android-serialization-offline-sync` |
| `android-state-management` | Model screen state, events, reducers, and side effects for Android UIs with predictable lifecycle-aware ownership. | `vendor/android-agent-skills/.github/skills/android-state-management` |
| `android-testing-ui` | Validate Android UI behavior with Compose UI tests, Espresso-style checks, screenshot assertions, and accessibility verification. | `vendor/android-agent-skills/.github/skills/android-testing-ui` |
| `android-testing-unit` | Write fast, focused Android unit tests for reducers, use cases, repositories, and lifecycle-safe state holders. | `vendor/android-agent-skills/.github/skills/android-testing-unit` |
| `android-ui-states-validation` | Review Android UI flows for empty, loading, error, offline, and edge-case behavior before release. | `vendor/android-agent-skills/.github/skills/android-ui-states-validation` |
| `android-viewsystem-foundations` | Handle XML layouts, ConstraintLayout, Fragments, ViewBinding, DataBinding, and classic Android UI lifecycle patterns. | `vendor/android-agent-skills/.github/skills/android-viewsystem-foundations` |
| `android-workmanager-notifications` | Schedule reliable background work, reminders, and notification delivery with WorkManager and Android execution limits. | `vendor/android-agent-skills/.github/skills/android-workmanager-notifications` |
| `android-architecture-clean` | Apply clean architecture boundaries, use cases, repositories, and lifecycle-aware presentation models in Android projects. | `vendor/android-agent-skills/skills/android-architecture-clean` |
| `android-ci-cd-release-playstore` | Automate Android CI, versioning, signing boundaries, release channels, and Play-ready delivery workflows. | `vendor/android-agent-skills/skills/android-ci-cd-release-playstore` |
| `android-coil-compose` | Use Coil in Jetpack Compose with AsyncImage, painter variants, sizing, and accessible image loading patterns. | `vendor/android-agent-skills/skills/android-coil-compose` |
| `android-compose-accessibility` | Make Compose interfaces accessible with semantics, announcements, contrast, focus order, and adaptive touch targets. | `vendor/android-agent-skills/skills/android-compose-accessibility` |
| `android-compose-foundations` | Build Android UI with Jetpack Compose foundations, layouts, modifiers, theming, and stable component structure. | `vendor/android-agent-skills/skills/android-compose-foundations` |
| `android-compose-performance` | Profile and improve Compose recomposition, layout, scrolling, startup, and rendering performance in Android apps. | `vendor/android-agent-skills/skills/android-compose-performance` |
| `android-compose-state-effects` | Manage Compose state, remember APIs, side effects, snapshots, and lifecycle-aware collection without leaks or loops. | `vendor/android-agent-skills/skills/android-compose-state-effects` |
| `android-compose-xml-interoperability` | Bridge Compose and the View system safely during incremental migrations, interoperability screens, and shared theming. | `vendor/android-agent-skills/skills/android-compose-xml-interoperability` |
| `android-coroutines-flow` | Use coroutines, Flow, structured concurrency, dispatchers, and cancellation-safe Android async pipelines. | `vendor/android-agent-skills/skills/android-coroutines-flow` |
| `android-di-hilt` | Wire Android dependency injection with Hilt, scopes, testing overrides, and module ownership boundaries. | `vendor/android-agent-skills/skills/android-di-hilt` |
| `android-emulator-automation` | Use semantic ADB and UIAutomator workflows to inspect, launch, and interact with Android apps from agents. | `vendor/android-agent-skills/skills/android-emulator-automation` |
| `android-gradle-build-logic` | Shape Android build logic with Gradle, version catalogs, plugins, convention patterns, and toolchain compatibility. | `vendor/android-agent-skills/skills/android-gradle-build-logic` |
| `android-gradle-build-performance` | Diagnose and improve Android and Gradle build performance with scans, cache checks, and bottleneck audits. | `vendor/android-agent-skills/skills/android-gradle-build-performance` |
| `android-kotlin-core` | Use Kotlin idioms safely in Android apps, including nullability, data classes, sealed types, extension functions, and collection pipelines. | `vendor/android-agent-skills/skills/android-kotlin-core` |
| `android-local-persistence-datastore` | Persist lightweight user and app preferences with DataStore, schema-safe models, and migration-aware defaults. | `vendor/android-agent-skills/skills/android-local-persistence-datastore` |
| `android-material3-design-system` | Apply Material 3 tokens, color, type, spacing, adaptive components, and theme ownership in Android apps. | `vendor/android-agent-skills/skills/android-material3-design-system` |
| `android-media-files-sharing` | Use modern Android file, media, picker, FileProvider, and share-sheet APIs with minimal permissions. | `vendor/android-agent-skills/skills/android-media-files-sharing` |
| `android-mobile-frontend-design` | Design Android mobile frontend experiences from scratch, improve existing screens, and fix UI issues with brand-forward, localization-safe, overflow-safe guidance across… | `vendor/android-agent-skills/skills/android-mobile-frontend-design` |
| `android-modernization-upgrade` | Bring very old Android projects to a current supported baseline with staged upgrades, deprecated API replacement, 16 KB alignment checks, and explicit handoff to special… | `vendor/android-agent-skills/skills/android-modernization-upgrade` |
| `android-modularization` | Design Android repositories with feature, core, and build-logic modules that scale without cyclic dependencies. | `vendor/android-agent-skills/skills/android-modularization` |
| `android-navigation-deeplinks` | Handle navigation graphs, back stack behavior, app links, intents, and destination ownership for Android apps. | `vendor/android-agent-skills/skills/android-navigation-deeplinks` |
| `android-networking-retrofit-okhttp` | Build Android networking stacks with Retrofit, OkHttp, interceptors, API contracts, and resilient error handling. | `vendor/android-agent-skills/skills/android-networking-retrofit-okhttp` |
| `android-performance-observability` | Measure startup, rendering, memory, jank, vitals, logs, and crash signals for Android apps with actionable traces. | `vendor/android-agent-skills/skills/android-performance-observability` |
| `android-permissions-activity-results` | Use modern permission requests, Activity Result APIs, and capability-gated UX in Android flows. | `vendor/android-agent-skills/skills/android-permissions-activity-results` |
| `android-room-database` | Model Room entities, DAOs, transactions, migrations, schema exports, and test-safe local persistence. | `vendor/android-agent-skills/skills/android-room-database` |
| `android-rxjava-to-coroutines-migration` | Migrate Android RxJava code to Kotlin coroutines and Flow with safe lifecycle-aware replacements. | `vendor/android-agent-skills/skills/android-rxjava-to-coroutines-migration` |
| `android-security-best-practices` | Apply Android app security guidance around secrets, storage, network trust, exported components, and least privilege. | `vendor/android-agent-skills/skills/android-security-best-practices` |
| `android-serialization-offline-sync` | Coordinate serialization, caching, conflict handling, and offline-first sync flows in Android apps. | `vendor/android-agent-skills/skills/android-serialization-offline-sync` |
| `android-state-management` | Model screen state, events, reducers, and side effects for Android UIs with predictable lifecycle-aware ownership. | `vendor/android-agent-skills/skills/android-state-management` |
| `android-testing-ui` | Validate Android UI behavior with Compose UI tests, Espresso-style checks, screenshot assertions, and accessibility verification. | `vendor/android-agent-skills/skills/android-testing-ui` |
| `android-testing-unit` | Write fast, focused Android unit tests for reducers, use cases, repositories, and lifecycle-safe state holders. | `vendor/android-agent-skills/skills/android-testing-unit` |
| `android-ui-states-validation` | Review Android UI flows for empty, loading, error, offline, and edge-case behavior before release. | `vendor/android-agent-skills/skills/android-ui-states-validation` |
| `android-viewsystem-foundations` | Handle XML layouts, ConstraintLayout, Fragments, ViewBinding, DataBinding, and classic Android UI lifecycle patterns. | `vendor/android-agent-skills/skills/android-viewsystem-foundations` |
| `android-workmanager-notifications` | Schedule reliable background work, reminders, and notification delivery with WorkManager and Android execution limits. | `vendor/android-agent-skills/skills/android-workmanager-notifications` |

## تست: JVM، Room، Compose UI، ADB، instrumentation — `skydoves/android-testing-skills`

- نقش: **phase** · لایسنس: Apache-2.0 · commit: `8665ed5964`
- کِی: فاز G (تست UI و instrumentation) و هر وقت کار روی app-smoke یا تست گوشی
- تعداد مهارت یافت‌شده: **54**

| مهارت | چه کاری می‌کند | مسیر |
|---|---|---|
| `installing-and-managing-apps` | Use this skill to install, uninstall, list, inspect, and reset Android apps via `adb install` (with `-r` reinstall, `-d` allow-downgrade, `-t` allow test packages, `-g`… | `vendor/android-testing-skills/adb/apps/installing-and-managing-apps` |
| `understanding-adb-architecture` | Use this skill to reason about the three-piece ADB topology (client CLI, host server on TCP 5037, on-device daemon `adbd`), the lifecycle commands `adb start-server` / `… | `vendor/android-testing-skills/adb/architecture/understanding-adb-architecture` |
| `scripting-adb-for-ci` | Use this skill to wire `adb` reliably into CI — bash idioms, exit codes, parallel device fan-out with `xargs -P`, port forwarding (`adb forward` LOCAL REMOTE vs `adb rev… | `vendor/android-testing-skills/adb/automation/scripting-adb-for-ci` |
| `capturing-screenshots-and-screenrecord` | Use this skill to capture visual artefacts from a device for test failures, golden image generation, QA repro, and demo videos. Covers `adb shell screencap -p` (PNG scre… | `vendor/android-testing-skills/adb/capture/capturing-screenshots-and-screenrecord` |
| `injecting-input-and-state` | Use this skill to drive an Android device from the host shell — inject taps, swipes, text, key events, and drag-and-drop via `adb shell input`; resize the display with `… | `vendor/android-testing-skills/adb/control/injecting-input-and-state` |
| `connecting-over-wifi` | Use this skill to connect ADB to an Android 11+ device wirelessly with the modern `adb pair` flow (pairing code or QR via `Settings → Developer options → Wireless debugg… | `vendor/android-testing-skills/adb/devices/connecting-over-wifi` |
| `connecting-to-devices` | Use this skill to attach a USB device or emulator to ADB, list transports with `adb devices` / `adb devices -l`, disambiguate among multiple devices using `-s SERIAL`, `… | `vendor/android-testing-skills/adb/devices/connecting-to-devices` |
| `extracting-logs-with-logcat` | Use this skill to read device logs for test failures, debug, smoke testing, and CI repros. Covers `adb logcat` (stream), `adb logcat -d` (dump and exit), `adb logcat -c`… | `vendor/android-testing-skills/adb/observability/extracting-logs-with-logcat` |
| `running-instrumented-tests-via-adb` | Use this skill to run instrumented Android tests directly through `adb shell am instrument -w -r` without going through Gradle. Covers the required `-w` (wait — REQUIRED… | `vendor/android-testing-skills/adb/tests/running-instrumented-tests-via-adb` |
| `extracting-test-artifacts` | Use this skill to move files between host and device with `adb pull` and `adb push`, including the modern `-z` (compression), `-Z` (no compression), `--sync`, and `-a` (… | `vendor/android-testing-skills/adb/transfer/extracting-test-artifacts` |
| `clicking-and-scrolling` | Use this skill to drive Jetpack Compose UI from tests with the high-level action APIs that do not go through a gesture builder — performClick, performScrollTo, performSc… | `vendor/android-testing-skills/compose/actions/clicking-and-scrolling` |
| `entering-text` | Use this skill to drive Jetpack Compose text fields from tests with the text-specific actions — performTextInput (insert at cursor via the InsertTextAtCursor semantics a… | `vendor/android-testing-skills/compose/actions/entering-text` |
| `injecting-mouse-and-keyboard` | Use this skill to drive Jetpack Compose UI from tests with non-touch input — performMouseInput (click, rightClick, doubleClick, tripleClick, longClick, animateMoveTo, dr… | `vendor/android-testing-skills/compose/actions/injecting-mouse-and-keyboard` |
| `injecting-touch-gestures` | Use this skill to drive Jetpack Compose UI with synthetic touch events through performTouchInput and the TouchInjectionScope DSL — click, longClick, doubleClick, swipe,… | `vendor/android-testing-skills/compose/actions/injecting-touch-gestures` |
| `asserting-bounds-and-dimensions` | Use this skill to verify Compose layout measurements from a UI test using `assertWidthIsEqualTo`, `assertHeightIsEqualTo`, `assertWidthIsAtLeast`, `assertHeightIsAtLeast… | `vendor/android-testing-skills/compose/assertions/asserting-bounds-and-dimensions` |
| `asserting-node-state-and-text` | Use this skill to verify a Compose semantics node's properties from a UI test using `assertExists`, `assertDoesNotExist`, `assertIsDisplayed`, `assertIsNotDisplayed`, `a… | `vendor/android-testing-skills/compose/assertions/asserting-node-state-and-text` |
| `auditing-compose-test-suite` | Use this skill to perform an end-to-end review of an existing Jetpack Compose UI test file or test suite. Sequences six audit phases (setup correctness, finder disciplin… | `vendor/android-testing-skills/compose/audit/auditing-compose-test-suite` |
| `enabling-accessibility-checks` | Use this skill to enable Espresso's `AccessibilityValidator` against the Compose semantics tree via `enableAccessibilityChecks(...)` from `androidx.compose.ui:ui-test-ac… | `vendor/android-testing-skills/compose/debug/enabling-accessibility-checks` |
| `printing-the-semantics-tree` | Use this skill to diagnose "no node matched", "found N nodes", and "useUnmergedTree" failures by dumping the actual semantics tree with `printToLog(tag, maxDepth)` and `… | `vendor/android-testing-skills/compose/debug/printing-the-semantics-tree` |
| `composing-semantics-matchers` | Use this skill to build precise Compose UI test queries by composing `SemanticsMatcher` predicates with `infix and`, `infix or`, and `operator not`, plus the prebuilt fi… | `vendor/android-testing-skills/compose/finders/composing-semantics-matchers` |
| `finding-nodes-by-tag-text-content` | Use this skill to locate Compose semantics nodes from a UI test using `onNodeWithTag`, `onNodeWithText`, `onNodeWithContentDescription`, `onAllNodes*`, and `onRoot`. Cov… | `vendor/android-testing-skills/compose/finders/finding-nodes-by-tag-text-content` |
| `traversing-the-semantics-tree` | Use this skill to navigate from one Compose semantics node to its relatives via `onParent`, `onChildren`, `onChild`, `onChildAt`, `onSibling`, `onSiblings`, `onAncestors… | `vendor/android-testing-skills/compose/finders/traversing-the-semantics-tree` |
| `testing-with-espresso-interop` | Use this skill to mix Compose finders and Espresso `onView` in the same test — for Android `Dialog` windows, IME (soft keyboard) state, `ComposeView` inside an Android V… | `vendor/android-testing-skills/compose/interop/testing-with-espresso-interop` |
| `structuring-a-compose-test` | Use this skill to structure a Jetpack Compose UI test class the way androidx itself writes them — `@MediumTest` + `@RunWith(AndroidJUnit4::class)`, a single `createCompo… | `vendor/android-testing-skills/compose/patterns/structuring-a-compose-test` |
| `testing-lazy-lists` | Use this skill to test `LazyColumn`, `LazyRow`, and `LazyVerticalGrid` correctly — tag the container with `Modifier.testTag(...)`, tag each item by its key, scroll via t… | `vendor/android-testing-skills/compose/patterns/testing-lazy-lists` |
| `testing-state-restoration` | Use this skill to test `rememberSaveable` round-trips with `StateRestorationTester`, the only supported tool for proving Compose state survives process death and configu… | `vendor/android-testing-skills/compose/patterns/testing-state-restoration` |
| `capturing-preview-screenshots-in-ci` | Use this skill to render every Jetpack Compose `@Preview` as a screenshot on a real Android device or emulator and publish a browsable HTML catalog from CI. Covers the C… | `vendor/android-testing-skills/compose/preview/capturing-preview-screenshots-in-ci` |
| `developing-with-compose-previews` | Use this skill to make `@Preview` functions the primary feedback loop for Jetpack Compose UI work — preview-driven development. Covers hoisting state out of composables… | `vendor/android-testing-skills/compose/preview/developing-with-compose-previews` |
| `choosing-test-rule-vs-runtest` | Use this skill to pick the correct Compose UI test entry point. Compares `createComposeRule()`, `createAndroidComposeRule<A>()`, `createEmptyComposeRule()`, `runComposeU… | `vendor/android-testing-skills/compose/setup/choosing-test-rule-vs-runtest` |
| `configuring-test-dependencies` | Use this skill to wire the correct Gradle dependency matrix for Jetpack Compose UI tests. Covers `androidTestImplementation("androidx.compose.ui:ui-test-junit4")`, the `… | `vendor/android-testing-skills/compose/setup/configuring-test-dependencies` |
| `setting-up-host-vs-device-tests` | Use this skill to choose between host (Robolectric/JVM) and device (instrumentation) tests for Jetpack Compose, and to configure each correctly. Covers the `androidHostT… | `vendor/android-testing-skills/compose/setup/setting-up-host-vs-device-tests` |
| `validating-compose-stability` | Use this skill to gate CI on Jetpack Compose stability — catch when a composable becomes unskippable/unrestartable or a parameter goes stable → unstable, before it ships… | `vendor/android-testing-skills/compose/stability/validating-compose-stability` |
| `controlling-the-test-clock` | Use this skill to drive the Compose test clock by hand with MainTestClock — currentTime, autoAdvance, advanceTimeByFrame, advanceTimeBy(milliseconds, ignoreFrameDuration… | `vendor/android-testing-skills/compose/synchronization/controlling-the-test-clock` |
| `synchronizing-with-idle` | Use this skill to choose the right idle-synchronization primitive in Compose UI tests — waitForIdle, awaitIdle, waitUntil(conditionDescription, timeoutMillis, condition)… | `vendor/android-testing-skills/compose/synchronization/synchronizing-with-idle` |
| `testing-animations-deterministically` | Use this skill to write non-flaky Compose animation tests by setting mainClock.autoAdvance = false and stepping frames by hand with advanceTimeByFrame and advanceTimeBy(… | `vendor/android-testing-skills/compose/synchronization/testing-animations-deterministically` |
| `choosing-what-to-test` | Use this skill to pick which behaviors to cover in an Android test suite using Google's five-category state vocabulary plus the explicit "what NOT to test" list from `/t… | `vendor/android-testing-skills/fundamentals/concepts/choosing-what-to-test` |
| `understanding-the-testing-pyramid` | Use this skill to size an Android test suite using Google's small / medium / big scope vocabulary and the qualitative pyramid. Explains why most apps should hold "many s… | `vendor/android-testing-skills/fundamentals/concepts/understanding-the-testing-pyramid` |
| `picking-test-doubles` | Use this skill to pick the right test double — fake, mock, stub, spy, dummy, or Robolectric shadow — for an Android test. Encodes Google's verbatim preference order ("fa… | `vendor/android-testing-skills/fundamentals/doubles/picking-test-doubles` |
| `applying-testing-strategies` | Use this skill to apply Android-team testing strategies — determinism, hermetic execution, Given-When-Then / Arrange-Act-Assert structure, naming conventions, and Hilt-b… | `vendor/android-testing-skills/fundamentals/strategies/applying-testing-strategies` |
| `organizing-test-source-sets` | Use this skill to organize Android test source sets — `src/test/`, `src/androidTest/`, the community `src/sharedTest/` convention, and the modern KMP-style `androidHostT… | `vendor/android-testing-skills/fundamentals/strategies/organizing-test-source-sets` |
| `writing-espresso-tests` | Use this skill to write Espresso 3.7.0 tests against Android Views — `onView(matcher).perform(action).check(matches(...))`, `onData(...)` for `AdapterView`, `RecyclerVie… | `vendor/android-testing-skills/instrumentation/espresso/writing-espresso-tests` |
| `running-tests-on-gradle-managed-devices` | Use this skill to run instrumented Android tests on Gradle Managed Devices (GMD) — emulators that Gradle provisions, boots, runs tests on, and tears down, so CI and ever… | `vendor/android-testing-skills/instrumentation/managed-devices/running-tests-on-gradle-managed-devices` |
| `running-instrumented-tests-with-androidjunit4` | Use this skill to stand up an Android instrumentation test source set with the canonical `AndroidJUnit4` runner, the correct `AndroidJUnitRunner` Gradle wiring, and supp… | `vendor/android-testing-skills/instrumentation/runner/running-instrumented-tests-with-androidjunit4` |
| `launching-activities-with-activityscenario` | Use this skill to launch, drive, and tear down an Activity from an instrumentation test using `ActivityScenario` and the JUnit4 wrapper `ActivityScenarioRule`. Covers `A… | `vendor/android-testing-skills/instrumentation/scenarios/launching-activities-with-activityscenario` |
| `launching-fragments-with-fragmentscenario` | Use this skill to test a `Fragment` in isolation using `FragmentScenario`, `launchFragmentInContainer<F>()`, and `launchFragment<F>()`. Covers the `androidx.fragment:fra… | `vendor/android-testing-skills/instrumentation/scenarios/launching-fragments-with-fragmentscenario` |
| `cross-app-tests-with-uiautomator` | Use this skill to drive cross-app and system-UI flows from instrumentation tests using UiAutomator 2.3.0 — `UiDevice`, `BySelector` / `UiObject2` (modern), `UiSelector`… | `vendor/android-testing-skills/instrumentation/uiautomator/cross-app-tests-with-uiautomator` |
| `testing-coroutines-with-runtest` | Use this skill to test suspend functions and coroutine-using classes on the JVM with kotlinx-coroutines-test. Covers runTest, TestScope, StandardTestDispatcher vs Unconf… | `vendor/android-testing-skills/jvm-tests/coroutines/testing-coroutines-with-runtest` |
| `testing-flows-with-turbine` | Use this skill to assert Flow emissions in tests with Cash App Turbine. Covers flow.test entry, ReceiveTurbine API (awaitItem, awaitComplete, awaitError, expectMostRecen… | `vendor/android-testing-skills/jvm-tests/coroutines/testing-flows-with-turbine` |
| `mocking-with-mockito` | Use this skill to wire Mockito (the dominant Android mocking framework, exclusively used by androidx itself) into a JVM unit-test suite. Covers `org.mockito:mockito-core… | `vendor/android-testing-skills/jvm-tests/mocking/mocking-with-mockito` |
| `mocking-with-mockk` | Use this skill to wire MockK (the Kotlin-first mocking framework) into a JVM unit-test suite, especially when coroutines, singleton/`object` mocking, or constructor mock… | `vendor/android-testing-skills/jvm-tests/mocking/mocking-with-mockk` |
| `using-robolectric-correctly` | Use this skill to run Android-aware unit tests on the JVM with Robolectric — the right runner choice (AndroidJUnit4 vs RobolectricTestRunner), @Config sdk/qualifiers/app… | `vendor/android-testing-skills/jvm-tests/robolectric/using-robolectric-correctly` |
| `configuring-junit4-on-android` | Use this skill to stand up a JUnit4-based JVM unit-test suite on an Android module. Covers the canonical Gradle dependency matrix (`junit:junit:4.13.2`, `androidx.test:c… | `vendor/android-testing-skills/jvm-tests/runner/configuring-junit4-on-android` |
| `writing-tests-with-kotlin-test` | Use this skill to write tests with the `kotlin.test` library — the multiplatform assertion + annotation API that compiles the same in `commonTest` and on the JVM (JUnit4… | `vendor/android-testing-skills/kotlin/kotlin-test/writing-tests-with-kotlin-test` |
| `migrating-from-android-test-classes` | Use this skill to migrate a codebase off the deprecated `android.test.*` testing classes that ship in the Android platform SDK onto AndroidX Test. Covers `Instrumentatio… | `vendor/android-testing-skills/platform/legacy/migrating-from-android-test-classes` |

## بازبینی UX جریان کاربر — `AjnasNB/mobile-app-ux-auditor-skill`

- نقش: **phase** · لایسنس: MIT · commit: `514c75823a`
- کِی: بعد از تثبیت جریان ثبت دارو، بعد از اسکن→ثبت، قبل از انتشار آزمایشی
- تعداد مهارت یافت‌شده: **2**

| مهارت | چه کاری می‌کند | مسیر |
|---|---|---|
| `mobile-app-ux-auditor` | Use when reviewing, redesigning, or implementing mobile app UI/UX flows in Flutter, React Native, Swift, SwiftUI, UIKit, Kotlin, Jetpack Compose, Java, or Android Views;… | `vendor/mobile-app-ux-auditor-skill` |
| `mobile-app-ux-auditor` | Use when reviewing, redesigning, or implementing mobile app UI/UX flows in Flutter, React Native, Swift, SwiftUI, UIKit, Kotlin, Jetpack Compose, Java, or Android Views;… | `vendor/mobile-app-ux-auditor-skill/skills/mobile-app-ux-auditor` |

## فایل‌های Rule آمادهٔ کپی (Cursor/Copilot/Codex) — `RanaNadeemAslam/android-ai-skills`

- نقش: **rules** · لایسنس: MIT · commit: `3d9174c18d`
- کِی: مرجع مقایسه‌ای؛ اگر با PROJECT-RULES.md تناقض داشت، PROJECT-RULES.md مقدم است
- تعداد مهارت یافت‌شده: **0**

_(بدون SKILL.md؛ ساختار rule/مرجع دارد — فایل README خودش را ببینید.)_

