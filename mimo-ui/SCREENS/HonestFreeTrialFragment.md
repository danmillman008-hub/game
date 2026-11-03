# صفحه — `HonestFreeTrialFragment`

> **خاستگاه ثبت:** `PRIOR_WORK_SCREEN_INVENTORY.csv` | **کلاس شواهد:** نام/ساختار `VERIFIED_STATIC`، نگاشت صفحه→لایه `DERIVED` (DEX xref + تطابق نام)، حالت‌ها `PARTIALLY_VERIFIED` (رشتهٔ منبع).

| ویژگی | مقدار |
|---|---|
| کلاس | `com.getmimo.ui.iap.freetrial.HonestFreeTrialFragment` |
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

- [`res/layout/free_trial_honest_fragment.xml`](../SOURCE/res/layout/free_trial_honest_fragment.xml) → [dossier](LAYOUTS/layout_free_trial_honest_fragment.md)

## ۲. درخت مؤلفه‌ها (همهٔ لایه‌های متصل)

### `res/layout/free_trial_honest_fragment.xml`

```text
└─ androidx.constraintlayout.widget.ConstraintLayout  #@id/cl_main
   ├─ ImageButton  #@id/ib_upgrade_modal_close
   ├─ TextView  #@id/tv_mimo_pro
   ├─ TextView  #@id/tv_title
   ├─ ScrollView  #@id/sv_main
   │  └─ androidx.constraintlayout.widget.ConstraintLayout  #@id/sv_honest_trial
   │     ├─ View
   │     ├─ ImageView  #@id/iv_arrow
   │     ├─ ImageView  #@id/iv_today
   │     ├─ TextView  #@id/tv_today
   │     ├─ ImageView  #@id/iv_unlock
   │     ├─ TextView  #@id/tv_now
   │     ├─ include  #@id/tv_now_description
   │     ├─ ImageView  #@id/iv_trial_reminder
   │     ├─ TextView  #@id/tv_trial_reminder
   │     ├─ ImageView  #@id/iv_trial_ends
   │     └─ TextView  #@id/tv_trial_ends
   ├─ ImageView  #@id/iv_one_time_offer
   ├─ LinearLayout  #@id/ll_pricing
   │  ├─ TextView  #@id/tv_yearly_price
   │  ├─ androidx.compose.ui.platform.ComposeView  #@id/mb_upgrade_modal_upgrade
   │  └─ TextView  #@id/tv_cancel_anytime
   ├─ androidx.compose.ui.platform.ComposeView  #@id/cv_paywall
   └─ androidx.constraintlayout.widget.Group  #@id/group_content
```

## ۳. رشته‌های مرتبط (فهرست کامل)

```text
honest_free_trial_day_1
honest_free_trial_day_2
honest_free_trial_first_step
honest_free_trial_now
honest_free_trial_price_label_part_1
honest_free_trial_price_label_part_2
honest_free_trial_price_label_part_3
honest_free_trial_title
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
