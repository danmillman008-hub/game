# ۰۹ — مدل پیشرفت

## ۱. موجودیت‌ها

| موجودیت | منبع شاهد | کلید |
|---|---|---|
| پیشرفت درس | جدول `lesson_progress` (بخش ۱۱) | `(lessonId, tutorialId, tutorialVersion, publishSetVersion)` |
| پیشرفت فصل | مشتق از درس‌ها | `chapterId` |
| پیشرفت آموزش | مشتق | `tutorialId` |
| پیشرفت مسیر | مشتق از بخش‌ها (`startIndex`) | `trackId` |
| آخرین تعامل | `/v1/tracks/completion/lastInteracted` | `trackId` |
| ETA | `/v1/tracks/{trackId}/eta` | `trackId` |

## ۲. قرارداد پیشرفت (پیشنهاد مبتنی بر شواهد)

```json
{ "lessonId": 67389, "tutorialId": 1001, "chapterId": 42, "state": "completed",
  "tutorialVersion": 3, "publishSetVersion": 753, "completedAt": "…", "attempts": 2 }
```
`state ∈ {unstarted, in_progress, completed, mastered}` — `mastered` از `SmartPracticeMastered`
استنباط شد (LOW).

## ۳. قواعد محاسبه

| سنجه | قاعدهٔ استنباطی |
|---|---|
| درصد مسیر | `startIndex` بخش جاری / کل آموزش‌ها |
| پایان فصل | همهٔ درس‌های فصل `completed` |
| پایان آموزش | همهٔ فصل‌ها پایان‌یافته |
| «درس بعدی» | اولین درس ناتمام به ترتیب گراف |
| ETA | میانگین زمان درس × درس‌های باقی‌مانده (سرور) |

## ۴. همگام‌سازی (شاهد: outbox)

`/v1/tutorials/{tutorialId}/progress` (POST) + صف آفلاین با حذف پس از موفقیت.
جزئیات در `11_LOCAL_DATA/SYNC_CONFLICTS.md`.

## ۵. کمبودها

| کمبود | اثر برای کنکور |
|---|---|
| پیشرفت «درصد» است، نه «تسلط» | نمی‌توان گفت «چقدر مسلط» |
| زمان صرف‌شده ثبت می‌شود؟ **UNKNOWN** | تحلیل زمان ممکن نیست |
| پیشرفت مستقل از نسخهٔ سؤال | کلید پاسخ تغییر کند ⇒ آمار آلوده |
