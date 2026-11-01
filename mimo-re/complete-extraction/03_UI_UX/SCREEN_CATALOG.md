# ۰۳ — کاتالوگ صفحه‌ها (Screen catalog)

**دامنه:** ۱۹۲ سطح رابط (۳۶ activity برنامه + ۲۲ fragment + ۲۲ modal + ۸۷ bottom sheet + بقیه third-party)
در `SCREEN_INVENTORY.csv` / `.json`. ماتریس حالت در `SCREEN_STATE_MATRIX.csv`.
**کلاس شواهد:** نام/ساختار `VERIFIED_STATIC`؛ حالت‌ها `PARTIALLY_VERIFIED` (شاهد = رشتهٔ منبع)؛
`NOT_TESTED` برای هر چیزی که نیاز به اجرا دارد.

## ۱. گروه‌بندی سفر کاربر

| # | سطح | هدف | ورود | خروج | حالت‌ها | شواهد |
|---|---|---|---|---|---|---|
| 1 | `SplashActivity` (+alias) | مسیریابی deep link، بوت جلسه | launcher، ۴ لینک | Main / Onboarding / Auth | boot, deep-link | manifest |
| 2 | `AuthenticationActivity` | ورود/ثبت‌نام | دکمه‌های CTA | Main | idle, submitting, error_* | رشته‌های `authentication_error_*` |
| 3 | `OnboardingActivity` + ۱۲ fragment | ساخت برنامهٔ یادگیری | پس از ثبت‌نام | Main | per-step، loading، offline | `nav_onboarding_graph.xml`, ۱۵۷ رشتهٔ `onboarding_*` |
| 4 | `MainActivity` | خانهٔ مسیرها | بوت | chapter/store/profile | loaded, loading, empty, offline, error | `NavigationBar` + رشته‌ها |
| 5 | `ChapterActivity` | اجرای درس‌ها | انتخاب فصل | chapter_end | in_progress, finished, offline | `chapter_end_*` (۵۲ رشته) |
| 6 | بازیکن تعاملی | خواندن+سنجش | از فصل | بازخورد/درس بعد | unanswered, wrong, correct, hint, solution | DSL + ۱۳,۰۴۳ بلوک `visible-if="wrong"` |
| 7 | بازیکن کد | ویرایش+اجرا | از فصل | تست‌ها | editing, running, passed, failed, compiler_error, offline | `executable_lesson_*` |
| 8 | پایان فصل | جشن+جایزه+ETA | اتمام | مسیر/فروشگاه | reward, streak_challenge, certificate | `reward_*`, `streak_challenge_*` |
| 9 | تمرین هوشمند | مرور هدفمند | تب تمرین | فصل بازخدمت‌شده | results, filtered_empty, offline | `practice_*` (۳۶ رشته) |
| 10 | مربی هوشمند (sheet) | کمک فوری | دکمه در درس | بستن/ارتقا | loading, streaming, quota, offline, disabled | `AiTutorViewModel$State` |
| 11 | فروشگاه/پی‌وال | خرید | CTA در مسیر/درس | خرید | plans, trial, discount, pending, offline | ۳۹+۳۹ رشته |
| 12 | پروفایل/گواهی/تنظیمات | هویت و دستاورد | تب | — | locked (مهمان), empty, offline | `profile_*`, `certificate*`, `settings_*` |
| 13 | ویجت زنجیره | حلقهٔ روزانه | launcher ویجت | بازگشت به درس | active, no_streak, inactive | `widget_*` |
| 14 | Developer Menu (۵۵ کلاس) | ابزار داخلی | فقط داخلی | — | — | `ui.developermenu.*` |

## ۲. ساختار صفحه — نمونهٔ کامل (الگوی قابل تکرار برای بقیه)

### `ChapterActivity` (بازیکن درس)
```
ChapterActivity
└── AppBar: [back] [progress "n/m"] [streak chip] [AI tutor]
    └── ContentPager (Fragment per lesson)
        ├── InteractiveLessonFragment
        │    ├── ScrollView: modules rendered in document order
        │    │    ├── Paragraph (visible-if)
        │    │    ├── CodeBlock (tabs per file, editable gaps, chip tray)
        │    │    ├── Selection (multi-select items)
        │    │    ├── WebView block (sandboxed HTML preview)
        │    │    └── Database block (result grid)
        │    └── BottomBar: [hint] [check] (state-dependent)
        └── ExecutableLessonFragment
             ├── Tabs: Instructions | Editor | Console | Tests
             ├── CodingKeyboard (Compose, 64dp height)
             └── BottomBar: [run] [see solution] [ask AI tutor]
Modal layer: RewardSheet → StreakChallengeSheet → UpgradeDrawer → NotificationPrompt
```
منابع اعداد: `04_DESIGN_SYSTEM.md` و `05_LESSON_DSL/`.

## ۳. حالت‌ها — اندازه‌گیری و پوشش

| ناحیه | حالت‌های شناسایی‌شده | شاهد |
|---|---|---|
| آفلاین | ۱۲ سطح (خانه، فصل، تمرین، فروشگاه، لیدربورد، پروفایل، مربی، گزارش درس، …) | ۱۴ رشتهٔ `*_offline_*` |
| خالی | playground، کد ذخیره‌شده، دوستان، فیلتر تمرین، کنسول | `empty`, `state_empty`, `playgrounds_empty_*`, `saved_code_empty_state_*` |
| خطا | سراسری + دامنه‌ای | `generic_error_retry` + ۷۱ رشتهٔ `*error*` |
| بارگذاری | آنبوردینگ برنامه، پایان فصل، کنسول، چت مربی | `onboarding_curriculum_loading`, `chapter_finished_loading`, `code_header_console_loading` |
| پی‌وال | مسیر، فصل، تمرین، مربی، گواهی، آیکون برنامه | `*_upgrade_*`, `keys_*` |

**پوشش:** ۲۴ جفت (سطح، حالت) به‌صورت شاهد مستقیم مستند شد؛ باقی حالت‌ها
`NOT_TESTED` هستند چون نیازمند اجرا هستند.

## ۴. آنچه نمی‌دانیم

* برچسب تب‌های نوار پایین (فقط آیکون هستند یا از سرور می‌آیند) — **UNKNOWN**.
* ترتیب دقیق گام‌های آنبوردینگ — **INFERRED** از نام fragment + رشته‌ها + گراف ناوبری.
* کدام صفحه View است و کدام Compose، در سطح هر صفحه — **PARTIALLY_VERIFIED**.
