# پروندهٔ لایه — `res/layout/lesson_interactive_output_console.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/lesson_interactive_output_console.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/lesson_interactive_output_console.xml`](../../SOURCE/res/layout/lesson_interactive_output_console.xml) |
| SHA-256 دیکد | `8f4795866ac70ccfff5c8cb3af905949d415a1791188e0b130f29319c0595431` |
| ریشه | `LinearLayout` |
| تعداد گره | 4 |
| تعداد شناسه | 3 |
| تگ‌های استفاده‌شده | 3 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 14 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ LinearLayout
   ├─ TextView  #@id/tv_lesson_output_title
   ├─ View  #@id/view_separator
   └─ TextView  #@id/tv_lesson_console
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `LinearLayout` | `android:orientation` | `vertical` |
| 2 | `LinearLayout` | `android:background` | `@color/background_primary` |
| 3 | `LinearLayout` | `android:layout_width` | `match_parent` |
| 4 | `LinearLayout` | `android:layout_height` | `wrap_content` |
| 5 | `LinearLayout` | `android:layout_marginBottom` | `8.000000dip` |
| 6 | `LinearLayout` | `android:layout_marginStart` | `@dimen/lesson_codeview_margin_start` |
| 7 | `LinearLayout` | `android:layout_marginEnd` | `@dimen/lesson_codeview_margin_end` |
| 8 | `TextView` | `android:textColor` | `@color/text_weak` |
| 9 | `TextView` | `android:id` | `@id/tv_lesson_output_title` |
| 10 | `TextView` | `android:layout_width` | `match_parent` |
| 11 | `TextView` | `android:layout_height` | `wrap_content` |
| 12 | `TextView` | `android:layout_margin` | `@dimen/spacing_m` |
| 13 | `TextView` | `android:text` | `@string/codeplayground_result_header_output` |
| 14 | `TextView` | `style` | `@style/TextTitle3` |
| 15 | `View` | `android:id` | `@id/view_separator` |
| 16 | `View` | `android:background` | `@color/line_secondary` |
| 17 | `View` | `android:layout_width` | `match_parent` |
| 18 | `View` | `android:layout_height` | `1.000000dip` |
| 19 | `TextView` | `android:id` | `@id/tv_lesson_console` |
| 20 | `TextView` | `android:paddingTop` | `@dimen/spacing_xs_expandable` |
| 21 | `TextView` | `android:paddingBottom` | `@dimen/spacing_m_expandable` |
| 22 | `TextView` | `android:visibility` | `gone` |
| 23 | `TextView` | `android:layout_width` | `match_parent` |
| 24 | `TextView` | `android:layout_height` | `wrap_content` |
| 25 | `TextView` | `style` | `@style/TextConsole` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/background_primary` | `#FFF6F7FB` / `#FF252746` (night) |
| `@color/line_secondary` | `#FFE4E6F1` / `#FF4A4D85` (night) |
| `@color/text_weak` | `#FF4A4D85` / `#CCFFFFFF` (night) |
| `@dimen/lesson_codeview_margin_end` | `0.000000dip` |
| `@dimen/lesson_codeview_margin_start` | `0.000000dip` |
| `@dimen/spacing_m` | `16.000000dip` |
| `@dimen/spacing_m_expandable` | `16.000000dip` / `24.000000dip` (sw600dp) |
| `@dimen/spacing_xs_expandable` | `8.000000dip` / `12.000000dip` (sw600dp) |
| `@string/codeplayground_result_header_output` | `Output` / `Ausgabe` (de) / `Output` (es) / `Résultat` (fr) / `Output` (in) / `Output` (it) / `Wynik` (pl) / `Saída` (pt-rBR) / `Результат` (ru) / `Çıktı` (tr) |
| `@style/TextConsole` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '15.000000sp', 'value_type': 'dimension'}, {'attr': 'android:typeface', 'attr_id': '0x01010096', 'value': '3', 'value_type': 'int_dec'}, {'attr': 'android:textColor', 'attr_id': '0x01010098', 'value': '@color/code_primary', 'value_type': 'reference'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '@dimen/code_line_spacing', 'value_type': 'reference'}, {'attr': 'android:fontFamily', 'attr_id': '0x010103AC', 'value': '@font/aeonik_mono', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '18.000000sp', 'value_type': 'dimension'}, {'attr': 'android:typeface', 'attr_id': '0x01010096', 'value': '3', 'value_type': 'int_dec'}, {'attr': 'android:textColor', 'attr_id': '0x01010098', 'value': '@color/code_primary', 'value_type': 'reference'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '@dimen/code_line_spacing', 'value_type': 'reference'}, {'attr': 'android:fontFamily', 'attr_id': '0x010103AC', 'value': '@font/aeonik_mono', 'value_type': 'reference'}]` (sw600dp) |
| `@style/TextTitle3` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '12.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '3.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_medium', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '15.599977sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '7.799988sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_medium', 'value_type': 'reference'}]` (sw600dp) |

## ۴. شناسه‌های `@id`

```text
@id/tv_lesson_console
@id/tv_lesson_output_title
@id/view_separator
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
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android" android:orientation="vertical" android:background="@color/background_primary" android:layout_width="match_parent" android:layout_height="wrap_content" android:layout_marginBottom="8.000000dip" android:layout_marginStart="@dimen/lesson_codeview_margin_start" android:layout_marginEnd="@dimen/lesson_codeview_margin_end">
  <TextView android:textColor="@color/text_weak" android:id="@id/tv_lesson_output_title" android:layout_width="match_parent" android:layout_height="wrap_content" android:layout_margin="@dimen/spacing_m" android:text="@string/codeplayground_result_header_output" style="@style/TextTitle3"/>
  <View android:id="@id/view_separator" android:background="@color/line_secondary" android:layout_width="match_parent" android:layout_height="1.000000dip"/>
  <TextView android:id="@id/tv_lesson_console" android:paddingTop="@dimen/spacing_xs_expandable" android:paddingBottom="@dimen/spacing_m_expandable" android:visibility="gone" android:layout_width="match_parent" android:layout_height="wrap_content" style="@style/TextConsole"/>
</LinearLayout>
```
