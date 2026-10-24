@echo off
setlocal
chcp 65001 >nul
pushd "%~dp0"
title TTAC APK analyzer

set "APK=%~1"
if "%APK%"=="" set /p APK=Drag the TTAC .apk file here and press Enter: 
set "APK=%APK:"=%"

if not exist "%APK%" (
  echo.
  echo [X] APK not found: %APK%
  echo     Drag the .apk file onto this RUN-ME.bat, or pass its path.
  echo.
  pause
  exit /b 1
)

echo.
echo ==== [1/3] Node.js check ====
where node >nul 2>nul
if errorlevel 1 (
  echo [X] Node.js not found. Install the LTS version from https://nodejs.org then run this again.
  pause
  exit /b 1
)
node -v
echo OK

echo.
echo ==== [2/3] Extracting endpoints and API keys ====
node "%~dp0extract-apk.mjs" "%APK%"
if errorlevel 1 (
  echo [X] extraction failed
  pause
  exit /b 1
)

echo.
echo ==== [3/3] REA deep inspection (optional, may take a minute) ====
where npx >nul 2>nul
if errorlevel 1 (
  echo [i] npx not available - skipping REA
) else (
  call npx -y rea-agents@latest inspect-android-package "%APK%" > "REPORT-REA.txt" 2>"REA-errors.log"
  if exist "REPORT-REA.txt" (
    for %%A in ("REPORT-REA.txt") do if %%~zA GTR 0 (echo [OK] REPORT-REA.txt created) else (del "REPORT-REA.txt" & echo [i] REA produced no output - skipped)
  )
)

echo.
echo ================= DONE =================
if exist "REPORT-APK.txt" echo  1) REPORT-APK.txt   ^<- send this one
if exist "REPORT-REA.txt" echo  2) REPORT-REA.txt   ^<- send this too if it exists
echo =======================================
echo.
explorer "%~dp0"
pause
