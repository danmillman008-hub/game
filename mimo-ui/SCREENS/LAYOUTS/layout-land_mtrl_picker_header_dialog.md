# پروندهٔ لایه — `res/layout-land/mtrl_picker_header_dialog.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout-land/mtrl_picker_header_dialog.xml` |
| فایل دیکدشده | [`SOURCE/res/layout-land/mtrl_picker_header_dialog.xml`](../../SOURCE/res/layout-land/mtrl_picker_header_dialog.xml) |
| SHA-256 دیکد | `e1c9f0328696ca00b61b934a55614b8d8ab1b83037d9dc35a7b038614b2175b1` |
| ریشه | `merge` |
| تعداد گره | 8 |
| تعداد شناسه | 5 |
| تگ‌های استفاده‌شده | 7 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 3 |
| ارجاع به منابع | 16 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ merge
   ├─ LinearLayout  #@id/mtrl_picker_header
   │  ├─ androidx.constraintlayout.widget.ConstraintLayout  #@id/mtrl_picker_header_title_and_selection
   │  │  ├─ androidx.constraintlayout.widget.Guideline  #@id/guideline
   │  │  ├─ TextView  #@id/mtrl_picker_title_text
   │  │  └─ TextView  #@id/mtrl_picker_header_selection_text
   │  └─ include
   └─ View
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `merge` | `android:layout_width` | `wrap_content` |
| 2 | `merge` | `android:layout_height` | `match_parent` |
| 3 | `LinearLayout` | `android:layout_gravity` | `0x00800003` |
| 4 | `LinearLayout` | `android:orientation` | `vertical` |
| 5 | `LinearLayout` | `android:id` | `@id/mtrl_picker_header` |
| 6 | `LinearLayout` | `android:paddingLeft` | `@dimen/mtrl_calendar_header_content_padding` |
| 7 | `LinearLayout` | `android:paddingRight` | `@dimen/mtrl_calendar_header_content_padding` |
| 8 | `LinearLayout` | `android:paddingBottom` | `@dimen/mtrl_calendar_header_content_padding` |
| 9 | `LinearLayout` | `android:layout_width` | `wrap_content` |
| 10 | `LinearLayout` | `android:layout_height` | `match_parent` |
| 11 | `LinearLayout` | `android:paddingStart` | `@dimen/mtrl_calendar_header_content_padding` |
| 12 | `LinearLayout` | `android:paddingEnd` | `@dimen/mtrl_calendar_header_content_padding` |
| 13 | `LinearLayout` | `style` | `?attr/materialCalendarHeaderLayout` |
| 14 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:id` | `@id/mtrl_picker_header_title_and_selection` |
| 15 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:paddingLeft` | `@dimen/mtrl_calendar_header_text_padding` |
| 16 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:focusable` | `false` |
| 17 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:focusableInTouchMode` | `false` |
| 18 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_width` | `@dimen/mtrl_calendar_landscape_header_width` |
| 19 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_height` | `0.000000dip` |
| 20 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_weight` | `1.000000` |
| 21 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:importantForAccessibility` | `yes` |
| 22 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:paddingStart` | `@dimen/mtrl_calendar_header_text_padding` |
| 23 | `androidx.constraintlayout.widget.Guideline` | `android:orientation` | `horizontal` |
| 24 | `androidx.constraintlayout.widget.Guideline` | `android:id` | `@id/guideline` |
| 25 | `androidx.constraintlayout.widget.Guideline` | `android:layout_width` | `wrap_content` |
| 26 | `androidx.constraintlayout.widget.Guideline` | `android:layout_height` | `wrap_content` |
| 27 | `androidx.constraintlayout.widget.Guideline` | `app:layout_constraintGuide_percent` | `0.550000` |
| 28 | `TextView` | `android:id` | `@id/mtrl_picker_title_text` |
| 29 | `TextView` | `android:layout_width` | `0.000000dip` |
| 30 | `TextView` | `android:layout_height` | `wrap_content` |
| 31 | `TextView` | `app:firstBaselineToTopHeight` | `@dimen/mtrl_calendar_title_baseline_to_top` |
| 32 | `TextView` | `app:layout_constrainedHeight` | `true` |
| 33 | `TextView` | `app:layout_constraintBottom_toTopOf` | `@id/guideline` |
| 34 | `TextView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 35 | `TextView` | `app:layout_constraintStart_toStartOf` | `0` |
| 36 | `TextView` | `app:layout_constraintTop_toTopOf` | `0` |
| 37 | `TextView` | `app:layout_constraintVertical_bias` | `0.000000` |
| 38 | `TextView` | `style` | `?attr/materialCalendarHeaderTitle` |
| 39 | `TextView` | `android:id` | `@id/mtrl_picker_header_selection_text` |
| 40 | `TextView` | `android:layout_width` | `0.000000dip` |
| 41 | `TextView` | `android:layout_height` | `0.000000dip` |
| 42 | `TextView` | `app:layout_constrainedHeight` | `true` |
| 43 | `TextView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 44 | `TextView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 45 | `TextView` | `app:layout_constraintStart_toStartOf` | `0` |
| 46 | `TextView` | `app:layout_constraintTop_toBottomOf` | `@id/mtrl_picker_title_text` |
| 47 | `TextView` | `app:lineHeight` | `@dimen/mtrl_calendar_header_selection_line_height` |
| 48 | `TextView` | `style` | `?attr/materialCalendarHeaderSelection` |
| 49 | `include` | `layout` | `@layout/mtrl_picker_header_toggle` |
| 50 | `View` | `android:layout_gravity` | `0x00800005` |
| 51 | `View` | `android:layout_width` | `@dimen/mtrl_calendar_header_divider_thickness` |
| 52 | `View` | `android:layout_height` | `match_parent` |
| 53 | `View` | `style` | `?attr/materialCalendarHeaderDivider` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@dimen/mtrl_calendar_header_content_padding` | `12.000000dip` / `4.000000dip` (land) |
| `@dimen/mtrl_calendar_header_divider_thickness` | `1.000000dip` |
| `@dimen/mtrl_calendar_header_selection_line_height` | `32.000000dip` |
| `@dimen/mtrl_calendar_header_text_padding` | `12.000000dip` |
| `@dimen/mtrl_calendar_landscape_header_width` | `0.000000dip` / `128.000000dip` (h360dp-land) / `168.000000dip` (h480dp-land) / `104.000000dip` (land) |
| `@dimen/mtrl_calendar_title_baseline_to_top` | `28.000000dip` / `24.000000dip` (land) |

## ۴. شناسه‌های `@id`

```text
@id/guideline
@id/mtrl_picker_header
@id/mtrl_picker_header_selection_text
@id/mtrl_picker_header_title_and_selection
@id/mtrl_picker_title_text
```

## ۵. ارجاع به لایه‌های دیگر

```text
@layout/mtrl_picker_header_toggle
match_parent
wrap_content
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

(هیچ صفحهٔ نام‌برداری به این لایه متصل نشد؛ ممکن است لایهٔ کتابخانه/`<include>` باشد)

## ۷. لایه‌هایی که این لایه را include می‌کنند

```text
res/layout/mtrl_picker_dialog.xml
```

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<merge xmlns:android="http://schemas.android.com/apk/res/android" xmlns:app="http://schemas.android.com/apk/res-auto" android:layout_width="wrap_content" android:layout_height="match_parent">
  <LinearLayout android:layout_gravity="0x00800003" android:orientation="vertical" android:id="@id/mtrl_picker_header" android:paddingLeft="@dimen/mtrl_calendar_header_content_padding" android:paddingRight="@dimen/mtrl_calendar_header_content_padding" android:paddingBottom="@dimen/mtrl_calendar_header_content_padding" android:layout_width="wrap_content" android:layout_height="match_parent" android:paddingStart="@dimen/mtrl_calendar_header_content_padding" android:paddingEnd="@dimen/mtrl_calendar_header_content_padding" style="?attr/materialCalendarHeaderLayout">
    <androidx.constraintlayout.widget.ConstraintLayout android:id="@id/mtrl_picker_header_title_and_selection" android:paddingLeft="@dimen/mtrl_calendar_header_text_padding" android:focusable="false" android:focusableInTouchMode="false" android:layout_width="@dimen/mtrl_calendar_landscape_header_width" android:layout_height="0.000000dip" android:layout_weight="1.000000" android:importantForAccessibility="yes" android:paddingStart="@dimen/mtrl_calendar_header_text_padding">
      <androidx.constraintlayout.widget.Guideline android:orientation="horizontal" android:id="@id/guideline" android:layout_width="wrap_content" android:layout_height="wrap_content" app:layout_constraintGuide_percent="0.550000"/>
      <TextView android:id="@id/mtrl_picker_title_text" android:layout_width="0.000000dip" android:layout_height="wrap_content" app:firstBaselineToTopHeight="@dimen/mtrl_calendar_title_baseline_to_top" app:layout_constrainedHeight="true" app:layout_constraintBottom_toTopOf="@id/guideline" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="0" app:layout_constraintVertical_bias="0.000000" style="?attr/materialCalendarHeaderTitle"/>
      <TextView android:id="@id/mtrl_picker_header_selection_text" android:layout_width="0.000000dip" android:layout_height="0.000000dip" app:layout_constrainedHeight="true" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/mtrl_picker_title_text" app:lineHeight="@dimen/mtrl_calendar_header_selection_line_height" style="?attr/materialCalendarHeaderSelection"/>
    </androidx.constraintlayout.widget.ConstraintLayout>
    <include layout="@layout/mtrl_picker_header_toggle"/>
  </LinearLayout>
  <View android:layout_gravity="0x00800005" android:layout_width="@dimen/mtrl_calendar_header_divider_thickness" android:layout_height="match_parent" style="?attr/materialCalendarHeaderDivider"/>
</merge>
```
