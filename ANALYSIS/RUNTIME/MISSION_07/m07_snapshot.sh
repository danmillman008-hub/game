#!/usr/bin/env bash
# usage: m07_snapshot.sh <LABEL>  — captures UI hierarchy, screenshot,
# consistent rooted SQLite backups, all private-state files, and a JSON
# row-level snapshot. Called once per comparable experiment state (A..I).
set +e
R=ANALYSIS/RUNTIME/MISSION_07
L="$1"
mkdir -p "$R/UI" "$R/DB/$L" "$R/EXPERIMENTS"
adb shell uiautomator dump /sdcard/m07_snap.xml </dev/null >/dev/null 2>&1
adb pull /sdcard/m07_snap.xml "$R/UI/$L.xml" </dev/null >/dev/null 2>&1
adb exec-out screencap -p > "$R/UI/$L.png" 2>/dev/null
{
  echo "MISSION 07 SNAPSHOT $L $(date -u +%FT%TZ)"
  echo "== focus =="; adb shell dumpsys window 2>/dev/null | tr -d '\r' | grep -m1 -i mCurrentFocus | sed 's/^ *//'
  echo "== resumed =="; adb shell dumpsys activity activities 2>/dev/null | tr -d '\r' | grep -m1 -iE 'topResumedActivity|mResumedActivity' | sed 's/^ *//'
  echo "== texts =="; grep -o 'text="[^"]*"' "$R/UI/$L.xml" 2>/dev/null | grep -v 'text=""' | sed 's/text=//' | tr '\n' '|' | cut -c1-1000; echo
  echo "== clickable =="; grep -o 'clickable="true"' "$R/UI/$L.xml" 2>/dev/null | wc -l
} > "$R/EXPERIMENTS/$L.state.txt"
# Full private tree listing (names + sizes), then bounded copy of selected dirs
adb shell 'find /data/data/com.getmimo -maxdepth 3 2>/dev/null | head -200' > "$R/DB/$L/DEVICE_TREE.txt" 2>&1
adb shell 'rm -rf /sdcard/m07_snap; mkdir -p /sdcard/m07_snap; for d in databases shared_prefs files/datastore no_backup; do if [ -e /data/data/com.getmimo/$d ]; then mkdir -p /sdcard/m07_snap/$(dirname $d); cp -a /data/data/com.getmimo/$d /sdcard/m07_snap/$d 2>/dev/null; fi; done' >/dev/null 2>&1
adb pull /sdcard/m07_snap "$R/DB/$L/private" </dev/null >/dev/null 2>&1
# Consistent SQLite .backup while app is live (root + device sqlite3)
for F in $(adb shell 'ls /data/data/com.getmimo/databases/' 2>/dev/null | tr -d '\r'); do
  case "$F" in *-wal|*-shm|*-journal) continue;; esac
  adb shell "sqlite3 /data/data/com.getmimo/databases/$F '.backup /sdcard/m07_consistent.db'" >/dev/null 2>&1
  adb pull /sdcard/m07_consistent.db "$R/DB/$L/consistent_$F" </dev/null >/dev/null 2>&1
  adb shell "sqlite3 /data/data/com.getmimo/databases/$F 'SELECT name FROM sqlite_master WHERE type=\"table\";'" >> "$R/DB/$L/DEVICE_TABLES.txt" 2>&1
done
python3 "$R/m07_db_snapshot.py" "$R/DB/$L" "SNAPSHOT_$L" "$R/DB/SNAPSHOT_$L.json" 2>&1 | tee -a "$R/LOGS/DB_SNAPSHOTS.txt"
