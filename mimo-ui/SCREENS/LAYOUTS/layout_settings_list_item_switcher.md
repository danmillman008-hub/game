# پروندهٔ لایه — `res/layout/settings_list_item_switcher.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/settings_list_item_switcher.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/settings_list_item_switcher.xml`](../../SOURCE/res/layout/settings_list_item_switcher.xml) |
| SHA-256 دیکد | `b5bdaeff6afcacf4fb4466942095d4e0e12e7d4b286c944186eb756780284fdb` |
| ریشه | `androidx.constraintlayout.widget.ConstraintLayout` |
| تعداد گره | 5 |
| تعداد شناسه | 4 |
| تگ‌های استفاده‌شده | 5 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 15 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ androidx.constraintlayout.widget.ConstraintLayout  #@id/layout_settings_list_item_switcher
   ├─ View
   ├─ ImageView  #@id/iv_settings_item_switcher_icon
   ├─ TextView  #@id/tv_settings_item_switcher_title
   └─ androidx.appcompat.widget.SwitchCompat  #@id/sw_settings_item_switcher
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:gravity` | `0x00000010` |
| 2 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:id` | `@id/layout_settings_list_item_switcher` |
| 3 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:background` | `@color/background_secondary` |
| 4 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_width` | `match_parent` |
| 5 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_height` | `56.000000dip` |
| 6 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:foreground` | `?attr/selectableItemBackground` |
| 7 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:paddingHorizontal` | `@dimen/spacing_m` |
| 8 | `View` | `android:background` | `@color/line_primary` |
| 9 | `View` | `android:layout_width` | `match_parent` |
| 10 | `View` | `android:layout_height` | `1.000000dip` |
| 11 | `View` | `app:layout_constraintEnd_toEndOf` | `0` |
| 12 | `View` | `app:layout_constraintStart_toStartOf` | `0` |
| 13 | `View` | `app:layout_constraintTop_toTopOf` | `0` |
| 14 | `ImageView` | `android:id` | `@id/iv_settings_item_switcher_icon` |
| 15 | `ImageView` | `android:layout_width` | `@dimen/icon_size_large` |
| 16 | `ImageView` | `android:layout_height` | `@dimen/icon_size_large` |
| 17 | `ImageView` | `android:layout_marginEnd` | `@dimen/spacing_m` |
| 18 | `ImageView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 19 | `ImageView` | `app:layout_constraintHorizontal_chainStyle` | `0` |
| 20 | `ImageView` | `app:layout_constraintStart_toStartOf` | `0` |
| 21 | `ImageView` | `app:layout_constraintTop_toTopOf` | `0` |
| 22 | `ImageView` | `app:tint` | `@color/icon_weak` |
| 23 | `TextView` | `android:textColor` | `@color/text_primary` |
| 24 | `TextView` | `android:id` | `@id/tv_settings_item_switcher_title` |
| 25 | `TextView` | `android:layout_width` | `0.000000dip` |
| 26 | `TextView` | `android:layout_height` | `wrap_content` |
| 27 | `TextView` | `android:layout_marginStart` | `16.000000dip` |
| 28 | `TextView` | `android:layout_marginEnd` | `32.000000dip` |
| 29 | `TextView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 30 | `TextView` | `app:layout_constraintEnd_toStartOf` | `@id/sw_settings_item_switcher` |
| 31 | `TextView` | `app:layout_constraintStart_toEndOf` | `@id/iv_settings_item_switcher_icon` |
| 32 | `TextView` | `app:layout_constraintTop_toTopOf` | `0` |
| 33 | `TextView` | `style` | `@style/TextP1` |
| 34 | `androidx.appcompat.widget.SwitchCompat` | `android:id` | `@id/sw_settings_item_switcher` |
| 35 | `androidx.appcompat.widget.SwitchCompat` | `android:layout_width` | `wrap_content` |
| 36 | `androidx.appcompat.widget.SwitchCompat` | `android:layout_height` | `0.000000dip` |
| 37 | `androidx.appcompat.widget.SwitchCompat` | `android:checked` | `false` |
| 38 | `androidx.appcompat.widget.SwitchCompat` | `android:thumb` | `@drawable/component_switch_thumb` |
| 39 | `androidx.appcompat.widget.SwitchCompat` | `android:layout_marginVertical` | `@dimen/spacing_s` |
| 40 | `androidx.appcompat.widget.SwitchCompat` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 41 | `androidx.appcompat.widget.SwitchCompat` | `app:layout_constraintEnd_toEndOf` | `0` |
| 42 | `androidx.appcompat.widget.SwitchCompat` | `app:layout_constraintTop_toTopOf` | `0` |
| 43 | `androidx.appcompat.widget.SwitchCompat` | `app:track` | `@drawable/component_switch_track` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/background_secondary` | `#FFFFFFFF` / `#FF333661` (night) |
| `@color/icon_weak` | `#FFA3A5C3` / `#80FFFFFF` (night) |
| `@color/line_primary` | `#FFEDEEF6` / `#FF3F4273` (night) |
| `@color/text_primary` | `#FF252746` / `#FFFFFFFF` (night) |
| `@dimen/icon_size_large` | `24.000000dip` |
| `@dimen/spacing_m` | `16.000000dip` |
| `@dimen/spacing_s` | `12.000000dip` |
| `@style/TextP1` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '18.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '5.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '23.399996sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '7.799988sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` (sw600dp) |

## ۴. شناسه‌های `@id`

```text
@id/iv_settings_item_switcher_icon
@id/layout_settings_list_item_switcher
@id/sw_settings_item_switcher
@id/tv_settings_item_switcher_title
```

## ۵. ارجاع به لایه‌های دیگر

```text
(none)
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

```text
com.getmimo.ui.settings.SettingsActivity
com.getmimo.ui.settings.SettingsFragment
```

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout xmlns:app="http://schemas.android.com/apk/res-auto" xmlns:android="http://schemas.android.com/apk/res/android" android:gravity="0x00000010" android:id="@id/layout_settings_list_item_switcher" android:background="@color/background_secondary" android:layout_width="match_parent" android:layout_height="56.000000dip" android:foreground="?attr/selectableItemBackground" android:paddingHorizontal="@dimen/spacing_m">
  <View android:background="@color/line_primary" android:layout_width="match_parent" android:layout_height="1.000000dip" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="0"/>
  <ImageView android:id="@id/iv_settings_item_switcher_icon" android:layout_width="@dimen/icon_size_large" android:layout_height="@dimen/icon_size_large" android:layout_marginEnd="@dimen/spacing_m" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintHorizontal_chainStyle="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="0" app:tint="@color/icon_weak"/>
  <TextView android:textColor="@color/text_primary" android:id="@id/tv_settings_item_switcher_title" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginStart="16.000000dip" android:layout_marginEnd="32.000000dip" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toStartOf="@id/sw_settings_item_switcher" app:layout_constraintStart_toEndOf="@id/iv_settings_item_switcher_icon" app:layout_constraintTop_toTopOf="0" style="@style/TextP1"/>
  <androidx.appcompat.widget.SwitchCompat android:id="@id/sw_settings_item_switcher" android:layout_width="wrap_content" android:layout_height="0.000000dip" android:checked="false" android:thumb="@drawable/component_switch_thumb" android:layout_marginVertical="@dimen/spacing_s" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toEndOf="0" app:layout_constraintTop_toTopOf="0" app:track="@drawable/component_switch_track"/>
</androidx.constraintlayout.widget.ConstraintLayout>
```
