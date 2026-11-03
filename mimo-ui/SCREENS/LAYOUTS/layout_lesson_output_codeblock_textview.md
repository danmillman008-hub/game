# پروندهٔ لایه — `res/layout/lesson_output_codeblock_textview.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/lesson_output_codeblock_textview.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/lesson_output_codeblock_textview.xml`](../../SOURCE/res/layout/lesson_output_codeblock_textview.xml) |
| SHA-256 دیکد | `b76dd12f31276e0e5aacbda8e8ea8482e3c7f3659aa939bec6aa2cf7d8b67da6` |
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
└─ TextView  #@id/tv_lesson_output_codeblock
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `TextView` | `android:id` | `@id/tv_lesson_output_codeblock` |
| 2 | `TextView` | `android:background` | `@drawable/code_background_corners_all` |
| 3 | `TextView` | `android:paddingTop` | `@dimen/lesson_codeview_padding_top` |
| 4 | `TextView` | `android:paddingBottom` | `@dimen/lesson_codeview_padding_bottom` |
| 5 | `TextView` | `android:layout_width` | `match_parent` |
| 6 | `TextView` | `android:layout_height` | `wrap_content` |
| 7 | `TextView` | `style` | `@style/TextLessonCode` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@dimen/lesson_codeview_padding_bottom` | `@dimen/spacing_s_expandable` |
| `@dimen/lesson_codeview_padding_top` | `@dimen/spacing_xs_expandable` |
| `@style/TextLessonCode` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '14.000000sp', 'value_type': 'dimension'}, {'attr': 'android:textColor', 'attr_id': '0x01010098', 'value': '@color/code_primary', 'value_type': 'reference'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '@dimen/code_line_spacing', 'value_type': 'reference'}, {'attr': 'android:fontFamily', 'attr_id': '0x010103AC', 'value': '@font/aeonik_mono', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '18.000000sp', 'value_type': 'dimension'}, {'attr': 'android:textColor', 'attr_id': '0x01010098', 'value': '@color/code_primary', 'value_type': 'reference'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '@dimen/code_line_spacing', 'value_type': 'reference'}, {'attr': 'android:fontFamily', 'attr_id': '0x010103AC', 'value': '@font/aeonik_mono', 'value_type': 'reference'}]` (sw600dp) |

## ۴. شناسه‌های `@id`

```text
@id/tv_lesson_output_codeblock
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
<TextView xmlns:android="http://schemas.android.com/apk/res/android" android:id="@id/tv_lesson_output_codeblock" android:background="@drawable/code_background_corners_all" android:paddingTop="@dimen/lesson_codeview_padding_top" android:paddingBottom="@dimen/lesson_codeview_padding_bottom" android:layout_width="match_parent" android:layout_height="wrap_content" style="@style/TextLessonCode"/>
```
