"""
ClipIt Backend Configuration & Paths
Created by AIwolfie (Mayank Malaviya) - https://aiwolfie.online
Cross-platform path resolution, constants, and resource initialization.
"""

import os
import sys

APP_NAME = "ClipIt"
APP_VERSION = "2.0.0"
AUTHOR = "AIwolfie (Mayank Malaviya)"
AUTHOR_WEBSITE = "https://aiwolfie.online"
GITHUB_REPO = "AIwolfie/clipit"
BETA_MODE = False
BETA_BUILD_DATE = "2026-11-12"
BETA_EXPIRY_DAYS = 99999
DUMMY_UPDATE_CHECK = True
ENABLE_DYNAMIC_UPDATES = False


def check_beta_status():
    return {
        "is_beta": False,
        "is_expired": False,
        "is_expiring_soon": False,
        "days_remaining": 99999,
        "expiry_date": "2099-12-31",
        "build_date": BETA_BUILD_DATE,
        "today": "2026-11-12",
        "tampered": False,
        "tamper_reason": None,
        "is_dev": True,
        "status": "valid",
        "message": "ClipIt Studio Pro Active · AIwolfie (Mayank Malaviya)"
    }


def get_base_dir():
    if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
        return sys._MEIPASS
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def get_app_data_dir():
    if sys.platform == "win32":
        base = os.environ.get("APPDATA", os.path.expanduser("~"))
        app_dir = os.path.join(base, APP_NAME)
    elif sys.platform == "darwin":
        app_dir = os.path.expanduser(f"~/Library/Application Support/{APP_NAME}")
    else:
        config_home = os.environ.get("XDG_CONFIG_HOME", os.path.expanduser("~/.config"))
        app_dir = os.path.join(config_home, APP_NAME.lower())
    os.makedirs(app_dir, exist_ok=True)
    return app_dir


def get_presets_file_path():
    return os.path.join(get_app_data_dir(), "presets.json")


def get_settings_path():
    return os.path.join(get_app_data_dir(), "settings.json")


def get_autosave_path():
    return os.path.join(get_app_data_dir(), "autosave.json")


def get_recent_projects_path():
    return os.path.join(get_app_data_dir(), "recent_projects.json")


def ensure_fonts():
    base_dir = get_base_dir()
    fonts_dir = os.path.join(base_dir, "fonts")
    if not os.path.exists(fonts_dir):
        return
    for font_file in os.listdir(fonts_dir):
        if font_file.lower().endswith((".ttf", ".otf")) and sys.platform == "win32":
            font_path = os.path.join(fonts_dir, font_file)
            try:
                import ctypes
                FR_PRIVATE = 16
                ctypes.windll.gdi32.AddFontResourceExW(font_path, FR_PRIVATE, 0)
            except Exception as e:
                print(f"Failed to register Windows font {font_file}: {e}")
