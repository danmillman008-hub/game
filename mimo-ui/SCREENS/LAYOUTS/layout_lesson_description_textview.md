# پروندهٔ لایه — `res/layout/lesson_description_textview.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/lesson_description_textview.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/lesson_description_textview.xml`](../../SOURCE/res/layout/lesson_description_textview.xml) |
| SHA-256 دیکد | `e48f8418ef1ac767769f860a7f3cd1e735284dbee352af9ec298b5b98ced5016` |
| ریشه | `TextView` |
| تعداد گره | 1 |
| تعداد شناسه | 0 |
| تگ‌های استفاده‌شده | 1 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 6 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ TextView
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `TextView` | `android:theme` | `@style/TextP2.Selectable` |
| 2 | `TextView` | `android:textColor` | `@color/text_primary` |
| 3 | `TextView` | `android:paddingTop` | `@dimen/lesson_description_margin_top` |
| 4 | `TextView` | `android:paddingBottom` | `@dimen/lesson_description_margin_bottom` |
| 5 | `TextView` | `android:layout_width` | `match_parent` |
| 6 | `TextView` | `android:layout_height` | `wrap_content` |
| 7 | `TextView` | `android:paddingStart` | `@dimen/lesson_description_margin_start` |
| 8 | `TextView` | `android:paddingEnd` | `@dimen/lesson_description_margin_end` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/text_primary` | `#FF252746` / `#FFFFFFFF` (night) |
| `@dimen/lesson_description_margin_bottom` | `8.000000dip` / `30.000000dip` (sw600dp) |
| `@dimen/lesson_description_margin_end` | `16.000000dip` / `0.000000dip` (sw600dp) |
| `@dimen/lesson_description_margin_start` | `16.000000dip` / `0.000000dip` (sw600dp) |
| `@dimen/lesson_description_margin_top` | `8.000000dip` / `30.000000dip` (sw600dp) |
| `@style/TextP2.Selectable` | `[{'attr': 'android:textColorHighlight', 'attr_id': '0x01010099', 'value': '@color/primary_default_alpha_70', 'value_type': 'reference'}, {'attr': 'android:textIsSelectable', 'attr_id': '0x01010316', 'value': 'true', 'value_type': 'int_boolean'}, {'attr': 'attr.colorControlActivated', 'attr_id': '0x7F040120', 'value': '@color/primary_default', 'value_type': 'reference'}]` |

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
<TextView xmlns:android="http://schemas.android.com/apk/res/android" android:theme="@style/TextP2.Selectable" android:textColor="@color/text_primary" android:paddingTop="@dimen/lesson_description_margin_top" android:paddingBottom="@dimen/lesson_description_margin_bottom" android:layout_width="match_parent" android:layout_height="wrap_content" android:paddingStart="@dimen/lesson_description_margin_start" android:paddingEnd="@dimen/lesson_description_margin_end"/>
```
