# پروندهٔ لایه — `res/layout-v33/glance_vertical_grid_four_columns_wrapwidth_expandheight.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout-v33/glance_vertical_grid_four_columns_wrapwidth_expandheight.xml` |
| فایل دیکدشده | [`SOURCE/res/layout-v33/glance_vertical_grid_four_columns_wrapwidth_expandheight.xml`](../../SOURCE/res/layout-v33/glance_vertical_grid_four_columns_wrapwidth_expandheight.xml) |
| SHA-256 دیکد | `fdc57701a81f1331490a99bed9ab5db3eee94f49d09afcaea6830e429f3c71cd` |
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
| 2 | `GridView` | `android:id` | `@id/glanceView` |
| 3 | `GridView` | `android:layout_width` | `wrap_content` |
| 4 | `GridView` | `android:layout_height` | `0.000000dip` |
| 5 | `GridView` | `android:listSelector` | `@0x0106000D` |
| 6 | `GridView` | `android:numColumns` | `4` |
| 7 | `GridView` | `android:divider` | `@null` |
| 8 | `GridView` | `android:layout_weight` | `1.000000` |
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
<GridView xmlns:android="http://schemas.android.com/apk/res/android" xmlns:app="http://schemas.android.com/apk/res-auto" android:theme="@style/Glance.AppWidget.Theme.GridChildren" android:id="@id/glanceView" android:layout_width="wrap_content" android:layout_height="0.000000dip" android:listSelector="@0x0106000D" android:numColumns="4" android:divider="@null" android:layout_weight="1.000000" android:layoutDirection="locale" app:glance_isTopLevelLayout="true" style="@style/Glance.AppWidget.VerticalGrid"/>
```
