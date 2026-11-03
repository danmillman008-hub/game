# پروندهٔ لایه — `res/layout/codeheader_plural_code_tabview.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/codeheader_plural_code_tabview.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/codeheader_plural_code_tabview.xml`](../../SOURCE/res/layout/codeheader_plural_code_tabview.xml) |
| SHA-256 دیکد | `2ade2ec60aec918d1247498920fefa783d6eadc531860ecd1e243b41f481b9e1` |
| ریشه | `LinearLayout` |
| تعداد گره | 3 |
| تعداد شناسه | 2 |
| تگ‌های استفاده‌شده | 3 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 7 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ LinearLayout
   ├─ TextView  #@id/tv_codeeditor_tab_title
   └─ ImageView  #@id/iv_codeeditor_tab_indicator_edited
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `LinearLayout` | `android:gravity` | `0x00800003` |
| 2 | `LinearLayout` | `android:orientation` | `horizontal` |
| 3 | `LinearLayout` | `android:layout_width` | `match_parent` |
| 4 | `LinearLayout` | `android:layout_height` | `match_parent` |
| 5 | `LinearLayout` | `android:paddingStart` | `@dimen/code_view_tab_padding_horizontal` |
| 6 | `LinearLayout` | `android:paddingEnd` | `@dimen/code_view_tab_padding_horizontal` |
| 7 | `TextView` | `android:textAppearance` | `@style/TextCodeEditorTitleWithMultipleTabs` |
| 8 | `TextView` | `android:layout_gravity` | `0x00800013` |
| 9 | `TextView` | `android:id` | `@id/tv_codeeditor_tab_title` |
| 10 | `TextView` | `android:paddingTop` | `@dimen/lesson_tablayout_padding_vertical` |
| 11 | `TextView` | `android:paddingBottom` | `@dimen/lesson_tablayout_padding_vertical` |
| 12 | `TextView` | `android:layout_width` | `wrap_content` |
| 13 | `TextView` | `android:layout_height` | `wrap_content` |
| 14 | `ImageView` | `android:layout_gravity` | `0x00000011` |
| 15 | `ImageView` | `android:id` | `@id/iv_codeeditor_tab_indicator_edited` |
| 16 | `ImageView` | `android:visibility` | `gone` |
| 17 | `ImageView` | `android:layout_width` | `wrap_content` |
| 18 | `ImageView` | `android:layout_height` | `wrap_content` |
| 19 | `ImageView` | `android:layout_marginStart` | `6.000000dip` |
| 20 | `ImageView` | `app:srcCompat` | `@drawable/indicator_selected` |
| 21 | `ImageView` | `app:tint` | `@color/support_green` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/support_green` | `#FF66BC5A` / `#FF78D86B` (night) |
| `@dimen/code_view_tab_padding_horizontal` | `@dimen/spacing_s_expandable` |
| `@dimen/lesson_tablayout_padding_vertical` | `10.000000dip` / `12.000000dip` (sw600dp) |
| `@style/TextCodeEditorTitleWithMultipleTabs` | `[{'attr': 'android:textColor', 'attr_id': '0x01010098', 'value': '@color/codeeditor_tab_color', 'value_type': 'reference'}]` |

## ۴. شناسه‌های `@id`

```text
@id/iv_codeeditor_tab_indicator_edited
@id/tv_codeeditor_tab_title
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
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android" xmlns:app="http://schemas.android.com/apk/res-auto" android:gravity="0x00800003" android:orientation="horizontal" android:layout_width="match_parent" android:layout_height="match_parent" android:paddingStart="@dimen/code_view_tab_padding_horizontal" android:paddingEnd="@dimen/code_view_tab_padding_horizontal">
  <TextView android:textAppearance="@style/TextCodeEditorTitleWithMultipleTabs" android:layout_gravity="0x00800013" android:id="@id/tv_codeeditor_tab_title" android:paddingTop="@dimen/lesson_tablayout_padding_vertical" android:paddingBottom="@dimen/lesson_tablayout_padding_vertical" android:layout_width="wrap_content" android:layout_height="wrap_content"/>
  <ImageView android:layout_gravity="0x00000011" android:id="@id/iv_codeeditor_tab_indicator_edited" android:visibility="gone" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginStart="6.000000dip" app:srcCompat="@drawable/indicator_selected" app:tint="@color/support_green"/>
</LinearLayout>
```
