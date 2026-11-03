# پروندهٔ لایه — `res/layout/coding_keyboard_item.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/coding_keyboard_item.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/coding_keyboard_item.xml`](../../SOURCE/res/layout/coding_keyboard_item.xml) |
| SHA-256 دیکد | `2d7c1b9990a6146e4f4afdccba9ed03a738ddab7eb52c39baebba7d9c902c459` |
| ریشه | `FrameLayout` |
| تعداد گره | 3 |
| تعداد شناسه | 1 |
| تگ‌های استفاده‌شده | 3 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 8 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ FrameLayout
   ├─ TextView  #@id/tv_coding_snippet_view
   └─ View
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `FrameLayout` | `android:layout_width` | `@dimen/coding_keyboard_snippet_width` |
| 2 | `FrameLayout` | `android:layout_height` | `@dimen/coding_keyboard_snippet_height` |
| 3 | `FrameLayout` | `android:foreground` | `?attr/selectableItemBackground` |
| 4 | `FrameLayout` | `android:hapticFeedbackEnabled` | `true` |
| 5 | `TextView` | `android:textColor` | `@color/text_weak` |
| 6 | `TextView` | `android:gravity` | `0x00000011` |
| 7 | `TextView` | `android:layout_gravity` | `0x00000011` |
| 8 | `TextView` | `android:id` | `@id/tv_coding_snippet_view` |
| 9 | `TextView` | `android:layout_width` | `wrap_content` |
| 10 | `TextView` | `android:layout_height` | `wrap_content` |
| 11 | `TextView` | `style` | `@style/TextCode1` |
| 12 | `View` | `android:layout_gravity` | `0x00800005` |
| 13 | `View` | `android:background` | `@color/line_primary` |
| 14 | `View` | `android:layout_width` | `1.000000dip` |
| 15 | `View` | `android:layout_height` | `match_parent` |
| 16 | `View` | `android:layout_marginVertical` | `@dimen/spacing_xs` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/line_primary` | `#FFEDEEF6` / `#FF3F4273` (night) |
| `@color/text_weak` | `#FF4A4D85` / `#CCFFFFFF` (night) |
| `@dimen/coding_keyboard_snippet_height` | `44.000000dip` |
| `@dimen/coding_keyboard_snippet_width` | `42.000000dip` |
| `@dimen/spacing_xs` | `8.000000dip` |
| `@style/TextCode1` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '16.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '6.000000dip', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_mono', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '20.799990sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '10.399995dip', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_mono', 'value_type': 'reference'}]` (sw600dp) |

## ۴. شناسه‌های `@id`

```text
@id/tv_coding_snippet_view
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
<FrameLayout xmlns:android="http://schemas.android.com/apk/res/android" android:layout_width="@dimen/coding_keyboard_snippet_width" android:layout_height="@dimen/coding_keyboard_snippet_height" android:foreground="?attr/selectableItemBackground" android:hapticFeedbackEnabled="true">
  <TextView android:textColor="@color/text_weak" android:gravity="0x00000011" android:layout_gravity="0x00000011" android:id="@id/tv_coding_snippet_view" android:layout_width="wrap_content" android:layout_height="wrap_content" style="@style/TextCode1"/>
  <View android:layout_gravity="0x00800005" android:background="@color/line_primary" android:layout_width="1.000000dip" android:layout_height="match_parent" android:layout_marginVertical="@dimen/spacing_xs"/>
</FrameLayout>
```
