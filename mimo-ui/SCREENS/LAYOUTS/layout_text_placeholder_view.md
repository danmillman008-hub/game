# پروندهٔ لایه — `res/layout/text_placeholder_view.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/text_placeholder_view.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/text_placeholder_view.xml`](../../SOURCE/res/layout/text_placeholder_view.xml) |
| SHA-256 دیکد | `9ec4ab8cf680b022be94339806d70954b5970b58f3ba340510c0423e220d6434` |
| ریشه | `FrameLayout` |
| تعداد گره | 3 |
| تعداد شناسه | 2 |
| تگ‌های استفاده‌شده | 3 |
| ویوهای سفارشی `com.getmimo` | 1 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 2 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ FrameLayout
   ├─ com.getmimo.ui.components.placeholder.PlaceholderView  #@id/placeholder_text_placeholder
   └─ TextView  #@id/tv_text_placeholder
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `FrameLayout` | `android:layout_width` | `match_parent` |
| 2 | `FrameLayout` | `android:layout_height` | `match_parent` |
| 3 | `com.getmimo.ui.components.placeholder.PlaceholderView` | `android:id` | `@id/placeholder_text_placeholder` |
| 4 | `com.getmimo.ui.components.placeholder.PlaceholderView` | `android:layout_width` | `match_parent` |
| 5 | `com.getmimo.ui.components.placeholder.PlaceholderView` | `android:layout_height` | `match_parent` |
| 6 | `TextView` | `android:ellipsize` | `end` |
| 7 | `TextView` | `android:id` | `@id/tv_text_placeholder` |
| 8 | `TextView` | `android:layout_width` | `match_parent` |
| 9 | `TextView` | `android:layout_height` | `match_parent` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|

## ۴. شناسه‌های `@id`

```text
@id/placeholder_text_placeholder
@id/tv_text_placeholder
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
  <com.getmimo.ui.components.placeholder.PlaceholderView android:id="@id/placeholder_text_placeholder" android:layout_width="match_parent" android:layout_height="match_parent"/>
  <TextView android:ellipsize="end" android:id="@id/tv_text_placeholder" android:layout_width="match_parent" android:layout_height="match_parent"/>
</FrameLayout>
```
