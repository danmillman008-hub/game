# ۱۱د — صف آفلاین

| قابلیت | شاهد | اطمینان |
|---|---|---|
| نوشتن پیشرفت آفلاین | `in_queue` | HIGH |
| ارسال گروهی | `postUnsyncedLessonProgress` | HIGH |
| بنر آفلاین | ۱۴ رشتهٔ `*_offline_*` | HIGH |
| بازیابی پس از kill | Room پایدار | HIGH |
| صف برای اجرای کد | — | **UNKNOWN** |
| صف برای گفتگوی مربی | — | **UNKNOWN** |

```
on_progress_event:
    upsert(lesson_progress, in_queue=1, tries+=1)
    schedule_flush(30s + jitter)
on_flush:
    rows = select where in_queue=1 order by started_at limit 50
    for tutorial group:
        POST /v1/tutorials/{id}/progress  (Idempotency-Key)
        2xx → DELETE where lesson_id in group
        4xx → in_queue=0, flag=rejected      # جلوگیری از حلقه
        5xx/network → backoff, attempts+=1
```
**سنجه‌های پایش:** عمق صف < ۱۰۰ · نرخ شکست < ۱٪ · همگام‌سازی p95 < ۶۰s · رکورد ردشده = ۰.
