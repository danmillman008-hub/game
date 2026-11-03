# پروندهٔ لایه — `res/layout/mdtp_date_picker_view_animator_v2.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/mdtp_date_picker_view_animator_v2.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/mdtp_date_picker_view_animator_v2.xml`](../../SOURCE/res/layout/mdtp_date_picker_view_animator_v2.xml) |
| SHA-256 دیکد | `0e440283ba6eb52ca2ce012aa665fb6808bbbcd51ccb1baebdf74e4eeb1fbf07` |
| ریشه | `FrameLayout` |
| تعداد گره | 2 |
| تعداد شناسه | 1 |
| تگ‌های استفاده‌شده | 2 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 3 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ FrameLayout
   └─ com.wdullaer.materialdatetimepicker.date.AccessibleDateAnimator  #@id/mdtp_animator
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `FrameLayout` | `android:layout_width` | `wrap_content` |
| 2 | `FrameLayout` | `android:layout_height` | `wrap_content` |
| 3 | `com.wdullaer.materialdatetimepicker.date.AccessibleDateAnimator` | `android:gravity` | `0x00000011` |
| 4 | `com.wdullaer.materialdatetimepicker.date.AccessibleDateAnimator` | `android:id` | `@id/mdtp_animator` |
| 5 | `com.wdullaer.materialdatetimepicker.date.AccessibleDateAnimator` | `android:clipChildren` | `false` |
| 6 | `com.wdullaer.materialdatetimepicker.date.AccessibleDateAnimator` | `android:clipToPadding` | `false` |
| 7 | `com.wdullaer.materialdatetimepicker.date.AccessibleDateAnimator` | `android:layout_width` | `@dimen/mdtp_date_picker_component_width_v2` |
| 8 | `com.wdullaer.materialdatetimepicker.date.AccessibleDateAnimator` | `android:layout_height` | `@dimen/mdtp_date_picker_view_animator_height_v2` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@dimen/mdtp_date_picker_component_width_v2` | `290.000000dip` |
| `@dimen/mdtp_date_picker_view_animator_height_v2` | `320.000000dip` / `285.000000dip` (land) / `400.000000dip` (sw600dp) |

## ۴. شناسه‌های `@id`

```text
@id/mdtp_animator
```

## ۵. ارجاع به لایه‌های دیگر

```text
(none)
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

(هیچ صفحهٔ نام‌برداری به این لایه متصل نشد؛ ممکن است لایهٔ کتابخانه/`<include>` باشد)

## ۷. لایه‌هایی که این لایه را include می‌کنند

```text
res/layout-land/mdtp_date_picker_dialog_v2.xml
res/layout/mdtp_date_picker_dialog_v2.xml
```

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<FrameLayout xmlns:android="http://schemas.android.com/apk/res/android" android:layout_width="wrap_content" android:layout_height="wrap_content">
  <com.wdullaer.materialdatetimepicker.date.AccessibleDateAnimator android:gravity="0x00000011" android:id="@id/mdtp_animator" android:clipChildren="false" android:clipToPadding="false" android:layout_width="@dimen/mdtp_date_picker_component_width_v2" android:layout_height="@dimen/mdtp_date_picker_view_animator_height_v2"/>
</FrameLayout>
```
