# پروندهٔ لایه — `res/layout/glance_check_box_view.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/glance_check_box_view.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/glance_check_box_view.xml`](../../SOURCE/res/layout/glance_check_box_view.xml) |
| SHA-256 دیکد | `11e9ede14ca7b188d31f736b8adccc5cc5f3e54569187134e5e85b7b7149bb1c` |
| ریشه | `CheckBox` |
| تعداد گره | 1 |
| تعداد شناسه | 0 |
| تگ‌های استفاده‌شده | 1 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 1 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ CheckBox
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `CheckBox` | `android:tag` | `glanceCompoundButton` |
| 2 | `CheckBox` | `android:layout_width` | `wrap_content` |
| 3 | `CheckBox` | `android:layout_height` | `wrap_content` |
| 4 | `CheckBox` | `android:textDirection` | `locale` |
| 5 | `CheckBox` | `style` | `@style/Glance.AppWidget.CheckBox` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@style/Glance.AppWidget.CheckBox` | `[]` |

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

```text
res/layout-v33/glance_check_box_center_horizontal_bottom.xml
res/layout-v33/glance_check_box_center_horizontal_center_vertical.xml
res/layout-v33/glance_check_box_center_horizontal_top.xml
res/layout-v33/glance_check_box_end_bottom.xml
res/layout-v33/glance_check_box_end_center_vertical.xml
res/layout-v33/glance_check_box_end_top.xml
res/layout-v33/glance_check_box_expandwidth_wrapheight.xml
res/layout-v33/glance_check_box_start_bottom.xml
res/layout-v33/glance_check_box_start_center_vertical.xml
res/layout-v33/glance_check_box_start_top.xml
res/layout-v33/glance_check_box_wrapwidth_expandheight.xml
res/layout/glance_check_box.xml
```

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<CheckBox xmlns:android="http://schemas.android.com/apk/res/android" android:tag="glanceCompoundButton" android:layout_width="wrap_content" android:layout_height="wrap_content" android:textDirection="locale" style="@style/Glance.AppWidget.CheckBox"/>
```
