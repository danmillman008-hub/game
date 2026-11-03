# پروندهٔ لایه — `res/layout/mdtp_date_picker_dialog.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/mdtp_date_picker_dialog.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/mdtp_date_picker_dialog.xml`](../../SOURCE/res/layout/mdtp_date_picker_dialog.xml) |
| SHA-256 دیکد | `7cb4b678bd30034ab11454d1e6541309d49bd83ab5b6a64f0ed36331548fbbc7` |
| ریشه | `LinearLayout` |
| تعداد گره | 5 |
| تعداد شناسه | 0 |
| تگ‌های استفاده‌شده | 2 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 3 |
| ارجاع به منابع | 6 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ LinearLayout
   ├─ LinearLayout
   │  ├─ include
   │  └─ include
   └─ include
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `LinearLayout` | `android:gravity` | `0x00000011` |
| 2 | `LinearLayout` | `android:orientation` | `vertical` |
| 3 | `LinearLayout` | `android:background` | `@color/mdtp_date_picker_view_animator` |
| 4 | `LinearLayout` | `android:layout_width` | `@dimen/mdtp_date_picker_component_width` |
| 5 | `LinearLayout` | `android:layout_height` | `wrap_content` |
| 6 | `LinearLayout` | `android:orientation` | `vertical` |
| 7 | `LinearLayout` | `android:background` | `@0x0106000D` |
| 8 | `LinearLayout` | `android:layout_width` | `wrap_content` |
| 9 | `LinearLayout` | `android:layout_height` | `wrap_content` |
| 10 | `include` | `layout` | `@layout/mdtp_date_picker_selected_date` |
| 11 | `include` | `layout` | `@layout/mdtp_date_picker_view_animator` |
| 12 | `include` | `layout` | `@layout/mdtp_done_button` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/mdtp_date_picker_view_animator` | `@android:0106000B` |
| `@dimen/mdtp_date_picker_component_width` | `270.000000dip` / `220.000000dip` (land) / `400.000000dip` (sw600dp) / `270.000000dip` (w560dp-land) |

## ۴. شناسه‌های `@id`

```text
(none)
```

## ۵. ارجاع به لایه‌های دیگر

```text
@layout/mdtp_date_picker_selected_date
@layout/mdtp_date_picker_view_animator
@layout/mdtp_done_button
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

(هیچ صفحهٔ نام‌برداری به این لایه متصل نشد؛ ممکن است لایهٔ کتابخانه/`<include>` باشد)

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android" android:gravity="0x00000011" android:orientation="vertical" android:background="@color/mdtp_date_picker_view_animator" android:layout_width="@dimen/mdtp_date_picker_component_width" android:layout_height="wrap_content">
  <LinearLayout android:orientation="vertical" android:background="@0x0106000D" android:layout_width="wrap_content" android:layout_height="wrap_content">
    <include layout="@layout/mdtp_date_picker_selected_date"/>
    <include layout="@layout/mdtp_date_picker_view_animator"/>
  </LinearLayout>
  <include layout="@layout/mdtp_done_button"/>
</LinearLayout>
```
