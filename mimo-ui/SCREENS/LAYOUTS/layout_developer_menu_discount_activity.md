# پروندهٔ لایه — `res/layout/developer_menu_discount_activity.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/developer_menu_discount_activity.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/developer_menu_discount_activity.xml`](../../SOURCE/res/layout/developer_menu_discount_activity.xml) |
| SHA-256 دیکد | `28763a6463b33ea6f659d7b9e72f1b1b4b00a906a6d2b91c76dc2264470a6103` |
| ریشه | `androidx.constraintlayout.widget.ConstraintLayout` |
| تعداد گره | 15 |
| تعداد شناسه | 13 |
| تگ‌های استفاده‌شده | 9 |
| ویوهای سفارشی `com.getmimo` | 3 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 3 |
| ارجاع به منابع | 27 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ androidx.constraintlayout.widget.ConstraintLayout
   ├─ com.google.android.material.appbar.AppBarLayout  #@id/appbar_discount_config
   │  └─ include  #@id/layout_toolbar
   └─ ScrollView  #@id/sv_developermenu_discount
      └─ LinearLayout
         ├─ TextView  #@id/tv_smart_discount_chapter_completed
         ├─ TextView  #@id/tv_smart_discount
         ├─ TextView  #@id/tv_discount_theme
         ├─ com.getmimo.ui.settings.SettingsListItemRadioGroup  #@id/rg_override_subscription_reactivate_discount
         ├─ TextView  #@id/tv_external_subscription
         ├─ com.getmimo.ui.settings.SettingsListSwitchItem  #@id/item_developer_menu_fake_remote_discount
         ├─ com.getmimo.ui.settings.SettingsListSwitchItem  #@id/item_developer_menu_fake_remote_discount_image
         ├─ com.getmimo.ui.settings.SettingsListSwitchItem  #@id/item_developer_menu_force_last_call_discount
         ├─ com.getmimo.ui.settings.SettingsListItem  #@id/item_developer_menu_reset_smart_discount
         └─ com.getmimo.ui.settings.SettingsListItem  #@id/item_developer_menu_smart_discount_send_push_notification
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:fitsSystemWindows` | `true` |
| 2 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_width` | `match_parent` |
| 3 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_height` | `match_parent` |
| 4 | `com.google.android.material.appbar.AppBarLayout` | `android:id` | `@id/appbar_discount_config` |
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
| 17 | `ScrollView` | `android:id` | `@id/sv_developermenu_discount` |
| 18 | `ScrollView` | `android:layout_width` | `match_parent` |
| 19 | `ScrollView` | `android:layout_height` | `0.000000dip` |
| 20 | `ScrollView` | `android:fillViewport` | `true` |
| 21 | `ScrollView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 22 | `ScrollView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 23 | `ScrollView` | `app:layout_constraintStart_toStartOf` | `0` |
| 24 | `ScrollView` | `app:layout_constraintTop_toBottomOf` | `@id/appbar_discount_config` |
| 25 | `ScrollView` | `app:layout_constraintVertical_bias` | `0.000000` |
| 26 | `LinearLayout` | `android:orientation` | `vertical` |
| 27 | `LinearLayout` | `android:layout_width` | `match_parent` |
| 28 | `LinearLayout` | `android:layout_height` | `wrap_content` |
| 29 | `TextView` | `android:gravity` | `0x00800003` |
| 30 | `TextView` | `android:layout_gravity` | `0x00000001` |
| 31 | `TextView` | `android:id` | `@id/tv_smart_discount_chapter_completed` |
| 32 | `TextView` | `android:layout_width` | `match_parent` |
| 33 | `TextView` | `android:layout_height` | `wrap_content` |
| 34 | `TextView` | `android:layout_marginTop` | `16.000000dip` |
| 35 | `TextView` | `android:layout_marginStart` | `16.000000dip` |
| 36 | `TextView` | `android:layout_marginEnd` | `16.000000dip` |
| 37 | `TextView` | `style` | `@style/TextP3` |
| 38 | `TextView` | `android:gravity` | `0x00800003` |
| 39 | `TextView` | `android:layout_gravity` | `0x00000001` |
| 40 | `TextView` | `android:id` | `@id/tv_smart_discount` |
| 41 | `TextView` | `android:layout_width` | `match_parent` |
| 42 | `TextView` | `android:layout_height` | `wrap_content` |
| 43 | `TextView` | `android:layout_marginTop` | `16.000000dip` |
| 44 | `TextView` | `android:layout_marginStart` | `16.000000dip` |
| 45 | `TextView` | `android:layout_marginEnd` | `16.000000dip` |
| 46 | `TextView` | `style` | `@style/TextP3` |
| 47 | `TextView` | `android:gravity` | `0x00800003` |
| 48 | `TextView` | `android:layout_gravity` | `0x00000001` |
| 49 | `TextView` | `android:id` | `@id/tv_discount_theme` |
| 50 | `TextView` | `android:layout_width` | `match_parent` |
| 51 | `TextView` | `android:layout_height` | `wrap_content` |
| 52 | `TextView` | `android:layout_marginTop` | `16.000000dip` |
| 53 | `TextView` | `android:layout_marginStart` | `16.000000dip` |
| 54 | `TextView` | `android:layout_marginEnd` | `16.000000dip` |
| 55 | `TextView` | `style` | `@style/TextP3` |
| 56 | `com.getmimo.ui.settings.SettingsListItemRadioGroup` | `android:id` | `@id/rg_override_subscription_reactivate_discount` |
| 57 | `com.getmimo.ui.settings.SettingsListItemRadioGroup` | `android:layout_width` | `match_parent` |
| 58 | `com.getmimo.ui.settings.SettingsListItemRadioGroup` | `android:layout_height` | `wrap_content` |
| 59 | `com.getmimo.ui.settings.SettingsListItemRadioGroup` | `android:layout_marginVertical` | `@dimen/spacing_m` |
| 60 | `com.getmimo.ui.settings.SettingsListItemRadioGroup` | `app:layout_constraintEnd_toEndOf` | `0` |
| 61 | `com.getmimo.ui.settings.SettingsListItemRadioGroup` | `app:layout_constraintStart_toStartOf` | `0` |
| 62 | `com.getmimo.ui.settings.SettingsListItemRadioGroup` | `app:settings_label` | `@string/developer_menu_discount_override_subscription` |
| 63 | `TextView` | `android:gravity` | `0x00800003` |
| 64 | `TextView` | `android:layout_gravity` | `0x00000001` |
| 65 | `TextView` | `android:id` | `@id/tv_external_subscription` |
| 66 | `TextView` | `android:layout_width` | `match_parent` |
| 67 | `TextView` | `android:layout_height` | `wrap_content` |
| 68 | `TextView` | `android:layout_marginHorizontal` | `@dimen/spacing_m` |
| 69 | `TextView` | `android:layout_marginVertical` | `@dimen/spacing_m` |
| 70 | `TextView` | `style` | `@style/TextP3` |
| 71 | `com.getmimo.ui.settings.SettingsListSwitchItem` | `android:id` | `@id/item_developer_menu_fake_remote_discount` |
| 72 | `com.getmimo.ui.settings.SettingsListSwitchItem` | `android:layout_width` | `match_parent` |
| 73 | `com.getmimo.ui.settings.SettingsListSwitchItem` | `android:layout_height` | `wrap_content` |
| 74 | `com.getmimo.ui.settings.SettingsListSwitchItem` | `app:settings_icon` | `@drawable/ic_star` |
| 75 | `com.getmimo.ui.settings.SettingsListSwitchItem` | `app:settings_label` | `@string/developer_menu_discount_fake_remote_discount` |
| 76 | `com.getmimo.ui.settings.SettingsListSwitchItem` | `android:id` | `@id/item_developer_menu_fake_remote_discount_image` |
| 77 | `com.getmimo.ui.settings.SettingsListSwitchItem` | `android:layout_width` | `match_parent` |
| 78 | `com.getmimo.ui.settings.SettingsListSwitchItem` | `android:layout_height` | `wrap_content` |
| 79 | `com.getmimo.ui.settings.SettingsListSwitchItem` | `app:settings_icon` | `@drawable/ic_star` |
| 80 | `com.getmimo.ui.settings.SettingsListSwitchItem` | `app:settings_label` | `@string/developer_menu_discount_fake_remote_discount_image` |
| 81 | `com.getmimo.ui.settings.SettingsListSwitchItem` | `android:id` | `@id/item_developer_menu_force_last_call_discount` |
| 82 | `com.getmimo.ui.settings.SettingsListSwitchItem` | `android:layout_width` | `match_parent` |
| 83 | `com.getmimo.ui.settings.SettingsListSwitchItem` | `android:layout_height` | `wrap_content` |
| 84 | `com.getmimo.ui.settings.SettingsListSwitchItem` | `app:settings_icon` | `@drawable/ic_star` |
| 85 | `com.getmimo.ui.settings.SettingsListSwitchItem` | `app:settings_label` | `@string/developer_menu_discount_force_last_call_discount` |
| 86 | `com.getmimo.ui.settings.SettingsListItem` | `android:id` | `@id/item_developer_menu_reset_smart_discount` |
| 87 | `com.getmimo.ui.settings.SettingsListItem` | `android:layout_width` | `match_parent` |
| 88 | `com.getmimo.ui.settings.SettingsListItem` | `android:layout_height` | `wrap_content` |
| 89 | `com.getmimo.ui.settings.SettingsListItem` | `app:settings_icon` | `@drawable/ic_close_circle_filled` |
| 90 | `com.getmimo.ui.settings.SettingsListItem` | `app:settings_label` | `@string/developer_menu_discount_reset_local_discount` |
| 91 | `com.getmimo.ui.settings.SettingsListItem` | `android:id` | `@id/item_developer_menu_smart_discount_send_push_notification` |
| 92 | `com.getmimo.ui.settings.SettingsListItem` | `android:layout_width` | `match_parent` |
| 93 | `com.getmimo.ui.settings.SettingsListItem` | `android:layout_height` | `wrap_content` |
| 94 | `com.getmimo.ui.settings.SettingsListItem` | `app:settings_icon` | `@drawable/ic_push_notification_timer_icon` |
| 95 | `com.getmimo.ui.settings.SettingsListItem` | `app:settings_label` | `@string/developer_menu_discount_send_push_notification` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/navbar_background` | `#FFFFFFFF` / `#FF333661` (night) |
| `@dimen/spacing_m` | `16.000000dip` |
| `@string/app_name` | `Mimo` / `Mimo` (de) / `Mimo` (es) / `Mimo` (fr) / `Mimo` (in) / `Mimo` (it) / `Mimo` (pl) / `Mimo` (pt-rBR) / `Mimo` (ru) / `Mimo` (tr) |
| `@string/developer_menu_discount_fake_remote_discount` | `Fake Remote Discount` |
| `@string/developer_menu_discount_fake_remote_discount_image` | `Fake Remote Discount Image` |
| `@string/developer_menu_discount_force_last_call_discount` | `Force Last Call Discount` |
| `@string/developer_menu_discount_override_subscription` | `Override current subscription` |
| `@string/developer_menu_discount_reset_local_discount` | `Reset discounts` |
| `@string/developer_menu_discount_send_push_notification` | `Send test push notification in 20s` |
| `@style/TextP3` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '14.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '3.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '18.199983sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '5.199982sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` (sw600dp) |

## ۴. شناسه‌های `@id`

```text
@id/appbar_discount_config
@id/item_developer_menu_fake_remote_discount
@id/item_developer_menu_fake_remote_discount_image
@id/item_developer_menu_force_last_call_discount
@id/item_developer_menu_reset_smart_discount
@id/item_developer_menu_smart_discount_send_push_notification
@id/layout_toolbar
@id/rg_override_subscription_reactivate_discount
@id/sv_developermenu_discount
@id/tv_discount_theme
@id/tv_external_subscription
@id/tv_smart_discount
@id/tv_smart_discount_chapter_completed
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
com.getmimo.ui.developermenu.discount.DeveloperMenuDiscountActivity
```

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout xmlns:app="http://schemas.android.com/apk/res-auto" xmlns:android="http://schemas.android.com/apk/res/android" android:fitsSystemWindows="true" android:layout_width="match_parent" android:layout_height="match_parent">
  <com.google.android.material.appbar.AppBarLayout android:id="@id/appbar_discount_config" android:background="@color/navbar_background" android:layout_width="match_parent" android:layout_height="wrap_content" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="0">
    <include android:id="@id/layout_toolbar" android:layout_width="match_parent" android:layout_height="wrap_content" android:title="@string/app_name" layout="@layout/toolbar"/>
  </com.google.android.material.appbar.AppBarLayout>
  <ScrollView android:orientation="vertical" android:id="@id/sv_developermenu_discount" android:layout_width="match_parent" android:layout_height="0.000000dip" android:fillViewport="true" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/appbar_discount_config" app:layout_constraintVertical_bias="0.000000">
    <LinearLayout android:orientation="vertical" android:layout_width="match_parent" android:layout_height="wrap_content">
      <TextView android:gravity="0x00800003" android:layout_gravity="0x00000001" android:id="@id/tv_smart_discount_chapter_completed" android:layout_width="match_parent" android:layout_height="wrap_content" android:layout_marginTop="16.000000dip" android:layout_marginStart="16.000000dip" android:layout_marginEnd="16.000000dip" style="@style/TextP3"/>
      <TextView android:gravity="0x00800003" android:layout_gravity="0x00000001" android:id="@id/tv_smart_discount" android:layout_width="match_parent" android:layout_height="wrap_content" android:layout_marginTop="16.000000dip" android:layout_marginStart="16.000000dip" android:layout_marginEnd="16.000000dip" style="@style/TextP3"/>
      <TextView android:gravity="0x00800003" android:layout_gravity="0x00000001" android:id="@id/tv_discount_theme" android:layout_width="match_parent" android:layout_height="wrap_content" android:layout_marginTop="16.000000dip" android:layout_marginStart="16.000000dip" android:layout_marginEnd="16.000000dip" style="@style/TextP3"/>
      <com.getmimo.ui.settings.SettingsListItemRadioGroup android:id="@id/rg_override_subscription_reactivate_discount" android:layout_width="match_parent" android:layout_height="wrap_content" android:layout_marginVertical="@dimen/spacing_m" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:settings_label="@string/developer_menu_discount_override_subscription"/>
      <TextView android:gravity="0x00800003" android:layout_gravity="0x00000001" android:id="@id/tv_external_subscription" android:layout_width="match_parent" android:layout_height="wrap_content" android:layout_marginHorizontal="@dimen/spacing_m" android:layout_marginVertical="@dimen/spacing_m" style="@style/TextP3"/>
      <com.getmimo.ui.settings.SettingsListSwitchItem android:id="@id/item_developer_menu_fake_remote_discount" android:layout_width="match_parent" android:layout_height="wrap_content" app:settings_icon="@drawable/ic_star" app:settings_label="@string/developer_menu_discount_fake_remote_discount"/>
      <com.getmimo.ui.settings.SettingsListSwitchItem android:id="@id/item_developer_menu_fake_remote_discount_image" android:layout_width="match_parent" android:layout_height="wrap_content" app:settings_icon="@drawable/ic_star" app:settings_label="@string/developer_menu_discount_fake_remote_discount_image"/>
      <com.getmimo.ui.settings.SettingsListSwitchItem android:id="@id/item_developer_menu_force_last_call_discount" android:layout_width="match_parent" android:layout_height="wrap_content" app:settings_icon="@drawable/ic_star" app:settings_label="@string/developer_menu_discount_force_last_call_discount"/>
      <com.getmimo.ui.settings.SettingsListItem android:id="@id/item_developer_menu_reset_smart_discount" android:layout_width="match_parent" android:layout_height="wrap_content" app:settings_icon="@drawable/ic_close_circle_filled" app:settings_label="@string/developer_menu_discount_reset_local_discount"/>
      <com.getmimo.ui.settings.SettingsListItem android:id="@id/item_developer_menu_smart_discount_send_push_notification" android:layout_width="match_parent" android:layout_height="wrap_content" app:settings_icon="@drawable/ic_push_notification_timer_icon" app:settings_label="@string/developer_menu_discount_send_push_notification"/>
    </LinearLayout>
  </ScrollView>
</androidx.constraintlayout.widget.ConstraintLayout>
```
