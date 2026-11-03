# صفحه — `SearchTrackFragment`

> **خاستگاه ثبت:** `DEX UI_CLASSES.json` | **کلاس شواهد:** نام/ساختار `VERIFIED_STATIC`، نگاشت صفحه→لایه `DERIVED` (DEX xref + تطابق نام)، حالت‌ها `PARTIALLY_VERIFIED` (رشتهٔ منبع).

| ویژگی | مقدار |
|---|---|
| کلاس | `com.getmimo.ui.tracksearch.SearchTrackFragment$onViewCreated$4$1` |
| نوع | `dex-ui-class` |
| exported (manifest) | `` |
| launchMode | `` |
| theme | `` |
| orientation | `` |
| targetActivity | `` |
| app-owned | `True` |
| فناوری | `view|compose (unresolved per screen)` |
| تعداد لایه‌های متصل | 2 |
| ComposeView | خیر |
| WebView | خیر |

## ۱. لایه‌های XML متصل (فهرست کامل)

- [`res/layout/search_track_fragment.xml`](../SOURCE/res/layout/search_track_fragment.xml) → [dossier](LAYOUTS/layout_search_track_fragment.md)
- [`res/layout/search_tracks_list_item.xml`](../SOURCE/res/layout/search_tracks_list_item.xml) → [dossier](LAYOUTS/layout_search_tracks_list_item.md)

## ۲. درخت مؤلفه‌ها (همهٔ لایه‌های متصل)

### `res/layout/search_track_fragment.xml`

```text
└─ androidx.constraintlayout.widget.ConstraintLayout
   ├─ androidx.constraintlayout.widget.ConstraintLayout  #@id/layout_searchbar_container
   │  ├─ ImageButton  #@id/btn_cancel_search
   │  └─ EditText  #@id/et_searchview
   ├─ androidx.recyclerview.widget.RecyclerView  #@id/rv_search_results
   └─ View  #@id/tintView
```

### `res/layout/search_tracks_list_item.xml`

```text
└─ androidx.constraintlayout.widget.ConstraintLayout
   ├─ com.google.android.material.card.MaterialCardView  #@id/cardview_banner
   │  ├─ ImageView  #@id/iv_item_icon_rectangle
   │  └─ ImageView  #@id/iv_item_icon_round
   ├─ TextView  #@id/tv_item_title
   └─ TextView  #@id/tv_item_description
```

## ۳. رشته‌های مرتبط (فهرست کامل)

```text
search_tracks
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
