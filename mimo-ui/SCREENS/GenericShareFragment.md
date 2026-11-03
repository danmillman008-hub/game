# صفحه — `GenericShareFragment`

> **خاستگاه ثبت:** `DEX UI_CLASSES.json` | **کلاس شواهد:** نام/ساختار `VERIFIED_STATIC`، نگاشت صفحه→لایه `DERIVED` (DEX xref + تطابق نام)، حالت‌ها `PARTIALLY_VERIFIED` (رشتهٔ منبع).

| ویژگی | مقدار |
|---|---|
| کلاس | `com.getmimo.ui.base.GenericShareFragment$setupView$1` |
| نوع | `dex-ui-class` |
| exported (manifest) | `` |
| launchMode | `` |
| theme | `` |
| orientation | `` |
| targetActivity | `` |
| app-owned | `True` |
| فناوری | `view|compose (unresolved per screen)` |
| تعداد لایه‌های متصل | 1 |
| ComposeView | خیر |
| WebView | خیر |

## ۱. لایه‌های XML متصل (فهرست کامل)

- [`res/layout/generic_share_fragment.xml`](../SOURCE/res/layout/generic_share_fragment.xml) → [dossier](LAYOUTS/layout_generic_share_fragment.md)

## ۲. درخت مؤلفه‌ها (همهٔ لایه‌های متصل)

### `res/layout/generic_share_fragment.xml`

```text
└─ merge
   └─ androidx.constraintlayout.widget.ConstraintLayout
      ├─ androidx.constraintlayout.widget.ConstraintLayout  #@id/layout_share
      │  ├─ FrameLayout  #@id/layout_shareable_image
      │  └─ include  #@id/layout_placeholder_original
      └─ LinearLayout  #@id/layout_share_options
         ├─ TextView  #@id/tv_share_to
         ├─ LinearLayout
         │  ├─ ImageView  #@id/iv_share_instagram
         │  ├─ ImageView  #@id/iv_share_facebook
         │  └─ ImageView  #@id/iv_share_others
         └─ TextView  #@id/tv_tag
```

## ۳. رشته‌های مرتبط (فهرست کامل)

(none)

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
