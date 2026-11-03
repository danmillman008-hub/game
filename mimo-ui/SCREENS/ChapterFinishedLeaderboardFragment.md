# صفحه — `ChapterFinishedLeaderboardFragment`

> **خاستگاه ثبت:** `DEX UI_CLASSES.json` | **کلاس شواهد:** نام/ساختار `VERIFIED_STATIC`، نگاشت صفحه→لایه `DERIVED` (DEX xref + تطابق نام)، حالت‌ها `PARTIALLY_VERIFIED` (رشتهٔ منبع).

| ویژگی | مقدار |
|---|---|
| کلاس | `com.getmimo.ui.chapter.chapterendview.leaderboard.ChapterFinishedLeaderboardFragment$setupAuthenticationObservers$2` |
| نوع | `dex-ui-class` |
| exported (manifest) | `` |
| launchMode | `` |
| theme | `` |
| orientation | `` |
| targetActivity | `` |
| app-owned | `True` |
| فناوری | `view|compose (unresolved per screen)` |
| تعداد لایه‌های متصل | 3 |
| ComposeView | بله |
| WebView | خیر |

## ۱. لایه‌های XML متصل (فهرست کامل)

- [`res/layout/chapter_finished_leaderboard_fragment.xml`](../SOURCE/res/layout/chapter_finished_leaderboard_fragment.xml) → [dossier](LAYOUTS/layout_chapter_finished_leaderboard_fragment.md)
- [`res/layout/chapter_finished_leaderboard_joined.xml`](../SOURCE/res/layout/chapter_finished_leaderboard_joined.xml) → [dossier](LAYOUTS/layout_chapter_finished_leaderboard_joined.md)
- [`res/layout/chapter_finished_leaderboard_status.xml`](../SOURCE/res/layout/chapter_finished_leaderboard_status.xml) → [dossier](LAYOUTS/layout_chapter_finished_leaderboard_status.md)

## ۲. درخت مؤلفه‌ها (همهٔ لایه‌های متصل)

### `res/layout/chapter_finished_leaderboard_fragment.xml`

```text
└─ FrameLayout  #@id/cl_chapter_finished_leaderboard
   ├─ androidx.constraintlayout.widget.ConstraintLayout  #@id/cl_main_content
   │  ├─ FrameLayout  #@id/fl_chapter_finished_leaderboard_container
   │  └─ androidx.compose.ui.platform.ComposeView  #@id/btn_chapter_finished_leaderboard_continue
   └─ ProgressBar  #@id/pb_loading
```

### `res/layout/chapter_finished_leaderboard_joined.xml`

```text
└─ androidx.constraintlayout.widget.ConstraintLayout
   ├─ TextView  #@id/tv_later
   ├─ app.rive.runtime.kotlin.RiveAnimationView  #@id/iv_chapter_finished_leaderboard_joined_icon
   ├─ TextView  #@id/tv_chapter_finished_leaderboard_joined_title
   └─ TextView  #@id/tv_chapter_finished_leaderboard_joined_description
```

### `res/layout/chapter_finished_leaderboard_status.xml`

```text
└─ androidx.constraintlayout.widget.ConstraintLayout
   ├─ Space  #@id/s_chapter_finished_top_space
   ├─ ImageView  #@id/iv_chapter_finished_leaderboard_status_image
   ├─ TextView  #@id/tv_chapter_finished_leaderboard_status_title
   ├─ TextView  #@id/tv_chapter_finished_leaderboard_status_description
   └─ LinearLayout  #@id/chapter_finished_leaderboard_status_user_container
      ├─ FrameLayout  #@id/fl_chapter_finished_leaderboard_status_1st_place
      │  └─ include  #@id/empty_user_item_1st_place
      ├─ View  #@id/v_chapter_finished_leaderboard_status_1st_place_divider
      ├─ FrameLayout  #@id/fl_chapter_finished_leaderboard_status_2nd_place
      │  └─ include  #@id/current_user_item
      ├─ View  #@id/v_chapter_finished_leaderboard_status_3rd_place_divider
      └─ FrameLayout  #@id/fl_chapter_finished_leaderboard_status_3rd_place
         └─ include  #@id/empty_user_item_3rd_place
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
