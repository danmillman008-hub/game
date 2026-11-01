# ۱۰ — کاتالوگ API (بازسازی‌شده از annotationها)

**منبع:** ۶۲ annotation مسیر + ۲۱ literal بدون annotation. تولید خودکار از `API_ENDPOINTS.json`.

**اهمیت:** این جدول، نخستین بازسازی *معتبر* سطح HTTP در این پروژه است؛ گزارش قبلی این بخش را
«غیرقابل استخراج» اعلام کرده بود که **رد شد** (نگاه کنید به `VERB_MAPPING.md`).

ستون «فعل» از نقشهٔ annotation مشتق شده؛ ستون اطمینان صادقانه است: MEDIUM یعنی فعل از نام متد
استنتاج شده، نه از annotation مستقیم.

## v1/user  (19 مسیر)

| مسیر | فعل | اطمینان | مالک (کلاس/متد) | annotation |
|---|---|---|---|---|
| `/v1/user/activity` | GET | HIGH | `Lsh/h;->a(Ljava/lang/String; Ljava/lang/String; Ld70/b;)` | `Lie0/f;` |
| `/v1/user/coins` | GET | HIGH | `Lqg/a;->a(Ld70/b;)` | `Lie0/f;` |
| `/v1/user/deviceTokens` | POST | MEDIUM | `Lhg/a;->c(Lcom/getmimo/data/model/analytics/DeviceToken; Ld70/b;)` | `Lie0/o;` |
| `/v1/user/events/subscribe` | GET | HIGH | `Lhg/a;->b(Ld70/b;)` | `Lie0/f;` |
| `/v1/user/favorites/tracks` | GET | HIGH | `Lxe/a;->a(Ld70/b;)` | `Lie0/f;` |
| `/v1/user/favorites/tracks/{trackId}` | DELETE | HIGH | `Lxe/a;->c(J Ld70/b;)` | `Lie0/b;` |
| `/v1/user/favorites/tracks/{trackId}` | POST | MEDIUM | `Lxe/a;->b(J Ld70/b;)` | `Lie0/o;` |
| `/v1/user/following/{userId}` | DELETE | HIGH | `Lih/a;->a(J Ld70/b;)` | `Lie0/b;` |
| `/v1/user/following/{userId}` | DELETE | HIGH | `Lih/a;->f(J Ld70/b;)` | `Lie0/p;` |
| `/v1/user/invitations` | GET | HIGH | `Lug/a;->a(Ld70/b;)` | `Lie0/f;` |
| `/v1/user/keys` | GET | HIGH | `Lbh/a;->b(Ljava/lang/String; Ld70/b;)` | `Lie0/f;` |
| `/v1/user/keys/consume` | POST | MEDIUM | `Lbh/a;->a(Ld70/b;)` | `Lie0/o;` |
| `/v1/user/rewards/next` | GET | HIGH | `Llh/a;->b(Ld70/b;)` | `Lie0/f;` |
| `/v1/user/rewards/{rewardId}/confirm` | POST | MEDIUM | `Llh/a;->a(J Ld70/b;)` | `Lie0/o;` |
| `/v1/user/settings` | GET | HIGH | `Lkf/a;->c(Ld70/b;)` | `Lie0/f;` |
| `/v1/user/settings` | PUT | LOW | `Lkf/a;->a(Lcom/getmimo/data/settings/model/Settings; Ld70/b;)` | `Lie0/n;` |
| `/v1/user/settings/avatar` | POST | MEDIUM | `Lkf/a;->e(Ld70/b;)` | `Lie0/o;` |
| `/v1/user/settings/avatar/{uploadId}` | DELETE | HIGH | `Lkf/a;->d(Ljava/lang/String; Lcom/getmimo/data/settings/model/ConfirmA` | `Lie0/p;` |
| `/v1/user/visits` | POST | MEDIUM | `Lhg/a;->a(Lcom/getmimo/data/model/AppName; Ld70/b;)` | `Lie0/o;` |

## v1/tracks  (7 مسیر)

| مسیر | فعل | اطمینان | مالک (کلاس/متد) | annotation |
|---|---|---|---|---|
| `/v1/tracks/completion/lastInteracted` | GET | HIGH | `Lcom/getmimo/data/source/remote/progress/CompletionApi;->getLastIntera` | `Lie0/f;` |
| `/v1/tracks/{trackId}/certificates` | GET | HIGH | `Log/a;->b(J Ljava/lang/String; J Ld70/b;)` | `Lie0/f;` |
| `/v1/tracks/{trackId}/completion` | GET | HIGH | `Lcom/getmimo/data/source/remote/progress/CompletionApi;->getTrackCompl` | `Lie0/f;` |
| `/v1/tracks/{trackId}/eta` | GET | HIGH | `Lcom/getmimo/data/source/remote/progress/TrackEtaApi;->getTrackEta(J J` | `Lie0/f;` |
| `/v1/tracks/{trackId}/tutorials/{tutorialId}/chapters/{chapterId}/lessons/{lessonId}/runFiles` | POST | MEDIUM | `Lhg/c;->b(J J J J J Z Ljava/lang/String; Lcom/getmimo/core/model/lesso` | `Lie0/o;` |
| `/v1/tracks/{trackId}/tutorials/{tutorialId}/chapters/{chapterId}/lessons/{lessonId}/savefiles` | POST | MEDIUM | `Ldh/a;->b(J J J J J Lcom/getmimo/data/model/lesson/SaveLessonFilesBody` | `Lie0/o;` |
| `/v1/tracks/{trackId}/tutorials/{tutorialId}/chapters/{chapterId}/savedFiles` | GET | HIGH | `Ldh/a;->a(J J J J Ld70/b;)` | `Lie0/f;` |

## v1/tutorials  (3 مسیر)

| مسیر | فعل | اطمینان | مالک (کلاس/متد) | annotation |
|---|---|---|---|---|
| `/v1/tutorials/drafts/{tutorialId}/chapters/{chapterId}/lessons/{lessonId}/render` | GET | HIGH | `Lng/a;->a(J J J Ld70/b;)` | `Lie0/f;` |
| `/v1/tutorials/{tutorialId}/lessons/{lessonIdentityId}/report` | POST | MEDIUM | `Lkh/a;->a(J J Lcom/getmimo/core/model/lesson/report/ReportLessonBody; ` | `Lie0/o;` |
| `/v1/tutorials/{tutorialId}/progress` | POST | MEDIUM | `Lcom/getmimo/data/source/remote/progress/LessonProgressApi;->postProgr` | `Lie0/o;` |

## v1/leaderboards  (3 مسیر)

| مسیر | فعل | اطمینان | مالک (کلاس/متد) | annotation |
|---|---|---|---|---|
| `/v1/leaderboards/friends` | GET | HIGH | `Lug/a;->c(Ld70/b;)` | `Lie0/f;` |
| `/v1/leaderboards/latest` | GET | HIGH | `Lch/a;->a(Ld70/b;)` | `Lie0/f;` |
| `/v1/leaderboards/{leaderboardId}/userrank` | GET | HIGH | `Lch/a;->b(J Ld70/b;)` | `Lie0/f;` |

## v1/preview  (1 مسیر)

| مسیر | فعل | اطمینان | مالک (کلاس/متد) | annotation |
|---|---|---|---|---|
| `/v1/preview/tracks/{trackId}/tutorials/{tutorialId}/chapters/{chapterId}/lessons/{lessonId}/runFiles` | POST | MEDIUM | `Lhg/c;->a(J J J J J Lcom/getmimo/core/model/lesson/executablefiles/Exe` | `Lie0/o;` |

## v1/code  (7 مسیر)

| مسیر | فعل | اطمینان | مالک (کلاس/متد) | annotation |
|---|---|---|---|---|
| `/v1/code` | GET | HIGH | `Lmh/c;->c(Ld70/b;)` | `Lie0/f;` |
| `/v1/code` | POST | MEDIUM | `Lmh/c;->d(Lcom/getmimo/data/model/savedcode/SaveCodeRequestBody; Ld70/` | `Lie0/o;` |
| `/v1/code/runfiles` | POST | MEDIUM | `Lhg/c;->c(Lcom/getmimo/data/model/codeexecution/CodePlaygroundExecutio` | `Lie0/o;` |
| `/v1/code/{savedCodeId}` | DELETE | HIGH | `Lmh/c;->e(J Ld70/b;)` | `Lie0/b;` |
| `/v1/code/{savedCodeId}` | PUT | LOW | `Lmh/c;->a(J Lcom/getmimo/data/model/savedcode/SaveCodeRequestBody; Ld7` | `Lie0/n;` |
| `/v1/code/{savedCodeId}/remixes` | POST | MEDIUM | `Lmh/c;->b(J Lcom/getmimo/data/model/savedcode/RemixCodeRequestBody; Ld` | `Lie0/o;` |
| `/v1/code/{savedCodeId}/runfiles` | POST | MEDIUM | `Lhg/c;->d(J Lcom/getmimo/data/model/codeexecution/CodePlaygroundExecut` | `Lie0/o;` |

## v1/products  (2 مسیر)

| مسیر | فعل | اطمینان | مالک (کلاس/متد) | annotation |
|---|---|---|---|---|
| `/v1/products/user` | GET | HIGH | `Lnh/c;->b(Ld70/b;)` | `Lie0/f;` |
| `/v1/products/user` | POST | MEDIUM | `Lnh/c;->a(Ljava/lang/String; Lcom/getmimo/data/model/store/ProductType` | `Lie0/o;` |

## v1/practice  (1 مسیر)

| مسیر | فعل | اطمینان | مالک (کلاس/متد) | annotation |
|---|---|---|---|---|
| `/v1/practice/statistics` | GET | HIGH | `Lhh/a;->a(Ld70/b;)` | `Lie0/f;` |

## v1/account  (2 مسیر)

| مسیر | فعل | اطمینان | مالک (کلاس/متد) | annotation |
|---|---|---|---|---|
| `/v1/account` | DELETE | HIGH | `Lhg/a;->e(Ljava/lang/String; Ld70/b;)` | `Lie0/b;` |
| `/v1/account/email` | PUT | LOW | `Lhg/a;->d(Lcom/getmimo/data/model/account/ChangeEmailRequestBody; Ld70` | `Lie0/n;` |

## v1/users  (4 مسیر)

| مسیر | فعل | اطمینان | مالک (کلاس/متد) | annotation |
|---|---|---|---|---|
| `/v1/users/{userId}/code` | GET | HIGH | `Lih/a;->b(J Ld70/b;)` | `Lie0/f;` |
| `/v1/users/{userId}/code/{savedCodeId}` | GET | HIGH | `Lih/a;->c(J J Ld70/b;)` | `Lie0/f;` |
| `/v1/users/{userId}/profile` | GET | HIGH | `Lih/a;->d(J Ld70/b;)` | `Lie0/f;` |
| `/v1/users/{userId}/report` | POST | MEDIUM | `Lih/a;->e(J Ld70/b;)` | `Lie0/o;` |

## v2  (1 مسیر)

| مسیر | فعل | اطمینان | مالک (کلاس/متد) | annotation |
|---|---|---|---|---|
| `/v2/client-config` | GET | HIGH | `Llg/a;->a(Ld70/b;)` | `Lie0/f;` |

## api  (7 مسیر)

| مسیر | فعل | اطمینان | مالک (کلاس/متد) | annotation |
|---|---|---|---|---|
| `/api/sendCustomerIoData` | POST | MEDIUM | `Lhg/b;->a(Lcom/getmimo/data/model/customerio/CustomerIoData; Ld70/b;)` | `Lie0/o;` |
| `/api/v1/branding` | GET | HIGH | `Lio/customer/messaginginapp/inbox/data/InboxService;->fetchBranding(Ld` | `Lie0/f;` |
| `/api/v1/logs/message/{messageId}` | POST | MEDIUM | `Lio/customer/messaginginapp/gist/data/listeners/GistQueueService;->log` | `Lie0/o;` |
| `/api/v1/logs/queue/{queueId}` | POST | MEDIUM | `Lio/customer/messaginginapp/gist/data/listeners/GistQueueService;->log` | `Lie0/o;` |
| `/api/v1/messages/{queueId}` | PUT | LOW | `Lio/customer/messaginginapp/gist/data/listeners/GistQueueService;->log` | `Lie0/n;` |
| `/api/v1/templates` | GET | HIGH | `Lio/customer/messaginginapp/inbox/data/InboxService;->fetchTemplates(L` | `Lie0/f;` |
| `/api/v4/users` | POST | MEDIUM | `Lio/customer/messaginginapp/gist/data/listeners/GistQueueService;->fet` | `Lie0/o;` |

## click  (1 مسیر)

| مسیر | فعل | اطمینان | مالک (کلاس/متد) | annotation |
|---|---|---|---|---|
| `/click/{linkId}` | POST | MEDIUM | `Lph/b;->a(Ljava/lang/String; Ld70/b;)` | `Lie0/o;` |

## push  (1 مسیر)

| مسیر | فعل | اطمینان | مالک (کلاس/متد) | annotation |
|---|---|---|---|---|
| `/push/events` | POST | MEDIUM | `Lhg/d;->a(Lcom/getmimo/data/model/analytics/PushNotificationDelivered;` | `Lie0/o;` |

## v1/aiTutor  (1 مسیر)

| مسیر | فعل | اطمینان | مالک (کلاس/متد) | annotation |
|---|---|---|---|---|
| `/v1/aiTutor/conversations/messages/count` | GET | HIGH | `Ljg/a;->a(Ld70/b;)` | `Lie0/f;` |

## v1/invitations  (1 مسیر)

| مسیر | فعل | اطمینان | مالک (کلاس/متد) | annotation |
|---|---|---|---|---|
| `/v1/invitations/{code}` | POST | MEDIUM | `Lug/a;->d(Ljava/lang/String; Ld70/b;)` | `Lie0/o;` |

## v1/package  (1 مسیر)

| مسیر | فعل | اطمینان | مالک (کلاس/متد) | annotation |
|---|---|---|---|---|
| `/v1/package/preview` | GET | HIGH | `Leh/a;->a(Ld70/b;)` | `Lie0/f;` |

## مسیرهای بدون annotation (۲۱ مورد)

| مسیر | تفسیر | شاهد |
|---|---|---|
| `/auth/login` | Firebase Auth REST | رشتهٔ ثابت در DEX |
| `/auth/revoke` | خروج | رشتهٔ ثابت در DEX |
| `/auth/token` | refresh token | رشتهٔ ثابت در DEX |
| `/authTokens:generate` | سرویس توکن | رشتهٔ ثابت در DEX |
| `/me/` | Customer.io identify | رشتهٔ ثابت در DEX |
| `/measurement_consent` | RevenueCat consent | رشتهٔ ثابت در DEX |
| `/tracks` | RevenueCat offerings/پکیج | رشتهٔ ثابت در DEX |
| `/tracks.json` | ? | رشتهٔ ثابت در DEX |
| `/v1/aiTutor/conversations` | مربی هوشمند | رشتهٔ ثابت در DEX |
| `/v1/aiTutor/conversations/` | ادامهٔ گفتگو | رشتهٔ ثابت در DEX |
| `/v1/customercenter/support/create-ticket` | پشتیبانی | رشتهٔ ثابت در DEX |
| `/v1/diagnostics` | تشخیص | رشتهٔ ثابت در DEX |
| `/v1/events` | تحلیل (Segment) | رشتهٔ ثابت در DEX |
| `/v1/health/connectivity` | سلامت شبکه | رشتهٔ ثابت در DEX |
| `/v1/offerings` | RevenueCat | رشتهٔ ثابت در DEX |
| `/v1/product_entitlement_mapping` | RevenueCat | رشتهٔ ثابت در DEX |
| `/v1/receipts` | رسید خرید | رشتهٔ ثابت در DEX |
| `/v1/subscribers/identify` | RevenueCat identify | رشتهٔ ثابت در DEX |
| `/v1/subscribers/redeem_purchase` | RevenueCat redeem | رشتهٔ ثابت در DEX |
| `/v1/tracks/` | ? | رشتهٔ ثابت در DEX |
| `/v2/purchase` | خرید نسخهٔ ۲ | رشتهٔ ثابت در DEX |