# پروندهٔ لایه — `res/layout/glance_button.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/glance_button.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/glance_button.xml`](../../SOURCE/res/layout/glance_button.xml) |
| SHA-256 دیکد | `e96bac6a48aedb2dd6e1a5f4ce0edc252ec44936a4526bf6c2a9438deb2e413f` |
| ریشه | `Button` |
| تعداد گره | 1 |
| تعداد شناسه | 0 |
| تگ‌های استفاده‌شده | 1 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 3 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ Button
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `Button` | `android:layout_width` | `wrap_content` |
| 2 | `Button` | `android:layout_height` | `wrap_content` |
| 3 | `Button` | `android:foreground` | `@drawable/glance_button_ripple` |
| 4 | `Button` | `android:minWidth` | `0.000000dip` |
| 5 | `Button` | `android:minHeight` | `0.000000dip` |
| 6 | `Button` | `android:stateListAnimator` | `@null` |
| 7 | `Button` | `app:glance_isTopLevelLayout` | `true` |
| 8 | `Button` | `style` | `@style/Glance.AppWidget.Button` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@style/Glance.AppWidget.Button` | `[]` |

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
<Button xmlns:app="http://schemas.android.com/apk/res-auto" xmlns:android="http://schemas.android.com/apk/res/android" android:layout_width="wrap_content" android:layout_height="wrap_content" android:foreground="@drawable/glance_button_ripple" android:minWidth="0.000000dip" android:minHeight="0.000000dip" android:stateListAnimator="@null" app:glance_isTopLevelLayout="true" style="@style/Glance.AppWidget.Button"/>
```
