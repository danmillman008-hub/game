# صفحه — `AuthenticationActivity`

> **خاستگاه ثبت:** `PRIOR_WORK_SCREEN_INVENTORY.csv` | **کلاس شواهد:** نام/ساختار `VERIFIED_STATIC`، نگاشت صفحه→لایه `DERIVED` (DEX xref + تطابق نام)، حالت‌ها `PARTIALLY_VERIFIED` (رشتهٔ منبع).

| ویژگی | مقدار |
|---|---|
| کلاس | `com.getmimo.ui.authentication.AuthenticationActivity` |
| نوع | `activity` |
| exported (manifest) | `` |
| launchMode | `` |
| theme | `@style/MaterialDarkModeTheme.TranslucentStatusBar.NoAnim` |
| orientation | `` |
| targetActivity | `` |
| app-owned | `True` |
| فناوری | `view|compose (unresolved per screen)` |
| تعداد لایه‌های متصل | 5 |
| ComposeView | بله |
| WebView | خیر |

## ۱. لایه‌های XML متصل (فهرست کامل)

- [`res/layout/authentication_activity.xml`](../SOURCE/res/layout/authentication_activity.xml) → [dossier](LAYOUTS/layout_authentication_activity.md)
- [`res/layout/authentication_fragment.xml`](../SOURCE/res/layout/authentication_fragment.xml) → [dossier](LAYOUTS/layout_authentication_fragment.md)
- [`res/layout/authentication_login_fragment.xml`](../SOURCE/res/layout/authentication_login_fragment.xml) → [dossier](LAYOUTS/layout_authentication_login_fragment.md)
- [`res/layout/authentication_terms_and_conditions.xml`](../SOURCE/res/layout/authentication_terms_and_conditions.xml) → [dossier](LAYOUTS/layout_authentication_terms_and_conditions.md)
- [`res/layout/authentication_toolbar.xml`](../SOURCE/res/layout/authentication_toolbar.xml) → [dossier](LAYOUTS/layout_authentication_toolbar.md)

## ۲. درخت مؤلفه‌ها (همهٔ لایه‌های متصل)

### `res/layout/authentication_activity.xml`

```text
└─ androidx.constraintlayout.widget.ConstraintLayout  #@id/container
   └─ ProgressBar  #@id/authentication_progress
```

### `res/layout/authentication_fragment.xml`

```text
└─ androidx.constraintlayout.widget.ConstraintLayout
   ├─ androidx.compose.ui.platform.ComposeView  #@id/btn_skip
   ├─ androidx.compose.ui.platform.ComposeView  #@id/benefits_content
   ├─ androidx.constraintlayout.widget.Barrier  #@id/footer_content
   ├─ androidx.compose.ui.platform.ComposeView  #@id/compose_content
   ├─ include  #@id/layout_terms_conditions
   └─ TextView  #@id/tv_delete_account
```

### `res/layout/authentication_login_fragment.xml`

```text
└─ androidx.constraintlayout.widget.ConstraintLayout
   ├─ ImageView  #@id/btn_back
   ├─ app.rive.runtime.kotlin.RiveAnimationView  #@id/rive_login
   ├─ TextView  #@id/tv_headline_authentication
   ├─ androidx.compose.ui.platform.ComposeView  #@id/btn_login_with_email
   ├─ TextView  #@id/tv_continue_with
   ├─ com.getmimo.ui.authentication.ButtonSocialLogin  #@id/btn_continue_google
   ├─ com.getmimo.ui.authentication.ButtonSocialLogin  #@id/btn_continue_facebook
   │  └─ com.facebook.login.widget.LoginButton  #@id/btn_facebook_login
   ├─ androidx.compose.ui.platform.ComposeView  #@id/cv_last_used_auth_method
   ├─ include  #@id/layout_terms_conditions
   └─ TextView  #@id/tv_delete_account
```

### `res/layout/authentication_terms_and_conditions.xml`

```text
└─ androidx.constraintlayout.widget.ConstraintLayout
   ├─ androidx.constraintlayout.helper.widget.Flow
   ├─ LinearLayout  #@id/ll_terms_conditions_prefix
   │  ├─ TextView  #@id/tv_terms_conditions_prefix
   │  └─ TextView  #@id/tv_sing_in_terms_conditions_prefix
   └─ TextView  #@id/tv_terms
```

### `res/layout/authentication_toolbar.xml`

```text
└─ androidx.constraintlayout.widget.ConstraintLayout
   ├─ ImageView  #@id/btn_back
   └─ TextView  #@id/tv_authentication_step
```

## ۳. رشته‌های مرتبط (فهرست کامل)

```text
authentication_error_email_login_invalid_credentials
authentication_error_login_generic
authentication_error_signup_email_already_in_use
authentication_error_signup_generic
authentication_error_social_different_provider
authentication_error_username_is_needed
```

## ۴. رنگ‌های مرتبط (فهرست کامل)

(none)

## ۵. دایمنشن‌های مرتبط (فهرست کامل)

```text
authentication_email_headline_margin_top
authentication_email_top_bar_margin_horizontal
authentication_email_top_bar_margin_top
```

## ۶. استایل‌های مرتبط (فهرست کامل)

(none)

## ۷. شواهد حالت‌ها (رشته‌های منبع)

```text
authentication_error_email_login_invalid_credentials
authentication_error_login_generic
authentication_error_signup_email_already_in_use
authentication_error_signup_generic
authentication_error_social_different_provider
authentication_error_username_is_needed
```

## ۸. ناوبری / deep link

(هیچ intent-filter/data برای این سطح اعلان نشده)
