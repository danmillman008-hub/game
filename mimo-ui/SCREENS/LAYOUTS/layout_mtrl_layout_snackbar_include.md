# پروندهٔ لایه — `res/layout/mtrl_layout_snackbar_include.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/mtrl_layout_snackbar_include.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/mtrl_layout_snackbar_include.xml`](../../SOURCE/res/layout/mtrl_layout_snackbar_include.xml) |
| SHA-256 دیکد | `753649d61477ec8a2685c7dac1bf10b977e7bd3bdfbb707d9003e970b1b7d25b` |
| ریشه | `view` |
| تعداد گره | 4 |
| تعداد شناسه | 3 |
| تگ‌های استفاده‌شده | 3 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 6 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ view
   ├─ TextView  #@id/snackbar_text
   ├─ Button  #@id/snackbar_action
   └─ Button  #@id/mtrl_snackbar_close
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `view` | `android:layout_gravity` | `0x00000050` |
| 2 | `view` | `android:layout_width` | `match_parent` |
| 3 | `view` | `android:layout_height` | `wrap_content` |
| 4 | `view` | `class` | `com.google.android.material.snackbar.SnackbarContentLayout` |
| 5 | `TextView` | `android:layout_gravity` | `0x00800013` |
| 6 | `TextView` | `android:id` | `@id/snackbar_text` |
| 7 | `TextView` | `android:layout_width` | `wrap_content` |
| 8 | `TextView` | `android:layout_height` | `wrap_content` |
| 9 | `TextView` | `android:layout_weight` | `1.000000` |
| 10 | `TextView` | `style` | `?attr/snackbarTextViewStyle` |
| 11 | `Button` | `android:layout_gravity` | `0x00800015` |
| 12 | `Button` | `android:id` | `@id/snackbar_action` |
| 13 | `Button` | `android:visibility` | `gone` |
| 14 | `Button` | `android:layout_width` | `wrap_content` |
| 15 | `Button` | `android:layout_height` | `wrap_content` |
| 16 | `Button` | `android:minWidth` | `48.000000dip` |
| 17 | `Button` | `style` | `?attr/snackbarButtonStyle` |
| 18 | `Button` | `android:layout_gravity` | `0x00800015` |
| 19 | `Button` | `android:id` | `@id/mtrl_snackbar_close` |
| 20 | `Button` | `android:visibility` | `gone` |
| 21 | `Button` | `android:layout_width` | `wrap_content` |
| 22 | `Button` | `android:layout_height` | `wrap_content` |
| 23 | `Button` | `style` | `?attr/snackbarCloseButtonStyle` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|

## ۴. شناسه‌های `@id`

```text
@id/mtrl_snackbar_close
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
<view xmlns:android="http://schemas.android.com/apk/res/android" android:layout_gravity="0x00000050" android:layout_width="match_parent" android:layout_height="wrap_content" class="com.google.android.material.snackbar.SnackbarContentLayout">
  <TextView android:layout_gravity="0x00800013" android:id="@id/snackbar_text" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_weight="1.000000" style="?attr/snackbarTextViewStyle"/>
  <Button android:layout_gravity="0x00800015" android:id="@id/snackbar_action" android:visibility="gone" android:layout_width="wrap_content" android:layout_height="wrap_content" android:minWidth="48.000000dip" style="?attr/snackbarButtonStyle"/>
  <Button android:layout_gravity="0x00800015" android:id="@id/mtrl_snackbar_close" android:visibility="gone" android:layout_width="wrap_content" android:layout_height="wrap_content" style="?attr/snackbarCloseButtonStyle"/>
</view>
```
