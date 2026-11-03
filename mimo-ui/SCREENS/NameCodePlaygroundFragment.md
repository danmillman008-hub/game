# صفحه — `NameCodePlaygroundFragment`

> **خاستگاه ثبت:** `PRIOR_WORK_SCREEN_INVENTORY.csv` | **کلاس شواهد:** نام/ساختار `VERIFIED_STATIC`، نگاشت صفحه→لایه `DERIVED` (DEX xref + تطابق نام)، حالت‌ها `PARTIALLY_VERIFIED` (رشتهٔ منبع).

| ویژگی | مقدار |
|---|---|
| کلاس | `com.getmimo.ui.codeplayground.NameCodePlaygroundFragment` |
| نوع | `fragment` |
| exported (manifest) | `` |
| launchMode | `` |
| theme | `` |
| orientation | `` |
| targetActivity | `` |
| app-owned | `True` |
| فناوری | `view binding` |
| تعداد لایه‌های متصل | 1 |
| ComposeView | بله |
| WebView | خیر |

## ۱. لایه‌های XML متصل (فهرست کامل)

- [`res/layout/name_code_playground_fragment.xml`](../SOURCE/res/layout/name_code_playground_fragment.xml) → [dossier](LAYOUTS/layout_name_code_playground_fragment.md)

## ۲. درخت مؤلفه‌ها (همهٔ لایه‌های متصل)

### `res/layout/name_code_playground_fragment.xml`

```text
└─ androidx.constraintlayout.widget.ConstraintLayout  #@id/root_name_code_playground
   └─ androidx.cardview.widget.CardView
      └─ androidx.constraintlayout.widget.ConstraintLayout
         ├─ TextView  #@id/tv_save_code_header
         ├─ TextView  #@id/tv_save_code_name
         ├─ TextView  #@id/tv_name_code_chars
         ├─ com.google.android.material.textfield.TextInputLayout  #@id/til_name_code
         │  └─ com.google.android.material.textfield.TextInputEditText  #@id/et_name_code
         │     └─ requestFocus
         ├─ ImageView  #@id/iv_public_playground
         ├─ TextView  #@id/tv_public_playground
         ├─ androidx.appcompat.widget.SwitchCompat  #@id/sw_public_playground
         ├─ androidx.compose.ui.platform.ComposeView  #@id/btn_name_code_enter
         ├─ androidx.compose.ui.platform.ComposeView  #@id/btn_name_code_cancel
         └─ androidx.constraintlayout.widget.Group  #@id/group_save_code_visibility
```

## ۳. رشته‌های مرتبط (فهرست کامل)

```text
name_code_playground_characters
name_code_playground_characters_dynamic
name_code_playground_header
name_code_playground_hint
name_code_playground_remix_header
rename_code_playground_header
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
