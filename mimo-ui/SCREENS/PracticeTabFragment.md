# صفحه — `PracticeTabFragment`

> **خاستگاه ثبت:** `DEX UI_CLASSES.json` | **کلاس شواهد:** نام/ساختار `VERIFIED_STATIC`، نگاشت صفحه→لایه `DERIVED` (DEX xref + تطابق نام)، حالت‌ها `PARTIALLY_VERIFIED` (رشتهٔ منبع).

| ویژگی | مقدار |
|---|---|
| کلاس | `com.getmimo.ui.practice.PracticeTabFragment$onViewCreated$5$1` |
| نوع | `dex-ui-class` |
| exported (manifest) | `` |
| launchMode | `` |
| theme | `` |
| orientation | `` |
| targetActivity | `` |
| app-owned | `True` |
| فناوری | `view|compose (unresolved per screen)` |
| تعداد لایه‌های متصل | 1 |
| ComposeView | بله |
| WebView | خیر |

## ۱. لایه‌های XML متصل (فهرست کامل)

- [`res/layout/practice_tab_fragment.xml`](../SOURCE/res/layout/practice_tab_fragment.xml) → [dossier](LAYOUTS/layout_practice_tab_fragment.md)

## ۲. درخت مؤلفه‌ها (همهٔ لایه‌های متصل)

### `res/layout/practice_tab_fragment.xml`

```text
└─ androidx.constraintlayout.widget.ConstraintLayout
   ├─ androidx.compose.ui.platform.ComposeView  #@id/cv_practice_tab
   ├─ com.google.android.material.appbar.AppBarLayout  #@id/appbar_practice
   │  └─ include  #@id/layout_toolbar
   └─ com.getmimo.ui.authentication.lock.AnonymousUserFeatureLockedView  #@id/anonymous_user_lock_view
```

## ۳. رشته‌های مرتبط (فهرست کامل)

```text
practice_tab_past_topics_title
practice_tab_see_all
practice_tab_stats_activities
practice_tab_stats_time_on_tasks
practice_tab_stats_title
practice_tab_unlock_header_signup
practice_tab_unlock_message_progress
practice_tab_unlock_message_signup
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
