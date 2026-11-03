# پروندهٔ لایه — `res/layout/m3_navigation_menu_subheader.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/m3_navigation_menu_subheader.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/m3_navigation_menu_subheader.xml`](../../SOURCE/res/layout/m3_navigation_menu_subheader.xml) |
| SHA-256 دیکد | `25461ef2aa825f77d0a3279bb6813743a5204cc6a34c4e0741f30c937e2890e0` |
| ریشه | `TextView` |
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
└─ TextView  #@id/navigation_menu_subheader_label
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `TextView` | `android:ellipsize` | `end` |
| 2 | `TextView` | `android:gravity` | `0x00800013` |
| 3 | `TextView` | `android:id` | `@id/navigation_menu_subheader_label` |
| 4 | `TextView` | `android:layout_width` | `match_parent` |
| 5 | `TextView` | `android:layout_height` | `wrap_content` |
| 6 | `TextView` | `android:layout_marginTop` | `@dimen/m3_navigation_subheader_top_margin` |
| 7 | `TextView` | `android:maxLines` | `1` |
| 8 | `TextView` | `android:filterTouchesWhenObscured` | `true` |
| 9 | `TextView` | `android:layout_marginStart` | `@dimen/m3_navigation_content_horizontal_margin` |
| 10 | `TextView` | `android:paddingHorizontal` | `@dimen/m3_navigation_subheader_horizontal_padding` |
| 11 | `TextView` | `android:paddingVertical` | `@dimen/m3_navigation_subheader_vertical_padding` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@dimen/m3_navigation_content_horizontal_margin` | `20.000000dip` |
| `@dimen/m3_navigation_subheader_horizontal_padding` | `16.000000dip` |
| `@dimen/m3_navigation_subheader_top_margin` | `12.000000dip` |
| `@dimen/m3_navigation_subheader_vertical_padding` | `8.000000dip` |

## ۴. شناسه‌های `@id`

```text
@id/navigation_menu_subheader_label
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
<TextView xmlns:android="http://schemas.android.com/apk/res/android" android:ellipsize="end" android:gravity="0x00800013" android:id="@id/navigation_menu_subheader_label" android:layout_width="match_parent" android:layout_height="wrap_content" android:layout_marginTop="@dimen/m3_navigation_subheader_top_margin" android:maxLines="1" android:filterTouchesWhenObscured="true" android:layout_marginStart="@dimen/m3_navigation_content_horizontal_margin" android:paddingHorizontal="@dimen/m3_navigation_subheader_horizontal_padding" android:paddingVertical="@dimen/m3_navigation_subheader_vertical_padding"/>
```
