# پروندهٔ لایه — `res/layout/mtrl_picker_actions.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/mtrl_picker_actions.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/mtrl_picker_actions.xml`](../../SOURCE/res/layout/mtrl_picker_actions.xml) |
| SHA-256 دیکد | `6422f8e209e335b7d551a67123267b9e16c499768359263f8ad9efdf92b477d2` |
| ریشه | `LinearLayout` |
| تعداد گره | 3 |
| تعداد شناسه | 3 |
| تگ‌های استفاده‌شده | 2 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 10 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ LinearLayout  #@id/date_picker_actions
   ├─ Button  #@id/cancel_button
   └─ Button  #@id/confirm_button
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `LinearLayout` | `android:gravity` | `0x00800005` |
| 2 | `LinearLayout` | `android:orientation` | `horizontal` |
| 3 | `LinearLayout` | `android:id` | `@id/date_picker_actions` |
| 4 | `LinearLayout` | `android:paddingRight` | `@dimen/mtrl_calendar_action_padding` |
| 5 | `LinearLayout` | `android:layout_width` | `match_parent` |
| 6 | `LinearLayout` | `android:layout_height` | `@dimen/mtrl_calendar_action_height` |
| 7 | `LinearLayout` | `android:paddingEnd` | `@dimen/mtrl_calendar_action_padding` |
| 8 | `Button` | `android:layout_gravity` | `0x00000010` |
| 9 | `Button` | `android:id` | `@id/cancel_button` |
| 10 | `Button` | `android:layout_width` | `wrap_content` |
| 11 | `Button` | `android:layout_height` | `wrap_content` |
| 12 | `Button` | `android:text` | `@string/mtrl_picker_cancel` |
| 13 | `Button` | `style` | `?attr/buttonBarNegativeButtonStyle` |
| 14 | `Button` | `android:layout_gravity` | `0x00000010` |
| 15 | `Button` | `android:id` | `@id/confirm_button` |
| 16 | `Button` | `android:layout_width` | `wrap_content` |
| 17 | `Button` | `android:layout_height` | `wrap_content` |
| 18 | `Button` | `android:minWidth` | `@dimen/mtrl_calendar_action_confirm_button_min_width` |
| 19 | `Button` | `android:text` | `@string/mtrl_picker_confirm` |
| 20 | `Button` | `style` | `?attr/buttonBarPositiveButtonStyle` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@dimen/mtrl_calendar_action_confirm_button_min_width` | `64.000000dip` |
| `@dimen/mtrl_calendar_action_height` | `52.000000dip` |
| `@dimen/mtrl_calendar_action_padding` | `8.000000dip` |
| `@string/mtrl_picker_cancel` | `Cancel` / `Kanselleer` (af) / `ይቅር` (am) / `إلغاء` (ar) / `Cancel` (as) / `Ləğv edin` (az) / `Скасаваць` (be) / `Отказ` (bg) / `বাতিল করুন` (bn) / `Otkaži` (bs) / `Cancel·la` (ca) / `Zrušit` (cs) / `Annuller` (da) / `Abbrechen` (de) / `Ακύρωση` (el) / `Cancel` (en-rGB) / `Cancelar` (es) / `Cancelar` (es-r419) / `Cancelar` (es-rUS) / `Tühista` (et) / `Utzi` (eu) / `لغو` (fa) / `Peru` (fi) / `Annuler` (fr) / `Annuler` (fr-rCA) / `Cancelar` (gl) / `રદ કરો` (gu) / `रद्द करें` (hi) / `Odustani` (hr) / `Mégse` (hu) / `Չեղարկել` (hy) / `Batal` (in) / `Hætta við` (is) / `Annulla` (it) / `ביטול` (iw) / `キャンセル` (ja) / `გაუქმება` (ka) / `Бас тарту` (kk) / `បោះ​បង់` (km) / `ರದ್ದುಮಾಡಿ` (kn) / `취소` (ko) / `Жокко чыгаруу` (ky) / `ຍົກເລີກ` (lo) / `Atšaukti` (lt) / `Atcelt` (lv) / `Откажи` (mk) / `റദ്ദാക്കുക` (ml) / `Цуцлах` (mn) / `रद्द करा` (mr) / `Batal` (ms) / `ပယ်ဖျက်ရန်` (my) / `Avbryt` (nb) / `रद्द गर्नुहोस्` (ne) / `Annuleren` (nl) / `Cancel` (or) / `ਰੱਦ ਕਰੋ` (pa) / `Anuluj` (pl) / `Cancelar` (pt-rBR) / `Cancelar` (pt-rPT) / `Anulați` (ro) / `Отмена` (ru) / `අවලංගු කරන්න` (si) / `Zrušiť` (sk) / `Prekliči` (sl) / `Anulo` (sq) / `Откажи` (sr) / `Avbryt` (sv) / `Ghairi` (sw) / `ரத்துசெய்` (ta) / `రద్దు చేయండి` (te) / `ยกเลิก` (th) / `Kanselahin` (tl) / `İptal` (tr) / `Скасувати` (uk) / `منسوخ کریں` (ur) / `Bekor qilish` (uz) / `Hủy` (vi) / `取消` (zh-rCN) / `取消` (zh-rHK) / `取消` (zh-rTW) / `Khansela` (zu) |
| `@string/mtrl_picker_confirm` | `OK` / `OK` (af) / `እሺ` (am) / `حسنًا` (ar) / `OK` (as) / `OK` (az) / `ОК` (be) / `OK` (bg) / `ঠিক আছে` (bn) / `Uredu` (bs) / `D’acord` (ca) / `OK` (cs) / `OK` (da) / `OK` (de) / `ΟΚ` (el) / `OK` (en-rGB) / `Aceptar` (es) / `Aceptar` (es-r419) / `Aceptar` (es-rUS) / `OK` (et) / `Ados` (eu) / `تأیید` (fa) / `OK` (fi) / `OK` (fr) / `OK` (fr-rCA) / `Aceptar` (gl) / `ઓકે` (gu) / `ठीक है` (hi) / `U redu` (hr) / `OK` (hu) / `Եղավ` (hy) / `Oke` (in) / `Í lagi` (is) / `OK` (it) / `אישור` (iw) / `OK` (ja) / `კარგი` (ka) / `Жарайды` (kk) / `យល់ព្រម` (km) / `ಸರಿ` (kn) / `확인` (ko) / `Жарайт` (ky) / `ຕົກລົງ` (lo) / `Gerai` (lt) / `Labi` (lv) / `Во ред` (mk) / `ശരി` (ml) / `OK` (mn) / `ओके` (mr) / `OK` (ms) / `OK` (my) / `OK` (nb) / `ठिक छ` (ne) / `OK` (nl) / `OK` (or) / `ਠੀਕ ਹੈ` (pa) / `OK` (pl) / `OK` (pt-rBR) / `OK` (pt-rPT) / `OK` (ro) / `ОК` (ru) / `හරි` (si) / `OK` (sk) / `V redu` (sl) / `Në rregull` (sq) / `Потврди` (sr) / `OK` (sv) / `Sawa` (sw) / `சரி` (ta) / `సరే` (te) / `ตกลง` (th) / `OK` (tl) / `Tamam` (tr) / `OK` (uk) / `ٹھیک ہے` (ur) / `OK` (uz) / `OK` (vi) / `确定` (zh-rCN) / `確定` (zh-rHK) / `確定` (zh-rTW) / `KULUNGILE` (zu) |

## ۴. شناسه‌های `@id`

```text
@id/cancel_button
@id/confirm_button
@id/date_picker_actions
```

## ۵. ارجاع به لایه‌های دیگر

```text
(none)
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

(هیچ صفحهٔ نام‌برداری به این لایه متصل نشد؛ ممکن است لایهٔ کتابخانه/`<include>` باشد)

## ۷. لایه‌هایی که این لایه را include می‌کنند

```text
res/layout/mtrl_picker_dialog.xml
```

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android" android:gravity="0x00800005" android:orientation="horizontal" android:id="@id/date_picker_actions" android:paddingRight="@dimen/mtrl_calendar_action_padding" android:layout_width="match_parent" android:layout_height="@dimen/mtrl_calendar_action_height" android:paddingEnd="@dimen/mtrl_calendar_action_padding">
  <Button android:layout_gravity="0x00000010" android:id="@id/cancel_button" android:layout_width="wrap_content" android:layout_height="wrap_content" android:text="@string/mtrl_picker_cancel" style="?attr/buttonBarNegativeButtonStyle"/>
  <Button android:layout_gravity="0x00000010" android:id="@id/confirm_button" android:layout_width="wrap_content" android:layout_height="wrap_content" android:minWidth="@dimen/mtrl_calendar_action_confirm_button_min_width" android:text="@string/mtrl_picker_confirm" style="?attr/buttonBarPositiveButtonStyle"/>
</LinearLayout>
```
