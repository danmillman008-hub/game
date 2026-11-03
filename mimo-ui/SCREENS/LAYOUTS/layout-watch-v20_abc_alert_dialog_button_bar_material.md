# پروندهٔ لایه — `res/layout-watch-v20/abc_alert_dialog_button_bar_material.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout-watch-v20/abc_alert_dialog_button_bar_material.xml` |
| فایل دیکدشده | [`SOURCE/res/layout-watch-v20/abc_alert_dialog_button_bar_material.xml`](../../SOURCE/res/layout-watch-v20/abc_alert_dialog_button_bar_material.xml) |
| SHA-256 دیکد | `f8bc3c49ea740138069d732abd24e7a9f004277b8b24c8119914d28e92042a6e` |
| ریشه | `androidx.appcompat.widget.ButtonBarLayout` |
| تعداد گره | 4 |
| تعداد شناسه | 4 |
| تگ‌های استفاده‌شده | 2 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 7 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ androidx.appcompat.widget.ButtonBarLayout  #@id/buttonPanel
   ├─ Button  #@0x0102001B
   ├─ Button  #@0x0102001A
   └─ Button  #@0x01020019
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `androidx.appcompat.widget.ButtonBarLayout` | `android:gravity` | `0x00000050` |
| 2 | `androidx.appcompat.widget.ButtonBarLayout` | `android:orientation` | `horizontal` |
| 3 | `androidx.appcompat.widget.ButtonBarLayout` | `android:id` | `@id/buttonPanel` |
| 4 | `androidx.appcompat.widget.ButtonBarLayout` | `android:paddingLeft` | `12.000000dip` |
| 5 | `androidx.appcompat.widget.ButtonBarLayout` | `android:paddingTop` | `4.000000dip` |
| 6 | `androidx.appcompat.widget.ButtonBarLayout` | `android:paddingRight` | `12.000000dip` |
| 7 | `androidx.appcompat.widget.ButtonBarLayout` | `android:paddingBottom` | `4.000000dip` |
| 8 | `androidx.appcompat.widget.ButtonBarLayout` | `android:layout_width` | `match_parent` |
| 9 | `androidx.appcompat.widget.ButtonBarLayout` | `android:layout_height` | `wrap_content` |
| 10 | `androidx.appcompat.widget.ButtonBarLayout` | `android:layoutDirection` | `locale` |
| 11 | `Button` | `android:id` | `@0x0102001B` |
| 12 | `Button` | `android:layout_width` | `wrap_content` |
| 13 | `Button` | `android:layout_height` | `wrap_content` |
| 14 | `Button` | `android:layout_weight` | `1.000000` |
| 15 | `Button` | `style` | `?attr/buttonBarNeutralButtonStyle` |
| 16 | `Button` | `android:id` | `@0x0102001A` |
| 17 | `Button` | `android:layout_width` | `wrap_content` |
| 18 | `Button` | `android:layout_height` | `wrap_content` |
| 19 | `Button` | `android:layout_weight` | `1.000000` |
| 20 | `Button` | `style` | `?attr/buttonBarNegativeButtonStyle` |
| 21 | `Button` | `android:id` | `@0x01020019` |
| 22 | `Button` | `android:layout_width` | `wrap_content` |
| 23 | `Button` | `android:layout_height` | `wrap_content` |
| 24 | `Button` | `android:layout_weight` | `1.000000` |
| 25 | `Button` | `style` | `?attr/buttonBarPositiveButtonStyle` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|

## ۴. شناسه‌های `@id`

```text
@0x01020019
@0x0102001A
@0x0102001B
@id/buttonPanel
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
<androidx.appcompat.widget.ButtonBarLayout xmlns:android="http://schemas.android.com/apk/res/android" android:gravity="0x00000050" android:orientation="horizontal" android:id="@id/buttonPanel" android:paddingLeft="12.000000dip" android:paddingTop="4.000000dip" android:paddingRight="12.000000dip" android:paddingBottom="4.000000dip" android:layout_width="match_parent" android:layout_height="wrap_content" android:layoutDirection="locale">
  <Button android:id="@0x0102001B" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_weight="1.000000" style="?attr/buttonBarNeutralButtonStyle"/>
  <Button android:id="@0x0102001A" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_weight="1.000000" style="?attr/buttonBarNegativeButtonStyle"/>
  <Button android:id="@0x01020019" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_weight="1.000000" style="?attr/buttonBarPositiveButtonStyle"/>
</androidx.appcompat.widget.ButtonBarLayout>
```
