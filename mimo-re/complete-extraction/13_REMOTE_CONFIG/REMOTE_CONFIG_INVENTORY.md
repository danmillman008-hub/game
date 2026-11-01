# ۱۳ — پیکربندی از راه دور

## ۱. مکانیزم‌های شناسایی‌شده

| مکانیزم | شاهد | نقش |
|---|---|---|
| `v2/client-config` | endpoint (GET) | پیکربندی اختصاصی کلاینت |
| Firebase Remote Config | ۹۱ کلاس `*remoteconfig*`، `FirebaseRemoteConfigFetcher` | پرچم + A/B |
| Feature flags | `feature_flag_ai_tutor_android`, `feature_flag_last_call_discount` | دو پرچم با نام صریح |
| A/B محتوا | `ContentExperiment`, `ParsedContentExperiment` (`originalTrackId`, `variantTrackId`, `visibilityPercentage`) | آزمایش مسیر |
| Dev menu config | `DevMenuRemoteConfigStorage` | تغییر مقدار در دستگاه |
| تخفیف | `remote_discount*` (۵ رشته) | قیمت/شروع/پایان |

## ۲. فهرست پرچم‌ها (آنچه با نام قابل اثبات است)

| پرچم | نوع | اثر | اطمینان |
|---|---|---|---|
| `feature_flag_ai_tutor_android` | boolean | نمایش مربی هوشمند | HIGH (نام) |
| `feature_flag_last_call_discount` | boolean | فعال‌سازی دراور تخفیف آخرین‌فرصت | HIGH (نام) |
| `content_experiment` | درصد/گروه | ایا کاربر نسخهٔ آزمایشی مسیر را ببیند | MEDIUM |
| `remote_discount*` | شیء | درصد/زمان تخفیف | MEDIUM |
| پرچم‌های کلید/تمرین | **UNKNOWN** | — | — |

> تنها **۲** پرچم boolean با نام صریح پیدا شد. بنابراین ادعای «فلگ‌محور بودن کامل» درست نیست؛
> بیشتر رفتارها **داده‌محور** (بستهٔ محتوا + پاسخ سرور) هستند، نه پرچم‌محور.

## ۳. نکتهٔ مهم معماری

`v2/client-config` نشان می‌دهد Mimo پیکربندی خودش را دارد و به Firebase RC محدود نیست.
بدنهٔ پاسخ **UNKNOWN** (هیچ DTO در بسته نبود).
