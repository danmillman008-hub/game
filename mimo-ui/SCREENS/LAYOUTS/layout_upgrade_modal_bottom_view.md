# پروندهٔ لایه — `res/layout/upgrade_modal_bottom_view.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/upgrade_modal_bottom_view.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/upgrade_modal_bottom_view.xml`](../../SOURCE/res/layout/upgrade_modal_bottom_view.xml) |
| SHA-256 دیکد | `f5a7ed18a5bed335cc9b7efbda8ab443171c04f6ad2b2973740e17bf4e0483ad` |
| ریشه | `merge` |
| تعداد گره | 6 |
| تعداد شناسه | 5 |
| تگ‌های استفاده‌شده | 4 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 1 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 18 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ merge
   ├─ View  #@id/view_bottom_part
   ├─ TextView  #@id/tv_countdown_timer
   ├─ TextView  #@id/tv_yearly_price
   ├─ androidx.compose.ui.platform.ComposeView  #@id/btn_upgrade_modal_upgrade
   └─ androidx.compose.ui.platform.ComposeView  #@id/btn_upgrade_modal_other_plans
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `View` | `android:id` | `@id/view_bottom_part` |
| 2 | `View` | `android:background` | `@color/background_primary` |
| 3 | `View` | `android:layout_width` | `match_parent` |
| 4 | `View` | `android:layout_height` | `0.000000dip` |
| 5 | `View` | `android:layout_marginTop` | `@dimen/spacing_l` |
| 6 | `View` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 7 | `View` | `app:layout_constraintTop_toTopOf` | `0` |
| 8 | `TextView` | `android:textColor` | `@color/text_reversed` |
| 9 | `TextView` | `android:gravity` | `0x00000011` |
| 10 | `TextView` | `android:id` | `@id/tv_countdown_timer` |
| 11 | `TextView` | `android:background` | `@drawable/upgrade_modal_countdown_background` |
| 12 | `TextView` | `android:padding` | `2.000000dip` |
| 13 | `TextView` | `android:visibility` | `gone` |
| 14 | `TextView` | `android:layout_width` | `80.000000dip` |
| 15 | `TextView` | `android:layout_height` | `wrap_content` |
| 16 | `TextView` | `android:lines` | `1` |
| 17 | `TextView` | `android:textAllCaps` | `true` |
| 18 | `TextView` | `app:layout_constraintBottom_toTopOf` | `@id/view_bottom_part` |
| 19 | `TextView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 20 | `TextView` | `app:layout_constraintStart_toStartOf` | `0` |
| 21 | `TextView` | `app:layout_constraintTop_toTopOf` | `@id/view_bottom_part` |
| 22 | `TextView` | `style` | `@style/TextTitle3` |
| 23 | `TextView` | `android:textColor` | `@color/text_primary` |
| 24 | `TextView` | `android:gravity` | `0x00000011` |
| 25 | `TextView` | `android:id` | `@id/tv_yearly_price` |
| 26 | `TextView` | `android:layout_width` | `match_parent` |
| 27 | `TextView` | `android:layout_height` | `wrap_content` |
| 28 | `TextView` | `android:layout_marginTop` | `24.000000dip` |
| 29 | `TextView` | `android:layout_marginHorizontal` | `@dimen/spacing_l` |
| 30 | `TextView` | `app:layout_constraintBottom_toTopOf` | `@id/btn_upgrade_modal_upgrade` |
| 31 | `TextView` | `app:layout_constraintTop_toTopOf` | `@id/view_bottom_part` |
| 32 | `TextView` | `style` | `@style/TextTitle2` |
| 33 | `androidx.compose.ui.platform.ComposeView` | `android:id` | `@id/btn_upgrade_modal_upgrade` |
| 34 | `androidx.compose.ui.platform.ComposeView` | `android:layout_width` | `match_parent` |
| 35 | `androidx.compose.ui.platform.ComposeView` | `android:layout_height` | `wrap_content` |
| 36 | `androidx.compose.ui.platform.ComposeView` | `android:layout_marginTop` | `@dimen/spacing_l` |
| 37 | `androidx.compose.ui.platform.ComposeView` | `android:layout_marginHorizontal` | `@dimen/spacing_s` |
| 38 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintBottom_toTopOf` | `@id/btn_upgrade_modal_other_plans` |
| 39 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintTop_toBottomOf` | `@id/tv_yearly_price` |
| 40 | `androidx.compose.ui.platform.ComposeView` | `android:textColor` | `@color/text_primary` |
| 41 | `androidx.compose.ui.platform.ComposeView` | `android:id` | `@id/btn_upgrade_modal_other_plans` |
| 42 | `androidx.compose.ui.platform.ComposeView` | `android:layout_width` | `wrap_content` |
| 43 | `androidx.compose.ui.platform.ComposeView` | `android:layout_height` | `wrap_content` |
| 44 | `androidx.compose.ui.platform.ComposeView` | `android:layout_marginTop` | `@dimen/spacing_xs` |
| 45 | `androidx.compose.ui.platform.ComposeView` | `android:layout_marginBottom` | `@dimen/spacing_m` |
| 46 | `androidx.compose.ui.platform.ComposeView` | `android:text` | `@string/upgrade_modal_other_plans` |
| 47 | `androidx.compose.ui.platform.ComposeView` | `android:layout_marginHorizontal` | `@dimen/modal_default_padding_horizontal` |
| 48 | `androidx.compose.ui.platform.ComposeView` | `android:paddingHorizontal` | `16.000000dip` |
| 49 | `androidx.compose.ui.platform.ComposeView` | `android:paddingVertical` | `4.000000dip` |
| 50 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 51 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 52 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintStart_toStartOf` | `0` |
| 53 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintTop_toBottomOf` | `@id/btn_upgrade_modal_upgrade` |
| 54 | `androidx.compose.ui.platform.ComposeView` | `style` | `@style/MaterialButton.TextButton` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/background_primary` | `#FFF6F7FB` / `#FF252746` (night) |
| `@color/text_primary` | `#FF252746` / `#FFFFFFFF` (night) |
| `@color/text_reversed` | `#FFFFFFFF` / `#FF252746` (night) |
| `@dimen/modal_default_padding_horizontal` | `24.000000dip` |
| `@dimen/spacing_l` | `24.000000dip` |
| `@dimen/spacing_m` | `16.000000dip` |
| `@dimen/spacing_s` | `12.000000dip` |
| `@dimen/spacing_xs` | `8.000000dip` |
| `@string/upgrade_modal_other_plans` | `View other plans` / `Andere Tarife anzeigen` (de) / `Ver otros planes` (es) / `Voir d'autres plans` (fr) / `Lihat paket lain` (in) / `Vedi altri piani` (it) / `Zobacz inne plany` (pl) / `Veja outros planos` (pt-rBR) / `Смотреть др. планы` (ru) / `Diğer planları gör` (tr) |
| `@style/MaterialButton.TextButton` | `[{'attr': 'android:textAppearance', 'attr_id': '0x01010034', 'value': '@style/TextButton1', 'value_type': 'reference'}, {'attr': 'android:textColor', 'attr_id': '0x01010098', 'value': '@color/material_button_text_state', 'value_type': 'reference'}, {'attr': 'attr.drawableTint', 'attr_id': '0x7F040218', 'value': '@color/material_button_text_state', 'value_type': 'reference'}, {'attr': 'attr.iconTint', 'attr_id': '0x7F0402FA', 'value': '@color/material_button_text_state', 'value_type': 'reference'}, {'attr': 'attr.rippleColor', 'attr_id': '0x7F0404F0', 'value': '@color/support_snow_light', 'value_type': 'reference'}]` |
| `@style/TextTitle2` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '14.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '4.000000sp', 'value_type': 'dimension'}, {'attr': 'android:letterSpacing', 'attr_id': '0x010104B6', 'value': '0.000000', 'value_type': 'float'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_medium', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '18.199983sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '10.399995sp', 'value_type': 'dimension'}, {'attr': 'android:letterSpacing', 'attr_id': '0x010104B6', 'value': '0.000000', 'value_type': 'float'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_medium', 'value_type': 'reference'}]` (sw600dp) |
| `@style/TextTitle3` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '12.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '3.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_medium', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '15.599977sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '7.799988sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_medium', 'value_type': 'reference'}]` (sw600dp) |

## ۴. شناسه‌های `@id`

```text
@id/btn_upgrade_modal_other_plans
@id/btn_upgrade_modal_upgrade
@id/tv_countdown_timer
@id/tv_yearly_price
@id/view_bottom_part
```

## ۵. ارجاع به لایه‌های دیگر

```text
(none)
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

```text
com.getmimo.ui.upgrade.UpgradeModalActivity
com.getmimo.ui.upgrade.UpgradeModalBottomView
```

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<merge xmlns:app="http://schemas.android.com/apk/res-auto" xmlns:android="http://schemas.android.com/apk/res/android">
  <View android:id="@id/view_bottom_part" android:background="@color/background_primary" android:layout_width="match_parent" android:layout_height="0.000000dip" android:layout_marginTop="@dimen/spacing_l" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintTop_toTopOf="0"/>
  <TextView android:textColor="@color/text_reversed" android:gravity="0x00000011" android:id="@id/tv_countdown_timer" android:background="@drawable/upgrade_modal_countdown_background" android:padding="2.000000dip" android:visibility="gone" android:layout_width="80.000000dip" android:layout_height="wrap_content" android:lines="1" android:textAllCaps="true" app:layout_constraintBottom_toTopOf="@id/view_bottom_part" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="@id/view_bottom_part" style="@style/TextTitle3"/>
  <TextView android:textColor="@color/text_primary" android:gravity="0x00000011" android:id="@id/tv_yearly_price" android:layout_width="match_parent" android:layout_height="wrap_content" android:layout_marginTop="24.000000dip" android:layout_marginHorizontal="@dimen/spacing_l" app:layout_constraintBottom_toTopOf="@id/btn_upgrade_modal_upgrade" app:layout_constraintTop_toTopOf="@id/view_bottom_part" style="@style/TextTitle2"/>
  <androidx.compose.ui.platform.ComposeView android:id="@id/btn_upgrade_modal_upgrade" android:layout_width="match_parent" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_l" android:layout_marginHorizontal="@dimen/spacing_s" app:layout_constraintBottom_toTopOf="@id/btn_upgrade_modal_other_plans" app:layout_constraintTop_toBottomOf="@id/tv_yearly_price"/>
  <androidx.compose.ui.platform.ComposeView android:textColor="@color/text_primary" android:id="@id/btn_upgrade_modal_other_plans" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_xs" android:layout_marginBottom="@dimen/spacing_m" android:text="@string/upgrade_modal_other_plans" android:layout_marginHorizontal="@dimen/modal_default_padding_horizontal" android:paddingHorizontal="16.000000dip" android:paddingVertical="4.000000dip" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/btn_upgrade_modal_upgrade" style="@style/MaterialButton.TextButton"/>
</merge>
```
