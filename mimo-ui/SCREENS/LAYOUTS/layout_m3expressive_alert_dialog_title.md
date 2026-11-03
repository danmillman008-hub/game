# پروندهٔ لایه — `res/layout/m3expressive_alert_dialog_title.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/m3expressive_alert_dialog_title.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/m3expressive_alert_dialog_title.xml`](../../SOURCE/res/layout/m3expressive_alert_dialog_title.xml) |
| SHA-256 دیکد | `e881b1f19c3ec34cab8f385fd700214e92231ac350ba078ffab0afec2d3c1fd5` |
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
   │  └─ TextView  #@id/alertTitle
   └─ android.widget.Space  #@id/titleDividerNoCustom
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `LinearLayout` | `android:orientation` | `vertical` |
| 2 | `LinearLayout` | `android:id` | `@id/topPanel` |
| 3 | `LinearLayout` | `android:layout_width` | `match_parent` |
| 4 | `LinearLayout` | `android:layout_height` | `wrap_content` |
| 5 | `LinearLayout` | `android:filterTouchesWhenObscured` | `true` |
| 6 | `LinearLayout` | `android:id` | `@id/title_template` |
| 7 | `LinearLayout` | `style` | `?attr/materialAlertDialogTitlePanelStyle` |
| 8 | `ImageView` | `android:id` | `@0x01020006` |
| 9 | `ImageView` | `style` | `?attr/materialAlertDialogTitleIconStyle` |
| 10 | `TextView` | `android:id` | `@id/alertTitle` |
| 11 | `TextView` | `style` | `?attr/materialAlertDialogTitleTextStyle` |
| 12 | `android.widget.Space` | `android:id` | `@id/titleDividerNoCustom` |
| 13 | `android.widget.Space` | `android:visibility` | `gone` |
| 14 | `android.widget.Space` | `android:layout_width` | `match_parent` |
| 15 | `android.widget.Space` | `android:layout_height` | `@dimen/m3_alert_dialog_title_bottom_margin` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@dimen/m3_alert_dialog_title_bottom_margin` | `16.000000dip` |

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
res/layout/m3expressive_alert_dialog.xml
```

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android" android:orientation="vertical" android:id="@id/topPanel" android:layout_width="match_parent" android:layout_height="wrap_content" android:filterTouchesWhenObscured="true">
  <LinearLayout android:id="@id/title_template" style="?attr/materialAlertDialogTitlePanelStyle">
    <ImageView android:id="@0x01020006" style="?attr/materialAlertDialogTitleIconStyle"/>
    <TextView android:id="@id/alertTitle" style="?attr/materialAlertDialogTitleTextStyle"/>
  </LinearLayout>
  <android.widget.Space android:id="@id/titleDividerNoCustom" android:visibility="gone" android:layout_width="match_parent" android:layout_height="@dimen/m3_alert_dialog_title_bottom_margin"/>
</LinearLayout>
```
