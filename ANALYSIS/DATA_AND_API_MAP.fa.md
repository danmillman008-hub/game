**REVIEW — گزارش فنی، بدون ادعای تأیید نهایی.** منبع حقیقت: APK اصلی Mimo 9.35
(`sha256 = 48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a`). وضعیتها: `OBSERVED` | `STATICALLY INFERRED` | `RUNTIME VERIFIED` | `SERVER CONFIRMED` | `UNKNOWN`.
هیچ شبیهساز/ADB/لاگ/اسکرینشات/پاسخ سرور در این جلسه وجود ندارد؛ `RUNTIME VERIFIED` و `SERVER CONFIRMED` = **۰**.

# DATA_AND_API_MAP — شبکه، پایگاهداده، مدلها و مالکیت وضعیت

> نوشتهٔ «مالکیت وضعیت» یعنی تعیین اینکه یک مقدار محلی ذخیره میشود، از سرور گرفته میشود، یا سرور مرجع نهایی آن است.
> در غیاب پاسخ سرور، **هیچ موردی `SERVER CONFIRMED` نیست**.

## ۱. مالکیت وضعیت (خلاصه)

| داده | محل | مالک | شاهد | وضعیت |
|---|---|---|---|---|
| پیشرفت درس `lesson_progress` | Room `mimo.db` | محلی + صف ارسال (`in_queue`) | `CREATE TABLE IF NOT EXISTS lesson_progress ...` / `SELECT * FROM lesson_progress WHERE in_queue = 1` | OBSERVED |
| اتمام tutorial/chapter | Room `tutorial_completions` / `chapter_completions` | محلی | دو `CREATE TABLE` + `SELECT COUNT(DISTINCT chapter_id)` | OBSERVED |
| وضعیت «آخرین مسیر تعاملشده» | سرور + کش محلی | نا مشخص | `GET /v1/tracks/completion/lastInteracted` + `CompletionRepository.fetchLastInteractedTrackId` | STATICALLY INFERRED |
| پاداش سکّهٔ هدف روزانه | پاسخ سرور | سرور (استنتاجی) | `PostProgressResponse::getDailyGoalCoinReward` + `POST /v1/user/rewards/{rewardId}/confirm` | STATICALLY INFERRED / نه SERVER CONFIRMED |
| محتوای درس/مسیر | Assets shipped (v753) | داخل APK | `assets/lessons-en/tracks/tracks.json` publishSetVersion=753 | OBSERVED |
| تنظیمات/ترجیحات | DataStore | محلی | `Lcom/getmimo/data/local/DataStoreUserPreferences;` + `libdatastore_shared_counter.so` | OBSERVED |
| پیکربندی کلاینت/فلگها | Remote Config / سرور | سرور (استنتاجی) | `RemoteConfigManager.kt` / `/v2/client-config` | STATICALLY INFERRED |
| نشست/احراز هویت | نا مشخص | نا مشخص | کلاسهای `ui/authentication/*` | UNKNOWN |

## ۲. طرحوارهٔ پایگاهداده (Room / SQLite)

نام پایگاهداده در رشتههای DEX: **google_app_measurement.db, google_app_measurement_local.db, mimo.db**.
تعداد عبارتهای SQL یافتشده: **68** (شامل WorkManager، Firebase و Room).

### ۲٫۱ جداول Mimo

| # | عبارت SQL (OBSERVED) |
|---|---|
| 1 | `CREATE TABLE IF NOT EXISTS `chapter_completions` (`chapter_id` INTEGER NOT NULL, `created_at` INTEGER NOT NULL, `track_id` INTEGER NOT NULL, `tutorial_id` INTEGER NOT NULL, PRIMARY KEY(`chapter_id`, `track_id`))` |
| 2 | `CREATE TABLE IF NOT EXISTS `lesson_progress` (`lesson_id` INTEGER NOT NULL, `completed_at` INTEGER NOT NULL, `started_at` INTEGER NOT NULL, `tries` INTEGER NOT NULL, `tutorial_id` INTEGER NOT NULL, `tutorial_version` IN |
| 3 | `CREATE TABLE IF NOT EXISTS `tutorial_completions` (`tutorial_id` INTEGER NOT NULL, `is_completed` INTEGER NOT NULL, `updated_at` INTEGER NOT NULL, `track_id` INTEGER NOT NULL, PRIMARY KEY(`tutorial_id`, `track_id`))` |
| 4 | `CREATE TABLE IF NOT EXISTS room_master_table (id INTEGER PRIMARY KEY,identity_hash TEXT)` |
| 5 | `DELETE FROM lesson_progress WHERE in_queue = 1` |
| 6 | `DELETE FROM lesson_progress WHERE lesson_id IN (` |
| 7 | `DROP TABLE IF EXISTS `chapter_completions`` |
| 8 | `DROP TABLE IF EXISTS `lesson_progress`` |
| 9 | `DROP TABLE IF EXISTS `tutorial_completions`` |
| 10 | `INSERT INTO `chapter_completions` (`chapter_id`,`created_at`,`track_id`,`tutorial_id`) VALUES (?,?,?,?)` |
| 11 | `INSERT INTO `lesson_progress` (`lesson_id`,`completed_at`,`started_at`,`tries`,`tutorial_id`,`tutorial_version`,`track_id`,`publish_set_version`,`attempts`,`is_practice_progress`,`in_queue`) VALUES (?,?,?,?,?,?,?,?,?,?, |
| 12 | `INSERT INTO `tutorial_completions` (`tutorial_id`,`is_completed`,`updated_at`,`track_id`) VALUES (?,?,?,?)` |
| 13 | `SELECT * FROM chapter_completions WHERE track_id = ?` |
| 14 | `SELECT * FROM chapter_completions WHERE track_id = ? AND tutorial_id in (` |
| 15 | `SELECT * FROM lesson_progress` |
| 16 | `SELECT * FROM lesson_progress WHERE in_queue = 1` |
| 17 | `SELECT * FROM tutorial_completions WHERE track_id = ?` |
| 18 | `SELECT * FROM tutorial_completions WHERE track_id = ? AND tutorial_id in (` |
| 19 | `SELECT 1 FROM sqlite_master WHERE type = 'table' AND name = 'room_master_table'` |
| 20 | `SELECT COUNT(DISTINCT chapter_id) FROM chapter_completions` |
| 21 | `SELECT identity_hash FROM room_master_table WHERE id = 42 LIMIT 1` |
| 22 | `UPDATE `chapter_completions` SET `chapter_id` = ?,`created_at` = ?,`track_id` = ?,`tutorial_id` = ? WHERE `chapter_id` = ? AND `track_id` = ?` |
| 23 | `UPDATE `lesson_progress` SET `lesson_id` = ?,`completed_at` = ?,`started_at` = ?,`tries` = ?,`tutorial_id` = ?,`tutorial_version` = ?,`track_id` = ?,`publish_set_version` = ?,`attempts` = ?,`is_practice_progress` = ?,`i |
| 24 | `UPDATE `tutorial_completions` SET `tutorial_id` = ?,`is_completed` = ?,`updated_at` = ?,`track_id` = ? WHERE `tutorial_id` = ? AND `track_id` = ?` |

### ۲٫۲ طرحوارهٔ `lesson_progress` (تطبیق دقیق)

ستونها از `CREATE TABLE` و `INSERT INTO`: `lesson_id, completed_at, started_at, tries,
tutorial_id, tutorial_version, track_id, publish_set_version, attempts,
is_practice_progress, in_queue` = **۱۱ ستون**. Ghidra دقیقاً **۱۱ متد `component1..component11`**
و getterهای متناظر برای `Lcom/getmimo/data/model/room/LessonProgress;` استخراج کرده است.
این تطبیق `OBSERVED` / `HIGH` است (`CONTROL_FLOW.txt`).

### ۲٫۳ سایر عبارتها (WorkManager / Firebase / migrations)

- `     CREATE TABLE IF NOT EXISTS `WorkProgress` (`work_spec_id` TEXT NOT NULL, `progress`     BLOB NOT NULL, PRIMARY KEY(`work_spec_id`), FOREIGN KEY(`work_spec_id`)     R`
- `ALTER TABLE queue ADD COLUMN has_realtime INTEGER;`
- `ALTER TABLE queue ADD COLUMN retry_count INTEGER;`
- `ALTER TABLE upload_queue ADD COLUMN associated_row_id INTEGER;`
- `ALTER TABLE upload_queue ADD COLUMN last_upload_timestamp INTEGER;`
- `ALTER TABLE user_attributes ADD COLUMN origin TEXT;`
- `CREATE INDEX IF NOT EXISTS `index_WorkSpec_last_enqueue_time` ON `WorkSpec` (`last_enqueue_time`)`
- `CREATE INDEX IF NOT EXISTS `index_WorkSpec_last_enqueue_time` ON`WorkSpec` (`last_enqueue_time`)`
- `CREATE TABLE IF NOT EXISTS `WorkProgress` (`work_spec_id` TEXT NOT NULL, `progress` BLOB NOT NULL, PRIMARY KEY(`work_spec_id`), FOREIGN KEY(`work_spec_id`) REFERENCES `Wo`
- `CREATE TABLE IF NOT EXISTS `WorkSpec` (`id` TEXT NOT NULL, `state` INTEGER NOT NULL, `worker_class_name` TEXT NOT NULL, `input_merger_class_name` TEXT NOT NULL, `input` B`
- `CREATE TABLE IF NOT EXISTS `_new_WorkSpec` (                 `id` TEXT NOT NULL,                 `state` INTEGER NOT NULL,                 `worker_class_name` TEXT NOT NU`
- `CREATE TABLE IF NOT EXISTS `_new_WorkSpec` (`id` TEXT NOT NULL, `state` INTEGER NOT NULL, `worker_class_name` TEXT NOT NULL, `input_merger_class_name` TEXT NOT NULL, `inp`
- `CREATE TABLE IF NOT EXISTS `_new_WorkSpec` (`id` TEXT NOT NULL, `state` INTEGER NOT NULL, `worker_class_name` TEXT NOT NULL, `input_merger_class_name` TEXT NOT NULL, `inp`
- `CREATE TABLE IF NOT EXISTS `_new_WorkSpec` (`id` TEXT NOT NULL, `state` INTEGER NOT NULL, `worker_class_name` TEXT NOT NULL, `input_merger_class_name` TEXT, `input` BLOB `
- `CREATE TABLE IF NOT EXISTS queue ( app_id TEXT NOT NULL, bundle_end_timestamp INTEGER NOT NULL, data BLOB NOT NULL);`
- `CREATE TABLE IF NOT EXISTS upload_queue ( app_id TEXT NOT NULL, upload_uri TEXT NOT NULL, upload_headers TEXT NOT NULL, upload_type INTEGER NOT NULL, measurement_batch BL`
- `CREATE TABLE IF NOT EXISTS user_attributes ( app_id TEXT NOT NULL, name TEXT NOT NULL, set_timestamp INTEGER NOT NULL, value BLOB NOT NULL, PRIMARY KEY (app_id, name)) ;`
- `DELETE FROM WorkProgress`
- `DELETE FROM workspec WHERE state IN (2, 3, 5) AND (last_enqueue_time + minimum_retention_duration) < `
- `DELETE from WorkProgress where work_spec_id=?`
- `DROP TABLE IF EXISTS `WorkProgress``
- `DROP TABLE IF EXISTS room_table_modification_log`

## ۳. نقاط API

دو مجموعهٔ مستقل داریم: **53 تعریف Retrofit حاشیهگذاریشده** (`MIMO_RETROFIT_ENDPOINTS.json`)
و **68 رشتهٔ مسیر `/v...` در جدول رشتههای DEX** (`APK_COMPLETE_INVENTORY.json`).
تفاوت این دو به معنی نقاط اضافیِ تأییدنشده است، نه لیست کامل API.

### ۳٫۱ افعال HTTP — هشدار

اعلانهای Retrofit توسط R8 به کلاسهای کوتاه `@f/@o/@n/@p/@b` تغییر نام یافتهاند.
**هیچ فعل HTTP از روی نام متد استنتاج نشده است** و چنین استنتاجی صریحاً رد میشود.
برچسبهای GET/POST/PUT/DELETE در جدول زیر **فقط حدس `LOW`** از روی الگوی اعلانها هستند؛
هویت واقعی `@f`/`@o`/`@n`/`@p`/`@b` **UNKNOWN** است. تعیین قطعی نیازمند ردیابی
دستورالعملهای `retrofit2.RequestFactory$Builder` در Ghidra **یا** ثبت درخواست/پاسخ در محیط تست مجاز است
(هیچکدام انجام نشده؛ `SERVER CONFIRMED` = ۰).

| فعل استنتاجی | تعداد |
|---|---|
| DELETE | 2 |
| GET | 26 |
| POST | 21 |
| POST/other | 1 |
| PUT | 3 |

### ۳٫۲ فهرست 53 تعریف Retrofit

| # | برچسب حدسی (LOW؛ فعل واقعی UNKNOWN) | مسیر | فایل کلاس | امضا |
|---|---|---|---|---|
| 1 | POST | `/api/sendCustomerIoData` | `hg/b.java` | `Object a(@a CustomerIoData customerIoData, d70.b<? super q> bVar);` |
| 2 | POST | `/click/{linkId}` | `ph/b.java` | `Object a(@s("linkId") String str, d70.b<? super q> bVar);` |
| 3 | POST | `/push/events` | `hg/d.java` | `Object a(@a PushNotificationDelivered pushNotificationDelivered, b<? super q> bVar);` |
| 4 | PUT | `/v1/account/email` | `hg/a.java` | `Object d(@ie0.a ChangeEmailRequestBody changeEmailRequestBody, d70.b<? super o0<q>> bVar);` |
| 5 | GET | `/v1/aiTutor/conversations/messages/count` | `jg/a.java` | `Object a(d70.b<? super AiTutorialConversationMessageCount> bVar);` |
| 6 | GET | `/v1/code` | `mh/c.java` | `Object c(d70.b<? super List<SavedCode>> bVar);` |
| 7 | POST | `/v1/code` | `mh/c.java` | `Object d(@a SaveCodeRequestBody saveCodeRequestBody, d70.b<? super SavedCode> bVar);` |
| 8 | POST | `/v1/code/runfiles` | `hg/c.java` | `Object c(@a CodePlaygroundExecutionBody codePlaygroundExecutionBody, d70.b<? super CodePlaygroundExecutionResponse> bVar);` |
| 9 | PUT | `/v1/code/{savedCodeId}` | `mh/c.java` | `Object a(@s("savedCodeId") long j5, @a SaveCodeRequestBody saveCodeRequestBody, d70.b<? super SavedCode> bVar);` |
| 10 | POST | `/v1/code/{savedCodeId}/remixes` | `mh/c.java` | `Object b(@s("savedCodeId") long j5, @a RemixCodeRequestBody remixCodeRequestBody, d70.b<? super SavedCode> bVar);` |
| 11 | POST | `/v1/code/{savedCodeId}/runfiles` | `hg/c.java` | `Object d(@s("savedCodeId") long j5, @a CodePlaygroundExecutionBody codePlaygroundExecutionBody, d70.b<? super CodePlaygroundExecut` |
| 12 | POST | `/v1/invitations/{code}` | `ug/a.java` | `Object d(@s("code") String str, d70.b<? super q> bVar);` |
| 13 | GET | `/v1/leaderboards/friends` | `ug/a.java` | `Object c(d70.b<? super Friends> bVar);` |
| 14 | GET | `/v1/leaderboards/latest` | `ch/a.java` | `Object a(d70.b<? super o0<Leaderboard>> bVar);` |
| 15 | GET | `/v1/leaderboards/{leaderboardId}/userrank` | `ch/a.java` | `Object b(@s("leaderboardId") long j5, d70.b<? super LeaderboardUserResult> bVar);` |
| 16 | GET | `/v1/package/preview` | `eh/a.java` | `Object a(d70.b<? super o0<ResponseBody>> bVar);` |
| 17 | GET | `/v1/practice/statistics` | `hh/a.java` | `Object a(d70.b<? super PracticeStatsResponse> bVar);` |
| 18 | POST | `/v1/preview/tracks/{trackId}/tutorials/{tutorialId}/chapters/{chapterId}/lessons/{lessonId}/runFiles` | `hg/c.java` | `Object a(@s("trackId") long j5, @s("tutorialId") long j10, @s("chapterId") long j11, @s("lessonId") long j12, @t("publishSetVersio` |
| 19 | GET | `/v1/products/user` | `nh/c.java` | `Object b(d70.b<? super RawProducts> bVar);` |
| 20 | POST | `/v1/products/user` | `nh/c.java` | `Object a(@i("Time-Zone") String str, @a ProductTypeBody productTypeBody, @t("useCoins") boolean z2, d70.b<? super RawPurchasedProd` |
| 21 | GET | `/v1/tracks/completion/lastInteracted` | `com/getmimo/data/source/remote/progress/CompletionApi.java` | `Object getLastInteractedTrack(d70.b<? super LastInteractedTrackResponse> bVar);` |
| 22 | GET | `/v1/tracks/{trackId}/certificates` | `og/a.java` | `Object b(@s("trackId") long j5, @t("fullName") String str, @t("trackVersion") long j10, d70.b<? super o0<ResponseBody>> bVar);` |
| 23 | GET | `/v1/tracks/{trackId}/completion` | `com/getmimo/data/source/remote/progress/CompletionApi.java` | `Object getTrackCompletion(@s("trackId") long j5, @t("trackVersion") long j10, d70.b<? super TrackCompletionResponse> bVar);` |
| 24 | GET | `/v1/tracks/{trackId}/eta` | `com/getmimo/data/source/remote/progress/TrackEtaApi.java` | `Object getTrackEta(@s("trackId") long j5, @t("trackVersion") long j10, d70.b<? super TrackEtaResponse> bVar);` |
| 25 | POST | `/v1/tracks/{trackId}/tutorials/{tutorialId}/chapters/{chapterId}/lessons/{lessonId}/runFiles` | `hg/c.java` | `Object b(@s("trackId") long j5, @s("tutorialId") long j10, @s("chapterId") long j11, @s("lessonId") long j12, @t("publishSetVersio` |
| 26 | POST | `/v1/tracks/{trackId}/tutorials/{tutorialId}/chapters/{chapterId}/lessons/{lessonId}/savefiles` | `dh/a.java` | `Object b(@s("trackId") long j5, @s("tutorialId") long j10, @s("chapterId") long j11, @s("lessonId") long j12, @t("publishSetVersio` |
| 27 | GET | `/v1/tracks/{trackId}/tutorials/{tutorialId}/chapters/{chapterId}/savedFiles` | `dh/a.java` | `Object a(@s("trackId") long j5, @s("tutorialId") long j10, @s("chapterId") long j11, @t("trackVersion") long j12, d70.b<? super Sa` |
| 28 | GET | `/v1/tutorials/drafts/{tutorialId}/chapters/{chapterId}/lessons/{lessonId}/render` | `ng/a.java` | `Object a(@s("tutorialId") long j5, @s("chapterId") long j10, @s("lessonId") long j11, d70.b<? super LessonDraftResponse> bVar);` |
| 29 | POST | `/v1/tutorials/{tutorialId}/lessons/{lessonIdentityId}/report` | `kh/a.java` | `Object a(@s("tutorialId") long j5, @s("lessonIdentityId") long j10, @ie0.a ReportLessonBody reportLessonBody, d70.b<? super q> bVa` |
| 30 | POST | `/v1/tutorials/{tutorialId}/progress` | `com/getmimo/data/source/remote/progress/LessonProgressApi.java` | `Object postProgress(@s("tutorialId") long j5, @a PostProgressRequestBody postProgressRequestBody, d70.b<? super PostProgressRespon` |
| 31 | GET | `/v1/user/activity` | `sh/h.java` | `Object a(@t("from") String str, @t("to") String str2, d70.b<? super UserActivityResponse> bVar);` |
| 32 | GET | `/v1/user/coins` | `qg/a.java` | `Object a(d70.b<? super Coins> bVar);` |
| 33 | POST | `/v1/user/deviceTokens` | `hg/a.java` | `Object c(@ie0.a DeviceToken deviceToken, d70.b<? super q> bVar);` |
| 34 | GET | `/v1/user/events/subscribe` | `hg/a.java` | `Object b(d70.b<? super PusherChannelResponse> bVar);` |
| 35 | GET | `/v1/user/favorites/tracks` | `xe/a.java` | `Object a(d70.b<? super FavoriteTracks> bVar);` |
| 36 | POST | `/v1/user/favorites/tracks/{trackId}` | `xe/a.java` | `Object b(@s("trackId") long j5, d70.b<? super FavoriteTracks> bVar);` |
| 37 | DELETE | `/v1/user/following/{userId}` | `ih/a.java` | `Object f(@s("userId") long j5, d70.b<? super o0<q>> bVar);` |
| 38 | POST/other | `/v1/user/following/{userId}` | `ih/a.java` | `Object a(@s("userId") long j5, d70.b<? super o0<q>> bVar);` |
| 39 | GET | `/v1/user/invitations` | `ug/a.java` | `Object a(d70.b<? super InvitationsOverview> bVar);` |
| 40 | GET | `/v1/user/keys` | `bh/a.java` | `Object b(@i("Time-Zone") String str, d70.b<? super UserKeys> bVar);` |
| 41 | POST | `/v1/user/keys/consume` | `bh/a.java` | `Object a(d70.b<? super UserKeys> bVar);` |
| 42 | GET | `/v1/user/rewards/next` | `lh/a.java` | `Object b(d70.b<? super Rewards> bVar);` |
| 43 | POST | `/v1/user/rewards/{rewardId}/confirm` | `lh/a.java` | `Object a(@s("rewardId") long j5, d70.b<? super q> bVar);` |
| 44 | GET | `/v1/user/settings` | `kf/a.java` | `Object c(d70.b<? super Settings> bVar);` |
| 45 | PUT | `/v1/user/settings` | `kf/a.java` | `Object a(@ie0.a Settings settings, d70.b<? super Settings> bVar);` |
| 46 | POST | `/v1/user/settings/avatar` | `kf/a.java` | `Object e(d70.b<? super AvatarUpdateResponse> bVar);` |
| 47 | DELETE | `/v1/user/settings/avatar/{uploadId}` | `kf/a.java` | `Object d(@s("uploadId") String str, @ie0.a ConfirmAvatarUploadBody confirmAvatarUploadBody, d70.b<? super q> bVar);` |
| 48 | POST | `/v1/user/visits` | `hg/a.java` | `Object a(@ie0.a AppName appName, d70.b<? super q> bVar);` |
| 49 | GET | `/v1/users/{userId}/code` | `ih/a.java` | `Object b(@s("userId") long j5, d70.b<? super PublicUserCode> bVar);` |
| 50 | GET | `/v1/users/{userId}/code/{savedCodeId}` | `ih/a.java` | `Object c(@s("userId") long j5, @s("savedCodeId") long j10, d70.b<? super SavedCode> bVar);` |
| 51 | GET | `/v1/users/{userId}/profile` | `ih/a.java` | `Object d(@s("userId") long j5, d70.b<? super PublicUser> bVar);` |
| 52 | POST | `/v1/users/{userId}/report` | `ih/a.java` | `Object e(@s("userId") long j5, d70.b<? super o0<q>> bVar);` |
| 53 | GET | `/v2/client-config` | `lg/a.java` | `Object a(d70.b<? super d> bVar);` |

### ۳٫۳ مدل درخواست/پاسخ، Repository فراخوان، تغییروضعیت

| مؤلفه | یافته | وضعیت |
|---|---|---|
| مدل درخواست/پاسخ | امضاها در جدول بالا؛ بدنهٔ مدلها عمدتاً JADX-stub یا R8شده | OBSERVED (امضا) / UNKNOWN (فیلدهای کامل) |
| Repository فراخوان | `DefaultRewardRepository`, `DefaultCoinsRepository`, `DefaultStreakRepository`, `DefaultLeaderboardRepository`, `CompletionRepository`, `LessonProgressRepository`, `SettingsRepository` | OBSERVED (نام کلاس) |
| ViewModel/UseCase فراخوان | `GetChapterEndSuccessState`, `GetPathMapState`, `GetChapterEndProgressWithEtaScreenData`, `CreateChapterEndScreens` | OBSERVED (نام) / STATICALLY INFERRED (نقش) |
| تغییروضعیت پس از پاسخ موفق | `INSERT/UPDATE lesson_progress`, `DELETE ... WHERE in_queue = 1`, `Confirmed reward with id` | OBSERVED (عبارت/رشته) / UNKNOWN (ترتیب اجرا) |
| ارتباط موجودیت محلی با پاسخ | همبستگی مستقیم ستون→فیلد پاسخ برقرار نشده | UNKNOWN |

## ۴. سایر ذخیرهسازیها و منابع

| منبع | مقدار | وضعیت |
|---|---|---|
| resources.arsc | 1 پکیج، 94401 ورودی در ۱۱۷ پیکربندی محلی | OBSERVED |
| انواع منبع پیشفرض | public=14023, bool=15, color=1455, dimen=1631, id=2233, integer=84, string=1721 | OBSERVED |
| Assets | 10564 فایل / 10317 JSON / بستههای محلی ['common', 'de', 'en', 'es', 'fr', 'id', 'it', 'pl', 'pt', 'ru', 'tr'] | OBSERVED |
| بومی | 12 کتابخانه .so | OBSERVED |
| DataStore/SharedPreferences | `DataStoreUserPreferences`، migrationـهای RevenueCat | OBSERVED (رشتهها) / UNKNOWN (فهرست کامل کلیدها) |

## شناسههای شاهد

- EV-0193, EV-0194, EV-0195, EV-0196, EV-0197, EV-0198
- EV-0233, EV-0234, EV-0235, EV-0236, EV-0237, EV-0238
- EV-0040
- EV-0173


---

## الحاق MISSION 02 — تصحیح و اتصال (بدون بازنویسی متن بالا)

> محتوای بالا **حفظ شد**؛ یافتههای جدید فقط به آن متصل میشوند.

- **افعال HTTP دیگر `LOW`/استنتاج از نام متد نیستند.** با دیکود `classes3.dex`
  `Lge0/r0;->a @0xabb18` (Retrofit `RequestFactory$Builder` R8شده) نگاشت
  `Lie0/f;→GET`, `Lie0/o;→POST`, `Lie0/n;→PATCH`, `Lie0/p;→PUT`,
  `Lie0/b;→DELETE`, `Lie0/m;→OPTIONS`, `Lie0/g;→HEAD` **از بایتکد** استخراج شد
  و ورودیهای `ie0.*` در ۵۳ فایل JADX تأیید شد (`HTTP_VERBS_RESOLVED.json`).
  **۶ برچسب قدیمی تصحیح شد**: `@n` در واقع `PATCH` (۳ نقطه)، `@p` در واقع `PUT` (۲)،
  `@b` در واقع `DELETE` (۱). شمارش صحیح: GET ۲۶ · POST ۲۱ · PATCH ۳ · PUT ۲ · DELETE ۱.
  همچنان **`SERVER CONFIRMED` = ۰** (هیچ پاسخی ثبت نشد).
- **گراف ارتباطات به سطح متد ارتقا یافت**: ۶٬۰۱۶ جفتفراخوانی درون `com/getmimo`
  با `DEX` + `insn_offset` + امضای کامل (`COMPLETE_COMPONENT_GRAPH.json`).
  لبههای `ui→viewmodel→usecase→repository` اکنون علاوه بر ارجاع نوعی، **دستورالعمل `invoke`** دارند؛
  با این حال الگو سراسری نیست.
- **زنجیرهٔ درس اثبات شد**: `isSolvedCorrectly @0xa56474` → `storeLessonProgress @0xa563da` →
  `addOrUpdateLessonProgressInQueue @0x997ddc` → `postProgress @0x998976` →
  `toLessonProgressSyncResult @0x998992` → صفحهٔ پایان چپتر `@0x9a282a` →
  `GetPathMapState$invoke$3` `@0x9a9240…0x9a9444`. جزئیات در `COMPLETE_APPLICATION_FLOW.fa.md`.
- **وضعیت runtime تغییر نکرد**: ممیزی MISSION 02 نشان داد emulator/ADB/KVM/SDK/حساب مجاز
  وجود ندارد؛ ۰/۹ آزمایش اجرا شد. ضمیمه در `RUNTIME_VERIFICATION.fa.md`.
- شکافها و پوشش بهروزشده: `FINAL_KNOWN_GAPS.fa.md`؛ شاهدها: `EV-M02-0001…0027` در `EVIDENCE_INDEX.json`.
