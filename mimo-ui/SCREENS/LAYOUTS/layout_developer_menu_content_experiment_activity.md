# پروندهٔ لایه — `res/layout/developer_menu_content_experiment_activity.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/developer_menu_content_experiment_activity.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/developer_menu_content_experiment_activity.xml`](../../SOURCE/res/layout/developer_menu_content_experiment_activity.xml) |
| SHA-256 دیکد | `8e63c9c285b55eadacade4fad3a3f264bf0adb5c5b4f96109a4fd1d9b070fca7` |
| ریشه | `androidx.constraintlayout.widget.ConstraintLayout` |
| تعداد گره | 6 |
| تعداد شناسه | 5 |
| تگ‌های استفاده‌شده | 6 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 1 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 3 |
| ارجاع به منابع | 15 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ androidx.constraintlayout.widget.ConstraintLayout
   ├─ include  #@id/layout_toolbar
   ├─ CheckBox  #@id/cb_override_content_experiment
   ├─ TextView  #@id/tv_content_experiment_label
   ├─ EditText  #@id/et_content_experiment_content
   └─ androidx.compose.ui.platform.ComposeView  #@id/btn_use_template
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:fitsSystemWindows` | `true` |
| 2 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_width` | `match_parent` |
| 3 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_height` | `match_parent` |
| 4 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:animateLayoutChanges` | `true` |
| 5 | `include` | `android:id` | `@id/layout_toolbar` |
| 6 | `include` | `android:layout_width` | `match_parent` |
| 7 | `include` | `android:layout_height` | `wrap_content` |
| 8 | `include` | `android:title` | `@string/developer_menu_content_experiment` |
| 9 | `include` | `layout` | `@layout/toolbar` |
| 10 | `CheckBox` | `android:textAppearance` | `@style/TextP2` |
| 11 | `CheckBox` | `android:id` | `@id/cb_override_content_experiment` |
| 12 | `CheckBox` | `android:layout_width` | `0.000000dip` |
| 13 | `CheckBox` | `android:layout_height` | `@dimen/developer_menu_item_height` |
| 14 | `CheckBox` | `android:text` | `@string/developer_menu_content_experiment_override` |
| 15 | `CheckBox` | `android:layout_marginStart` | `@dimen/general_margin_16dp` |
| 16 | `CheckBox` | `android:layout_marginEnd` | `@dimen/general_margin_16dp` |
| 17 | `CheckBox` | `app:layout_constraintEnd_toEndOf` | `0` |
| 18 | `CheckBox` | `app:layout_constraintStart_toStartOf` | `0` |
| 19 | `CheckBox` | `app:layout_constraintTop_toBottomOf` | `@id/layout_toolbar` |
| 20 | `TextView` | `android:textAppearance` | `@style/TextP2` |
| 21 | `TextView` | `android:textColor` | `@color/text_weak` |
| 22 | `TextView` | `android:gravity` | `0x00800003` |
| 23 | `TextView` | `android:id` | `@id/tv_content_experiment_label` |
| 24 | `TextView` | `android:layout_width` | `0.000000dip` |
| 25 | `TextView` | `android:layout_height` | `wrap_content` |
| 26 | `TextView` | `android:layout_marginTop` | `@dimen/general_margin_16dp` |
| 27 | `TextView` | `android:text` | `@string/developer_menu_content_experiment_label` |
| 28 | `TextView` | `android:layout_marginStart` | `@dimen/general_margin_16dp` |
| 29 | `TextView` | `android:layout_marginEnd` | `@dimen/general_margin_16dp` |
| 30 | `TextView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 31 | `TextView` | `app:layout_constraintStart_toStartOf` | `0` |
| 32 | `TextView` | `app:layout_constraintTop_toBottomOf` | `@id/cb_override_content_experiment` |
| 33 | `EditText` | `android:textSize` | `@dimen/code_editor_text_size` |
| 34 | `EditText` | `android:gravity` | `0x00800033` |
| 35 | `EditText` | `android:id` | `@id/et_content_experiment_content` |
| 36 | `EditText` | `android:padding` | `6.000000dip` |
| 37 | `EditText` | `android:layout_width` | `0.000000dip` |
| 38 | `EditText` | `android:layout_height` | `400.000000dip` |
| 39 | `EditText` | `android:layout_marginTop` | `8.000000dip` |
| 40 | `EditText` | `android:fontFamily` | `@font/aeonik_mono` |
| 41 | `EditText` | `android:layout_marginStart` | `@dimen/general_margin_16dp` |
| 42 | `EditText` | `android:layout_marginEnd` | `@dimen/general_margin_16dp` |
| 43 | `EditText` | `app:layout_constraintEnd_toEndOf` | `0` |
| 44 | `EditText` | `app:layout_constraintStart_toStartOf` | `0` |
| 45 | `EditText` | `app:layout_constraintTop_toBottomOf` | `@id/tv_content_experiment_label` |
| 46 | `androidx.compose.ui.platform.ComposeView` | `android:id` | `@id/btn_use_template` |
| 47 | `androidx.compose.ui.platform.ComposeView` | `android:layout_width` | `wrap_content` |
| 48 | `androidx.compose.ui.platform.ComposeView` | `android:layout_height` | `wrap_content` |
| 49 | `androidx.compose.ui.platform.ComposeView` | `android:layout_marginBottom` | `@dimen/general_margin_16dp` |
| 50 | `androidx.compose.ui.platform.ComposeView` | `android:layout_marginStart` | `@dimen/general_margin_16dp` |
| 51 | `androidx.compose.ui.platform.ComposeView` | `android:layout_marginEnd` | `@dimen/general_margin_16dp` |
| 52 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 53 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 54 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintStart_toStartOf` | `0` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/text_weak` | `#FF4A4D85` / `#CCFFFFFF` (night) |
| `@dimen/code_editor_text_size` | `15.000000sp` / `18.000000sp` (sw600dp) |
| `@dimen/developer_menu_item_height` | `56.000000dip` / `70.000000dip` (sw600dp) |
| `@dimen/general_margin_16dp` | `16.000000dip` / `20.000000dip` (sw600dp) |
| `@string/developer_menu_content_experiment` | `Content experiment` |
| `@string/developer_menu_content_experiment_label` | `Enter the content experiment below` |
| `@string/developer_menu_content_experiment_override` | `Override content experiment` |
| `@style/TextP2` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '16.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '4.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '20.799990sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '7.799988sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` (sw600dp) |

## ۴. شناسه‌های `@id`

```text
@id/btn_use_template
@id/cb_override_content_experiment
@id/et_content_experiment_content
@id/layout_toolbar
@id/tv_content_experiment_label
```

## ۵. ارجاع به لایه‌های دیگر

```text
@layout/toolbar
match_parent
wrap_content
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

```text
com.getmimo.ui.developermenu.DeveloperMenuActivity
com.getmimo.ui.developermenu.DeveloperMenuFragment
com.getmimo.ui.developermenu.contentexperiment.DevelopersMenuContentExperimentActivity
```

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout xmlns:app="http://schemas.android.com/apk/res-auto" xmlns:android="http://schemas.android.com/apk/res/android" android:fitsSystemWindows="true" android:layout_width="match_parent" android:layout_height="match_parent" android:animateLayoutChanges="true">
  <include android:id="@id/layout_toolbar" android:layout_width="match_parent" android:layout_height="wrap_content" android:title="@string/developer_menu_content_experiment" layout="@layout/toolbar"/>
  <CheckBox android:textAppearance="@style/TextP2" android:id="@id/cb_override_content_experiment" android:layout_width="0.000000dip" android:layout_height="@dimen/developer_menu_item_height" android:text="@string/developer_menu_content_experiment_override" android:layout_marginStart="@dimen/general_margin_16dp" android:layout_marginEnd="@dimen/general_margin_16dp" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/layout_toolbar"/>
  <TextView android:textAppearance="@style/TextP2" android:textColor="@color/text_weak" android:gravity="0x00800003" android:id="@id/tv_content_experiment_label" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginTop="@dimen/general_margin_16dp" android:text="@string/developer_menu_content_experiment_label" android:layout_marginStart="@dimen/general_margin_16dp" android:layout_marginEnd="@dimen/general_margin_16dp" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/cb_override_content_experiment"/>
  <EditText android:textSize="@dimen/code_editor_text_size" android:gravity="0x00800033" android:id="@id/et_content_experiment_content" android:padding="6.000000dip" android:layout_width="0.000000dip" android:layout_height="400.000000dip" android:layout_marginTop="8.000000dip" android:fontFamily="@font/aeonik_mono" android:layout_marginStart="@dimen/general_margin_16dp" android:layout_marginEnd="@dimen/general_margin_16dp" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/tv_content_experiment_label"/>
  <androidx.compose.ui.platform.ComposeView android:id="@id/btn_use_template" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginBottom="@dimen/general_margin_16dp" android:layout_marginStart="@dimen/general_margin_16dp" android:layout_marginEnd="@dimen/general_margin_16dp" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0"/>
</androidx.constraintlayout.widget.ConstraintLayout>
```
