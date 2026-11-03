# پروندهٔ لایه — `res/layout/glance_check_box.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/glance_check_box.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/glance_check_box.xml`](../../SOURCE/res/layout/glance_check_box.xml) |
| SHA-256 دیکد | `a869dbda60ea565e4dc0cb24782cc9e2b9aab527ecf67bc1a3f5cb8ae7ebcdda` |
| ریشه | `FrameLayout` |
| تعداد گره | 2 |
| تعداد شناسه | 1 |
| تگ‌های استفاده‌شده | 2 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 2 |
| ارجاع به منابع | 3 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ FrameLayout
   └─ ViewStub  #@id/checkBox
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `FrameLayout` | `android:layout_width` | `wrap_content` |
| 2 | `FrameLayout` | `android:layout_height` | `wrap_content` |
| 3 | `FrameLayout` | `android:textDirection` | `locale` |
| 4 | `FrameLayout` | `app:glance_isTopLevelLayout` | `true` |
| 5 | `FrameLayout` | `style` | `@style/Glance.AppWidget.CheckBox` |
| 6 | `ViewStub` | `android:id` | `@id/checkBox` |
| 7 | `ViewStub` | `android:layout` | `@layout/glance_check_box_view` |
| 8 | `ViewStub` | `android:layout_width` | `wrap_content` |
| 9 | `ViewStub` | `android:layout_height` | `wrap_content` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@style/Glance.AppWidget.CheckBox` | `[]` |

## ۴. شناسه‌های `@id`

```text
@id/checkBox
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
<FrameLayout xmlns:app="http://schemas.android.com/apk/res-auto" xmlns:android="http://schemas.android.com/apk/res/android" android:layout_width="wrap_content" android:layout_height="wrap_content" android:textDirection="locale" app:glance_isTopLevelLayout="true" style="@style/Glance.AppWidget.CheckBox">
  <ViewStub android:id="@id/checkBox" android:layout="@layout/glance_check_box_view" android:layout_width="wrap_content" android:layout_height="wrap_content"/>
</FrameLayout>
```
