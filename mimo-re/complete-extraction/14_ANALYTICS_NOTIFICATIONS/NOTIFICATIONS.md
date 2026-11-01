# ۱۴ب — اعلان‌ها

## ۱. کانال‌ها

| کانال | شاهد |
|---|---|
| Firebase Messaging | `MimoFirebaseMessagingService`, مجوز `C2D_MESSAGE` |
| Customer.io In-App + Push | ۳۵۱ کلاس، `customerIoServiceWrapper`, `pushNotificationRegistry` |
| اعلان محلی/زمان‌بند | `POST_NOTIFICATIONS`, `RECEIVE_BOOT_COMPLETED` |
| In-app message | `in_app_messaging` در `feature-evidence.json` |
| ویجت | `MimoStreakWidget` + `StreakWidgetRefreshWorker` |

## ۲. جریان ثبت توکن (VERIFIED_STATIC از رشته‌ها)

```
onNewToken(token) → DefaultDeviceTokensRepository.sendPushRegistrationToken
    → POST /v1/user/deviceTokens
    (خطا: "Error while sending push registration ID to backend.")
    (Customer.io: unregister/clear → "Cleared push registration id")
```
⇒ **دو رجیستری** (Mimo + Customer.io) با هم‌گام‌سازی.

## ۳. انواع اعلان (استنباط از رشته‌ها)

| نوع | شاهد | هدف |
|---|---|---|
| یادآوری زنجیره | `streak_*notification*` | بازگشت روزانه |
| بازفعال‌سازی | `reactivation_flow`, `after_inactivity` | کاربر رهاشده |
| تخفیف آخرین‌فرصت | `feature_flag_last_call_discount` | فروش |
| پایان دورهٔ آزمایشی | `pro_expiration_*` | تبدیل |
| پیام درون‌برنامه‌ای | Customer.io | راهنما/نظرسنجی |

## ۴. ارزیابی برای دانش‌آموز کنکور

| الگو | توصیه |
|---|---|
| یادآوری روزانه زنجیره | ❌ |
| یادآوری برنامهٔ مطالعه (زمان انتخاب‌شده) | ✅ |
| اعلان والد دربارهٔ پیشرفت فرزند | ✅ (نیاز بازار ایران) |
| اعلان آزمون نزدیک | ✅ |
| تخفیف فوری/تایمر | ❌ |
| سقف روزانه | حداکثر ۲ اعلان؛ ساعت ساکت ۲۲–۸ |

## ۵. پیاده‌سازی پیشنهادی

```
/v1/user/devices  POST {token, provider, locale, tz, appVersion}
server: صف زمان‌بندی با respect tz + quiet hours + frequency cap
deep link: mimo://... معادل: konkur://exam/{id}
```
