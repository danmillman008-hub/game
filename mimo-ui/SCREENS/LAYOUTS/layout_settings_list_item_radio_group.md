# پروندهٔ لایه — `res/layout/settings_list_item_radio_group.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/settings_list_item_radio_group.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/settings_list_item_radio_group.xml`](../../SOURCE/res/layout/settings_list_item_radio_group.xml) |
| SHA-256 دیکد | `287e7216693d8e5ac8c51d03b07518f0a013caa17f22fa3263bca39644df13b9` |
| ریشه | `androidx.constraintlayout.widget.ConstraintLayout` |
| تعداد گره | 4 |
| تعداد شناسه | 3 |
| تگ‌های استفاده‌شده | 4 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 7 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ androidx.constraintlayout.widget.ConstraintLayout
   ├─ ImageView  #@id/iv_settings_item_radio_group_group_icon
   ├─ TextView  #@id/tv_settings_item_radio_group_group_title
   └─ RadioGroup  #@id/tv_settings_item_radio_group_group
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:padding` | `@dimen/spacing_m` |
| 2 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_width` | `match_parent` |
| 3 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_height` | `wrap_content` |
| 4 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:minHeight` | `56.000000dip` |
| 5 | `ImageView` | `android:id` | `@id/iv_settings_item_radio_group_group_icon` |
| 6 | `ImageView` | `android:layout_width` | `24.000000dip` |
| 7 | `ImageView` | `android:layout_height` | `24.000000dip` |
| 8 | `ImageView` | `app:layout_constraintStart_toStartOf` | `0` |
| 9 | `ImageView` | `app:layout_constraintTop_toTopOf` | `0` |
| 10 | `ImageView` | `app:tint` | `@color/icon_weak` |
| 11 | `TextView` | `android:textColor` | `@color/text_primary` |
| 12 | `TextView` | `android:id` | `@id/tv_settings_item_radio_group_group_title` |
| 13 | `TextView` | `android:layout_width` | `0.000000dip` |
| 14 | `TextView` | `android:layout_height` | `wrap_content` |
| 15 | `TextView` | `android:layout_marginStart` | `16.000000dip` |
| 16 | `TextView` | `android:layout_marginEnd` | `32.000000dip` |
| 17 | `TextView` | `app:layout_constraintBottom_toBottomOf` | `@id/iv_settings_item_radio_group_group_icon` |
| 18 | `TextView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 19 | `TextView` | `app:layout_constraintStart_toEndOf` | `@id/iv_settings_item_radio_group_group_icon` |
| 20 | `TextView` | `app:layout_constraintTop_toTopOf` | `@id/iv_settings_item_radio_group_group_icon` |
| 21 | `TextView` | `style` | `@style/TextP1` |
| 22 | `RadioGroup` | `android:orientation` | `vertical` |
| 23 | `RadioGroup` | `android:id` | `@id/tv_settings_item_radio_group_group` |
| 24 | `RadioGroup` | `android:layout_width` | `0.000000dip` |
| 25 | `RadioGroup` | `android:layout_height` | `wrap_content` |
| 26 | `RadioGroup` | `android:layout_marginTop` | `16.000000dip` |
| 27 | `RadioGroup` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 28 | `RadioGroup` | `app:layout_constraintEnd_toEndOf` | `0` |
| 29 | `RadioGroup` | `app:layout_constraintStart_toStartOf` | `0` |
| 30 | `RadioGroup` | `app:layout_constraintTop_toBottomOf` | `@id/tv_settings_item_radio_group_group_title` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/icon_weak` | `#FFA3A5C3` / `#80FFFFFF` (night) |
| `@color/text_primary` | `#FF252746` / `#FFFFFFFF` (night) |
| `@dimen/spacing_m` | `16.000000dip` |
| `@style/TextP1` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '18.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '5.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '23.399996sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '7.799988sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` (sw600dp) |

## ۴. شناسه‌های `@id`

```text
@id/iv_settings_item_radio_group_group_icon
@id/tv_settings_item_radio_group_group
@id/tv_settings_item_radio_group_group_title
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
<androidx.constraintlayout.widget.ConstraintLayout xmlns:android="http://schemas.android.com/apk/res/android" xmlns:app="http://schemas.android.com/apk/res-auto" android:padding="@dimen/spacing_m" android:layout_width="match_parent" android:layout_height="wrap_content" android:minHeight="56.000000dip">
  <ImageView android:id="@id/iv_settings_item_radio_group_group_icon" android:layout_width="24.000000dip" android:layout_height="24.000000dip" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="0" app:tint="@color/icon_weak"/>
  <TextView android:textColor="@color/text_primary" android:id="@id/tv_settings_item_radio_group_group_title" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginStart="16.000000dip" android:layout_marginEnd="32.000000dip" app:layout_constraintBottom_toBottomOf="@id/iv_settings_item_radio_group_group_icon" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toEndOf="@id/iv_settings_item_radio_group_group_icon" app:layout_constraintTop_toTopOf="@id/iv_settings_item_radio_group_group_icon" style="@style/TextP1"/>
  <RadioGroup android:orientation="vertical" android:id="@id/tv_settings_item_radio_group_group" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginTop="16.000000dip" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/tv_settings_item_radio_group_group_title"/>
</androidx.constraintlayout.widget.ConstraintLayout>
```
