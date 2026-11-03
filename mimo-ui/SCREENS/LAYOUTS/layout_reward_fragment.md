# پروندهٔ لایه — `res/layout/reward_fragment.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/reward_fragment.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/reward_fragment.xml`](../../SOURCE/res/layout/reward_fragment.xml) |
| SHA-256 دیکد | `286df4db97b9fe947be75a584ef18556cef7776961baa5d7d0615882e82ac3cf` |
| ریشه | `androidx.constraintlayout.widget.ConstraintLayout` |
| تعداد گره | 10 |
| تعداد شناسه | 9 |
| تگ‌های استفاده‌شده | 6 |
| ویوهای سفارشی `com.getmimo` | 1 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 19 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ androidx.constraintlayout.widget.ConstraintLayout
   ├─ TextView  #@id/tv_reward_bottom_sheet_header
   ├─ TextView  #@id/tv_reward_bottom_sheet_description
   ├─ View  #@id/divider_reward_bottom_sheet
   ├─ TextSwitcher  #@id/tv_reward_bottom_sheet_status_line_1
   ├─ TextSwitcher  #@id/tv_reward_bottom_sheet_status_line_2
   └─ LinearLayout  #@id/layout_reward_boxes
      ├─ com.getmimo.ui.reward.RewardBox  #@id/reward_box_1
      ├─ com.getmimo.ui.reward.RewardBox  #@id/reward_box_2
      └─ com.getmimo.ui.reward.RewardBox  #@id/reward_box_3
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:orientation` | `vertical` |
| 2 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_width` | `match_parent` |
| 3 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_height` | `wrap_content` |
| 4 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:minHeight` | `200.000000dip` |
| 5 | `TextView` | `android:textColor` | `@color/text_primary` |
| 6 | `TextView` | `android:id` | `@id/tv_reward_bottom_sheet_header` |
| 7 | `TextView` | `android:layout_width` | `wrap_content` |
| 8 | `TextView` | `android:layout_height` | `wrap_content` |
| 9 | `TextView` | `android:layout_marginTop` | `@dimen/spacing_m` |
| 10 | `TextView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 11 | `TextView` | `app:layout_constraintStart_toStartOf` | `0` |
| 12 | `TextView` | `app:layout_constraintTop_toTopOf` | `0` |
| 13 | `TextView` | `style` | `@style/TextH1` |
| 14 | `TextView` | `android:textColor` | `@color/text_weak` |
| 15 | `TextView` | `android:gravity` | `0x00000011` |
| 16 | `TextView` | `android:id` | `@id/tv_reward_bottom_sheet_description` |
| 17 | `TextView` | `android:layout_width` | `0.000000dip` |
| 18 | `TextView` | `android:layout_height` | `wrap_content` |
| 19 | `TextView` | `android:layout_marginTop` | `@dimen/spacing_l` |
| 20 | `TextView` | `android:layout_marginHorizontal` | `@dimen/spacing_xxl` |
| 21 | `TextView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 22 | `TextView` | `app:layout_constraintStart_toStartOf` | `0` |
| 23 | `TextView` | `app:layout_constraintTop_toBottomOf` | `@id/tv_reward_bottom_sheet_header` |
| 24 | `TextView` | `style` | `@style/TextP1` |
| 25 | `View` | `android:id` | `@id/divider_reward_bottom_sheet` |
| 26 | `View` | `android:background` | `@color/line_primary` |
| 27 | `View` | `android:layout_width` | `0.000000dip` |
| 28 | `View` | `android:layout_height` | `1.000000dip` |
| 29 | `View` | `android:layout_marginTop` | `@dimen/spacing_l` |
| 30 | `View` | `android:layout_marginHorizontal` | `@dimen/spacing_s` |
| 31 | `View` | `app:layout_constraintEnd_toEndOf` | `0` |
| 32 | `View` | `app:layout_constraintStart_toStartOf` | `0` |
| 33 | `View` | `app:layout_constraintTop_toBottomOf` | `@id/tv_reward_bottom_sheet_description` |
| 34 | `TextSwitcher` | `android:id` | `@id/tv_reward_bottom_sheet_status_line_1` |
| 35 | `TextSwitcher` | `android:layout_width` | `0.000000dip` |
| 36 | `TextSwitcher` | `android:layout_height` | `wrap_content` |
| 37 | `TextSwitcher` | `android:layout_marginTop` | `@dimen/spacing_m` |
| 38 | `TextSwitcher` | `app:layout_constraintEnd_toEndOf` | `0` |
| 39 | `TextSwitcher` | `app:layout_constraintStart_toStartOf` | `0` |
| 40 | `TextSwitcher` | `app:layout_constraintTop_toBottomOf` | `@id/divider_reward_bottom_sheet` |
| 41 | `TextSwitcher` | `android:id` | `@id/tv_reward_bottom_sheet_status_line_2` |
| 42 | `TextSwitcher` | `android:layout_width` | `0.000000dip` |
| 43 | `TextSwitcher` | `android:layout_height` | `wrap_content` |
| 44 | `TextSwitcher` | `android:layout_marginTop` | `2.000000dip` |
| 45 | `TextSwitcher` | `app:layout_constraintEnd_toEndOf` | `0` |
| 46 | `TextSwitcher` | `app:layout_constraintStart_toStartOf` | `0` |
| 47 | `TextSwitcher` | `app:layout_constraintTop_toBottomOf` | `@id/tv_reward_bottom_sheet_status_line_1` |
| 48 | `LinearLayout` | `android:gravity` | `0x00000011` |
| 49 | `LinearLayout` | `android:orientation` | `horizontal` |
| 50 | `LinearLayout` | `android:id` | `@id/layout_reward_boxes` |
| 51 | `LinearLayout` | `android:layout_width` | `match_parent` |
| 52 | `LinearLayout` | `android:layout_height` | `match_parent` |
| 53 | `LinearLayout` | `android:layout_marginTop` | `@dimen/spacing_m` |
| 54 | `LinearLayout` | `android:layout_marginBottom` | `@dimen/spacing_l` |
| 55 | `LinearLayout` | `android:weightSum` | `3.000000` |
| 56 | `LinearLayout` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 57 | `LinearLayout` | `app:layout_constraintEnd_toEndOf` | `0` |
| 58 | `LinearLayout` | `app:layout_constraintHeight_max` | `120.000000dip` |
| 59 | `LinearLayout` | `app:layout_constraintStart_toStartOf` | `0` |
| 60 | `LinearLayout` | `app:layout_constraintTop_toBottomOf` | `@id/tv_reward_bottom_sheet_status_line_2` |
| 61 | `com.getmimo.ui.reward.RewardBox` | `android:id` | `@id/reward_box_1` |
| 62 | `com.getmimo.ui.reward.RewardBox` | `android:layout_width` | `0.000000dip` |
| 63 | `com.getmimo.ui.reward.RewardBox` | `android:layout_height` | `wrap_content` |
| 64 | `com.getmimo.ui.reward.RewardBox` | `android:layout_weight` | `1.000000` |
| 65 | `com.getmimo.ui.reward.RewardBox` | `android:layout_marginHorizontal` | `@dimen/spacing_xs` |
| 66 | `com.getmimo.ui.reward.RewardBox` | `android:id` | `@id/reward_box_2` |
| 67 | `com.getmimo.ui.reward.RewardBox` | `android:layout_width` | `0.000000dip` |
| 68 | `com.getmimo.ui.reward.RewardBox` | `android:layout_height` | `wrap_content` |
| 69 | `com.getmimo.ui.reward.RewardBox` | `android:layout_weight` | `1.000000` |
| 70 | `com.getmimo.ui.reward.RewardBox` | `android:layout_marginHorizontal` | `@dimen/spacing_xs` |
| 71 | `com.getmimo.ui.reward.RewardBox` | `android:id` | `@id/reward_box_3` |
| 72 | `com.getmimo.ui.reward.RewardBox` | `android:layout_width` | `0.000000dip` |
| 73 | `com.getmimo.ui.reward.RewardBox` | `android:layout_height` | `wrap_content` |
| 74 | `com.getmimo.ui.reward.RewardBox` | `android:layout_weight` | `1.000000` |
| 75 | `com.getmimo.ui.reward.RewardBox` | `android:layout_marginHorizontal` | `@dimen/spacing_xs` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/line_primary` | `#FFEDEEF6` / `#FF3F4273` (night) |
| `@color/text_primary` | `#FF252746` / `#FFFFFFFF` (night) |
| `@color/text_weak` | `#FF4A4D85` / `#CCFFFFFF` (night) |
| `@dimen/spacing_l` | `24.000000dip` |
| `@dimen/spacing_m` | `16.000000dip` |
| `@dimen/spacing_s` | `12.000000dip` |
| `@dimen/spacing_xs` | `8.000000dip` |
| `@dimen/spacing_xxl` | `40.000000dip` |
| `@style/TextH1` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '24.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '4.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_fono_medium', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '31.199984sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '10.199983sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_fono_medium', 'value_type': 'reference'}]` (sw600dp) |
| `@style/TextP1` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '18.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '5.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '23.399996sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '7.799988sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` (sw600dp) |

## ۴. شناسه‌های `@id`

```text
@id/divider_reward_bottom_sheet
@id/layout_reward_boxes
@id/reward_box_1
@id/reward_box_2
@id/reward_box_3
@id/tv_reward_bottom_sheet_description
@id/tv_reward_bottom_sheet_header
@id/tv_reward_bottom_sheet_status_line_1
@id/tv_reward_bottom_sheet_status_line_2
```

## ۵. ارجاع به لایه‌های دیگر

```text
(none)
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

```text
com.getmimo.ui.reward.RewardFragment$loadUserName$1
```

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout xmlns:android="http://schemas.android.com/apk/res/android" xmlns:app="http://schemas.android.com/apk/res-auto" android:orientation="vertical" android:layout_width="match_parent" android:layout_height="wrap_content" android:minHeight="200.000000dip">
  <TextView android:textColor="@color/text_primary" android:id="@id/tv_reward_bottom_sheet_header" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_m" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="0" style="@style/TextH1"/>
  <TextView android:textColor="@color/text_weak" android:gravity="0x00000011" android:id="@id/tv_reward_bottom_sheet_description" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_l" android:layout_marginHorizontal="@dimen/spacing_xxl" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/tv_reward_bottom_sheet_header" style="@style/TextP1"/>
  <View android:id="@id/divider_reward_bottom_sheet" android:background="@color/line_primary" android:layout_width="0.000000dip" android:layout_height="1.000000dip" android:layout_marginTop="@dimen/spacing_l" android:layout_marginHorizontal="@dimen/spacing_s" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/tv_reward_bottom_sheet_description"/>
  <TextSwitcher android:id="@id/tv_reward_bottom_sheet_status_line_1" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_m" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/divider_reward_bottom_sheet"/>
  <TextSwitcher android:id="@id/tv_reward_bottom_sheet_status_line_2" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginTop="2.000000dip" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/tv_reward_bottom_sheet_status_line_1"/>
  <LinearLayout android:gravity="0x00000011" android:orientation="horizontal" android:id="@id/layout_reward_boxes" android:layout_width="match_parent" android:layout_height="match_parent" android:layout_marginTop="@dimen/spacing_m" android:layout_marginBottom="@dimen/spacing_l" android:weightSum="3.000000" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toEndOf="0" app:layout_constraintHeight_max="120.000000dip" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/tv_reward_bottom_sheet_status_line_2">
    <com.getmimo.ui.reward.RewardBox android:id="@id/reward_box_1" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_weight="1.000000" android:layout_marginHorizontal="@dimen/spacing_xs"/>
    <com.getmimo.ui.reward.RewardBox android:id="@id/reward_box_2" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_weight="1.000000" android:layout_marginHorizontal="@dimen/spacing_xs"/>
    <com.getmimo.ui.reward.RewardBox android:id="@id/reward_box_3" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_weight="1.000000" android:layout_marginHorizontal="@dimen/spacing_xs"/>
  </LinearLayout>
</androidx.constraintlayout.widget.ConstraintLayout>
```
