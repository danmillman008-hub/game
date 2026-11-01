# ۱۷ج — قرارداد API هدف

```
Auth:      POST /v1/auth/otp/request | /v1/auth/otp/verify | /v1/auth/refresh
Profile:   GET  /v1/me | PATCH /v1/me | GET /v1/me/entitlement
Content:   GET  /v1/content/manifest | GET /v1/content/pack/{id}/{version}
Concepts:  GET  /v1/concepts | GET /v1/concepts/{id}/graph
Questions: GET  /v1/questions?concept=&difficulty=&cursor=
Practice:  POST /v1/practice/session | POST /v1/practice/answer
Exams:     POST /v1/exams | POST /v1/exams/{id}/answer | POST /v1/exams/{id}/submit
           GET  /v1/exams/{id}/result
Mastery:   GET  /v1/mastery | GET /v1/mastery/review-queue
Analytics: GET  /v1/analytics/weakness | GET /v1/analytics/forecast
Assistant: POST /v1/assistant/messages | GET /v1/assistant/conversations/{id}
Sync:      POST /v1/sync/progress (batch + Idempotency-Key)
Config:    GET  /v1/config
```

## قراردادهای عمومی

| مورد | قاعده |
|---|---|
| احراز | `Authorization: Bearer <access>` + `refresh` کوتاه‌عمر |
| Idempotency | هدر `Idempotency-Key` روی همهٔ POST های نوشتنی |
| صفحه‌بندی | cursor: `{items[], nextCursor}` |
| خطا | `{code, message, details}` + `traceId` |
| نسخه | `X-Min-Client-Version` (اجبار به‌روزرسانی) |
| زمان | ISO-8601 UTC |
| نرخ | ۱۰۰/min/کاربر + `Retry-After` |
| فشرده‌سازی | gzip برای pack |
| آفلاین | همهٔ GET های محتوایی کش‌پذیر با ETag |

## تفاوت با Mimo (صادقانه)

| موضوع | Mimo | هدف |
|---|---|---|
| مسیرها | ۶۲ endpoint پراکنده | ۲۲ endpoint با دامنهٔ روشن |
| نسخه | v1 + یک v2 | v1 با نسخه‌بندی محتوایی |
| خطا | نامعلوم | ساخت‌یافته |
| آزمون | ❌ | هسته |
| تراز/رتبه | ❌ | هسته |
