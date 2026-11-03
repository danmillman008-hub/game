# پروندهٔ لایه — `res/layout/flashbar_dropdown_layout.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/flashbar_dropdown_layout.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/flashbar_dropdown_layout.xml`](../../SOURCE/res/layout/flashbar_dropdown_layout.xml) |
| SHA-256 دیکد | `157eddfdbcc4646162aa50524bbfc2e437b1a771c7f3d790057fb3ee156ad8a0` |
| ریشه | `LinearLayout` |
| تعداد گره | 5 |
| تعداد شناسه | 4 |
| تگ‌های استفاده‌شده | 4 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 10 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ LinearLayout  #@id/fbRoot
   └─ LinearLayout  #@id/fbContent
      └─ androidx.constraintlayout.widget.ConstraintLayout
         ├─ ImageView  #@id/fbIcon
         └─ TextView  #@id/fbMessage
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `LinearLayout` | `android:orientation` | `vertical` |
| 2 | `LinearLayout` | `android:id` | `@id/fbRoot` |
| 3 | `LinearLayout` | `android:layout_width` | `match_parent` |
| 4 | `LinearLayout` | `android:layout_height` | `wrap_content` |
| 5 | `LinearLayout` | `android:minHeight` | `@dimen/flashbar_playground_min_height` |
| 6 | `LinearLayout` | `android:id` | `@id/fbContent` |
| 7 | `LinearLayout` | `android:layout_width` | `match_parent` |
| 8 | `LinearLayout` | `android:layout_height` | `wrap_content` |
| 9 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_width` | `match_parent` |
| 10 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_height` | `wrap_content` |
| 11 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:minHeight` | `@dimen/flashbar_playground_min_height` |
| 12 | `ImageView` | `android:id` | `@id/fbIcon` |
| 13 | `ImageView` | `android:layout_width` | `24.000000dip` |
| 14 | `ImageView` | `android:layout_height` | `24.000000dip` |
| 15 | `ImageView` | `android:layout_marginTop` | `@dimen/flashbar_playground_icon_vertical_margin` |
| 16 | `ImageView` | `android:layout_marginBottom` | `@dimen/flashbar_playground_icon_vertical_margin` |
| 17 | `ImageView` | `android:layout_marginStart` | `@dimen/flashbar_playground_icon_horizontal_margin` |
| 18 | `ImageView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 19 | `ImageView` | `app:layout_constraintStart_toStartOf` | `0` |
| 20 | `ImageView` | `app:layout_constraintTop_toTopOf` | `0` |
| 21 | `TextView` | `android:id` | `@id/fbMessage` |
| 22 | `TextView` | `android:visibility` | `gone` |
| 23 | `TextView` | `android:layout_width` | `0.000000dip` |
| 24 | `TextView` | `android:layout_height` | `wrap_content` |
| 25 | `TextView` | `android:layout_marginTop` | `@dimen/flashbar_playground_vertical_margin` |
| 26 | `TextView` | `android:layout_marginBottom` | `@dimen/flashbar_playground_vertical_margin` |
| 27 | `TextView` | `android:minLines` | `2` |
| 28 | `TextView` | `android:layout_marginStart` | `@dimen/flashbar_playground_horizontal_margin` |
| 29 | `TextView` | `android:layout_marginEnd` | `@dimen/flashbar_playground_horizontal_margin` |
| 30 | `TextView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 31 | `TextView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 32 | `TextView` | `app:layout_constraintStart_toEndOf` | `@id/fbIcon` |
| 33 | `TextView` | `app:layout_constraintTop_toTopOf` | `0` |
| 34 | `TextView` | `style` | `@style/TextFlashbarMessage` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@dimen/flashbar_playground_horizontal_margin` | `12.000000dip` / `24.000000dip` (sw600dp) |
| `@dimen/flashbar_playground_icon_horizontal_margin` | `12.000000dip` / `24.000000dip` (sw600dp) |
| `@dimen/flashbar_playground_icon_vertical_margin` | `20.000000dip` / `24.000000dip` (sw600dp) |
| `@dimen/flashbar_playground_min_height` | `70.000000dip` / `72.000000dip` (sw600dp) |
| `@dimen/flashbar_playground_vertical_margin` | `12.000000dip` / `24.000000dip` (sw600dp) |
| `@style/TextFlashbarMessage` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '13.000000sp', 'value_type': 'dimension'}, {'attr': 'android:textColor', 'attr_id': '0x01010098', 'value': '@color/white', 'value_type': 'reference'}, {'attr': 'android:gravity', 'attr_id': '0x010100AF', 'value': '0x00000010', 'value_type': 'int_hex'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '3.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '16.000000sp', 'value_type': 'dimension'}, {'attr': 'android:textColor', 'attr_id': '0x01010098', 'value': '@color/white', 'value_type': 'reference'}, {'attr': 'android:fontFamily', 'attr_id': '0x010103AC', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` (sw600dp) |

## ۴. شناسه‌های `@id`

```text
@id/fbContent
@id/fbIcon
@id/fbMessage
@id/fbRoot
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
<LinearLayout xmlns:app="http://schemas.android.com/apk/res-auto" xmlns:android="http://schemas.android.com/apk/res/android" android:orientation="vertical" android:id="@id/fbRoot" android:layout_width="match_parent" android:layout_height="wrap_content" android:minHeight="@dimen/flashbar_playground_min_height">
  <LinearLayout android:id="@id/fbContent" android:layout_width="match_parent" android:layout_height="wrap_content">
    <androidx.constraintlayout.widget.ConstraintLayout android:layout_width="match_parent" android:layout_height="wrap_content" android:minHeight="@dimen/flashbar_playground_min_height">
      <ImageView android:id="@id/fbIcon" android:layout_width="24.000000dip" android:layout_height="24.000000dip" android:layout_marginTop="@dimen/flashbar_playground_icon_vertical_margin" android:layout_marginBottom="@dimen/flashbar_playground_icon_vertical_margin" android:layout_marginStart="@dimen/flashbar_playground_icon_horizontal_margin" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="0"/>
      <TextView android:id="@id/fbMessage" android:visibility="gone" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginTop="@dimen/flashbar_playground_vertical_margin" android:layout_marginBottom="@dimen/flashbar_playground_vertical_margin" android:minLines="2" android:layout_marginStart="@dimen/flashbar_playground_horizontal_margin" android:layout_marginEnd="@dimen/flashbar_playground_horizontal_margin" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toEndOf="@id/fbIcon" app:layout_constraintTop_toTopOf="0" style="@style/TextFlashbarMessage"/>
    </androidx.constraintlayout.widget.ConstraintLayout>
  </LinearLayout>
</LinearLayout>
```
