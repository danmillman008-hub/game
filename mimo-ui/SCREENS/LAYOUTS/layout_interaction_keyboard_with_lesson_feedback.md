# پروندهٔ لایه — `res/layout/interaction_keyboard_with_lesson_feedback.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/interaction_keyboard_with_lesson_feedback.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/interaction_keyboard_with_lesson_feedback.xml`](../../SOURCE/res/layout/interaction_keyboard_with_lesson_feedback.xml) |
| SHA-256 دیکد | `53190d597c4bb3eb1c0fa2963025add2747e8e02a2261c573e790f97b09012b8` |
| ریشه | `merge` |
| تعداد گره | 3 |
| تعداد شناسه | 3 |
| تگ‌های استفاده‌شده | 3 |
| ویوهای سفارشی `com.getmimo` | 2 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 13 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ merge  #@id/container_interaction_keyboard
   ├─ com.getmimo.ui.lesson.view.InteractionKeyboardView  #@id/interaction_keyboard
   └─ com.getmimo.ui.lesson.view.tags.TagSelectionView  #@id/fillthegap_view
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `merge` | `android:id` | `@id/container_interaction_keyboard` |
| 2 | `com.getmimo.ui.lesson.view.InteractionKeyboardView` | `android:layout_gravity` | `0x00000050` |
| 3 | `com.getmimo.ui.lesson.view.InteractionKeyboardView` | `android:id` | `@id/interaction_keyboard` |
| 4 | `com.getmimo.ui.lesson.view.InteractionKeyboardView` | `android:background` | `@color/transparent` |
| 5 | `com.getmimo.ui.lesson.view.InteractionKeyboardView` | `android:clipChildren` | `false` |
| 6 | `com.getmimo.ui.lesson.view.InteractionKeyboardView` | `android:clipToPadding` | `false` |
| 7 | `com.getmimo.ui.lesson.view.InteractionKeyboardView` | `android:layout_width` | `match_parent` |
| 8 | `com.getmimo.ui.lesson.view.InteractionKeyboardView` | `android:layout_height` | `@dimen/interaction_keyboard_height` |
| 9 | `com.getmimo.ui.lesson.view.tags.TagSelectionView` | `android:gravity` | `0x00000051` |
| 10 | `com.getmimo.ui.lesson.view.tags.TagSelectionView` | `android:id` | `@id/fillthegap_view` |
| 11 | `com.getmimo.ui.lesson.view.tags.TagSelectionView` | `android:background` | `@color/background_secondary` |
| 12 | `com.getmimo.ui.lesson.view.tags.TagSelectionView` | `android:paddingBottom` | `16.000000dip` |
| 13 | `com.getmimo.ui.lesson.view.tags.TagSelectionView` | `android:visibility` | `visible` |
| 14 | `com.getmimo.ui.lesson.view.tags.TagSelectionView` | `android:layout_width` | `match_parent` |
| 15 | `com.getmimo.ui.lesson.view.tags.TagSelectionView` | `android:layout_height` | `wrap_content` |
| 16 | `com.getmimo.ui.lesson.view.tags.TagSelectionView` | `android:baselineAligned` | `false` |
| 17 | `com.getmimo.ui.lesson.view.tags.TagSelectionView` | `app:layout_constraintWidth_max` | `@dimen/lessonview_content_maxwidth` |
| 18 | `com.getmimo.ui.lesson.view.tags.TagSelectionView` | `app:tag_corner_radius` | `@dimen/cardview_corner_radius` |
| 19 | `com.getmimo.ui.lesson.view.tags.TagSelectionView` | `app:tag_enable_unselection` | `false` |
| 20 | `com.getmimo.ui.lesson.view.tags.TagSelectionView` | `app:tag_item_color` | `@color/selection_enabled` |
| 21 | `com.getmimo.ui.lesson.view.tags.TagSelectionView` | `app:tag_item_color_selected` | `@color/selection_selected` |
| 22 | `com.getmimo.ui.lesson.view.tags.TagSelectionView` | `app:tag_item_elevation` | `@dimen/cardview_elevation` |
| 23 | `com.getmimo.ui.lesson.view.tags.TagSelectionView` | `app:tag_item_layout` | `@layout/lesson_interaction_selection_item_layout` |
| 24 | `com.getmimo.ui.lesson.view.tags.TagSelectionView` | `app:tag_item_text_color` | `@color/text_primary` |
| 25 | `com.getmimo.ui.lesson.view.tags.TagSelectionView` | `app:tag_item_text_selected_color` | `@color/selection_selected` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/background_secondary` | `#FFFFFFFF` / `#FF333661` (night) |
| `@color/selection_enabled` | `#FFFFFFFF` / `#FF3F4273` (night) |
| `@color/selection_selected` | `#FFEDEEF6` / `#FF4A4D85` (night) |
| `@color/text_primary` | `#FF252746` / `#FFFFFFFF` (night) |
| `@color/transparent` | `#00000000` |
| `@dimen/cardview_corner_radius` | `6.000000dip` |
| `@dimen/cardview_elevation` | `1.500000dip` |
| `@dimen/interaction_keyboard_height` | `68.000000dip` |
| `@dimen/lessonview_content_maxwidth` | `@dimen/content_max_width` |

## ۴. شناسه‌های `@id`

```text
@id/container_interaction_keyboard
@id/fillthegap_view
@id/interaction_keyboard
```

## ۵. ارجاع به لایه‌های دیگر

```text
(none)
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

(هیچ صفحهٔ نام‌برداری به این لایه متصل نشد؛ ممکن است لایهٔ کتابخانه/`<include>` باشد)

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<merge xmlns:android="http://schemas.android.com/apk/res/android" xmlns:app="http://schemas.android.com/apk/res-auto" android:id="@id/container_interaction_keyboard">
  <com.getmimo.ui.lesson.view.InteractionKeyboardView android:layout_gravity="0x00000050" android:id="@id/interaction_keyboard" android:background="@color/transparent" android:clipChildren="false" android:clipToPadding="false" android:layout_width="match_parent" android:layout_height="@dimen/interaction_keyboard_height"/>
  <com.getmimo.ui.lesson.view.tags.TagSelectionView android:gravity="0x00000051" android:id="@id/fillthegap_view" android:background="@color/background_secondary" android:paddingBottom="16.000000dip" android:visibility="visible" android:layout_width="match_parent" android:layout_height="wrap_content" android:baselineAligned="false" app:layout_constraintWidth_max="@dimen/lessonview_content_maxwidth" app:tag_corner_radius="@dimen/cardview_corner_radius" app:tag_enable_unselection="false" app:tag_item_color="@color/selection_enabled" app:tag_item_color_selected="@color/selection_selected" app:tag_item_elevation="@dimen/cardview_elevation" app:tag_item_layout="@layout/lesson_interaction_selection_item_layout" app:tag_item_text_color="@color/text_primary" app:tag_item_text_selected_color="@color/selection_selected"/>
</merge>
```
