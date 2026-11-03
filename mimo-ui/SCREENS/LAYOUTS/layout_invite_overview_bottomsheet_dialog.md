# پروندهٔ لایه — `res/layout/invite_overview_bottomsheet_dialog.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/invite_overview_bottomsheet_dialog.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/invite_overview_bottomsheet_dialog.xml`](../../SOURCE/res/layout/invite_overview_bottomsheet_dialog.xml) |
| SHA-256 دیکد | `95ccf28e693f7070c5283f5403ad7e79db797784754066322044d95e848af29e` |
| ریشه | `merge` |
| تعداد گره | 5 |
| تعداد شناسه | 3 |
| تگ‌های استفاده‌شده | 5 |
| ویوهای سفارشی `com.getmimo` | 1 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 3 |
| ارجاع به منابع | 8 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ merge
   └─ androidx.constraintlayout.widget.ConstraintLayout
      ├─ include  #@id/invite_bottomsheet_dialog_content
      ├─ com.getmimo.ui.components.common.OfflineView  #@id/layout_invitations_offline
      └─ ProgressBar  #@id/pb_invitations_loading
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:orientation` | `vertical` |
| 2 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:background` | `@color/background_primary` |
| 3 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_width` | `match_parent` |
| 4 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_height` | `wrap_content` |
| 5 | `androidx.constraintlayout.widget.ConstraintLayout` | `app:layout_constraintTop_toBottomOf` | `@id/cv_bottom_sheet_header` |
| 6 | `include` | `android:id` | `@id/invite_bottomsheet_dialog_content` |
| 7 | `include` | `android:visibility` | `invisible` |
| 8 | `include` | `android:layout_width` | `match_parent` |
| 9 | `include` | `android:layout_height` | `wrap_content` |
| 10 | `include` | `layout` | `@layout/invitations_overview_bottomsheet` |
| 11 | `com.getmimo.ui.components.common.OfflineView` | `android:layout_gravity` | `0x00000011` |
| 12 | `com.getmimo.ui.components.common.OfflineView` | `android:id` | `@id/layout_invitations_offline` |
| 13 | `com.getmimo.ui.components.common.OfflineView` | `android:visibility` | `gone` |
| 14 | `com.getmimo.ui.components.common.OfflineView` | `android:layout_width` | `match_parent` |
| 15 | `com.getmimo.ui.components.common.OfflineView` | `android:layout_height` | `wrap_content` |
| 16 | `com.getmimo.ui.components.common.OfflineView` | `android:layout_marginTop` | `60.000000dip` |
| 17 | `com.getmimo.ui.components.common.OfflineView` | `android:layout_marginBottom` | `60.000000dip` |
| 18 | `com.getmimo.ui.components.common.OfflineView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 19 | `com.getmimo.ui.components.common.OfflineView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 20 | `com.getmimo.ui.components.common.OfflineView` | `app:layout_constraintStart_toStartOf` | `0` |
| 21 | `com.getmimo.ui.components.common.OfflineView` | `app:layout_constraintTop_toTopOf` | `0` |
| 22 | `com.getmimo.ui.components.common.OfflineView` | `app:offline_description` | `@string/friends_offline_message` |
| 23 | `ProgressBar` | `android:id` | `@id/pb_invitations_loading` |
| 24 | `ProgressBar` | `android:visibility` | `gone` |
| 25 | `ProgressBar` | `android:layout_width` | `32.000000dip` |
| 26 | `ProgressBar` | `android:layout_height` | `32.000000dip` |
| 27 | `ProgressBar` | `android:layout_marginTop` | `260.000000dip` |
| 28 | `ProgressBar` | `android:layout_marginBottom` | `260.000000dip` |
| 29 | `ProgressBar` | `android:indeterminateTint` | `@color/progress_primary` |
| 30 | `ProgressBar` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 31 | `ProgressBar` | `app:layout_constraintEnd_toEndOf` | `0` |
| 32 | `ProgressBar` | `app:layout_constraintStart_toStartOf` | `0` |
| 33 | `ProgressBar` | `app:layout_constraintTop_toTopOf` | `0` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/background_primary` | `#FFF6F7FB` / `#FF252746` (night) |
| `@color/progress_primary` | `#FF7E4BDE` / `#FFA175EA` (night) |
| `@string/friends_offline_message` | `Connect to the internet to
see and invite your friends` / `Verbinde dich mit dem Internet, /num deine Freunde zu sehen und einzuladen` (de) / `Conéctate a internet para ver e invitar a otras personas` (es) / `Connecte-toi à Internet pour 
voir et inviter tes amis.` (fr) / `Hubungkan ke internet untuk
melihat dan mengundang temanmu` (in) / `Connettiti a internet per vedere
e invitare i tuoi amici` (it) / `Połącz się z internetem, aby
zobaczyć i zaprosić znajomych` (pl) / `Conecte-se à internet para ver
e convidar seus amigos` (pt-rBR) / `Подключись к интернету, чтобы
просматривать и приглашать друзей` (ru) / `Arkadaşlarını görmek ve davet etmek için
internete bağlan` (tr) |

## ۴. شناسه‌های `@id`

```text
@id/invite_bottomsheet_dialog_content
@id/layout_invitations_offline
@id/pb_invitations_loading
```

## ۵. ارجاع به لایه‌های دیگر

```text
@layout/invitations_overview_bottomsheet
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
<merge>
  <androidx.constraintlayout.widget.ConstraintLayout xmlns:android="http://schemas.android.com/apk/res/android" xmlns:app="http://schemas.android.com/apk/res-auto" android:orientation="vertical" android:background="@color/background_primary" android:layout_width="match_parent" android:layout_height="wrap_content" app:layout_constraintTop_toBottomOf="@id/cv_bottom_sheet_header">
    <include android:id="@id/invite_bottomsheet_dialog_content" android:visibility="invisible" android:layout_width="match_parent" android:layout_height="wrap_content" layout="@layout/invitations_overview_bottomsheet"/>
    <com.getmimo.ui.components.common.OfflineView android:layout_gravity="0x00000011" android:id="@id/layout_invitations_offline" android:visibility="gone" android:layout_width="match_parent" android:layout_height="wrap_content" android:layout_marginTop="60.000000dip" android:layout_marginBottom="60.000000dip" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="0" app:offline_description="@string/friends_offline_message"/>
    <ProgressBar android:id="@id/pb_invitations_loading" android:visibility="gone" android:layout_width="32.000000dip" android:layout_height="32.000000dip" android:layout_marginTop="260.000000dip" android:layout_marginBottom="260.000000dip" android:indeterminateTint="@color/progress_primary" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="0"/>
  </androidx.constraintlayout.widget.ConstraintLayout>
</merge>
```
