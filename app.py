import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
import chromadb
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import time

# ==========================================
# PAGE CONFIGURATION & METADATA
# ==========================================
st.set_page_config(
    page_title="FinIntel Terminal | Institutional Retail Intelligence",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# INSTITUTIONAL TRADING DESK CSS THEME
# ==========================================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }
    
    .stApp {
        background-color: #0B0E14;
        color: #E6EDF3;
    }

    /* Terminal Header */
    .terminal-nav {
        background: #161B22;
        border-bottom: 1px solid #30363D;
        padding: 14px 24px;
        margin: -1rem -1rem 1.5rem -1rem;
        display: flex;
        justify-content: space-between;
        align-items: center;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.5);
    }
    .terminal-title {
        font-family: 'JetBrains Mono', monospace;
        font-size: 18px;
        font-weight: 700;
        color: #58A6FF;
        display: flex;
        align-items: center;
        gap: 10px;
    }
    .terminal-status {
        font-family: 'JetBrains Mono', monospace;
        font-size: 11px;
        font-weight: 600;
        padding: 4px 10px;
        border-radius: 4px;
        background: rgba(35, 134, 54, 0.2);
        color: #3FB950;
        border: 1px solid rgba(46, 160, 67, 0.4);
    }

    /* Section Headers */
    .pro-header {
        font-family: 'Inter', sans-serif;
        font-size: 14px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        color: #8B949E;
        margin-top: 22px;
        margin-bottom: 14px;
        border-left: 3px solid #58A6FF;
        padding-left: 10px;
    }

    /* Metric Cards with Aesthetic Inner/Inset Shadow */
    .metric-container {
        background: #12161F;
        border: 1px solid #30363D;
        border-radius: 10px;
        padding: 18px;
        box-shadow: inset 0 3px 10px rgba(0, 0, 0, 0.75), 0 4px 12px rgba(0, 0, 0, 0.3);
        transition: all 0.25s ease-in-out;
    }
    .metric-container:hover {
        border-color: #58A6FF;
        box-shadow: inset 0 2px 8px rgba(0, 0, 0, 0.6), 0 6px 18px rgba(88, 166, 255, 0.2);
        transform: translateY(-2px);
    }
    .metric-title {
        font-family: 'JetBrains Mono', monospace;
        font-size: 11px;
        font-weight: 600;
        text-transform: uppercase;
        color: #8B949E;
        letter-spacing: 0.05em;
    }
    .metric-num {
        font-
