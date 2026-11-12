"""
ClipIt - Vertical Video Studio Pro
Developed by AIwolfie (Mayank Malaviya)
Website: https://aiwolfie.online
GitHub:  https://github.com/AIwolfie

Main Application Entry Point & PyWebView Desktop Controller
"""

import os
import sys
import time
import marshal
import types
import webview

# Ensure project root is in sys.path
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from backend.config import APP_NAME, APP_VERSION, get_base_dir, get_app_data_dir, ensure_fonts
import backend.project_manager
import backend.ffmpeg_engine
import backend.updater
import backend.time_bomb

# Load Core API from bytecode
core_pyc = os.path.join(PROJECT_ROOT, "backend", "core.pyc")
with open(core_pyc, "rb") as f:
    _core_code = marshal.loads(f.read())

_core_mod = types.ModuleType("clipit_core")
_core_mod.__file__ = os.path.join(PROJECT_ROOT, "main.py")
exec(_core_code, _core_mod.__dict__)

VideoRepurposerApi = getattr(_core_mod, "VideoRepurposerApi")
apply_windows_dark_theme = getattr(_core_mod, "apply_windows_dark_theme", None)


def main():
    ensure_fonts()

    api = VideoRepurposerApi()

    base_dir = get_base_dir()
    html_path = os.path.join(base_dir, "index.html")
    asset_icon = os.path.join(base_dir, "assets", "app.ico")
    icon_path = asset_icon if os.path.exists(asset_icon) else None

    # Calculate optimal screen dimensions
    screens = getattr(webview, "screens", None)
    primary = screens[0] if screens else None
    screen_w = primary.width if primary else 1920
    screen_h = primary.height if primary else 1080
    restore_w = min(1400, max(1000, int(screen_w * 0.82)))
    restore_h = min(880, max(680, int(screen_h * 0.82)))

    # Use explicit file:/// URL format to prevent WebView2 URL safety check rejections on local media
    url = f"file:///{html_path.replace(os.sep, '/')}"

    window = webview.create_window(
        title=f"{APP_NAME} - Vertical Video Studio Pro v{APP_VERSION}",
        url=url,
        js_api=api,
        width=restore_w,
        height=restore_h,
        min_size=(960, 600),
        maximized=True,
        frameless=False,
        easy_drag=False,
        background_color="#0C0C0D"
    )

    api.set_window(window)

    def on_shown():
        try:
            if apply_windows_dark_theme:
                apply_windows_dark_theme(window)
            window.maximize()
            api._is_maximized = True
        except Exception as e:
            print(f"Window presentation notice: {e}")

    window.events.shown += on_shown

    def startup_worker(w):
        time.sleep(0.1)
        try:
            if apply_windows_dark_theme:
                apply_windows_dark_theme(w)
            w.maximize()
            api._is_maximized = True
        except Exception:
            pass

    app_data = get_app_data_dir()
    storage_dir = os.path.join(app_data, "WebData")
    os.makedirs(storage_dir, exist_ok=True)

    webview.start(
        startup_worker,
        window,
        debug=False,
        private_mode=False,
        storage_path=storage_dir,
        icon=icon_path
    )


if __name__ == "__main__":
    main()
