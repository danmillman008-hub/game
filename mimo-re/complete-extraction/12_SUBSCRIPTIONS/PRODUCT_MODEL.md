# ۱۲ — مدل خرید و اشتراک

## ۱. اجزا (VERIFIED_STATIC)

| جزء | شاهد |
|---|---|
| RevenueCat | ۲,۴۳۶ کلاس (`com.revenuecat`) — موتور اصلی |
| Google Play Billing | مجوز `com.android.vending.BILLING` |
| محصولات | `v1/products/user`, `v1/package`، `AllPlansActivity` |
| تخفیف | `DiscountedSubscription`, `RemoteConfigDiscount`، رشتهٔ شمارش معکوس |
| آزمایش | `trial_*`، `in_app_offer_*` |
| بازیابی | `restore_purchases` |
| ارتقا | `UpgradeDrawer`, `ShowUpgradeDialogType`, `UpgradeSource` (۲۵+ مقدار) |

## ۲. سطوح اشتراک (استنباط از رشته‌ها)

| سطح | شاهد | تفاوت |
|---|---|---|
| Free | محدودیت کلید/مربی | — |
| **Pro** | `*_pro_*`، `keys_unlimited_keys_pro_subtitle` | کلید نامحدود |
| **Max** | `*_max_*`، `keys_unlimited_keys_max_subtitle` | + مزایای بیشتر |

## ۳. نقاط نمایش پی‌وال (Paywall touchpoints) — اندازه‌گیری‌شده

| نقطه | شاهد |
|---|---|
| مسیر/بنر مسیر | `track_content_upgrade_pro_*`, `PaywallTrackingSource$LastCall$PathBanner` |
| فصل | `chapter_upgrade_*` |
| پایان درس | `lesson_completed_upgrade_*` |
| کلید صفر | `keys_zero_*` |
| تمرین هوشمند | `SmartPracticeChargedModal` |
| مربی هوشمند | `ShowUpgradeDialogType$AiTutor` |
| گواهی | `certificate_upselling_*` |
| آیکون برنامه | `settings_app_icon_*` |
| لیگ/لیدربورد | `iap_podium_*`, `league_*` |

⇒ **۹ نقطه**؛ این «تراکم پی‌وال» بالاست و برای کنکور توصیه نمی‌شود (بیش از ۳ نقطه آزاردهنده است).

## ۴. ردیابی

`PaywallTrackingSource` + `upgrade_source` در رویدادهای تحلیلی ⇒ هر نمایش/کلیک قابل انتساب است.
این الگو **ارزش کپی دارد** (اندازه‌گیری قیف واقعی).
