# ۱۴ — معماری تحلیل (Analytics)

## ۱. ابزارها (VERIFIED_STATIC از شمارش کلاس)

| ابزار | کلاس | نقش |
|---|---|---|
| **Segment** | ۱۳۷ | روتر رویداد (تازه شناسایی شد) |
| Mixpanel | ۶۲ | تحلیل محصول |
| Firebase Analytics | بخشی از ۵,۷۱۸ کلاس `com.google` | پایه |
| Adjust | ۳۱۵ | اتریبیوشن نصب |
| Customer.io | ۳۵۱ | پیام چرخهٔ عمر + Inbox |
| AppsFlyer? | ❌ شاهدی نبود | — |
| Facebook SDK | ۱۱۷ | رویداد + ورود |
| RevenueCat | ۲,۴۳۶ | رویداد خرید |
| سرور خودی | `/v1/events` (literal) | آینهٔ رویداد |

## ۲. تصحیح مهمِ گزارش قبلی

| ادعای قبلی | واقعیت اندازه‌گیری‌شده |
|---|---|
| «۳۰۵ رویداد تحلیلی» | **۳۰۵ کلاس `properties/*` است** (نه رویداد) |
| — | ۲۳۷ شناسهٔ snake_case متمایز در بستهٔ `com.getmimo.analytics` |
| — | رویدادها به‌صورت رشتهٔ ثابت در فراخوانی‌ها هستند و **بدون decompiler قابل شمارش کامل نیستند** |

⇒ فهرست کامل نام رویدادها **NOT_ACCESSIBLE** با ابزار فعلی. آنچه داریم:
`ANALYTICS_EVENT_CATALOG.csv` (۱۸۹ ردیف، اطمینان LOW — اتحاد رشته‌های کلاس‌ها).
این را باید به‌عنوان «شاهد خام» استفاده کرد، نه «فهرست رویداد».

## ۳. ساختار رویداد (بازسازی از کلاس‌های property)

```
event: segment.track(name, properties)
properties ← کلاس‌های نوع‌دار: e.g. ShowUpgradeDialog{upgradeDialogType, timesShown,
             continueToPurchaseScreen, trackId, tutorialId, lessonId, discountPercentage}
```
⇒ Mimo **schema مستقل برای هر رویداد** دارد (۱۷۵ کلاس property). این بهترین الگوی قابل کپی است:
هر رویداد یک کلاس، هر فیلد یک مقدار نوع‌دار.

## ۴. مدل ردیابی

| لایه | شاهد |
|---|---|
| `Analytics` (facade) | `Analytics$ShowUpgradeDialog` و ۳۰۴ کلاس دیگر |
| `properties/` | ۳۰۵ کلاس، شامل `upgrade/`, `paywall/`, `lesson/` |
| `source/remote/analytics` | ارسال: Segment/Mixpanel/سرور |
| People/User props | `PeopleProperty` (active_coin_count, active_streak_length, adid …) |

## ۵. توصیهٔ الزامی برای محصول هدف

1. **فهرست رویداد ثابت** (حداکثر ۴۰ رویداد) با schema (بدون کلاس per-event در کلاینت).
2. یک‌بار ارسال، چند مقصد (مانند Segment) — نه کد مستقیم برای هر ابزار.
3. PII ممنوع: شمارهٔ موبایل/کد ملی هش شوند.
4. رویدادهای آموزشی حیاتی (کنکور): `question_answered`, `exam_started`, `exam_finished`,
   `review_scheduled`, `hint_used`, `assistant_message`, `mock_exam_scored`.
5. اندازه‌گیریِ **یادگیری**، نه فقط کلیک.
