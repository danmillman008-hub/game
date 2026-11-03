# صفحه — `SplashActivity`

> **خاستگاه ثبت:** `PRIOR_WORK_SCREEN_INVENTORY.csv` | **کلاس شواهد:** نام/ساختار `VERIFIED_STATIC`، نگاشت صفحه→لایه `DERIVED` (DEX xref + تطابق نام)، حالت‌ها `PARTIALLY_VERIFIED` (رشتهٔ منبع).

| ویژگی | مقدار |
|---|---|
| کلاس | `com.getmimo.ui.SplashActivity` |
| نوع | `activity` |
| exported (manifest) | `true` |
| launchMode | `` |
| theme | `@style/MaterialTheme.Launcher` |
| orientation | `` |
| targetActivity | `` |
| app-owned | `True` |
| فناوری | `view|compose (unresolved per screen)` |
| تعداد لایه‌های متصل | 1 |
| ComposeView | خیر |
| WebView | خیر |

## ۱. لایه‌های XML متصل (فهرست کامل)

- [`res/layout/splash_screen_view.xml`](../SOURCE/res/layout/splash_screen_view.xml) → [dossier](LAYOUTS/layout_splash_screen_view.md)

## ۲. درخت مؤلفه‌ها (همهٔ لایه‌های متصل)

### `res/layout/splash_screen_view.xml`

```text
└─ FrameLayout
   └─ ImageView  #@id/splashscreen_icon_view
```

## ۳. رشته‌های مرتبط (فهرست کامل)

(none)

## ۴. رنگ‌های مرتبط (فهرست کامل)

(none)

## ۵. دایمنشن‌های مرتبط (فهرست کامل)

```text
splashscreen_icon_mask_size_no_background
splashscreen_icon_mask_size_with_background
splashscreen_icon_mask_stroke_no_background
splashscreen_icon_mask_stroke_with_background
splashscreen_icon_size
splashscreen_icon_size_no_background
splashscreen_icon_size_with_background
```

## ۶. استایل‌های مرتبط (فهرست کامل)

(none)

## ۷. شواهد حالت‌ها (رشته‌های منبع)

(none)

## ۸. ناوبری / deep link

```json
[
  {
    "android:scheme": "https",
    "android:host": "getmimo.com",
    "android:path": "/login"
  },
  {
    "android:scheme": "https",
    "android:host": "getmimo.com",
    "android:path": "/register"
  },
  {
    "android:scheme": "https",
    "android:host": "getmimo.com",
    "android:path": "/onboarding/experience"
  },
  {
    "android:scheme": "https",
    "android:host": "getmimo.com",
    "android:path": "/onboarding/goal"
  },
  {
    "android:scheme": "https",
    "android:host": "getmimo.com",
    "android:path": "/resetpassword"
  },
  {
    "android:scheme": "mimo",
    "android:host": "getmimo.com",
    "android:path": "/login"
  },
  {
    "android:scheme": "mimo",
    "android:host": "getmimo.com",
    "android:path": "/register"
  },
  {
    "android:scheme": "mimo",
    "android:host": "getmimo.com",
    "android:path": "/onboarding/experience"
  },
  {
    "android:scheme": "mimo",
    "android:host": "getmimo.com",
    "android:path": "/onboarding/goal"
  },
  {
    "android:scheme": "mimo",
    "android:host": "getmimo.com",
    "android:path": "/resetpassword"
  },
  {
    "android:scheme": "mimo",
    "android:host": "getmimo.com",
    "android:path": "/deeplink/continuelearning"
  },
  {
    "android:scheme": "mimo",
    "android:host": "getmimo.com",
    "android:path": "/deeplink/support"
  },
  {
    "android:scheme": "mimo",
    "android:host": "getmimo.com",
    "android:path": "/deeplink/practiceshortcut"
  }
]
```
