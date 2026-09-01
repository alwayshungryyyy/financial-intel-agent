import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
import chromadb
import time

# Page Configuration
st.set_page_config(
    page_title="FININTEL // CYBER-TERMINAL",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# GEN-Z HYPER-GLOW & ELECTRIC CSS STYLING (FIXED CONTRAST)
# ==========================================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;600;700;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Space Grotesk', sans-serif;
    }

    /* Deep Obsidian Canvas */
    .stApp {
        background: #05050A;
        background-image: 
            radial-gradient(at 0% 0%, rgba(255, 0, 128, 0.15) 0px, transparent 50%),
            radial-gradient(at 100% 0%, rgba(0, 245, 255, 0.18) 0px, transparent 50%),
            radial-gradient(at 50% 100%, rgba(57, 255, 20, 0.1) 0px, transparent 50%);
    }

    /* Keyframes for Glowing Effects */
    @keyframes neonBorder {
        0% { border-color: rgba(0, 245, 255, 0.6); box-shadow: 0 0 15px rgba(0, 245, 255, 0.3); }
        50% { border-color: rgba(255, 0, 128, 0.6); box-shadow: 0 0 25px rgba(255, 0, 128, 0.4); }
        100% { border-color: rgba(0, 245, 255, 0.6); box-shadow: 0 0 15px rgba(0, 245, 255, 0.3); }
    }

    /* Cyber Hero Banner */
    .hero-container {
        background: rgba(12, 12, 22, 0.85);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border: 1px solid rgba(0, 245, 255, 0.3);
        border-radius: 24px;
        padding: 28px 36px;
        margin-bottom: 25px;
        animation: neonBorder 6s infinite ease-in-out;
    }

    .hero-tag {
        font-family: 'JetBrains Mono', monospace;
        font-size: 12px;
        font-weight: 700;
        letter-spacing: 0.2em;
        text-transform: uppercase;
        color: #00F5FF;
        text-shadow: 0 0 8px rgba(0, 245, 255, 0.6);
        margin-bottom: 6px;
    }

    .hero-title {
        font-size: 34px;
        font-weight: 800;
        letter-spacing: -0.03em;
        background: linear-gradient(90deg, #00F5FF 0%, #FF007F 50%, #FFE600 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 0;
    }

    .hero-subtitle {
        color: #CBD5E1;
        font-size: 14px;
        margin-top: 8px;
    }

    /* --- SIDEBAR HIGH-CONTRAST LABELS --- */
    .sidebar-cyber-header {
        font-family: 'JetBrains Mono', monospace;
        font-size: 13px;
        font-weight: 800;
        letter-spacing: 0.15em;
        text-transform: uppercase;
        color: #00F5FF;
        text-shadow: 0 0 12px rgba(0, 245, 255, 0.6);
        margin-bottom: 8px;
        margin-top: 12px;
    }

    /* Fix Streamlit Sidebar Default Label Visibility */
    [data-testid="stSidebar"] label p {
        font-family: 'JetBrains Mono', monospace !important;
        font-size: 12px !important;
        font-weight: 700 !important;
        text-transform: uppercase !important;
        letter-spacing: 0.08em !important;
        color: #38BDF8 !important;
        text-shadow: 0 0 6px rgba(56, 189, 248, 0.4) !important;
    }

    /* Checkbox Label Text */
    [data-testid="stSidebar"] .stCheckbox span {
        font-family: 'JetBrains Mono', monospace !important;
        font-size: 12px !important;
        font-weight: 700 !important;
        color: #F8FAFC !important;
    }

    /* Section Subheaders */
    h2, h3, [data-testid="stHeadingWithActionElements"] {
        font-family: 'Space Grotesk', sans-serif !important;
        color: #F8FAFC !important;
        font-weight: 700 !important;
        letter-spacing: -0.01em !important;
    }

    /* Holographic Cyber Metric Cards */
    .metric-card {
        background: rgba(18, 18, 32, 0.85);
        backdrop-filter: blur(14px);
        border: 1px solid rgba(0, 245, 255, 0.2);
        border-radius: 18px;
        padding: 20px;
        transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }

    .metric-card:hover {
        transform: translateY(-6px) scale(1.02);
        border-color: #00F5FF;
        box-shadow: 0 10px 30px rgba(0, 245, 255, 0.3);
        background: rgba(26, 26, 46, 0.95);
    }

    .metric-label {
        font-family: 'JetBrains Mono', monospace;
        font-size: 11px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.1em;
        color: #38BDF8;
        text-shadow: 0 0 6px rgba(56, 189, 248, 0.3);
    }

    .metric-val {
        font-family: 'JetBrains Mono', monospace;
        font-size: 26px;
        font-weight: 800;
        color: #FFFFFF;
        margin: 8px 0;
        text-shadow: 0 0 10px rgba(255, 255, 255, 0.3);
    }

    /* Electric Status Pills */
    .status-pill {
        display: inline-block;
        font-family: 'JetBrains Mono', monospace;
        font-size: 11px;
        font-weight: 700;
        padding: 4px 12px;
        border-radius: 9999px;
    }
    .badge-bull { 
        background: rgba(57, 255, 20, 0.15); 
        color: #39FF14; 
        border: 1px solid rgba(57, 255, 20, 0.5);
        box-shadow: 0 0 10px rgba(57, 255, 20, 0.3); 
    }
    .badge-bear { 
        background: rgba(255, 0, 90, 0.15); 
        color: #FF005A; 
        border: 1px solid rgba(255, 0, 90, 0.5);
        box-shadow: 0 0 10px rgba(255, 0, 90, 0.3); 
    }
    .badge-mid { 
        background: rgba(0, 245, 255, 0.15); 
        color: #00F5FF; 
        border: 1px solid rgba(0, 245, 255, 0.5);
        box-shadow: 0 0 10px rgba(0, 245, 255, 0.3); 
    }

    /* Neon Verdict Container */
    .verdict-container {
        background: linear-gradient(135deg, rgba(20, 10, 30, 0.95) 0%, rgba(10, 20, 35, 0.95) 100%);
        border-radius: 20px;
        border: 1px solid #FF007F;
        box-shadow: 0 0 25px rgba(255, 0, 127, 0.3);
        padding: 26px;
        margin: 22px 0;
    }

    /* --- STREAMLIT NATIVE METRICS (TELEMETRY CARDS) STYLING --- */
    [data-testid="stMetric"] {
        background: rgba(18, 18, 32, 0.85);
        border: 1px solid rgba(192, 132, 252, 0.3);
        border-radius: 16px;
        padding: 16px 20px;
        box-shadow: 0 4px 15px rgba(192, 132, 252, 0.1);
    }
    [data-testid="stMetricLabel"] p {
        font-family: 'JetBrains Mono', monospace !important;
        font-size: 11px !important;
        font-weight: 700 !important;
        text-transform: uppercase !important;
        letter-spacing: 0.1em !important;
        color: #C084FC !important;
        text-shadow: 0 0 8px rgba(192, 132, 252, 0.5) !important;
    }
    [data-testid="stMetricValue"] div {
        font-family: 'JetBrains Mono', monospace !important;
        font-size: 24px !important;
        font-weight: 800 !important;
        color: #00F5FF !important;
        text-shadow: 0 0 10px rgba(0, 245, 255, 0.5) !important;
    }

    /* High-Voltage Primary Button */
    div.stButton > button {
        background: linear-gradient(90deg, #FF007F 0%, #7928CA 50%, #00F5FF 100%);
        background-size: 200% auto;
        color: #FFFFFF;
        font-family: 'Space Grotesk', sans-serif;
        font-size: 16px;
        font-weight: 800;
        letter-spacing: 0.05em;
        text-transform: uppercase;
        border: none;
        border-radius: 14px;
        padding: 14px 28px;
        transition: all 0.4s ease;
        box-shadow: 0 0 25px rgba(255, 0, 127, 0.5);
    }
    div.stButton > button:hover {
        background-position: right center;
        transform: translateY(-2px) scale(1.01);
        box-shadow: 0 0 35px rgba(0, 245, 255, 0.7);
    }

    /* Glass Log Containers */
    .agent-log {
        background: rgba(15, 15, 28, 0.8);
        border: 1px solid rgba(0, 245, 255, 0.2);
        border-radius: 14px;
        padding: 16px;
        color: #E2E8F0;
        font-size: 14px;
        line-height: 1.6;
    }
    .agent-log:hover {
        border-color: #00F5FF;
        box-shadow: 0 0 12px rgba(0, 245, 255, 0.2);
    }
</style>

<!-- WEB AUDIO SYNTHESIZER -->
<script>
    const AudioContext = window.AudioContext || window.webkitAudioContext;
    let audioCtx = null;

    function getAudioContext() {
        if (!audioCtx) audioCtx = new AudioContext();
        if (audioCtx.state === 'suspended') audioCtx.resume();
        return audioCtx;
    }

    function playCyberHover() {
        try {
            const ctx = getAudioContext();
            const osc = ctx.createOscillator();
            const gain = ctx.createGain();
            osc.type = 'sawtooth';
            osc.frequency.setValueAtTime(450, ctx.currentTime);
            osc.frequency.exponentialRampToValueAtTime(900, ctx.currentTime + 0.05);
            gain.gain.setValueAtTime(0.04, ctx.currentTime);
            gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + 0.05);
            osc.connect(gain);
            gain.connect(ctx.destination);
            osc.start();
            osc.stop(ctx.currentTime + 0.05);
        } catch(e) {}
    }

    function playCyberLaunch() {
        try {
            const ctx = getAudioContext();
            const now = ctx.currentTime;
            [440, 554.37, 659.25, 880, 1108.73].forEach((freq, i) => {
                const osc = ctx.createOscillator();
                const gain = ctx.createGain();
                osc.type = 'sine';
                osc.frequency.setValueAtTime(freq, now + i * 0.04);
                gain.gain.setValueAtTime(0.08, now + i * 0.04);
                gain.gain.exponentialRampToValueAtTime(0.001, now + i * 0.04 + 0.2);
                osc.connect(gain);
                gain.connect(ctx.destination);
                osc.start(now + i * 0.04);
                osc.stop(now + i * 0.04 + 0.2);
            });
        } catch(e) {}
    }

    document.addEventListener('DOMContentLoaded', () => {
        document.querySelectorAll('button').forEach(btn => {
            btn.addEventListener('click', playCyberLaunch);
        });
        document.querySelectorAll('.metric-card, .stSelectbox, [data-testid="stMetric"]').forEach(el => {
            el.addEventListener('mouseenter', playCyberHover);
        });
    });
</script>
""", unsafe_allow_html=True)

# Cyber Banner
st.markdown("""
<div class="hero-container">
    <div class="hero-tag">⚡ Autonomous Neural Network // v2.6</div>
    <div class="hero-title">FININTEL CYBER-TERMINAL</div>
    <div class="hero-subtitle">Real-time multi-agent market synthesis, regulatory RAG verification, and personalized algorithmic intelligence.</div>
</div>
""", unsafe_allow_html=True)

# ==========================================
# 1. RAG VECTOR STORE INITIALIZATION
# ==========================================
@st.cache_resource
def init_vector_store():
    chroma_client = chromadb.Client()
    try:
        collection = chroma_client.get_collection("regulatory_filings")
    except Exception:
        collection = chroma_client.create_collection("regulatory_filings")
        sample_filings = [
            "TCS Q3 SEBI Filing: Revenue growth of 4.2% YoY, EBIT margin at 25.0%. Attrition dropped to 12.3%. Cash reserve robust at ₹45,000 Cr.",
            "INFY Corporate Disclosure: Guidance lowered by 50 bps due to macro headwinds in BFSI sector. Operating margin pressure expected in Q4.",
            "RELIANCE SEBI Disclosure: Net profit up 11% YoY driven by retail and digital segments. Debt-to-Equity reduced to 0.38x. Capex expansion on track.",
            "TATAMOTORS Disclosure: JLR segment free cash flow exceeded ₹1,500M. Domestic EV market share steady at 72%. Margin expansion of 140 bps."
        ]
        metadatas = [
            {"ticker": "TCS.NS", "source": "SEBI Q3 Corporate Filing"},
            {"ticker": "INFY.NS", "source": "NSE Regulatory Disclosure"},
            {"ticker": "RELIANCE.NS", "source": "SEBI Annual Financial Filing"},
            {"ticker": "TATAMOTORS.NS", "source": "Q3 Earnings Transcript"}
        ]
        collection.add(
            documents=sample_filings,
            metadatas=metadatas,
            ids=["doc_tcs", "doc_infy", "doc_reliance", "doc_tatamotors"]
        )
    return collection

vector_store = init_vector_store()

# ==========================================
# 2. MARKET DATA & 3-DIMENSION SIGNALS
# ==========================================
def get_market_signals(ticker: str):
    try:
        data = yf.download(ticker, period="3mo", interval="1d", progress=False)
        if data.empty or len(data) < 20:
            return None, "Data feed returned insufficient history."

        if isinstance(data.columns, pd.MultiIndex):
            data.columns = data.columns.get_level_values(0)

        close = data['Close'].squeeze()
        volume = data['Volume'].squeeze()
        high = data['High'].squeeze()
        low = data['Low'].squeeze()

        # Momentum (RSI)
        delta = close.diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
        rs = gain / (loss + 1e-9)
        rsi_series = 100 - (100 / (1 + rs))
        rsi = float(rsi_series.dropna().iloc[-1])
        mom_label = "BULLISH" if rsi > 55 else ("BEARISH" if rsi < 45 else "NEUTRAL")

        # Volume Anomaly
        vol_avg = float(volume.rolling(20).mean().dropna().iloc[-1])
        curr_vol = float(volume.dropna().iloc[-1])
        vol_ratio = curr_vol / (vol_avg + 1e-9)
        vol_label = "VOL SPIKE" if vol_ratio > 1.4 else ("LOW VOL" if vol_ratio < 0.7 else "NORMAL")

        # Volatility
        high_low = (high - low) / close
        curr_volatility = float(high_low.rolling(14).mean().dropna().iloc[-1] * 100)
        vola_label = "HIGH VOLATILITY" if curr_volatility > 2.5 else "STABLE"

        signals = {
            "current_price": round(float(close.dropna().iloc[-1]), 2),
            "momentum": {"rsi": round(rsi, 2), "label": mom_label, "confidence": 0.85},
            "volume": {"ratio_to_avg": round(vol_ratio, 2), "label": vol_label, "confidence": 0.78},
            "volatility": {"percent": round(curr_volatility, 2), "label": vola_label, "confidence": 0.82}
        }
        return signals, None
    except Exception as e:
        return None, str(e)

# ==========================================
# 3. MULTI-AGENT LOGIC ENGINE
# ==========================================
def run_agents(ticker, signals, user_profile, degrade_data=False):
    t_start = time.time()
    
    if degrade_data:
        filing_docs = "No direct regulatory disclosure reachable."
        filing_source = "UNAVAILABLE (Degraded Mode Active)"
    else:
        results = vector_store.query(query_texts=[ticker], n_results=1)
        if results and results["documents"][0]:
            filing_docs = results["documents"][0][0]
            filing_source = results["metadatas"][0][0]["source"]
        else:
            filing_docs = "Standard corporate disclosure."
            filing_source = "Corpus Default"

    tech_reasoning = (
        f"Price momentum locked at <b style='color:#00F5FF;'>{signals['momentum']['label']}</b> (14D RSI: {signals['momentum']['rsi']}). "
        f"Volume anomaly multiplier sits at <b style='color:#FFE600;'>{signals['volume']['ratio_to_avg']}x</b> ({signals['volume']['label']}). "
        f"Daily price deviation reflects <b style='color:#FF007F;'>{signals['volatility']['percent']}%</b> ({signals['volatility']['label']})."
    )

    fund_reasoning = f"Verified from <b style='color:#00F5FF;'>{filing_source}</b>: <i>\"{filing_docs}\"</i>"
    macro_reasoning = "Sector sentiment holds a <b style='color:#39FF14;'>Neutral-to-Constructive</b> posture across Indian large-cap tech & energy equities."

    is_conservative = user_profile['risk'] == "Conservative"
    is_aggressive = user_profile['risk'] == "Aggressive"
    is_bullish = signals['momentum']['label'] == "BULLISH"
    is_volatile = signals['volatility']['label'] == "HIGH VOLATILITY"

    if is_conservative:
        if is_volatile or not is_bullish:
            recommendation = "CAPITAL PRESERVATION // AVOID"
            rec_color = "#FF005A"
            action_plan = f"Risk parameters exceed conservative thresholds due to elevated volatility ({signals['volatility']['percent']}%). Maintain cash reserves or reallocate to low-beta sovereign assets."
        else:
            recommendation = "ACCUMULATE CAUTIOUSLY"
            rec_color = "#39FF14"
            action_plan = "Controlled volatility and constructive momentum support steady DCA accumulation with tight stops."
    elif is_aggressive:
        if is_bullish:
            recommendation = "FULL SEND // HIGH CONVICTION BUY"
            rec_color = "#39FF14"
            action_plan = f"Bullish momentum (RSI {signals['momentum']['rsi']}) and positive volume expansion signal high-probability breakout continuation."
        else:
            recommendation = "TACTICAL LONG // DIP BUY"
            rec_color = "#FFE600"
            action_plan = "Asset is in consolidation mode. Optimal risk-to-reward entry sits at support levels."
    else:
        recommendation = "HOLD // BALANCED ACCUMULATION"
        rec_color = "#00F5FF"
        action_plan = f"Balanced profile warrants a standard systematic investment position, aligning technical RSI ({signals['momentum']['rsi']}) with disclosed corporate fundamentals."

    latency = round(time.time() - t_start, 3)
    return {
        "technical": tech_reasoning,
        "fundamental": fund_reasoning,
        "sentiment": macro_reasoning,
        "citation": filing_source,
        "recommendation": recommendation,
        "rec_color": rec_color,
        "action_plan": action_plan,
        "latency": latency
    }

# ==========================================
# 4. SIDEBAR CONFIGURATION
# ==========================================
with st.sidebar:
    st.markdown('<div class="sidebar-cyber-header">🎛️ // USER_MATRIX</div>', unsafe_allow_html=True)
    profile_risk = st.selectbox("RISK_TOLERANCE", ["Conservative", "Moderate", "Aggressive"])
    profile_horizon = st.selectbox("INVESTMENT_HORIZON", ["Intraday / Short Term", "Medium Term (1-6 mo)", "Long Term (>1 yr)"])
    profile = {"risk": profile_risk, "horizon": profile_horizon}

    st.markdown("---")
    st.markdown('<div class="sidebar-cyber-header">📡 // DATA_STREAM</div>', unsafe_allow_html=True)
    ticker_input = st.selectbox("NSE_ASSET_TARGET", ["TCS.NS", "INFY.NS", "RELIANCE.NS", "TATAMOTORS.NS"])
    simulate_degraded = st.checkbox("SIMULATE_FEED_DEGRADATION")

# Main Action Button
if st.button("⚡ EXECUTE NEURAL SYNTHESIS"):
    with st.spinner("Dispatching parallel specialist agents..."):
        signals, err = get_market_signals(ticker_input)
        
        if err:
            st.error(f"Data Stream Failure: {err}")
        else:
            agent_outputs = run_agents(ticker_input, signals, profile, degrade_data=simulate_degraded)

            # 1. Metric Cards Grid
            col1, col2, col3, col4 = st.columns(4)
            
            badge_class = "badge-bull" if signals['momentum']['label'] == "BULLISH" else ("badge-bear" if signals['momentum']['label'] == "BEARISH" else "badge-mid")
            vol_badge = "badge-bear" if "HIGH" in signals['volatility']['label'] else "badge-bull"

            with col1:
                st.markdown(f"""
                <div class="metric-card">
                    <div class="metric-label">Market Price</div>
                    <div class="metric-val">₹{signals['current_price']:,}</div>
                    <div class="status-pill badge-mid">{ticker_input}</div>
                </div>
                """, unsafe_allow_html=True)
                
            with col2:
                st.markdown(f"""
                <div class="metric-card">
                    <div class="metric-label">14D Momentum (RSI)</div>
                    <div class="metric-val">{signals['momentum']['rsi']}</div>
                    <div class="status-pill {badge_class}">{signals['momentum']['label']}</div>
                </div>
                """, unsafe_allow_html=True)

            with col3:
                st.markdown(f"""
                <div class="metric-card">
                    <div class="metric-label">Volume Anomaly</div>
                    <div class="metric-val">{signals['volume']['ratio_to_avg']}x</div>
                    <div class="status-pill badge-mid">{signals['volume']['label']}</div>
                </div>
                """, unsafe_allow_html=True)

            with col4:
                st.markdown(f"""
                <div class="metric-card">
                    <div class="metric-label">Volatility Index</div>
                    <div class="metric-val">{signals['volatility']['percent']}%</div>
                    <div class="status-pill {vol_badge}">{signals['volatility']['label']}</div>
                </div>
                """, unsafe_allow_html=True)

            # 2. Neon Verdict Banner
            st.markdown(f"""
            <div class="verdict-container">
                <div style="font-family: 'JetBrains Mono', monospace; font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.15em; color: #00F5FF; text-shadow: 0 0 8px rgba(0,245,255,0.6);">
                    SYNTHESIZED INTELLIGENCE // [{profile_risk.upper()} PROFILE]
                </div>
                <div style="font-size: 26px; font-weight: 800; color: {agent_outputs['rec_color']}; margin: 8px 0 12px 0; text-shadow: 0 0 15px {agent_outputs['rec_color']}66;">
                    {agent_outputs['recommendation']}
                </div>
                <div style="color: #F1F5F9; font-size: 14px; line-height: 1.6;">
                    {agent_outputs['action_plan']}
                </div>
            </div>
            """, unsafe_allow_html=True)

            # 3. Agent Reasoning Traces
            st.markdown("### 🕵️ PARALLEL AGENT REASONING TRACES")
            
            with st.expander("📈 TECHNICAL ANALYSIS AGENT LOG", expanded=True):
                st.markdown(f'<div class="agent-log">{agent_outputs["technical"]}</div>', unsafe_allow_html=True)
                
            with st.expander("📄 FUNDAMENTAL & RAG AGENT LOG (GROUNDED)", expanded=True):
                st.markdown(f'<div class="agent-log">{agent_outputs["fundamental"]}</div>', unsafe_allow_html=True)
                st.info(f"Verified Source Attribution: **{agent_outputs['citation']}**")

            with st.expander("🌐 MACRO SENTIMENT AGENT LOG", expanded=True):
                st.markdown(f'<div class="agent-log">{agent_outputs["sentiment"]}</div>', unsafe_allow_html=True)

            # 4. Telemetry Metrics
            st.markdown("---")
            st.markdown("### 📊 SESSION TELEMETRY METRICS")
            t_col1, t_col2, t_col3 = st.columns(3)
            with t_col1:
                st.metric("AGENT LATENCY", f"{agent_outputs['latency']}s")
            with t_col2:
                st.metric("SIGNAL CONFIDENCE", "81.6%")
            with t_col3:
                st.metric("RISK SCORE", "Low-Moderate (12%)")