**REVIEW — گزارش فنی، بدون ادعای تأیید نهایی.** منبع حقیقت: APK اصلی Mimo 9.35
(`sha256 = 48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a`). وضعیتها: `OBSERVED` | `STATICALLY INFERRED` | `RUNTIME VERIFIED` | `SERVER CONFIRMED` | `UNKNOWN`.
هیچ شبیهساز/ADB/لاگ/اسکرینشات/پاسخ سرور در این جلسه وجود ندارد؛ `RUNTIME VERIFIED` و `SERVER CONFIRMED` = **۰**.

# COVERAGE_REPORT — پوشش، بازیافتها، شکستها و ناشناختهها

> **مأموریت «کامل» اعلام نمیشود.** معیار تکمیل، بازسازی و تأیید رفتار است، نه تولید فایل.

## ۱. مخرجهای اندازهگیری شده (`COVERAGE_METRICS.json`)

| کمیت | مقدار | وضعیت |
|---|---|---|
| dex_files | 12 | OBSERVED |
| dex_bytes | 28836088 | OBSERVED |
| class_defs | 29454 | OBSERVED |
| defined_methods | 129071 | OBSERVED |
| methods_with_code | 122546 | OBSERVED |
| methods_without_code | 6525 | OBSERVED |
| method_ids_references | 149567 | OBSERVED |
| field_ids_references | 89600 | OBSERVED |
| string_ids | 121252 | OBSERVED |
| type_ids | 40069 | OBSERVED |
| proto_ids | 37799 | OBSERVED |
| mimo_type_descriptors | 3133 | OBSERVED |

### ۱٫۱ باز reconcile مستقل اعداد قبلی

| ادعای قبلی | منبع مستقل | نتیجه |
|---|---|---|
| ۱۲۲٬۵۴۶ تابع Ghidra | جمع `code_item` در map_list هر ۱۲ DEX = ۱۲۲٬۵۴۶؛ `defined_methods_with_code` = ۱۲۲٬۵۴۶ | ✅ تطابق دقیق، تکتک DEXها (`OBSERVED/HIGH`) |
| ۱٬۲۸۴٬۵۴۲ نماد Ghidra | جمع ۱۲ سربرگ `=== PROGRAM ... symbols=` = ۱٬۲۸۴٬۵۴۲ | ✅ تطابق حسابی؛ **ترکیب نمادها UNKNOWN** |
| ۱۲۹٬۰۷۱ متد (JADX MCP) | جمع `defined_methods_from_class_data` = ۱۲۹٬۰۷۱ | ✅ تطابق دقیق (cross-check اضافی) |

ترکیب نمادها:پایه ساختاری DEX **590287** آیتم، باقیماندهٔ **694255** برچسب تولیدشده توسط Ghidra
(`string_data::`، `EXTERNAL.dex-N::`، برچسبهای کلاس/متد/داده). فرمول دقیق تولید نماد
از سرآیند DEX قابل استخراج نیست ← `UNKNOWN`.

## ۲. درصد پوشش (مخرج واقعی)

| معیار | صورت | مخرج | درصد | یادداشت |
|---|---|---|---|---|
| dex_imported_by_ghidra | 12 | 12 | 100.0 |  |
| dex_auto_analysed_by_ghidra | 12 | 12 | 100.0 |  |
| ghidra_functions_vs_methods_with_code | 122546 | 122546 | 100.0 |  |
| smali_class_files_vs_class_defs | 17626 | 29454 | 59.8425 |  |
| smali_failures_vs_class_defs | 11828 | 29454 | 40.1575 |  |
| jadx_1_5_6_com_getmimo_java_vs_primary_dex_mimo_class_defs | 2211 | 3032 | 72.9222 | JADX 1.5.6 was run on classes.dex only; denominator is the com.getmimo class_defs of that DEX. |
| jadx_1_5_6_stub_file_rate | 2179 | 2211 | 98.5527 | files containing "Method not decompiled" stubs / emitted Java files |
| ghidra_symbol_total_arithmetic_verified | 1284542 | 1284542 | 100.0 | composition remains UNKNOWN; see APK_COMPLETE_INVENTORY.json -> symbol_composition_probe |
| runtime_verified_behaviours | 0 | undefined (no emulator/ADB available) | 0.0 |  |
| server_confirmed_responses | 0 | undefined (no authorized test environment) | 0.0 |  |

## ۳. آنچه بازیابی شد

- همهٔ ۱۲ DEX: هدر، Adler32، SHA-1، map_list، string/type/proto/field/method id، class_def، class_data، code_item (`OBSERVED`).
- Manifest باینری: ۶۱ activity + ۶ alias + ۱۹ service + ۲۰ receiver + ۸ provider + ۲۴ permission + ۵۱ meta-data + ۹ deep-link filter (`OBSERVED`).
- resources.arsc: ۱ پکیج، ۹۴٬۴۰۱ ورودی، ۱۱۷ پیکربندی محلی، ۱۴٬۰۲۳ آیتم public، ۱٬۷۲۱ رشته، ۱٬۶۳۱ dimen، ۲٬۲۳۳ id (`OBSERVED`).
- ۱۲ کتابخانهٔ بومی، ۱۰٬۵۶۴ asset، ۱۰٬۳۱۷ JSON، ۱۱ بستهٔ زبانی محتوا، ۱۰۵٬۶۱۱ رشتهٔ یکتای DEX (`OBSERVED`).
- طرحوارهٔ Room: `lesson_progress` (۱۱ ستون)، `chapter_completions`، `tutorial_completions` + ۶۸ عبارت SQL (`OBSERVED`).
- ۵۳ تعریف Retrofit + ۶۸ رشتهٔ مسیر، ۳٬۱۳۳ توصیفگر `com.getmimo`، ۴٬۱۹۹ لبهٔ ساختاری و ۱۶۱٬۹۴۶ لبهٔ Smali (`OBSERVED`/`STATICALLY INFERRED`).
- ۵۳۹ `DebugMetadata`، ۸۴ فیلد ماشین حالت، ۶۵۲ کلاس suspend، ۱۲۲ تابع هدف با دستورالعمل Dalvik (`OBSERVED`).
- دادهٔ shipped v753: ۱۹ مسیر / ۱۴۴ section / ۲٬۰۰۲ ارجاع tutorial / ۶ نوع گره / ۰ نقض پیوستگی (`OBSERVED`).

## ۴. شکستها و عناصر ازدسترفته

| مورد | مقدار | توضیح |
|---|---|---|
| شکست Smali | 11828 کلاس (40.1575% از class_def) | همه در `classes.dex`؛ `Invalid element width` ۳/۵/…/۱۹. یکسان در baksmali ۲.۳.۴ و smali ۳.x → ساختار payload DEX، نه نسخهٔ ابزار. |
| Smali تولیدشده | 17626 فایل (59.8425%) | پوشش کامل Smali ادعا نمیشود. |
| JADX ۱.۵.۶ | 2211 فایل Java / 2179 فایل دارای stub (98.5527%) | 243002 خطای گزارششده؛ بدنهٔ متدها بازسازی نشده است. |
| xref رشته→تابع Ghidra | ۰ | آنالایزر Reference در PSPEC لودر DEX غیرفعال است؛ نسبت قطعی فیلد به کلاس باز است. |
| R8 mapping | فایل وجود ندارد | فقط ۴۹۱ نگاشت از `DebugMetadata.c`؛ دیابسکیشن کامل UNKNOWN. |
| متدهای بدون بدنه | 6525 | abstract/interface/native طبق `code_off=0`؛ **اینها «عملکرد گمشده» نیستند** (قید ۷ پروژه). |

## ۵. وضعیت نهایی چهارگانه

### WHAT WE KNOW — `OBSERVED`
- ساختار باینری APK و ۱۲ DEX، هشها، شمارشها و تطابق کامل ۱۲۲٬۵۴۶ تابع Ghidra با `code_item`.
- فهرست مؤلفههای Manifest، منابع، کتابخانههای بومی، assetها و طرحوارهٔ Room.
- نام کلاسها، امضاها، رشتههای وضعیت، نقاط API حاشیهگذاریشده و دستورالعملهای ۱۲۲ تابع هدف.
- مدل دادهٔ v753 و اینکه مختصات گرهها در assetها وجود ندارد.

### WHAT WE INFER — `STATICALLY INFERRED`

- لایهبندی SCREEN→VIEWMODEL→USECASE→REPOSITORY تنها در بخشی از گراف دیده شد (لبههای ui→viewmodel ۱۸، viewmodel→usecase ۳۴، usecase→repository ۷۹ مرجع نوعی)؛ **سراسری نیست**.
- فعل HTTP (فقط حدس LOW؛ استنتاج از نام متد رد شده است)؛ مالکیت سروری پاداش؛ نقش کامپوزابلها و routeها.
- معنای فیلدهای `toString()` کاتلین در غیاب xref.

### WHAT WE VERIFIED AT RUNTIME — `RUNTIME VERIFIED` / `SERVER CONFIRMED`

- **۰ مورد.** نه شبیهساز/ADB تأییدشده، نه اسکرینشات، نه UI hierarchy، نه logcat، نه پاسخ سرور.
- هیچ استنتاج استاتیکی بهعنوان مشاهدهٔ اجرا جلوه داده نشده است.

### WHAT WE STILL DO NOT KNOW — `UNKNOWN`

- اعداد `dp` فاصلهٔ عمودی/افقی، تابع منحنی، X/Y گرهها، مقدار `scrollPositionX`/`scrollPositionY` و انیمیشنها.
- ضرایب عددی `rewardMultiplier` / `rewardedSparksForCorrectAnswer`، وزن «درست از بار اول»، آستانههای ETA و ترتیب صفحههای پایان چپتر.
- ترکیب دقیق ۱٬۲۸۴٬۵۴۲ نماد Ghidra، نگاشت کامل R8، نقشهٔ routeهای `NavHost`، نشست/توکن، قواعد لیگ و Streak.
- بدنهٔ پاسخهای سرور و تغییروضعیت پس از آنها، و کلیهٔ رفتارهای runtime.

## ۶. معیارهای تکمیل (مادهٔ ۱۲) — ارزیابی صادقانه

| معیار | وضعیت |
|---|---|
| همهٔ ۱۲ DEX محاسبه شدند | ✅ بله (`OBSERVED`) |
| مؤلفههای اصلی اپ شناسایی شدند | ✅ بله، **تا سطح نام/لایه**؛ نقش کامل UNKNOWN |
| روابط زیرسیستمها نگاشت شدند | ⚠️ جزئی (لبههای نوعی + لبههای Smali)، نه گراف کامل |
| ناوبری و جریان داده بازسازی شدند | ⚠️ جزئی؛ مسیر کامل routeها UNKNOWN |
| حالت محلی و راهدور مهم شناسایی شد | ✅ بله (Room/DataStore/API)، مالکیت برخی UNKNOWN |
| منطق Learning Path تحلیل شد | ⚠️ مدل داده بله، **هندسه خیر** |
| منطق درس و امتیاز تحلیل شد | ⚠️ چرخهٔ ذخیره/همگامسازی بله، **فرمول عددی خیر** |
| ماشینهای حالت coroutine مهم نگاشت شدند | ⚠️ فیلدها و ۱۲۲ بدنهٔ دستورالعملی؛ نمای کامل گذارها خیر |
| شاهد به نتایج مهم پیوست شد | ✅ 309 ورودی در `EVIDENCE_INDEX.json` |
| وضعیت تأیید runtime افشا شد | ✅ بله (۰ مورد) |
| ناشناختهها صریحاً مستند شدند | ✅ بله |
| بازیابی کامل سورس | ❌ خیر، و ادعا نمیشود |

## ۷. شمارش شواهد

| وضعیت | تعداد |
|---|---|
| OBSERVED | 231 |
| STATICALLY INFERRED | 67 |
| UNKNOWN | 11 |

| سطح اطمینان | تعداد |
|---|---|
| HIGH | 231 |
| LOW | 54 |
| MEDIUM | 13 |
| UNKNOWN | 11 |


`RUNTIME VERIFIED` = ۰، `SERVER CONFIRMED` = ۰ (ستونها خالیاند، حذف نشدهاند).
