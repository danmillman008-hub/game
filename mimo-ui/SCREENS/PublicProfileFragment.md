# صفحه — `PublicProfileFragment`

> **خاستگاه ثبت:** `DEX UI_CLASSES.json` | **کلاس شواهد:** نام/ساختار `VERIFIED_STATIC`، نگاشت صفحه→لایه `DERIVED` (DEX xref + تطابق نام)، حالت‌ها `PARTIALLY_VERIFIED` (رشتهٔ منبع).

| ویژگی | مقدار |
|---|---|
| کلاس | `com.getmimo.ui.publicprofile.PublicProfileFragment$collectData$1` |
| نوع | `dex-ui-class` |
| exported (manifest) | `` |
| launchMode | `` |
| theme | `` |
| orientation | `` |
| targetActivity | `` |
| app-owned | `True` |
| فناوری | `view|compose (unresolved per screen)` |
| تعداد لایه‌های متصل | 3 |
| ComposeView | خیر |
| WebView | خیر |

## ۱. لایه‌های XML متصل (فهرست کامل)

- [`res/layout/public_profile_activity.xml`](../SOURCE/res/layout/public_profile_activity.xml) → [dossier](LAYOUTS/layout_public_profile_activity.md)
- [`res/layout/public_profile_code_header_view.xml`](../SOURCE/res/layout/public_profile_code_header_view.xml) → [dossier](LAYOUTS/layout_public_profile_code_header_view.md)
- [`res/layout/public_profile_fragment.xml`](../SOURCE/res/layout/public_profile_fragment.xml) → [dossier](LAYOUTS/layout_public_profile_fragment.md)

## ۲. درخت مؤلفه‌ها (همهٔ لایه‌های متصل)

### `res/layout/public_profile_activity.xml`

```text
└─ FrameLayout  #@id/layout_public_profile_activity
```

### `res/layout/public_profile_code_header_view.xml`

```text
└─ TextView  #@id/tv_playgrounds_header
```

### `res/layout/public_profile_fragment.xml`

```text
└─ androidx.constraintlayout.widget.ConstraintLayout  #@id/layout_profile_root
   ├─ com.google.android.material.appbar.AppBarLayout  #@id/appbar_profile
   │  └─ include  #@id/layout_toolbar
   ├─ androidx.recyclerview.widget.RecyclerView  #@id/rv_profile
   └─ com.getmimo.ui.components.common.OfflineView  #@id/profile_offline_view
```

## ۳. رشته‌های مرتبط (فهرست کامل)

```text
public_profile_report_user
public_profile_report_user_dialog_content
public_profile_report_user_dialog_header
public_profile_successfully_followed_profile
public_profile_successfully_reported
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
