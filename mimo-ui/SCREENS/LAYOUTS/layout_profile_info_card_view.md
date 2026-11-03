# پروندهٔ لایه — `res/layout/profile_info_card_view.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/profile_info_card_view.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/profile_info_card_view.xml`](../../SOURCE/res/layout/profile_info_card_view.xml) |
| SHA-256 دیکد | `9c29e951a429858018f2368d112843f8d6bc96dbacf380c7b22bcdca05703325` |
| ریشه | `merge` |
| تعداد گره | 6 |
| تعداد شناسه | 4 |
| تگ‌های استفاده‌شده | 5 |
| ویوهای سفارشی `com.getmimo` | 1 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 10 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ merge
   └─ androidx.constraintlayout.widget.ConstraintLayout
      ├─ ImageView  #@id/iv_profile_card_icon
      ├─ TextView  #@id/tv_profile_card_value
      ├─ TextView  #@id/tv_profile_card_label
      └─ com.getmimo.ui.components.placeholder.PlaceholderView  #@id/profile_card_placeholder
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_width` | `match_parent` |
| 2 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_height` | `wrap_content` |
| 3 | `ImageView` | `android:id` | `@id/iv_profile_card_icon` |
| 4 | `ImageView` | `android:layout_width` | `32.000000dip` |
| 5 | `ImageView` | `android:layout_height` | `32.000000dip` |
| 6 | `ImageView` | `android:layout_marginTop` | `@dimen/spacing_m` |
| 7 | `ImageView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 8 | `ImageView` | `app:layout_constraintStart_toStartOf` | `0` |
| 9 | `ImageView` | `app:layout_constraintTop_toTopOf` | `0` |
| 10 | `TextView` | `android:textColor` | `@color/text_primary` |
| 11 | `TextView` | `android:id` | `@id/tv_profile_card_value` |
| 12 | `TextView` | `android:layout_width` | `wrap_content` |
| 13 | `TextView` | `android:layout_height` | `wrap_content` |
| 14 | `TextView` | `android:layout_marginTop` | `@dimen/spacing_xs` |
| 15 | `TextView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 16 | `TextView` | `app:layout_constraintStart_toStartOf` | `0` |
| 17 | `TextView` | `app:layout_constraintTop_toBottomOf` | `@id/iv_profile_card_icon` |
| 18 | `TextView` | `style` | `@style/TextH3` |
| 19 | `TextView` | `android:textColor` | `@color/text_weak` |
| 20 | `TextView` | `android:id` | `@id/tv_profile_card_label` |
| 21 | `TextView` | `android:layout_width` | `wrap_content` |
| 22 | `TextView` | `android:layout_height` | `wrap_content` |
| 23 | `TextView` | `android:layout_marginTop` | `@dimen/spacing_xs` |
| 24 | `TextView` | `android:layout_marginBottom` | `@dimen/spacing_m` |
| 25 | `TextView` | `android:textAllCaps` | `true` |
| 26 | `TextView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 27 | `TextView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 28 | `TextView` | `app:layout_constraintStart_toStartOf` | `0` |
| 29 | `TextView` | `app:layout_constraintTop_toBottomOf` | `@id/tv_profile_card_value` |
| 30 | `TextView` | `style` | `@style/TextLabel3` |
| 31 | `com.getmimo.ui.components.placeholder.PlaceholderView` | `android:id` | `@id/profile_card_placeholder` |
| 32 | `com.getmimo.ui.components.placeholder.PlaceholderView` | `android:layout_width` | `0.000000dip` |
| 33 | `com.getmimo.ui.components.placeholder.PlaceholderView` | `android:layout_height` | `0.000000dip` |
| 34 | `com.getmimo.ui.components.placeholder.PlaceholderView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 35 | `com.getmimo.ui.components.placeholder.PlaceholderView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 36 | `com.getmimo.ui.components.placeholder.PlaceholderView` | `app:layout_constraintStart_toStartOf` | `0` |
| 37 | `com.getmimo.ui.components.placeholder.PlaceholderView` | `app:layout_constraintTop_toTopOf` | `0` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/text_primary` | `#FF252746` / `#FFFFFFFF` (night) |
| `@color/text_weak` | `#FF4A4D85` / `#CCFFFFFF` (night) |
| `@dimen/spacing_m` | `16.000000dip` |
| `@dimen/spacing_xs` | `8.000000dip` |
| `@style/TextH3` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '18.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '5.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_fono_medium', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '23.399996sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '13.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_fono_medium', 'value_type': 'reference'}]` (sw600dp) |
| `@style/TextLabel3` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '12.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '3.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_bold', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '15.599977sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '7.799988sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_bold', 'value_type': 'reference'}]` (sw600dp) |

## ۴. شناسه‌های `@id`

```text
@id/iv_profile_card_icon
@id/profile_card_placeholder
@id/tv_profile_card_label
@id/tv_profile_card_value
```

## ۵. ارجاع به لایه‌های دیگر

```text
(none)
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

```text
com.getmimo.ui.profile.main.ProfileFragment
```

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<merge xmlns:android="http://schemas.android.com/apk/res/android" xmlns:app="http://schemas.android.com/apk/res-auto">
  <androidx.constraintlayout.widget.ConstraintLayout android:layout_width="match_parent" android:layout_height="wrap_content">
    <ImageView android:id="@id/iv_profile_card_icon" android:layout_width="32.000000dip" android:layout_height="32.000000dip" android:layout_marginTop="@dimen/spacing_m" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="0"/>
    <TextView android:textColor="@color/text_primary" android:id="@id/tv_profile_card_value" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_xs" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/iv_profile_card_icon" style="@style/TextH3"/>
    <TextView android:textColor="@color/text_weak" android:id="@id/tv_profile_card_label" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_xs" android:layout_marginBottom="@dimen/spacing_m" android:textAllCaps="true" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/tv_profile_card_value" style="@style/TextLabel3"/>
    <com.getmimo.ui.components.placeholder.PlaceholderView android:id="@id/profile_card_placeholder" android:layout_width="0.000000dip" android:layout_height="0.000000dip" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="0"/>
  </androidx.constraintlayout.widget.ConstraintLayout>
</merge>
```
