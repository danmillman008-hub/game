# پروندهٔ لایه — `res/layout/glance_check_box_text.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/glance_check_box_text.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/glance_check_box_text.xml`](../../SOURCE/res/layout/glance_check_box_text.xml) |
| SHA-256 دیکد | `80ca96087c4bb2b4099ef6200762262db2c85d0fb6e05144f9eec304349ce340` |
| ریشه | `TextView` |
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
└─ TextView
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `TextView` | `android:layout_width` | `wrap_content` |
| 2 | `TextView` | `android:layout_height` | `wrap_content` |
| 3 | `TextView` | `android:textDirection` | `locale` |
| 4 | `TextView` | `style` | `@style/Glance.AppWidget.CheckBoxText` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@style/Glance.AppWidget.CheckBoxText` | `[]` |

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
res/layout-v33/glance_check_box_backport_center_horizontal_bottom.xml
res/layout-v33/glance_check_box_backport_center_horizontal_center_vertical.xml
res/layout-v33/glance_check_box_backport_center_horizontal_top.xml
res/layout-v33/glance_check_box_backport_end_bottom.xml
res/layout-v33/glance_check_box_backport_end_center_vertical.xml
res/layout-v33/glance_check_box_backport_end_top.xml
res/layout-v33/glance_check_box_backport_expandwidth_wrapheight.xml
res/layout-v33/glance_check_box_backport_start_bottom.xml
res/layout-v33/glance_check_box_backport_start_center_vertical.xml
res/layout-v33/glance_check_box_backport_start_top.xml
res/layout-v33/glance_check_box_backport_wrapwidth_expandheight.xml
res/layout/glance_check_box_backport.xml
```

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<TextView xmlns:android="http://schemas.android.com/apk/res/android" android:layout_width="wrap_content" android:layout_height="wrap_content" android:textDirection="locale" style="@style/Glance.AppWidget.CheckBoxText"/>
```
