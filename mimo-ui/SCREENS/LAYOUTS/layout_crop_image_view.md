# پروندهٔ لایه — `res/layout/crop_image_view.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/crop_image_view.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/crop_image_view.xml`](../../SOURCE/res/layout/crop_image_view.xml) |
| SHA-256 دیکد | `9938b6a5fceef77a86247b95e248d431aad4528232af5455f2c2359cfdcaa75a` |
| ریشه | `merge` |
| تعداد گره | 4 |
| تعداد شناسه | 3 |
| تگ‌های استفاده‌شده | 4 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 3 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ merge
   ├─ ImageView  #@id/ImageView_image
   ├─ com.canhub.cropper.CropOverlayView  #@id/CropOverlayView
   └─ ProgressBar  #@id/CropProgressBar
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `ImageView` | `android:id` | `@id/ImageView_image` |
| 2 | `ImageView` | `android:layout_width` | `match_parent` |
| 3 | `ImageView` | `android:layout_height` | `match_parent` |
| 4 | `ImageView` | `android:scaleType` | `centerInside` |
| 5 | `ImageView` | `android:adjustViewBounds` | `true` |
| 6 | `com.canhub.cropper.CropOverlayView` | `android:id` | `@id/CropOverlayView` |
| 7 | `com.canhub.cropper.CropOverlayView` | `android:visibility` | `invisible` |
| 8 | `com.canhub.cropper.CropOverlayView` | `android:layout_width` | `match_parent` |
| 9 | `com.canhub.cropper.CropOverlayView` | `android:layout_height` | `match_parent` |
| 10 | `ProgressBar` | `android:layout_gravity` | `0x00000011` |
| 11 | `ProgressBar` | `android:id` | `@id/CropProgressBar` |
| 12 | `ProgressBar` | `android:layout_width` | `wrap_content` |
| 13 | `ProgressBar` | `android:layout_height` | `wrap_content` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|

## ۴. شناسه‌های `@id`

```text
@id/CropOverlayView
@id/CropProgressBar
@id/ImageView_image
```

## ۵. ارجاع به لایه‌های دیگر

```text
(none)
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

```text
com.canhub.cropper.CropImageActivity
```

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<merge xmlns:android="http://schemas.android.com/apk/res/android">
  <ImageView android:id="@id/ImageView_image" android:layout_width="match_parent" android:layout_height="match_parent" android:scaleType="centerInside" android:adjustViewBounds="true"/>
  <com.canhub.cropper.CropOverlayView android:id="@id/CropOverlayView" android:visibility="invisible" android:layout_width="match_parent" android:layout_height="match_parent"/>
  <ProgressBar android:layout_gravity="0x00000011" android:id="@id/CropProgressBar" android:layout_width="wrap_content" android:layout_height="wrap_content"/>
</merge>
```
