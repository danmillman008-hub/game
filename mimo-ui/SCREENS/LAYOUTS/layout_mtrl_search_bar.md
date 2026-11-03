# پروندهٔ لایه — `res/layout/mtrl_search_bar.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/mtrl_search_bar.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/mtrl_search_bar.xml`](../../SOURCE/res/layout/mtrl_search_bar.xml) |
| SHA-256 دیکد | `0264f70a3150220841b191707c01fdad2e35dbe380e3c98420707fc24a22fc79` |
| ریشه | `FrameLayout` |
| تعداد گره | 3 |
| تعداد شناسه | 3 |
| تگ‌های استفاده‌شده | 2 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 3 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ FrameLayout  #@id/open_search_bar_text_view_container
   ├─ TextView  #@id/open_search_bar_text_view
   └─ TextView  #@id/open_search_bar_placeholder_text_view
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `FrameLayout` | `android:id` | `@id/open_search_bar_text_view_container` |
| 2 | `FrameLayout` | `android:layout_width` | `wrap_content` |
| 3 | `FrameLayout` | `android:layout_height` | `wrap_content` |
| 4 | `TextView` | `android:ellipsize` | `end` |
| 5 | `TextView` | `android:id` | `@id/open_search_bar_text_view` |
| 6 | `TextView` | `android:layout_width` | `wrap_content` |
| 7 | `TextView` | `android:layout_height` | `wrap_content` |
| 8 | `TextView` | `android:maxLines` | `1` |
| 9 | `TextView` | `android:importantForAccessibility` | `no` |
| 10 | `TextView` | `android:ellipsize` | `end` |
| 11 | `TextView` | `android:id` | `@id/open_search_bar_placeholder_text_view` |
| 12 | `TextView` | `android:visibility` | `invisible` |
| 13 | `TextView` | `android:layout_width` | `wrap_content` |
| 14 | `TextView` | `android:layout_height` | `wrap_content` |
| 15 | `TextView` | `android:maxLines` | `1` |
| 16 | `TextView` | `android:importantForAccessibility` | `no` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|

## ۴. شناسه‌های `@id`

```text
@id/open_search_bar_placeholder_text_view
@id/open_search_bar_text_view
@id/open_search_bar_text_view_container
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
<FrameLayout xmlns:android="http://schemas.android.com/apk/res/android" android:id="@id/open_search_bar_text_view_container" android:layout_width="wrap_content" android:layout_height="wrap_content">
  <TextView android:ellipsize="end" android:id="@id/open_search_bar_text_view" android:layout_width="wrap_content" android:layout_height="wrap_content" android:maxLines="1" android:importantForAccessibility="no"/>
  <TextView android:ellipsize="end" android:id="@id/open_search_bar_placeholder_text_view" android:visibility="invisible" android:layout_width="wrap_content" android:layout_height="wrap_content" android:maxLines="1" android:importantForAccessibility="no"/>
</FrameLayout>
```
