# پروندهٔ لایه — `res/layout/abc_alert_dialog_button_bar_material.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/abc_alert_dialog_button_bar_material.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/abc_alert_dialog_button_bar_material.xml`](../../SOURCE/res/layout/abc_alert_dialog_button_bar_material.xml) |
| SHA-256 دیکد | `b24f6cc5d365dad9f13f110fadef1a60f656c6bdc75611b7b6373dc779d7bd08` |
| ریشه | `ScrollView` |
| تعداد گره | 6 |
| تعداد شناسه | 5 |
| تگ‌های استفاده‌شده | 4 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 9 |

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
| 9 | `androidx.appcompat.widget.ButtonBarLayout` | `android:paddingLeft` | `12.000000dip` |
| 10 | `androidx.appcompat.widget.ButtonBarLayout` | `android:paddingTop` | `4.000000dip` |
| 11 | `androidx.appcompat.widget.ButtonBarLayout` | `android:paddingRight` | `12.000000dip` |
| 12 | `androidx.appcompat.widget.ButtonBarLayout` | `android:paddingBottom` | `4.000000dip` |
| 13 | `androidx.appcompat.widget.ButtonBarLayout` | `android:layout_width` | `match_parent` |
| 14 | `androidx.appcompat.widget.ButtonBarLayout` | `android:layout_height` | `wrap_content` |
| 15 | `androidx.appcompat.widget.ButtonBarLayout` | `android:layoutDirection` | `locale` |
| 16 | `Button` | `android:id` | `@0x0102001B` |
| 17 | `Button` | `android:layout_width` | `wrap_content` |
| 18 | `Button` | `android:layout_height` | `wrap_content` |
| 19 | `Button` | `style` | `?attr/buttonBarNeutralButtonStyle` |
| 20 | `android.widget.Space` | `android:id` | `@id/spacer` |
| 21 | `android.widget.Space` | `android:visibility` | `invisible` |
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
res/layout/abc_alert_dialog_material.xml
```

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<ScrollView xmlns:android="http://schemas.android.com/apk/res/android" android:id="@id/buttonPanel" android:layout_width="match_parent" android:layout_height="wrap_content" android:fillViewport="true" android:scrollIndicators="0x00000003" style="?attr/buttonBarStyle">
  <androidx.appcompat.widget.ButtonBarLayout android:gravity="0x00000050" android:orientation="horizontal" android:paddingLeft="12.000000dip" android:paddingTop="4.000000dip" android:paddingRight="12.000000dip" android:paddingBottom="4.000000dip" android:layout_width="match_parent" android:layout_height="wrap_content" android:layoutDirection="locale">
    <Button android:id="@0x0102001B" android:layout_width="wrap_content" android:layout_height="wrap_content" style="?attr/buttonBarNeutralButtonStyle"/>
    <android.widget.Space android:id="@id/spacer" android:visibility="invisible" android:layout_width="0.000000dip" android:layout_height="0.000000dip" android:layout_weight="1.000000"/>
    <Button android:id="@0x0102001A" android:layout_width="wrap_content" android:layout_height="wrap_content" style="?attr/buttonBarNegativeButtonStyle"/>
    <Button android:id="@0x01020019" android:layout_width="wrap_content" android:layout_height="wrap_content" style="?attr/buttonBarPositiveButtonStyle"/>
  </androidx.appcompat.widget.ButtonBarLayout>
</ScrollView>
```
