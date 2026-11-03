# پروندهٔ لایه — `res/layout/splash_screen_view.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/splash_screen_view.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/splash_screen_view.xml`](../../SOURCE/res/layout/splash_screen_view.xml) |
| SHA-256 دیکد | `7ccd89effcc2994ec284dc8bfd0ac420d399de557537aa86c5bf4e48378d1e44` |
| ریشه | `FrameLayout` |
| تعداد گره | 2 |
| تعداد شناسه | 1 |
| تگ‌های استفاده‌شده | 2 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 2 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ FrameLayout
   └─ ImageView  #@id/splashscreen_icon_view
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `FrameLayout` | `android:fitsSystemWindows` | `false` |
| 2 | `FrameLayout` | `android:layout_width` | `match_parent` |
| 3 | `FrameLayout` | `android:layout_height` | `match_parent` |
| 4 | `FrameLayout` | `android:animateLayoutChanges` | `false` |
| 5 | `ImageView` | `android:layout_gravity` | `0x00000011` |
| 6 | `ImageView` | `android:id` | `@id/splashscreen_icon_view` |
| 7 | `ImageView` | `android:layout_width` | `?attr/splashScreenIconSize` |
| 8 | `ImageView` | `android:layout_height` | `?attr/splashScreenIconSize` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|

## ۴. شناسه‌های `@id`

```text
@id/splashscreen_icon_view
```

## ۵. ارجاع به لایه‌های دیگر

```text
(none)
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

```text
com.getmimo.ui.SplashActivity
```

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<FrameLayout xmlns:android="http://schemas.android.com/apk/res/android" android:fitsSystemWindows="false" android:layout_width="match_parent" android:layout_height="match_parent" android:animateLayoutChanges="false">
  <ImageView android:layout_gravity="0x00000011" android:id="@id/splashscreen_icon_view" android:layout_width="?attr/splashScreenIconSize" android:layout_height="?attr/splashScreenIconSize"/>
</FrameLayout>
```
