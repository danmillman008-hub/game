# پروندهٔ لایه — `res/layout/abc_tooltip.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/abc_tooltip.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/abc_tooltip.xml`](../../SOURCE/res/layout/abc_tooltip.xml) |
| SHA-256 دیکد | `dc5ec90ef4ca2cb38b6671d0ec933eaccf687d745fcdf11a4ce872e0facd801d` |
| ریشه | `LinearLayout` |
| تعداد گره | 2 |
| تعداد شناسه | 1 |
| تگ‌های استفاده‌شده | 2 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 7 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ LinearLayout
   └─ TextView  #@id/message
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `LinearLayout` | `android:orientation` | `vertical` |
| 2 | `LinearLayout` | `android:layout_width` | `wrap_content` |
| 3 | `LinearLayout` | `android:layout_height` | `wrap_content` |
| 4 | `TextView` | `android:textAppearance` | `@style/TextAppearance.AppCompat.Tooltip` |
| 5 | `TextView` | `android:textColor` | `?attr/tooltipForegroundColor` |
| 6 | `TextView` | `android:ellipsize` | `end` |
| 7 | `TextView` | `android:id` | `@id/message` |
| 8 | `TextView` | `android:background` | `?attr/tooltipFrameBackground` |
| 9 | `TextView` | `android:paddingLeft` | `@dimen/tooltip_horizontal_padding` |
| 10 | `TextView` | `android:paddingTop` | `@dimen/tooltip_vertical_padding` |
| 11 | `TextView` | `android:paddingRight` | `@dimen/tooltip_horizontal_padding` |
| 12 | `TextView` | `android:paddingBottom` | `@dimen/tooltip_vertical_padding` |
| 13 | `TextView` | `android:layout_width` | `wrap_content` |
| 14 | `TextView` | `android:layout_height` | `wrap_content` |
| 15 | `TextView` | `android:layout_margin` | `@dimen/tooltip_margin` |
| 16 | `TextView` | `android:maxWidth` | `256.000000dip` |
| 17 | `TextView` | `android:maxLines` | `3` |
| 18 | `TextView` | `android:paddingStart` | `@dimen/tooltip_horizontal_padding` |
| 19 | `TextView` | `android:paddingEnd` | `@dimen/tooltip_horizontal_padding` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@dimen/tooltip_horizontal_padding` | `16.000000dip` |
| `@dimen/tooltip_margin` | `8.000000dip` |
| `@dimen/tooltip_vertical_padding` | `6.500001dip` |
| `@style/TextAppearance.AppCompat.Tooltip` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '14.000000sp', 'value_type': 'dimension'}, {'attr': 'android:fontFamily', 'attr_id': '0x010103AC', 'value': 'sans-serif', 'value_type': 'string'}]` |

## ۴. شناسه‌های `@id`

```text
@id/message
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
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android" android:orientation="vertical" android:layout_width="wrap_content" android:layout_height="wrap_content">
  <TextView android:textAppearance="@style/TextAppearance.AppCompat.Tooltip" android:textColor="?attr/tooltipForegroundColor" android:ellipsize="end" android:id="@id/message" android:background="?attr/tooltipFrameBackground" android:paddingLeft="@dimen/tooltip_horizontal_padding" android:paddingTop="@dimen/tooltip_vertical_padding" android:paddingRight="@dimen/tooltip_horizontal_padding" android:paddingBottom="@dimen/tooltip_vertical_padding" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_margin="@dimen/tooltip_margin" android:maxWidth="256.000000dip" android:maxLines="3" android:paddingStart="@dimen/tooltip_horizontal_padding" android:paddingEnd="@dimen/tooltip_horizontal_padding"/>
</LinearLayout>
```
