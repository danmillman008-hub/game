# پروندهٔ لایه — `res/layout/search_track_fragment.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/search_track_fragment.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/search_track_fragment.xml`](../../SOURCE/res/layout/search_track_fragment.xml) |
| SHA-256 دیکد | `01871d3eab3a3508eb6f928dd709bfe746f41aff6e2a20f78df34b1c1f0c6057` |
| ریشه | `androidx.constraintlayout.widget.ConstraintLayout` |
| تعداد گره | 6 |
| تعداد شناسه | 5 |
| تگ‌های استفاده‌شده | 5 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 15 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ androidx.constraintlayout.widget.ConstraintLayout
   ├─ androidx.constraintlayout.widget.ConstraintLayout  #@id/layout_searchbar_container
   │  ├─ ImageButton  #@id/btn_cancel_search
   │  └─ EditText  #@id/et_searchview
   ├─ androidx.recyclerview.widget.RecyclerView  #@id/rv_search_results
   └─ View  #@id/tintView
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:fitsSystemWindows` | `true` |
| 2 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_width` | `match_parent` |
| 3 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_height` | `match_parent` |
| 4 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:id` | `@id/layout_searchbar_container` |
| 5 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:background` | `@color/navbar_background` |
| 6 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_width` | `match_parent` |
| 7 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_height` | `@dimen/toolbar_height` |
| 8 | `androidx.constraintlayout.widget.ConstraintLayout` | `app:layout_constraintEnd_toEndOf` | `0` |
| 9 | `androidx.constraintlayout.widget.ConstraintLayout` | `app:layout_constraintStart_toStartOf` | `0` |
| 10 | `androidx.constraintlayout.widget.ConstraintLayout` | `app:layout_constraintTop_toTopOf` | `0` |
| 11 | `ImageButton` | `android:id` | `@id/btn_cancel_search` |
| 12 | `ImageButton` | `android:layout_width` | `48.000000dip` |
| 13 | `ImageButton` | `android:layout_height` | `0.000000dip` |
| 14 | `ImageButton` | `android:layout_marginStart` | `20.000000dip` |
| 15 | `ImageButton` | `android:layout_marginEnd` | `20.000000dip` |
| 16 | `ImageButton` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 17 | `ImageButton` | `app:layout_constraintEnd_toEndOf` | `0` |
| 18 | `ImageButton` | `app:layout_constraintTop_toTopOf` | `0` |
| 19 | `ImageButton` | `app:srcCompat` | `@drawable/ic_close` |
| 20 | `ImageButton` | `app:tint` | `@color/icon_weak` |
| 21 | `ImageButton` | `style` | `@style/ButtonSearchCancel` |
| 22 | `EditText` | `android:id` | `@id/et_searchview` |
| 23 | `EditText` | `android:layout_width` | `0.000000dip` |
| 24 | `EditText` | `android:layout_height` | `match_parent` |
| 25 | `EditText` | `android:hint` | `@string/search_tracks` |
| 26 | `EditText` | `android:singleLine` | `true` |
| 27 | `EditText` | `android:drawablePadding` | `12.000000dip` |
| 28 | `EditText` | `android:inputType` | `0x00000001` |
| 29 | `EditText` | `android:imeOptions` | `0x00000006` |
| 30 | `EditText` | `android:drawableStart` | `@drawable/ic_search` |
| 31 | `EditText` | `android:layout_marginStart` | `8.000000dip` |
| 32 | `EditText` | `android:transitionName` | `searchView` |
| 33 | `EditText` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 34 | `EditText` | `app:layout_constraintEnd_toStartOf` | `@id/btn_cancel_search` |
| 35 | `EditText` | `app:layout_constraintStart_toStartOf` | `0` |
| 36 | `EditText` | `app:layout_constraintTop_toTopOf` | `0` |
| 37 | `EditText` | `style` | `@style/MaterialEditText` |
| 38 | `androidx.recyclerview.widget.RecyclerView` | `android:id` | `@id/rv_search_results` |
| 39 | `androidx.recyclerview.widget.RecyclerView` | `android:background` | `@color/white` |
| 40 | `androidx.recyclerview.widget.RecyclerView` | `android:visibility` | `gone` |
| 41 | `androidx.recyclerview.widget.RecyclerView` | `android:layout_width` | `0.000000dip` |
| 42 | `androidx.recyclerview.widget.RecyclerView` | `android:layout_height` | `0.000000dip` |
| 43 | `androidx.recyclerview.widget.RecyclerView` | `app:layoutManager` | `androidx.recyclerview.widget.LinearLayoutManager` |
| 44 | `androidx.recyclerview.widget.RecyclerView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 45 | `androidx.recyclerview.widget.RecyclerView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 46 | `androidx.recyclerview.widget.RecyclerView` | `app:layout_constraintStart_toStartOf` | `0` |
| 47 | `androidx.recyclerview.widget.RecyclerView` | `app:layout_constraintTop_toBottomOf` | `@id/layout_searchbar_container` |
| 48 | `View` | `android:id` | `@id/tintView` |
| 49 | `View` | `android:background` | `@color/background_primary` |
| 50 | `View` | `android:layout_width` | `0.000000dip` |
| 51 | `View` | `android:layout_height` | `0.000000dip` |
| 52 | `View` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 53 | `View` | `app:layout_constraintEnd_toEndOf` | `0` |
| 54 | `View` | `app:layout_constraintStart_toStartOf` | `0` |
| 55 | `View` | `app:layout_constraintTop_toBottomOf` | `@id/layout_searchbar_container` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/background_primary` | `#FFF6F7FB` / `#FF252746` (night) |
| `@color/icon_weak` | `#FFA3A5C3` / `#80FFFFFF` (night) |
| `@color/navbar_background` | `#FFFFFFFF` / `#FF333661` (night) |
| `@color/white` | `#FFFFFFFF` |
| `@dimen/toolbar_height` | `56.000000dip` |
| `@string/search_tracks` | `Search tracks` |
| `@style/ButtonSearchCancel` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '16.000000sp', 'value_type': 'dimension'}, {'attr': 'android:textColor', 'attr_id': '0x01010098', 'value': '@color/white', 'value_type': 'reference'}, {'attr': 'android:gravity', 'attr_id': '0x010100AF', 'value': '0x00000011', 'value_type': 'int_hex'}, {'attr': 'android:layout_gravity', 'attr_id': '0x010100B3', 'value': '0x00000011', 'value_type': 'int_hex'}, {'attr': 'android:background', 'attr_id': '0x010100D4', 'value': '@null', 'value_type': 'reference'}, {'attr': 'android:padding', 'attr_id': '0x010100D5', 'value': '0.000000dip', 'value_type': 'dimension'}, {'attr': 'android:layout_margin', 'attr_id': '0x010100F6', 'value': '0.000000dip', 'value_type': 'dimension'}, {'attr': 'android:foreground', 'attr_id': '0x01010109', 'value': '?android:0101030E', 'value_type': 'attribute'}, {'attr': 'android:textAllCaps', 'attr_id': '0x0101038C', 'value': 'false', 'value_type': 'int_boolean'}, {'attr': 'android:fontFamily', 'attr_id': '0x010103AC', 'value': '@font/aeonik_pro_medium_normal', 'value_type': 'reference'}]` |
| `@style/MaterialEditText` | `[{'attr': 'android:textColor', 'attr_id': '0x01010098', 'value': '@color/text_primary', 'value_type': 'reference'}, {'attr': 'android:textColorHint', 'attr_id': '0x0101009A', 'value': '@color/text_weak', 'value_type': 'reference'}, {'attr': 'android:padding', 'attr_id': '0x010100D5', 'value': '@dimen/spacing_s', 'value_type': 'reference'}]` |

## ۴. شناسه‌های `@id`

```text
@id/btn_cancel_search
@id/et_searchview
@id/layout_searchbar_container
@id/rv_search_results
@id/tintView
```

## ۵. ارجاع به لایه‌های دیگر

```text
(none)
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

```text
com.getmimo.ui.tracksearch.SearchTrackFragment$onViewCreated$4$1
```

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout xmlns:android="http://schemas.android.com/apk/res/android" xmlns:app="http://schemas.android.com/apk/res-auto" android:fitsSystemWindows="true" android:layout_width="match_parent" android:layout_height="match_parent">
  <androidx.constraintlayout.widget.ConstraintLayout android:id="@id/layout_searchbar_container" android:background="@color/navbar_background" android:layout_width="match_parent" android:layout_height="@dimen/toolbar_height" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="0">
    <ImageButton android:id="@id/btn_cancel_search" android:layout_width="48.000000dip" android:layout_height="0.000000dip" android:layout_marginStart="20.000000dip" android:layout_marginEnd="20.000000dip" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toEndOf="0" app:layout_constraintTop_toTopOf="0" app:srcCompat="@drawable/ic_close" app:tint="@color/icon_weak" style="@style/ButtonSearchCancel"/>
    <EditText android:id="@id/et_searchview" android:layout_width="0.000000dip" android:layout_height="match_parent" android:hint="@string/search_tracks" android:singleLine="true" android:drawablePadding="12.000000dip" android:inputType="0x00000001" android:imeOptions="0x00000006" android:drawableStart="@drawable/ic_search" android:layout_marginStart="8.000000dip" android:transitionName="searchView" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toStartOf="@id/btn_cancel_search" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="0" style="@style/MaterialEditText"/>
  </androidx.constraintlayout.widget.ConstraintLayout>
  <androidx.recyclerview.widget.RecyclerView android:id="@id/rv_search_results" android:background="@color/white" android:visibility="gone" android:layout_width="0.000000dip" android:layout_height="0.000000dip" app:layoutManager="androidx.recyclerview.widget.LinearLayoutManager" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/layout_searchbar_container"/>
  <View android:id="@id/tintView" android:background="@color/background_primary" android:layout_width="0.000000dip" android:layout_height="0.000000dip" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/layout_searchbar_container"/>
</androidx.constraintlayout.widget.ConstraintLayout>
```
