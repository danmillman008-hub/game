# ۰۴ — کاتالوگ کامل صفحات (هیچ صفحهای حذف نشده)

**تعداد: 276 سطح رابط.** ۱۹۲ سطح از `CATALOGS/PRIOR_WORK_SCREEN_INVENTORY.csv`
(مهندسی معکوس قبلی شما) + 84 کلاس صفحهای که این بار مستقیماً از DEX استخراج شدند.
هر سطر زیر یک پروندهٔ جداگانه در `SCREENS/` دارد که شامل: کلاس، نوع، تم manifests،
deep linkها، **فهرست کامل لایههای متصل**، درخت مؤلفههای **همهٔ** لایهها، فهرست کامل
رشتهها/رنگها/دایمنشنها/استایلهای مرتبط و شواهد حالتها است.

## ساختار پروندهٔ هر صفحه (یکسان برای همه)

| بخش | محتوا | کلاس شواهد |
|---|---|---|
| ۱ | لایههای XML متصل (همه) | `DERIVED` (xref لایه از `const` در DEX + تطابق نام) |
| ۲ | درخت مؤلفههای همهٔ لایهها | `VERIFIED_STATIC` |
| ۳–۶ | رشتهها / رنگها / دایمنها / استایلها (کامل) | `VERIFIED_STATIC` |
| ۷ | شواهد حالتها (offline/empty/error/loading/locked/upgrade) | `PARTIALLY_VERIFIED` |
| ۸ | ناوبری و deep link | `VERIFIED_STATIC` |

## فهرست کامل (276 ردیف)

| # | صفحه | نوع | لایه | رشته | رنگ | دایمن | استایل | C | W | پرونده |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `ABTestConfigActivity` | activity | 1 | 0 | 0 | 0 | 0 | — | — | [باز](ABTestConfigActivity.md) |
| 2 | `ActionTrampolineActivity` | activity | 0 | 0 | 0 | 0 | 0 | — | — | [باز](ActionTrampolineActivity.md) |
| 3 | `AdActivity` | activity | 0 | 262 | 19 | 348 | 94 | — | — | [باز](AdActivity.md) |
| 4 | `AiTutorBottomSheetKt` | dex-ui-class | 0 | 0 | 0 | 0 | 0 | — | — | [باز](AiTutorBottomSheetKt.md) |
| 5 | `AiTutorBottomSheetKt$AiTutorBottomSheet$1$1` | bottom_sheet | 0 | 0 | 0 | 0 | 0 | — | — | [باز](AiTutorBottomSheetKt_AiTutorBottomSheet_1_1.md) |
| 6 | `AiTutorBottomSheetKt$AiTutorBottomSheet$5$1` | bottom_sheet | 0 | 0 | 0 | 0 | 0 | — | — | [باز](AiTutorBottomSheetKt_AiTutorBottomSheet_5_1.md) |
| 7 | `AllPlansActivity` | activity | 1 | 1 | 0 | 0 | 0 | ✓ | — | [باز](AllPlansActivity.md) |
| 8 | `AnimatedResultBottomSheetKt` | dex-ui-class | 0 | 0 | 0 | 0 | 0 | — | — | [باز](AnimatedResultBottomSheetKt.md) |
| 9 | `AnimatedResultBottomSheetKt$AnimatedResultBottomSheet$4$1` | bottom_sheet | 0 | 0 | 0 | 0 | 0 | — | — | [باز](AnimatedResultBottomSheetKt_AnimatedResultBottomSheet_4_1.md) |
| 10 | `AnimatedResultBottomSheetKt$AnimatedResultBottomSheet$5$1` | bottom_sheet | 0 | 0 | 0 | 0 | 0 | — | — | [باز](AnimatedResultBottomSheetKt_AnimatedResultBottomSheet_5_1.md) |
| 11 | `AnimatedResultBottomSheetKt$AnimatedResultBottomSheetContent$2$1` | bottom_sheet | 0 | 0 | 0 | 0 | 0 | — | — | [باز](AnimatedResultBottomSheetKt_AnimatedResultBottomSheetContent_2_1.md) |
| 12 | `AnonymousLogoutDialogFragment` | dex-ui-class | 0 | 0 | 0 | 0 | 0 | — | — | [باز](AnonymousLogoutDialogFragment.md) |
| 13 | `AskForNameFragment` | fragment | 1 | 1 | 0 | 0 | 0 | ✓ | — | [باز](AskForNameFragment.md) |
| 14 | `AuthenticationActivity` | activity | 5 | 6 | 0 | 3 | 0 | ✓ | — | [باز](AuthenticationActivity.md) |
| 15 | `AuthenticationFragment` | dex-ui-class | 5 | 6 | 0 | 3 | 0 | ✓ | — | [باز](AuthenticationFragment.md) |
| 16 | `AuthenticationScreenType` | dex-ui-class | 0 | 0 | 0 | 0 | 0 | — | — | [باز](AuthenticationScreenType.md) |
| 17 | `AwesomeModeActivity` | activity | 1 | 4 | 0 | 0 | 0 | — | — | [باز](AwesomeModeActivity.md) |
| 18 | `AwesomeModeLessonFragment` | dex-ui-class | 0 | 1 | 0 | 0 | 0 | — | — | [باز](AwesomeModeLessonFragment.md) |
| 19 | `BasicModalResult` | dex-ui-class | 0 | 0 | 0 | 0 | 0 | — | — | [باز](BasicModalResult.md) |
| 20 | `BasicModalResultType` | dex-ui-class | 0 | 0 | 0 | 0 | 0 | — | — | [باز](BasicModalResultType.md) |
| 21 | `BottomSheetKeysViewModel` | dex-ui-class | 0 | 0 | 0 | 0 | 0 | — | — | [باز](BottomSheetKeysViewModel.md) |
| 22 | `BottomSheetKeysViewModel$getSubscriptionTier$2` | bottom_sheet | 0 | 0 | 0 | 0 | 0 | — | — | [باز](BottomSheetKeysViewModel_getSubscriptionTier_2.md) |
| 23 | `BottomSheetKeysViewModel$initialize$1` | bottom_sheet | 0 | 0 | 0 | 0 | 0 | — | — | [باز](BottomSheetKeysViewModel_initialize_1.md) |
| 24 | `BottomSheetKeysViewModel$initialize$1$1` | bottom_sheet | 0 | 0 | 0 | 0 | 0 | — | — | [باز](BottomSheetKeysViewModel_initialize_1_1.md) |
| 25 | `BottomSheetKeysViewModel$initialize$1$1$1` | bottom_sheet | 0 | 0 | 0 | 0 | 0 | — | — | [باز](BottomSheetKeysViewModel_initialize_1_1_1.md) |
| 26 | `BottomSheetKeysViewModel$initialize$1$1$2` | bottom_sheet | 0 | 0 | 0 | 0 | 0 | — | — | [باز](BottomSheetKeysViewModel_initialize_1_1_2.md) |
| 27 | `BottomSheetKeysViewModel$initialize$1$1$3` | bottom_sheet | 0 | 0 | 0 | 0 | 0 | — | — | [باز](BottomSheetKeysViewModel_initialize_1_1_3.md) |
| 28 | `BottomSheetKeysViewModel$initialize$1$1$4` | bottom_sheet | 0 | 0 | 0 | 0 | 0 | — | — | [باز](BottomSheetKeysViewModel_initialize_1_1_4.md) |
| 29 | `BottomSheetKeysViewModel$initialize$1$1$5` | bottom_sheet | 0 | 0 | 0 | 0 | 0 | — | — | [باز](BottomSheetKeysViewModel_initialize_1_1_5.md) |
| 30 | `BottomSheetKeysViewModel$observeKeys$2` | bottom_sheet | 0 | 0 | 0 | 0 | 0 | — | — | [باز](BottomSheetKeysViewModel_observeKeys_2.md) |
| 31 | `BottomSheetKeysViewModel$observeKeys$2$1` | bottom_sheet | 0 | 0 | 0 | 0 | 0 | — | — | [باز](BottomSheetKeysViewModel_observeKeys_2_1.md) |
| 32 | `BottomSheetKeysViewModel$observeKeys$2$1$1` | bottom_sheet | 0 | 0 | 0 | 0 | 0 | — | — | [باز](BottomSheetKeysViewModel_observeKeys_2_1_1.md) |
| 33 | `BottomSheetKeysViewModel$observePurchaseUpdates$2` | bottom_sheet | 0 | 0 | 0 | 0 | 0 | — | — | [باز](BottomSheetKeysViewModel_observePurchaseUpdates_2.md) |
| 34 | `BottomSheetKeysViewModel$observePurchaseUpdates$2$1` | bottom_sheet | 0 | 0 | 0 | 0 | 0 | — | — | [باز](BottomSheetKeysViewModel_observePurchaseUpdates_2_1.md) |
| 35 | `BottomSheetKeysViewModel$observePurchaseUpdates$2$1$2` | bottom_sheet | 0 | 0 | 0 | 0 | 0 | — | — | [باز](BottomSheetKeysViewModel_observePurchaseUpdates_2_1_2.md) |
| 36 | `BottomSheetKeysViewModel$observePurchaseUpdates$2$1$invokeSuspend$$inlined$filter$1$1` | bottom_sheet | 0 | 0 | 0 | 0 | 0 | — | — | [باز](BottomSheetKeysViewModel_observePurchaseUpdates_2_1_invokeSuspend__inlined_filter_1_1.md) |
| 37 | `BottomSheetKeysViewModel$observePurchaseUpdates$2$1$invokeSuspend$$inlined$filter$1$2$1` | bottom_sheet | 0 | 0 | 0 | 0 | 0 | — | — | [باز](BottomSheetKeysViewModel_observePurchaseUpdates_2_1_invokeSuspend__inlined_filter_1_2_1.md) |
| 38 | `BottomSheetKeysViewModel$showUpgradeToPro$1` | bottom_sheet | 0 | 0 | 0 | 0 | 0 | — | — | [باز](BottomSheetKeysViewModel_showUpgradeToPro_1.md) |
| 39 | `BottomSheetKeysViewModel$showUpgradeToPro$1$1` | bottom_sheet | 0 | 0 | 0 | 0 | 0 | — | — | [باز](BottomSheetKeysViewModel_showUpgradeToPro_1_1.md) |
| 40 | `BottomSheetKeysViewModel$updatePaywallId$2` | bottom_sheet | 0 | 0 | 0 | 0 | 0 | — | — | [باز](BottomSheetKeysViewModel_updatePaywallId_2.md) |
| 41 | `BottomSheetWrapperKt` | dex-ui-class | 0 | 0 | 0 | 0 | 0 | — | — | [باز](BottomSheetWrapperKt.md) |
| 42 | `BottomSheetWrapperKt$BottomSheetWrapper$3$1` | bottom_sheet | 0 | 0 | 0 | 0 | 0 | — | — | [باز](BottomSheetWrapperKt_BottomSheetWrapper_3_1.md) |
| 43 | `BottomSheetWrapperKt$BottomSheetWrapper$4$1` | bottom_sheet | 0 | 0 | 0 | 0 | 0 | — | — | [باز](BottomSheetWrapperKt_BottomSheetWrapper_4_1.md) |
| 44 | `BottomSheetWrapperKt$BottomSheetWrapper$hideAction$1$1$1` | bottom_sheet | 0 | 0 | 0 | 0 | 0 | — | — | [باز](BottomSheetWrapperKt_BottomSheetWrapper_hideAction_1_1_1.md) |
| 45 | `CertificateActivity` | activity | 7 | 50 | 0 | 0 | 0 | ✓ | — | [باز](CertificateActivity.md) |
| 46 | `CertificateUpgradeActivity` | activity | 1 | 0 | 0 | 0 | 0 | ✓ | — | [باز](CertificateUpgradeActivity.md) |
| 47 | `ChangeAppIconActivity` | activity | 0 | 0 | 0 | 0 | 0 | — | — | [باز](ChangeAppIconActivity.md) |
| 48 | `ChangeAppearanceActivity` | activity | 0 | 0 | 0 | 0 | 0 | — | — | [باز](ChangeAppearanceActivity.md) |
| 49 | `ChangeEmailActivity` | activity | 0 | 11 | 0 | 0 | 0 | — | — | [باز](ChangeEmailActivity.md) |
| 50 | `ChangeEmailScreenKt` | dex-ui-class | 0 | 0 | 0 | 0 | 0 | — | — | [باز](ChangeEmailScreenKt.md) |
| 51 | `ChapterActivity` | activity | 11 | 56 | 5 | 2 | 0 | ✓ | — | [باز](ChapterActivity.md) |
| 52 | `ChapterFinishedEtaFragment` | dex-ui-class | 0 | 0 | 0 | 0 | 0 | — | — | [باز](ChapterFinishedEtaFragment.md) |
| 53 | `ChapterFinishedFragment` | dex-ui-class | 7 | 2 | 0 | 0 | 0 | ✓ | — | [باز](ChapterFinishedFragment.md) |
| 54 | `ChapterFinishedFragment$showRatingBottomSheet$1$1$1` | bottom_sheet | 7 | 0 | 0 | 0 | 0 | ✓ | — | [باز](ChapterFinishedFragment_showRatingBottomSheet_1_1_1.md) |
| 55 | `ChapterFinishedFragment$showRatingBottomSheet$1$2` | bottom_sheet | 7 | 0 | 0 | 0 | 0 | ✓ | — | [باز](ChapterFinishedFragment_showRatingBottomSheet_1_2.md) |
| 56 | `ChapterFinishedFreeStreakGoalFragment` | dex-ui-class | 0 | 0 | 0 | 0 | 0 | — | — | [باز](ChapterFinishedFreeStreakGoalFragment.md) |
| 57 | `ChapterFinishedLeaderboardFragment` | dex-ui-class | 3 | 0 | 0 | 0 | 0 | ✓ | — | [باز](ChapterFinishedLeaderboardFragment.md) |
| 58 | `ChapterFinishedShareStreakFragment` | dex-ui-class | 1 | 0 | 0 | 0 | 0 | — | — | [باز](ChapterFinishedShareStreakFragment.md) |
| 59 | `ChapterFinishedStreakChallengeFragmentKt` | dex-ui-class | 0 | 0 | 0 | 0 | 0 | — | — | [باز](ChapterFinishedStreakChallengeFragmentKt.md) |
| 60 | `ChapterFinishedStreakFragment` | dex-ui-class | 1 | 0 | 0 | 0 | 0 | ✓ | — | [باز](ChapterFinishedStreakFragment.md) |
| 61 | `ChapterFinishedViewModel` | dex-ui-class | 0 | 0 | 0 | 0 | 0 | — | — | [باز](ChapterFinishedViewModel.md) |
| 62 | `ChapterFinishedViewModel$shouldShowRatingBottomSheet$1` | bottom_sheet | 0 | 0 | 0 | 0 | 0 | — | — | [باز](ChapterFinishedViewModel_shouldShowRatingBottomSheet_1.md) |
| 63 | `CodePlaygroundActivity` | activity | 3 | 6 | 0 | 0 | 0 | ✓ | — | [باز](CodePlaygroundActivity.md) |
| 64 | `CodePlaygroundNewCodeFileFragment` | dex-ui-class | 0 | 0 | 0 | 0 | 0 | — | — | [باز](CodePlaygroundNewCodeFileFragment.md) |
| 65 | `ComposableSingletons` | dex-ui-class | 0 | 0 | 0 | 0 | 0 | — | — | [باز](ComposableSingletons.md) |
| 66 | `ComposableSingletons$BottomSheetWrapperKt$lambda$-783399894$1$1$1` | bottom_sheet | 0 | 0 | 0 | 0 | 0 | — | — | [باز](ComposableSingletons_BottomSheetWrapperKt_lambda_-783399894_1_1_1.md) |
| 67 | `CropImageActivity` | activity | 2 | 1 | 0 | 0 | 0 | — | — | [باز](CropImageActivity.md) |
| 68 | `CustomImageCropActivity` | activity | 0 | 0 | 0 | 0 | 0 | — | — | [باز](CustomImageCropActivity.md) |
| 69 | `CustomTabActivity` | activity | 0 | 0 | 0 | 0 | 0 | — | — | [باز](CustomTabActivity.md) |
| 70 | `CustomTabMainActivity` | activity | 0 | 0 | 0 | 0 | 0 | — | — | [باز](CustomTabMainActivity.md) |
| 71 | `CustomViewsActivity` | activity | 1 | 0 | 0 | 0 | 0 | — | — | [باز](CustomViewsActivity.md) |
| 72 | `CustomerCenterActivity` | activity | 0 | 0 | 0 | 0 | 0 | — | — | [باز](CustomerCenterActivity.md) |
| 73 | `DevMenuRemoteConfigActivity` | activity | 1 | 0 | 0 | 0 | 0 | ✓ | — | [باز](DevMenuRemoteConfigActivity.md) |
| 74 | `DeveloperMenuActivity` | activity | 6 | 67 | 0 | 1 | 0 | ✓ | — | [باز](DeveloperMenuActivity.md) |
| 75 | `DeveloperMenuCampaignActivity` | activity | 1 | 4 | 0 | 0 | 0 | — | — | [باز](DeveloperMenuCampaignActivity.md) |
| 76 | `DeveloperMenuDiscountActivity` | activity | 1 | 11 | 0 | 0 | 0 | — | — | [باز](DeveloperMenuDiscountActivity.md) |
| 77 | `DeveloperMenuFragment` | fragment | 6 | 67 | 0 | 1 | 0 | ✓ | — | [باز](DeveloperMenuFragment.md) |
| 78 | `DevelopersMenuContentExperimentActivity` | activity | 1 | 0 | 0 | 0 | 0 | ✓ | — | [باز](DevelopersMenuContentExperimentActivity.md) |
| 79 | `ExecutableLessonFragment` | dex-ui-class | 0 | 14 | 0 | 1 | 0 | — | — | [باز](ExecutableLessonFragment.md) |
| 80 | `ExecutableLessonScreenKt` | dex-ui-class | 0 | 0 | 0 | 0 | 0 | — | — | [باز](ExecutableLessonScreenKt.md) |
| 81 | `ExecutableLessonViewModel` | dex-ui-class | 0 | 0 | 0 | 0 | 0 | — | — | [باز](ExecutableLessonViewModel.md) |
| 82 | `ExtendedUpsellFlowActivity` | activity | 0 | 0 | 0 | 0 | 0 | — | — | [باز](ExtendedUpsellFlowActivity.md) |
| 83 | `ExtendedUpsellFlowScreenKt` | dex-ui-class | 0 | 0 | 0 | 0 | 0 | — | — | [باز](ExtendedUpsellFlowScreenKt.md) |
| 84 | `FacebookActivity` | activity | 7 | 32 | 13 | 16 | 7 | — | — | [باز](FacebookActivity.md) |
| 85 | `FakeLeaderboardsResultBottomSheetDialogFragment` | dex-ui-class | 0 | 0 | 0 | 0 | 0 | — | — | [باز](FakeLeaderboardsResultBottomSheetDialogFragment.md) |
| 86 | `FakeLeaderboardsResultBottomSheetDialogFragment$onViewCreated$1` | bottom_sheet | 0 | 0 | 0 | 0 | 0 | — | — | [باز](FakeLeaderboardsResultBottomSheetDialogFragment_onViewCreated_1.md) |
| 87 | `FakeLeaderboardsResultBottomSheetDialogFragment$onViewCreated$1$1` | bottom_sheet | 0 | 0 | 0 | 0 | 0 | — | — | [باز](FakeLeaderboardsResultBottomSheetDialogFragment_onViewCreated_1_1.md) |
| 88 | `FakeStreakBottomSheetDialogFragment` | dex-ui-class | 0 | 0 | 0 | 0 | 0 | — | — | [باز](FakeStreakBottomSheetDialogFragment.md) |
| 89 | `FakeStreakBottomSheetDialogFragment$onViewCreated$1` | bottom_sheet | 0 | 0 | 0 | 0 | 0 | — | — | [باز](FakeStreakBottomSheetDialogFragment_onViewCreated_1.md) |
| 90 | `FakeStreakBottomSheetDialogFragment$onViewCreated$1$1` | bottom_sheet | 0 | 0 | 0 | 0 | 0 | — | — | [باز](FakeStreakBottomSheetDialogFragment_onViewCreated_1_1.md) |
| 91 | `FeatureIntroductionModalData` | dex-ui-class | 0 | 0 | 0 | 0 | 0 | — | — | [باز](FeatureIntroductionModalData.md) |
| 92 | `FreeStreakGoalScreenKt` | dex-ui-class | 0 | 0 | 0 | 0 | 0 | — | — | [باز](FreeStreakGoalScreenKt.md) |
| 93 | `GenericIdpActivity` | activity | 0 | 0 | 0 | 0 | 0 | — | — | [باز](GenericIdpActivity.md) |
| 94 | `GenericShareFragment` | dex-ui-class | 1 | 0 | 0 | 0 | 0 | — | — | [باز](GenericShareFragment.md) |
| 95 | `GistModalActivity` | activity | 0 | 0 | 0 | 0 | 0 | — | — | [باز](GistModalActivity.md) |
| 96 | `GoogleApiActivity` | activity | 0 | 1 | 0 | 0 | 0 | — | — | [باز](GoogleApiActivity.md) |
| 97 | `HardModeAiTutorIntroBottomSheetKt` | dex-ui-class | 0 | 0 | 0 | 0 | 0 | — | — | [باز](HardModeAiTutorIntroBottomSheetKt.md) |
| 98 | `HardModeAiTutorIntroBottomSheetKt$HardModeAiTutorAnimatedSpeechBubble$1$1` | bottom_sheet | 0 | 0 | 0 | 0 | 0 | — | — | [باز](HardModeAiTutorIntroBottomSheetKt_HardModeAiTutorAnimatedSpeechBubble_1_1.md) |
| 99 | `HiddenActivity` | activity | 0 | 0 | 0 | 0 | 0 | — | — | [باز](HiddenActivity.md) |
| 100 | `HonestFreeTrialFragment` | fragment | 1 | 8 | 0 | 0 | 0 | ✓ | — | [باز](HonestFreeTrialFragment.md) |
| 101 | `IdentityCredentialApiHiddenActivity` | activity | 0 | 0 | 0 | 0 | 0 | — | — | [باز](IdentityCredentialApiHiddenActivity.md) |
| 102 | `ImageSourceChooserContentKt` | dex-ui-class | 0 | 0 | 0 | 0 | 0 | — | — | [باز](ImageSourceChooserContentKt.md) |
| 103 | `InputConsoleActivity` | activity | 0 | 6 | 0 | 0 | 0 | — | — | [باز](InputConsoleActivity.md) |
| 104 | `InstructionsBottomSheetKt` | dex-ui-class | 0 | 0 | 0 | 0 | 0 | — | — | [باز](InstructionsBottomSheetKt.md) |
| 105 | `InstructionsBottomSheetKt$InstructionsBottomSheet$1$1` | bottom_sheet | 0 | 0 | 0 | 0 | 0 | — | — | [باز](InstructionsBottomSheetKt_InstructionsBottomSheet_1_1.md) |
| 106 | `InstructionsBottomSheetKt$InstructionsBottomSheetHeader$2$1` | bottom_sheet | 0 | 0 | 0 | 0 | 0 | — | — | [باز](InstructionsBottomSheetKt_InstructionsBottomSheetHeader_2_1.md) |
| 107 | `IntegratedWebViewActivity` | activity | 1 | 0 | 0 | 0 | 0 | — | ✓ | [باز](IntegratedWebViewActivity.md) |
| 108 | `InteractiveLessonBaseFragment` | dex-ui-class | 0 | 0 | 0 | 0 | 0 | — | — | [باز](InteractiveLessonBaseFragment.md) |
| 109 | `InteractiveLessonFragment` | dex-ui-class | 0 | 0 | 0 | 0 | 0 | — | — | [باز](InteractiveLessonFragment.md) |
| 110 | `InteractiveLessonValidatedInputFragment` | dex-ui-class | 0 | 0 | 0 | 0 | 0 | — | — | [باز](InteractiveLessonValidatedInputFragment.md) |
| 111 | `InteractiveWebViewLessonFragment` | dex-ui-class | 0 | 0 | 0 | 0 | 0 | — | — | [باز](InteractiveWebViewLessonFragment.md) |
| 112 | `IntroSlidesActivity` | activity | 2 | 1 | 0 | 1 | 0 | ✓ | — | [باز](IntroSlidesActivity.md) |
| 113 | `IntroductionFragment` | fragment | 4 | 3 | 0 | 0 | 0 | ✓ | — | [باز](IntroductionFragment.md) |
| 114 | `InvisibleActionTrampolineActivity` | activity | 0 | 0 | 0 | 0 | 0 | — | — | [باز](InvisibleActionTrampolineActivity.md) |
| 115 | `InviteOverviewBottomSheetDialogFragment` | dex-ui-class | 0 | 0 | 0 | 0 | 0 | — | — | [باز](InviteOverviewBottomSheetDialogFragment.md) |
| 116 | `InviteOverviewBottomSheetDialogFragment$handleInvitationsOverviewData$2` | bottom_sheet | 0 | 0 | 0 | 0 | 0 | — | — | [باز](InviteOverviewBottomSheetDialogFragment_handleInvitationsOverviewData_2.md) |
| 117 | `InviteOverviewBottomSheetDialogFragment$handleInvitationsOverviewData$3` | bottom_sheet | 0 | 0 | 0 | 0 | 0 | — | — | [باز](InviteOverviewBottomSheetDialogFragment_handleInvitationsOverviewData_3.md) |
| 118 | `KeysBottomSheetKt` | dex-ui-class | 0 | 0 | 0 | 0 | 0 | — | — | [باز](KeysBottomSheetKt.md) |
| 119 | `KeysBottomSheetKt$KeysBottomSheet$1$1` | bottom_sheet | 0 | 0 | 0 | 0 | 0 | — | — | [باز](KeysBottomSheetKt_KeysBottomSheet_1_1.md) |
| 120 | `KeysBottomSheetKt$KeysBottomSheet$2$1` | bottom_sheet | 0 | 0 | 0 | 0 | 0 | — | — | [باز](KeysBottomSheetKt_KeysBottomSheet_2_1.md) |
| 121 | `KeysBottomSheetKt$KeysBottomSheet$3$1$2$1` | bottom_sheet | 0 | 0 | 0 | 0 | 0 | — | — | [باز](KeysBottomSheetKt_KeysBottomSheet_3_1_2_1.md) |
| 122 | `KeysLocalDiscountBottomSheetKt` | dex-ui-class | 0 | 0 | 0 | 0 | 0 | — | — | [باز](KeysLocalDiscountBottomSheetKt.md) |
| 123 | `KeysLocalDiscountBottomSheetKt$KeysLocalDiscountBottomSheet$1$1` | bottom_sheet | 0 | 0 | 0 | 0 | 0 | — | — | [باز](KeysLocalDiscountBottomSheetKt_KeysLocalDiscountBottomSheet_1_1.md) |
| 124 | `KeysLocalDiscountBottomSheetViewModel` | dex-ui-class | 0 | 0 | 0 | 0 | 0 | — | — | [باز](KeysLocalDiscountBottomSheetViewModel.md) |
| 125 | `KeysLocalDiscountBottomSheetViewModel$container$1` | bottom_sheet | 0 | 0 | 0 | 0 | 0 | — | — | [باز](KeysLocalDiscountBottomSheetViewModel_container_1.md) |
| 126 | `KeysLocalDiscountBottomSheetViewModel$container$1$1` | bottom_sheet | 0 | 0 | 0 | 0 | 0 | — | — | [باز](KeysLocalDiscountBottomSheetViewModel_container_1_1.md) |
| 127 | `KeysLocalDiscountBottomSheetViewModel$container$1$1$1` | bottom_sheet | 0 | 0 | 0 | 0 | 0 | — | — | [باز](KeysLocalDiscountBottomSheetViewModel_container_1_1_1.md) |
| 128 | `KeysLocalDiscountBottomSheetViewModel$container$1$1$2` | bottom_sheet | 0 | 0 | 0 | 0 | 0 | — | — | [باز](KeysLocalDiscountBottomSheetViewModel_container_1_1_2.md) |
| 129 | `KeysLocalDiscountBottomSheetViewModel$container$1$1$3` | bottom_sheet | 0 | 0 | 0 | 0 | 0 | — | — | [باز](KeysLocalDiscountBottomSheetViewModel_container_1_1_3.md) |
| 130 | `KeysLocalDiscountBottomSheetViewModel$getTitleAndSubtitle$2` | bottom_sheet | 0 | 0 | 0 | 0 | 0 | — | — | [باز](KeysLocalDiscountBottomSheetViewModel_getTitleAndSubtitle_2.md) |
| 131 | `KeysLocalDiscountBottomSheetViewModel$observePurchaseUpdates$2` | bottom_sheet | 0 | 0 | 0 | 0 | 0 | — | — | [باز](KeysLocalDiscountBottomSheetViewModel_observePurchaseUpdates_2.md) |
| 132 | `KeysLocalDiscountBottomSheetViewModel$observePurchaseUpdates$2$1` | bottom_sheet | 0 | 0 | 0 | 0 | 0 | — | — | [باز](KeysLocalDiscountBottomSheetViewModel_observePurchaseUpdates_2_1.md) |
| 133 | `KeysLocalDiscountBottomSheetViewModel$observePurchaseUpdates$2$1$2` | bottom_sheet | 0 | 0 | 0 | 0 | 0 | — | — | [باز](KeysLocalDiscountBottomSheetViewModel_observePurchaseUpdates_2_1_2.md) |
| 134 | `KeysLocalDiscountBottomSheetViewModel$observePurchaseUpdates$2$1$invokeSuspend$$inlined$filter$1$1` | bottom_sheet | 0 | 0 | 0 | 0 | 0 | — | — | [باز](KeysLocalDiscountBottomSheetViewModel_observePurchaseUpdates_2_1_invokeSuspend__inlined_filter_1_1.md) |
| 135 | `KeysLocalDiscountBottomSheetViewModel$observePurchaseUpdates$2$1$invokeSuspend$$inlined$filter$1$2$1` | bottom_sheet | 0 | 0 | 0 | 0 | 0 | — | — | [باز](KeysLocalDiscountBottomSheetViewModel_observePurchaseUpdates_2_1_invokeSuspend__inlined_filter_1_2_1.md) |
| 136 | `KeysLocalDiscountBottomSheetViewModel$startCountdown$2` | bottom_sheet | 0 | 0 | 0 | 0 | 0 | — | — | [باز](KeysLocalDiscountBottomSheetViewModel_startCountdown_2.md) |
| 137 | `KeysLocalDiscountBottomSheetViewModel$startCountdown$2$1` | bottom_sheet | 0 | 0 | 0 | 0 | 0 | — | — | [باز](KeysLocalDiscountBottomSheetViewModel_startCountdown_2_1.md) |
| 138 | `LeaderboardFragment` | dex-ui-class | 25 | 51 | 0 | 9 | 0 | ✓ | — | [باز](LeaderboardFragment.md) |
| 139 | `LearningCompanionsIntroActivity` | activity | 0 | 2 | 0 | 0 | 0 | — | — | [باز](LearningCompanionsIntroActivity.md) |
| 140 | `LearningCompanionsIntroFragment` | dex-ui-class | 0 | 2 | 0 | 0 | 0 | — | — | [باز](LearningCompanionsIntroFragment.md) |
| 141 | `LoginSetEmailFragment` | dex-ui-class | 1 | 0 | 0 | 0 | 0 | ✓ | — | [باز](LoginSetEmailFragment.md) |
| 142 | `LoginSetPasswordFragment` | dex-ui-class | 1 | 0 | 0 | 0 | 0 | ✓ | — | [باز](LoginSetPasswordFragment.md) |
| 143 | `MainActivity` | activity | 1 | 0 | 0 | 3 | 0 | — | — | [باز](MainActivity.md) |
| 144 | `MainActivity$showRewardBottomSheet$1` | bottom_sheet | 1 | 0 | 0 | 0 | 0 | — | — | [باز](MainActivity_showRewardBottomSheet_1.md) |
| 145 | `MainActivity$showRewardBottomSheet$fragment$1` | bottom_sheet | 1 | 0 | 0 | 0 | 0 | — | — | [باز](MainActivity_showRewardBottomSheet_fragment_1.md) |
| 146 | `MainViewModel` | dex-ui-class | 0 | 0 | 0 | 0 | 0 | — | — | [باز](MainViewModel.md) |
| 147 | `ModalData` | dex-ui-class | 0 | 0 | 0 | 0 | 0 | — | — | [باز](ModalData.md) |
| 148 | `ModalData$AppIconChangeNeedsRestart` | modal | 0 | 0 | 0 | 0 | 0 | — | — | [باز](ModalData_AppIconChangeNeedsRestart.md) |
| 149 | `ModalData$CertificateCompletionInfo` | modal | 0 | 0 | 0 | 0 | 0 | — | — | [باز](ModalData_CertificateCompletionInfo.md) |
| 150 | `ModalData$CertificateNotFinishedYetModalData` | modal | 0 | 0 | 0 | 0 | 0 | — | — | [باز](ModalData_CertificateNotFinishedYetModalData.md) |
| 151 | `ModalData$CertificateProfessionalInfo` | modal | 0 | 0 | 0 | 0 | 0 | — | — | [باز](ModalData_CertificateProfessionalInfo.md) |
| 152 | `ModalData$ContentRearrange` | modal | 0 | 0 | 0 | 0 | 0 | — | — | [باز](ModalData_ContentRearrange.md) |
| 153 | `ModalData$DeveloperMenuDownloadLiveContent` | modal | 0 | 0 | 0 | 0 | 0 | — | — | [باز](ModalData_DeveloperMenuDownloadLiveContent.md) |
| 154 | `ModalData$DeveloperMenuLiveDeploymentError` | modal | 0 | 0 | 0 | 0 | 0 | — | — | [باز](ModalData_DeveloperMenuLiveDeploymentError.md) |
| 155 | `ModalData$FirebaseInAppMessages` | modal | 0 | 0 | 0 | 0 | 0 | — | — | [باز](ModalData_FirebaseInAppMessages.md) |
| 156 | `ModalData$FriendsAcceptedInviteNoPro` | modal | 0 | 0 | 0 | 0 | 0 | — | — | [باز](ModalData_FriendsAcceptedInviteNoPro.md) |
| 157 | `ModalData$FriendsAcceptedInvitePro` | modal | 0 | 0 | 0 | 0 | 0 | — | — | [باز](ModalData_FriendsAcceptedInvitePro.md) |
| 158 | `ModalData$InputConsoleIntroduction` | modal | 0 | 0 | 0 | 0 | 0 | — | — | [باز](ModalData_InputConsoleIntroduction.md) |
| 159 | `ModalData$InviteFriendsNoPro` | modal | 0 | 0 | 0 | 0 | 0 | — | — | [باز](ModalData_InviteFriendsNoPro.md) |
| 160 | `ModalData$InviteFriendsPro` | modal | 0 | 0 | 0 | 0 | 0 | — | — | [باز](ModalData_InviteFriendsPro.md) |
| 161 | `ModalData$JoinedAnInvite` | modal | 0 | 0 | 0 | 0 | 0 | — | — | [باز](ModalData_JoinedAnInvite.md) |
| 162 | `ModalData$NotificationsSettings` | modal | 0 | 0 | 0 | 0 | 0 | — | — | [باز](ModalData_NotificationsSettings.md) |
| 163 | `ModalData$PendingPurchase` | modal | 0 | 0 | 0 | 0 | 0 | — | — | [باز](ModalData_PendingPurchase.md) |
| 164 | `ModalData$SmartPracticeChargedModal` | modal | 0 | 0 | 0 | 0 | 0 | — | — | [باز](ModalData_SmartPracticeChargedModal.md) |
| 165 | `ModalData$SmartPracticeMasteredModal` | modal | 0 | 0 | 0 | 0 | 0 | — | — | [باز](ModalData_SmartPracticeMasteredModal.md) |
| 166 | `ModalData$StreakChallengeFailure` | modal | 0 | 0 | 0 | 0 | 0 | — | — | [باز](ModalData_StreakChallengeFailure.md) |
| 167 | `ModalData$StreakChallengeSuccess` | modal | 0 | 0 | 0 | 0 | 0 | — | — | [باز](ModalData_StreakChallengeSuccess.md) |
| 168 | `ModalData$StreakRepairModal` | modal | 0 | 0 | 0 | 0 | 0 | — | — | [باز](ModalData_StreakRepairModal.md) |
| 169 | `ModalData$TrialStartedEnableNotification` | modal | 0 | 0 | 0 | 0 | 0 | — | — | [باز](ModalData_TrialStartedEnableNotification.md) |
| 170 | `ModalDialogTestActivity` | activity | 0 | 0 | 0 | 0 | 0 | — | — | [باز](ModalDialogTestActivity.md) |
| 171 | `NameCodePlaygroundFragment` | fragment | 1 | 6 | 0 | 0 | 0 | ✓ | — | [باز](NameCodePlaygroundFragment.md) |
| 172 | `NonInteractiveLessonFragment` | dex-ui-class | 0 | 0 | 0 | 0 | 0 | — | — | [باز](NonInteractiveLessonFragment.md) |
| 173 | `NotDismissableBottomSheetBehavior` | bottom_sheet | 0 | 0 | 0 | 0 | 0 | — | — | [باز](NotDismissableBottomSheetBehavior.md) |
| 174 | `NotificationHandlerActivity` | activity | 0 | 0 | 0 | 0 | 0 | — | — | [باز](NotificationHandlerActivity.md) |
| 175 | `OnboardingActivity` | activity | 11 | 158 | 0 | 6 | 0 | ✓ | — | [باز](OnboardingActivity.md) |
| 176 | `OnboardingDevicePreferenceFragment` | fragment | 0 | 4 | 0 | 0 | 0 | — | — | [باز](OnboardingDevicePreferenceFragment.md) |
| 177 | `OnboardingDeviceReassuranceFragment` | fragment | 0 | 6 | 0 | 0 | 0 | — | — | [باز](OnboardingDeviceReassuranceFragment.md) |
| 178 | `OnboardingMotiveReassuranceFragment` | fragment | 0 | 5 | 0 | 0 | 0 | — | — | [باز](OnboardingMotiveReassuranceFragment.md) |
| 179 | `OnboardingPathReassuranceFragment` | fragment | 0 | 6 | 0 | 0 | 0 | — | — | [باز](OnboardingPathReassuranceFragment.md) |
| 180 | `OnboardingPickAPathFragment` | dex-ui-class | 1 | 17 | 0 | 0 | 0 | ✓ | — | [باز](OnboardingPickAPathFragment.md) |
| 181 | `OnboardingPreparingCurriculumFragment` | fragment | 0 | 0 | 0 | 0 | 0 | — | — | [باز](OnboardingPreparingCurriculumFragment.md) |
| 182 | `OnboardingSelectPathContainerFragment` | fragment | 1 | 0 | 0 | 0 | 0 | — | — | [باز](OnboardingSelectPathContainerFragment.md) |
| 183 | `OnboardingSetDailyGoalFragment` | fragment | 1 | 1 | 0 | 0 | 0 | ✓ | — | [باز](OnboardingSetDailyGoalFragment.md) |
| 184 | `OnboardingSetDailyGoalViewModel` | dex-ui-class | 0 | 0 | 0 | 0 | 0 | — | — | [باز](OnboardingSetDailyGoalViewModel.md) |
| 185 | `OnboardingSkillPreferenceFragment` | fragment | 0 | 5 | 0 | 0 | 0 | — | — | [باز](OnboardingSkillPreferenceFragment.md) |
| 186 | `OutOfContextTestingActivity` | activity | 0 | 0 | 0 | 0 | 0 | — | — | [باز](OutOfContextTestingActivity.md) |
| 187 | `PathCompletionEstimationFragment` | fragment | 1 | 16 | 0 | 0 | 0 | ✓ | — | [باز](PathCompletionEstimationFragment.md) |
| 188 | `PathMapFragment` | dex-ui-class | 0 | 3 | 0 | 0 | 0 | — | — | [باز](PathMapFragment.md) |
| 189 | `PathMapScreenKt` | dex-ui-class | 0 | 0 | 0 | 0 | 0 | — | — | [باز](PathMapScreenKt.md) |
| 190 | `PathMapViewModel` | dex-ui-class | 0 | 0 | 0 | 0 | 0 | — | — | [باز](PathMapViewModel.md) |
| 191 | `PathOverviewScreenKt` | dex-ui-class | 0 | 0 | 0 | 0 | 0 | — | — | [باز](PathOverviewScreenKt.md) |
| 192 | `PaywallActivity` | activity | 0 | 0 | 0 | 0 | 0 | — | — | [باز](PaywallActivity.md) |
| 193 | `PaywallActivityKt` | dex-ui-class | 0 | 0 | 0 | 0 | 0 | — | — | [باز](PaywallActivityKt.md) |
| 194 | `PickAPathViewsKt` | dex-ui-class | 0 | 0 | 0 | 0 | 0 | — | — | [باز](PickAPathViewsKt.md) |
| 195 | `PlayCoreDialogWrapperActivity` | activity | 0 | 0 | 0 | 0 | 0 | — | — | [باز](PlayCoreDialogWrapperActivity.md) |
| 196 | `PracticeTabFragment` | dex-ui-class | 1 | 8 | 0 | 0 | 0 | ✓ | — | [باز](PracticeTabFragment.md) |
| 197 | `PracticeTabScreenKt` | dex-ui-class | 0 | 0 | 0 | 0 | 0 | — | — | [باز](PracticeTabScreenKt.md) |
| 198 | `PreviewActivity` | activity | 1 | 8 | 0 | 0 | 0 | — | — | [باز](PreviewActivity.md) |
| 199 | `ProfessionalCertificateActivity` | activity | 0 | 0 | 0 | 0 | 0 | — | — | [باز](ProfessionalCertificateActivity.md) |
| 200 | `ProfessionalCertificateDownloadDialogKt` | dex-ui-class | 0 | 0 | 0 | 0 | 0 | — | — | [باز](ProfessionalCertificateDownloadDialogKt.md) |
| 201 | `ProfileFragment` | fragment | 21 | 28 | 0 | 4 | 0 | ✓ | — | [باز](ProfileFragment.md) |
| 202 | `ProjectScreenKt` | dex-ui-class | 0 | 0 | 0 | 0 | 0 | — | — | [باز](ProjectScreenKt.md) |
| 203 | `ProjectViewModel` | dex-ui-class | 0 | 0 | 0 | 0 | 0 | — | — | [باز](ProjectViewModel.md) |
| 204 | `ProxyAmazonBillingActivity` | activity | 0 | 0 | 0 | 0 | 0 | — | — | [باز](ProxyAmazonBillingActivity.md) |
| 205 | `ProxyBillingActivity` | activity | 0 | 0 | 0 | 0 | 0 | — | — | [باز](ProxyBillingActivity.md) |
| 206 | `ProxyBillingActivityV2` | activity | 0 | 0 | 0 | 0 | 0 | — | — | [باز](ProxyBillingActivityV2.md) |
| 207 | `PublicProfileActivity` | activity | 3 | 5 | 0 | 0 | 0 | — | — | [باز](PublicProfileActivity.md) |
| 208 | `PublicProfileFragment` | dex-ui-class | 3 | 5 | 0 | 0 | 0 | — | — | [باز](PublicProfileFragment.md) |
| 209 | `ReactivationActivity` | activity | 0 | 24 | 0 | 0 | 0 | — | — | [باز](ReactivationActivity.md) |
| 210 | `ReactivationActivityKt` | dex-ui-class | 0 | 0 | 0 | 0 | 0 | — | — | [باز](ReactivationActivityKt.md) |
| 211 | `ReactivationPaywallScreenKt` | dex-ui-class | 0 | 0 | 0 | 0 | 0 | — | — | [باز](ReactivationPaywallScreenKt.md) |
| 212 | `RecaptchaActivity` | activity | 0 | 0 | 0 | 0 | 0 | — | — | [باز](RecaptchaActivity.md) |
| 213 | `RemoteDiscountBottomSheetKt` | dex-ui-class | 0 | 0 | 0 | 0 | 0 | — | — | [باز](RemoteDiscountBottomSheetKt.md) |
| 214 | `RemoteDiscountBottomSheetKt$RemoteDiscountBottomSheet$1$1` | bottom_sheet | 0 | 0 | 0 | 0 | 0 | — | — | [باز](RemoteDiscountBottomSheetKt_RemoteDiscountBottomSheet_1_1.md) |
| 215 | `ReportLessonFragment` | dex-ui-class | 1 | 11 | 0 | 0 | 0 | ✓ | — | [باز](ReportLessonFragment.md) |
| 216 | `ResubscribeProPaywallFragment` | dex-ui-class | 0 | 0 | 0 | 0 | 0 | — | — | [باز](ResubscribeProPaywallFragment.md) |
| 217 | `ResubscribeProPaywallFragmentKt` | dex-ui-class | 0 | 0 | 0 | 0 | 0 | — | — | [باز](ResubscribeProPaywallFragmentKt.md) |
| 218 | `RewardFragment` | dex-ui-class | 6 | 8 | 0 | 0 | 0 | — | — | [باز](RewardFragment.md) |
| 219 | `RewardScreenViewModel` | dex-ui-class | 0 | 0 | 0 | 0 | 0 | — | — | [باز](RewardScreenViewModel.md) |
| 220 | `RewardTabletDialogFragment` | dex-ui-class | 1 | 0 | 0 | 0 | 0 | — | — | [باز](RewardTabletDialogFragment.md) |
| 221 | `Screen` | dex-ui-class | 0 | 24 | 0 | 17 | 9 | — | — | [باز](Screen.md) |
| 222 | `SearchTrackFragment` | dex-ui-class | 2 | 1 | 0 | 0 | 0 | — | — | [باز](SearchTrackFragment.md) |
| 223 | `SetDailyGoalActivity` | activity | 4 | 1 | 0 | 0 | 0 | ✓ | — | [باز](SetDailyGoalActivity.md) |
| 224 | `SetExperienceFragment` | fragment | 1 | 7 | 0 | 0 | 0 | ✓ | — | [باز](SetExperienceFragment.md) |
| 225 | `SetMotiveFragment` | fragment | 0 | 6 | 0 | 0 | 0 | — | — | [باز](SetMotiveFragment.md) |
| 226 | `SetOccupationFragment` | fragment | 1 | 6 | 0 | 0 | 0 | — | — | [باز](SetOccupationFragment.md) |
| 227 | `SetReminderTimeFragment` | fragment | 1 | 0 | 0 | 0 | 0 | ✓ | — | [باز](SetReminderTimeFragment.md) |
| 228 | `SetWorkFunctionFragment` | fragment | 1 | 8 | 0 | 0 | 0 | — | — | [باز](SetWorkFunctionFragment.md) |
| 229 | `SettingsActivity` | activity | 7 | 72 | 0 | 0 | 0 | ✓ | — | [باز](SettingsActivity.md) |
| 230 | `SettingsFragment` | fragment | 7 | 72 | 0 | 0 | 0 | ✓ | — | [باز](SettingsFragment.md) |
| 231 | `ShowInviteDialogSource$InviteBottomSheet` | bottom_sheet | 0 | 0 | 0 | 0 | 0 | — | — | [باز](ShowInviteDialogSource_InviteBottomSheet.md) |
| 232 | `SignInHubActivity` | activity | 0 | 0 | 0 | 0 | 0 | — | — | [باز](SignInHubActivity.md) |
| 233 | `SignUpSetEmailFragment` | dex-ui-class | 1 | 0 | 0 | 0 | 0 | ✓ | — | [باز](SignUpSetEmailFragment.md) |
| 234 | `SignUpSetPasswordFragment` | dex-ui-class | 1 | 0 | 0 | 0 | 0 | ✓ | — | [باز](SignUpSetPasswordFragment.md) |
| 235 | `SignUpSetUsernameFragment` | dex-ui-class | 1 | 0 | 0 | 0 | 0 | ✓ | — | [باز](SignUpSetUsernameFragment.md) |
| 236 | `SimulatedStoreErrorDialogActivity` | activity | 0 | 0 | 0 | 0 | 0 | — | — | [باز](SimulatedStoreErrorDialogActivity.md) |
| 237 | `SplashActivity` | activity | 1 | 0 | 0 | 7 | 0 | — | — | [باز](SplashActivity.md) |
| 238 | `StoreBottomSheetKt` | dex-ui-class | 0 | 0 | 0 | 0 | 0 | — | — | [باز](StoreBottomSheetKt.md) |
| 239 | `StoreBottomSheetKt$StoreBottomSheet$2$1$1$1` | bottom_sheet | 0 | 0 | 0 | 0 | 0 | — | — | [باز](StoreBottomSheetKt_StoreBottomSheet_2_1_1_1.md) |
| 240 | `StoreBottomSheetKt$StoreBottomSheet$6$1` | bottom_sheet | 0 | 0 | 0 | 0 | 0 | — | — | [باز](StoreBottomSheetKt_StoreBottomSheet_6_1.md) |
| 241 | `StoreBottomSheetKt$StoreBottomSheet$7$1` | bottom_sheet | 0 | 0 | 0 | 0 | 0 | — | — | [باز](StoreBottomSheetKt_StoreBottomSheet_7_1.md) |
| 242 | `StoreBottomSheetKt$StoreBottomSheet$8$1` | bottom_sheet | 0 | 0 | 0 | 0 | 0 | — | — | [باز](StoreBottomSheetKt_StoreBottomSheet_8_1.md) |
| 243 | `StoreBottomSheetKt$StoreBottomSheet$9$1` | bottom_sheet | 0 | 0 | 0 | 0 | 0 | — | — | [باز](StoreBottomSheetKt_StoreBottomSheet_9_1.md) |
| 244 | `StoreBottomSheetKt$StoreBottomSheet$9$1$1` | bottom_sheet | 0 | 0 | 0 | 0 | 0 | — | — | [باز](StoreBottomSheetKt_StoreBottomSheet_9_1_1.md) |
| 245 | `StreakBottomSheetFragment` | dex-ui-class | 1 | 0 | 0 | 0 | 0 | ✓ | — | [باز](StreakBottomSheetFragment.md) |
| 246 | `StreakBottomSheetFragment$configureRecyclerView$2` | bottom_sheet | 1 | 0 | 0 | 0 | 0 | ✓ | — | [باز](StreakBottomSheetFragment_configureRecyclerView_2.md) |
| 247 | `StreakBottomSheetFragment$configureRecyclerView$3` | bottom_sheet | 1 | 0 | 0 | 0 | 0 | ✓ | — | [باز](StreakBottomSheetFragment_configureRecyclerView_3.md) |
| 248 | `StreakBottomSheetFragment$configureRecyclerView$4` | bottom_sheet | 1 | 0 | 0 | 0 | 0 | ✓ | — | [باز](StreakBottomSheetFragment_configureRecyclerView_4.md) |
| 249 | `StreakBottomSheetFragment$configureRecyclerView$5` | bottom_sheet | 1 | 0 | 0 | 0 | 0 | ✓ | — | [باز](StreakBottomSheetFragment_configureRecyclerView_5.md) |
| 250 | `StreakBottomSheetFragment$configureRecyclerView$streakMonthAdapter$1` | bottom_sheet | 1 | 0 | 0 | 0 | 0 | ✓ | — | [باز](StreakBottomSheetFragment_configureRecyclerView_streakMonthAdapter_1.md) |
| 251 | `StreakBottomSheetFragment$onViewCreated$1` | bottom_sheet | 1 | 0 | 0 | 0 | 0 | ✓ | — | [باز](StreakBottomSheetFragment_onViewCreated_1.md) |
| 252 | `StreakBottomSheetFragment$onViewCreated$1$1` | bottom_sheet | 1 | 0 | 0 | 0 | 0 | ✓ | — | [باز](StreakBottomSheetFragment_onViewCreated_1_1.md) |
| 253 | `StreakBottomSheetFragment$onViewCreated$2` | bottom_sheet | 1 | 0 | 0 | 0 | 0 | ✓ | — | [باز](StreakBottomSheetFragment_onViewCreated_2.md) |
| 254 | `StreakBottomSheetFragment$onViewCreated$2$1` | bottom_sheet | 1 | 0 | 0 | 0 | 0 | ✓ | — | [باز](StreakBottomSheetFragment_onViewCreated_2_1.md) |
| 255 | `StreakBottomSheetViewModel` | dex-ui-class | 0 | 0 | 0 | 0 | 0 | — | — | [باز](StreakBottomSheetViewModel.md) |
| 256 | `StreakBottomSheetViewModel$fetchProfileData$1` | bottom_sheet | 0 | 0 | 0 | 0 | 0 | — | — | [باز](StreakBottomSheetViewModel_fetchProfileData_1.md) |
| 257 | `StreakBottomSheetViewModel$special$$inlined$map$1$1` | bottom_sheet | 0 | 0 | 0 | 0 | 0 | — | — | [باز](StreakBottomSheetViewModel_special__inlined_map_1_1.md) |
| 258 | `StreakBottomSheetViewModel$special$$inlined$map$1$2$1` | bottom_sheet | 0 | 0 | 0 | 0 | 0 | — | — | [باز](StreakBottomSheetViewModel_special__inlined_map_1_2_1.md) |
| 259 | `StreakBottomSheetViewModel$special$$inlined$map$2$1` | bottom_sheet | 0 | 0 | 0 | 0 | 0 | — | — | [باز](StreakBottomSheetViewModel_special__inlined_map_2_1.md) |
| 260 | `StreakBottomSheetViewModel$special$$inlined$map$2$2$1` | bottom_sheet | 0 | 0 | 0 | 0 | 0 | — | — | [باز](StreakBottomSheetViewModel_special__inlined_map_2_2_1.md) |
| 261 | `StreakBottomSheetViewModel$trackOpenStreakBottomSheet$1` | bottom_sheet | 0 | 0 | 0 | 0 | 0 | — | — | [باز](StreakBottomSheetViewModel_trackOpenStreakBottomSheet_1.md) |
| 262 | `StreakBottomSheetViewModel$userStreakInfo$1` | bottom_sheet | 0 | 0 | 0 | 0 | 0 | — | — | [باز](StreakBottomSheetViewModel_userStreakInfo_1.md) |
| 263 | `StreakBottomSheetViewModel$userStreakMonth$3` | bottom_sheet | 0 | 0 | 0 | 0 | 0 | — | — | [باز](StreakBottomSheetViewModel_userStreakMonth_3.md) |
| 264 | `StreakBottomSheetViewModel$userStreakMonth$lambda$1$$inlined$map$1$1` | bottom_sheet | 0 | 0 | 0 | 0 | 0 | — | — | [باز](StreakBottomSheetViewModel_userStreakMonth_lambda_1__inlined_map_1_1.md) |
| 265 | `StreakBottomSheetViewModel$userStreakMonth$lambda$1$$inlined$map$1$2$1` | bottom_sheet | 0 | 0 | 0 | 0 | 0 | — | — | [باز](StreakBottomSheetViewModel_userStreakMonth_lambda_1__inlined_map_1_2_1.md) |
| 266 | `TrialReminderChoiceFragment` | fragment | 0 | 3 | 0 | 0 | 0 | — | — | [باز](TrialReminderChoiceFragment.md) |
| 267 | `UpgradeCompletedActivity` | activity | 0 | 6 | 0 | 0 | 0 | — | — | [باز](UpgradeCompletedActivity.md) |
| 268 | `UpgradeCompletedScreenKt` | dex-ui-class | 0 | 0 | 0 | 0 | 0 | — | — | [باز](UpgradeCompletedScreenKt.md) |
| 269 | `UpgradeModalActivity` | activity | 3 | 21 | 0 | 1 | 0 | ✓ | — | [باز](UpgradeModalActivity.md) |
| 270 | `UpgradeModalBottomView` | dex-ui-class | 1 | 0 | 0 | 0 | 0 | ✓ | — | [باز](UpgradeModalBottomView.md) |
| 271 | `UpgradeModalContent` | dex-ui-class | 0 | 0 | 0 | 0 | 0 | — | — | [باز](UpgradeModalContent.md) |
| 272 | `UpgradeModalPageData` | dex-ui-class | 0 | 0 | 0 | 0 | 0 | — | — | [باز](UpgradeModalPageData.md) |
| 273 | `ViewsKt` | dex-ui-class | 0 | 0 | 0 | 0 | 0 | — | — | [باز](ViewsKt.md) |
| 274 | `WebViewActivity` | activity | 0 | 0 | 0 | 0 | 0 | — | — | [باز](WebViewActivity.md) |
| 275 | `WebViewActivityResult` | dex-ui-class | 0 | 0 | 0 | 0 | 0 | — | — | [باز](WebViewActivityResult.md) |
| 276 | `WrapperFragmentActivity` | activity | 1 | 0 | 0 | 0 | 0 | — | — | [باز](WrapperFragmentActivity.md) |

## گروهبندی سفر کاربر (برای خواندن سریع)

| # | سفر | سطوح کلیدی |
|---|---|---|
| ۱ | بوت / ورود | `SplashActivity` (+ ۶ alias)، `AuthenticationActivity`، `SignupActivity` |
| ۲ | آنبوردینگ | `OnboardingActivity` + ۱۲ مرحله + `nav_onboarding_graph.xml` |
| ۳ | خانهٔ مسیرها | `MainActivity`، تبها، کارت مسیر |
| ۴ | اجرای درس | `ChapterActivity`، `LessonInteractive*Fragment`، `ExecutableLesson*Fragment` |
| ۵ | پایان فصل | `ChapterFinished*Fragment`، زنجیرهٔ مودال جایزه/زنجیره/ارتقا |
| ۶ | تمرین / مربی / فروشگاه | `Practice*`, `AiTutor*`, `AllPlans*`, `Paywall*` |
| ۷ | پروفایل / تنظیمات | `Profile*`, `Settings*`, `Certificate*`, `ChangeAppIconActivity` |
| ۸ | ویجت / دولوپر | `MimoStreakWidget`, `DeveloperMenu*` |

> `CATALOGS/SCREEN_INDEX.csv` همان جدول بالا به صورت ماشینی است.
> `SCREENS/INDEX.md` نسخهٔ Markdown با لینک مستقیم به تکتک پروندهها.
