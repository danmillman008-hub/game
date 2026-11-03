# پروندهٔ لایه — `res/layout/set_daily_goal_card_item.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/set_daily_goal_card_item.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/set_daily_goal_card_item.xml`](../../SOURCE/res/layout/set_daily_goal_card_item.xml) |
| SHA-256 دیکد | `e6d6a46f9f33094a90e680057992f18acafd0b22ddc532e623d38f1a5b18844f` |
| ریشه | `androidx.constraintlayout.widget.ConstraintLayout` |
| تعداد گره | 4 |
| تعداد شناسه | 3 |
| تگ‌های استفاده‌شده | 3 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 8 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ androidx.constraintlayout.widget.ConstraintLayout
   ├─ com.google.android.material.radiobutton.MaterialRadioButton  #@id/radio_daily_goal_level
   ├─ TextView  #@id/tv_daily_goal_level_name
   └─ TextView  #@id/tv_daily_goal_level
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_gravity` | `0x00000011` |
| 2 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_width` | `match_parent` |
| 3 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_height` | `wrap_content` |
| 4 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:paddingHorizontal` | `@dimen/spacing_m` |
| 5 | `com.google.android.material.radiobutton.MaterialRadioButton` | `android:id` | `@id/radio_daily_goal_level` |
| 6 | `com.google.android.material.radiobutton.MaterialRadioButton` | `android:focusable` | `false` |
| 7 | `com.google.android.material.radiobutton.MaterialRadioButton` | `android:clickable` | `false` |
| 8 | `com.google.android.material.radiobutton.MaterialRadioButton` | `android:layout_width` | `wrap_content` |
| 9 | `com.google.android.material.radiobutton.MaterialRadioButton` | `android:layout_height` | `wrap_content` |
| 10 | `com.google.android.material.radiobutton.MaterialRadioButton` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 11 | `com.google.android.material.radiobutton.MaterialRadioButton` | `app:layout_constraintStart_toStartOf` | `0` |
| 12 | `com.google.android.material.radiobutton.MaterialRadioButton` | `app:layout_constraintTop_toTopOf` | `0` |
| 13 | `com.google.android.material.radiobutton.MaterialRadioButton` | `style` | `@style/MaterialRadioButton` |
| 14 | `TextView` | `android:textColor` | `@color/text_primary` |
| 15 | `TextView` | `android:id` | `@id/tv_daily_goal_level_name` |
| 16 | `TextView` | `android:layout_width` | `wrap_content` |
| 17 | `TextView` | `android:layout_height` | `wrap_content` |
| 18 | `TextView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 19 | `TextView` | `app:layout_constraintStart_toEndOf` | `@id/radio_daily_goal_level` |
| 20 | `TextView` | `app:layout_constraintTop_toTopOf` | `0` |
| 21 | `TextView` | `style` | `@style/TextSelection1` |
| 22 | `TextView` | `android:id` | `@id/tv_daily_goal_level` |
| 23 | `TextView` | `android:layout_width` | `wrap_content` |
| 24 | `TextView` | `android:layout_height` | `wrap_content` |
| 25 | `TextView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 26 | `TextView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 27 | `TextView` | `app:layout_constraintTop_toTopOf` | `0` |
| 28 | `TextView` | `style` | `@style/TextRadioButtonChoiceCardDetails` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/text_primary` | `#FF252746` / `#FFFFFFFF` (night) |
| `@dimen/spacing_m` | `16.000000dip` |
| `@style/MaterialRadioButton` | `[{'attr': 'attr.buttonTint', 'attr_id': '0x7F0400B5', 'value': '@color/material_radiobutton', 'value_type': 'reference'}, {'attr': 'attr.useMaterialThemeColors', 'attr_id': '0x7F040680', 'value': 'false', 'value_type': 'int_boolean'}]` |
| `@style/TextRadioButtonChoiceCardDetails` | `[{'attr': 'android:textColor', 'attr_id': '0x01010098', 'value': '@color/text_primary', 'value_type': 'reference'}]` |
| `@style/TextSelection1` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '18.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '10.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_medium', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '23.399996sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '13.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_medium', 'value_type': 'reference'}]` (sw600dp) |

## ۴. شناسه‌های `@id`

```text
@id/radio_daily_goal_level
@id/tv_daily_goal_level
@id/tv_daily_goal_level_name
```

## ۵. ارجاع به لایه‌های دیگر

```text
(none)
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

```text
com.getmimo.ui.profile.SetDailyGoalActivity
```

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout xmlns:android="http://schemas.android.com/apk/res/android" xmlns:app="http://schemas.android.com/apk/res-auto" android:layout_gravity="0x00000011" android:layout_width="match_parent" android:layout_height="wrap_content" android:paddingHorizontal="@dimen/spacing_m">
  <com.google.android.material.radiobutton.MaterialRadioButton android:id="@id/radio_daily_goal_level" android:focusable="false" android:clickable="false" android:layout_width="wrap_content" android:layout_height="wrap_content" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="0" style="@style/MaterialRadioButton"/>
  <TextView android:textColor="@color/text_primary" android:id="@id/tv_daily_goal_level_name" android:layout_width="wrap_content" android:layout_height="wrap_content" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintStart_toEndOf="@id/radio_daily_goal_level" app:layout_constraintTop_toTopOf="0" style="@style/TextSelection1"/>
  <TextView android:id="@id/tv_daily_goal_level" android:layout_width="wrap_content" android:layout_height="wrap_content" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toEndOf="0" app:layout_constraintTop_toTopOf="0" style="@style/TextRadioButtonChoiceCardDetails"/>
</androidx.constraintlayout.widget.ConstraintLayout>
```
