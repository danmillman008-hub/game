MISSION 04 - SCREENSHOTS (real runtime evidence)
Reference run: 41998643355 | commit 92e87fe8d061ea4c11089f40a7c8ce73d34d816a
Branch: arena/aebb90b7-game | Emulator: API 36 / Android 16 / pixel_7 / google_apis / x86_64
All PNGs were captured by `adb exec-out screencap -p` on the SAME emulator
after the exact-SHA APK was installed and com.getmimo was launched.
Screenshot byte counts are recorded in LOGS/SCREENSHOT_INFO.txt.
The runner caps each PNG at 4 MB; no PNG in this set was truncated.

TEST-000_emulator_home.png         launcher after boot (context only, NOT Mimo evidence)
TEST-002_splash.png                34,635 B  - 3 s after `am start`
TEST-003_initial_screen.png       65,373 B  - first usable Mimo screen
TEST-004_first_usable_screen.png  65,373 B  - stable name, same frame (genuine Mimo UI)
SCREENSHOT_RUN_41997137033_ANR_OVERLAY.png - historical: system "Pixel Launcher
  isn't responding" dialog over dimmed Mimo onboarding; archived as a resolved
  automation failure, NOT accepted as Mimo UI evidence.

Final frame content (visual readback): onboarding carousel slide 3
"Change your career" / "Use your portfolio of projects to apply for a job and
change your career", purple "Get started" button, "I already have an account"
link, three page dots. No launcher, no system dialog.
A launcher-only screenshot is explicitly NOT Mimo evidence.
