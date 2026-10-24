"""
Prototipe Sistem Informasi Departemen Teknik JDC — versi Streamlit.

Aplikasi ini menampilkan prototipe HTML (prototipe.html) secara utuh di dalam
Streamlit sehingga dapat di-deploy ke Streamlit Community Cloud dan diakses
oleh pihak lain melalui tautan publik.
"""
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="SI Teknik JDC — Prototipe",
    page_icon="🛠️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Sembunyikan elemen bawaan Streamlit dan buat prototipe memenuhi layar.
st.markdown(
    """
    <style>
      #MainMenu, header[data-testid="stHeader"], footer,
      [data-testid="stToolbar"], [data-testid="stDecoration"],
      [data-testid="stStatusWidget"], [data-testid="collapsedControl"] {
          display: none !important;
      }
      .stApp, .main, .block-container,
      [data-testid="stAppViewContainer"], [data-testid="stMain"],
      [data-testid="stMainBlockContainer"] {
          padding: 0 !important;
          margin: 0 !important;
          max-width: 100% !important;
      }
      [data-testid="stVerticalBlock"] { gap: 0 !important; }
      iframe {
          display: block;
          width: 100% !important;
          height: 100vh !important;
          border: none;
      }
    </style>
    """,
    unsafe_allow_html=True,
)

HTML_FILE = Path(__file__).parent / "prototipe.html"


@st.cache_data(show_spinner=False)
def load_prototype(path: str) -> str:
    return Path(path).read_text(encoding="utf-8")


components.html(load_prototype(str(HTML_FILE)), height=900, scrolling=True)
