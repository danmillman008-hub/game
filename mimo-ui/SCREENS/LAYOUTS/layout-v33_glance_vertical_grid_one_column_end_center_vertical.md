# پروندهٔ لایه — `res/layout-v33/glance_vertical_grid_one_column_end_center_vertical.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout-v33/glance_vertical_grid_one_column_end_center_vertical.xml` |
| فایل دیکدشده | [`SOURCE/res/layout-v33/glance_vertical_grid_one_column_end_center_vertical.xml`](../../SOURCE/res/layout-v33/glance_vertical_grid_one_column_end_center_vertical.xml) |
| SHA-256 دیکد | `72d39deb89fcf45266ac705d3d04fc2a5612e5ab60fe53c277ea22f26d8e7da8` |
| ریشه | `GridView` |
| تعداد گره | 1 |
| تعداد شناسه | 1 |
| تگ‌های استفاده‌شده | 1 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 5 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ GridView  #@id/glanceView
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `GridView` | `android:theme` | `@style/Glance.AppWidget.Theme.GridChildren` |
| 2 | `GridView` | `android:layout_gravity` | `0x00800015` |
| 3 | `GridView` | `android:id` | `@id/glanceView` |
| 4 | `GridView` | `android:layout_width` | `wrap_content` |
| 5 | `GridView` | `android:layout_height` | `wrap_content` |
| 6 | `GridView` | `android:listSelector` | `@0x0106000D` |
| 7 | `GridView` | `android:numColumns` | `1` |
| 8 | `GridView` | `android:divider` | `@null` |
| 9 | `GridView` | `android:layoutDirection` | `locale` |
| 10 | `GridView` | `app:glance_isTopLevelLayout` | `true` |
| 11 | `GridView` | `style` | `@style/Glance.AppWidget.VerticalGrid` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@style/Glance.AppWidget.Theme.GridChildren` | `[]` |
| `@style/Glance.AppWidget.VerticalGrid` | `[]` |

## ۴. شناسه‌های `@id`

```text
@id/glanceView
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
<GridView xmlns:android="http://schemas.android.com/apk/res/android" xmlns:app="http://schemas.android.com/apk/res-auto" android:theme="@style/Glance.AppWidget.Theme.GridChildren" android:layout_gravity="0x00800015" android:id="@id/glanceView" android:layout_width="wrap_content" android:layout_height="wrap_content" android:listSelector="@0x0106000D" android:numColumns="1" android:divider="@null" android:layoutDirection="locale" app:glance_isTopLevelLayout="true" style="@style/Glance.AppWidget.VerticalGrid"/>
```
