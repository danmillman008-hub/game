# AGENTS.md — راهنمای ایجنت در این ریپو

## محصول

اپلیکیشن اندروید انبارگردانی داروخانه، برند موقت **«انبار دارو»**، پکیج
`ir.darookhaneh.stock`. فارسی، RTL، فونت وزیرمتن، **آفلاین اول**، بدون اکانت آنلاین.
کد محصول در `android/` است. مدل داده: دارو → بچ → موجودی (Room).

## قوانین سخت (بدون استثنا)

1. **اول `agent-skills/PROJECT-RULES.md` را بخوان.** بر هر مهارتی مقدم است.
2. **Android-only**: KMP / expect-actual / iOS اضافه نکن.
3. **DI ما Koin است، نه Hilt.** پیشنهادهای Hilt-محور مهارت‌ها را اجرا نکن.
4. هر پارامتر سازنده باید در گراف Koin ثبت شود؛ مقدار پیش‌فرض تزریق نمی‌شود
   (تاریخ این باگ: `docs/POSTMORTEM-2026-10-25-launch-crash.md`). وابستگی جدید ⇒
   ثبت صریح + سبز شدن `KoinGraphTest`.
5. **هیچ IO/query/side effect در Composable**؛ `collectAsStateWithLifecycle`.
6. **ML Kit bundled** را با Code Scanner یا نسخهٔ وابسته به Play Services عوض نکن.
7. منطق دارو/بچ/موجودی بدون تست تحویل نمی‌شود؛ موجودی در یک transaction اتمیک.
8. هیچ فایلی از `agent-skills/` نباید وارد `android/` یا APK شود.

## مهارت‌ها

- فهرست: `agent-skills/INDEX.md` · راهنما و نقشهٔ فازها: `agent-skills/README.md`
- **فقط مهارت مرتبط با کار جاری** را بخوان، نه همه.
- مهارت = چک‌لیست و داور؛ دستور تغییر معماری نیست.
- بررسی سلامت نصب: `python3 agent-skills/tools/check.py`

## بیلد و تأیید

سندباکس JDK/Android SDK ندارد؛ بیلد فقط روی GitHub Actions:

- `product-build` → assemble debug+release، تست واحد، انتشار APK در Release `apk-latest`
- `app-smoke` → نصب و اجرای واقعی روی امولاتور AOSP + crash buffer در Issue
- `skills-check` → اعتبارسنجی `agent-skills/`

«بیلد سبز» کافی نیست؛ **اپ باید روی دستگاه باز شود** (`VERDICT_* = APP_RUNNING`).
