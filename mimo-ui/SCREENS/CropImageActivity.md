# صفحه — `CropImageActivity`

> **خاستگاه ثبت:** `PRIOR_WORK_SCREEN_INVENTORY.csv` | **کلاس شواهد:** نام/ساختار `VERIFIED_STATIC`، نگاشت صفحه→لایه `DERIVED` (DEX xref + تطابق نام)، حالت‌ها `PARTIALLY_VERIFIED` (رشتهٔ منبع).

| ویژگی | مقدار |
|---|---|
| کلاس | `com.canhub.cropper.CropImageActivity` |
| نوع | `activity` |
| exported (manifest) | `true` |
| launchMode | `` |
| theme | `` |
| orientation | `` |
| targetActivity | `` |
| app-owned | `False` |
| فناوری | `third-party` |
| تعداد لایه‌های متصل | 2 |
| ComposeView | خیر |
| WebView | خیر |

## ۱. لایه‌های XML متصل (فهرست کامل)

- [`res/layout/crop_image_activity.xml`](../SOURCE/res/layout/crop_image_activity.xml) → [dossier](LAYOUTS/layout_crop_image_activity.md)
- [`res/layout/crop_image_view.xml`](../SOURCE/res/layout/crop_image_view.xml) → [dossier](LAYOUTS/layout_crop_image_view.md)

## ۲. درخت مؤلفه‌ها (همهٔ لایه‌های متصل)

### `res/layout/crop_image_activity.xml`

```text
└─ com.canhub.cropper.CropImageView  #@id/cropImageView
```

### `res/layout/crop_image_view.xml`

```text
└─ merge
   ├─ ImageView  #@id/ImageView_image
   ├─ com.canhub.cropper.CropOverlayView  #@id/CropOverlayView
   └─ ProgressBar  #@id/CropProgressBar
```

## ۳. رشته‌های مرتبط (فهرست کامل)

```text
crop_image_menu_crop
```

## ۴. رنگ‌های مرتبط (فهرست کامل)

(none)

## ۵. دایمنشن‌های مرتبط (فهرست کامل)

(none)

## ۶. استایل‌های مرتبط (فهرست کامل)

(none)

## ۷. شواهد حالت‌ها (رشته‌های منبع)

(none)

## ۸. ناوبری / deep link

(هیچ intent-filter/data برای این سطح اعلان نشده)
