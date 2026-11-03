# پروندهٔ لایه — `res/layout/abc_dialog_title_material.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/abc_dialog_title_material.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/abc_dialog_title_material.xml`](../../SOURCE/res/layout/abc_dialog_title_material.xml) |
| SHA-256 دیکد | `4eddf497464c6817ba739a3a517617078a649f5cd1b3e1a0d5c86320ef756789` |
| ریشه | `androidx.appcompat.widget.FitWindowsLinearLayout` |
| تعداد گره | 3 |
| تعداد شناسه | 1 |
| تگ‌های استفاده‌شده | 3 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 4 |
| ارجاع به منابع | 5 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ androidx.appcompat.widget.FitWindowsLinearLayout
   ├─ TextView  #@id/title
   └─ include
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `androidx.appcompat.widget.FitWindowsLinearLayout` | `android:orientation` | `vertical` |
| 2 | `androidx.appcompat.widget.FitWindowsLinearLayout` | `android:fitsSystemWindows` | `true` |
| 3 | `androidx.appcompat.widget.FitWindowsLinearLayout` | `android:layout_width` | `match_parent` |
| 4 | `androidx.appcompat.widget.FitWindowsLinearLayout` | `android:layout_height` | `match_parent` |
| 5 | `TextView` | `android:ellipsize` | `end` |
| 6 | `TextView` | `android:layout_gravity` | `0x00800003` |
| 7 | `TextView` | `android:id` | `@id/title` |
| 8 | `TextView` | `android:paddingLeft` | `?attr/dialogPreferredPadding` |
| 9 | `TextView` | `android:paddingTop` | `@dimen/abc_dialog_padding_top_material` |
| 10 | `TextView` | `android:paddingRight` | `?attr/dialogPreferredPadding` |
| 11 | `TextView` | `android:layout_width` | `match_parent` |
| 12 | `TextView` | `android:layout_height` | `wrap_content` |
| 13 | `TextView` | `android:singleLine` | `true` |
| 14 | `TextView` | `android:textAlignment` | `viewStart` |
| 15 | `TextView` | `style` | `?0x0101005B` |
| 16 | `include` | `android:layout_width` | `match_parent` |
| 17 | `include` | `android:layout_height` | `wrap_content` |
| 18 | `include` | `android:layout_weight` | `1.000000` |
| 19 | `include` | `layout` | `@layout/abc_screen_content_include` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@dimen/abc_dialog_padding_top_material` | `18.000000dip` |

## ۴. شناسه‌های `@id`

```text
@id/title
```

## ۵. ارجاع به لایه‌های دیگر

```text
1.000000
@layout/abc_screen_content_include
match_parent
wrap_content
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

(هیچ صفحهٔ نام‌برداری به این لایه متصل نشد؛ ممکن است لایهٔ کتابخانه/`<include>` باشد)

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<androidx.appcompat.widget.FitWindowsLinearLayout xmlns:android="http://schemas.android.com/apk/res/android" android:orientation="vertical" android:fitsSystemWindows="true" android:layout_width="match_parent" android:layout_height="match_parent">
  <TextView android:ellipsize="end" android:layout_gravity="0x00800003" android:id="@id/title" android:paddingLeft="?attr/dialogPreferredPadding" android:paddingTop="@dimen/abc_dialog_padding_top_material" android:paddingRight="?attr/dialogPreferredPadding" android:layout_width="match_parent" android:layout_height="wrap_content" android:singleLine="true" android:textAlignment="viewStart" style="?0x0101005B"/>
  <include android:layout_width="match_parent" android:layout_height="wrap_content" android:layout_weight="1.000000" layout="@layout/abc_screen_content_include"/>
</androidx.appcompat.widget.FitWindowsLinearLayout>
```
