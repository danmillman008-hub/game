# REVIEW — اصلاح مسیر تحلیل (بدون ابزار جدید،REAL ANALYSIS CHAIN)

> وضعیت: **REVIEW / منتظر تأیید شما**. هیچ «تأییدشده»ای ادعا نمیشود.
> تاریخ: ۲۰۲۶‑۱۱‑۰۵ | شاخه: `arena/aebb90b7-game`
> دامنه این سند: فقط `ANALYSIS/` و `TOOLS/` و ورکفلو موقت تحلیل. به `mimo-ui/UPGRADE`، ZIP، MANIFEST، verifier و طرح v12 در Drive **هیچ دستی زده نشده است**.

---

## ۱. پذیرش اصلاحیه شما

اصلاحیه پذیرفته شد:

- REA و Ghidra **حذف نشدند**؛ در `TOOLS/rea` و `TOOLS/ghidra`، جدا از خط اصلی `mimo-ui/UPGRADE` باقی ماندند.
- **هیچ ابزار جدیدی به مجموعه اضافه نشد**؛ نه JEB، نه نسخه تازهای از JADX روی کل APK، نه دیکامپایلر/پلاگین تازه. JEB فقط یک خرید/اجرای جداگانه است (`REA_JEB_MCP_URL=http://127.0.0.1:8425/mcp`) و REA آن را نصب نمیکند؛ فعلاً توصیه و اضافه نشده است.
- بهجای «اضافهکردن ابزار»، **زنجیره تحلیل اصلاح شد**: Ghidra با Auto Analysis واقعی، Smali دقیق، Kotlin `DebugMetadata` / ماشین حالت coroutine، و الحاق شواهد.
- جستوجوی نسخههای بیشتر JADX روی کل APK متوقف شد. نتیجه صادقانه JADX ۱.۵.۶ همان است که قبلاً ثبت شد: ۲٬۲۱۱ فایل Java، ۲٬۱۷۹ فایل دارای stub «Method not decompiled»، ۲۴۳٬۰۰۲ خطای `jadx.log`. JADX برای **بازسازی نامها/امضاها/آنوتیشنها** استفاده شد، نه برای ادعای بدنه کامل متدها.

نقشها همان چیزی است که شما تعیین کردید:

| لایه | ابزار | نقش واقعی (آنچه انجام شد) |
|---|---|---|
| مدیریت وظیفه/شواهد | REA | جهتدهی، `doctor`، نگهداشت محدودیتها؛ **جایگزین خودکار شکست JADX با Ghidra نیست** |
| بازسازی Java/Kotlin | JADX ۱.۱.۰ / ۱.۵.۶ / MCP | نام کلاسها، `@Metadata`، `@f70/c` = `DebugMetadata`، امضاها، ۵۳ نقطه Retrofit |
| کنترل جریان سطح پایین | Ghidra ۱۲.۲ + Auto Analysis | **۱۲۲٬۵۴۶ تابع**، ۱٬۲۸۴٬۵۴۲ نماد، دستورالعملهای Dalvik واقعی، شاخهها و `invoke_*` |
| اسمبلی دقیق | Baksmali / Apktool (smali ۲.۳.۴ و ۳.x) | ۱۷٬۶۲۶ فایل `.smali`، ۵۳۹ آنوتیشن `DebugMetadata`، ۸۴ فیلد ماشین حالت |
| JDK جدا | Temurin JDK ۲۵ (Ghidra) و Temurin **full JDK ۲۱** (REA، دارای `jdk.compiler`) | دو `JAVA_HOME` مجزا در همان ورکفلو؛ `jdk.compiler@21.0.13` تأیید شد |

---

## ۲. اصلاحات اجراشده (قبل → بعد)

| مورد | قبل | بعد |
|---|---|---|
| پوشش DEX | فقط ۳ فایل در Ghidra | **همه ۱۲ فایل** `ANALYSIS/_INPUT/classes*.dex` (۲۸٬۸۳۶٬۰۸۸ بایت) + `DEX_INVENTORY.json` |
| Auto Analysis | `-noanalysis` → **functions=0** | بدون `-noanalysis` روی **همه ۱۲ DEX** → ۵۴٬۵۳۰ / ۵۳٬۲۴۷ / ۱۴٬۷۰۴ / ۴۱ / ۳×۸ تابع |
| نمادها | ۹۰٬۲۴۸ نماد (فقط ۳ DEX، `-noanalysis`) | ۶۸۱٬۹۷۶ + ۴۶۳٬۵۰۰ + ۱۳۶٬۹۷۷ + ۱٬۵۳۷ + ۵۵۲ = **۱٬۲۸۴٬۵۴۲ نماد** |
| کنترل جریان | هیچ | ۶۰ تابع `ui::path::map` + ۶۲ تابع نمره/اتمام با دستورالعمل Dalvik؛ ۲۵٬۹۸۰ شاخه و ۴۱٬۶۲۹ `invoke` در ۸٬۰۰۰ تابع نخست `classes.dex` |
| JDK | `jdk4py` فقط `java 25.0.2`، بدون `jdk.compiler` / `javac` → `rea doctor` ناسالم | جداگانه: JDK ۲۵ برای Ghidra، **full JDK ۲۱** برای REA؛ `rea doctor --provider jadx` → `healthy:true`، `node ✓`، `jadx ✓`، `ghidra ✓`، `ghidra-headless ✓`، `native_decompiler ✓` |
| JADX | تلاش برای نسخههای بیشتر | متوقف؛ محدودیت شفاف ثبت شد |
| Coroutine | فقط حدس | ۵۳۹ `@f70/c` (`DebugMetadata`)، ۶۵۲ کلاس `SuspendLambda`/`invokeSuspend`، فیلدهای `label:I` (۴۶)، `L$0..L$4` (۳۳)، `J$0` (۳)، `I$0/I$1` (۲) |

### وضعیت صادقانه `rea doctor`
`healthy:true` ولی `environment_healthy:false`. دو «config drift» باقی است و پنهان نشده: REA انتظار Ghidra ۱۲٫۱.x دارد (ما ۱۲٫۲ داریم) و انتظار JDK ۲۵+ دارد (ما عمداً ۲۱ جداگانه دادیم)؛ Hopper/IDA هم نصب نیستند و خارج از دامنهاند. **ادعای سلامت کامل محیط REA نمیشود.**

### محدودیت Smali (مهم)
 Baksmali ۲.۳.۴ و Apktool ۲.۹.۳ (با smali مدرن ۳.x) هر دو روی `classes.dex` دقیقاً **۱۱٬۸۲۸ شکست** `Invalid element width: 3/5/7/…/19` میدهند؛ نتیجه یکسان یعنی مشکل «نسخه ابزار» نیست، بلکه ساختار payload آرایههای این DEX است. بنابراین:

- ۱۷٬۶۲۶ فایل `.smali` تولید شد، اما **۰ فایل برای `com/getmimo/ui/path/map`** و فقط `ChapterFinishedSynchronizationException.smali` در آن ناحیه پیدا شد.
- **ادعای پوشش کامل Smali نمیشود.** جای خالی آن را Ghidra Auto Analysis (همان ۱۲۲٬۵۴۶ تابع disassembleشده) پر میکند، نه ادعای دیکامپایل Java.
- اسکن خام `0x0300`/`0x0100` که به ۵۵٬۴۷۸ کاندیدای بیمعنا رسید، **پارسر معتبر `code_item` نبود**؛ کنار گذاشته شد و تکرار نشد.
- `DebugMetadata` در ۵۳۹ مورد فقط فیلدهای `c/f/l/m/v` دارد؛ جدولهای `n/i/s` (نام متغیرهای spilled) توسط R8 **حذف شدهاند** و صفر مربوط به `path.map`/`chapterendview` بهدلیل همان شکست Smali است، نہ نبود coroutine.

### الحاق شواهد (جایی که صادقانه شکست خورد)
اسکریپت `MimoControlFlow.java` تلاش کرد xref از رشتههای `string_data` به تابع صاحبش بگیرد: **۰ xref** در خروجی. علت: آنالایزر `Reference` در PSPEC لودر DEX غیرفعال است و `const_string` با ایندکس رشته کار میکند. نتیجه: نام فیلدها معتبرند، ولی **نسبتدادن قطعی هر فیلد به یک کلاس خاص** همچنان نیازمند خواندن `const_string` در بدنه توابع است. این هم ثبت شد، نه پنهان.

---

## ۳. هدف ۱ — `com.getmimo.ui.path.map`: مختصات، فواصل، منحنی، اسکرول و داده v753

### ۳.۱ آنچه قطعی است (از خود APK، بدون حدس رابط)

داده shipped `assets/lessons-en/tracks/tracks.json` با `publishSetVersion: 753`:

- **۱۹ مسیر (track)**، **۱۴۴ section**، **۲٬۰۰۲ ارجاع tutorial**.
- ساختار هر track: `id, version, title, descriptionContent, onboardingCategory, isNew, isHidden, iconBanner, sections[], tutorials[]`.
- هر section: `name, description, startIndex, endIndex, tutorialIds[]`.
- **۰ نقض پیوستگی** در تمام ۱۴۴ section: `startIndex` همیشه `endIndex+1` بخش قبل و آخرین `endIndex = tutorials.length-1` است.
- ارجاع tutorial: فقط `id, version, type, title` — شش نوع: `course` ۱٬۰۰۸، `practiceRequired` ۳۲۱، `practiceOptional` ۲۸۸، `guidedProjectOptional` ۲۱۷، `guidedProject` ۱۱۰، `challenges` ۵۸.
- نمونه واقعی: track ۵۰ «Full-Stack Developer» = **۴۹۲ گره** در **۲۰ section**؛ بزرگترین مسیرها ۴۹۲ / ۳۷۶ / ۲۱۹ / ۲۰۸ / ۱۸۰ گره.

**نتیجه کلیدی:** در اسکن **تمام ۱۰٬۳۵۲ JSON داخلی APK**، هیچ `x/y`، `nodeX`، `bezier`، `spacing` یا `pathOffset` در دادههای مسیر/درس پیدا نشد؛ تنها `x/y`ها مربوط به انیمیشنهای Lottie هستند (`res/raw/onboarding_curriculum.json` یک Lottie ۳۳۲×۶۳۱ و ۲۰۱ فریم است، نه نقشه مسیر). یعنی **مختصات گرهها دادهمحور نیستند؛ در کد Compose محاسبه میشوند** و `tracks.json` فقط ترتیب و نوع و برچسب گرهها را میدهد. ترتیب گره = ایندکس در `tutorials[]`؛ مرز section = `startIndex/endIndex`.

تفاوت مهم با fixture قدیمی `assets/testdata/test-tracks.json` (v52): آنجا ۲۵ مسیر و فیلدهای `difficulty`, `color`, `shortDescriptionContent`, `slug`, `icon` وجود دارد که در v753 **حذف شدهاند**؛ v753 بهجای آن `onboardingCategory` و `sections[].startIndex/endIndex` دارد. هر مدلی که روی v52 بنا شود، ذاتاً با نسخه shipped همخوان نیست.

### ۳.۲ مدل هندسی که از نام فیلدهای `toString()` کاتلین بازیابی شد

R8 نام کلاسها را عوض میکند، ولی رشتههای `toString()` کلاسهای data را نگه میدارد. فیلدهای یافتشده در جدول رشتههای DEX (و `ANALYSIS/MIMO_COMPLETION_ENGINE.json`):

- ایندکس/ساختار: `chapterIndex`, `chapterIndexInSection`, `sectionIndex`, `selectedSectionIndex`, `columnCount`, `columnGutter`, `endIndex`, `activeNodeIds`, `currentNodeId`, `activeModalNodeId`, `childNodes`, `ancestorNodeIds`, `childrenByNodeId`
- فاصله/شعاع/منحنی: `mainAxisSpacing`, `crossAxisArrangementSpacing`, `itemSpacing`, `iconSpacing`, `titleSpacing`, `dotRadius`, `groupOffset`, `sectionHeaderRadius`, `verticalEllipseRadius`, `radiusY`, `snapRadius`, `touchRadius`, `boxRadius`, `cornerRadius`, `borderPath`, `boxPosition`
- اسکرول/آفست: `scrollPosition`, `scrollPositionX`, `instructionsScrollOffset`, `offsetX`, `offsetXPx`, `offsetY`, `offsetYPx`, `panOffset`, `pageSpacing`
- وضعیت/ETA: `forcePathOverviewEtaEnabled`, `currentTrackTitle`, `currentSectionEstimatedCompletionAt`, `trackEstimatedCompletionAt`, `sectionEstimatedCompletionByIndex`

**احتیاط:** برخی از این نامها (مثلاً `childNodes`, `columnGutter`, `mainAxisSpacing`) ممکن است از کتابخانههای همراه (Compose / CodeMirror / Rive) باشند؛ بهدلیل ۰ xref، **نسبت قطعی به `PathMapState` ادعا نمیشود**.

### ۳.۳ واحدهای کد و جریان وضعیت (از `@Metadata` و Ghidra)

- فایلهای منبع بازیابیشده: `PathMapScreen.kt`, `PathMapViewModel.kt`, `Views.kt`, `PathToolbar.kt`, `TutorialSpotlight.kt`, `PracticeOptionalIntro.kt`, `ResubscribeMascotOverlay.kt`, `GetPathMapState.kt`, `GetPathMapDialogs.kt`.
- ۷۵ کلاس Java در بسته `path/map` ثبت شد (`PATH_MAP_SIGNATURES.json`)؛ ۱۲ کلاس R8شده `a..l` و حدود ۵۰ لامبدای `PathMapScreenKt$PathMapScreen$...`.
- interactorها: `GetPathMapState` (شامل `getProBannerState`, `subscriptionAndKeysFlow`, `invoke$1..3`)، `GetPathMapDialogs` (dialog گواهی/دوستان/Streak).
- اکشنهای `PathMapViewModel`: `refreshPathMapState`, `fetchTrackEta`, `navigateToChapter`, `onTutorialClick`, `onNextSectionShown`, `onCertificateClick`, `setHardModeEnabled`, `shouldStartChapterInHardMode`, `refreshDialogs`, `catchGenericError`, `pathOverviewTooltipState`, `practiceOptionalIntroTutorial`, `showResubscribeMascotOverlay`.
- Ghidra اکنون **۶۰ تابع `com::getmimo::ui::path::map::*`** را با دستورالعمل واقعی (`iget_object`, `const_string`, `invoke_static`, `if_eqz`، …) استخراج کرده است؛ ازجمله `PathMapScreenKt$PathMapScreen$10$1$job$1::invokeSuspend` (لامبدایjob مربوط به اسکرول/انیمیشن) که ۳۵ دستورالعمل آن در `CONTROL_FLOW.txt` موجود است.
- `PathMapFragment` کاملاً **Compose** است؛ ۰ لایه XML برای نقشه مسیر.

### ۳.۴ آنچه هنوز نمیدانیم (و نباید جعل کرد)

- اعداد دقیق `dp` فاصله عمودی/افقی، ضریب سینوس/بیضی منحنی، شعاع گره، و فرمول `scrollPositionX` هنوز از ثابتهای `const/high16`/float بدنة توابع R8شده استخراج نشدهاند.
- نگاشت هر فیلد هندسی به کلاس صاحبش (بهخاطر ۰ xref) انجام نشده است.
- **هیچ اجرای runtime، شبیهساز، ADB، لاگ یا اسکرینشات Compose انجام نشده است**؛ بنابراین **ادعای بازسازی پیکسلبهپیکسل گرهها/منحنی/موقعیت اسکرول ممنوع و بیاعتبار است**. این همان «Behavior Verification» است که خودتان شرط کردید و همچنان در صف انتظار است.

---

## ۴. هدف ۲ — `ChapterFinishedViewModel` / Progress / Completion: فرمول نمره، شرط پایان، وضعیت ذخیره، پیوند سرور

### ۴.۱ مدل `LessonProgress` (Ghidra، امضاها و بدنهها)

`com::getmimo::data::model::room::LessonProgress` دارای **۱۱ مؤلفه** (`component1..component11`) و getterهای بازیابیشده:

`getLessonId`, `getTutorialId`, `getTrackId`, `getPublishSetVersion`, `getTutorialVersion`, `getStartedAt`, `getCompletedAt`, `getAttempts`, `getTries`, `getInQueue`, `isPracticeProgress`, `isSolvedCorrectly`.

سازنده آن: `(Lcom/getmimo/ui/lesson/interactive/LessonBundle; Lorg/joda/time/Instant; I I) → LessonProgress` — یعنی **ورودی فرمول نمره: بسته درس + لحظه شروع + دو عدد صحیح** (يکي احتمالاً attempt/try و دیگري شمار پاسخ درست).

`isSolvedCorrectly` در Ghidra واقعاً disassemble شد:
```
iget v1,[v0:0x472e] ; if_lt v1,1 -> return 0 ; else return 1
```
یعنی شرط «حلشده» یک **`>= 1` روی یک فیلد int** است (بهاحتمال `correctLessons`)؛ عدد جادویی XP/Sparks در آن دیده نمیشود.

فیلدهای `toString()` مرتبط: `completedAt`, `correctLessons`, `correctLessonsFirstTry`, `rewardedSparksForCorrectAnswer`, `rewardMultiplier`, `firstTry`, `isFirstTry`. بنابراین **فرمول نمره حداقل شامل «تعداد پاسخ درست»، «درست از بار اول» و «ضریب پاداش» است** — اما ضرایب عددی و وزن هرکدام همچنان ناشناختهاند.

### ۴.۲ صف progress و ذخیره محلی (Room)

`LessonProgressQueue.kt` با متدها: `storeLessonProgress`, `storeAndPostAllLessonProgress`, `updateCorrectAnswersCount`, `getCorrectLessonProgressCount`, `getCorrectLessonsFirstTryCount`, `clearLessonProgressQueue`, `getRewardMultiplier`.

دو جدول Room با SQL کامل در رشتههای DEX:

```
chapter_completions (chapter_id, created_at, track_id, tutorial_id,
                     PRIMARY KEY(chapter_id, track_id))
tutorial_completions(tutorial_id, is_completed, updated_at, track_id,
                     PRIMARY KEY(tutorial_id, track_id))
```
بههمراه `INSERT / UPDATE / SELECT * … WHERE track_id = ? / SELECT COUNT(DISTINCT chapter_id) … / DROP TABLE`.

`CompletionRepository` (محلی): `attachTutorialCompletionToTrack`, `attachTutorialAndChapterCompletionToTrack`, `fetchTrackCompletion`, `fetchLastInteractedTrackId`, `getChapterCompletionCount`, `getRecentlyCompletedTutorialTitles`.

پس **پایان درس = ثبت `LessonProgress` محلی + علامت `is_completed` در `tutorial_completions` + ردیف `chapter_completions` + صف ارسال به سرور**؛ شرط «پایان چپتر/مسیر» از `COUNT(DISTINCT chapter_id)` و `getTrackCompletion` تغذیه میشود. رشته `CreateLessonProgress: completedAt date (` و `createLessonProgressWhenSwiping` نشان میدهد حتی جابهجایی/swipe هم progress میسازد.

### ۴.۳ پیوند سرور (Retrofit، ۵۳ نقطه؛ `MIMO_RETROFIT_ENDPOINTS.json`)

نقاط مرتبط: `POST /v1/tutorials/{tutorialId}/progress`، `GET /v1/tracks/{trackId}/completion`، `GET /v1/tracks/completion/lastInteracted`، `GET /v1/tracks/{trackId}/eta`، `GET /v1/user/rewards/next`، `POST /v1/user/rewards/{rewardId}/confirm`، `GET /v1/user/coins`، `GET /v1/user/activity`، `GET /v1/user/settings`، `GET /v1/leaderboards/latest`، `GET /v1/leaderboards/{leaderboardId}/userrank`.

`PostProgressResponse::getDailyGoalCoinReward` در Ghidra بدنهاش استخراج شد → **پاداش سکّه هدف روزانه از پاسخ سرور میآید**، نه محاسبه محلی. رشته `Confirmed reward with id` و نقطه `/confirm` تأیید میکنند که Reward **server-confirm** است. توضیح «افعال HTTP استنتاجشده از آنوتیشنهای R8شده (`@f`=GET …) هستند، نه مشاهده runtime» همچنان پابرجاست.

### ۴.۴ صفحه پایان چپتر (حالتها و شرطها)

- منابع: `ChapterFinishedFragment.kt`, `ChapterFinishedViewModel.kt`, `ChapterFinishedEtaViewModel.kt`, `ChapterFinishedStreakFragment.kt`, `ChapterFinishedLeaderboardFragment.kt`, `ChapterFinishedFreeStreakGoalFragment.kt`, `ChapterFinishedStreakChallengeFragment.kt`, `ChapterFinishedDailyGoalProgressView.kt`, `GetChapterEndSuccessState.kt`, `GetChapterEndProgressWithEtaScreenData.kt`, `CreateChapterEndScreens.kt`, `CompletionRepository.kt`, `DefaultRewardRepository.kt`, `DefaultStreakRepository.kt`, `DefaultCoinsRepository.kt`, `DefaultLeaderboardRepository.kt`.
- data classها: `ChapterFinishedStats(earnedSparks=`, `BoxAnimationState(earnedCoins=`, `DailyGoal(sparksCount=`, `ChapterFinishedShareData(currentStreak=`, `ChapterCompletion(chapterId=`, `ChapterEndProgressWithEtaScreenData(variant=`.
- فیلدهای وضعیت: `hasReachedDailyGoal`, `todayDailyGoal`, `progressBarDailyGoal`, `dailyGoalCoinReward / dailyGoalCoinsReward / dailyGoalRewardCoins`, `isStreakGoalReached`, `userCurrentStreak / userLongestStreak`, `userCoins`, `sparksCount`, `sparksGoal`, `rewardAmount`, `rewardId`, `rewardMultiplier`, `showRewardBadge`, `hasUserSeenChapterEndScreenToday`, `forceChapterEndProgressEtaEnabled`, `estimatedCompletionAt`, `currentSectionEstimatedCompletionAt`, `trackEstimatedCompletionAt`, `leaderboardChapterEndState`.
- منابع رابطهای `values/string.xml`: `xp`, `xp_earned`, `total_xp`, `streak_drawer_daily_xp = %1$d / %2$d XP`, `sparks_daily_goal`, `sparks_goal_reached_coins = You earned %1$d coins!`, `level_x_multiplier = Level %d multiplier`, `level_practice_multiplier`, `multiplier = x %d`, `accuracy`, `daily_goal_level_1/2/3 = Casual/Regular/Serious`, `chapter_end_progress_eta_quarter/half/three_left_*`, `certificates_*` — یعنی **شرطهای نمایش صفحه پایان بر حسب کسر ¼ / ½ / «۳ درس مانده» و ETA و streak و لیگ است**، نه فقط «درس تمام شد».
- چهار ارز: XP / Sparks / Coins / Keys؛ پنج لیگ Wooden…Golden؛ هدف روزانه Casual/Regular/Serious؛ Reward و لیگ وابسته به تأیید سرور.

### ۴.۵ آنچه هنوز نمیدانیم

ضریب عددی `rewardMultiplier`، مقدار `rewardedSparksForCorrectAnswer`، وزن `correctLessonsFirstTry`، آستانه دقیق نمایش ETA، ترتیب دقیق صفحههای `CreateChapterEndScreens`، و رفتار آفلاین→آنلاین صف همگی نیازمند خواندن ثابتهای عددی بدنهها + **مشاهده runtime/سرور** هستند. هیچکدام ادعا نشدهاند.

---

## ۵. فایلهای تولید/بهروزشده در این مرحله

| فایل | محتوا |
|---|---|
| `ANALYSIS/DEX_INVENTORY.json` | ۱۲ DEX، ۲۸٬۸۳۶٬۰۸۸ بایت، class_def / code_item / refها، ۱۸ نوع map استاندارد |
| `ANALYSIS/_INPUT/classes*.dex` | هر ۱۲ DEX استخراجشده از APK اصلی |
| `ANALYSIS/GHIDRA/DEX_COVERAGE.txt` | اثبات import هر ۱۲ DEX |
| `ANALYSIS/GHIDRA/CONTROL_FLOW.txt` | Auto Analysis هر ۱۲ DEX + ۱۲۲ تابع هدف با دستورالعمل Dalvik + رشتههای هندسی/نمره (xref=۰، صادقانه) |
| `ANALYSIS/GHIDRA/TARGET_FUNCTIONS.json` | همان توابع بهصورت ساختاریافته (run ۳) |
| `ANALYSIS/GHIDRA/REA_DOCTOR.json` | `healthy:true` روی full JDK ۲۱ مجزا + driftها |
| `ANALYSIS/GHIDRA/auto_analysis.log`, `coverage.log`, `run.log`, `README.md` | لاگ کامل چهار اجرای ورکفلو |
| `ANALYSIS/COROUTINE_STATE_MACHINES.json` | ۵۳۹ `DebugMetadata`، ۸۴ فیلد `label/L$/I$/J$`، ۶۵۲ کلاس suspend، `n/i/s` حذفشده |
| `ANALYSIS/KOTLIN_METADATA.json` | ۲۱۲ کلاس با `d2` / `DebugMetadata` بازیابیشده |
| `ANALYSIS/MIMO_COMPLETION_ENGINE.json` | فیلدها، SQL، صف، نقاط API، منابع صفحه پایان |
| `ANALYSIS/PATH_MAP_SIGNATURES.json` | ۷۵ کلاس `path/map` + ۸ فایل منبع کاتلین |
| `ANALYSIS/MIMO_SCORING_STRINGS.json` | رشتههای XP/Sparks/Coins/Goal/Chapter-end از `values/string.xml` |
| `ANALYSIS/_TOOLCHAIN/ghidra_scripts/*.java` | `MimoDexCoverage` و `MimoControlFlow` |
| `.github/workflows/mimo-re-toolchain.yml` | وکفلو موقت: proxy GitHub، JDK ۲۵ Ghidra، Auto Analysis ۱۲ DEX، JDK ۲۱ REA |

ورکفلوها: `41939776550` (همه ۱۲ DEX + Auto Analysis روی `classes.dex` + `rea doctor`)، `41940117221` (رفع `getFunctionCount`)، `41940704898` (Auto Analysis روی **همه ۱۲**)، `41941513296` (xref + توابع هدف `ui::path::map`/نمره) — همگی سبز.

---

## ۶. مرزهایی که رعایت شد

- `mimo-ui/UPGRADE`، `DESIGN/index.html`، ZIP، MANIFEST، `verify_upgrade.py` و ۹ فایل جایگزین v12.5-fa در Drive **دستنخورده** باقی ماندند؛ هیچ ساختار/کد/بیلد جدیدی ایجاد نشد.
- تأیید نهایی v12.5-fa همچنان **انجام نشده**؛ این سند هم **REVIEW است و تأیید نیست**.
- `SAVED` در پروتوتایپ فقط **in-memory** است (در صورت اشاره به پروتوتایپ، این نکته همچنان افشا میشود)؛ هیچ `localStorage`ای وجود ندارد.
- ادعا نشد: دیکامپایل کامل بدنه متدها توسط JADX، پوشش کامل Smali، اینترنت آزاد/VPN پیکربندیشده، سلامت کامل محیط REA، رفتار runtime/سرور، نصب باینری Ghidra بهصورت محلی، درک جزءبهجزء کامل اپ، یا بازسازی پیکسلبهپیکسل گرهها.

---

## ۷. گام بعد (پیشنهاد، بدون اجرا تا دستور شما)

**Behavior Verification**: اجرای APK اصلی روی emulator/ADB، گرفتن لاگ و اسکرینشات از `PathMapScreen` و `ChapterFinishedFragment`، و تطبیق `scrollPositionX`/فواصل/ضرایب نمره با شواهد استاتیک بالا. تا پیش از آن، هر عدد `dp` یا ضریب XP/Sparks فقط حدس است و وارد طراحی نمیشود. JEB نیز فعلاً خرید/اضافه نمیشود؛ اگر روزی مطرح شد، فقط روی چند متد شکستخورده بهصورت آزمایشی و با مقایسه Smali/JADX.
