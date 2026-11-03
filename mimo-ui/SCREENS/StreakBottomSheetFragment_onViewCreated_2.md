# صفحه — `StreakBottomSheetFragment$onViewCreated$2`

> **خاستگاه ثبت:** `PRIOR_WORK_SCREEN_INVENTORY.csv` | **کلاس شواهد:** نام/ساختار `VERIFIED_STATIC`، نگاشت صفحه→لایه `DERIVED` (DEX xref + تطابق نام)، حالت‌ها `PARTIALLY_VERIFIED` (رشتهٔ منبع).

| ویژگی | مقدار |
|---|---|
| کلاس | `com.getmimo.ui.streaks.bottomsheet.StreakBottomSheetFragment$onViewCreated$2` |
| نوع | `bottom_sheet` |
| exported (manifest) | `` |
| launchMode | `` |
| theme | `` |
| orientation | `` |
| targetActivity | `` |
| app-owned | `True` |
| فناوری | `view|compose` |
| تعداد لایه‌های متصل | 1 |
| ComposeView | بله |
| WebView | خیر |

## ۱. لایه‌های XML متصل (فهرست کامل)

- [`res/layout/streak_bottom_sheet_content.xml`](../SOURCE/res/layout/streak_bottom_sheet_content.xml) → [dossier](LAYOUTS/layout_streak_bottom_sheet_content.md)

## ۲. درخت مؤلفه‌ها (همهٔ لایه‌های متصل)

### `res/layout/streak_bottom_sheet_content.xml`

```text
└─ merge
   ├─ com.getmimo.ui.authentication.lock.AnonymousUserFeatureLockedView  #@id/anonymous_user_lock_view
   ├─ com.getmimo.ui.components.common.OfflineView  #@id/offline_view
   └─ androidx.core.widget.NestedScrollView  #@id/calendar_content_scroll_view
      └─ androidx.constraintlayout.widget.ConstraintLayout
         ├─ ImageView  #@id/ib_calendar_previous_month
         ├─ TextView  #@id/tv_calendar_month_name
         ├─ ImageButton  #@id/ib_calendar_next_month
         ├─ GridView  #@id/gv_calendar_header
         ├─ androidx.recyclerview.widget.RecyclerView  #@id/rv_calendar
         ├─ androidx.constraintlayout.widget.Guideline  #@id/guideline_layout_vertical_middle
         ├─ View
         ├─ androidx.compose.ui.platform.ComposeView  #@id/info_card_streak_challenge
         ├─ com.getmimo.ui.profile.view.ProfileInfoCard  #@id/info_card_streak
         ├─ com.getmimo.ui.profile.view.ProfileInfoCard  #@id/info_card_xp
         ├─ com.getmimo.ui.profile.view.ProfileInfoCard  #@id/info_card_league
         └─ androidx.compose.ui.platform.ComposeView  #@id/info_card_longest_streak
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
