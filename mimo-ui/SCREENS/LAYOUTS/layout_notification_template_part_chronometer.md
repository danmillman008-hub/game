# پروندهٔ لایه — `res/layout/notification_template_part_chronometer.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/notification_template_part_chronometer.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/notification_template_part_chronometer.xml`](../../SOURCE/res/layout/notification_template_part_chronometer.xml) |
| SHA-256 دیکد | `9a0158205eae58d6a8abc3abbe5cbdd80444f3ad55df0df358cfece3c0949f4a` |
| ریشه | `Chronometer` |
| تعداد گره | 1 |
| تعداد شناسه | 1 |
| تگ‌های استفاده‌شده | 1 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 2 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ Chronometer  #@id/chronometer
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `Chronometer` | `android:textAppearance` | `@style/TextAppearance.Compat.Notification.Time` |
| 2 | `Chronometer` | `android:id` | `@id/chronometer` |
| 3 | `Chronometer` | `android:layout_width` | `wrap_content` |
| 4 | `Chronometer` | `android:layout_height` | `wrap_content` |
| 5 | `Chronometer` | `android:singleLine` | `true` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@style/TextAppearance.Compat.Notification.Time` | `[]` |

## ۴. شناسه‌های `@id`

```text
@id/chronometer
```

## ۵. ارجاع به لایه‌های دیگر

```text
(none)
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

(هیچ صفحهٔ نام‌برداری به این لایه متصل نشد؛ ممکن است لایهٔ کتابخانه/`<include>` باشد)

## ۷. لایه‌هایی که این لایه را include می‌کنند

```text
res/layout/notification_template_custom_big.xml
```

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<Chronometer xmlns:android="http://schemas.android.com/apk/res/android" android:textAppearance="@style/TextAppearance.Compat.Notification.Time" android:id="@id/chronometer" android:layout_width="wrap_content" android:layout_height="wrap_content" android:singleLine="true"/>
```
