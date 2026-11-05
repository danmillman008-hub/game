**REVIEW — وضعیت تأیید رفتار. در این جلسه هیچ رفتاری `RUNTIME VERIFIED` یا `SERVER CONFIRMED` نشده است.**
دستور مادهٔ ۸ صریح است: «When an approved emulator and ADB environment are available …».
چنین محیط تأییدشدهٔ شبیهساز/ADB و محیط تست مجاز شبکهای در اختیار نبود؛ بنابراین مادهٔ ۸ به
**مستندسازی دقیق شواهد غایب** محدود شد، نه شبیهسازی مشاهده.

---

# RUNTIME_VERIFICATION — مشاهدهشده در برابر تأییدنشده

## ۱. وضعیت محیط

| پیشنیاز | وضعیت | شاهد |
|---|---|---|
| APK اصلی (تغییرنیافته) | ✅ موجود | `sha256=48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a`، ۱۴۲٬۳۵۳٬۴۹۹ بایت |
| شبیهساز/Android SDK/emulator تأییدشده | ❌ غایب | هیچ `adb`, `emulator`, `aapt2`, `apksigner` در محیط تحلیل نصب/استفاده نشد |
| ADB / دستگاه | ❌ غایب | ۰ جلسه، ۰ `adb shell` |
| محیط تست شبکهای مجاز | ❌ غایب | ۰ درخواست/پاسخ ثبتشده |
| Ghidra / REA / JADX / Smali | ✅ استاتیک | چهار اجرای سبز workflow؛ ولی **هیچکدام اجراکنندهٔ اپ نیستند** |
| تغییر APK/DEX/منابع/شواهد | ❌ انجام نشد | تمام پارسرها read-only؛ `ANALYSIS/_INPUT/` بایتبهبایت با APK یکسان است |

## ۲. جدول رفتارهای درخواستی

| # | رفتار (مادهٔ ۸) | خروجی خواستهشده | وضعیت | شاهد تولیدشده |
|---|---|---|---|---|
| ۱ | راهاندازی اپ | screenshot + logcat | `UNKNOWN / تأییدنشده` | none |
| ۲ | ناوبری بین صفحات | screenshot + UI hierarchy + transition | `UNKNOWN / تأییدنشده` | none |
| ۳ | اسکرول مسیر یادگیری | screenshot + لاگ اسکرول | `UNKNOWN / تأییدنشده` | none |
| ۴ | انتخاب گره | UI hierarchy + screenshot | `UNKNOWN / تأییدنشده` | none |
| ۵ | پیشروی در درس | screenshot + logcat | `UNKNOWN / تأییدنشده` | none |
| ۶ | اتمام چپتر | screenshot + transition | `UNKNOWN / تأییدنشده` | none |
| ۷ | نمایش پاداش و پیشرفت | screenshot + مقادیر مشاهدهشده | `UNKNOWN / تأییدنشده` | none |
| ۸ | رفتار شبکه (فقط محیط تست مجاز) | request/response | `UNKNOWN / تأییدنشده` | none |

شمارش دقیق: **۰ اسکرینشات · ۰ ADB UI hierarchy · ۰ logcat · ۰ transition ضبطشده ·
۰ state change مشاهدهشده · ۰ network capture**.
هیچ استنتاج استاتیکی بهعنوان مشاهدهٔ اجرا برچسب نخورده است.

## ۳. شواهد غایب، موردبهمورد (Explicit missing evidence)

| آنچه نیاز است | آنچه فعلاً داریم | آنچه کم است |
|---|---|---|
| مختصات واقعی گرهها (X/Y) | نام فیلدها: `offsetX`, `offsetXPx`, `columnCount`, `dotRadius` | مقادیر `dp`/px، تابع تبدیل، `density`، جهت |
| فاصلهٔ عمودی/افقی گرهها | `mainAxisSpacing`, `crossAxisArrangementSpacing`, `itemSpacing` | مقادیر عددی و اینکه کدامیک اعمال میشود |
| منحنی مسیر | `verticalEllipseRadius`, `radiusY`, `borderPath`, `libandroidx.graphics.path.so` | تابع منحنی، control pointها، رسم واقعی |
| موقعیت اسکرول / بازیابی آن | `scrollPosition`, `scrollPositionX`, `instructionsScrollOffset`, `PathMapScreenKt$...$job$1::invokeSuspend @0x50aa64b8` | مقدار اولیه، `rememberSaveable`، رفتار پس از چرخش/بازگشت |
| وضعیت بصری گرهها | ۶ نوع `type` در v753 | نگاشت type → رنگ/آیکون/قفل/انیمیشن |
| فرمول امتیاز | `isSolvedCorrectly: intField >= 1` @`0x509744bc`؛ `rewardMultiplier`, `rewardedSparksForCorrectAnswer` | ضرایب، وزن first‑try، XP/Sparks/Coins واقعی |
| شرط پایان چپتر | `SELECT COUNT(DISTINCT chapter_id)`, `is_completed`, `chapter_end_progress_eta_*` | آستانهها، ترتیب صفحهها، `variant` |
| پاداش سروری | `PostProgressResponse::getDailyGoalCoinReward`, `/v1/user/rewards/{rewardId}/confirm` | بدنهٔ پاسخ، اثر شکست، زمانبندی confirm |
| ناوبری | ۹ deep-link filter، ۳۰۰ رشتهٔ routeمانند، ۱۰ کلاس `Navigation*` | گراف `NavHost`، routeهای واقعی، back stack |
| نشست/توکن | کلاسهای `ui/authentication/*` | ذخیرهٔ امن، تازهسازی، logout |
| WorkManager/سرویسها | ۱۹ service، ۲۰ receiver، جداول `WorkSpec` | زمانبندی واقعی و اثر آنها |

## ۴. آنچه *استاتیک* مشاهده شد (برچسب درست: `OBSERVED`)

اینها **RUNTIME VERIFIED نیستند** و صرفاً بایت/رشته/دستورالعملاند:

- ۱۲ DEX، ۲۹٬۴۵۴ class_def، ۱۲۲٬۵۴۶ `code_item`، ۱٬۲۸۴٬۵۴۲ نماد Ghidra.
- بدنهٔ disassembleشدهٔ ۱۲۲ تابع هدف (`GHIDRA/CONTROL_FLOW.txt`) ازجمله
  `LessonProgress::isSolvedCorrectly @0x509744bc` و `GetPathMapState$invoke$2::invokeSuspend @0x509a8f34`.
- ۶۸ عبارت SQL، ۵۳ تعریف Retrofit، ۶۸ رشتهٔ مسیر، ۹۴٬۴۰۱ ورودی منبع، ۱۲ کتابخانهٔ `.so`.
- ۵۳۹ `DebugMetadata`، ۸۴ فیلد ماشین حالت، ۶۵۲ کلاس suspend.
- shipped v753: ۱۹ مسیر / ۱۴۴ section / ۲٬۰۰۲ tutorial / ۰ نقض پیوستگی.

## ۵. پروتکل پیشنهادی برای وقتی محیط تأیید شد (اجرا نشده است)

1. نصب APK **اصلی و دستنخورده** روی emulator، بدون تغییر باینری و بدون دستکاری دادهٔ کاربر production.
2. `adb shell uiautomator dump` + `adb logcat` + اسکرینشات در هر گام؛ ثبت هش APK قبل/بعد.
3. دنباله: launch → onboarding/skip → MainActivity → تب Learn → اسکرول مسیر → انتخاب گره →
   اجرای درس → اتمام → صفحهٔ پایان چپتر → نمایش پاداش/پیشرفت.
4. فقط در **محیط تست مجاز**، ثبت درخواست/پاسخ نقاط `/progress`, `/completion`, `/rewards/*`.
5. مقایسهٔ مقادیر مشاهدهشده با فیلدهای استاتیک (`rewardMultiplier`, `scrollPositionX`, …) و
   **ارتقای برچسب فقط پس از تطابق واقعی**.

> ممنوعیتها: تغییر production user data ❌؛ جلوه دادن استنتاج استاتیک بهعنوان مشاهدهٔ runtime ❌؛
> ادعای شبکه بدون محیط مجاز ❌. هیچکدام انجام نشده است.

## ۶. پیامد بر سایر اسناد

`LEARNING_PATH_ENGINE.fa.md` و `LESSON_AND_SCORING_ENGINE.fa.md` بنابراین
**هیچ ادعای پیکسلبهپیکسل، مقدار `dp`، ضریب امتیاز یا `SERVER CONFIRMED`** ندارند.
`COVERAGE_REPORT.fa.md` سطر `runtime_verified_behaviours = 0` و
`server_confirmed_responses = 0` را با مخرج «تعریفنشده» ثبت کرده است.
`EVIDENCE_INDEX.json` شامل ۱۱ ورودی `UNKNOWN` است که ۷ تای آنها دقیقاً رفتارهای مادهٔ ۸اند.
