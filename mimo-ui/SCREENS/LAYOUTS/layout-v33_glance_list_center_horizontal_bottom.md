# پروندهٔ لایه — `res/layout-v33/glance_list_center_horizontal_bottom.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout-v33/glance_list_center_horizontal_bottom.xml` |
| فایل دیکدشده | [`SOURCE/res/layout-v33/glance_list_center_horizontal_bottom.xml`](../../SOURCE/res/layout-v33/glance_list_center_horizontal_bottom.xml) |
| SHA-256 دیکد | `a739107b0121152e733a64fb6a1b1ab39f82431595cb5282175aa2936777e38e` |
| ریشه | `ListView` |
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
└─ ListView  #@id/glanceView
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `ListView` | `android:theme` | `@style/Glance.AppWidget.Theme.ListChildren` |
| 2 | `ListView` | `android:layout_gravity` | `0x00000051` |
| 3 | `ListView` | `android:id` | `@id/glanceView` |
| 4 | `ListView` | `android:layout_width` | `wrap_content` |
| 5 | `ListView` | `android:layout_height` | `wrap_content` |
| 6 | `ListView` | `android:listSelector` | `@0x0106000D` |
| 7 | `ListView` | `android:divider` | `@null` |
| 8 | `ListView` | `android:layoutDirection` | `locale` |
| 9 | `ListView` | `app:glance_isTopLevelLayout` | `true` |
| 10 | `ListView` | `style` | `@style/Glance.AppWidget.List` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@style/Glance.AppWidget.List` | `[]` |
| `@style/Glance.AppWidget.Theme.ListChildren` | `[]` |

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
<ListView xmlns:app="http://schemas.android.com/apk/res-auto" xmlns:android="http://schemas.android.com/apk/res/android" android:theme="@style/Glance.AppWidget.Theme.ListChildren" android:layout_gravity="0x00000051" android:id="@id/glanceView" android:layout_width="wrap_content" android:layout_height="wrap_content" android:listSelector="@0x0106000D" android:divider="@null" android:layoutDirection="locale" app:glance_isTopLevelLayout="true" style="@style/Glance.AppWidget.List"/>
```
