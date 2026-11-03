# پروندهٔ لایه — `res/layout/abtest_config_item.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/abtest_config_item.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/abtest_config_item.xml`](../../SOURCE/res/layout/abtest_config_item.xml) |
| SHA-256 دیکد | `81428e84e4952bab0a736c19175530b1e7802cf491666f318665156c225ac512` |
| ریشه | `androidx.constraintlayout.widget.ConstraintLayout` |
| تعداد گره | 4 |
| تعداد شناسه | 3 |
| تگ‌های استفاده‌شده | 3 |
| ویوهای سفارشی `com.getmimo` | 1 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 9 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ androidx.constraintlayout.widget.ConstraintLayout
   ├─ TextView  #@id/tv_abtest_config_item_title
   ├─ TextView  #@id/tv_abtest_config_item_current_variant
   └─ com.getmimo.ui.settings.SettingsListItemRadioGroup  #@id/rg_abtest_config_override_variant
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:background` | `?attr/selectableItemBackground` |
| 2 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_width` | `match_parent` |
| 3 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_height` | `wrap_content` |
| 4 | `TextView` | `android:textColor` | `@color/text_primary` |
| 5 | `TextView` | `android:id` | `@id/tv_abtest_config_item_title` |
| 6 | `TextView` | `android:layout_width` | `0.000000dip` |
| 7 | `TextView` | `android:layout_height` | `wrap_content` |
| 8 | `TextView` | `android:layout_marginTop` | `8.000000dip` |
| 9 | `TextView` | `android:layout_marginBottom` | `8.000000dip` |
| 10 | `TextView` | `android:layout_marginStart` | `16.000000dip` |
| 11 | `TextView` | `android:layout_marginEnd` | `8.000000dip` |
| 12 | `TextView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 13 | `TextView` | `app:layout_constraintStart_toStartOf` | `0` |
| 14 | `TextView` | `app:layout_constraintTop_toTopOf` | `0` |
| 15 | `TextView` | `style` | `@style/TextH4` |
| 16 | `TextView` | `android:textColor` | `@color/text_weak` |
| 17 | `TextView` | `android:id` | `@id/tv_abtest_config_item_current_variant` |
| 18 | `TextView` | `android:layout_width` | `0.000000dip` |
| 19 | `TextView` | `android:layout_height` | `wrap_content` |
| 20 | `TextView` | `android:layout_marginTop` | `8.000000dip` |
| 21 | `TextView` | `android:layout_marginBottom` | `8.000000dip` |
| 22 | `TextView` | `android:layout_marginStart` | `16.000000dip` |
| 23 | `TextView` | `android:layout_marginEnd` | `8.000000dip` |
| 24 | `TextView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 25 | `TextView` | `app:layout_constraintStart_toStartOf` | `0` |
| 26 | `TextView` | `app:layout_constraintTop_toBottomOf` | `@id/tv_abtest_config_item_title` |
| 27 | `TextView` | `style` | `@style/TextP3` |
| 28 | `com.getmimo.ui.settings.SettingsListItemRadioGroup` | `android:id` | `@id/rg_abtest_config_override_variant` |
| 29 | `com.getmimo.ui.settings.SettingsListItemRadioGroup` | `android:layout_width` | `match_parent` |
| 30 | `com.getmimo.ui.settings.SettingsListItemRadioGroup` | `android:layout_height` | `wrap_content` |
| 31 | `com.getmimo.ui.settings.SettingsListItemRadioGroup` | `android:layout_marginTop` | `8.000000dip` |
| 32 | `com.getmimo.ui.settings.SettingsListItemRadioGroup` | `app:layout_constraintEnd_toEndOf` | `0` |
| 33 | `com.getmimo.ui.settings.SettingsListItemRadioGroup` | `app:layout_constraintStart_toStartOf` | `0` |
| 34 | `com.getmimo.ui.settings.SettingsListItemRadioGroup` | `app:layout_constraintTop_toBottomOf` | `@id/tv_abtest_config_item_current_variant` |
| 35 | `com.getmimo.ui.settings.SettingsListItemRadioGroup` | `app:settings_label` | `@string/developer_menu_disable_override_motive_variant` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/text_primary` | `#FF252746` / `#FFFFFFFF` (night) |
| `@color/text_weak` | `#FF4A4D85` / `#CCFFFFFF` (night) |
| `@string/developer_menu_disable_override_motive_variant` | `Override variant` |
| `@style/TextH4` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '16.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '4.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_fono_medium', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '20.799990sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '11.399995sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_fono_medium', 'value_type': 'reference'}]` (sw600dp) |
| `@style/TextP3` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '14.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '3.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '18.199983sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '5.199982sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` (sw600dp) |

## ۴. شناسه‌های `@id`

```text
@id/rg_abtest_config_override_variant
@id/tv_abtest_config_item_current_variant
@id/tv_abtest_config_item_title
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
<androidx.constraintlayout.widget.ConstraintLayout xmlns:app="http://schemas.android.com/apk/res-auto" xmlns:android="http://schemas.android.com/apk/res/android" android:background="?attr/selectableItemBackground" android:layout_width="match_parent" android:layout_height="wrap_content">
  <TextView android:textColor="@color/text_primary" android:id="@id/tv_abtest_config_item_title" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginTop="8.000000dip" android:layout_marginBottom="8.000000dip" android:layout_marginStart="16.000000dip" android:layout_marginEnd="8.000000dip" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="0" style="@style/TextH4"/>
  <TextView android:textColor="@color/text_weak" android:id="@id/tv_abtest_config_item_current_variant" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginTop="8.000000dip" android:layout_marginBottom="8.000000dip" android:layout_marginStart="16.000000dip" android:layout_marginEnd="8.000000dip" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/tv_abtest_config_item_title" style="@style/TextP3"/>
  <com.getmimo.ui.settings.SettingsListItemRadioGroup android:id="@id/rg_abtest_config_override_variant" android:layout_width="match_parent" android:layout_height="wrap_content" android:layout_marginTop="8.000000dip" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/tv_abtest_config_item_current_variant" app:settings_label="@string/developer_menu_disable_override_motive_variant"/>
</androidx.constraintlayout.widget.ConstraintLayout>
```
