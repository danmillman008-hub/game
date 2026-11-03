# پروندهٔ لایه — `res/layout/dialog_loading_progress.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/dialog_loading_progress.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/dialog_loading_progress.xml`](../../SOURCE/res/layout/dialog_loading_progress.xml) |
| SHA-256 دیکد | `d03426c0e437da1244b3a94f671fc5d17bb9ace32a868dea8c69b958b257aa96` |
| ریشه | `LinearLayout` |
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
└─ LinearLayout
   └─ ProgressBar  #@id/progress_bar
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `LinearLayout` | `android:gravity` | `0x00000011` |
| 2 | `LinearLayout` | `android:orientation` | `vertical` |
| 3 | `LinearLayout` | `android:padding` | `24.000000dip` |
| 4 | `LinearLayout` | `android:layout_width` | `match_parent` |
| 5 | `LinearLayout` | `android:layout_height` | `wrap_content` |
| 6 | `ProgressBar` | `android:id` | `@id/progress_bar` |
| 7 | `ProgressBar` | `android:layout_width` | `wrap_content` |
| 8 | `ProgressBar` | `android:layout_height` | `wrap_content` |
| 9 | `ProgressBar` | `android:indeterminate` | `true` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|

## ۴. شناسه‌های `@id`

```text
@id/progress_bar
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
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android" android:gravity="0x00000011" android:orientation="vertical" android:padding="24.000000dip" android:layout_width="match_parent" android:layout_height="wrap_content">
  <ProgressBar android:id="@id/progress_bar" android:layout_width="wrap_content" android:layout_height="wrap_content" android:indeterminate="true"/>
</LinearLayout>
```
