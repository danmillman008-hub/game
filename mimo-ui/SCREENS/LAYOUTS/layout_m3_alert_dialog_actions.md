# پروندهٔ لایه — `res/layout/m3_alert_dialog_actions.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/m3_alert_dialog_actions.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/m3_alert_dialog_actions.xml`](../../SOURCE/res/layout/m3_alert_dialog_actions.xml) |
| SHA-256 دیکد | `62ba773f7e4f36116a5ca96abb1226166e08fb561678756362eb9b646967e9ce` |
| ریشه | `ScrollView` |
| تعداد گره | 6 |
| تعداد شناسه | 5 |
| تگ‌های استفاده‌شده | 4 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 13 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ ScrollView  #@id/buttonPanel
   └─ androidx.appcompat.widget.ButtonBarLayout
      ├─ Button  #@0x0102001B
      ├─ android.widget.Space  #@id/spacer
      ├─ Button  #@0x0102001A
      └─ Button  #@0x01020019
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `ScrollView` | `android:id` | `@id/buttonPanel` |
| 2 | `ScrollView` | `android:layout_width` | `match_parent` |
| 3 | `ScrollView` | `android:layout_height` | `wrap_content` |
| 4 | `ScrollView` | `android:fillViewport` | `true` |
| 5 | `ScrollView` | `android:scrollIndicators` | `0x00000003` |
| 6 | `ScrollView` | `style` | `?attr/buttonBarStyle` |
| 7 | `androidx.appcompat.widget.ButtonBarLayout` | `android:gravity` | `0x00000050` |
| 8 | `androidx.appcompat.widget.ButtonBarLayout` | `android:orientation` | `horizontal` |
| 9 | `androidx.appcompat.widget.ButtonBarLayout` | `android:paddingLeft` | `?attr/dialogPreferredPadding` |
| 10 | `androidx.appcompat.widget.ButtonBarLayout` | `android:paddingTop` | `@dimen/m3_alert_dialog_action_top_padding` |
| 11 | `androidx.appcompat.widget.ButtonBarLayout` | `android:paddingRight` | `?attr/dialogPreferredPadding` |
| 12 | `androidx.appcompat.widget.ButtonBarLayout` | `android:paddingBottom` | `@dimen/m3_alert_dialog_action_bottom_padding` |
| 13 | `androidx.appcompat.widget.ButtonBarLayout` | `android:layout_width` | `match_parent` |
| 14 | `androidx.appcompat.widget.ButtonBarLayout` | `android:layout_height` | `wrap_content` |
| 15 | `androidx.appcompat.widget.ButtonBarLayout` | `android:layoutDirection` | `locale` |
| 16 | `Button` | `android:id` | `@0x0102001B` |
| 17 | `Button` | `android:layout_width` | `wrap_content` |
| 18 | `Button` | `android:layout_height` | `wrap_content` |
| 19 | `Button` | `style` | `?attr/buttonBarNeutralButtonStyle` |
| 20 | `android.widget.Space` | `android:id` | `@id/spacer` |
| 21 | `android.widget.Space` | `android:visibility` | `?attr/materialAlertDialogButtonSpacerVisibility` |
| 22 | `android.widget.Space` | `android:layout_width` | `0.000000dip` |
| 23 | `android.widget.Space` | `android:layout_height` | `0.000000dip` |
| 24 | `android.widget.Space` | `android:layout_weight` | `1.000000` |
| 25 | `Button` | `android:id` | `@0x0102001A` |
| 26 | `Button` | `android:layout_width` | `wrap_content` |
| 27 | `Button` | `android:layout_height` | `wrap_content` |
| 28 | `Button` | `style` | `?attr/buttonBarNegativeButtonStyle` |
| 29 | `Button` | `android:id` | `@0x01020019` |
| 30 | `Button` | `android:layout_width` | `wrap_content` |
| 31 | `Button` | `android:layout_height` | `wrap_content` |
| 32 | `Button` | `style` | `?attr/buttonBarPositiveButtonStyle` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@dimen/m3_alert_dialog_action_bottom_padding` | `14.000000dip` |
| `@dimen/m3_alert_dialog_action_top_padding` | `14.000000dip` |

## ۴. شناسه‌های `@id`

```text
@0x01020019
@0x0102001A
@0x0102001B
@id/buttonPanel
@id/spacer
```

## ۵. ارجاع به لایه‌های دیگر

```text
(none)
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

(هیچ صفحهٔ نام‌برداری به این لایه متصل نشد؛ ممکن است لایهٔ کتابخانه/`<include>` باشد)

## ۷. لایه‌هایی که این لایه را include می‌کنند

```text
res/layout/m3_alert_dialog.xml
res/layout/m3expressive_alert_dialog.xml
```

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<ScrollView xmlns:android="http://schemas.android.com/apk/res/android" android:id="@id/buttonPanel" android:layout_width="match_parent" android:layout_height="wrap_content" android:fillViewport="true" android:scrollIndicators="0x00000003" style="?attr/buttonBarStyle">
  <androidx.appcompat.widget.ButtonBarLayout android:gravity="0x00000050" android:orientation="horizontal" android:paddingLeft="?attr/dialogPreferredPadding" android:paddingTop="@dimen/m3_alert_dialog_action_top_padding" android:paddingRight="?attr/dialogPreferredPadding" android:paddingBottom="@dimen/m3_alert_dialog_action_bottom_padding" android:layout_width="match_parent" android:layout_height="wrap_content" android:layoutDirection="locale">
    <Button android:id="@0x0102001B" android:layout_width="wrap_content" android:layout_height="wrap_content" style="?attr/buttonBarNeutralButtonStyle"/>
    <android.widget.Space android:id="@id/spacer" android:visibility="?attr/materialAlertDialogButtonSpacerVisibility" android:layout_width="0.000000dip" android:layout_height="0.000000dip" android:layout_weight="1.000000"/>
    <Button android:id="@0x0102001A" android:layout_width="wrap_content" android:layout_height="wrap_content" style="?attr/buttonBarNegativeButtonStyle"/>
    <Button android:id="@0x01020019" android:layout_width="wrap_content" android:layout_height="wrap_content" style="?attr/buttonBarPositiveButtonStyle"/>
  </androidx.appcompat.widget.ButtonBarLayout>
</ScrollView>
```
