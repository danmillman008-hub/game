**REVIEW — گزارش فنی، بدون ادعای تأیید نهایی.** منبع حقیقت: APK اصلی Mimo 9.35
(`sha256 = 48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a`). وضعیتها: `OBSERVED` | `STATICALLY INFERRED` | `RUNTIME VERIFIED` | `SERVER CONFIRMED` | `UNKNOWN`.
هیچ شبیهساز/ADB/لاگ/اسکرینشات/پاسخ سرور در این جلسه وجود ندارد؛ `RUNTIME VERIFIED` و `SERVER CONFIRMED` = **۰**.

# COMPONENT_CATALOG — کاتالوگ مؤلفهها

## ۱. دامنه و روش

کاتالوگ از **class_def های واقعی `Lcom/getmimo/`** در ۱۲ DEX ساخته شد
(**3133 کلاس** از 29454 class_def کل)؛ طبقهبندی لایها بر اساس مسیر بسته و نام کلاس است و
`STATICALLY INFERRED` محسوب میشود، نه مشاهدهٔ اجرا. لبهها و شمارشها در
`COMPONENT_GRAPH.json` و شناسهها در `EVIDENCE_INDEX.json` هستند.
لایهبندی **ادعای معماری سراسری نیست**؛ فقط توزیع نامها است.

## ۲. توزیع لایهها 

| لایه | عنوان فارسی | تعداد | `OBSERVED` / `STATICALLY INFERRED` | نمونه کلاسها |
|---|---|---|---|---|
| ui | رابط/کامپوزابلها | 1232 | OBSERVED (تعداد) / STATICALLY INFERRED (نقش) | Lcom/getmimo/ui/SplashActivity$checkAuthentication$1;, Lcom/getmimo/ui/SplashActivity$onCreate$2;, Lcom/getmimo/ui/a; |
| viewmodel | ViewModel | 583 | OBSERVED (تعداد) / STATICALLY INFERRED (نقش) | Lcom/getmimo/ui/SplashViewModel$checkForUpdate$1;, Lcom/getmimo/ui/aitutor/AiTutorViewModel$AiTutorInfo;, Lcom/getmimo/ui/aitutor/AiTutorViewModel$State; |
| model | مدل داده | 344 | OBSERVED (تعداد) / STATICALLY INFERRED (نقش) | Lcom/getmimo/analytics/model/ContentExperiment;, Lcom/getmimo/analytics/model/ContentExperimentState$Ended;, Lcom/getmimo/analytics/model/ContentExperimentState$Ignore; |
| analytics | Analytics/Properties | 326 | OBSERVED (تعداد) / STATICALLY INFERRED (نقش) | Lcom/getmimo/analytics/AdjustTokenNotAvailableException;, Lcom/getmimo/analytics/Analytics$AiTutorInteraction$PromptType;, Lcom/getmimo/analytics/Analytics$Core$GuidedProjectUpsellShown$Type; |
| usecase_interactor | UseCase/Interactor | 169 | OBSERVED (تعداد) / STATICALLY INFERRED (نقش) | Lcom/getmimo/data/source/remote/pusher/AwesomeModePusherUseCase$onAuthenticationError$$inlined$filterIsInstance$1$1;, Lcom/getmimo/data/source/remote/pusher/AwesomeModePusherUseCase$onAuthenticationError$$inlined$filterI |
| repository_remote | Repository/منبع راهدور | 162 | OBSERVED (تعداد) / STATICALLY INFERRED (نقش) | Lcom/getmimo/data/source/remote/account/AccountDeleteWork$doWork$1;, Lcom/getmimo/data/source/remote/account/AccountDeleteWork;, Lcom/getmimo/data/source/remote/account/AccountDeletionFailedException; |
| repository_local | Repository/محلی | 105 | OBSERVED (تعداد) / STATICALLY INFERRED (نقش) | Lcom/getmimo/data/local/DataStoreUserPreferences$clear$1;, Lcom/getmimo/data/local/DataStoreUserPreferences$clear$2;, Lcom/getmimo/data/local/DataStoreUserPreferences$consumeHardModeIntro$1; |
| entry_point | Activity/Fragment نقطه ورود | 62 | OBSERVED (تعداد) / STATICALLY INFERRED (نقش) | Lcom/getmimo/analytics/properties/AuthenticationLocation$Activity;, Lcom/getmimo/apputil/crop/CustomImageCropActivity;, Lcom/getmimo/core/model/streak/UserActivity; |
| repository | Repository (سایر) | 60 | OBSERVED (تعداد) / STATICALLY INFERRED (نقش) | Lcom/getmimo/data/content/tracks/DefaultFavoriteTracksRepository$addTrackToFavorites$1;, Lcom/getmimo/data/content/tracks/DefaultFavoriteTracksRepository$getFavoriteTracks$1;, Lcom/getmimo/data/content/tracks/DefaultFavo |
| other_mimo | سایر com.getmimo | 38 | OBSERVED (تعداد) / STATICALLY INFERRED (نقش) | Lcom/getmimo/apputil/FlashbarType;, Lcom/getmimo/apputil/FlowExtensionsKt$ignoreAndLogNonNetworkExceptions$1;, Lcom/getmimo/apputil/FlowViewExtensionsKt$afterTextChanges$1; |
| data_other | سایر data/core | 34 | OBSERVED (تعداد) / STATICALLY INFERRED (نقش) | Lcom/getmimo/data/devmenu/subscriptions/SubscriptionType;, Lcom/getmimo/data/firebase/DevMenuRemoteConfigStorage$addRemoteConfigItem$1;, Lcom/getmimo/data/firebase/DevMenuRemoteConfigStorage$addRemoteConfigItem$2; |
| navigation | Navigation | 10 | OBSERVED (تعداد) / STATICALLY INFERRED (نقش) | Lcom/getmimo/analytics/properties/pacingmechanic/ShowPacingDialogSource$PathNavigationBar;, Lcom/getmimo/ui/navigation/NavigationBar$NavigationBarSavedState;, Lcom/getmimo/ui/navigation/NavigationBar$listenToTabChanges$1 |
| background_worker | Worker/پسزمینه | 5 | OBSERVED (تعداد) / STATICALLY INFERRED (نقش) | Lcom/getmimo/data/settings/work/UpdateNotificationsSettingsWork$doWork$1;, Lcom/getmimo/data/settings/work/UpdateNotificationsSettingsWork$doWork$2;, Lcom/getmimo/data/settings/work/UpdateNotificationsSettingsWork; |
| application | Application | 3 | OBSERVED (تعداد) / STATICALLY INFERRED (نقش) | Lcom/getmimo/App$onCreate$1;, Lcom/getmimo/App$onCreate$2$1;, Lcom/getmimo/App; |

⚠️ تعداد لایه `ui` شامل کلاسهای لامبدای کاتلین (`PathMapScreenKt$...`) نیز هست؛
پس «تعداد کامپوزابل» نیست. `analytics` عمدتاً enum/propertyهای ردیابی است.

## ۳. توزیع زیرسیستمها (A…P)

| زیرسیستم | کلاس | لایه غالب | نمونه کلاس (عنوان ستون اصلاحشده) |
|---|---|---|---|
| A — راهاندازی/Init | 30 | ui:15, viewmodel:10, application:3 | Lcom/getmimo/App$onCreate$1;, Lcom/getmimo/App$onCreate$2$1; |
| B — احراز هویت/نشست | 176 | ui:78, repository_remote:33, analytics:23 | Lcom/getmimo/analytics/AdjustTokenNotAvailableException;, Lcom/getmimo/analytics/properties/AuthenticationLocation$Activity; |
| C — Onboarding | 171 | ui:63, analytics:62, viewmodel:24 | Lcom/getmimo/analytics/properties/AuthenticationLocation$Onboarding;, Lcom/getmimo/analytics/properties/OnboardingDevicePreference$Both; |
| D — خانه/داشبورد | 51 | ui:24, repository_local:15, analytics:5 | Lcom/getmimo/analytics/properties/OnboardingGoal$DashboardsOrReports;, Lcom/getmimo/analytics/properties/OpenLessonSourceProperty$TrackOverview; |
| E — مسیر یادگیری | 297 | ui:101, model:73, usecase_interactor:55 | Lcom/getmimo/analytics/properties/CertificateRequestSource$PathMap;, Lcom/getmimo/analytics/properties/CertificateRequestSource$Profile; |
| F — اجرای درس | 500 | ui:219, viewmodel:137, model:115 | Lcom/getmimo/analytics/properties/AiTutorInteractionSource$InteractiveLesson;, Lcom/getmimo/analytics/properties/LessonType$InteractiveWebView; |
| G — پیشرفت درس | 47 | repository_remote:17, repository_local:11, model:10 | Lcom/getmimo/data/model/codeeditor/autocompletion/AutoCompletionResponse;, Lcom/getmimo/data/model/progress/LastInteractedTrackResponse; |
| H — تمرین/چالش | 114 | ui:49, viewmodel:32, analytics:15 | Lcom/getmimo/analytics/Analytics$LessonStreakChallenge$LessonStreakChallengeSource;, Lcom/getmimo/analytics/properties/AuthenticationLocation$Practice; |
| I — پایان چپتر/نمره | 84 | ui:51, viewmodel:15, usecase_interactor:13 | Lcom/getmimo/analytics/properties/AuthenticationLocation$ChapterEnd;, Lcom/getmimo/analytics/properties/KeysPaywallSourceProperty$ChapterEnd; |
| J — پاداش/ارزها | 173 | repository_local:70, ui:22, model:21 | Lcom/getmimo/analytics/properties/OnboardingWorkFunction$ProductManagement;, Lcom/getmimo/analytics/properties/PurchaseProductSource$ChapterEnd; |
| K — هدف روزانه/Streak | 139 | ui:69, viewmodel:24, repository:15 | Lcom/getmimo/analytics/Analytics$LessonStreakChallenge$LessonStreakChallengeSource;, Lcom/getmimo/analytics/properties/OnboardingGoal$BuildHabit; |
| L — لیدربورد/لیگ | 88 | ui:42, viewmodel:19, model:11 | Lcom/getmimo/analytics/properties/AuthenticationLocation$LeaderBoards;, Lcom/getmimo/analytics/properties/ViewPublicProfileSource$Leaderboard; |
| M — AI Tutor | 82 | viewmodel:31, ui:23, repository_local:15 | Lcom/getmimo/analytics/Analytics$AiTutorInteraction$PromptType;, Lcom/getmimo/analytics/properties/AiTutorInteractionSource$ExecutableLesson; |
| N — تنظیمات | 227 | repository_local:70, ui:66, repository:26 | Lcom/getmimo/analytics/properties/AuthenticationLocation$Settings;, Lcom/getmimo/analytics/properties/GetHelpSource$Settings; |
| O — پیکربندی/Feature flags | 51 | model:12, data_other:10, repository:10 | Lcom/getmimo/analytics/FirebaseRemoteConfigFetcher$fetchAndPersistAbTestUserGroup$1;, Lcom/getmimo/analytics/FirebaseRemoteConfigFetcher$fetchAndPersistAbTestUserGroup$2; |
| P — اشتراک/پرداخت | 288 | ui:88, viewmodel:86, repository_remote:53 | Lcom/getmimo/analytics/Analytics$Core$MaxUpsellPaywallShown$Source;, Lcom/getmimo/analytics/Analytics$Core$PaywallShown$Source; |

## ۴. مؤلفههای کلیدی (برگزیده از نامهای بازیابیشده)

### ۴٫۱ نقطههای ورود و Application
| نقش | کلاس | `OBSERVED` در | سند |
|---|---|---|---|
| Application | com.getmimo.App | AndroidManifest.xml | EV-0030.. |
| Activity | com.getmimo.ui.learningcompanions.LearningCompanionsIntroActivity | AndroidManifest.xml | APK_COMPLETE_INVENTORY.json |
| Activity | com.getmimo.ui.SplashActivity | AndroidManifest.xml | APK_COMPLETE_INVENTORY.json |
| Activity | com.getmimo.ui.authentication.AuthenticationActivity | AndroidManifest.xml | APK_COMPLETE_INVENTORY.json |
| Activity | com.facebook.FacebookActivity | AndroidManifest.xml | APK_COMPLETE_INVENTORY.json |
| Activity | com.facebook.CustomTabActivity | AndroidManifest.xml | APK_COMPLETE_INVENTORY.json |
| Activity | com.getmimo.ui.main.MainActivity | AndroidManifest.xml | APK_COMPLETE_INVENTORY.json |
| Activity | com.getmimo.ui.chapter.ChapterActivity | AndroidManifest.xml | APK_COMPLETE_INVENTORY.json |
| Activity | com.getmimo.ui.iap.allplans.AllPlansActivity | AndroidManifest.xml | APK_COMPLETE_INVENTORY.json |
| Activity | com.getmimo.ui.profile.SetDailyGoalActivity | AndroidManifest.xml | APK_COMPLETE_INVENTORY.json |
| Activity | com.getmimo.ui.onboarding.intro.IntroSlidesActivity | AndroidManifest.xml | APK_COMPLETE_INVENTORY.json |
| Activity | com.getmimo.ui.onboarding.OnboardingActivity | AndroidManifest.xml | APK_COMPLETE_INVENTORY.json |
| Activity | com.getmimo.ui.settings.SettingsActivity | AndroidManifest.xml | APK_COMPLETE_INVENTORY.json |
| Activity | com.getmimo.ui.settings.appearance.ChangeAppearanceActivity | AndroidManifest.xml | APK_COMPLETE_INVENTORY.json |
| Activity | com.getmimo.ui.settings.appicons.ChangeAppIconActivity | AndroidManifest.xml | APK_COMPLETE_INVENTORY.json |

### ۴٫۲ ViewModelها، Interactorها و Repositoryها (نمونه مستند)

**ViewModel** (583 کلاس در لایه)

- Lcom/getmimo/ui/aitutor/AiTutorViewModel;
- Lcom/getmimo/ui/chapter/ChapterViewModel;
- Lcom/getmimo/ui/leaderboard/LeaderboardViewModel;
- Lcom/getmimo/ui/lesson/report/ReportLessonViewModel;
- Lcom/getmimo/ui/onboarding/dailygoal/OnboardingSetDailyGoalViewModel;
- Lcom/getmimo/ui/onboarding/intro/IntroSlidesViewModel;
- Lcom/getmimo/ui/onboarding/selectpath/pickapath/OnboardingPickAPathViewModel;
- Lcom/getmimo/ui/publicprofile/PublicProfileViewModel;
- Lcom/getmimo/ui/settings/SettingsViewModel;

**UseCase/Interactor** (169 کلاس در لایه)

- Lcom/getmimo/interactors/aitutor/a;
- Lcom/getmimo/interactors/appicons/a;
- Lcom/getmimo/interactors/appupdate/a;
- Lcom/getmimo/interactors/appupdate/b;
- Lcom/getmimo/interactors/authentication/ChangeEmailResult;
- Lcom/getmimo/interactors/authentication/DeleteAccountResult;
- Lcom/getmimo/interactors/authentication/a;
- Lcom/getmimo/interactors/authentication/b;
- Lcom/getmimo/interactors/authentication/c;
- Lcom/getmimo/interactors/authentication/d;
- Lcom/getmimo/interactors/authentication/e;
- Lcom/getmimo/interactors/certificates/a;
- Lcom/getmimo/interactors/certificates/b;
- Lcom/getmimo/interactors/chapter/a;

**Repository** (60 کلاس در لایه)

- (فقط کلاسهای داخلی/لامبدا یافت شد)

**Remote repository/API** (162 کلاس در لایه)

- Lcom/getmimo/data/source/remote/account/AccountDeleteWork;
- Lcom/getmimo/data/source/remote/account/AccountDeletionFailedException;
- Lcom/getmimo/data/source/remote/account/EmailChangeRejectedException;
- Lcom/getmimo/data/source/remote/account/a;
- Lcom/getmimo/data/source/remote/ads/AdNotPreloadedException;
- Lcom/getmimo/data/source/remote/analytics/FreeTrialDuration;
- Lcom/getmimo/data/source/remote/analytics/a;
- Lcom/getmimo/data/source/remote/authentication/AccessTokenUnavailableException;
- Lcom/getmimo/data/source/remote/authentication/AuthenticationException;
- Lcom/getmimo/data/source/remote/authentication/AuthenticationUserCollisionException;
- Lcom/getmimo/data/source/remote/authentication/PostVisitWorker;
- Lcom/getmimo/data/source/remote/authentication/a;
- Lcom/getmimo/data/source/remote/authentication/b;
- Lcom/getmimo/data/source/remote/awesome/LessonDraftResponse;

**Local repository / DataStore** (105 کلاس در لایه)

- Lcom/getmimo/data/local/a;
- Lcom/getmimo/data/model/room/ChapterCompletion;
- Lcom/getmimo/data/model/room/Converters;
- Lcom/getmimo/data/model/room/LessonProgress;
- Lcom/getmimo/data/model/room/TutorialCompletion;
- Lcom/getmimo/data/source/local/aitutor/SystemMessage;
- Lcom/getmimo/data/source/local/aitutor/UserMessage;
- Lcom/getmimo/data/source/local/aitutor/a;
- Lcom/getmimo/data/source/local/aitutor/b;
- Lcom/getmimo/data/source/local/aitutor/c;
- Lcom/getmimo/data/source/local/aitutor/d;
- Lcom/getmimo/data/source/local/aitutor/e;
- Lcom/getmimo/data/source/local/aitutor/f;
- Lcom/getmimo/data/source/local/codeeditor/codingkeyboard/a;

**Worker** (5 کلاس در لایه)

- Lcom/getmimo/data/settings/work/UpdateNotificationsSettingsWork;
- Lcom/getmimo/ui/widget/StreakWidgetRefreshWorker;

### ۴٫۳ سرویسها، گیرندهها و Providerها (از Manifest)

**Service** (19):

- com.getmimo.data.notification.MimoFirebaseMessagingService
- com.getmimo.apputil.notification.NotPremiumNotificationService
- com.getmimo.data.source.remote.savedcode.AutoSaveCodeService
- com.google.android.gms.metadata.ModuleDependencies
- com.google.firebase.components.ComponentDiscoveryService
- androidx.credentials.playservices.CredentialProviderMetadataHolder
- com.google.firebase.messaging.FirebaseMessagingService
- com.google.firebase.sessions.SessionLifecycleService
- com.google.android.datatransport.runtime.backends.TransportBackendDiscovery
- androidx.glance.appwidget.GlanceRemoteViewsService
- com.google.android.gms.ads.AdService
- androidx.work.impl.background.systemjob.SystemJobService
- androidx.work.impl.foreground.SystemForegroundService
- com.google.android.gms.auth.api.signin.RevocationBoundService
- com.google.android.gms.measurement.AppMeasurementService
- com.google.android.gms.measurement.AppMeasurementJobService
- androidx.core.widget.RemoteViewsCompatService
- androidx.room.MultiInstanceInvalidationService
- com.google.android.datatransport.runtime.scheduling.jobscheduling.JobInfoSchedulerService

**BroadcastReceiver** (20):

- com.getmimo.apputil.notification.NotificationPublisher
- com.getmimo.apputil.share.CodePlaygroundShareReceiver
- com.getmimo.apputil.share.SharePromoLinkReceiver
- com.getmimo.apputil.share.InviteFriendsShareReceiver
- com.getmimo.apputil.share.ShareToStoryReceiver
- com.getmimo.ui.widget.MimoStreakSmallWidgetReceiver
- com.getmimo.ui.widget.MimoStreakMediumWidgetReceiver
- com.getmimo.ui.widget.MimoStreakLargeWidgetReceiver
- com.google.firebase.iid.FirebaseInstanceIdReceiver
- androidx.glance.appwidget.action.ActionCallbackBroadcastReceiver
- androidx.glance.appwidget.UnmanagedSessionReceiver
- androidx.glance.appwidget.MyPackageReplacedReceiver
- androidx.work.impl.utils.ForceStopRunnable$BroadcastReceiver
- androidx.work.impl.background.systemalarm.RescheduleReceiver
- androidx.work.impl.diagnostics.DiagnosticsReceiver
- com.google.android.gms.measurement.AppMeasurementReceiver
- com.facebook.CurrentAccessTokenExpirationBroadcastReceiver
- com.facebook.AuthenticationTokenManager$CurrentAuthenticationTokenChangedBroadcastReceiver
- androidx.profileinstaller.ProfileInstallReceiver
- com.google.android.datatransport.runtime.scheduling.jobscheduling.AlarmManagerSchedulerBroadcastReceiver

**ContentProvider** (8):

- androidx.core.content.FileProvider
- androidx.startup.InitializationProvider
- com.canhub.cropper.CropFileProvider
- com.google.android.gms.ads.MobileAdsInitProvider
- com.google.firebase.provider.FirebaseInitProvider
- com.facebook.internal.FacebookInitProvider
- org.jetbrains.compose.resources.AndroidContextProvider
- com.adjust.sdk.SystemLifecycleContentProvider

### ۴٫۴ وابستگیهای بومی و کتابخانهای

| نوع | مورد | وضعیت |
|---|---|---|
| native .so | 12 کتابخانه در ۲ ABI | OBSERVED |
| native | libandroidx.graphics.path.so | OBSERVED — مرتبط با رسم Path در Compose (نقش دقیق INFERRED) |
| native | librive-android.so / libdatastore_shared_counter.so / libsigner.so / libyrf.so | OBSERVED |
| Compose | androidx.compose 1.12.1 / material3 1.4.0 / adaptive 1.3.0 | OBSERVED (META-INF/*.version) |
| androidx.compose.animation_animation-core.version | 1.12.1 | OBSERVED |
| androidx.compose.animation_animation.version | 1.12.1 | OBSERVED |
| androidx.compose.foundation_foundation-layout.version | 1.12.1 | OBSERVED |
| androidx.compose.foundation_foundation.version | 1.12.1 | OBSERVED |
| androidx.compose.material3.adaptive_adaptive.version | 1.3.0 | OBSERVED |
| androidx.compose.material3_material3-window-size-class.version | 1.4.0 | OBSERVED |
| androidx.compose.material3_material3.version | 1.4.0 | OBSERVED |
| androidx.compose.material_material-ripple.version | 1.12.1 | OBSERVED |
| androidx.compose.material_material.version | 1.12.1 | OBSERVED |
| androidx.compose.runtime_runtime-annotation.version | 1.12.1 | OBSERVED |
| androidx.compose.runtime_runtime-livedata.version | 1.12.1 | OBSERVED |
| androidx.compose.runtime_runtime-retain.version | 1.12.1 | OBSERVED |
| androidx.compose.runtime_runtime-saveable.version | 1.12.1 | OBSERVED |
| androidx.compose.runtime_runtime.version | 1.12.1 | OBSERVED |
| androidx.compose.ui_ui-geometry.version | 1.12.1 | OBSERVED |
| androidx.compose.ui_ui-graphics.version | 1.12.1 | OBSERVED |

## ۵. نگاشت نامهای R8

| مورد | مقدار | وضعیت |
|---|---|---|
| R8 map-id | r8-map-id-6b1b9a7aabb67c08b10510c084e2abcbeb53083883bac13e4d61278a32657bc6 | OBSERVED در source_file_idx |
| فایل mapping در APK | خیر | OBSERVED (عدم وجود) |
| نگاشت کلاس کوتاه → نام منطقی | 491 | OBSERVED (بخشی) |
| نام فایلهای منبع کاتلین بازیافته | 178 | OBSERVED |
| دیابسکیشن کامل کلاسهای کوتاهنام | انجامنشده | UNKNOWN |

نمونهای از نگاشتهای قابل اتکا (از `DebugMetadata.c`):

- `Landroidx/core/view/ViewKt$allViews$1;` ← `androidx.core.view.ViewKt$allViews$1`
- `Lcom/google/firebase/datastorage/JavaDataStorage$editSync$1$1;` ← `com.google.firebase.datastorage.JavaDataStorage$editSync$1$1`
- `Lcom/google/firebase/datastorage/JavaDataStorage$editSync$1;` ← `com.google.firebase.datastorage.JavaDataStorage$editSync$1`
- `Lcom/google/firebase/datastorage/JavaDataStorage$getAllSync$1;` ← `com.google.firebase.datastorage.JavaDataStorage$getAllSync$1`
- `Lcom/google/firebase/datastorage/JavaDataStorage$getSync$1;` ← `com.google.firebase.datastorage.JavaDataStorage$getSync$1`
- `Lcom/google/firebase/datastorage/JavaDataStorage$putSync$1$1;` ← `com.google.firebase.datastorage.JavaDataStorage$putSync$1$1`
- `Lcom/google/firebase/datastorage/JavaDataStorage$putSync$1;` ← `com.google.firebase.datastorage.JavaDataStorage$putSync$1`
- `Lcom/google/firebase/remoteconfig/RemoteConfigKt$configUpdates$1;` ← `com.google.firebase.remoteconfig.RemoteConfigKt$configUpdates$1`
- `Lcom/google/firebase/sessions/FirebaseSessions$1;` ← `com.google.firebase.sessions.FirebaseSessions$1`
- `Lcom/google/firebase/sessions/InstallationId$Companion$create$1;` ← `com.google.firebase.sessions.InstallationId$Companion`

## ۶. شناسههای شاهد مرتبط

- EV-0032
- EV-0286
- EV-0041
- EV-0043
- EV-0296

