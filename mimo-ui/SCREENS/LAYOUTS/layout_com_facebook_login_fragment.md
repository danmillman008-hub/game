# پروندهٔ لایه — `res/layout/com_facebook_login_fragment.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/com_facebook_login_fragment.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/com_facebook_login_fragment.xml`](../../SOURCE/res/layout/com_facebook_login_fragment.xml) |
| SHA-256 دیکد | `f42e63931fd0e888025af96a03ff57ccba65825f81f8df90483ebe8a31fcbeb9` |
| ریشه | `RelativeLayout` |
| تعداد گره | 2 |
| تعداد شناسه | 1 |
| تگ‌های استفاده‌شده | 2 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 1 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ RelativeLayout
   └─ ProgressBar  #@id/com_facebook_login_fragment_progress_bar
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `RelativeLayout` | `android:layout_width` | `match_parent` |
| 2 | `RelativeLayout` | `android:layout_height` | `match_parent` |
| 3 | `ProgressBar` | `android:id` | `@id/com_facebook_login_fragment_progress_bar` |
| 4 | `ProgressBar` | `android:visibility` | `gone` |
| 5 | `ProgressBar` | `android:layout_width` | `wrap_content` |
| 6 | `ProgressBar` | `android:layout_height` | `50.000000dip` |
| 7 | `ProgressBar` | `android:indeterminate` | `true` |
| 8 | `ProgressBar` | `android:indeterminateOnly` | `true` |
| 9 | `ProgressBar` | `android:layout_centerInParent` | `true` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|

## ۴. شناسه‌های `@id`

```text
@id/com_facebook_login_fragment_progress_bar
```

## ۵. ارجاع به لایه‌های دیگر

```text
(none)
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

```text
com.facebook.FacebookActivity
```

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android" android:layout_width="match_parent" android:layout_height="match_parent">
  <ProgressBar android:id="@id/com_facebook_login_fragment_progress_bar" android:visibility="gone" android:layout_width="wrap_content" android:layout_height="50.000000dip" android:indeterminate="true" android:indeterminateOnly="true" android:layout_centerInParent="true"/>
</RelativeLayout>
```
