# ۱۲د — یکپارچگی RevenueCat

## ۱. ردپای اندازه‌گیری‌شده

| مورد | مقدار |
|---|---|
| کلاس‌های `com.revenuecat` | **۲,۴۳۶** |
| مسیرهای third-party (literal) | `/v1/offerings`, `/v1/product_entitlement_mapping`, `/v1/subscribers/identify`, `/v1/subscribers/redeem_purchase`, `/v2/purchase`, `/v1/receipts` |
| مسیرهای اول‌طرف مرتبط | `/v1/products/user`, `/v1/package`, `/v1/account` |
| مجوز | `com.android.vending.BILLING` |

## ۲. مدل استنباطی (MEDIUM)

```
1) شناسهٔ کاربر اپ → RevenueCat identify  (app_user_id = شناسهٔ Mimo)
2) offerings → بسته‌های قابل خرید
3) purchase → Play Billing → RevenueCat → webhook → سرور Mimo
4) سرور: /v1/receipts (اعتبارسنجی) + entitlement
5) کلاینت: /v1/account → سطح Pro/Max
```
نکته: وجود `identify` + `redeem_purchase` + `receipts` نشان می‌دهد Mimo هم RevenueCat و
هم اعتبارسنجی سروری خودش را دارد ⇒ دو منبع حقیقت، که ریسک اختلاف دارد.

## ۳. آنچه نمی‌توان بازسازی کرد

| مورد | دلیل |
|---|---|
| شناسهٔ محصولات Play | در پنل Play، نه در APK |
| قیمت‌ها | از Play/RevenueCat در زمان اجرا |
| ساختار `offerings` | پاسخ سرور |
| تست خرید | نیازمند حساب و پرداخت واقعی — **NOT_TESTED** و ممنوع |

## ۴. توصیه برای محصول هدف

* یک منبع حقیقت: **سرور**. RevenueCat (یا معادل) فقط رویداد می‌دهد.
* entitlement باید شامل `tier`, `expiresAt`, `features[]` باشد، نه فقط `isPro`.
* برای بازار ایران: درگاه داخلی + اشتراک ماهانه/سالانه + کد تخفیف سازمانی (مدارس).
