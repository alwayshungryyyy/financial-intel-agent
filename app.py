# ==========================================
# INSTITUTIONAL TRADING DESK CSS THEME (GLOW ENHANCED)
# ==========================================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }
    
    /* Background Canvas with Subtle Ambient Glow Grid */
    .stApp {
        background-color: #07090E;
        background-image: 
            radial-gradient(at 0% 0%, rgba(88, 166, 255, 0.08) 0px, transparent 50%),
            radial-gradient(at 100% 100%, rgba(163, 113, 247, 0.08) 0px, transparent 50%),
            radial-gradient(at 50% 50%, rgba(35, 134, 54, 0.04) 0px, transparent 60%);
        background-attachment: fixed;
        color: #E6EDF3;
    }

    /* Terminal Header */
    .terminal-nav {
        background: rgba(22, 27, 34, 0.85);
        backdrop-filter: blur(12px);
        border-bottom: 1px solid #30363D;
        padding: 14px 24px;
        margin: -1rem -1rem 1.5rem -1rem;
        display: flex;
        justify-content: space-between;
        align-items: center;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.6);
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

    /* Metric Cards with Inset Shadow */
    .metric-container {
        background: rgba(18, 22, 31, 0.85);
        backdrop-filter: blur(8px);
        border: 1px solid #30363D;
        border-radius: 10px;
        padding: 18px;
        box-shadow: inset 0 3px 10px rgba(0, 0, 0, 0.75), 0 4px 12px rgba(0, 0, 0, 0.3);
        transition: all 0.25s ease-in-out;
    }
    .metric-container:hover {
        border-color: #58A6FF;
        box-shadow: inset 0 2px 8px rgba(0, 0, 0, 0.6), 0 6px 18px rgba(88, 166, 255, 0.25);
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
        font-family: 'JetBrains Mono', monospace;
        font-size: 24px;
        font-weight: 700;
        color: #F0F6FC;
        margin: 6px 0;
    }
    .metric-tag {
        display: inline-block;
        font-family: 'JetBrains Mono', monospace;
        font-size: 10px;
        font-weight: 700;
        padding: 2px 8px;
        border-radius: 4px;
    }
    .tag-bull { background: rgba(35, 134, 54, 0.2); color: #3FB950; border: 1px solid rgba(46, 160, 67, 0.4); }
    .tag-bear { background: rgba(218, 54, 51, 0.2); color: #F85149; border: 1px solid rgba(248, 81, 73, 0.4); }
    .tag-neutral { background: rgba(139, 148, 158, 0.2); color: #C9D1D9; border: 1px solid rgba(139, 148, 158, 0.4); }

    /* Glowing Container for Pie Charts */
    .pie-glow-box {
        background: rgba(22, 27, 34, 0.75);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(88, 166, 255, 0.3);
        border-radius: 12px;
        padding: 16px;
        box-shadow: 0 0 20px rgba(88, 166, 255, 0.12), inset 0 1px 1px rgba(255, 255, 255, 0.05);
        transition: all 0.3s ease;
    }
    .pie-glow-box:hover {
        border-color: #58A6FF;
        box-shadow: 0 0 28px rgba(88, 166, 255, 0.25), inset 0 1px 1px rgba(255, 255, 255, 0.1);
        transform: translateY(-2px);
    }

    /* Verdict Card with Rigid Layout & Fixed Text Sizes */
    .verdict-card {
        background: linear-gradient(145deg, rgba(22, 27, 34, 0.9) 0%, rgba(13, 17, 23, 0.9) 100%);
        backdrop-filter: blur(8px);
        border: 1px solid #58A6FF;
        border-radius: 10px;
        padding: 22px;
        margin: 10px 0;
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.5), inset 0 1px 0 rgba(255, 255, 255, 0.05);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    .verdict-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 12px 28px rgba(0, 0, 0, 0.65), 0 0 15px rgba(88, 166, 255, 0.15);
    }
    .verdict-header {
        font-family: 'JetBrains Mono', monospace !important;
        font-size: 11px !important;
        font-weight: 700 !important;
        color: #58A6FF !important;
        text-transform: uppercase !important;
        letter-spacing: 0.06em !important;
        margin-bottom: 8px !important;
    }
    .verdict-title {
        font-size: 18px !important;
        font-weight: 700 !important;
        margin: 6px 0 10px 0 !important;
        line-height: 1.3 !important;
    }
    .verdict-body {
        color: #C9D1D9 !important;
        font-size: 13.5px !important;
        line-height: 1.6 !important;
        font-weight: 400 !important;
        min-height: 85px;
    }

    /* Article Boxes with Dark Gradient Backgrounds & Deep Shadows */
    .agent-box {
        background: linear-gradient(135deg, rgba(22, 27, 34, 0.85) 0%, rgba(15, 19, 25, 0.85) 100%);
        backdrop-filter: blur(8px);
        border: 1px solid #30363D;
        border-radius: 10px;
        padding: 20px 24px;
        margin-bottom: 20px;
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.45), inset 0 1px 1px rgba(255, 255, 255, 0.03);
        transition: border-color 0.2s ease, box-shadow 0.2s ease;
    }
    .agent-box:hover {
        border-color: #58A6FF;
        box-shadow: 0 12px 28px rgba(88, 166, 255, 0.15);
    }
    .agent-header-title {
        font-size: 15px !important;
        font-weight: 700 !important;
        color: #F0F6FC !important;
        margin-bottom: 10px !important;
        display: flex;
        align-items: center;
        gap: 8px;
    }
    .agent-content-text {
        font-size: 13.5px !important;
        color: #C9D1D9 !important;
        line-height: 1.65 !important;
    }
    .citation-badge {
        display: inline-block;
        background: #090D12;
        border: 1px solid #30363D;
        border-radius: 4px;
        padding: 4px 10px;
        font-family: 'JetBrains Mono', monospace;
        font-size: 11px;
        font-weight: 600;
        color: #58A6FF;
        margin-top: 12px;
        box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.5);
    }

    /* Sidebar Adjustments */
    [data-testid="stSidebar"] {
        background-color: #12161F !important;
        border-right: 1px solid #30363D !important;
    }
    [data-testid="stSidebar"] label p {
        font-family: 'JetBrains Mono', monospace !important;
        font-size: 11px !important;
        font-weight: 600 !important;
        text-transform: uppercase !important;
        color: #8B949E !important;
    }

    /* Action Trigger Button */
    div.stButton > button {
        background: #238636;
        color: #FFFFFF;
        font-family: 'JetBrains Mono', monospace;
        font-size: 13px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        border: 1px solid rgba(240, 246, 252, 0.1);
        border-radius: 6px;
        padding: 10px 20px;
        width: 100%;
        box-shadow: 0 4px 12px rgba(35, 134, 54, 0.3);
        transition: all 0.2s ease;
    }
    div.stButton > button:hover {
        background: #2EA043;
        border-color: #58A6FF;
        box-shadow: 0 6px 16px rgba(35, 134, 54, 0.45);
    }

    /* Telemetry KPI Metrics */
    [data-testid="stMetric"] {
        background: rgba(18, 22, 31, 0.85);
        border: 1px solid #30363D;
        border-radius: 6px;
        padding: 12px 16px;
        box-shadow: inset 0 2px 6px rgba(0, 0, 0, 0.6), 0 4px 12px rgba(0, 0, 0, 0.3);
    }
    [data-testid="stMetricLabel"] p {
        font-family: 'JetBrains Mono', monospace !important;
        font-size: 10px !important;
        font-weight: 600 !important;
        text-transform: uppercase !important;
        color: #8B949E !important;
    }
    [data-testid="stMetricValue"] div {
        font-family: 'JetBrains Mono', monospace !important;
        font-size: 18px !important;
        font-weight: 700 !important;
        color: #58A6FF !important;
    }
</style>
""", unsafe_allow_html=True)
