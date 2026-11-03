# پروندهٔ لایه — `res/layout/seekbar_with_intervals.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/seekbar_with_intervals.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/seekbar_with_intervals.xml`](../../SOURCE/res/layout/seekbar_with_intervals.xml) |
| SHA-256 دیکد | `2c3ef0074c7798b8a3c7189a72367b838357deabec2ac665abaa7950e72f29db` |
| ریشه | `merge` |
| تعداد گره | 4 |
| تعداد شناسه | 4 |
| تگ‌های استفاده‌شده | 3 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 2 |
| ارجاع به منابع | 6 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ merge  #@id/seekbar_with_intervals
   ├─ LinearLayout  #@id/intervals_text
   ├─ LinearLayout  #@id/intervals_dots
   └─ androidx.appcompat.widget.AppCompatSeekBar  #@id/seekbar
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `merge` | `android:id` | `@id/seekbar_with_intervals` |
| 2 | `merge` | `android:layout_width` | `match_parent` |
| 3 | `merge` | `android:layout_height` | `wrap_content` |
| 4 | `LinearLayout` | `android:orientation` | `horizontal` |
| 5 | `LinearLayout` | `android:id` | `@id/intervals_text` |
| 6 | `LinearLayout` | `android:layout_width` | `match_parent` |
| 7 | `LinearLayout` | `android:layout_height` | `wrap_content` |
| 8 | `LinearLayout` | `app:layout_constraintTop_toTopOf` | `0` |
| 9 | `LinearLayout` | `android:orientation` | `horizontal` |
| 10 | `LinearLayout` | `android:id` | `@id/intervals_dots` |
| 11 | `LinearLayout` | `android:layout_width` | `match_parent` |
| 12 | `LinearLayout` | `android:layout_height` | `wrap_content` |
| 13 | `LinearLayout` | `android:paddingHorizontal` | `@dimen/spacing_xs` |
| 14 | `LinearLayout` | `app:layout_constraintBottom_toBottomOf` | `@id/seekbar` |
| 15 | `LinearLayout` | `app:layout_constraintTop_toTopOf` | `@id/seekbar` |
| 16 | `androidx.appcompat.widget.AppCompatSeekBar` | `android:id` | `@id/seekbar` |
| 17 | `androidx.appcompat.widget.AppCompatSeekBar` | `android:layout_width` | `match_parent` |
| 18 | `androidx.appcompat.widget.AppCompatSeekBar` | `android:layout_height` | `wrap_content` |
| 19 | `androidx.appcompat.widget.AppCompatSeekBar` | `android:layout_marginTop` | `10.000000dip` |
| 20 | `androidx.appcompat.widget.AppCompatSeekBar` | `app:layout_constraintTop_toBottomOf` | `@id/intervals_text` |
| 21 | `androidx.appcompat.widget.AppCompatSeekBar` | `style` | `@style/MySeekBar` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@dimen/spacing_xs` | `8.000000dip` |
| `@style/MySeekBar` | `[{'attr': 'android:paddingLeft', 'attr_id': '0x010100D6', 'value': '20.000000dip', 'value_type': 'dimension'}, {'attr': 'android:paddingRight', 'attr_id': '0x010100D8', 'value': '20.000000dip', 'value_type': 'dimension'}, {'attr': 'android:maxHeight', 'attr_id': '0x01010120', 'value': '8.000000dip', 'value_type': 'dimension'}, {'attr': 'android:indeterminateOnly', 'attr_id': '0x0101013A', 'value': 'false', 'value_type': 'int_boolean'}, {'attr': 'android:indeterminateDrawable', 'attr_id': '0x0101013B', 'value': '@drawable/seekbar_mimo', 'value_type': 'reference'}, {'attr': 'android:progressDrawable', 'attr_id': '0x0101013C', 'value': '@drawable/seekbar_mimo', 'value_type': 'reference'}, {'attr': 'android:minHeight', 'attr_id': '0x01010140', 'value': '8.000000dip', 'value_type': 'dimension'}, {'attr': 'android:thumb', 'attr_id': '0x01010142', 'value': '@drawable/seek_bar_thumb_mimo', 'value_type': 'reference'}]` |

## ۴. شناسه‌های `@id`

```text
@id/intervals_dots
@id/intervals_text
@id/seekbar
@id/seekbar_with_intervals
```

## ۵. ارجاع به لایه‌های دیگر

```text
match_parent
wrap_content
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

(هیچ صفحهٔ نام‌برداری به این لایه متصل نشد؛ ممکن است لایهٔ کتابخانه/`<include>` باشد)

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<merge xmlns:app="http://schemas.android.com/apk/res-auto" xmlns:android="http://schemas.android.com/apk/res/android" android:id="@id/seekbar_with_intervals" android:layout_width="match_parent" android:layout_height="wrap_content">
  <LinearLayout android:orientation="horizontal" android:id="@id/intervals_text" android:layout_width="match_parent" android:layout_height="wrap_content" app:layout_constraintTop_toTopOf="0"/>
  <LinearLayout android:orientation="horizontal" android:id="@id/intervals_dots" android:layout_width="match_parent" android:layout_height="wrap_content" android:paddingHorizontal="@dimen/spacing_xs" app:layout_constraintBottom_toBottomOf="@id/seekbar" app:layout_constraintTop_toTopOf="@id/seekbar"/>
  <androidx.appcompat.widget.AppCompatSeekBar android:id="@id/seekbar" android:layout_width="match_parent" android:layout_height="wrap_content" android:layout_marginTop="10.000000dip" app:layout_constraintTop_toBottomOf="@id/intervals_text" style="@style/MySeekBar"/>
</merge>
```
