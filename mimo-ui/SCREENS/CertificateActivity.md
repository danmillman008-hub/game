# صفحه — `CertificateActivity`

> **خاستگاه ثبت:** `PRIOR_WORK_SCREEN_INVENTORY.csv` | **کلاس شواهد:** نام/ساختار `VERIFIED_STATIC`، نگاشت صفحه→لایه `DERIVED` (DEX xref + تطابق نام)، حالت‌ها `PARTIALLY_VERIFIED` (رشتهٔ منبع).

| ویژگی | مقدار |
|---|---|
| کلاس | `com.getmimo.ui.certificates.CertificateActivity` |
| نوع | `activity` |
| exported (manifest) | `` |
| launchMode | `` |
| theme | `@style/MaterialDarkModeTheme.NoAnim` |
| orientation | `` |
| targetActivity | `` |
| app-owned | `True` |
| فناوری | `view|compose (unresolved per screen)` |
| تعداد لایه‌های متصل | 7 |
| ComposeView | بله |
| WebView | خیر |

## ۱. لایه‌های XML متصل (فهرست کامل)

- [`res/layout/certificate_activity.xml`](../SOURCE/res/layout/certificate_activity.xml) → [dossier](LAYOUTS/layout_certificate_activity.md)
- [`res/layout/certificate_download_dialog_fragment.xml`](../SOURCE/res/layout/certificate_download_dialog_fragment.xml) → [dossier](LAYOUTS/layout_certificate_download_dialog_fragment.md)
- [`res/layout/certificate_upgrade_activity.xml`](../SOURCE/res/layout/certificate_upgrade_activity.xml) → [dossier](LAYOUTS/layout_certificate_upgrade_activity.md)
- [`res/layout/profile_certificate_view.xml`](../SOURCE/res/layout/profile_certificate_view.xml) → [dossier](LAYOUTS/layout_profile_certificate_view.md)
- [`res/layout/profile_certificates_item.xml`](../SOURCE/res/layout/profile_certificates_item.xml) → [dossier](LAYOUTS/layout_profile_certificates_item.md)
- [`res/layout/profile_certificates_max_item.xml`](../SOURCE/res/layout/profile_certificates_max_item.xml) → [dossier](LAYOUTS/layout_profile_certificates_max_item.md)
- [`res/layout/profile_certificates_view.xml`](../SOURCE/res/layout/profile_certificates_view.xml) → [dossier](LAYOUTS/layout_profile_certificates_view.md)

## ۲. درخت مؤلفه‌ها (همهٔ لایه‌های متصل)

### `res/layout/certificate_activity.xml`

```text
└─ androidx.constraintlayout.widget.ConstraintLayout  #@id/layout_certificate_activity
   ├─ com.google.android.material.appbar.AppBarLayout  #@id/appbar_certificate
   │  └─ include  #@id/layout_toolbar
   ├─ ImageView  #@id/iv_certificate_pdf
   ├─ ProgressBar  #@id/pb_certificate
   └─ androidx.compose.ui.platform.ComposeView  #@id/btn_download_certificate
```

### `res/layout/certificate_download_dialog_fragment.xml`

```text
└─ FrameLayout  #@id/layout_base_modal
   └─ androidx.cardview.widget.CardView
      └─ androidx.constraintlayout.widget.ConstraintLayout
         ├─ app.rive.runtime.kotlin.RiveAnimationView  #@id/rive_congrats_animation
         ├─ ImageButton  #@id/iv_modal_close
         ├─ TextView  #@id/tv_base_modal_title
         ├─ TextView  #@id/tv_base_modal_description
         ├─ com.google.android.material.textfield.TextInputLayout  #@id/til_certificate_download_dialog_name
         │  └─ com.google.android.material.textfield.TextInputEditText  #@id/et_certificate_download_dialog_name
         └─ androidx.compose.ui.platform.ComposeView  #@id/btn_primary_action
```

### `res/layout/certificate_upgrade_activity.xml`

```text
└─ androidx.constraintlayout.widget.ConstraintLayout
   ├─ LinearLayout  #@id/ll_certificate_upgrade
   │  ├─ ImageView  #@id/iv_badge
   │  ├─ TextView
   │  └─ TextView  #@id/tv_user_name
   ├─ TextView  #@id/tv_title
   ├─ LinearLayout  #@id/ll_advantages_upgrade
   │  ├─ TextView
   │  ├─ TextView
   │  └─ TextView
   ├─ TextView  #@id/tv_secured_by
   ├─ androidx.compose.ui.platform.ComposeView  #@id/btn_upgrade
   └─ androidx.compose.ui.platform.ComposeView  #@id/btn_no_thanks
```

### `res/layout/profile_certificate_view.xml`

```text
└─ androidx.constraintlayout.widget.ConstraintLayout
   ├─ ImageView  #@id/iv_certificate_icon
   ├─ TextView  #@id/tv_certificate_title
   ├─ com.google.android.material.progressindicator.CircularProgressIndicator  #@id/certificate_progress
   ├─ TextView  #@id/tv_certificate_progress_text
   ├─ ImageView  #@id/iv_certificate_download
   └─ View  #@id/v_separator
```

### `res/layout/profile_certificates_item.xml`

```text
└─ LinearLayout
   ├─ TextView
   └─ com.getmimo.ui.profile.view.ProfileCertificatesView  #@id/profile_paths_progress_view
```

### `res/layout/profile_certificates_max_item.xml`

```text
└─ androidx.constraintlayout.widget.ConstraintLayout
   ├─ TextView  #@id/tv_certificate_title
   ├─ ImageView  #@id/iv_certificate_info_icon
   └─ com.getmimo.ui.profile.view.ProfileCertificatesView  #@id/profile_paths_progress_view
```

### `res/layout/profile_certificates_view.xml`

```text
└─ merge
   └─ LinearLayout  #@id/profile_paths_container
```

## ۳. رشته‌های مرتبط (فهرست کامل)

```text
certificate
certificate_snackbar_download_message
certificate_upselling_boost_your_learning
certificate_upselling_closer_to_certificate
certificate_upselling_download_all
certificate_upselling_get_your_certificate_now
certificate_upselling_likely_to_finish
certificates_download
certificates_finished_track_content
certificates_finished_track_dialog_action_submit
certificates_finished_track_dialog_hint
certificates_finished_track_dialog_text
certificates_finished_track_dialog_title
certificates_finished_track_headline
certificates_of_completion
certificates_permission_denied_message
certificates_permission_denied_title
certificates_permission_rationale_description
certificates_permission_rationale_title
certificates_professional_check_your_email
certificates_professional_dialog_description
certificates_professional_dialog_email
certificates_professional_dialog_email_plus_error
certificates_professional_dialog_error
certificates_professional_dialog_name
certificates_professional_dialog_title
certificates_professional_email
certificates_professional_title
certificates_unfinished_track_content
certificates_unfinished_track_dialog_action
certificates_unfinished_track_dialog_text
certificates_unfinished_track_dialog_title
certificates_unfinished_track_headline
error_certificate_download
error_certificate_get
error_certificate_invalid_username
get_certificate
path_completion_estimation_certificate
path_overview_certificate_completion_title
path_overview_certificate_percent_complete
pro_upsell_certificate_comment_1
pro_upsell_certificate_comment_2
profile_certificates
profile_certificates_completion_description
profile_certificates_completion_title
profile_certificates_professional_description
profile_certificates_professional_title
upgrade_modal_certificate_ltc_description
upgrade_modal_certificate_other_description
upgrade_modal_certificate_title
```

## ۴. رنگ‌های مرتبط (فهرست کامل)

(none)

## ۵. دایمنشن‌های مرتبط (فهرست کامل)

(none)

## ۶. استایل‌های مرتبط (فهرست کامل)

(none)

## ۷. شواهد حالت‌ها (رشته‌های منبع)

```text
certificates_professional_dialog_email_plus_error
certificates_professional_dialog_error
error_certificate_download
error_certificate_get
error_certificate_invalid_username
upgrade_modal_certificate_ltc_description
upgrade_modal_certificate_other_description
upgrade_modal_certificate_title
```

## ۸. ناوبری / deep link

(هیچ intent-filter/data برای این سطح اعلان نشده)
