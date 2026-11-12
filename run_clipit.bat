@echo off
:: =========================================================================
:: ClipIt - Vertical Video Studio Pro
:: Developed by AIwolfie (Mayank Malaviya)
:: Website: https://aiwolfie.online | GitHub: https://github.com/AIwolfie
:: =========================================================================
title ClipIt - Vertical Video Studio Pro
cd /d "%~dp0"
set PYTHONUTF8=1
set PYTHONIOENCODING=utf-8

where python >nul 2>nul
if %ERRORLEVEL% neq 0 (
    echo [ERROR] Python is not found in PATH.
    echo Please ensure Python 3.10+ is installed and added to your PATH environment variable.
    pause
    exit /b 1
)

if not exist "ffmpeg.exe" (
    where ffmpeg >nul 2>nul
    if %ERRORLEVEL% neq 0 (
        echo [INFO] FFmpeg binary not found in root or system PATH.
        echo Launching automatic setup utility...
        call setup_ffmpeg.bat
    )
)

echo Starting ClipIt Studio Pro...
python main.py

if %ERRORLEVEL% neq 0 (
    echo.
    echo [NOTICE] Application closed with return code %ERRORLEVEL%.
    pause
)
