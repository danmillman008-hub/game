# پروندهٔ لایه — `res/layout/developer_menu_campaign_activity.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/developer_menu_campaign_activity.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/developer_menu_campaign_activity.xml`](../../SOURCE/res/layout/developer_menu_campaign_activity.xml) |
| SHA-256 دیکد | `dab6c94a47c1133c0aea84b85f2e8b925439ba879d7f331490ca50020446cf30` |
| ریشه | `androidx.constraintlayout.widget.ConstraintLayout` |
| تعداد گره | 12 |
| تعداد شناسه | 9 |
| تگ‌های استفاده‌شده | 6 |
| ویوهای سفارشی `com.getmimo` | 1 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 3 |
| ارجاع به منابع | 18 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ androidx.constraintlayout.widget.ConstraintLayout
   ├─ com.google.android.material.appbar.AppBarLayout  #@id/appbar_abtest__config
   │  └─ include  #@id/layout_toolbar
   └─ ScrollView
      └─ androidx.constraintlayout.widget.ConstraintLayout
         ├─ TextView  #@id/tv_dev_menu_campaign
         ├─ TextView  #@id/tv_dev_menu_campaign_parameter
         ├─ TextView  #@id/tv_dev_menu_campaign_value
         ├─ com.getmimo.ui.settings.SettingsListItemRadioGroup  #@id/rg_dev_menu_campaign
         ├─ TextView  #@id/tv_dev_menu_campaign_allows_free_trial
         ├─ TextView  #@id/tv_dev_menu_campaign_allows_free_trial_value
         └─ com.getmimo.ui.settings.SettingsListItemRadioGroup  #@id/rg_dev_menu_campaign_allows_free_trial
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:fitsSystemWindows` | `true` |
| 2 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_width` | `match_parent` |
| 3 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_height` | `match_parent` |
| 4 | `com.google.android.material.appbar.AppBarLayout` | `android:id` | `@id/appbar_abtest__config` |
| 5 | `com.google.android.material.appbar.AppBarLayout` | `android:background` | `@color/navbar_background` |
| 6 | `com.google.android.material.appbar.AppBarLayout` | `android:layout_width` | `match_parent` |
| 7 | `com.google.android.material.appbar.AppBarLayout` | `android:layout_height` | `wrap_content` |
| 8 | `com.google.android.material.appbar.AppBarLayout` | `app:layout_constraintEnd_toEndOf` | `0` |
| 9 | `com.google.android.material.appbar.AppBarLayout` | `app:layout_constraintStart_toStartOf` | `0` |
| 10 | `com.google.android.material.appbar.AppBarLayout` | `app:layout_constraintTop_toTopOf` | `0` |
| 11 | `include` | `android:id` | `@id/layout_toolbar` |
| 12 | `include` | `android:layout_width` | `match_parent` |
| 13 | `include` | `android:layout_height` | `wrap_content` |
| 14 | `include` | `android:title` | `@string/app_name` |
| 15 | `include` | `layout` | `@layout/toolbar` |
| 16 | `ScrollView` | `android:orientation` | `vertical` |
| 17 | `ScrollView` | `android:layout_width` | `match_parent` |
| 18 | `ScrollView` | `android:layout_height` | `0.000000dip` |
| 19 | `ScrollView` | `android:fillViewport` | `true` |
| 20 | `ScrollView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 21 | `ScrollView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 22 | `ScrollView` | `app:layout_constraintStart_toStartOf` | `0` |
| 23 | `ScrollView` | `app:layout_constraintTop_toBottomOf` | `@id/appbar_abtest__config` |
| 24 | `ScrollView` | `app:layout_constraintVertical_bias` | `0.000000` |
| 25 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_width` | `match_parent` |
| 26 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_height` | `wrap_content` |
| 27 | `TextView` | `android:id` | `@id/tv_dev_menu_campaign` |
| 28 | `TextView` | `android:layout_width` | `0.000000dip` |
| 29 | `TextView` | `android:layout_height` | `wrap_content` |
| 30 | `TextView` | `android:layout_marginTop` | `8.000000dip` |
| 31 | `TextView` | `android:layout_marginBottom` | `8.000000dip` |
| 32 | `TextView` | `android:text` | `@string/developer_menu_campaign_parameter` |
| 33 | `TextView` | `android:layout_marginStart` | `16.000000dip` |
| 34 | `TextView` | `android:layout_marginEnd` | `8.000000dip` |
| 35 | `TextView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 36 | `TextView` | `app:layout_constraintStart_toStartOf` | `0` |
| 37 | `TextView` | `app:layout_constraintTop_toTopOf` | `0` |
| 38 | `TextView` | `style` | `@style/TextP1` |
| 39 | `TextView` | `android:id` | `@id/tv_dev_menu_campaign_parameter` |
| 40 | `TextView` | `android:layout_width` | `0.000000dip` |
| 41 | `TextView` | `android:layout_height` | `wrap_content` |
| 42 | `TextView` | `android:layout_marginTop` | `8.000000dip` |
| 43 | `TextView` | `android:layout_marginBottom` | `8.000000dip` |
| 44 | `TextView` | `android:text` | `@string/developer_menu_campaign_user_coming_from_campaign` |
| 45 | `TextView` | `android:layout_marginStart` | `16.000000dip` |
| 46 | `TextView` | `android:layout_marginEnd` | `8.000000dip` |
| 47 | `TextView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 48 | `TextView` | `app:layout_constraintStart_toStartOf` | `0` |
| 49 | `TextView` | `app:layout_constraintTop_toBottomOf` | `@id/tv_dev_menu_campaign` |
| 50 | `TextView` | `style` | `@style/TextP1` |
| 51 | `TextView` | `android:id` | `@id/tv_dev_menu_campaign_value` |
| 52 | `TextView` | `android:layout_width` | `0.000000dip` |
| 53 | `TextView` | `android:layout_height` | `wrap_content` |
| 54 | `TextView` | `android:layout_marginTop` | `8.000000dip` |
| 55 | `TextView` | `android:layout_marginBottom` | `8.000000dip` |
| 56 | `TextView` | `android:layout_marginStart` | `16.000000dip` |
| 57 | `TextView` | `android:layout_marginEnd` | `8.000000dip` |
| 58 | `TextView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 59 | `TextView` | `app:layout_constraintStart_toStartOf` | `0` |
| 60 | `TextView` | `app:layout_constraintTop_toBottomOf` | `@id/tv_dev_menu_campaign_parameter` |
| 61 | `TextView` | `style` | `@style/TextP3` |
| 62 | `com.getmimo.ui.settings.SettingsListItemRadioGroup` | `android:id` | `@id/rg_dev_menu_campaign` |
| 63 | `com.getmimo.ui.settings.SettingsListItemRadioGroup` | `android:layout_width` | `match_parent` |
| 64 | `com.getmimo.ui.settings.SettingsListItemRadioGroup` | `android:layout_height` | `wrap_content` |
| 65 | `com.getmimo.ui.settings.SettingsListItemRadioGroup` | `android:layout_marginTop` | `8.000000dip` |
| 66 | `com.getmimo.ui.settings.SettingsListItemRadioGroup` | `app:layout_constraintEnd_toEndOf` | `0` |
| 67 | `com.getmimo.ui.settings.SettingsListItemRadioGroup` | `app:layout_constraintStart_toStartOf` | `0` |
| 68 | `com.getmimo.ui.settings.SettingsListItemRadioGroup` | `app:layout_constraintTop_toBottomOf` | `@id/tv_dev_menu_campaign_value` |
| 69 | `com.getmimo.ui.settings.SettingsListItemRadioGroup` | `app:settings_label` | `@string/developer_menu_disable_override_coming_from_campaign` |
| 70 | `TextView` | `android:id` | `@id/tv_dev_menu_campaign_allows_free_trial` |
| 71 | `TextView` | `android:layout_width` | `0.000000dip` |
| 72 | `TextView` | `android:layout_height` | `wrap_content` |
| 73 | `TextView` | `android:layout_marginTop` | `8.000000dip` |
| 74 | `TextView` | `android:layout_marginBottom` | `8.000000dip` |
| 75 | `TextView` | `android:text` | `@string/developer_menu_campaign_allows_free_trial` |
| 76 | `TextView` | `android:layout_marginStart` | `16.000000dip` |
| 77 | `TextView` | `android:layout_marginEnd` | `8.000000dip` |
| 78 | `TextView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 79 | `TextView` | `app:layout_constraintStart_toStartOf` | `0` |
| 80 | `TextView` | `app:layout_constraintTop_toBottomOf` | `@id/rg_dev_menu_campaign` |
| 81 | `TextView` | `style` | `@style/TextP1` |
| 82 | `TextView` | `android:id` | `@id/tv_dev_menu_campaign_allows_free_trial_value` |
| 83 | `TextView` | `android:layout_width` | `0.000000dip` |
| 84 | `TextView` | `android:layout_height` | `wrap_content` |
| 85 | `TextView` | `android:layout_marginTop` | `8.000000dip` |
| 86 | `TextView` | `android:layout_marginBottom` | `8.000000dip` |
| 87 | `TextView` | `android:layout_marginStart` | `16.000000dip` |
| 88 | `TextView` | `android:layout_marginEnd` | `8.000000dip` |
| 89 | `TextView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 90 | `TextView` | `app:layout_constraintStart_toStartOf` | `0` |
| 91 | `TextView` | `app:layout_constraintTop_toBottomOf` | `@id/tv_dev_menu_campaign_allows_free_trial` |
| 92 | `TextView` | `style` | `@style/TextP3` |
| 93 | `com.getmimo.ui.settings.SettingsListItemRadioGroup` | `android:id` | `@id/rg_dev_menu_campaign_allows_free_trial` |
| 94 | `com.getmimo.ui.settings.SettingsListItemRadioGroup` | `android:layout_width` | `match_parent` |
| 95 | `com.getmimo.ui.settings.SettingsListItemRadioGroup` | `android:layout_height` | `wrap_content` |
| 96 | `com.getmimo.ui.settings.SettingsListItemRadioGroup` | `android:layout_marginTop` | `8.000000dip` |
| 97 | `com.getmimo.ui.settings.SettingsListItemRadioGroup` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 98 | `com.getmimo.ui.settings.SettingsListItemRadioGroup` | `app:layout_constraintEnd_toEndOf` | `0` |
| 99 | `com.getmimo.ui.settings.SettingsListItemRadioGroup` | `app:layout_constraintStart_toStartOf` | `0` |
| 100 | `com.getmimo.ui.settings.SettingsListItemRadioGroup` | `app:layout_constraintTop_toBottomOf` | `@id/tv_dev_menu_campaign_allows_free_trial_value` |
| 101 | `com.getmimo.ui.settings.SettingsListItemRadioGroup` | `app:settings_label` | `@string/developer_menu_disable_override_coming_from_campaign` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/navbar_background` | `#FFFFFFFF` / `#FF333661` (night) |
| `@string/app_name` | `Mimo` / `Mimo` (de) / `Mimo` (es) / `Mimo` (fr) / `Mimo` (in) / `Mimo` (it) / `Mimo` (pl) / `Mimo` (pt-rBR) / `Mimo` (ru) / `Mimo` (tr) |
| `@string/developer_menu_campaign_allows_free_trial` | `Campaign allows free trial :` |
| `@string/developer_menu_campaign_parameter` | `User campaign : %s` |
| `@string/developer_menu_campaign_user_coming_from_campaign` | `User comes from a campaign :` |
| `@string/developer_menu_disable_override_coming_from_campaign` | `Override value to` |
| `@style/TextP1` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '18.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '5.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '23.399996sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '7.799988sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` (sw600dp) |
| `@style/TextP3` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '14.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '3.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '18.199983sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '5.199982sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` (sw600dp) |

## ۴. شناسه‌های `@id`

```text
@id/appbar_abtest__config
@id/layout_toolbar
@id/rg_dev_menu_campaign
@id/rg_dev_menu_campaign_allows_free_trial
@id/tv_dev_menu_campaign
@id/tv_dev_menu_campaign_allows_free_trial
@id/tv_dev_menu_campaign_allows_free_trial_value
@id/tv_dev_menu_campaign_parameter
@id/tv_dev_menu_campaign_value
```

## ۵. ارجاع به لایه‌های دیگر

```text
@layout/toolbar
match_parent
wrap_content
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

```text
com.getmimo.ui.developermenu.DeveloperMenuActivity
com.getmimo.ui.developermenu.DeveloperMenuFragment
com.getmimo.ui.developermenu.campaign.DeveloperMenuCampaignActivity
```

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout xmlns:app="http://schemas.android.com/apk/res-auto" xmlns:android="http://schemas.android.com/apk/res/android" android:fitsSystemWindows="true" android:layout_width="match_parent" android:layout_height="match_parent">
  <com.google.android.material.appbar.AppBarLayout android:id="@id/appbar_abtest__config" android:background="@color/navbar_background" android:layout_width="match_parent" android:layout_height="wrap_content" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="0">
    <include android:id="@id/layout_toolbar" android:layout_width="match_parent" android:layout_height="wrap_content" android:title="@string/app_name" layout="@layout/toolbar"/>
  </com.google.android.material.appbar.AppBarLayout>
  <ScrollView android:orientation="vertical" android:layout_width="match_parent" android:layout_height="0.000000dip" android:fillViewport="true" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/appbar_abtest__config" app:layout_constraintVertical_bias="0.000000">
    <androidx.constraintlayout.widget.ConstraintLayout android:layout_width="match_parent" android:layout_height="wrap_content">
      <TextView android:id="@id/tv_dev_menu_campaign" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginTop="8.000000dip" android:layout_marginBottom="8.000000dip" android:text="@string/developer_menu_campaign_parameter" android:layout_marginStart="16.000000dip" android:layout_marginEnd="8.000000dip" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="0" style="@style/TextP1"/>
      <TextView android:id="@id/tv_dev_menu_campaign_parameter" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginTop="8.000000dip" android:layout_marginBottom="8.000000dip" android:text="@string/developer_menu_campaign_user_coming_from_campaign" android:layout_marginStart="16.000000dip" android:layout_marginEnd="8.000000dip" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/tv_dev_menu_campaign" style="@style/TextP1"/>
      <TextView android:id="@id/tv_dev_menu_campaign_value" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginTop="8.000000dip" android:layout_marginBottom="8.000000dip" android:layout_marginStart="16.000000dip" android:layout_marginEnd="8.000000dip" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/tv_dev_menu_campaign_parameter" style="@style/TextP3"/>
      <com.getmimo.ui.settings.SettingsListItemRadioGroup android:id="@id/rg_dev_menu_campaign" android:layout_width="match_parent" android:layout_height="wrap_content" android:layout_marginTop="8.000000dip" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/tv_dev_menu_campaign_value" app:settings_label="@string/developer_menu_disable_override_coming_from_campaign"/>
      <TextView android:id="@id/tv_dev_menu_campaign_allows_free_trial" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginTop="8.000000dip" android:layout_marginBottom="8.000000dip" android:text="@string/developer_menu_campaign_allows_free_trial" android:layout_marginStart="16.000000dip" android:layout_marginEnd="8.000000dip" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/rg_dev_menu_campaign" style="@style/TextP1"/>
      <TextView android:id="@id/tv_dev_menu_campaign_allows_free_trial_value" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginTop="8.000000dip" android:layout_marginBottom="8.000000dip" android:layout_marginStart="16.000000dip" android:layout_marginEnd="8.000000dip" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/tv_dev_menu_campaign_allows_free_trial" style="@style/TextP3"/>
      <com.getmimo.ui.settings.SettingsListItemRadioGroup android:id="@id/rg_dev_menu_campaign_allows_free_trial" android:layout_width="match_parent" android:layout_height="wrap_content" android:layout_marginTop="8.000000dip" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/tv_dev_menu_campaign_allows_free_trial_value" app:settings_label="@string/developer_menu_disable_override_coming_from_campaign"/>
    </androidx.constraintlayout.widget.ConstraintLayout>
  </ScrollView>
</androidx.constraintlayout.widget.ConstraintLayout>
```
