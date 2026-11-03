# پروندهٔ لایه — `res/layout/m3expressive_alert_dialog.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/m3expressive_alert_dialog.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/m3expressive_alert_dialog.xml`](../../SOURCE/res/layout/m3expressive_alert_dialog.xml) |
| SHA-256 دیکد | `59480fec790cd2585d23b5e28f2a18bc52a8421259a53e7f8d7908e05ae46060` |
| ریشه | `androidx.appcompat.widget.AlertDialogLayout` |
| تعداد گره | 13 |
| تعداد شناسه | 10 |
| تگ‌های استفاده‌شده | 8 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 4 |
| ارجاع به منابع | 18 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ androidx.appcompat.widget.AlertDialogLayout  #@id/parentPanel
   ├─ include
   ├─ FrameLayout  #@id/contentPanel
   │  ├─ ImageView  #@id/scrollIndicatorUp
   │  ├─ androidx.core.widget.NestedScrollView  #@id/scrollView
   │  │  └─ LinearLayout
   │  │     ├─ android.widget.Space  #@id/textSpacerNoTitle
   │  │     ├─ TextView  #@0x0102000B
   │  │     └─ android.widget.Space  #@id/textSpacerNoButtons
   │  └─ ImageView  #@id/scrollIndicatorDown
   ├─ FrameLayout  #@id/customPanel
   │  └─ FrameLayout  #@id/custom
   └─ include
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `androidx.appcompat.widget.AlertDialogLayout` | `android:gravity` | `0x00800033` |
| 2 | `androidx.appcompat.widget.AlertDialogLayout` | `android:orientation` | `vertical` |
| 3 | `androidx.appcompat.widget.AlertDialogLayout` | `android:id` | `@id/parentPanel` |
| 4 | `androidx.appcompat.widget.AlertDialogLayout` | `android:clipChildren` | `true` |
| 5 | `androidx.appcompat.widget.AlertDialogLayout` | `android:layout_width` | `match_parent` |
| 6 | `androidx.appcompat.widget.AlertDialogLayout` | `android:layout_height` | `wrap_content` |
| 7 | `androidx.appcompat.widget.AlertDialogLayout` | `android:filterTouchesWhenObscured` | `true` |
| 8 | `include` | `layout` | `@layout/m3expressive_alert_dialog_title` |
| 9 | `FrameLayout` | `android:id` | `@id/contentPanel` |
| 10 | `FrameLayout` | `android:layout_width` | `match_parent` |
| 11 | `FrameLayout` | `android:layout_height` | `wrap_content` |
| 12 | `FrameLayout` | `android:minHeight` | `48.000000dip` |
| 13 | `ImageView` | `android:layout_gravity` | `0x00000030` |
| 14 | `ImageView` | `android:id` | `@id/scrollIndicatorUp` |
| 15 | `ImageView` | `android:background` | `#1F000000` |
| 16 | `ImageView` | `android:visibility` | `gone` |
| 17 | `ImageView` | `android:layout_width` | `match_parent` |
| 18 | `ImageView` | `android:layout_height` | `1.000000dip` |
| 19 | `ImageView` | `android:contentDescription` | `@null` |
| 20 | `ImageView` | `app:backgroundTint` | `?0x01010030` |
| 21 | `androidx.core.widget.NestedScrollView` | `android:id` | `@id/scrollView` |
| 22 | `androidx.core.widget.NestedScrollView` | `android:clipToPadding` | `false` |
| 23 | `androidx.core.widget.NestedScrollView` | `android:layout_width` | `match_parent` |
| 24 | `androidx.core.widget.NestedScrollView` | `android:layout_height` | `wrap_content` |
| 25 | `LinearLayout` | `android:orientation` | `vertical` |
| 26 | `LinearLayout` | `android:layout_width` | `match_parent` |
| 27 | `LinearLayout` | `android:layout_height` | `wrap_content` |
| 28 | `android.widget.Space` | `android:id` | `@id/textSpacerNoTitle` |
| 29 | `android.widget.Space` | `android:visibility` | `gone` |
| 30 | `android.widget.Space` | `android:layout_width` | `match_parent` |
| 31 | `android.widget.Space` | `android:layout_height` | `@dimen/m3expressive_alert_dialog_top_padding` |
| 32 | `TextView` | `android:id` | `@0x0102000B` |
| 33 | `TextView` | `android:paddingLeft` | `?attr/dialogPreferredPadding` |
| 34 | `TextView` | `android:paddingRight` | `?attr/dialogPreferredPadding` |
| 35 | `TextView` | `android:layout_width` | `match_parent` |
| 36 | `TextView` | `android:layout_height` | `wrap_content` |
| 37 | `TextView` | `style` | `?attr/materialAlertDialogBodyTextStyle` |
| 38 | `android.widget.Space` | `android:id` | `@id/textSpacerNoButtons` |
| 39 | `android.widget.Space` | `android:visibility` | `gone` |
| 40 | `android.widget.Space` | `android:layout_width` | `match_parent` |
| 41 | `android.widget.Space` | `android:layout_height` | `@dimen/m3expressive_alert_dialog_bottom_padding` |
| 42 | `ImageView` | `android:layout_gravity` | `0x00000050` |
| 43 | `ImageView` | `android:id` | `@id/scrollIndicatorDown` |
| 44 | `ImageView` | `android:background` | `#1F000000` |
| 45 | `ImageView` | `android:visibility` | `gone` |
| 46 | `ImageView` | `android:layout_width` | `match_parent` |
| 47 | `ImageView` | `android:layout_height` | `1.000000dip` |
| 48 | `ImageView` | `android:contentDescription` | `@null` |
| 49 | `ImageView` | `app:backgroundTint` | `?0x01010030` |
| 50 | `FrameLayout` | `android:id` | `@id/customPanel` |
| 51 | `FrameLayout` | `android:layout_width` | `match_parent` |
| 52 | `FrameLayout` | `android:layout_height` | `wrap_content` |
| 53 | `FrameLayout` | `android:minHeight` | `48.000000dip` |
| 54 | `FrameLayout` | `android:id` | `@id/custom` |
| 55 | `FrameLayout` | `android:layout_width` | `match_parent` |
| 56 | `FrameLayout` | `android:layout_height` | `wrap_content` |
| 57 | `include` | `android:layout_width` | `match_parent` |
| 58 | `include` | `android:layout_height` | `wrap_content` |
| 59 | `include` | `layout` | `@layout/m3_alert_dialog_actions` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@dimen/m3expressive_alert_dialog_bottom_padding` | `24.000000dip` |
| `@dimen/m3expressive_alert_dialog_top_padding` | `24.000000dip` |

## ۴. شناسه‌های `@id`

```text
@0x0102000B
@id/contentPanel
@id/custom
@id/customPanel
@id/parentPanel
@id/scrollIndicatorDown
@id/scrollIndicatorUp
@id/scrollView
@id/textSpacerNoButtons
@id/textSpacerNoTitle
```

## ۵. ارجاع به لایه‌های دیگر

```text
@layout/m3_alert_dialog_actions
@layout/m3expressive_alert_dialog_title
match_parent
wrap_content
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

(هیچ صفحهٔ نام‌برداری به این لایه متصل نشد؛ ممکن است لایهٔ کتابخانه/`<include>` باشد)

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<androidx.appcompat.widget.AlertDialogLayout xmlns:app="http://schemas.android.com/apk/res-auto" xmlns:android="http://schemas.android.com/apk/res/android" android:gravity="0x00800033" android:orientation="vertical" android:id="@id/parentPanel" android:clipChildren="true" android:layout_width="match_parent" android:layout_height="wrap_content" android:filterTouchesWhenObscured="true">
  <include layout="@layout/m3expressive_alert_dialog_title"/>
  <FrameLayout android:id="@id/contentPanel" android:layout_width="match_parent" android:layout_height="wrap_content" android:minHeight="48.000000dip">
    <ImageView android:layout_gravity="0x00000030" android:id="@id/scrollIndicatorUp" android:background="#1F000000" android:visibility="gone" android:layout_width="match_parent" android:layout_height="1.000000dip" android:contentDescription="@null" app:backgroundTint="?0x01010030"/>
    <androidx.core.widget.NestedScrollView android:id="@id/scrollView" android:clipToPadding="false" android:layout_width="match_parent" android:layout_height="wrap_content">
      <LinearLayout android:orientation="vertical" android:layout_width="match_parent" android:layout_height="wrap_content">
        <android.widget.Space android:id="@id/textSpacerNoTitle" android:visibility="gone" android:layout_width="match_parent" android:layout_height="@dimen/m3expressive_alert_dialog_top_padding"/>
        <TextView android:id="@0x0102000B" android:paddingLeft="?attr/dialogPreferredPadding" android:paddingRight="?attr/dialogPreferredPadding" android:layout_width="match_parent" android:layout_height="wrap_content" style="?attr/materialAlertDialogBodyTextStyle"/>
        <android.widget.Space android:id="@id/textSpacerNoButtons" android:visibility="gone" android:layout_width="match_parent" android:layout_height="@dimen/m3expressive_alert_dialog_bottom_padding"/>
      </LinearLayout>
    </androidx.core.widget.NestedScrollView>
    <ImageView android:layout_gravity="0x00000050" android:id="@id/scrollIndicatorDown" android:background="#1F000000" android:visibility="gone" android:layout_width="match_parent" android:layout_height="1.000000dip" android:contentDescription="@null" app:backgroundTint="?0x01010030"/>
  </FrameLayout>
  <FrameLayout android:id="@id/customPanel" android:layout_width="match_parent" android:layout_height="wrap_content" android:minHeight="48.000000dip">
    <FrameLayout android:id="@id/custom" android:layout_width="match_parent" android:layout_height="wrap_content"/>
  </FrameLayout>
  <include android:layout_width="match_parent" android:layout_height="wrap_content" layout="@layout/m3_alert_dialog_actions"/>
</androidx.appcompat.widget.AlertDialogLayout>
```
