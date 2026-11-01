# ۱۳ب — آزمایش‌ها (A/B)

## ۱. آزمایش محتوا (تأییدشده)

```
ParsedContentExperiment$Experiment { originalTrackId, variantTrackId, visibilityPercentage }
ContentExperiment { originalTrackId, variantTrackId, useTheVariant }
ContentExperimentState$Started { contentExperiment }
FirebaseRemoteConfigFetcher → fetchAndPersistAbTestUserGroup()
```
⇒ Mimo می‌تواند **کل مسیر** را به دو نسخه تقسیم کند و درصد کاربران را به نسخهٔ آزمایشی بدهد.
گروه کاربر در Remote Config ذخیره می‌شود (پایدار).

## ۲. رویدادهای مرتبط (شاهد)

`ContentExperimentState$Started`, `ShowUpgradeDialog` (`timesShown`, `discountPercentage`),
`PaywallTrackingSource` (۱۵+ منبع).

## ۳. آنچه نمی‌دانیم

| مورد | وضعیت |
|---|---|
| معیار برد (metric) | **UNKNOWN** |
| اندازهٔ نمونه/مدت | **UNKNOWN** |
| آزمایش قیمت | شاهدی نیست (فقط تخفیف) |
| آزمایش UI (طرح درس) | شاهدی نیست |

## ۴. طرح پیشنهادی

| آزمایش | معیار | ریسک |
|---|---|---|
| طول درس (۵ vs ۸ سؤال) | نرخ اتمام جلسه | کم |
| بازخورد per-gap vs کلی | نرخ تلاش مجدد | کم |
| آزمون ۱۰ vs ۲۰ سؤالی | درصد اتمام | متوسط |
| پیام مربی (کوتاه vs توضیحی) | نرخ پذیرش راهنما | متوسط |
| قیمت — **انجام ندهید** | — | اخلاقی/قانونی (تبعیض قیمتی) |
