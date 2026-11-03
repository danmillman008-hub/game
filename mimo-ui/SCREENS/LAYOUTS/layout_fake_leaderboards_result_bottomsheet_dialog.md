# پروندهٔ لایه — `res/layout/fake_leaderboards_result_bottomsheet_dialog.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/fake_leaderboards_result_bottomsheet_dialog.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/fake_leaderboards_result_bottomsheet_dialog.xml`](../../SOURCE/res/layout/fake_leaderboards_result_bottomsheet_dialog.xml) |
| SHA-256 دیکد | `7a6e566c6b67cbc2d0fb1968523885585662b58404b3ef300e391e142f9d8f7c` |
| ریشه | `LinearLayout` |
| تعداد گره | 7 |
| تعداد شناسه | 3 |
| تگ‌های استفاده‌شده | 5 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 1 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 7 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ LinearLayout
   ├─ TextView
   ├─ com.google.android.material.textfield.TextInputLayout
   │  └─ com.google.android.material.textfield.TextInputEditText  #@id/et_fake_leaderboards_result_rank
   ├─ com.google.android.material.textfield.TextInputLayout
   │  └─ com.google.android.material.textfield.TextInputEditText  #@id/et_fake_leaderboards_result_league
   └─ androidx.compose.ui.platform.ComposeView  #@id/btn_fake_leaderboards_result
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `LinearLayout` | `android:orientation` | `vertical` |
| 2 | `LinearLayout` | `android:layout_width` | `match_parent` |
| 3 | `LinearLayout` | `android:layout_height` | `wrap_content` |
| 4 | `TextView` | `android:gravity` | `0x00000011` |
| 5 | `TextView` | `android:layout_width` | `match_parent` |
| 6 | `TextView` | `android:layout_height` | `wrap_content` |
| 7 | `TextView` | `android:layout_marginTop` | `16.000000dip` |
| 8 | `TextView` | `android:text` | `Promotion zone: 1 - 15
Neutral zone: 16 - 40
Demotion zone: 41 - 50` |
| 9 | `TextView` | `style` | `@style/TextLabel3` |
| 10 | `com.google.android.material.textfield.TextInputLayout` | `android:layout_gravity` | `0x00000011` |
| 11 | `com.google.android.material.textfield.TextInputLayout` | `android:layout_width` | `200.000000dip` |
| 12 | `com.google.android.material.textfield.TextInputLayout` | `android:layout_height` | `wrap_content` |
| 13 | `com.google.android.material.textfield.TextInputLayout` | `android:layout_marginTop` | `16.000000dip` |
| 14 | `com.google.android.material.textfield.TextInputEditText` | `android:id` | `@id/et_fake_leaderboards_result_rank` |
| 15 | `com.google.android.material.textfield.TextInputEditText` | `android:layout_width` | `match_parent` |
| 16 | `com.google.android.material.textfield.TextInputEditText` | `android:layout_height` | `match_parent` |
| 17 | `com.google.android.material.textfield.TextInputEditText` | `android:hint` | `Leaderboard Rank (1-50)` |
| 18 | `com.google.android.material.textfield.TextInputEditText` | `android:inputType` | `0x00000002` |
| 19 | `com.google.android.material.textfield.TextInputEditText` | `style` | `@style/TextLabel2` |
| 20 | `com.google.android.material.textfield.TextInputLayout` | `android:layout_gravity` | `0x00000011` |
| 21 | `com.google.android.material.textfield.TextInputLayout` | `android:layout_width` | `200.000000dip` |
| 22 | `com.google.android.material.textfield.TextInputLayout` | `android:layout_height` | `wrap_content` |
| 23 | `com.google.android.material.textfield.TextInputLayout` | `android:layout_marginTop` | `16.000000dip` |
| 24 | `com.google.android.material.textfield.TextInputEditText` | `android:id` | `@id/et_fake_leaderboards_result_league` |
| 25 | `com.google.android.material.textfield.TextInputEditText` | `android:layout_width` | `match_parent` |
| 26 | `com.google.android.material.textfield.TextInputEditText` | `android:layout_height` | `match_parent` |
| 27 | `com.google.android.material.textfield.TextInputEditText` | `android:hint` | `Leaderboard League (1-5)` |
| 28 | `com.google.android.material.textfield.TextInputEditText` | `android:inputType` | `0x00000002` |
| 29 | `com.google.android.material.textfield.TextInputEditText` | `style` | `@style/TextLabel2` |
| 30 | `androidx.compose.ui.platform.ComposeView` | `android:layout_gravity` | `0x00000011` |
| 31 | `androidx.compose.ui.platform.ComposeView` | `android:id` | `@id/btn_fake_leaderboards_result` |
| 32 | `androidx.compose.ui.platform.ComposeView` | `android:layout_width` | `wrap_content` |
| 33 | `androidx.compose.ui.platform.ComposeView` | `android:layout_height` | `wrap_content` |
| 34 | `androidx.compose.ui.platform.ComposeView` | `android:layout_marginTop` | `@dimen/spacing_m` |
| 35 | `androidx.compose.ui.platform.ComposeView` | `android:layout_marginBottom` | `@dimen/spacing_l` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@dimen/spacing_l` | `24.000000dip` |
| `@dimen/spacing_m` | `16.000000dip` |
| `@style/TextLabel2` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '14.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '4.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '18.199983sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '10.399995sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` (sw600dp) |
| `@style/TextLabel3` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '12.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '3.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_bold', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '15.599977sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '7.799988sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_bold', 'value_type': 'reference'}]` (sw600dp) |

## ۴. شناسه‌های `@id`

```text
@id/btn_fake_leaderboards_result
@id/et_fake_leaderboards_result_league
@id/et_fake_leaderboards_result_rank
```

## ۵. ارجاع به لایه‌های دیگر

```text
(none)
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

```text
com.getmimo.ui.leaderboard.LeaderboardFragment$observeViewModelEvents$1$1$1
```

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android" android:orientation="vertical" android:layout_width="match_parent" android:layout_height="wrap_content">
  <TextView android:gravity="0x00000011" android:layout_width="match_parent" android:layout_height="wrap_content" android:layout_marginTop="16.000000dip" android:text="Promotion zone: 1 - 15&#10;Neutral zone: 16 - 40&#10;Demotion zone: 41 - 50" style="@style/TextLabel3"/>
  <com.google.android.material.textfield.TextInputLayout android:layout_gravity="0x00000011" android:layout_width="200.000000dip" android:layout_height="wrap_content" android:layout_marginTop="16.000000dip">
    <com.google.android.material.textfield.TextInputEditText android:id="@id/et_fake_leaderboards_result_rank" android:layout_width="match_parent" android:layout_height="match_parent" android:hint="Leaderboard Rank (1-50)" android:inputType="0x00000002" style="@style/TextLabel2"/>
  </com.google.android.material.textfield.TextInputLayout>
  <com.google.android.material.textfield.TextInputLayout android:layout_gravity="0x00000011" android:layout_width="200.000000dip" android:layout_height="wrap_content" android:layout_marginTop="16.000000dip">
    <com.google.android.material.textfield.TextInputEditText android:id="@id/et_fake_leaderboards_result_league" android:layout_width="match_parent" android:layout_height="match_parent" android:hint="Leaderboard League (1-5)" android:inputType="0x00000002" style="@style/TextLabel2"/>
  </com.google.android.material.textfield.TextInputLayout>
  <androidx.compose.ui.platform.ComposeView android:layout_gravity="0x00000011" android:id="@id/btn_fake_leaderboards_result" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_m" android:layout_marginBottom="@dimen/spacing_l"/>
</LinearLayout>
```
