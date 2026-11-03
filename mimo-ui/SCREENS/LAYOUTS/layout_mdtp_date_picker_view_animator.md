# پروندهٔ لایه — `res/layout/mdtp_date_picker_view_animator.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/mdtp_date_picker_view_animator.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/mdtp_date_picker_view_animator.xml`](../../SOURCE/res/layout/mdtp_date_picker_view_animator.xml) |
| SHA-256 دیکد | `1fc62fd5416911e34201699c232daf39e56a67df733ac920b1a796b13909955a` |
| ریشه | `FrameLayout` |
| تعداد گره | 2 |
| تعداد شناسه | 1 |
| تگ‌های استفاده‌شده | 2 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 5 |

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
| 5 | `com.wdullaer.materialdatetimepicker.date.AccessibleDateAnimator` | `android:background` | `@0x0106000D` |
| 6 | `com.wdullaer.materialdatetimepicker.date.AccessibleDateAnimator` | `android:paddingLeft` | `@dimen/mdtp_date_picker_view_animator_padding` |
| 7 | `com.wdullaer.materialdatetimepicker.date.AccessibleDateAnimator` | `android:paddingRight` | `@dimen/mdtp_date_picker_view_animator_padding` |
| 8 | `com.wdullaer.materialdatetimepicker.date.AccessibleDateAnimator` | `android:layout_width` | `@dimen/mdtp_date_picker_component_width` |
| 9 | `com.wdullaer.materialdatetimepicker.date.AccessibleDateAnimator` | `android:layout_height` | `@dimen/mdtp_date_picker_view_animator_height` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@dimen/mdtp_date_picker_component_width` | `270.000000dip` / `220.000000dip` (land) / `400.000000dip` (sw600dp) / `270.000000dip` (w560dp-land) |
| `@dimen/mdtp_date_picker_view_animator_height` | `252.000000dip` / `220.000000dip` (land) / `400.000000dip` (sw600dp) |
| `@dimen/mdtp_date_picker_view_animator_padding` | `8.000000dip` |

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
res/layout-land/mdtp_date_picker_dialog.xml
res/layout-sw600dp-land-v13/mdtp_date_picker_dialog.xml
res/layout-sw600dp-v13/mdtp_date_picker_dialog.xml
res/layout-w270dp-h560dp-v13/mdtp_date_picker_dialog.xml
res/layout/mdtp_date_picker_dialog.xml
```

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<FrameLayout xmlns:android="http://schemas.android.com/apk/res/android" android:layout_width="wrap_content" android:layout_height="wrap_content">
  <com.wdullaer.materialdatetimepicker.date.AccessibleDateAnimator android:gravity="0x00000011" android:id="@id/mdtp_animator" android:background="@0x0106000D" android:paddingLeft="@dimen/mdtp_date_picker_view_animator_padding" android:paddingRight="@dimen/mdtp_date_picker_view_animator_padding" android:layout_width="@dimen/mdtp_date_picker_component_width" android:layout_height="@dimen/mdtp_date_picker_view_animator_height"/>
</FrameLayout>
```
