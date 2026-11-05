**REVIEW — چرخهٔ درس و موتور امتیاز. فرمول عددی تأییدنشده است و عددی اختراع نمیشود.**
منبع: APK اصلی Mimo 9.35 (`sha256=48ce1740…`)، `classes.dex`، Ghidra 12.2 Auto Analysis، رشتههای DEX، `resources.arsc`.
`RUNTIME VERIFIED` = ۰، `SERVER CONFIRMED` = ۰.

---

# LESSON_AND_SCORING_ENGINE — اجرای درس، اتمام، پاداش

## ۱. چرخهٔ کامل (`OBSERVED` = رشته/بدنه، `STATICALLY INFERRED` = ترتیب)

```mermaid
flowchart TD
  A[انتخاب درس<br/>PathMap / ChapterActivity] --> B[LessonBundle<br/>OBSERVED: نام در امضا]
  B --> C[اجرای تمرین/پاسخ<br/>INFERRED]
  C --> D[ارزیابی پاسخ<br/>isSolvedCorrectly @0x509744bc<br/>OBSERVED]
  D --> E[LessonProgress ساخته میشود<br/>@0x50973940, 11 iput<br/>OBSERVED]
  E --> F[INSERT lesson_progress / in_queue=1<br/>OBSERVED]
  F --> G[LessonProgressQueue<br/>storeAndPostAllLessonProgress<br/>OBSERVED: نام]
  G --> H[POST /v1/tutorials/{tutorialId}/progress<br/>OBSERVED: مسیر]
  H --> I[PostProgressResponse<br/>getDailyGoalCoinReward @0x5096c6b8<br/>OBSERVED]
  I --> J[chapter_completions / tutorial_completions<br/>OBSERVED]
  J --> K[ChapterFinished* UI / ETA / Streak / Reward<br/>OBSERVED: نام; ترتیب UNKNOWN]
  K --> L[/v1/user/rewards/next + /confirm<br/>OBSERVED: مسیر]
```

## ۲. مدل `LessonProgress` — `OBSERVED / HIGH` (تطبیق دوتایی)

**منبع الف — رشتهٔ SQL داخل DEX:**
```sql
CREATE TABLE IF NOT EXISTS `lesson_progress` (
  `lesson_id` INTEGER NOT NULL, `completed_at` INTEGER NOT NULL,
  `started_at` INTEGER NOT NULL, `tries` INTEGER NOT NULL,
  `tutorial_id` INTEGER NOT NULL, `tutorial_version` INTEGER,
  `track_id` INTEGER NOT NULL, `publish_set_version` INTEGER,
  `attempts` INTEGER, `is_practice_progress` INTEGER, `in_queue` INTEGER, ...)
```
**منبع ب — Ghidra `classes.dex`:** `Lcom/getmimo/data/model/room/LessonProgress;` دارای
**۱۱ متد `component1..component11`** (`@0x50973b40 … 0x50973e74`) و getterهای:
`getLessonId`, `getCompletedAt`, `getStartedAt`, `getTries`, `getTutorialId`,
`getTutorialVersion`, `getTrackId`, `getPublishSetVersion`, `getAttempts`,
`isPracticeProgress`, `getInQueue`, `isSolvedCorrectly`, `isPracticeProgress`,
`copy`, `copy$default`, `equals`, `hashCode`, `toString`.

| ستون (`OBSERVED`) | getter (`OBSERVED`) | آدرس Ghidra |
|---|---|---|
| `lesson_id` | `getLessonId` | `0x50974184` |
| `completed_at` | `getCompletedAt` | `0x50974100` |
| `started_at` | `getStartedAt` | `0x509741ec` |
| `tries` | `getTries` | `0x5097425c` |
| `tutorial_id` | `getTutorialId` | `0x509742cc` |
| `tutorial_version` | `getTutorialVersion` | `0x50974308` |
| `track_id` | `getTrackId` | `0x5097422c` |
| `publish_set_version` | `getPublishSetVersion` | `0x509741b4` |
| `attempts` | `getAttempts` | `0x509740a8` |
| `is_practice_progress` | `isPracticeProgress` | `0x5097445c` |
| `in_queue` | `getInQueue` | `0x5097413c` |

سازنده (امضای DEX، `OBSERVED`):
`(Lcom/getmimo/ui/lesson/interactive/LessonBundle; Lorg/joda/time/Instant; I I) → LessonProgress`
— یعنی ورودیها «بستهٔ درس + لحظه + دو عدد صحیح»اند؛ **این دو int کدامند `UNKNOWN`** است
(احتمال `tries`/`attempts` فقط `STATICALLY INFERRED`).

بدنهٔ سازنده `@0x50973940` دقیقاً **۱۱ دستور `iput*`** روی فیلدهای `0x4726…0x4730` دارد →
تطبیق ۱۱ ستون / ۱۱ مؤلفه / ۱۱ `iput`، `OBSERVED/HIGH`.

## ۳. شرط «پاسخ درست» — تنها فرمول قابلخواندن (`OBSERVED / HIGH`)

`LessonProgress::isSolvedCorrectly @0x509744bc` (Ghidra disassembly):
```
509744bc  move_object v1,v5
509744be  iget v1,[v1:0x472e]
509744c2  const_4 v3,0x2
509744c4  const_4 v3,0x1
509744c6  move v0,v3
509744c8  if_lt v1,v0,0x509744d0
509744cc  const_4 v4,0x1
509744ce  return v0          ; 1
509744d0  const_4 v3,0x2
509744d2  const_4 v3,0x0
509744d4  move v1,v3
509744d6  return v1          ; 0
```
⇒ **شرط = `یک فیلد int >= 1`** → `true`، در غیر این صورت `false`.
کدام فیلد (offset `0x472e`) دقیقاً مشخص نیست؛ `getAttempts`/`getTries` نامزدند (`STATICALLY INFERRED`).
`const_4`های مضاعف، دستورالعملهای مرده/بازماندهٔ R8 هستند؛ **بهعنوان منطق اضافی تفسیر نشدهاند**.

## ۴. صف progress و پایداری محلی — `OBSERVED`

`LessonProgressQueue.kt` و کلاسهای لامبدای آن:
`storeLessonProgress`, `storeAndPostAllLessonProgress`, `updateCorrectAnswersCount`,
`getCorrectLessonProgressCount`, `getCorrectLessonsFirstTryCount`, `clearLessonProgressQueue`,
`getRewardMultiplier`.

| عبارت SQL (`OBSERVED`) | معنای مستقیم |
|---|---|
| `SELECT * FROM lesson_progress` | خواندن کل صف |
| `SELECT * FROM lesson_progress WHERE in_queue = 1` | رکوردهای در انتظار ارسال |
| `INSERT INTO lesson_progress (...) VALUES (?,?,?,?,?,?,?,?,?,?,?)` | درج رکورد ۱۱ ستونی |
| `DELETE FROM lesson_progress WHERE in_queue = 1` | پاکسازی پس از ارسال (`INFERRED`) |
| `DELETE FROM lesson_progress WHERE lesson_id IN (...)` | حذف گروهی |
| `CREATE TABLE IF NOT EXISTS chapter_completions (chapter_id, created_at, track_id, tutorial_id, PRIMARY KEY(chapter_id, track_id))` | اتمام چپتر |
| `CREATE TABLE IF NOT EXISTS tutorial_completions (tutorial_id, is_completed, updated_at, track_id, PRIMARY KEY(tutorial_id, track_id))` | اتمام tutorial |
| `SELECT COUNT(DISTINCT chapter_id) FROM chapter_completions` | شمارش چپترهای تمامشده |
| `CREATE TABLE room_master_table` / `SELECT identity_hash FROM room_master_table WHERE id = 42` | Room bookkeeping |

`CompletionRepository` (`classes.dex @0x50984214 … 0x50984750`):
`attachTutorialCompletionToTrack`, `attachTutorialAndChapterCompletionToTrack`,
`fetchTrackCompletion` (دو واریانت), `fetchLastInteractedTrackId`, `getChapterCompletionCount`,
`getRecentlyCompletedTutorialTitles`.

پایگاهداده: `mimo.db` (رشتهٔ DEX). همچنین جداول `queue`/`upload_queue`/`user_attributes`
(مربوط به Firebase/measurement) و `WorkSpec`/`WorkProgress` (WorkManager) یافت شدند؛
**آنها جدول MimoProgress نیستند**.

## ۵. پاداش، ارزها و صفحهٔ پایان چپتر

| شاهد | نوع | وضعیت |
|---|---|---|
| `, rewardMultiplier=` / `, rewardedSparksForCorrectAnswer=` | رشتهٔ `toString()` کاتلین | `OBSERVED` (نام) / `UNKNOWN` (مقدار و صاحب کلاس) |
| `, correctLessons=` / `, correctLessonsFirstTry=` | همان | `OBSERVED` (نام) |
| `ChapterFinishedStats(earnedSparks=` / `BoxAnimationState(earnedCoins=` / `DailyGoal(sparksCount=` | پیشوند data class | `OBSERVED` (نام) |
| `ChapterFinishedViewModel.kt`, `GetChapterEndSuccessState.kt`, `CreateChapterEndScreens.kt`, `GetChapterEndProgressWithEtaScreenData.kt`, `ChapterFinishedEtaViewModel.kt`, `ChapterFinishedStreakFragment.kt`, `ChapterFinishedLeaderboardFragment.kt`, `ChapterFinishedFreeStreakGoalFragment.kt`, `ChapterFinishedDailyGoalProgressView.kt` | نام فایل منبع | `OBSERVED` |
| `PostProgressResponse::getDailyGoalCoinReward @0x5096c6b8` | `iget` + `return` | `OBSERVED/HIGH` |
| `POST /v1/user/rewards/{rewardId}/confirm`, `GET /v1/user/rewards/next` | مسیر Retrofit | `OBSERVED` (مسیر) / `INFERRED` (فعل) |
| `Confirmed reward with id` | رشتهٔ DEX | `OBSERVED` |
| `GET /v1/user/coins`, `GET /v1/user/activity`, `GET /v1/leaderboards/latest` | مسیر Retrofit | `OBSERVED` |
| `xp`, `xp_earned`, `total_xp`, `streak_drawer_daily_xp=%1$d / %2$d XP`, `sparks_goal_reached_coins=You earned %1$d coins!`, `level_x_multiplier=Level %d multiplier`, `multiplier=x %d`, `daily_goal_level_1/2/3=Casual/Regular/Serious` | `values/string.xml` / `MIMO_SCORING_STRINGS.json` | `OBSERVED` |
| شرطهای ETA: `chapter_end_progress_eta_quarter_*` (¼)، `half_*` (½)، `three_left_*` («۳ درس مانده») | رشتهها | `OBSERVED` (وجود) / `UNKNOWN` (آستانهٔ عددی و ترتیب) |

## ۶. جدول فرمولها — تفکیک صریح

| فرمول / رفتار | پیادهسازی تأییدشده (`OBSERVED`) | رفتار استنتاجی (`STATICALLY INFERRED`) | حلنشده (`UNKNOWN`) |
|---|---|---|---|
| شرط حل صحیح درس | `isSolvedCorrectly`: `intField >= 1` @`0x509744bc` | فیلد مربوط به `attempts`/`tries` است | هویت دقیق فیلد `0x472e` |
| شمارش تلاشها | ستونهای `tries`, `attempts`؛ `updateCorrectAnswersCount` | شمارش پاسخ درست در صف | ترتیب افزایش و حد饱和 |
| پاداش «درست از بار اول» | `getCorrectLessonsFirstTryCount`, `correctLessonsFirstTry` | امتیاز اضافی برای first‑try | وزن و ضریب |
| `rewardedSparksForCorrectAnswer` | فقط نام فیلد | وجود امتیاز بهازای پاسخ درست | **مقدار عددی** |
| `rewardMultiplier` | فقط نام فیلد + `getRewardMultiplier` + `level_x_multiplier` | ضربکنندهٔ سطح/تمرین | **مقدار، منبع (سرور/محلی)، زمان اعمال** |
| پاداش سکّهٔ هدف روزانه | `PostProgressResponse::getDailyGoalCoinReward` | **سرور مقدار را میدهد** | مقدار، شرط فعالسازی (`SERVER CONFIRMED` = ۰) |
| تأیید Reward | مسیر `/confirm` + رشته `Confirmed reward with id` | Reward نیازمند confirm سرور است | بدنهٔ درخواست/پاسخ، اثر failure |
| آستانهٔ اتمام چپتر | `COUNT(DISTINCT chapter_id)`, `is_completed` | رسیدن به انتهای `tutorialIds` بخش | آستانهٔ دقیق و ترتیب emit |
| ETA | `chapter_end_progress_eta_*`، `/v1/tracks/{trackId}/eta` | نمایش در ¼ / ½ / ۳ درس مانده | فرمول تاریخ، `variant`، شرط نمایش |
| Streak / هدف روزانه | `hasReachedDailyGoal`, `todayDailyGoal`, `progressBarDailyGoal`, `userCurrentStreak`, `userLongestStreak` | بروزرسانی پس از اتمام درس | قواعد شکستن/ترمیم، مقادیر ۳ سطح |
| XP / لیگ | `total_xp`, `GET /v1/leaderboards/latest` | XP هفتگی مبنای لیگ | فرمول XP، قواعد صعود/سقوط |

### تفکیک محلی در برابر سرور
- **محلی (`OBSERVED`)**: `lesson_progress`، `chapter_completions`، `tutorial_completions`، `in_queue`،
  `DataStoreUserPreferences`، assetهای v753.
- **سرور (مسیر `OBSERVED`، مالکیت `INFERRED`)**: `POST …/progress`، `GET …/completion`،
  `GET …/eta`، `GET /v1/user/rewards/next`، `POST …/confirm`، `GET /v1/user/coins`.
- **server‑authoritative (`STATICALLY INFERRED`, اکیداً نه `SERVER CONFIRMED`)**: مقدار
  `dailyGoalCoinReward` در `PostProgressResponse` و تأیید نهایی Reward.
- **ترکیب دقیق فیلد پاسخ → ستون محلی**: `UNKNOWN`.

## ۷. شکافها و ممنوعیتها

- JADX ۱.۵.۶ بدنهٔ ۲٬۱۷۹/۲٬۲۱۱ فایل `com.getmimo` را stub داد؛ بنابراین **فقدان متد Java = فقدان عملکرد نیست** (قید ۷).
  Ghidra بدنهٔ بایتکد ۱۲۲٬۵۴۶ تابع را داد، ولی معادل Java/Kotlin سطحبالا نساخت.
- ۰ xref رشته→تابع → انتساب `rewardMultiplier` به یک کلاس خاص `UNKNOWN`.
- بدون ADB/emulator هیچ مشاهدهٔ اجرایی از امتیاز، انیمیشن `BoxAnimationState`، ترتیب صفحهها یا پاسخ سرور وجود ندارد.
- هیچ ضریب عددی، آستانهٔ درصد یا مقدار XP/Sparks/Coins جعل نشده است.

## ۸. شناسههای شاهد

`EVIDENCE_INDEX.json`: ردیفهای «LessonProgress rewardMultiplier», «rewardedSparksForCorrectAnswer»,
«correctLessonsFirstTry», «Room lesson_progress SELECT», «chapter_completions CREATE TABLE»,
«ChapterFinishedViewModel source file», «PostProgressResponse», «Ghidra disassembled SCORING function»,
«Server-authoritative reward confirmation», «Exact numeric scoring formula … unresolved».
