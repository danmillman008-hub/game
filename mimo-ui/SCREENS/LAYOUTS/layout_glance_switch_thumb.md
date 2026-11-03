# پروندهٔ لایه — `res/layout/glance_switch_thumb.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/glance_switch_thumb.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/glance_switch_thumb.xml`](../../SOURCE/res/layout/glance_switch_thumb.xml) |
| SHA-256 دیکد | `a022164663aaa360c5197e42cf43eb61356472cc676134e83a0313fbf085ec66` |
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
| 1 | `ImageView` | `android:layout_gravity` | `0x00800013` |
| 2 | `ImageView` | `android:layout_width` | `wrap_content` |
| 3 | `ImageView` | `android:layout_height` | `wrap_content` |
| 4 | `ImageView` | `android:src` | `@drawable/glance_switch_thumb_animated` |
| 5 | `ImageView` | `style` | `@style/Glance.AppWidget.SwitchThumb` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@style/Glance.AppWidget.SwitchThumb` | `[]` |

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
res/layout-v33/glance_swtch_backport_center_horizontal_bottom.xml
res/layout-v33/glance_swtch_backport_center_horizontal_center_vertical.xml
res/layout-v33/glance_swtch_backport_center_horizontal_top.xml
res/layout-v33/glance_swtch_backport_end_bottom.xml
res/layout-v33/glance_swtch_backport_end_center_vertical.xml
res/layout-v33/glance_swtch_backport_end_top.xml
res/layout-v33/glance_swtch_backport_expandwidth_wrapheight.xml
res/layout-v33/glance_swtch_backport_start_bottom.xml
res/layout-v33/glance_swtch_backport_start_center_vertical.xml
res/layout-v33/glance_swtch_backport_start_top.xml
res/layout-v33/glance_swtch_backport_wrapwidth_expandheight.xml
res/layout/glance_swtch_backport.xml
```

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<ImageView xmlns:android="http://schemas.android.com/apk/res/android" android:layout_gravity="0x00800013" android:layout_width="wrap_content" android:layout_height="wrap_content" android:src="@drawable/glance_switch_thumb_animated" style="@style/Glance.AppWidget.SwitchThumb"/>
```
