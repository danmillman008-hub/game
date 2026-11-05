MISSION 04 - UI HIERARCHY (original XML dumps)
Reference run: 41998643355 | commit 92e87fe8d061ea4c11089f40a7c8ce73d34d816a
Branch: arena/aebb90b7-game | Emulator: API 36 / Android 16 / pixel_7 / google_apis / x86_64
Files here are the UNEDITED output of `adb shell uiautomator dump` + `adb pull`.
No hierarchy file was synthesised, edited or invented.

TEST-000_emulator_home.xml            launcher nodes (com.google.android.apps.nexuslauncher)
TEST-003_initial_screen.xml           ORIGINAL XML of the real Mimo screen
                                      (15 nodes with package="com.getmimo")
UI_HIERARCHY_RUN_41996366953.xml      historical: launcher-only, rejected
UI_HIERARCHY_RUN_41997137033.xml      historical: ANR dialog only (4 android nodes), rejected

LOGS/UI_HIERARCHY_CHECK.txt records the final check:
  mimo_nodes_in_ui_hierarchy=true
  15 package="com.getmimo"
