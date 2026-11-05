**REVIEW — MISSION 02.** این سند زنجیرهٔ واقعی درس/امتیاز را تا سطح **دستورالعمل DEX** اثبات میکند.
هیچ فرمول عددی کشف نشده و هیچ فرمولی حدس زده نمیشود.
`RUNTIME VERIFIED` = ۰ · `SERVER CONFIRMED` = ۰ · منبع `classes.dex` (و `classes3.dex` برای فعل HTTP).

---

# LESSON_SCORING_VERIFICATION — منطق درس و امتیازدهی

## ۱. زنجیرهٔ اثباتشده (همه `OBSERVED/HIGH`، آفستها در `classes.dex`)

| # | پرسش مادهٔ ۴ | پاسخ مستند | شاهد |
|---|---|---|---|
| ۱ | پاسخ کجا بررسی میشود؟ | `ExecutableLessonViewModel$doOnLessonCorrectlySolved$2::invokeSuspend` → `LessonProgress::isSolvedCorrectly()` | `0xa56474` |
| ۱ب | شرط درست چیست؟ | `iget [0x472e]` + `if_lt v1,1` ⇒ **یک فیلد `int >= 1`** | Ghidra `0x509744bc` |
| ۲ | تلاشها چگونه تغییر میکند؟ | `LessonProgressQueue::storeLessonProgress` → `updateCorrectAnswersCount` (`0x997e08`)، `LessonProgress::getAttempts()` (`0x997e22`)، `updateLessonStreakDetector` (`0x997e32`) | `0xa563da`, `0x997ddc` |
| ۲ب | شمارش پاسخ درست | `getCorrectLessonProgressCount` → `isSolvedCorrectly` @`0x997900`؛ `getCorrectLessonsFirstTryCount` → `isSolvedCorrectly` @`0x997ac8` | `OBSERVED` |
| ۳ | وضعیت صحیح چگونه ذخیره میشود؟ | `storeLessonProgress` → `LessonProgressRepository::addOrUpdateLessonProgressInQueue` | `0x997ddc` |
| ۳ب | طرحواره | `lesson_progress(lesson_id, completed_at, started_at, tries, tutorial_id, tutorial_version, track_id, publish_set_version, attempts, is_practice_progress, in_queue)` — ۱۱ ستون ↔ ۱۱ `componentN` ↔ ۱۱ `iput` @`0x50973940` | `OBSERVED` |
| ۴ | محلی ↔ سرور | `postUnsyncedLessonProgress$2`: DAO @`0x99881a` → `getTutorialId` @`0x998880` → `toProgressList` @`0x998924` → `LessonProgressApi::postProgress` @`0x998976` → `toLessonProgressSyncResult` @`0x998992` → DAO @`0x998a08` | `OBSERVED` |
| ۴ب | فعل HTTP | **`POST`** `/v1/tutorials/{tutorialId}/progress` — حلشده از `classes3.dex Lge0/r0;->a` (`Lie0/o;` → `const-string 'POST'` @`0xabbf0`)، **نه از نام متد** | `OBSERVED` / نه `SERVER CONFIRMED` |
| ۴ج | SQL | `SELECT * FROM lesson_progress WHERE in_queue = 1` · `INSERT INTO lesson_progress (...) VALUES (?,?,?,?,?,?,?,?,?,?,?)` · `DELETE FROM lesson_progress WHERE in_queue = 1` | `OBSERVED` |
| ۵ | چه چیزی از سرور برمیگردد؟ | `PostProgressResponse`، خواندهشده توسط `toLessonProgressSyncResult`: `getReachedGoal()` @`0x998cf4` و `getDailyGoalCoinReward()` @`0x998cfe` | `OBSERVED` (کد) / `UNKNOWN` (مقادیر) |
| ۶ | پاداش چگونه نمایش داده میشود؟ | `GetChapterEndSuccessState$storeAndPostAllLessonProgress$lessonProgressSyncResult$1::invokeSuspend` → interactor چپتر @`0x9a282a` و `storeAndPostAllLessonProgress` @`0x9a284a`؛ `DefaultRewardRepository$sendConfirmationRequestToBackend$2` @`0x99b564`؛ `MainViewModel$confirmRewardAndLookForNewRewards$1` @`0xa8ddc8`؛ `POST /v1/user/rewards/{rewardId}/confirm` | `OBSERVED` (فراخوانی) / `INFERRED` (ترتیب UI) |
| ۷ |وضعیت گره بعدی | `GetPathMapState$invoke$3` → `isCompleted()` @`0x9a940c`, `isRequired()` @`0x9a93e6`, `getType()` @`0x9a92f4` | `OBSERVED` (خواندن) |
| ۷ب | قاعدهٔ باز شدن گره بعدی | **بازسازی نشد** | **`UNKNOWN`** |

## ۲. آنچه «کشف فرمول» محسوب نمیشود

| فقط یافتهایم | وضعیت |
|---|---|
| نام فیلد `rewardMultiplier`, `rewardedSparksForCorrectAnswer`, `correctLessons`, `correctLessonsFirstTry` | `OBSERVED` (رشتهٔ `toString`) — **فرمول نیست** |
| getter `Reward::getRewardMultiplier()`، فراخوانیشده در `ui/main/d;->G(Reward;)Z` @`0xa92e04` | `OBSERVED` (فراخوانی) — **مقدار/ضریب نیست** |
| `getDailyGoalCoinReward()` | `OBSERVED` (getter) — **مقدار سکّه مشاهده نشد** |
| `getReachedGoal()` | `OBSERVED` (getter) — **شرط آستانه مشخص نشد** |
| `SELECT COUNT(DISTINCT chapter_id) FROM chapter_completions` | `OBSERVED` (SQL) — **آستانهٔ اتمام چپتر نیست** |
| `ChapterFinishedStats(earnedSparks=`, `BoxAnimationState(earnedCoins=`, `DailyGoal(sparksCount=` | `OBSERVED` (نام data class) — **عدد نیست** |
| `sparks_goal_reached_coins=You earned %1$d coins!`, `level_x_multiplier=Level %d multiplier` | `OBSERVED` (رشتهٔ منبع) — **فرمول نیست** |

### جدول فرمولها (بدون حدس)

| فرمول | پیادهسازی تأییدشده | حلنشده |
|---|---|---|
| شرط پاسخ صحیح | `intField >= 1` @`0x509744bc` | هویت دقیق فیلد `0x472e` (`attempts` یا `tries`؟ `INFERRED`) |
| افزایش تلاش | ستونهای `tries`/`attempts` + `updateCorrectAnswersCount` | ترتیب، سقف، شرایط first-try |
| `rewardMultiplier` | فقط getter | **مقدار، منبع، زمان اعمال** |
| `rewardedSparksForCorrectAnswer` | فقط نام | **مقدار** |
| آستانهٔ اتمام چپتر | `chapter_completions`, `COUNT(DISTINCT chapter_id)` | **شرط دقیق** |
| ETA | `chapter_end_progress_eta_*` و `GET /v1/tracks/{trackId}/eta` (فعل `GET` حلشده) | فرمول و variantها |
| Streak / هدف روزانه | `hasReachedDailyGoal`, `todayDailyGoal` | قواعد شکستن/ترمیم و ۳ سطح |
| XP / لیگ | `total_xp`, `GET /v1/leaderboards/latest` | فرمول XP و صعود/سقوط |

## ۳. تفکیک مالکیت

- **محلی (`OBSERVED`)**: `lesson_progress`، `chapter_completions`، `tutorial_completions`، پرچم `in_queue`، `DataStoreUserPreferences`.
- **کلاینت → سرور (`OBSERVED` مسیر / فعل، `INFERRED` اجرا)**: `POST /v1/tutorials/{tutorialId}/progress`، `POST /v1/user/rewards/{rewardId}/confirm`.
- **server-authoritative (`STATICALLY INFERRED`)**: `getReachedGoal`, `getDailyGoalCoinReward` در `PostProgressResponse`.
  **`SERVER CONFIRMED` = ۰** — هیچ پاسخ HTTP ثبت نشد.
- **همگامسازی**: `SELECT … WHERE in_queue = 1` → `postProgress` → `DELETE … WHERE in_queue = 1`
  بهصورت **عبارت/فراخوانی جداگانه** مشاهده شد؛ ترتیب اجرا، retry و رفتار آفلاین `UNKNOWN`.

## ۴. تصحیح مهم نسبت به مرحلهٔ ۱

مرحلهٔ ۱ افعال HTTP را «`LOW` / استنتاجی» و فاقد قطعیت اعلام کرده بود.
در این مرحله، با دیکود `Lge0/r0;->a` در `classes3.dex` نگاشت
`Lie0/f;→GET`, `Lie0/o;→POST`, `Lie0/n;→PATCH`, `Lie0/p;→PUT`, `Lie0/b;→DELETE`,
`Lie0/m;→OPTIONS`, `Lie0/g;→HEAD` **از بایتکد** بهدست آمد و
**۶ برچسب قبلی تصحیح شد** (مثلاً `PUT /v1/account/email` در واقع `PATCH` است،
`DELETE /v1/user/settings/avatar/{uploadId}` در واقع `PUT` است).
همهٔ ۵۳ نقطه اکنون `OBSERVED/HIGH` بهعنوان **فعل سمت کلاینت**اند؛
ولی همچنان **`SERVER CONFIRMED` نیستند**. جزئیات: `HTTP_VERBS_RESOLVED.json`.

## ۵. شکاف «مشاهدهٔ واقعی»

بدون emulator/ADB: پاسخ واقعی کاربر، تعداد تلاشها در عمل، مقادیر پاداش،
بدنهٔ درخواست/پاسخ، ترتیب صفحههای پایان چپتر، و قاعدهٔ unlock گره بعدی
**هیچکدام مشاهده نشدند**. ممیزی دقیق مانع در `RUNTIME_VERIFICATION.fa.md`، ضمیمهٔ MISSION 02.
شاهدها: `EV-M02-0008`, `EV-M02-0009`, `EV-M02-0010..0013`, `EV-M02-0017`.
EOF