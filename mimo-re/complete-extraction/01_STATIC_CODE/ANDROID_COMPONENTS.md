# ۰۱ب — فهرست کامپوننت‌های اندروید

منبع: `ANDROID_COMPONENTS.csv` (۱۰۸ ردیف: ۶۱ activity، ۱۹ service، ۸ provider، ۲۰ receiver).

## ۱. اکتیویتی‌های صادرشده (۸ مورد) و ریسک آن‌ها

| کامپوننت | فیلترها | مسیر/طرح | ارزیابی |
|---|---|---|---|
| `com.getmimo.ui.SplashActivity` | ۳ | `https|mimo://getmimo.com/login`, `/register`, `/deeplink/continuelearning`, `/deeplink/support` | لازم برای deep link |
| `com.getmimo.ui.MainActivity` | ۳ | `https|mimo://getmimo.com/profile`, `/learn/.*` | الگوی **wildcard** — هر مسیر learn پذیرفته می‌شود |
| `com.facebook.CustomTabActivity` | ۲ | `fbconnect://cct.com.getmimo` | OAuth فیس‌بوک |
| `com.canhub.cropper.CropImageActivity` | ۱ | — | برش تصویر پروفایل |
| `firebase.auth.internal.GenericIdpActivity` | ۰ | `genericidp://firebase.auth/` | `singleTask` |
| `firebase.auth.internal.RecaptchaActivity` | ۰ | `recaptcha://firebase.auth/` | `singleTask` |
| `saschpe.android.customtabs.WebViewActivity` | ۰ | — | مرورگر داخلی |
| `androidx.compose.ui.tooling.PreviewActivity` | ۰ | — | **ابزار QA در بیلد تولید** |

## ۲. Activity-alias

`main_activity` در بسته `com.getmimo.ui.SplashActivity_default` است؛ یعنی راه‌انداز یک alias
از `SplashActivity` است. جفت‌شدن با `ChangeAppIconActivity` و
`ModalData$AppIconChangeNeedsRestart` نشان می‌دهد تغییر آیکون برنامه با سوئیچ alias انجام
می‌شود (INFERRED، شاهد: نام alias + کلاس‌ها + رشتهٔ «requires restart»).

## ۳. سرویس‌ها (۱۹) — نقش‌ها

Firebase Messaging، WorkManager (`SystemJobService`)، RevenueCat، Adjust، Customer.io،
`StreakWidgetRefreshWorker` و سرویس‌های foreground مرتبط با اجرای کد/دانلود محتوا
(بر پایهٔ نام؛ VERIFIED_STATIC برای نام، INFERRED برای نقش).

## ۴. Providerها (۸) و Receiverها (۲۰)

Providerها شامل FileProvider و initializerهای AndroidX/Firebase/WorkManager هستند؛
Receiverها شامل بوت، به‌روزرسانی ویجت، اعلان‌های Firebase و اتریبیوشن Adjust.

## ۵. اجزای غیرقابل‌دسترس (NOT_ACCESSIBLE)

* Developer Menu: هیچ اکتیویتی صادرشده‌ای به `DeveloperMenuActivity` نمی‌رسد (VERIFIED_STATIC).
* `AwesomeModeActivity` (پیش‌نمایش زنده) هم صادر نشده است.
