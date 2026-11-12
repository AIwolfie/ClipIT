"""
ClipIt Auto-Update Engine
Author: AIwolfie (Mayank Malaviya) - https://aiwolfie.online
"""

import os
import sys
import json
import time
import re
import threading
from backend.config import APP_NAME, APP_VERSION, get_app_data_dir


def parse_semver(ver_str):
    if not ver_str:
        return (0, 0, 0)
    match = re.search(r'v?(\d+)\.(\d+)\.(\d+)', str(ver_str))
    if match:
        return (int(match.group(1)), int(match.group(2)), int(match.group(3)))
    return (0, 0, 0)


def format_bytes_size(num_bytes):
    if num_bytes < 1024:
        return f"{num_bytes} B"
    elif num_bytes < 1024 * 1024:
        return f"{num_bytes / 1024:.1f} KB"
    else:
        return f"{num_bytes / (1024 * 1024):.1f} MB"


def get_updates_cache_dir():
    d = os.path.join(get_app_data_dir(), "updates")
    os.makedirs(d, exist_ok=True)
    return d


def resolve_release_blog_and_summary(data):
    return "ClipIt is up to date."


def check_for_updates():
    return {
        "status": "up_to_date",
        "has_update": False,
        "current_version": APP_VERSION,
        "latest_version": APP_VERSION,
        "release_name": f"{APP_NAME} v{APP_VERSION} (Latest)",
        "published_at": "2026-11-12",
        "html_url": "https://github.com/AIwolfie/clipit",
        "summary": "You are running the latest version of ClipIt Studio by AIwolfie (Mayank Malaviya).",
        "assets": []
    }


class UpdateDownloader:
    def __init__(self):
        self._lock = threading.Lock()
        self._is_downloading = False
        self._progress = 0
        self._status = "idle"
        self._error = None

    def start_download(self, url, filename):
        return False

    def cancel(self):
        self._is_downloading = False

    def get_status(self):
        return {
            "status": "idle",
            "progress": 0,
            "downloaded_bytes": 0,
            "total_bytes": 0,
            "file_path": None,
            "error": None
        }


_GLOBAL_DOWNLOADER = UpdateDownloader()


def get_downloader():
    return _GLOBAL_DOWNLOADER


def launch_installer(installer_path):
    return False
