# پروندهٔ لایه — `res/layout/custom_views_activity.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/custom_views_activity.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/custom_views_activity.xml`](../../SOURCE/res/layout/custom_views_activity.xml) |
| SHA-256 دیکد | `600cd756e6b590fb3791815c6915c70fe706badf277a1951f9590aaae48b3761` |
| ریشه | `LinearLayout` |
| تعداد گره | 2 |
| تعداد شناسه | 1 |
| تگ‌های استفاده‌شده | 2 |
| ویوهای سفارشی `com.getmimo` | 1 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 1 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ LinearLayout
   └─ com.getmimo.ui.lesson.view.database.DatabaseView  #@id/database_view
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `LinearLayout` | `android:orientation` | `vertical` |
| 2 | `LinearLayout` | `android:layout_width` | `match_parent` |
| 3 | `LinearLayout` | `android:layout_height` | `match_parent` |
| 4 | `com.getmimo.ui.lesson.view.database.DatabaseView` | `android:id` | `@id/database_view` |
| 5 | `com.getmimo.ui.lesson.view.database.DatabaseView` | `android:layout_width` | `match_parent` |
| 6 | `com.getmimo.ui.lesson.view.database.DatabaseView` | `android:layout_height` | `wrap_content` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|

## ۴. شناسه‌های `@id`

```text
@id/database_view
```

## ۵. ارجاع به لایه‌های دیگر

```text
(none)
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

```text
com.getmimo.ui.developermenu.viewcomponents.customviews.CustomViewsActivity
```

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android" android:orientation="vertical" android:layout_width="match_parent" android:layout_height="match_parent">
  <com.getmimo.ui.lesson.view.database.DatabaseView android:id="@id/database_view" android:layout_width="match_parent" android:layout_height="wrap_content"/>
</LinearLayout>
```
