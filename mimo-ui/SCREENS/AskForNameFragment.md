# صفحه — `AskForNameFragment`

> **خاستگاه ثبت:** `PRIOR_WORK_SCREEN_INVENTORY.csv` | **کلاس شواهد:** نام/ساختار `VERIFIED_STATIC`، نگاشت صفحه→لایه `DERIVED` (DEX xref + تطابق نام)، حالت‌ها `PARTIALLY_VERIFIED` (رشتهٔ منبع).

| ویژگی | مقدار |
|---|---|
| کلاس | `com.getmimo.ui.common.AskForNameFragment` |
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

- [`res/layout/ask_for_name_fragment.xml`](../SOURCE/res/layout/ask_for_name_fragment.xml) → [dossier](LAYOUTS/layout_ask_for_name_fragment.md)

## ۲. درخت مؤلفه‌ها (همهٔ لایه‌های متصل)

### `res/layout/ask_for_name_fragment.xml`

```text
└─ FrameLayout  #@id/root_name_code_playground
   └─ androidx.cardview.widget.CardView
      └─ androidx.constraintlayout.widget.ConstraintLayout
         ├─ TextView  #@id/tv_ask_for_name_title
         ├─ com.google.android.material.textfield.TextInputLayout  #@id/til_ask_for_name
         │  └─ com.google.android.material.textfield.TextInputEditText  #@id/et_ask_for_name
         │     └─ requestFocus
         ├─ TextView  #@id/tv_name_code_chars
         └─ androidx.compose.ui.platform.ComposeView  #@id/btn_ask_for_name_enter
```

## ۳. رشته‌های مرتبط (فهرست کامل)

```text
leaderboard_ask_for_name_title
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
