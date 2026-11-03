# پروندهٔ لایه — `res/layout/design_layout_snackbar_include.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/design_layout_snackbar_include.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/design_layout_snackbar_include.xml`](../../SOURCE/res/layout/design_layout_snackbar_include.xml) |
| SHA-256 دیکد | `1342f60548c5802498c59b100b07910c27b2f3a7e3dd7d23be0187340913d2c5` |
| ریشه | `view` |
| تعداد گره | 3 |
| تعداد شناسه | 2 |
| تگ‌های استفاده‌شده | 3 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 10 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ view
   ├─ TextView  #@id/snackbar_text
   └─ Button  #@id/snackbar_action
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `view` | `android:theme` | `@style/ThemeOverlay.AppCompat.Dark` |
| 2 | `view` | `android:layout_gravity` | `0x00000050` |
| 3 | `view` | `android:layout_width` | `match_parent` |
| 4 | `view` | `android:layout_height` | `wrap_content` |
| 5 | `view` | `class` | `com.google.android.material.snackbar.SnackbarContentLayout` |
| 6 | `TextView` | `android:textAppearance` | `@style/TextAppearance.Design.Snackbar.Message` |
| 7 | `TextView` | `android:ellipsize` | `end` |
| 8 | `TextView` | `android:layout_gravity` | `0x00800013` |
| 9 | `TextView` | `android:id` | `@id/snackbar_text` |
| 10 | `TextView` | `android:paddingLeft` | `@dimen/design_snackbar_padding_horizontal` |
| 11 | `TextView` | `android:paddingTop` | `@dimen/design_snackbar_padding_vertical` |
| 12 | `TextView` | `android:paddingRight` | `@dimen/design_snackbar_padding_horizontal` |
| 13 | `TextView` | `android:paddingBottom` | `@dimen/design_snackbar_padding_vertical` |
| 14 | `TextView` | `android:layout_width` | `wrap_content` |
| 15 | `TextView` | `android:layout_height` | `wrap_content` |
| 16 | `TextView` | `android:maxLines` | `@integer/design_snackbar_text_max_lines` |
| 17 | `TextView` | `android:layout_weight` | `1.000000` |
| 18 | `TextView` | `android:textAlignment` | `viewStart` |
| 19 | `Button` | `android:textColor` | `?attr/colorAccent` |
| 20 | `Button` | `android:layout_gravity` | `0x00800015` |
| 21 | `Button` | `android:id` | `@id/snackbar_action` |
| 22 | `Button` | `android:visibility` | `gone` |
| 23 | `Button` | `android:layout_width` | `wrap_content` |
| 24 | `Button` | `android:layout_height` | `wrap_content` |
| 25 | `Button` | `android:layout_marginLeft` | `@dimen/design_snackbar_extra_spacing_horizontal` |
| 26 | `Button` | `android:minWidth` | `48.000000dip` |
| 27 | `Button` | `android:layout_marginStart` | `@dimen/design_snackbar_extra_spacing_horizontal` |
| 28 | `Button` | `style` | `?attr/borderlessButtonStyle` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@dimen/design_snackbar_extra_spacing_horizontal` | `0.000000dip` / `24.000000dip` (sw600dp) |
| `@dimen/design_snackbar_padding_horizontal` | `12.000000dip` |
| `@dimen/design_snackbar_padding_vertical` | `14.000000dip` |
| `@style/TextAppearance.Design.Snackbar.Message` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '@dimen/design_snackbar_text_size', 'value_type': 'reference'}, {'attr': 'android:textColor', 'attr_id': '0x01010098', 'value': '?android:01010036', 'value_type': 'attribute'}]` |
| `@style/ThemeOverlay.AppCompat.Dark` | `[]` |

## ۴. شناسه‌های `@id`

```text
@id/snackbar_action
@id/snackbar_text
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
<view xmlns:android="http://schemas.android.com/apk/res/android" android:theme="@style/ThemeOverlay.AppCompat.Dark" android:layout_gravity="0x00000050" android:layout_width="match_parent" android:layout_height="wrap_content" class="com.google.android.material.snackbar.SnackbarContentLayout">
  <TextView android:textAppearance="@style/TextAppearance.Design.Snackbar.Message" android:ellipsize="end" android:layout_gravity="0x00800013" android:id="@id/snackbar_text" android:paddingLeft="@dimen/design_snackbar_padding_horizontal" android:paddingTop="@dimen/design_snackbar_padding_vertical" android:paddingRight="@dimen/design_snackbar_padding_horizontal" android:paddingBottom="@dimen/design_snackbar_padding_vertical" android:layout_width="wrap_content" android:layout_height="wrap_content" android:maxLines="@integer/design_snackbar_text_max_lines" android:layout_weight="1.000000" android:textAlignment="viewStart"/>
  <Button android:textColor="?attr/colorAccent" android:layout_gravity="0x00800015" android:id="@id/snackbar_action" android:visibility="gone" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginLeft="@dimen/design_snackbar_extra_spacing_horizontal" android:minWidth="48.000000dip" android:layout_marginStart="@dimen/design_snackbar_extra_spacing_horizontal" style="?attr/borderlessButtonStyle"/>
</view>
```
