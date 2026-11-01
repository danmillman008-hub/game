# Mission 7 — Push Notifications

## Stack (VERIFIED_STATIC)
- Firebase Cloud Messaging: `com.google.firebase.messaging.*` decompiled; a `FirebaseMessagingService` subclass is
  registered in the manifest.
- Token registration: `com.getmimo.analytics.a` calls `FirebaseMessaging.c().f()` (get token) and stores it.

## Deep links
Notification payload → `MainActivity` intent (the single deep-link entry). The route grammar is not recovered
(`Q-109`), so notification→screen mapping is UNKNOWN.

## Permissions
`POST_NOTIFICATIONS` is among the 24 manifest permissions (targetSdk 36 ⇒ runtime permission), but no permission
request flow was recovered in the inspected subset.

## What is not claimed
Notification content, scheduling, local notifications, or channel configuration — none recovered.
