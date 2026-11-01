# ۱۰ج — مدل احراز هویت

## ۱. اجزا (VERIFIED_STATIC)

| جزء | شاهد |
|---|---|
| Firebase Auth | `com.google.firebase.auth` (کلاس‌های `GenericIdpActivity`, `RecaptchaActivity`) |
| توکن Bearer | رشته‌های `Authorization`, `Bearer ` در `AiTutorRepository` |
| Firebase Auth REST | `/auth/login`, `/auth/token`, `/auth/revoke`, `/authTokens:generate` (literal) |
| ورود مهمان | `guest_*` رشته‌ها + `/v1/account` |
| ورود اجتماعی | Facebook SDK (`CustomTabActivity`, `fbconnect://`)، Google (GMS) |
| بیومتریک | `USE_BIOMETRIC` + `USE_FINGERPRINT` مجوزها |
| پروفایل | `/v1/users/{userId}/profile`, `/v1/account/email` (PUT) |

## ۲. جریان استنباطی

```
1) SplashActivity → FirebaseAuth.currentUser
2) اگر null: AuthenticationActivity (ایمیل/Google/Facebook/مهمان)
3) دریافت ID token از Firebase → Authorization: Bearer <idToken>
4) سرور Mimo: /v1/account (پروفایل + entitlement)
5) تازه‌سازی خودکار توکن (Firebase)
6) خروج: FirebaseAuth.signOut + /auth/revoke (INFERRED)
```

## ۳. نکات امنیتی مشاهده‌شده

| یافته | ارزیابی |
|---|---|
| توکن در هدر Bearer (استاندارد) | ✅ |
| Firebase Auth REST literals در بسته | عادی (SDK) |
| بیومتریک محلی برای محافظت از نشست | ✅ ولی بدون تأیید اجرا |
| `DYNAMIC_RECEIVER_NOT_EXPORTED_PERMISSION` | ✅ سازگاری اندروید ۱۴ |
| `WRITE_EXTERNAL_STORAGE` | ⚠️ قدیمی/غیرلازم |
| `PreviewActivity` و Developer Menu در بیلد تولید | ⚠️ سطح حمله |

## ۴. برای محصول هدف (کنکور)

| نیاز | تصمیم پیشنهادی |
|---|---|
| ورود دانش‌آموز | شمارهٔ موبایل + OTP (ایران) یا ایمیل |
| مهمان | لازم است (آنبوردینگ بدون اصطکاک) |
| چند دستگاهی | همان حساب، همگام‌سازی پیشرفت |
| نقش‌ها | دانش‌آموز / معلم / والد / ادمین |
| کد ملی / مشخصات | مورد نیاز برای کارنامه — با رمزنگاری و رضایت |
| پیوند خانوادگی | والد ↔ دانش‌آموز (Mimo ندارد) |

**هیچ‌کدام از این‌ها از Mimo قابل کپی نیست**؛ فقط الگوی «Firebase + Bearer + entitlement» منتقل می‌شود.
