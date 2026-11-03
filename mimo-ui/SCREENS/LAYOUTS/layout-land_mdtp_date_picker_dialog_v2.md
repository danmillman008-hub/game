# پروندهٔ لایه — `res/layout-land/mdtp_date_picker_dialog_v2.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout-land/mdtp_date_picker_dialog_v2.xml` |
| فایل دیکدشده | [`SOURCE/res/layout-land/mdtp_date_picker_dialog_v2.xml`](../../SOURCE/res/layout-land/mdtp_date_picker_dialog_v2.xml) |
| SHA-256 دیکد | `d9be5728a974eb8a5a8e9d7021113bc9794dda90eb2f89a4618083b6e88b5552` |
| ریشه | `LinearLayout` |
| تعداد گره | 6 |
| تعداد شناسه | 0 |
| تگ‌های استفاده‌شده | 2 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 7 |
| ارجاع به منابع | 5 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ LinearLayout
   ├─ include
   ├─ include
   └─ LinearLayout
      ├─ include
      └─ include
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `LinearLayout` | `android:orientation` | `horizontal` |
| 2 | `LinearLayout` | `android:background` | `@0x0106000D` |
| 3 | `LinearLayout` | `android:layout_width` | `wrap_content` |
| 4 | `LinearLayout` | `android:layout_height` | `wrap_content` |
| 5 | `include` | `layout` | `@layout/mdtp_date_picker_header_view_v2` |
| 6 | `include` | `layout` | `@layout/mdtp_date_picker_selected_date_v2` |
| 7 | `LinearLayout` | `android:orientation` | `vertical` |
| 8 | `LinearLayout` | `android:background` | `@0x0106000D` |
| 9 | `LinearLayout` | `android:layout_width` | `wrap_content` |
| 10 | `LinearLayout` | `android:layout_height` | `match_parent` |
| 11 | `include` | `layout` | `@layout/mdtp_date_picker_view_animator_v2` |
| 12 | `include` | `android:layout_width` | `match_parent` |
| 13 | `include` | `android:layout_height` | `wrap_content` |
| 14 | `include` | `android:layout_marginTop` | `16777184.000000dip` |
| 15 | `include` | `layout` | `@layout/mdtp_done_button` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|

## ۴. شناسه‌های `@id`

```text
(none)
```

## ۵. ارجاع به لایه‌های دیگر

```text
16777184.000000dip
@layout/mdtp_date_picker_header_view_v2
@layout/mdtp_date_picker_selected_date_v2
@layout/mdtp_date_picker_view_animator_v2
@layout/mdtp_done_button
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
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android" android:orientation="horizontal" android:background="@0x0106000D" android:layout_width="wrap_content" android:layout_height="wrap_content">
  <include layout="@layout/mdtp_date_picker_header_view_v2"/>
  <include layout="@layout/mdtp_date_picker_selected_date_v2"/>
  <LinearLayout android:orientation="vertical" android:background="@0x0106000D" android:layout_width="wrap_content" android:layout_height="match_parent">
    <include layout="@layout/mdtp_date_picker_view_animator_v2"/>
    <include android:layout_width="match_parent" android:layout_height="wrap_content" android:layout_marginTop="16777184.000000dip" layout="@layout/mdtp_done_button"/>
  </LinearLayout>
</LinearLayout>
```
