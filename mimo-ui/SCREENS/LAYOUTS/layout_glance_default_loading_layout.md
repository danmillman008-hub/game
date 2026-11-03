# پروندهٔ لایه — `res/layout/glance_default_loading_layout.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/glance_default_loading_layout.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/glance_default_loading_layout.xml`](../../SOURCE/res/layout/glance_default_loading_layout.xml) |
| SHA-256 دیکد | `097bd4f5396ecd434ba71dcbca3572f01339dbaffab967b18e102d5a313a0e2e` |
| ریشه | `FrameLayout` |
| تعداد گره | 2 |
| تعداد شناسه | 0 |
| تگ‌های استفاده‌شده | 2 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 1 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ FrameLayout
   └─ ProgressBar
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `FrameLayout` | `android:layout_width` | `match_parent` |
| 2 | `FrameLayout` | `android:layout_height` | `match_parent` |
| 3 | `FrameLayout` | `style` | `@style/Glance.AppWidget.Background.Loading` |
| 4 | `ProgressBar` | `android:layout_gravity` | `0x00000011` |
| 5 | `ProgressBar` | `android:layout_width` | `wrap_content` |
| 6 | `ProgressBar` | `android:layout_height` | `wrap_content` |
| 7 | `ProgressBar` | `android:indeterminate` | `true` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@style/Glance.AppWidget.Background.Loading` | `[{'attr': 'android:background', 'attr_id': '0x010100D4', 'value': '@drawable/glance_loading_layout_background', 'value_type': 'reference'}]` |

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
<FrameLayout xmlns:android="http://schemas.android.com/apk/res/android" android:layout_width="match_parent" android:layout_height="match_parent" style="@style/Glance.AppWidget.Background.Loading">
  <ProgressBar android:layout_gravity="0x00000011" android:layout_width="wrap_content" android:layout_height="wrap_content" android:indeterminate="true"/>
</FrameLayout>
```
