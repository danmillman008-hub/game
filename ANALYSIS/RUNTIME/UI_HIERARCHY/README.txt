MIMO MISSION 03 - UI_HIERARCHY/ DIRECTORY NOTE
=============================================
Authoritative Run ID: 41951780483
Timestamp UTC: 2026-11-05T01:58:21Z
Device: API 36 / Android 16 / pixel_7 / google_apis / x86_64 / headless
APK SHA expected: 48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a

CONTENTS
--------
TEST-000_emulator_home.xml  (6661 bytes, 16 <node> elements)

This hierarchy was produced successfully in the authoritative run:

  adb shell uiautomator dump --compressed /sdcard/window.xml
  -> UI hierchary dumped to: /sdcard/window.xml
  -> uiautomator_exit=0
  adb pull /sdcard/window.xml
  -> /sdcard/window.xml: 1 file pulled, 0 skipped. 1.2 MB/s (6661 bytes ...)
  -> uiautomator_pull_exit=0

Observed content (parsed from the XML):
  root: <hierarchy rotation="0">, root bounds [0,0][1080,2400]
  all 16 nodes belong to package com.google.android.apps.nexuslauncher
  classes: TextView x7, FrameLayout x2, ImageView x2, ScrollView, ViewPager,
           ViewGroup, View, ImageButton
  visible texts: "Thu, Nov 5", "Gmail", "Photos", "YouTube", "Phone",
                 "Messages", "Chrome"

HISTORICAL FAILURES (do not conflate with the above)
---------------------------------------------------
In earlier runs 41950152436 and 41950695024 the same command failed with
"ERROR: null root node returned by UiTestAutomationBridge" and no XML was
produced. That was a transient SYSTEM-LEVEL UiTestAutomationBridge failure
before/around device wake-up, not a Compose limitation. Adding
`input keyevent 26 / 82 / 3` plus a 15 s wait fixed it.

IMPORTANT DISTINCTION
---------------------
1. The XML here is the SYSTEM PIXEL LAUNCHER hierarchy only. It contains
   NO com.getmimo node, NO Learning Path node, NO lesson screen, NO measured
   in-app geometry. It is RUNTIME VERIFIED evidence about the emulator's
   launcher, not about the Mimo application.
2. The known limitation that Jetpack Compose components are not exposed by
   `uiautomator dump` was NOT tested in this mission: the Mimo APK was never
   installed and no Compose screen was ever launched. That limitation remains
   UNKNOWN here; it must not be inferred from the transient system failures.

VISUAL EVIDENCE
---------------
../SCREENSHOTS/TEST-000_emulator_home.png (1370561 bytes, real Pixel launcher
with app icons). Run 41950152436 produced a uniformly blank framebuffer
(15584 bytes) before wake/unlock; both states are recorded.

No com.getmimo process ever existed on the device. TEST-001..009 remain
0/9 executed and 9/9 BLOCKED (see ../TEST_RESULTS.json).
