MIMO MISSION 03 - UI_HIERARCHY/ DIRECTORY NOTE
=============================================
Run ID: 41950695024 (and 41950152436)
Timestamp UTC: 2026-11-05T01:49:09Z
Device: API 36 / Android 16 / pixel_7 / google_apis / x86_64 / headless
APK SHA expected: 48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a

STATUS: NO XML HIERARCHY FILE WAS PRODUCED. This directory is intentionally
empty of XML; this note is the record of that fact.

Exact observed command and result (see ../LOGS/uiautomator_000.txt):

  adb shell uiautomator dump --compressed /sdcard/window.xml
  -> ERROR: null root node returned by UiTestAutomationBridge.
  -> uiautomator_exit=0
  adb pull /sdcard/window.xml
  -> adb: error: failed to stat remote object '/sdcard/window.xml':
     No such file or directory
  -> uiautomator_pull_exit=1

IMPORTANT DISTINCTION (do not conflate):
1. The failure above is a SYSTEM-LEVEL UiTestAutomationBridge failure on the
   booted Android 16 emulator (NexusLauncherActivity was resumed and Awake).
2. The well-known limitation that Jetpack Compose components are not exposed
   by uiautomator dump was NOT tested in this mission, because the Mimo APK
   was never installed and no Compose screen was ever launched. That
   limitation therefore remains UNKNOWN, not OBSERVED, here.

Screenshots are preserved as the primary visual evidence:
  ../SCREENSHOTS/TEST-000_emulator_home.png (408735 bytes, real Pixel launcher)
The earlier run 41950152436 produced a uniformly blank framebuffer (15584
bytes) before the device was woken/unlocked; that is recorded separately.

No com.getmimo process existed on the device. No application UI, no Learning
Path nodes, no lesson screens and no in-app interactions were observed.
Everything about the Mimo UI remains UNKNOWN.
