"""
Frontend configuration — API base URL and refresh settings.
"""
import os

import streamlit as st

def get_config(key: str, default: str) -> str:
    """Fetch from st.secrets first, then os.getenv."""
    try:
        if key in st.secrets:
            return st.secrets[key]
    except Exception:
        pass
    return os.getenv(key, default)

BACKEND_URL: str = get_config("BACKEND_URL", "http://localhost:8000")
DEFAULT_REFRESH_SECONDS: int = int(get_config("DEFAULT_REFRESH_SECONDS", "60"))

REFRESH_OPTIONS = {
    "30 seconds": 30,
    "60 seconds": 60,
    "5 minutes": 300,
}
