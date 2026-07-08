# ══════════════════════════════════════════════════════════════
# PRICE & PROMOTIONS RCA TOOL — Streamlit frontend (Databricks Apps)
# ------------------------------------------------------------------
# Rendering strategy:
#   Native Streamlit widgets (st.metric / st.dataframe / st.columns)
#   can't reach the polished enterprise look in the reference design,
#   so the entire UI is authored as semantic HTML + a single CSS
#   stylesheet and rendered through one full-fidelity surface.
#   Python stays clean: data.py holds data, components.py builds markup.
# ══════════════════════════════════════════════════════════════

from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

import data
import components as ui

# ─────────────────────────────────────────────────────────────
# PAGE CONFIG
# ─────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Price & Promotion RCA Tool",
    page_icon="🔷",
    layout="wide",
    initial_sidebar_state="collapsed",
)

BASE_DIR = Path(__file__).parent
FONT_LINK = (
    '<link rel="preconnect" href="https://fonts.googleapis.com">'
    '<link href="https://fonts.googleapis.com/css2?'
    'family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">'
)


# ─────────────────────────────────────────────────────────────
# CSS — injected once at startup
# ─────────────────────────────────────────────────────────────
def load_css() -> str:
    """Read the external stylesheet (single source of truth for styling)."""
    return (BASE_DIR / "style.css").read_text(encoding="utf-8")


def inject_css(css: str) -> None:
    """Apply CSS to the parent Streamlit document (hides default chrome)."""
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────
# PAGE ASSEMBLY
# ─────────────────────────────────────────────────────────────
def build_body() -> str:
    """Compose the full page from reusable component functions."""
    return f"""
    <div class="ppr-app">
      {ui.render_nav()}
      {ui.render_pagehead()}
      {ui.render_kpi_cards(data.get_kpis())}
      {ui.render_articles_table(data.get_articles(), data.get_pagination())}
      <div class="section-gap"></div>
      {ui.render_investigation(data.get_investigation())}
    </div>"""


def render_app(css: str, body: str) -> None:
    """
    Render the assembled HTML inside a self-contained surface so the
    layout is identical to the design reference (no widget interference).
    """
    document = f"""<!DOCTYPE html><html lang="en"><head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      {FONT_LINK}
      <style>
        html,body{{margin:0;padding:0;background:#F8FAFC;}}
        body{{padding:2px 2px 24px;}}
        {css}
      </style>
    </head><body>{body}</body></html>"""
    # Height fits the compact desktop layout; scrolling covers responsive stacking.
    components.html(document, height=1300, scrolling=True)


# ─────────────────────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────────────────────
def main() -> None:
    css = load_css()
    inject_css(css)          # strips Streamlit chrome on the parent doc
    render_app(css, build_body())


if __name__ == "__main__":
    main()
