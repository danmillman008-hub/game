# پروندهٔ لایه — `res/layout/loading_view.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/loading_view.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/loading_view.xml`](../../SOURCE/res/layout/loading_view.xml) |
| SHA-256 دیکد | `e498d666788401af933ac68c35e60d52ddeedb0bc3c24ae969651a8b738a2ebc` |
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
   └─ ProgressBar  #@id/loading_view
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `FrameLayout` | `android:layout_width` | `match_parent` |
| 2 | `FrameLayout` | `android:layout_height` | `match_parent` |
| 3 | `ProgressBar` | `android:layout_gravity` | `0x00000011` |
| 4 | `ProgressBar` | `android:id` | `@id/loading_view` |
| 5 | `ProgressBar` | `android:layout_width` | `wrap_content` |
| 6 | `ProgressBar` | `android:layout_height` | `wrap_content` |
| 7 | `ProgressBar` | `android:elevation` | `2.000000dip` |
| 8 | `ProgressBar` | `android:indeterminateTint` | `@color/progress_primary` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/progress_primary` | `#FF7E4BDE` / `#FFA175EA` (night) |

## ۴. شناسه‌های `@id`

```text
@id/loading_view
```

## ۵. ارجاع به لایه‌های دیگر

```text
(none)
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

(هیچ صفحهٔ نام‌برداری به این لایه متصل نشد؛ ممکن است لایهٔ کتابخانه/`<include>` باشد)

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<FrameLayout xmlns:android="http://schemas.android.com/apk/res/android" android:layout_width="match_parent" android:layout_height="match_parent">
  <ProgressBar android:layout_gravity="0x00000011" android:id="@id/loading_view" android:layout_width="wrap_content" android:layout_height="wrap_content" android:elevation="2.000000dip" android:indeterminateTint="@color/progress_primary"/>
</FrameLayout>
```
