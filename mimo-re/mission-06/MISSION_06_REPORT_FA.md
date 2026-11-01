# MISSION 6 — خلاصهٔ فارسی

## دامنه
بازسازی معماری و رفتار کلاینت Mimo 9.35 بر پایهٔ همان APK موجود در محیط. هیچ اجرایی انجام نشده؛ هیچ رفتاری
به سرور نسبت داده نشده؛ هفت برچسب شواهد [0 مورد VERIFIED_RUNTIME] (`VERIFIED_STATIC`، `VERIFIED_RUNTIME`، `VERIFIED_EXPERIMENTAL`،
`INFERRED`، `UNKNOWN`، `NOT_RECOVERED`، `BLOCKED`) به‌کار رفته و `VERIFIED_RUNTIME` صفر است.

## نتیجهٔ اصلی
- محتوا: `Track → Section → Tutorial(ids) → Chapter → Lesson → LessonContent`؛ کلید پنج‌جزئی
  `LessonIdentifier{trackId, trackVersion, tutorialId, chapterId, lessonId}`.
- DSL: ۲۹ تگ، هفت پارسر `te.a`…`te.g`، گس‌تر از آنچه پیش‌تر تصور می‌شد (تگ‌ها HTML-شکل‌اند: `p`، `img`، `br`).
- ارزیابی: مقایسهٔ دقیق، سپس نرمال‌سازی `lower()` + نگه‌داشتن `[a-z0-9<.]`؛ پاسخ درست از خودِ ماژول کد
  بریده می‌شود.
- زمان اجرا: `IDLE → AWAITING → CORRECT|PARTIAL|INCORRECT → SOLVED` با `RESET`.
- ماندگاری: سه جدول Room؛ صف ارسال با `in_queue`، ارسال دسته‌ای، حذف پس از ۲xx.
- شبکه: `https://api.mimo.org`، Bearer، ۶۲ اندپوینت.
- مربی هوش مصنوعی: SSE با `FinishReason ∈ {Length, Stop}`؛ بدون تاریخچهٔ محلی.
- بازی‌وارسازی: سکه/کلید/استریک/لیگ/جدول؛ **XP وجود ندارد**.
- طراحی: فونت Aeonik (۱۵ فایل)؛ مقادیر رنگ با ابزار موجود قابل استخراج نبود (`BLOCKED`).

## محدودیت‌ها
اجرای اپ (دستگاه/حساب/شبکه/بیلد اصلی) ممکن نبود؛ ۱۵ آزمون زمان‌اجرا با انتظار مشتق‌شده از کد برنامه‌ریزی و
`BLOCKED` ثبت شده‌اند (`15_RUNTIME/96_TEST_TO_SOURCE_MATRIX.csv`).

## مسیرهای مهم
`MISSION_06_REPORT.md`، `16_INDEX_AND_EVIDENCE/`، `20_FINAL_AUDIT/118_UNRESOLVED_CLAIMS.md`،
`20_FINAL_AUDIT/119_FINAL_REPRODUCIBILITY_REPORT.md`، `report.html`.
