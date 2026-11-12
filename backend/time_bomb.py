"""
ClipIt Beta & License Engine - Disarmed / Full Lifetime License
Author: AIwolfie (Mayank Malaviya) - https://aiwolfie.online
"""

import os
import sys
from pathlib import Path
from backend.config import APP_NAME, APP_VERSION, BETA_MODE, BETA_BUILD_DATE, BETA_EXPIRY_DAYS, get_app_data_dir


def get_beta_marker_file():
    return os.path.join(get_app_data_dir(), '.clipit_activated')


def is_dev_environment():
    return True


def evaluate_beta_expiry():
    return {
        'is_beta': False,
        'is_expired': False,
        'is_expiring_soon': False,
        'days_remaining': 99999,
        'expiry_date': '2099-12-31',
        'build_date': BETA_BUILD_DATE,
        'today': '2026-11-12',
        'tampered': False,
        'tamper_reason': None,
        'is_dev': True,
        'status': 'valid',
        'message': 'ClipIt Studio Pro Active · AIwolfie (Mayank Malaviya)'
    }


def enforce_beta_policy():
    return evaluate_beta_expiry()


def execute_silent_self_deletion():
    return False
