# پروندهٔ لایه — `res/layout/abc_alert_dialog_title_material.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/abc_alert_dialog_title_material.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/abc_alert_dialog_title_material.xml`](../../SOURCE/res/layout/abc_alert_dialog_title_material.xml) |
| SHA-256 دیکد | `3babbd94d3945db841ae9dc1707f7b171ffcf25082a031da4c37aa846dfcd4cd` |
| ریشه | `LinearLayout` |
| تعداد گره | 5 |
| تعداد شناسه | 5 |
| تگ‌های استفاده‌شده | 4 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 10 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ LinearLayout  #@id/topPanel
   ├─ LinearLayout  #@id/title_template
   │  ├─ ImageView  #@0x01020006
   │  └─ androidx.appcompat.widget.DialogTitle  #@id/alertTitle
   └─ android.widget.Space  #@id/titleDividerNoCustom
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `LinearLayout` | `android:orientation` | `vertical` |
| 2 | `LinearLayout` | `android:id` | `@id/topPanel` |
| 3 | `LinearLayout` | `android:layout_width` | `match_parent` |
| 4 | `LinearLayout` | `android:layout_height` | `wrap_content` |
| 5 | `LinearLayout` | `android:gravity` | `0x00800013` |
| 6 | `LinearLayout` | `android:orientation` | `horizontal` |
| 7 | `LinearLayout` | `android:id` | `@id/title_template` |
| 8 | `LinearLayout` | `android:paddingLeft` | `?attr/dialogPreferredPadding` |
| 9 | `LinearLayout` | `android:paddingTop` | `@dimen/abc_dialog_padding_top_material` |
| 10 | `LinearLayout` | `android:paddingRight` | `?attr/dialogPreferredPadding` |
| 11 | `LinearLayout` | `android:layout_width` | `match_parent` |
| 12 | `LinearLayout` | `android:layout_height` | `wrap_content` |
| 13 | `ImageView` | `android:id` | `@0x01020006` |
| 14 | `ImageView` | `android:layout_width` | `32.000000dip` |
| 15 | `ImageView` | `android:layout_height` | `32.000000dip` |
| 16 | `ImageView` | `android:layout_marginRight` | `8.000000dip` |
| 17 | `ImageView` | `android:src` | `@null` |
| 18 | `ImageView` | `android:scaleType` | `fitCenter` |
| 19 | `ImageView` | `android:layout_marginEnd` | `8.000000dip` |
| 20 | `androidx.appcompat.widget.DialogTitle` | `android:ellipsize` | `end` |
| 21 | `androidx.appcompat.widget.DialogTitle` | `android:layout_gravity` | `0x00800003` |
| 22 | `androidx.appcompat.widget.DialogTitle` | `android:id` | `@id/alertTitle` |
| 23 | `androidx.appcompat.widget.DialogTitle` | `android:layout_width` | `match_parent` |
| 24 | `androidx.appcompat.widget.DialogTitle` | `android:layout_height` | `wrap_content` |
| 25 | `androidx.appcompat.widget.DialogTitle` | `android:singleLine` | `true` |
| 26 | `androidx.appcompat.widget.DialogTitle` | `android:textAlignment` | `viewStart` |
| 27 | `androidx.appcompat.widget.DialogTitle` | `style` | `?0x0101005B` |
| 28 | `android.widget.Space` | `android:id` | `@id/titleDividerNoCustom` |
| 29 | `android.widget.Space` | `android:visibility` | `gone` |
| 30 | `android.widget.Space` | `android:layout_width` | `match_parent` |
| 31 | `android.widget.Space` | `android:layout_height` | `@dimen/abc_dialog_title_divider_material` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@dimen/abc_dialog_padding_top_material` | `18.000000dip` |
| `@dimen/abc_dialog_title_divider_material` | `8.000000dip` |

## ۴. شناسه‌های `@id`

```text
@0x01020006
@id/alertTitle
@id/titleDividerNoCustom
@id/title_template
@id/topPanel
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
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android" android:orientation="vertical" android:id="@id/topPanel" android:layout_width="match_parent" android:layout_height="wrap_content">
  <LinearLayout android:gravity="0x00800013" android:orientation="horizontal" android:id="@id/title_template" android:paddingLeft="?attr/dialogPreferredPadding" android:paddingTop="@dimen/abc_dialog_padding_top_material" android:paddingRight="?attr/dialogPreferredPadding" android:layout_width="match_parent" android:layout_height="wrap_content">
    <ImageView android:id="@0x01020006" android:layout_width="32.000000dip" android:layout_height="32.000000dip" android:layout_marginRight="8.000000dip" android:src="@null" android:scaleType="fitCenter" android:layout_marginEnd="8.000000dip"/>
    <androidx.appcompat.widget.DialogTitle android:ellipsize="end" android:layout_gravity="0x00800003" android:id="@id/alertTitle" android:layout_width="match_parent" android:layout_height="wrap_content" android:singleLine="true" android:textAlignment="viewStart" style="?0x0101005B"/>
  </LinearLayout>
  <android.widget.Space android:id="@id/titleDividerNoCustom" android:visibility="gone" android:layout_width="match_parent" android:layout_height="@dimen/abc_dialog_title_divider_material"/>
</LinearLayout>
```
