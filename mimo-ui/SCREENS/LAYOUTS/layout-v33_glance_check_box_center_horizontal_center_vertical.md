# پروندهٔ لایه — `res/layout-v33/glance_check_box_center_horizontal_center_vertical.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout-v33/glance_check_box_center_horizontal_center_vertical.xml` |
| فایل دیکدشده | [`SOURCE/res/layout-v33/glance_check_box_center_horizontal_center_vertical.xml`](../../SOURCE/res/layout-v33/glance_check_box_center_horizontal_center_vertical.xml) |
| SHA-256 دیکد | `d1c8cd06c64ea27f57af73e412aded4256fdce7718ac3bb1ace29b6fd0bbbcc5` |
| ریشه | `FrameLayout` |
| تعداد گره | 2 |
| تعداد شناسه | 2 |
| تگ‌های استفاده‌شده | 2 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 2 |
| ارجاع به منابع | 4 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ FrameLayout  #@id/glanceView
   └─ ViewStub  #@id/checkBox
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `FrameLayout` | `android:layout_gravity` | `0x00000011` |
| 2 | `FrameLayout` | `android:id` | `@id/glanceView` |
| 3 | `FrameLayout` | `android:layout_width` | `wrap_content` |
| 4 | `FrameLayout` | `android:layout_height` | `wrap_content` |
| 5 | `FrameLayout` | `android:textDirection` | `locale` |
| 6 | `FrameLayout` | `android:layoutDirection` | `locale` |
| 7 | `FrameLayout` | `app:glance_isTopLevelLayout` | `true` |
| 8 | `FrameLayout` | `style` | `@style/Glance.AppWidget.CheckBox` |
| 9 | `ViewStub` | `android:id` | `@id/checkBox` |
| 10 | `ViewStub` | `android:layout` | `@layout/glance_check_box_view` |
| 11 | `ViewStub` | `android:layout_width` | `wrap_content` |
| 12 | `ViewStub` | `android:layout_height` | `wrap_content` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@style/Glance.AppWidget.CheckBox` | `[]` |

## ۴. شناسه‌های `@id`

```text
@id/checkBox
@id/glanceView
```

## ۵. ارجاع به لایه‌های دیگر

```text
@layout/glance_check_box_view
wrap_content
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

(هیچ صفحهٔ نام‌برداری به این لایه متصل نشد؛ ممکن است لایهٔ کتابخانه/`<include>` باشد)

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<FrameLayout xmlns:app="http://schemas.android.com/apk/res-auto" xmlns:android="http://schemas.android.com/apk/res/android" android:layout_gravity="0x00000011" android:id="@id/glanceView" android:layout_width="wrap_content" android:layout_height="wrap_content" android:textDirection="locale" android:layoutDirection="locale" app:glance_isTopLevelLayout="true" style="@style/Glance.AppWidget.CheckBox">
  <ViewStub android:id="@id/checkBox" android:layout="@layout/glance_check_box_view" android:layout_width="wrap_content" android:layout_height="wrap_content"/>
</FrameLayout>
```
