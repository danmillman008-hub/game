# صفحه — `SetWorkFunctionFragment`

> **خاستگاه ثبت:** `PRIOR_WORK_SCREEN_INVENTORY.csv` | **کلاس شواهد:** نام/ساختار `VERIFIED_STATIC`، نگاشت صفحه→لایه `DERIVED` (DEX xref + تطابق نام)، حالت‌ها `PARTIALLY_VERIFIED` (رشتهٔ منبع).

| ویژگی | مقدار |
|---|---|
| کلاس | `com.getmimo.ui.onboarding.workfunction.SetWorkFunctionFragment` |
| نوع | `fragment` |
| exported (manifest) | `` |
| launchMode | `` |
| theme | `` |
| orientation | `` |
| targetActivity | `` |
| app-owned | `True` |
| فناوری | `view binding` |
| تعداد لایه‌های متصل | 1 |
| ComposeView | خیر |
| WebView | خیر |

## ۱. لایه‌های XML متصل (فهرست کامل)

- [`res/layout/onboarding_step_2b_set_work_function_fragment.xml`](../SOURCE/res/layout/onboarding_step_2b_set_work_function_fragment.xml) → [dossier](LAYOUTS/layout_onboarding_step_2b_set_work_function_fragment.md)

## ۲. درخت مؤلفه‌ها (همهٔ لایه‌های متصل)

### `res/layout/onboarding_step_2b_set_work_function_fragment.xml`

```text
└─ androidx.constraintlayout.widget.ConstraintLayout
   └─ ScrollView
      └─ androidx.constraintlayout.widget.ConstraintLayout
         ├─ TextView  #@id/tv_set_work_function_title
         └─ LinearLayout  #@id/layout_work_functions
            ├─ com.getmimo.ui.onboarding.motive.OnboardingMotiveButton  #@id/btn_work_function_marketing
            ├─ com.getmimo.ui.onboarding.motive.OnboardingMotiveButton  #@id/btn_work_function_sales
            ├─ com.getmimo.ui.onboarding.motive.OnboardingMotiveButton  #@id/btn_work_function_customer_support
            ├─ com.getmimo.ui.onboarding.motive.OnboardingMotiveButton  #@id/btn_work_function_software_it_data
            ├─ com.getmimo.ui.onboarding.motive.OnboardingMotiveButton  #@id/btn_work_function_product_management
            ├─ com.getmimo.ui.onboarding.motive.OnboardingMotiveButton  #@id/btn_work_function_admin_finance
            └─ com.getmimo.ui.onboarding.motive.OnboardingMotiveButton  #@id/btn_work_function_other
```

## ۳. رشته‌های مرتبط (فهرست کامل)

```text
onboarding_set_work_function_admin_finance
onboarding_set_work_function_customer_support
onboarding_set_work_function_marketing
onboarding_set_work_function_other
onboarding_set_work_function_product_management
onboarding_set_work_function_sales
onboarding_set_work_function_software_it_data
onboarding_set_work_function_title
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
