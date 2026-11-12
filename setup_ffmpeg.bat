@echo off
:: =========================================================================
:: ClipIt - FFmpeg Auto-Setup Utility
:: Developed by AIwolfie (Mayank Malaviya)
:: Website: https://aiwolfie.online | GitHub: https://github.com/AIwolfie
:: =========================================================================
title ClipIt - FFmpeg Setup Utility
cd /d "%~dp0"

echo [1/3] Checking existing FFmpeg binaries...
if exist "ffmpeg.exe" (
    if exist "ffprobe.exe" (
        echo [OK] ffmpeg.exe and ffprobe.exe are already present in project root.
        pause
        exit /b 0
    )
)

echo [2/3] Downloading official FFmpeg build (Gyan.dev Essentials)...
set "ZIP_URL=https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip"
set "TEMP_ZIP=%TEMP%\ffmpeg_clipit.zip"
set "EXTRACT_DIR=%TEMP%\ffmpeg_clipit_extract"

curl.exe -L "%ZIP_URL%" -o "%TEMP_ZIP%" --progress-bar
if %ERRORLEVEL% neq 0 (
    echo [ERROR] Failed to download FFmpeg. Please check your internet connection or install FFmpeg manually.
    pause
    exit /b 1
)

echo [3/3] Extracting binaries...
if exist "%EXTRACT_DIR%" rmdir /s /q "%EXTRACT_DIR%"
mkdir "%EXTRACT_DIR%"
tar.exe -xf "%TEMP_ZIP%" -C "%EXTRACT_DIR%"

for /r "%EXTRACT_DIR%" %%f in (ffmpeg.exe ffprobe.exe) do (
    copy /y "%%f" "%~dp0" >nul
)

del /f /q "%TEMP_ZIP%" >nul 2>&1
rmdir /s /q "%EXTRACT_DIR%" >nul 2>&1

if exist "ffmpeg.exe" (
    echo [SUCCESS] FFmpeg successfully installed into ClipIt Studio.
) else (
    echo [WARNING] Extraction failed. Please download ffmpeg.exe manually and place in project root.
)

pause
