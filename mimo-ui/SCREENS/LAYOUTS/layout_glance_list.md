# پروندهٔ لایه — `res/layout/glance_list.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/glance_list.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/glance_list.xml`](../../SOURCE/res/layout/glance_list.xml) |
| SHA-256 دیکد | `34704b8b269ca097c2e11288634032da08094a92d0937da50acacd209b192343` |
| ریشه | `ListView` |
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
└─ ListView
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `ListView` | `android:theme` | `@style/Glance.AppWidget.Theme.ListChildren` |
| 2 | `ListView` | `android:layout_width` | `wrap_content` |
| 3 | `ListView` | `android:layout_height` | `wrap_content` |
| 4 | `ListView` | `android:listSelector` | `@0x0106000D` |
| 5 | `ListView` | `android:divider` | `@null` |
| 6 | `ListView` | `app:glance_isTopLevelLayout` | `true` |
| 7 | `ListView` | `style` | `@style/Glance.AppWidget.List` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@style/Glance.AppWidget.List` | `[]` |
| `@style/Glance.AppWidget.Theme.ListChildren` | `[]` |

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
<ListView xmlns:android="http://schemas.android.com/apk/res/android" xmlns:app="http://schemas.android.com/apk/res-auto" android:theme="@style/Glance.AppWidget.Theme.ListChildren" android:layout_width="wrap_content" android:layout_height="wrap_content" android:listSelector="@0x0106000D" android:divider="@null" app:glance_isTopLevelLayout="true" style="@style/Glance.AppWidget.List"/>
```
