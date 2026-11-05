MISSION 04 - LOGS (reproducible runtime evidence)
Reference run: 41998643355 | commit 92e87fe8d061ea4c11089f40a7c8ce73d34d816a
Branch: arena/aebb90b7-game | Emulator: API 36 / Android 16 / pixel_7 / google_apis / x86_64

CURRENT RUN
  APK_TRANSFER.txt          transfer method results, part sizes/SHAs, SHA_MATCH_OK
  apk_download.txt          preverified_by_transfer_step=yes (second SHA gate)
  LOGCAT_MIMO.txt           logcat filtered to the Mimo process (pid 4266)
  ANR_DISMISSAL.txt         anr_dialog_attempt_1 none; focus = IntroSlidesActivity
  UI_HIERARCHY_CHECK.txt    mimo_nodes_in_ui_hierarchy=true, 15 com.getmimo nodes
  SCREENSHOT_INFO.txt       PNG byte counts
  EMULATOR_FAILURE_EXCERPT.txt  historical E2B 403 diagnostics (run 41994008902)

ARCHIVED RUN-BY-RUN (do not confuse with the reference run)
  APK_TRANSFER_RUN_41996366953.txt / _41997137033.txt / _41997975847.txt
  APPLICATION_LAUNCH_RUN_41996366953.txt / _41997137033.txt / _41997975847.txt
  UI_HIERARCHY_RUN_41996366953.xml / _RUN_41997137033.xml
  SCREENSHOT_RUN_41997137033_ANR_OVERLAY.png

No access token, signed URL or credential is printed in any log; URL values were
redacted by transfer_apk.sh and the endpoint config file was deleted in-run.
