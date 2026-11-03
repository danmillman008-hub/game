# پروندهٔ لایه — `res/layout/glance_radio_icon.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/glance_radio_icon.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/glance_radio_icon.xml`](../../SOURCE/res/layout/glance_radio_icon.xml) |
| SHA-256 دیکد | `81209d39e18f343f07ae20fd610ca832ce30a7e6664116beb07c3535c8a37b97` |
| ریشه | `ImageView` |
| تعداد گره | 1 |
| تعداد شناسه | 0 |
| تگ‌های استفاده‌شده | 1 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 2 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ ImageView
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `ImageView` | `android:layout_width` | `32.000000dip` |
| 2 | `ImageView` | `android:layout_height` | `32.000000dip` |
| 3 | `ImageView` | `android:src` | `@drawable/glance_btn_radio_material_anim` |
| 4 | `ImageView` | `android:layout_centerVertical` | `true` |
| 5 | `ImageView` | `style` | `@style/Glance.AppWidget.RadioButtonIcon` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@style/Glance.AppWidget.RadioButtonIcon` | `[]` |

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
res/layout-v33/glance_radio_button_backport_center_horizontal_bottom.xml
res/layout-v33/glance_radio_button_backport_center_horizontal_center_vertical.xml
res/layout-v33/glance_radio_button_backport_center_horizontal_top.xml
res/layout-v33/glance_radio_button_backport_end_bottom.xml
res/layout-v33/glance_radio_button_backport_end_center_vertical.xml
res/layout-v33/glance_radio_button_backport_end_top.xml
res/layout-v33/glance_radio_button_backport_expandwidth_wrapheight.xml
res/layout-v33/glance_radio_button_backport_start_bottom.xml
res/layout-v33/glance_radio_button_backport_start_center_vertical.xml
res/layout-v33/glance_radio_button_backport_start_top.xml
res/layout-v33/glance_radio_button_backport_wrapwidth_expandheight.xml
res/layout/glance_radio_button_backport.xml
```

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<ImageView xmlns:android="http://schemas.android.com/apk/res/android" android:layout_width="32.000000dip" android:layout_height="32.000000dip" android:src="@drawable/glance_btn_radio_material_anim" android:layout_centerVertical="true" style="@style/Glance.AppWidget.RadioButtonIcon"/>
```
