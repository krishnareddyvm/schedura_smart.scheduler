import os
from functools import lru_cache

import streamlit as st


@lru_cache(maxsize=1)
def _load_css_content() -> str:
    """Load the shared theme stylesheet once."""
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    css_path = os.path.join(base_dir, "assets", "theme.css")
    if os.path.exists(css_path):
        with open(css_path, "r", encoding="utf-8") as css_file:
            return css_file.read()
    return ""


def inject_custom_css() -> None:
    """Inject the shared CSS into the current Streamlit page."""
    css = _load_css_content()
    if css:
        st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)
