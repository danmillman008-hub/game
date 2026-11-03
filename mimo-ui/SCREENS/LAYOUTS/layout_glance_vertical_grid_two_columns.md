# پروندهٔ لایه — `res/layout/glance_vertical_grid_two_columns.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/glance_vertical_grid_two_columns.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/glance_vertical_grid_two_columns.xml`](../../SOURCE/res/layout/glance_vertical_grid_two_columns.xml) |
| SHA-256 دیکد | `aef0e48297a9d5c302bb2a70c5f0aeabd52b67ec9961b18cfaa4f19d67b7b846` |
| ریشه | `GridView` |
| تعداد گره | 1 |
| تعداد شناسه | 0 |
| تگ‌های استفاده‌شده | 1 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 4 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ GridView
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `GridView` | `android:theme` | `@style/Glance.AppWidget.Theme.GridChildren` |
| 2 | `GridView` | `android:layout_width` | `wrap_content` |
| 3 | `GridView` | `android:layout_height` | `wrap_content` |
| 4 | `GridView` | `android:listSelector` | `@0x0106000D` |
| 5 | `GridView` | `android:numColumns` | `2` |
| 6 | `GridView` | `android:divider` | `@null` |
| 7 | `GridView` | `app:glance_isTopLevelLayout` | `true` |
| 8 | `GridView` | `style` | `@style/Glance.AppWidget.VerticalGrid` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@style/Glance.AppWidget.Theme.GridChildren` | `[]` |
| `@style/Glance.AppWidget.VerticalGrid` | `[]` |

## ۴. شناسه‌های `@id`

```text
(none)
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
<GridView xmlns:app="http://schemas.android.com/apk/res-auto" xmlns:android="http://schemas.android.com/apk/res/android" android:theme="@style/Glance.AppWidget.Theme.GridChildren" android:layout_width="wrap_content" android:layout_height="wrap_content" android:listSelector="@0x0106000D" android:numColumns="2" android:divider="@null" app:glance_isTopLevelLayout="true" style="@style/Glance.AppWidget.VerticalGrid"/>
```
