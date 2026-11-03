# پروندهٔ لایه — `res/layout/fake_subscription_bottomsheet_dialog.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/fake_subscription_bottomsheet_dialog.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/fake_subscription_bottomsheet_dialog.xml`](../../SOURCE/res/layout/fake_subscription_bottomsheet_dialog.xml) |
| SHA-256 دیکد | `49d82b6231b90bebccb189fabf4a0308ba5e2f6aefaa4763ad4e9bbba7b6f24e` |
| ریشه | `LinearLayout` |
| تعداد گره | 8 |
| تعداد شناسه | 7 |
| تگ‌های استفاده‌شده | 5 |
| ویوهای سفارشی `com.getmimo` | 1 |
| `ComposeView` | 1 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 11 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ LinearLayout
   ├─ com.getmimo.ui.settings.SettingsListSwitchItem  #@id/switch_no_subscription
   ├─ com.getmimo.ui.settings.SettingsListSwitchItem  #@id/switch_subscription_with_trial
   ├─ com.getmimo.ui.settings.SettingsListSwitchItem  #@id/switch_subscription_without_trial
   ├─ TextView  #@id/tv_end_date_label
   ├─ CalendarView  #@id/cv_main
   ├─ com.getmimo.ui.settings.SettingsListSwitchItem  #@id/switch_is_cancelled
   └─ androidx.compose.ui.platform.ComposeView  #@id/btn_apply
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `LinearLayout` | `android:orientation` | `vertical` |
| 2 | `LinearLayout` | `android:padding` | `@dimen/spacing_m` |
| 3 | `LinearLayout` | `android:layout_width` | `match_parent` |
| 4 | `LinearLayout` | `android:layout_height` | `wrap_content` |
| 5 | `com.getmimo.ui.settings.SettingsListSwitchItem` | `android:id` | `@id/switch_no_subscription` |
| 6 | `com.getmimo.ui.settings.SettingsListSwitchItem` | `android:layout_width` | `match_parent` |
| 7 | `com.getmimo.ui.settings.SettingsListSwitchItem` | `android:layout_height` | `wrap_content` |
| 8 | `com.getmimo.ui.settings.SettingsListSwitchItem` | `app:settings_icon` | `@drawable/ic_plus` |
| 9 | `com.getmimo.ui.settings.SettingsListSwitchItem` | `app:settings_label` | `No subscription` |
| 10 | `com.getmimo.ui.settings.SettingsListSwitchItem` | `android:id` | `@id/switch_subscription_with_trial` |
| 11 | `com.getmimo.ui.settings.SettingsListSwitchItem` | `android:layout_width` | `match_parent` |
| 12 | `com.getmimo.ui.settings.SettingsListSwitchItem` | `android:layout_height` | `wrap_content` |
| 13 | `com.getmimo.ui.settings.SettingsListSwitchItem` | `app:settings_icon` | `@drawable/ic_plus` |
| 14 | `com.getmimo.ui.settings.SettingsListSwitchItem` | `app:settings_label` | `Subscription with free trial` |
| 15 | `com.getmimo.ui.settings.SettingsListSwitchItem` | `android:id` | `@id/switch_subscription_without_trial` |
| 16 | `com.getmimo.ui.settings.SettingsListSwitchItem` | `android:layout_width` | `match_parent` |
| 17 | `com.getmimo.ui.settings.SettingsListSwitchItem` | `android:layout_height` | `wrap_content` |
| 18 | `com.getmimo.ui.settings.SettingsListSwitchItem` | `app:settings_icon` | `@drawable/ic_plus` |
| 19 | `com.getmimo.ui.settings.SettingsListSwitchItem` | `app:settings_label` | `Subscription without free trial` |
| 20 | `TextView` | `android:textColor` | `@color/primary_default` |
| 21 | `TextView` | `android:id` | `@id/tv_end_date_label` |
| 22 | `TextView` | `android:paddingTop` | `@dimen/spacing_m` |
| 23 | `TextView` | `android:layout_width` | `wrap_content` |
| 24 | `TextView` | `android:layout_height` | `wrap_content` |
| 25 | `TextView` | `android:text` | `Select end date:` |
| 26 | `TextView` | `style` | `@style/TextH3` |
| 27 | `CalendarView` | `android:layout_gravity` | `0x00000001` |
| 28 | `CalendarView` | `android:id` | `@id/cv_main` |
| 29 | `CalendarView` | `android:layout_width` | `wrap_content` |
| 30 | `CalendarView` | `android:layout_height` | `wrap_content` |
| 31 | `com.getmimo.ui.settings.SettingsListSwitchItem` | `android:id` | `@id/switch_is_cancelled` |
| 32 | `com.getmimo.ui.settings.SettingsListSwitchItem` | `android:layout_width` | `match_parent` |
| 33 | `com.getmimo.ui.settings.SettingsListSwitchItem` | `android:layout_height` | `wrap_content` |
| 34 | `com.getmimo.ui.settings.SettingsListSwitchItem` | `app:settings_icon` | `@drawable/ic_plus` |
| 35 | `com.getmimo.ui.settings.SettingsListSwitchItem` | `app:settings_label` | `Is subscription cancelled` |
| 36 | `androidx.compose.ui.platform.ComposeView` | `android:layout_gravity` | `0x00000011` |
| 37 | `androidx.compose.ui.platform.ComposeView` | `android:id` | `@id/btn_apply` |
| 38 | `androidx.compose.ui.platform.ComposeView` | `android:layout_width` | `wrap_content` |
| 39 | `androidx.compose.ui.platform.ComposeView` | `android:layout_height` | `wrap_content` |
| 40 | `androidx.compose.ui.platform.ComposeView` | `android:layout_marginTop` | `16.000000dip` |
| 41 | `androidx.compose.ui.platform.ComposeView` | `android:layout_marginBottom` | `24.000000dip` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/primary_default` | `#FF7E4BDE` / `#FF885BDE` (night) |
| `@dimen/spacing_m` | `16.000000dip` |
| `@style/TextH3` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '18.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '5.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_fono_medium', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '23.399996sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '13.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_fono_medium', 'value_type': 'reference'}]` (sw600dp) |

## ۴. شناسه‌های `@id`

```text
@id/btn_apply
@id/cv_main
@id/switch_is_cancelled
@id/switch_no_subscription
@id/switch_subscription_with_trial
@id/switch_subscription_without_trial
@id/tv_end_date_label
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
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android" xmlns:app="http://schemas.android.com/apk/res-auto" android:orientation="vertical" android:padding="@dimen/spacing_m" android:layout_width="match_parent" android:layout_height="wrap_content">
  <com.getmimo.ui.settings.SettingsListSwitchItem android:id="@id/switch_no_subscription" android:layout_width="match_parent" android:layout_height="wrap_content" app:settings_icon="@drawable/ic_plus" app:settings_label="No subscription"/>
  <com.getmimo.ui.settings.SettingsListSwitchItem android:id="@id/switch_subscription_with_trial" android:layout_width="match_parent" android:layout_height="wrap_content" app:settings_icon="@drawable/ic_plus" app:settings_label="Subscription with free trial"/>
  <com.getmimo.ui.settings.SettingsListSwitchItem android:id="@id/switch_subscription_without_trial" android:layout_width="match_parent" android:layout_height="wrap_content" app:settings_icon="@drawable/ic_plus" app:settings_label="Subscription without free trial"/>
  <TextView android:textColor="@color/primary_default" android:id="@id/tv_end_date_label" android:paddingTop="@dimen/spacing_m" android:layout_width="wrap_content" android:layout_height="wrap_content" android:text="Select end date:" style="@style/TextH3"/>
  <CalendarView android:layout_gravity="0x00000001" android:id="@id/cv_main" android:layout_width="wrap_content" android:layout_height="wrap_content"/>
  <com.getmimo.ui.settings.SettingsListSwitchItem android:id="@id/switch_is_cancelled" android:layout_width="match_parent" android:layout_height="wrap_content" app:settings_icon="@drawable/ic_plus" app:settings_label="Is subscription cancelled"/>
  <androidx.compose.ui.platform.ComposeView android:layout_gravity="0x00000011" android:id="@id/btn_apply" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginTop="16.000000dip" android:layout_marginBottom="24.000000dip"/>
</LinearLayout>
```
