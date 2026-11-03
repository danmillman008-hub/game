# پروندهٔ لایه — `res/layout/design_navigation_item_header.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/design_navigation_item_header.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/design_navigation_item_header.xml`](../../SOURCE/res/layout/design_navigation_item_header.xml) |
| SHA-256 دیکد | `9ad22b6c8c932ff7f586393587088f000aa31355d2beb38d148d928b63889fe6` |
| ریشه | `LinearLayout` |
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
└─ LinearLayout  #@id/navigation_header_container
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `LinearLayout` | `android:orientation` | `vertical` |
| 2 | `LinearLayout` | `android:id` | `@id/navigation_header_container` |
| 3 | `LinearLayout` | `android:paddingBottom` | `@dimen/design_navigation_separator_vertical_padding` |
| 4 | `LinearLayout` | `android:layout_width` | `match_parent` |
| 5 | `LinearLayout` | `android:layout_height` | `wrap_content` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@dimen/design_navigation_separator_vertical_padding` | `8.000000dip` |

## ۴. شناسه‌های `@id`

```text
@id/navigation_header_container
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
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android" android:orientation="vertical" android:id="@id/navigation_header_container" android:paddingBottom="@dimen/design_navigation_separator_vertical_padding" android:layout_width="match_parent" android:layout_height="wrap_content"/>
```
