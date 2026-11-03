# پروندهٔ لایه — `res/layout/mtrl_picker_header_fullscreen.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/mtrl_picker_header_fullscreen.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/mtrl_picker_header_fullscreen.xml`](../../SOURCE/res/layout/mtrl_picker_header_fullscreen.xml) |
| SHA-256 دیکد | `938636fbff5bc1055da0a3f887b9d90f1eac185b20f0cc13656f3522be557409` |
| ریشه | `merge` |
| تعداد گره | 10 |
| تعداد شناسه | 6 |
| تگ‌های استفاده‌شده | 7 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 3 |
| ارجاع به منابع | 25 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ merge
   ├─ LinearLayout  #@id/fullscreen_header
   │  ├─ com.google.android.material.button.MaterialButton  #@id/cancel_button
   │  ├─ FrameLayout  #@id/mtrl_picker_header_title_and_selection
   │  │  ├─ TextView  #@id/mtrl_picker_title_text
   │  │  └─ TextView  #@id/mtrl_picker_header_selection_text
   │  └─ LinearLayout
   │     ├─ com.google.android.material.button.MaterialButton  #@id/confirm_button
   │     └─ include
   └─ View
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `merge` | `android:layout_width` | `match_parent` |
| 2 | `merge` | `android:layout_height` | `wrap_content` |
| 3 | `LinearLayout` | `android:layout_gravity` | `0x00000031` |
| 4 | `LinearLayout` | `android:orientation` | `horizontal` |
| 5 | `LinearLayout` | `android:id` | `@id/fullscreen_header` |
| 6 | `LinearLayout` | `android:paddingLeft` | `@dimen/mtrl_calendar_header_content_padding_fullscreen` |
| 7 | `LinearLayout` | `android:paddingTop` | `@dimen/mtrl_calendar_header_content_padding_fullscreen` |
| 8 | `LinearLayout` | `android:paddingRight` | `@dimen/mtrl_calendar_header_content_padding_fullscreen` |
| 9 | `LinearLayout` | `android:layout_width` | `match_parent` |
| 10 | `LinearLayout` | `android:layout_height` | `@dimen/mtrl_calendar_header_height_fullscreen` |
| 11 | `LinearLayout` | `android:paddingStart` | `@dimen/mtrl_calendar_header_content_padding_fullscreen` |
| 12 | `LinearLayout` | `android:paddingEnd` | `@dimen/mtrl_calendar_header_content_padding_fullscreen` |
| 13 | `LinearLayout` | `style` | `?attr/materialCalendarHeaderLayout` |
| 14 | `com.google.android.material.button.MaterialButton` | `android:gravity` | `0x00000011` |
| 15 | `com.google.android.material.button.MaterialButton` | `android:layout_gravity` | `0x00000030` |
| 16 | `com.google.android.material.button.MaterialButton` | `android:id` | `@id/cancel_button` |
| 17 | `com.google.android.material.button.MaterialButton` | `android:padding` | `12.000000dip` |
| 18 | `com.google.android.material.button.MaterialButton` | `android:layout_width` | `@dimen/mtrl_min_touch_target_size` |
| 19 | `com.google.android.material.button.MaterialButton` | `android:layout_height` | `@dimen/mtrl_min_touch_target_size` |
| 20 | `com.google.android.material.button.MaterialButton` | `android:insetTop` | `0.000000dip` |
| 21 | `com.google.android.material.button.MaterialButton` | `android:insetBottom` | `0.000000dip` |
| 22 | `com.google.android.material.button.MaterialButton` | `android:contentDescription` | `@string/mtrl_picker_cancel` |
| 23 | `com.google.android.material.button.MaterialButton` | `app:icon` | `@drawable/material_ic_clear_black_24dp` |
| 24 | `com.google.android.material.button.MaterialButton` | `style` | `?attr/materialCalendarHeaderCancelButton` |
| 25 | `FrameLayout` | `android:id` | `@id/mtrl_picker_header_title_and_selection` |
| 26 | `FrameLayout` | `android:paddingLeft` | `@dimen/mtrl_calendar_header_text_padding` |
| 27 | `FrameLayout` | `android:focusable` | `false` |
| 28 | `FrameLayout` | `android:focusableInTouchMode` | `false` |
| 29 | `FrameLayout` | `android:layout_width` | `0.000000dip` |
| 30 | `FrameLayout` | `android:layout_height` | `match_parent` |
| 31 | `FrameLayout` | `android:layout_weight` | `1.000000` |
| 32 | `FrameLayout` | `android:importantForAccessibility` | `yes` |
| 33 | `FrameLayout` | `android:paddingStart` | `@dimen/mtrl_calendar_header_text_padding` |
| 34 | `TextView` | `android:gravity` | `0x00800053` |
| 35 | `TextView` | `android:layout_gravity` | `0x00800033` |
| 36 | `TextView` | `android:id` | `@id/mtrl_picker_title_text` |
| 37 | `TextView` | `android:layout_width` | `match_parent` |
| 38 | `TextView` | `android:layout_height` | `wrap_content` |
| 39 | `TextView` | `app:firstBaselineToTopHeight` | `@dimen/mtrl_calendar_title_baseline_to_top_fullscreen` |
| 40 | `TextView` | `style` | `?attr/materialCalendarHeaderTitle` |
| 41 | `TextView` | `android:gravity` | `0x00800053` |
| 42 | `TextView` | `android:layout_gravity` | `0x00800033` |
| 43 | `TextView` | `android:id` | `@id/mtrl_picker_header_selection_text` |
| 44 | `TextView` | `android:layout_width` | `match_parent` |
| 45 | `TextView` | `android:layout_height` | `wrap_content` |
| 46 | `TextView` | `app:firstBaselineToTopHeight` | `@dimen/mtrl_calendar_selection_baseline_to_top_fullscreen` |
| 47 | `TextView` | `app:lineHeight` | `@dimen/mtrl_calendar_header_selection_line_height` |
| 48 | `TextView` | `style` | `?attr/materialCalendarHeaderSelection` |
| 49 | `LinearLayout` | `android:orientation` | `@integer/mtrl_calendar_header_orientation` |
| 50 | `LinearLayout` | `android:layout_width` | `wrap_content` |
| 51 | `LinearLayout` | `android:layout_height` | `wrap_content` |
| 52 | `com.google.android.material.button.MaterialButton` | `android:layout_gravity` | `0x00800035` |
| 53 | `com.google.android.material.button.MaterialButton` | `android:id` | `@id/confirm_button` |
| 54 | `com.google.android.material.button.MaterialButton` | `android:layout_width` | `wrap_content` |
| 55 | `com.google.android.material.button.MaterialButton` | `android:layout_height` | `@dimen/mtrl_min_touch_target_size` |
| 56 | `com.google.android.material.button.MaterialButton` | `android:text` | `@string/mtrl_picker_save` |
| 57 | `com.google.android.material.button.MaterialButton` | `android:contentDescription` | `@string/mtrl_picker_save` |
| 58 | `com.google.android.material.button.MaterialButton` | `style` | `?attr/materialCalendarHeaderConfirmButton` |
| 59 | `include` | `layout` | `@layout/mtrl_picker_header_toggle` |
| 60 | `View` | `android:layout_gravity` | `0x00000050` |
| 61 | `View` | `android:layout_width` | `match_parent` |
| 62 | `View` | `android:layout_height` | `@dimen/mtrl_calendar_header_divider_thickness` |
| 63 | `View` | `style` | `?attr/materialCalendarHeaderDivider` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@dimen/mtrl_calendar_header_content_padding_fullscreen` | `4.000000dip` |
| `@dimen/mtrl_calendar_header_divider_thickness` | `1.000000dip` |
| `@dimen/mtrl_calendar_header_height_fullscreen` | `128.000000dip` / `96.000000dip` (land) |
| `@dimen/mtrl_calendar_header_selection_line_height` | `32.000000dip` |
| `@dimen/mtrl_calendar_header_text_padding` | `12.000000dip` |
| `@dimen/mtrl_calendar_selection_baseline_to_top_fullscreen` | `104.000000dip` / `68.000000dip` (land) |
| `@dimen/mtrl_calendar_title_baseline_to_top_fullscreen` | `68.000000dip` / `32.000000dip` (land) |
| `@dimen/mtrl_min_touch_target_size` | `48.000000dip` |
| `@string/mtrl_picker_cancel` | `Cancel` / `Kanselleer` (af) / `ይቅር` (am) / `إلغاء` (ar) / `Cancel` (as) / `Ləğv edin` (az) / `Скасаваць` (be) / `Отказ` (bg) / `বাতিল করুন` (bn) / `Otkaži` (bs) / `Cancel·la` (ca) / `Zrušit` (cs) / `Annuller` (da) / `Abbrechen` (de) / `Ακύρωση` (el) / `Cancel` (en-rGB) / `Cancelar` (es) / `Cancelar` (es-r419) / `Cancelar` (es-rUS) / `Tühista` (et) / `Utzi` (eu) / `لغو` (fa) / `Peru` (fi) / `Annuler` (fr) / `Annuler` (fr-rCA) / `Cancelar` (gl) / `રદ કરો` (gu) / `रद्द करें` (hi) / `Odustani` (hr) / `Mégse` (hu) / `Չեղարկել` (hy) / `Batal` (in) / `Hætta við` (is) / `Annulla` (it) / `ביטול` (iw) / `キャンセル` (ja) / `გაუქმება` (ka) / `Бас тарту` (kk) / `បោះ​បង់` (km) / `ರದ್ದುಮಾಡಿ` (kn) / `취소` (ko) / `Жокко чыгаруу` (ky) / `ຍົກເລີກ` (lo) / `Atšaukti` (lt) / `Atcelt` (lv) / `Откажи` (mk) / `റദ്ദാക്കുക` (ml) / `Цуцлах` (mn) / `रद्द करा` (mr) / `Batal` (ms) / `ပယ်ဖျက်ရန်` (my) / `Avbryt` (nb) / `रद्द गर्नुहोस्` (ne) / `Annuleren` (nl) / `Cancel` (or) / `ਰੱਦ ਕਰੋ` (pa) / `Anuluj` (pl) / `Cancelar` (pt-rBR) / `Cancelar` (pt-rPT) / `Anulați` (ro) / `Отмена` (ru) / `අවලංගු කරන්න` (si) / `Zrušiť` (sk) / `Prekliči` (sl) / `Anulo` (sq) / `Откажи` (sr) / `Avbryt` (sv) / `Ghairi` (sw) / `ரத்துசெய்` (ta) / `రద్దు చేయండి` (te) / `ยกเลิก` (th) / `Kanselahin` (tl) / `İptal` (tr) / `Скасувати` (uk) / `منسوخ کریں` (ur) / `Bekor qilish` (uz) / `Hủy` (vi) / `取消` (zh-rCN) / `取消` (zh-rHK) / `取消` (zh-rTW) / `Khansela` (zu) |
| `@string/mtrl_picker_save` | `Save` / `Stoor` (af) / `አስቀምጥ` (am) / `حفظ` (ar) / `Save` (as) / `Saxlayın` (az) / `Захаваць` (be) / `Запазване` (bg) / `সেভ করুন` (bn) / `Sačuvaj` (bs) / `Desa` (ca) / `Uložit` (cs) / `Gem` (da) / `Speichern` (de) / `Αποθήκευση` (el) / `Save` (en-rGB) / `Guardar` (es) / `Guardar` (es-r419) / `Guardar` (es-rUS) / `Salvesta` (et) / `Gorde` (eu) / `ذخیره` (fa) / `Tallenna` (fi) / `Enregistrer` (fr) / `Enregistrer` (fr-rCA) / `Gardar` (gl) / `સાચવો` (gu) / `सेव करें` (hi) / `Spremi` (hr) / `Mentés` (hu) / `Պահել` (hy) / `Simpan` (in) / `Vista` (is) / `Salva` (it) / `שמירה` (iw) / `保存` (ja) / `შენახვა` (ka) / `Сақтау` (kk) / `រក្សាទុក` (km) / `ಸೇವ್ ಮಾಡಿ` (kn) / `저장` (ko) / `Сактоо` (ky) / `ບັນທຶກ` (lo) / `Išsaugoti` (lt) / `Saglabāt` (lv) / `Зачувај` (mk) / `സംരക്ഷിക്കുക` (ml) / `Хадгалах` (mn) / `सेव्ह करा` (mr) / `Simpan` (ms) / `သိမ်းရန်` (my) / `Lagre` (nb) / `सुरक्षित गर्नु` (ne) / `Opslaan` (nl) / `Save` (or) / `ਰੱਖਿਅਤ ਕਰੋ` (pa) / `Zapisz` (pl) / `Salvar` (pt-rBR) / `Guardar` (pt-rPT) / `Salvați` (ro) / `Сохранить` (ru) / `සුරකින්න` (si) / `Uložiť` (sk) / `Shrani` (sl) / `Ruaj` (sq) / `Сачувај` (sr) / `Spara` (sv) / `Hifadhi` (sw) / `சேமி` (ta) / `సేవ్ చేయండి` (te) / `บันทึก` (th) / `I-save` (tl) / `Kaydet` (tr) / `Зберегти` (uk) / `محفوظ کریں` (ur) / `Saqlash` (uz) / `Lưu` (vi) / `保存` (zh-rCN) / `儲存` (zh-rHK) / `儲存` (zh-rTW) / `Londoloza` (zu) |

## ۴. شناسه‌های `@id`

```text
@id/cancel_button
@id/confirm_button
@id/fullscreen_header
@id/mtrl_picker_header_selection_text
@id/mtrl_picker_header_title_and_selection
@id/mtrl_picker_title_text
```

## ۵. ارجاع به لایه‌های دیگر

```text
@layout/mtrl_picker_header_toggle
match_parent
wrap_content
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

(هیچ صفحهٔ نام‌برداری به این لایه متصل نشد؛ ممکن است لایهٔ کتابخانه/`<include>` باشد)

## ۷. لایه‌هایی که این لایه را include می‌کنند

```text
res/layout/mtrl_picker_fullscreen.xml
```

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<merge xmlns:android="http://schemas.android.com/apk/res/android" xmlns:app="http://schemas.android.com/apk/res-auto" android:layout_width="match_parent" android:layout_height="wrap_content">
  <LinearLayout android:layout_gravity="0x00000031" android:orientation="horizontal" android:id="@id/fullscreen_header" android:paddingLeft="@dimen/mtrl_calendar_header_content_padding_fullscreen" android:paddingTop="@dimen/mtrl_calendar_header_content_padding_fullscreen" android:paddingRight="@dimen/mtrl_calendar_header_content_padding_fullscreen" android:layout_width="match_parent" android:layout_height="@dimen/mtrl_calendar_header_height_fullscreen" android:paddingStart="@dimen/mtrl_calendar_header_content_padding_fullscreen" android:paddingEnd="@dimen/mtrl_calendar_header_content_padding_fullscreen" style="?attr/materialCalendarHeaderLayout">
    <com.google.android.material.button.MaterialButton android:gravity="0x00000011" android:layout_gravity="0x00000030" android:id="@id/cancel_button" android:padding="12.000000dip" android:layout_width="@dimen/mtrl_min_touch_target_size" android:layout_height="@dimen/mtrl_min_touch_target_size" android:insetTop="0.000000dip" android:insetBottom="0.000000dip" android:contentDescription="@string/mtrl_picker_cancel" app:icon="@drawable/material_ic_clear_black_24dp" style="?attr/materialCalendarHeaderCancelButton"/>
    <FrameLayout android:id="@id/mtrl_picker_header_title_and_selection" android:paddingLeft="@dimen/mtrl_calendar_header_text_padding" android:focusable="false" android:focusableInTouchMode="false" android:layout_width="0.000000dip" android:layout_height="match_parent" android:layout_weight="1.000000" android:importantForAccessibility="yes" android:paddingStart="@dimen/mtrl_calendar_header_text_padding">
      <TextView android:gravity="0x00800053" android:layout_gravity="0x00800033" android:id="@id/mtrl_picker_title_text" android:layout_width="match_parent" android:layout_height="wrap_content" app:firstBaselineToTopHeight="@dimen/mtrl_calendar_title_baseline_to_top_fullscreen" style="?attr/materialCalendarHeaderTitle"/>
      <TextView android:gravity="0x00800053" android:layout_gravity="0x00800033" android:id="@id/mtrl_picker_header_selection_text" android:layout_width="match_parent" android:layout_height="wrap_content" app:firstBaselineToTopHeight="@dimen/mtrl_calendar_selection_baseline_to_top_fullscreen" app:lineHeight="@dimen/mtrl_calendar_header_selection_line_height" style="?attr/materialCalendarHeaderSelection"/>
    </FrameLayout>
    <LinearLayout android:orientation="@integer/mtrl_calendar_header_orientation" android:layout_width="wrap_content" android:layout_height="wrap_content">
      <com.google.android.material.button.MaterialButton android:layout_gravity="0x00800035" android:id="@id/confirm_button" android:layout_width="wrap_content" android:layout_height="@dimen/mtrl_min_touch_target_size" android:text="@string/mtrl_picker_save" android:contentDescription="@string/mtrl_picker_save" style="?attr/materialCalendarHeaderConfirmButton"/>
      <include layout="@layout/mtrl_picker_header_toggle"/>
    </LinearLayout>
  </LinearLayout>
  <View android:layout_gravity="0x00000050" android:layout_width="match_parent" android:layout_height="@dimen/mtrl_calendar_header_divider_thickness" style="?attr/materialCalendarHeaderDivider"/>
</merge>
```
