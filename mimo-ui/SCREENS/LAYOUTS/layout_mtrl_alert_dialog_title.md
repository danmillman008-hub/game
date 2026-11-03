# پروندهٔ لایه — `res/layout/mtrl_alert_dialog_title.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/mtrl_alert_dialog_title.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/mtrl_alert_dialog_title.xml`](../../SOURCE/res/layout/mtrl_alert_dialog_title.xml) |
| SHA-256 دیکد | `5cb99cbeb640ca3904d035edd23e1ce27ba5f887caf2ecc0f83dba6e9445e393` |
| ریشه | `LinearLayout` |
| تعداد گره | 5 |
| تعداد شناسه | 5 |
| تگ‌های استفاده‌شده | 4 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 9 |

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
| 5 | `LinearLayout` | `android:id` | `@id/title_template` |
| 6 | `LinearLayout` | `style` | `?attr/materialAlertDialogTitlePanelStyle` |
| 7 | `ImageView` | `android:id` | `@0x01020006` |
| 8 | `ImageView` | `style` | `?attr/materialAlertDialogTitleIconStyle` |
| 9 | `androidx.appcompat.widget.DialogTitle` | `android:id` | `@id/alertTitle` |
| 10 | `androidx.appcompat.widget.DialogTitle` | `style` | `?attr/materialAlertDialogTitleTextStyle` |
| 11 | `android.widget.Space` | `android:id` | `@id/titleDividerNoCustom` |
| 12 | `android.widget.Space` | `android:visibility` | `gone` |
| 13 | `android.widget.Space` | `android:layout_width` | `match_parent` |
| 14 | `android.widget.Space` | `android:layout_height` | `@dimen/abc_dialog_title_divider_material` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
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
res/layout/mtrl_alert_dialog.xml
```

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android" android:orientation="vertical" android:id="@id/topPanel" android:layout_width="match_parent" android:layout_height="wrap_content">
  <LinearLayout android:id="@id/title_template" style="?attr/materialAlertDialogTitlePanelStyle">
    <ImageView android:id="@0x01020006" style="?attr/materialAlertDialogTitleIconStyle"/>
    <androidx.appcompat.widget.DialogTitle android:id="@id/alertTitle" style="?attr/materialAlertDialogTitleTextStyle"/>
  </LinearLayout>
  <android.widget.Space android:id="@id/titleDividerNoCustom" android:visibility="gone" android:layout_width="match_parent" android:layout_height="@dimen/abc_dialog_title_divider_material"/>
</LinearLayout>
```
