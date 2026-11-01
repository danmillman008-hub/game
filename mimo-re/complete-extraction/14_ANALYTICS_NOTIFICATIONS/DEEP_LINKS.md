# ۱۴ج — لینک‌های عمیق (بازتولیدشده)

منبع: `DEEP_LINKS.csv` (پارس Manifest).

| host | scheme | path | مقصد |
|---|---|---|---|
| `getmimo.com` | `https` \| `mimo` | `/learn/.*` | `MainActivity` (wildcard) |
| `getmimo.com` | `https` \| `mimo` | `/profile` | `MainActivity` |
| `getmimo.com` | `https` \| `mimo` | `/login` | `SplashActivity` |
| `getmimo.com` | `https` \| `mimo` | `/register` | `SplashActivity` |
| `getmimo.com` | `https` \| `mimo` | `/deeplink/continuelearning` | `SplashActivity` |
| `getmimo.com` | `https` \| `mimo` | `/deeplink/support` | `SplashActivity` |
| `fbconnect` | — | `cct.com.getmimo` | `CustomTabActivity` |
| `genericidp` | — | `firebase.auth` | `GenericIdpActivity` |
| `recaptcha` | — | `firebase.auth` | `RecaptchaActivity` |

## ۲. مشاهدهٔ امنیتی

* `/learn/.*` یک **wildcard** است: هر مسیری از دامنهٔ mimo.com به `MainActivity` می‌رود.
  اگر کلاینت مسیر را parse و به شناسه نگاشت می‌کند، ورودی نامعتبر باید رد شود (UNKNOWN).
* `SplashActivity` صادرشده با ۴ مسیر ⇒ سطح حملهٔ ورودی خارجی.
* هیچ `verified`/App Links (assetlinks) قابل تأیید نیست (در Manifest قابل بررسی نیست بدون aapt).

```
dumpsys  →  adb shell am start -a android.intent.action.VIEW -d "https://getmimo.com/learn/1001"
```
این دستور برای تست زمان‌اجرا لازم است — **NOT_TESTED** (بدون دستگاه).
