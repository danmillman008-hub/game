# پروندهٔ لایه — `res/layout/mtrl_calendar_month_navigation.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/mtrl_calendar_month_navigation.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/mtrl_calendar_month_navigation.xml`](../../SOURCE/res/layout/mtrl_calendar_month_navigation.xml) |
| SHA-256 دیکد | `d5b413d7812a9d5dbdb907f842c807769019fcb155ac7caeb1cc634765dd9c51` |
| ریشه | `LinearLayout` |
| تعداد گره | 5 |
| تعداد شناسه | 4 |
| تگ‌های استفاده‌شده | 3 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 15 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ LinearLayout  #@id/month_navigation_bar
   ├─ FrameLayout
   │  └─ com.google.android.material.button.MaterialButton  #@id/month_navigation_fragment_toggle
   ├─ com.google.android.material.button.MaterialButton  #@id/month_navigation_previous
   └─ com.google.android.material.button.MaterialButton  #@id/month_navigation_next
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `LinearLayout` | `android:orientation` | `horizontal` |
| 2 | `LinearLayout` | `android:id` | `@id/month_navigation_bar` |
| 3 | `LinearLayout` | `android:paddingTop` | `@dimen/mtrl_calendar_navigation_top_padding` |
| 4 | `LinearLayout` | `android:paddingBottom` | `@dimen/mtrl_calendar_navigation_bottom_padding` |
| 5 | `LinearLayout` | `android:layout_width` | `match_parent` |
| 6 | `LinearLayout` | `android:layout_height` | `wrap_content` |
| 7 | `FrameLayout` | `android:layout_width` | `0.000000dip` |
| 8 | `FrameLayout` | `android:layout_height` | `match_parent` |
| 9 | `FrameLayout` | `android:layout_weight` | `1.000000` |
| 10 | `com.google.android.material.button.MaterialButton` | `android:gravity` | `0x00800013` |
| 11 | `com.google.android.material.button.MaterialButton` | `android:layout_gravity` | `0x00800003` |
| 12 | `com.google.android.material.button.MaterialButton` | `android:id` | `@id/month_navigation_fragment_toggle` |
| 13 | `com.google.android.material.button.MaterialButton` | `android:layout_width` | `wrap_content` |
| 14 | `com.google.android.material.button.MaterialButton` | `android:layout_height` | `@dimen/mtrl_calendar_navigation_height` |
| 15 | `com.google.android.material.button.MaterialButton` | `android:insetTop` | `0.000000dip` |
| 16 | `com.google.android.material.button.MaterialButton` | `android:insetBottom` | `0.000000dip` |
| 17 | `com.google.android.material.button.MaterialButton` | `android:accessibilityLiveRegion` | `1` |
| 18 | `com.google.android.material.button.MaterialButton` | `app:icon` | `@drawable/material_ic_menu_arrow_down_black_24dp` |
| 19 | `com.google.android.material.button.MaterialButton` | `app:iconGravity` | `0x00000004` |
| 20 | `com.google.android.material.button.MaterialButton` | `app:iconPadding` | `4.000000dip` |
| 21 | `com.google.android.material.button.MaterialButton` | `style` | `?attr/materialCalendarYearNavigationButton` |
| 22 | `com.google.android.material.button.MaterialButton` | `android:gravity` | `0x00000011` |
| 23 | `com.google.android.material.button.MaterialButton` | `android:id` | `@id/month_navigation_previous` |
| 24 | `com.google.android.material.button.MaterialButton` | `android:layout_width` | `@dimen/mtrl_min_touch_target_size` |
| 25 | `com.google.android.material.button.MaterialButton` | `android:layout_height` | `@dimen/mtrl_calendar_navigation_height` |
| 26 | `com.google.android.material.button.MaterialButton` | `android:insetTop` | `0.000000dip` |
| 27 | `com.google.android.material.button.MaterialButton` | `android:insetBottom` | `0.000000dip` |
| 28 | `com.google.android.material.button.MaterialButton` | `android:contentDescription` | `@string/mtrl_picker_a11y_prev_month` |
| 29 | `com.google.android.material.button.MaterialButton` | `app:icon` | `@drawable/material_ic_keyboard_arrow_previous_black_24dp` |
| 30 | `com.google.android.material.button.MaterialButton` | `style` | `?attr/materialCalendarMonthNavigationButton` |
| 31 | `com.google.android.material.button.MaterialButton` | `android:gravity` | `0x00000011` |
| 32 | `com.google.android.material.button.MaterialButton` | `android:id` | `@id/month_navigation_next` |
| 33 | `com.google.android.material.button.MaterialButton` | `android:layout_width` | `@dimen/mtrl_min_touch_target_size` |
| 34 | `com.google.android.material.button.MaterialButton` | `android:layout_height` | `@dimen/mtrl_calendar_navigation_height` |
| 35 | `com.google.android.material.button.MaterialButton` | `android:insetTop` | `0.000000dip` |
| 36 | `com.google.android.material.button.MaterialButton` | `android:insetBottom` | `0.000000dip` |
| 37 | `com.google.android.material.button.MaterialButton` | `android:contentDescription` | `@string/mtrl_picker_a11y_next_month` |
| 38 | `com.google.android.material.button.MaterialButton` | `app:icon` | `@drawable/material_ic_keyboard_arrow_next_black_24dp` |
| 39 | `com.google.android.material.button.MaterialButton` | `style` | `?attr/materialCalendarMonthNavigationButton` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@dimen/mtrl_calendar_navigation_bottom_padding` | `4.000000dip` |
| `@dimen/mtrl_calendar_navigation_height` | `48.000000dip` |
| `@dimen/mtrl_calendar_navigation_top_padding` | `4.000000dip` |
| `@dimen/mtrl_min_touch_target_size` | `48.000000dip` |
| `@string/mtrl_picker_a11y_next_month` | `Change to next month` / `Verander na volgende maand` (af) / `ወደ የሚቀጥለው ወር ቀይር` (am) / `التغيير إلى الشهر التالي` (ar) / `Change to next month` (as) / `Növbəti aya dəyişin` (az) / `Перайсці да наступнага месяца` (be) / `Преминаване към следващия месец` (bg) / `আগামী মাসে যান` (bn) / `Promijeni na sljedeći mjesec` (bs) / `Canvia al mes següent` (ca) / `Přejít na další měsíc` (cs) / `Skift til næste måned` (da) / `Zum nächsten Monat wechseln` (de) / `Αλλαγή στον επόμενο μήνα` (el) / `Change to next month` (en-rGB) / `Cambiar al mes siguiente` (es) / `Cambiar al mes siguiente` (es-r419) / `Cambiar al mes siguiente` (es-rUS) / `Vaheta järgmisele kuule` (et) / `Aldatu hurrengo hilabetera` (eu) / `تغییر به ماه بعدی` (fa) / `Vaihda seuraavaan kuukauteen` (fi) / `Passer au mois suivant` (fr) / `Passer au mois suivant` (fr-rCA) / `Cambiar ao mes seguinte` (gl) / `આગલા મહિના પર બદલો` (gu) / `अगले महीने पर जाएं` (hi) / `Prijelaz na sljedeći mjesec` (hr) / `Váltás a következő hónapra` (hu) / `Անցնել հաջորդ ամիս` (hy) / `Ubah ke bulan berikutnya` (in) / `Breyta í næsta mánuð` (is) / `Passa al mese successivo` (it) / `מעבר לחודש הבא` (iw) / `翌月に変更` (ja) / `შემდეგ თვეზე გადასვლა` (ka) / `Келесі айға өту` (kk) / `ប្ដូរ​ទៅ​ខែបន្ទាប់` (km) / `ಮುಂದಿನ ತಿಂಗಳಿಗೆ ಬದಲಿಸಿ` (kn) / `다음 달로 변경` (ko) / `Кийинки айга өзгөртүү` (ky) / `ປ່ຽນເປັນເດືອນຕໍ່ໄປ` (lo) / `Pakeisti į kitą mėnesį` (lt) / `Pāriet uz nākamo mēnesi` (lv) / `Промени на следниот месец` (mk) / `അടുത്ത മാസത്തിലേക്ക് മാറ്റുക` (ml) / `Дараагийн сар луу өөрчлөх` (mn) / `पुढील महिन्यावर बदला` (mr) / `Tukar kepada bulan seterusnya` (ms) / `နောက်လသို့ ပြောင်းရန်` (my) / `Endre til neste måned` (nb) / `अर्को महिनामा सार्नुहोस्` (ne) / `Naar volgende maand gaan` (nl) / `Change to next month` (or) / `ਅਗਲੇ ਮਹੀਨੇ 'ਤੇ ਜਾਓ` (pa) / `Zmień na następny miesiąc` (pl) / `Alterar para o próximo mês` (pt-rBR) / `Mudar para o mês seguinte` (pt-rPT) / `Treceți la luna următoare` (ro) / `Перейти к следующему месяцу` (ru) / `ලබන මාසයට වෙනස් කරන්න` (si) / `Ďalší mesiac` (sk) / `Spremeni na naslednji mesec` (sl) / `Ndrysho te muaji i ardhshëm` (sq) / `Пређите на следећи месец` (sr) / `Ändra till nästa månad` (sv) / `Nenda kwenye mwezi unaofuata` (sw) / `அடுத்த மாதத்தைக் காட்டு` (ta) / `వచ్చే నెలకు మార్చుతుంది` (te) / `เปลี่ยนไปที่เดือนถัดไป` (th) / `Lumipat sa susunod na buwan` (tl) / `Sonraki aya değiştir` (tr) / `Перейти до наступного місяця` (uk) / `اگلے مہینہ میں منتقل کریں` (ur) / `Keyingi oyga oʻzgartirish` (uz) / `Chuyển sang tháng tiếp theo` (vi) / `转到下个月` (zh-rCN) / `變更為下個月` (zh-rHK) / `變更至下個月` (zh-rTW) / `Shintshela kunyanga elandelayo` (zu) |
| `@string/mtrl_picker_a11y_prev_month` | `Change to previous month` / `Verander na vorige maand` (af) / `ወደ ቀዳሚው ወር ቀይር` (am) / `التغيير إلى الشهر السابق` (ar) / `Change to previous month` (as) / `Əvvəlki aya dəyişin` (az) / `Перайсці да папярэдняга месяца` (be) / `Преминаване към предишния месец` (bg) / `আগের মাসে যান` (bn) / `Promijeni na prethodni mjesec` (bs) / `Canvia al mes anterior` (ca) / `Přejít na předchozí měsíc` (cs) / `Skift til forrige måned` (da) / `Zum vorherigen Monat wechseln` (de) / `Αλλαγή στον προηγούμενο μήνα` (el) / `Change to previous month` (en-rGB) / `Cambiar al mes anterior` (es) / `Cambiar al mes anterior` (es-r419) / `Cambiar al mes anterior` (es-rUS) / `Vaheta eelmisele kuule` (et) / `Aldatu aurreko hilabetera` (eu) / `تغییر به ماه قبلی` (fa) / `Vaihda edelliseen kuukauteen` (fi) / `Passer au mois précédent` (fr) / `Passer au mois précédent` (fr-rCA) / `Cambiar ao mes anterior` (gl) / `પાછલા મહિના પર બદલો` (gu) / `पिछले महीने पर जाएं` (hi) / `Pomicanje na prethodni mjesec` (hr) / `Váltás az előző hónapra` (hu) / `Անցնել նախորդ ամիս` (hy) / `Ubah ke bulan sebelumnya` (in) / `Breyta í fyrri mánuð` (is) / `Passa al mese precedente` (it) / `מעבר לחודש הקודם` (iw) / `前月に変更` (ja) / `წინა თვეზე გადასვლა` (ka) / `Алдыңғы айға өту` (kk) / `ប្ដូរ​ទៅ​ខែមុន` (km) / `ಹಿಂದಿನ ತಿಂಗಳಿಗೆ ಬದಲಿಸಿ` (kn) / `이전 달로 변경` (ko) / `Мурунку айга өзгөртүү` (ky) / `ປ່ຽນເປັນເດືອນຜ່ານມາ` (lo) / `Pakeisti į ankstesnį mėnesį` (lt) / `Pāriet uz iepriekšējo mēnesi` (lv) / `Промени на претходниот месец` (mk) / `മുമ്പത്തെ മാസത്തിലേക്ക് മാറ്റുക` (ml) / `Өмнөх сар луу өөрчлөх` (mn) / `मागील महिन्यावर बदला` (mr) / `Tukar kepada bulan sebelumnya` (ms) / `ယခင်လသို့ ပြောင်းရန်` (my) / `Endre til forrige måned` (nb) / `अघिल्लो महिनामा सार्नुहोस्` (ne) / `Naar vorige maand gaan` (nl) / `Change to previous month` (or) / `ਪਿਛਲੇ ਮਹੀਨੇ 'ਤੇ ਜਾਓ` (pa) / `Zmień na poprzedni miesiąc` (pl) / `Alterar para o mês anterior` (pt-rBR) / `Mudar para o mês anterior` (pt-rPT) / `Treceți la luna anterioară` (ro) / `Перейти к предыдущему месяцу` (ru) / `කලින් මාසයට වෙනස් කරන්න` (si) / `Predchádzajúci mesiac` (sk) / `Spremeni na prejšnji mesec` (sl) / `Ndrysho te muaji i kaluar` (sq) / `Пређите на претходни месец` (sr) / `Ändra till föregående månad` (sv) / `Rudi kwenye mwezi uliotangulia` (sw) / `முந்தைய மாதத்தைக் காட்டு` (ta) / `మునుపటి నెలకు మార్చుతుంది` (te) / `เปลี่ยนไปที่เดือนก่อนหน้า` (th) / `Lumipat sa nakaraang buwan` (tl) / `Önceki aya değiştir` (tr) / `Перейти до попереднього місяця` (uk) / `گزشتہ ماہ میں منتقل کریں` (ur) / `Avvalgi oyga oʻzgartirish` (uz) / `Chuyển về tháng trước` (vi) / `转到上个月` (zh-rCN) / `變更為上個月` (zh-rHK) / `變更至上個月` (zh-rTW) / `Shintshela kunyanga edlule` (zu) |

## ۴. شناسه‌های `@id`

```text
@id/month_navigation_bar
@id/month_navigation_fragment_toggle
@id/month_navigation_next
@id/month_navigation_previous
```

## ۵. ارجاع به لایه‌های دیگر

```text
(none)
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

(هیچ صفحهٔ نام‌برداری به این لایه متصل نشد؛ ممکن است لایهٔ کتابخانه/`<include>` باشد)

## ۷. لایه‌هایی که این لایه را include می‌کنند

```text
res/layout/mtrl_calendar_horizontal.xml
```

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android" xmlns:app="http://schemas.android.com/apk/res-auto" android:orientation="horizontal" android:id="@id/month_navigation_bar" android:paddingTop="@dimen/mtrl_calendar_navigation_top_padding" android:paddingBottom="@dimen/mtrl_calendar_navigation_bottom_padding" android:layout_width="match_parent" android:layout_height="wrap_content">
  <FrameLayout android:layout_width="0.000000dip" android:layout_height="match_parent" android:layout_weight="1.000000">
    <com.google.android.material.button.MaterialButton android:gravity="0x00800013" android:layout_gravity="0x00800003" android:id="@id/month_navigation_fragment_toggle" android:layout_width="wrap_content" android:layout_height="@dimen/mtrl_calendar_navigation_height" android:insetTop="0.000000dip" android:insetBottom="0.000000dip" android:accessibilityLiveRegion="1" app:icon="@drawable/material_ic_menu_arrow_down_black_24dp" app:iconGravity="0x00000004" app:iconPadding="4.000000dip" style="?attr/materialCalendarYearNavigationButton"/>
  </FrameLayout>
  <com.google.android.material.button.MaterialButton android:gravity="0x00000011" android:id="@id/month_navigation_previous" android:layout_width="@dimen/mtrl_min_touch_target_size" android:layout_height="@dimen/mtrl_calendar_navigation_height" android:insetTop="0.000000dip" android:insetBottom="0.000000dip" android:contentDescription="@string/mtrl_picker_a11y_prev_month" app:icon="@drawable/material_ic_keyboard_arrow_previous_black_24dp" style="?attr/materialCalendarMonthNavigationButton"/>
  <com.google.android.material.button.MaterialButton android:gravity="0x00000011" android:id="@id/month_navigation_next" android:layout_width="@dimen/mtrl_min_touch_target_size" android:layout_height="@dimen/mtrl_calendar_navigation_height" android:insetTop="0.000000dip" android:insetBottom="0.000000dip" android:contentDescription="@string/mtrl_picker_a11y_next_month" app:icon="@drawable/material_ic_keyboard_arrow_next_black_24dp" style="?attr/materialCalendarMonthNavigationButton"/>
</LinearLayout>
```
