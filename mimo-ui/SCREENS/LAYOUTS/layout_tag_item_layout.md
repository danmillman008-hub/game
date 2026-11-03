# پروندهٔ لایه — `res/layout/tag_item_layout.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/tag_item_layout.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/tag_item_layout.xml`](../../SOURCE/res/layout/tag_item_layout.xml) |
| SHA-256 دیکد | `3d8ac1ef78e0c3f497465ca5563eb6e86f1780a5a58d18c156223875bae442ea` |
| ریشه | `androidx.cardview.widget.CardView` |
| تعداد گره | 2 |
| تعداد شناسه | 1 |
| تگ‌های استفاده‌شده | 2 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 4 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ androidx.cardview.widget.CardView
   └─ TextView  #@id/item_name
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `androidx.cardview.widget.CardView` | `android:layout_width` | `match_parent` |
| 2 | `androidx.cardview.widget.CardView` | `android:layout_height` | `wrap_content` |
| 3 | `androidx.cardview.widget.CardView` | `android:foreground` | `?attr/selectableItemBackground` |
| 4 | `androidx.cardview.widget.CardView` | `app:cardCornerRadius` | `@dimen/cardview_corner_radius` |
| 5 | `androidx.cardview.widget.CardView` | `app:elevation` | `@dimen/cardview_elevation` |
| 6 | `TextView` | `android:gravity` | `0x00000011` |
| 7 | `TextView` | `android:id` | `@id/item_name` |
| 8 | `TextView` | `android:layout_width` | `wrap_content` |
| 9 | `TextView` | `android:layout_height` | `wrap_content` |
| 10 | `TextView` | `android:singleLine` | `false` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@dimen/cardview_corner_radius` | `6.000000dip` |
| `@dimen/cardview_elevation` | `1.500000dip` |

## ۴. شناسه‌های `@id`

```text
@id/item_name
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
<androidx.cardview.widget.CardView xmlns:app="http://schemas.android.com/apk/res-auto" xmlns:android="http://schemas.android.com/apk/res/android" android:layout_width="match_parent" android:layout_height="wrap_content" android:foreground="?attr/selectableItemBackground" app:cardCornerRadius="@dimen/cardview_corner_radius" app:elevation="@dimen/cardview_elevation">
  <TextView android:gravity="0x00000011" android:id="@id/item_name" android:layout_width="wrap_content" android:layout_height="wrap_content" android:singleLine="false"/>
</androidx.cardview.widget.CardView>
```
