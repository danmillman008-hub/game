# پروندهٔ لایه — `res/layout-v33/glance_check_box_backport_end_bottom.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout-v33/glance_check_box_backport_end_bottom.xml` |
| فایل دیکدشده | [`SOURCE/res/layout-v33/glance_check_box_backport_end_bottom.xml`](../../SOURCE/res/layout-v33/glance_check_box_backport_end_bottom.xml) |
| SHA-256 دیکد | `269114c568858bc8042c8e539e5ce013702a622cf2f6673cb7cc81d2b0844f28` |
| ریشه | `LinearLayout` |
| تعداد گره | 3 |
| تعداد شناسه | 3 |
| تگ‌های استفاده‌شده | 2 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 6 |
| ارجاع به منابع | 7 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ LinearLayout  #@id/glanceView
   ├─ ViewStub  #@id/checkBoxIcon
   └─ ViewStub  #@id/checkBoxText
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `LinearLayout` | `android:gravity` | `0x00000010` |
| 2 | `LinearLayout` | `android:layout_gravity` | `0x00800055` |
| 3 | `LinearLayout` | `android:orientation` | `horizontal` |
| 4 | `LinearLayout` | `android:id` | `@id/glanceView` |
| 5 | `LinearLayout` | `android:tag` | `glanceCompoundButton` |
| 6 | `LinearLayout` | `android:layout_width` | `wrap_content` |
| 7 | `LinearLayout` | `android:layout_height` | `wrap_content` |
| 8 | `LinearLayout` | `android:layoutDirection` | `locale` |
| 9 | `LinearLayout` | `app:glance_isTopLevelLayout` | `true` |
| 10 | `LinearLayout` | `style` | `@style/Glance.AppWidget.CheckBoxBackport` |
| 11 | `ViewStub` | `android:id` | `@id/checkBoxIcon` |
| 12 | `ViewStub` | `android:layout` | `@layout/glance_check_box_image` |
| 13 | `ViewStub` | `android:layout_width` | `32.000000dip` |
| 14 | `ViewStub` | `android:layout_height` | `32.000000dip` |
| 15 | `ViewStub` | `android:id` | `@id/checkBoxText` |
| 16 | `ViewStub` | `android:layout` | `@layout/glance_check_box_text` |
| 17 | `ViewStub` | `android:layout_width` | `0.000000dip` |
| 18 | `ViewStub` | `android:layout_height` | `wrap_content` |
| 19 | `ViewStub` | `android:layout_weight` | `1.000000` |
| 20 | `ViewStub` | `android:textDirection` | `locale` |
| 21 | `ViewStub` | `style` | `@style/Glance.AppWidget.CheckBoxText` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@style/Glance.AppWidget.CheckBoxBackport` | `[]` |
| `@style/Glance.AppWidget.CheckBoxText` | `[]` |

## ۴. شناسه‌های `@id`

```text
@id/checkBoxIcon
@id/checkBoxText
@id/glanceView
```

## ۵. ارجاع به لایه‌های دیگر

```text
0.000000dip
1.000000
32.000000dip
@layout/glance_check_box_image
@layout/glance_check_box_text
wrap_content
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

(هیچ صفحهٔ نام‌برداری به این لایه متصل نشد؛ ممکن است لایهٔ کتابخانه/`<include>` باشد)

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android" xmlns:app="http://schemas.android.com/apk/res-auto" android:gravity="0x00000010" android:layout_gravity="0x00800055" android:orientation="horizontal" android:id="@id/glanceView" android:tag="glanceCompoundButton" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layoutDirection="locale" app:glance_isTopLevelLayout="true" style="@style/Glance.AppWidget.CheckBoxBackport">
  <ViewStub android:id="@id/checkBoxIcon" android:layout="@layout/glance_check_box_image" android:layout_width="32.000000dip" android:layout_height="32.000000dip"/>
  <ViewStub android:id="@id/checkBoxText" android:layout="@layout/glance_check_box_text" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_weight="1.000000" android:textDirection="locale" style="@style/Glance.AppWidget.CheckBoxText"/>
</LinearLayout>
```
