# صفحه — `SetOccupationFragment`

> **خاستگاه ثبت:** `PRIOR_WORK_SCREEN_INVENTORY.csv` | **کلاس شواهد:** نام/ساختار `VERIFIED_STATIC`، نگاشت صفحه→لایه `DERIVED` (DEX xref + تطابق نام)، حالت‌ها `PARTIALLY_VERIFIED` (رشتهٔ منبع).

| ویژگی | مقدار |
|---|---|
| کلاس | `com.getmimo.ui.onboarding.occupation.SetOccupationFragment` |
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

- [`res/layout/onboarding_step_2a_set_occupation_fragment.xml`](../SOURCE/res/layout/onboarding_step_2a_set_occupation_fragment.xml) → [dossier](LAYOUTS/layout_onboarding_step_2a_set_occupation_fragment.md)

## ۲. درخت مؤلفه‌ها (همهٔ لایه‌های متصل)

### `res/layout/onboarding_step_2a_set_occupation_fragment.xml`

```text
└─ androidx.constraintlayout.widget.ConstraintLayout
   └─ ScrollView
      └─ androidx.constraintlayout.widget.ConstraintLayout
         ├─ TextView  #@id/tv_set_occupation_title
         └─ LinearLayout  #@id/layout_motive
            ├─ com.getmimo.ui.onboarding.motive.OnboardingMotiveButton  #@id/btn_occupation_high_school
            ├─ com.getmimo.ui.onboarding.motive.OnboardingMotiveButton  #@id/btn_occupation_university
            ├─ com.getmimo.ui.onboarding.motive.OnboardingMotiveButton  #@id/btn_occupation_professional
            ├─ com.getmimo.ui.onboarding.motive.OnboardingMotiveButton  #@id/btn_occupation_self_employed
            └─ com.getmimo.ui.onboarding.motive.OnboardingMotiveButton  #@id/btn_occupation_none
```

## ۳. رشته‌های مرتبط (فهرست کامل)

```text
onboarding_set_occupation_high_school_student
onboarding_set_occupation_none
onboarding_set_occupation_professional
onboarding_set_occupation_self_employed
onboarding_set_occupation_title
onboarding_set_occupation_university_student
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
