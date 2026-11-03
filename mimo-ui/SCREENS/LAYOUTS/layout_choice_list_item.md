# پروندهٔ لایه — `res/layout/choice_list_item.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/choice_list_item.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/choice_list_item.xml`](../../SOURCE/res/layout/choice_list_item.xml) |
| SHA-256 دیکد | `37e454bea1c679dc2a857bd988ed3a7adfb8fb78cfd83db4ddb9be1f2916895c` |
| ریشه | `TextView` |
| تعداد گره | 1 |
| تعداد شناسه | 0 |
| تگ‌های استفاده‌شده | 1 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 8 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ TextView
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `TextView` | `android:textColor` | `@color/text_primary` |
| 2 | `TextView` | `android:gravity` | `0x00000010` |
| 3 | `TextView` | `android:background` | `@drawable/multiplechoice_background_unselected` |
| 4 | `TextView` | `android:layout_width` | `match_parent` |
| 5 | `TextView` | `android:layout_height` | `wrap_content` |
| 6 | `TextView` | `android:layout_margin` | `@dimen/spacing_xxs` |
| 7 | `TextView` | `android:layout_marginTop` | `@dimen/spacing_s` |
| 8 | `TextView` | `android:foreground` | `?attr/selectableItemBackground` |
| 9 | `TextView` | `android:minHeight` | `48.000000dip` |
| 10 | `TextView` | `android:elevation` | `@dimen/multiplechoice_elevation` |
| 11 | `TextView` | `android:paddingHorizontal` | `@dimen/spacing_m` |
| 12 | `TextView` | `android:paddingVertical` | `@dimen/spacing_s` |
| 13 | `TextView` | `style` | `@style/TextP1` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/text_primary` | `#FF252746` / `#FFFFFFFF` (night) |
| `@dimen/multiplechoice_elevation` | `1.000000dip` |
| `@dimen/spacing_m` | `16.000000dip` |
| `@dimen/spacing_s` | `12.000000dip` |
| `@dimen/spacing_xxs` | `4.000000dip` |
| `@style/TextP1` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '18.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '5.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '23.399996sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '7.799988sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` (sw600dp) |

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
<TextView xmlns:android="http://schemas.android.com/apk/res/android" android:textColor="@color/text_primary" android:gravity="0x00000010" android:background="@drawable/multiplechoice_background_unselected" android:layout_width="match_parent" android:layout_height="wrap_content" android:layout_margin="@dimen/spacing_xxs" android:layout_marginTop="@dimen/spacing_s" android:foreground="?attr/selectableItemBackground" android:minHeight="48.000000dip" android:elevation="@dimen/multiplechoice_elevation" android:paddingHorizontal="@dimen/spacing_m" android:paddingVertical="@dimen/spacing_s" style="@style/TextP1"/>
```
