# ۱۱ب — همگام‌سازی و تعارض

## ۱. الگوی تأییدشده (HIGH)

```
کلاس: LessonProgressRepository$postUnsyncedLessonProgress$2
رشته: DELETE FROM lesson_progress WHERE lesson_id IN (…)
```
```
1) رویداد درس → INSERT/UPDATE lesson_progress (in_queue=1)
2) periodic / پایان درس → POST /v1/tutorials/{tutorialId}/progress
3) موفق → DELETE … WHERE lesson_id IN (ارسال‌شده‌ها)
4) خطا → رکورد باقی می‌ماند
```
⇒ local DB نقش **صف** را دارد، نه آرشیو. آمار کامل فقط سمت سرور است.

## ۲. تعارض: دانش و نادانسته

| سناریو | رفتار | اطمینان |
|---|---|---|
| دو دستگاه هم‌زمان | آخرین نوشتن برنده | INFERRED LOW |
| نسخهٔ محتوا تغییر کرده | سرور با `publishSetVersion` تصمیم می‌گیرد | MEDIUM |
| تکرار ارسال | idempotent؟ **UNKNOWN** | — |
| قطع شبکه در میانه | رکورد می‌ماند | HIGH |

## ۳. طرح قطعی برای محصول هدف

```sql
CREATE TABLE outbox (
  id TEXT PRIMARY KEY, kind TEXT NOT NULL, payload TEXT NOT NULL,
  attempts INTEGER NOT NULL DEFAULT 0, next_retry_at TEXT, created_at TEXT NOT NULL
);
```
1. `Idempotency-Key` = hash(lessonId, attemptNo, deviceId) ⇒ سرور تکرار را حذف می‌کند.
2. ادغام پیشرفت: `max(attempts)`, «اولین completedAt» برنده (نه آخرین).
3. هر رکورد `contentVersion` دارد؛ تغییر کلید پاسخ ⇒ آمار «آلوده» علامت می‌خورد.
4. خطای ۴xx دائمی ⇒ رکورد از صف خارج و در `rejected` ثبت می‌شود (جلوگیری از صف بی‌پایان).
5. backoff نمایی: ۱، ۵، ۳۰، ۱۲۰، ۶۰۰ ثانیه با jitter.
