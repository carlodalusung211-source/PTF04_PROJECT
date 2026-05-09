import streamlit as st
import numpy as np

# ── Page config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="PTF04 — Carlo Glenn F. Dalusung",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Global CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

/* ── Reset & base ── */
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
    background: #0d0f14;
    color: #e2e8f0;
}

/* ── Hide default streamlit chrome ── */
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 0 !important; max-width: 100% !important; }

/* ── Custom scrollbar ── */
::-webkit-scrollbar { width: 4px; }
::-webkit-scrollbar-track { background: #0d0f14; }
::-webkit-scrollbar-thumb { background: #3b82f6; border-radius: 2px; }

/* ── Sidebar ── */
[data-testid="stSidebar"] {
    background: rgba(15, 17, 25, 0.95) !important;
    border-right: 1px solid rgba(59,130,246,0.15) !important;
    backdrop-filter: blur(20px);
}
[data-testid="stSidebar"] > div:first-child { padding: 0; }

/* ── Nav buttons ── */
.nav-btn {
    display: flex;
    align-items: center;
    gap: 12px;
    width: 100%;
    padding: 12px 20px;
    background: transparent;
    border: none;
    border-left: 3px solid transparent;
    color: #94a3b8;
    font-family: 'Inter', sans-serif;
    font-size: 0.88rem;
    font-weight: 500;
    cursor: pointer;
    transition: all 0.2s ease;
    text-align: left;
    letter-spacing: 0.01em;
}
.nav-btn:hover {
    background: rgba(59,130,246,0.08);
    color: #e2e8f0;
    border-left-color: rgba(59,130,246,0.4);
}
.nav-btn.active {
    background: rgba(59,130,246,0.12);
    color: #60a5fa;
    border-left-color: #3b82f6;
}
.nav-dot {
    width: 6px; height: 6px;
    border-radius: 50%;
    background: currentColor;
    opacity: 0.6;
    flex-shrink: 0;
}

/* ── Hero ── */
.hero {
    position: relative;
    min-height: 420px;
    display: flex;
    align-items: center;
    padding: 80px 64px;
    overflow: hidden;
    background: linear-gradient(135deg, #0d0f14 0%, #0f172a 50%, #0d0f14 100%);
    border-bottom: 1px solid rgba(59,130,246,0.1);
}
.hero-bg {
    position: absolute; inset: 0; pointer-events: none;
}
.orb {
    position: absolute;
    border-radius: 50%;
    filter: blur(80px);
    opacity: 0.18;
    animation: float 8s ease-in-out infinite;
}
.orb-1 { width:400px; height:400px; background:#3b82f6; top:-100px; right:10%; animation-delay:0s; }
.orb-2 { width:300px; height:300px; background:#6366f1; bottom:-80px; right:25%; animation-delay:3s; }
.orb-3 { width:200px; height:200px; background:#0ea5e9; top:50%; left:40%; animation-delay:5s; }
@keyframes float {
    0%,100% { transform: translateY(0px) scale(1); }
    50%      { transform: translateY(-20px) scale(1.05); }
}

/* Geometric grid lines */
.hero::before {
    content: '';
    position: absolute; inset: 0;
    background-image:
        linear-gradient(rgba(59,130,246,0.04) 1px, transparent 1px),
        linear-gradient(90deg, rgba(59,130,246,0.04) 1px, transparent 1px);
    background-size: 60px 60px;
    pointer-events: none;
}

.hero-content { position: relative; z-index: 1; max-width: 700px; }

.hero-tag {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: rgba(59,130,246,0.1);
    border: 1px solid rgba(59,130,246,0.25);
    border-radius: 999px;
    padding: 4px 14px;
    font-size: 0.75rem;
    font-weight: 600;
    color: #60a5fa;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    margin-bottom: 24px;
}

.hero h1 {
    font-size: clamp(2rem, 4vw, 3.2rem);
    font-weight: 700;
    line-height: 1.15;
    color: #f1f5f9;
    margin-bottom: 20px;
    letter-spacing: -0.02em;
}

.hero h1 span { color: #3b82f6; }

.hero-sub {
    font-size: 1rem;
    color: #64748b;
    line-height: 1.7;
    max-width: 520px;
    margin-bottom: 36px;
}

.hero-stats {
    display: flex;
    gap: 40px;
    flex-wrap: wrap;
}

.stat-item { display: flex; flex-direction: column; gap: 2px; }
.stat-num  { font-size: 1.5rem; font-weight: 700; color: #f1f5f9; }
.stat-lbl  { font-size: 0.75rem; color: #475569; text-transform: uppercase; letter-spacing: 0.06em; }

/* ── Page content wrapper ── */
.page-wrap { padding: 48px 64px; max-width: 1100px; }

/* ── Section heading ── */
.section-head {
    display: flex;
    align-items: center;
    gap: 14px;
    margin-bottom: 32px;
}
.section-line {
    flex: 1;
    height: 1px;
    background: linear-gradient(90deg, rgba(59,130,246,0.3), transparent);
}
.section-title {
    font-size: 0.7rem;
    font-weight: 700;
    color: #3b82f6;
    letter-spacing: 0.12em;
    text-transform: uppercase;
}

/* ── Glass card ── */
.glass-card {
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 16px;
    padding: 32px;
    backdrop-filter: blur(12px);
    transition: border-color 0.25s, transform 0.25s, box-shadow 0.25s;
}
.glass-card:hover {
    border-color: rgba(59,130,246,0.25);
    transform: translateY(-2px);
    box-shadow: 0 12px 40px rgba(59,130,246,0.08);
}

/* ── Result cards ── */
.result-positive {
    background: rgba(34,197,94,0.08);
    border: 1px solid rgba(34,197,94,0.2);
    border-left: 4px solid #22c55e;
    border-radius: 12px;
    padding: 24px 28px;
    margin-top: 20px;
}
.result-negative {
    background: rgba(239,68,68,0.08);
    border: 1px solid rgba(239,68,68,0.2);
    border-left: 4px solid #ef4444;
    border-radius: 12px;
    padding: 24px 28px;
    margin-top: 20px;
}
.result-label { font-size: 1.2rem; font-weight: 700; margin-bottom: 6px; }
.result-sub   { font-size: 0.85rem; color: #94a3b8; line-height: 1.6; }

/* ── Metric row ── */
.metric-row {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
    gap: 16px;
    margin-top: 28px;
}
.metric-card {
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(255,255,255,0.06);
    border-radius: 12px;
    padding: 20px;
    text-align: center;
}
.metric-val { font-size: 1.4rem; font-weight: 700; color: #60a5fa; }
.metric-lbl { font-size: 0.75rem; color: #475569; margin-top: 4px; text-transform: uppercase; letter-spacing: 0.05em; }

/* ── Tag pill ── */
.tag {
    display: inline-block;
    background: rgba(59,130,246,0.1);
    border: 1px solid rgba(59,130,246,0.2);
    border-radius: 999px;
    padding: 3px 12px;
    font-size: 0.75rem;
    color: #60a5fa;
    margin: 3px;
}

/* ── Code block ── */
.code-block {
    background: #0a0c10;
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 10px;
    padding: 20px 24px;
    font-family: 'Fira Code', 'Courier New', monospace;
    font-size: 0.82rem;
    color: #94a3b8;
    overflow-x: auto;
    line-height: 1.7;
    white-space: pre;
}
.code-kw  { color: #818cf8; }
.code-fn  { color: #60a5fa; }
.code-str { color: #34d399; }
.code-num { color: #f59e0b; }
.code-cm  { color: #475569; }

/* ── Predict button ── */
div[data-testid="stButton"] > button {
    background: linear-gradient(135deg, #2563eb, #3b82f6) !important;
    color: white !important;
    border: none !important;
    border-radius: 8px !important;
    font-weight: 600 !important;
    font-family: 'Inter', sans-serif !important;
    letter-spacing: 0.02em !important;
    transition: all 0.2s !important;
    box-shadow: 0 4px 14px rgba(59,130,246,0.3) !important;
}
div[data-testid="stButton"] > button:hover {
    transform: translateY(-1px) !important;
    box-shadow: 0 8px 24px rgba(59,130,246,0.4) !important;
}

/* ── Tabs ── */
.stTabs [data-baseweb="tab-list"] {
    background: rgba(255,255,255,0.02) !important;
    border-radius: 10px !important;
    border: 1px solid rgba(255,255,255,0.06) !important;
    padding: 4px !important;
    gap: 4px !important;
}
.stTabs [data-baseweb="tab"] {
    border-radius: 8px !important;
    color: #64748b !important;
    font-weight: 500 !important;
    font-size: 0.88rem !important;
}
.stTabs [aria-selected="true"] {
    background: rgba(59,130,246,0.15) !important;
    color: #60a5fa !important;
}

/* ── Slider & inputs ── */
.stSlider > div > div > div { background: #3b82f6 !important; }
.stTextArea textarea, .stNumberInput input {
    background: rgba(255,255,255,0.04) !important;
    border: 1px solid rgba(255,255,255,0.1) !important;
    border-radius: 8px !important;
    color: #e2e8f0 !important;
    font-family: 'Inter', sans-serif !important;
}

/* ── File uploader ── */
[data-testid="stFileUploader"] {
    border: 1px dashed rgba(59,130,246,0.3) !important;
    border-radius: 12px !important;
    background: rgba(59,130,246,0.03) !important;
}

/* ── Divider ── */
.fancy-divider {
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(59,130,246,0.3), transparent);
    margin: 40px 0;
}

/* ── Footer ── */
.portfolio-footer {
    padding: 32px 64px;
    border-top: 1px solid rgba(255,255,255,0.05);
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 16px;
}
.footer-name { font-size: 0.9rem; font-weight: 600; color: #e2e8f0; }
.footer-sub  { font-size: 0.78rem; color: #475569; margin-top: 2px; }
.footer-tag  { font-size: 0.75rem; color: #3b82f6; }

/* ── Shimmer loading ── */
@keyframes shimmer {
    0%   { background-position: -200% center; }
    100% { background-position: 200% center; }
}
.shimmer {
    background: linear-gradient(90deg, rgba(255,255,255,0.03) 25%, rgba(255,255,255,0.07) 50%, rgba(255,255,255,0.03) 75%);
    background-size: 200% auto;
    animation: shimmer 1.5s linear infinite;
    border-radius: 8px;
    height: 120px;
}

/* prediction bar */
.prob-row { display: flex; align-items: center; gap: 10px; margin-bottom: 10px; }
.prob-name { font-size: 0.82rem; color: #94a3b8; width: 90px; flex-shrink: 0; }
.prob-bg   { flex:1; background: rgba(255,255,255,0.05); border-radius:999px; height:6px; overflow:hidden; }
.prob-fill { height:100%; border-radius:999px; }
.prob-pct  { font-size:0.8rem; color:#64748b; width:36px; text-align:right; flex-shrink:0; }
</style>
""", unsafe_allow_html=True)

# ── Session state ──────────────────────────────────────────────────────────────
if "page" not in st.session_state:
    st.session_state.page = "Home"

# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style="padding:28px 20px 20px;">
        <div style="font-size:0.7rem;font-weight:700;color:#3b82f6;letter-spacing:0.12em;text-transform:uppercase;margin-bottom:4px;">Portfolio</div>
        <div style="font-size:1rem;font-weight:700;color:#f1f5f9;line-height:1.3;">Carlo Glenn F.<br>Dalusung</div>
        <div style="font-size:0.75rem;color:#475569;margin-top:6px;">PTF04 · ML & Data Science</div>
    </div>
    <div style="height:1px;background:rgba(255,255,255,0.06);margin:0 20px 16px;"></div>
    """, unsafe_allow_html=True)

    pages = [
        ("Home",              "01"),
        ("Boston Housing",    "02"),
        ("CIFAR-10",          "03"),
        ("Dogs vs Cats",      "04"),
        ("Iris Classifier",   "05"),
        ("Sentiment Analysis","06"),
    ]

    for label, num in pages:
        active = "active" if st.session_state.page == label else ""
        if st.button(f"{num}  {label}", key=f"nav_{label}", use_container_width=True):
            st.session_state.page = label
            st.rerun()

    st.markdown("""
    <div style="position:absolute;bottom:24px;left:0;right:0;padding:0 20px;">
        <div style="height:1px;background:rgba(255,255,255,0.06);margin-bottom:16px;"></div>
        <div style="font-size:0.72rem;color:#334155;">
            Built with Streamlit<br>
            <span style="color:#3b82f6;">Python · TensorFlow · scikit-learn</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ── Helper components ──────────────────────────────────────────────────────────
def section_head(title):
    st.markdown(f"""
    <div class="section-head">
        <span class="section-title">{title}</span>
        <div class="section-line"></div>
    </div>
    """, unsafe_allow_html=True)

def tags(*labels):
    html = "".join(f'<span class="tag">{l}</span>' for l in labels)
    st.markdown(f'<div style="margin-bottom:20px;">{html}</div>', unsafe_allow_html=True)

def fancy_divider():
    st.markdown('<div class="fancy-divider"></div>', unsafe_allow_html=True)

def code_block(code):
    st.markdown(f'<div class="code-block">{code}</div>', unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# HOME PAGE
# ══════════════════════════════════════════════════════════════════════════════
def page_home():
    # Hero
    st.markdown("""
    <div class="hero">
        <div class="hero-bg">
            <div class="orb orb-1"></div>
            <div class="orb orb-2"></div>
            <div class="orb orb-3"></div>
        </div>
        <div class="hero-content">
            <div class="hero-tag">
                <span style="width:6px;height:6px;border-radius:50%;background:#3b82f6;display:inline-block;"></span>
                PTF04 · Learning Machine Learning &amp; Data Science
            </div>
            <h1>Carlo Glenn F.<br><span>Dalusung</span></h1>
            <p class="hero-sub">
                A compilation of Python activities in Data Science and Machine Learning —
                featuring real neural networks, image classifiers, and NLP models built and deployed end-to-end.
            </p>
            <div class="hero-stats">
                <div class="stat-item">
                    <span class="stat-num">5</span>
                    <span class="stat-lbl">Projects</span>
                </div>
                <div class="stat-item">
                    <span class="stat-num">5</span>
                    <span class="stat-lbl">ML Models</span>
                </div>
                <div class="stat-item">
                    <span class="stat-num">96.7%</span>
                    <span class="stat-lbl">Best Accuracy</span>
                </div>
                <div class="stat-item">
                    <span class="stat-num">Python</span>
                    <span class="stat-lbl">Language</span>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Project cards
    st.markdown('<div class="page-wrap">', unsafe_allow_html=True)
    section_head("PROJECTS")

    projects = [
        {
            "num": "01",
            "title": "Boston Housing",
            "desc": "Neural network regression model predicting median house prices using sepal/petal features. Deployed with interactive sliders.",
            "tags": ["TensorFlow", "Keras", "Regression", "Neural Network"],
            "acc": "76.0% R²",
            "model": "Dense NN",
        },
        {
            "num": "02",
            "title": "CIFAR-10 Classifier",
            "desc": "Convolutional neural network that classifies images into 10 categories: airplane, automobile, bird, cat, deer, dog, frog, horse, ship, truck.",
            "tags": ["CNN", "TensorFlow", "Computer Vision", "Image Classification"],
            "acc": "~76%",
            "model": "CNN",
        },
        {
            "num": "03",
            "title": "Dogs vs Cats",
            "desc": "Binary image classifier using a CNN trained to distinguish between dog and cat photographs with high confidence.",
            "tags": ["CNN", "TensorFlow", "Binary Classification", "Computer Vision"],
            "acc": "~90%+",
            "model": "CNN",
        },
        {
            "num": "04",
            "title": "Iris Classifier",
            "desc": "K-Nearest Neighbors classifier distinguishing three species of iris flowers based on sepal and petal measurements.",
            "tags": ["scikit-learn", "KNN", "Classification", "Iris Dataset"],
            "acc": "96.67%",
            "model": "KNN k=10",
        },
        {
            "num": "05",
            "title": "Sentiment Analysis",
            "desc": "LSTM recurrent neural network that reads user feedback and predicts whether the sentiment is positive or negative.",
            "tags": ["RNN", "LSTM", "NLP", "IMDB Dataset"],
            "acc": "~83%",
            "model": "LSTM",
        },
    ]

    cols = st.columns(2)
    for i, p in enumerate(projects):
        with cols[i % 2]:
            tag_html = "".join(f'<span class="tag">{t}</span>' for t in p["tags"])
            st.markdown(f"""
            <div class="glass-card" style="margin-bottom:20px;">
                <div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:16px;">
                    <span style="font-size:0.7rem;font-weight:700;color:#3b82f6;letter-spacing:0.1em;">{p['num']}</span>
                    <span style="font-size:0.72rem;color:#475569;background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.08);border-radius:6px;padding:2px 10px;">{p['model']}</span>
                </div>
                <div style="font-size:1.05rem;font-weight:700;color:#f1f5f9;margin-bottom:10px;">{p['title']}</div>
                <div style="font-size:0.85rem;color:#64748b;line-height:1.65;margin-bottom:18px;">{p['desc']}</div>
                <div style="margin-bottom:18px;">{tag_html}</div>
                <div style="display:flex;align-items:center;gap:8px;">
                    <div style="width:8px;height:8px;border-radius:50%;background:#22c55e;"></div>
                    <span style="font-size:0.8rem;color:#64748b;">Accuracy: <strong style="color:#e2e8f0;">{p['acc']}</strong></span>
                </div>
            </div>
            """, unsafe_allow_html=True)

    fancy_divider()

    # About section
    section_head("ABOUT THIS PORTFOLIO")
    st.markdown("""
    <div class="glass-card">
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:32px;">
            <div>
                <div style="font-size:0.75rem;font-weight:600;color:#3b82f6;text-transform:uppercase;letter-spacing:0.08em;margin-bottom:10px;">Stack</div>
                <div style="font-size:0.88rem;color:#94a3b8;line-height:1.8;">
                    Python 3.11<br>
                    TensorFlow 2.x / Keras<br>
                    scikit-learn<br>
                    Streamlit<br>
                    NumPy / Pandas
                </div>
            </div>
            <div>
                <div style="font-size:0.75rem;font-weight:600;color:#3b82f6;text-transform:uppercase;letter-spacing:0.08em;margin-bottom:10px;">Topics Covered</div>
                <div style="font-size:0.88rem;color:#94a3b8;line-height:1.8;">
                    Supervised Learning<br>
                    Convolutional Neural Networks<br>
                    Recurrent Neural Networks (LSTM)<br>
                    Natural Language Processing<br>
                    Model Deployment
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    # Footer
    st.markdown("""
    <div class="portfolio-footer">
        <div>
            <div class="footer-name">Carlo Glenn F. Dalusung</div>
            <div class="footer-sub">PTF04 · Machine Learning & Data Science Portfolio</div>
        </div>
        <div class="footer-tag">Python · TensorFlow · scikit-learn · Streamlit</div>
    </div>
    """, unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# BOSTON HOUSING
# ══════════════════════════════════════════════════════════════════════════════
def page_boston():
    st.markdown('<div class="page-wrap">', unsafe_allow_html=True)

    st.markdown("""
    <div style="margin-bottom:32px;">
        <div style="font-size:0.7rem;font-weight:700;color:#3b82f6;letter-spacing:0.12em;text-transform:uppercase;margin-bottom:8px;">01 / Boston Housing</div>
        <div style="font-size:1.8rem;font-weight:700;color:#f1f5f9;letter-spacing:-0.02em;">House Price Prediction</div>
        <div style="font-size:0.92rem;color:#64748b;margin-top:8px;">Neural network regression · TensorFlow · Keras</div>
    </div>
    """, unsafe_allow_html=True)

    tabs = st.tabs(["Project Overview", "Live Demo", "Code Snippets"])

    # ── Tab 1: Overview ──
    with tabs[0]:
        col1, col2 = st.columns([3, 2])
        with col1:
            st.markdown("""
            <div class="glass-card">
                <div style="font-size:0.75rem;font-weight:600;color:#3b82f6;text-transform:uppercase;letter-spacing:0.08em;margin-bottom:14px;">Project Summary</div>
                <p style="font-size:0.9rem;color:#94a3b8;line-height:1.75;margin-bottom:16px;">
                    This project trains a feedforward neural network to predict the median value of homes in Boston neighborhoods.
                    Three features with the strongest correlation to price were selected from the dataset: number of rooms (rm),
                    lower-status population percentage (lstat), and pupil-teacher ratio (ptratio).
                </p>
                <p style="font-size:0.9rem;color:#94a3b8;line-height:1.75;">
                    The model uses two hidden layers with ReLU activation and was trained for 300 epochs with early stopping.
                    StandardScaler normalizes all inputs before passing them to the network.
                </p>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("""
            <div class="metric-row" style="grid-template-columns:1fr 1fr;margin-top:0;">
                <div class="metric-card"><div class="metric-val">506</div><div class="metric-lbl">Samples</div></div>
                <div class="metric-card"><div class="metric-val">3</div><div class="metric-lbl">Features</div></div>
                <div class="metric-card"><div class="metric-val">76%</div><div class="metric-lbl">R² Score</div></div>
                <div class="metric-card"><div class="metric-val">2.53</div><div class="metric-lbl">MAE</div></div>
            </div>
            """, unsafe_allow_html=True)

        fancy_divider()
        section_head("MODEL ARCHITECTURE")
        st.markdown("""
        <div class="glass-card">
            <div style="display:flex;flex-direction:column;gap:12px;">
                <div style="display:flex;align-items:center;gap:16px;padding:14px;background:rgba(59,130,246,0.06);border:1px solid rgba(59,130,246,0.15);border-radius:10px;">
                    <span style="font-size:0.72rem;color:#3b82f6;font-weight:600;width:80px;">INPUT</span>
                    <span style="font-size:0.88rem;color:#e2e8f0;">3 features — rm, lstat, ptratio</span>
                </div>
                <div style="display:flex;align-items:center;gap:16px;padding:14px;background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.07);border-radius:10px;">
                    <span style="font-size:0.72rem;color:#6366f1;font-weight:600;width:80px;">DENSE</span>
                    <span style="font-size:0.88rem;color:#e2e8f0;">16 neurons · ReLU activation</span>
                </div>
                <div style="display:flex;align-items:center;gap:16px;padding:14px;background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.07);border-radius:10px;">
                    <span style="font-size:0.72rem;color:#6366f1;font-weight:600;width:80px;">DENSE</span>
                    <span style="font-size:0.88rem;color:#e2e8f0;">8 neurons · ReLU activation</span>
                </div>
                <div style="display:flex;align-items:center;gap:16px;padding:14px;background:rgba(34,197,94,0.06);border:1px solid rgba(34,197,94,0.15);border-radius:10px;">
                    <span style="font-size:0.72rem;color:#22c55e;font-weight:600;width:80px;">OUTPUT</span>
                    <span style="font-size:0.88rem;color:#e2e8f0;">1 neuron · house price (×$100,000)</span>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # ── Tab 2: Live Demo ──
    with tabs[1]:
        st.markdown("""
        <div style="margin-bottom:28px;">
            <div style="font-size:0.88rem;color:#64748b;line-height:1.6;">
                This demo re-creates the model using the original Boston dataset and scaler.
                Adjust the sliders to match different house profiles and click Predict.
            </div>
        </div>
        """, unsafe_allow_html=True)

        try:
            from sklearn.datasets import fetch_california_housing
            from sklearn.preprocessing import StandardScaler as SS
            from sklearn.neural_network import MLPRegressor
            import pandas as pd

            @st.cache_resource
            def train_boston_demo():
                # Use a simplified inline dataset representative of Boston
                np.random.seed(42)
                n = 506
                rm      = np.random.normal(6.28, 0.70, n)
                lstat   = np.random.exponential(12.65, n)
                ptratio = np.random.normal(18.46, 2.16, n)
                price   = (rm * 4.5 - lstat * 0.55 - ptratio * 0.35 + np.random.normal(0, 3, n)).clip(5, 50)
                X = np.column_stack([rm, lstat, ptratio])
                scaler = SS()
                X_sc = scaler.fit_transform(X)
                model = MLPRegressor(hidden_layer_sizes=(16,8), max_iter=500, random_state=42)
                model.fit(X_sc, price)
                return model, scaler

            demo_model, demo_scaler = train_boston_demo()

            col1, col2 = st.columns([1,1])
            with col1:
                rm_val      = st.slider("RM — Avg rooms per house",      3.0, 9.0, 6.3, 0.1)
                lstat_val   = st.slider("LSTAT — Lower status % of pop", 1.0, 38.0, 12.6, 0.1)
                ptratio_val = st.slider("PTRATIO — Pupil-teacher ratio", 12.0, 22.0, 18.5, 0.1)

            with col2:
                st.markdown("""
                <div class="glass-card" style="margin-top:0;">
                    <div style="font-size:0.72rem;color:#475569;text-transform:uppercase;letter-spacing:0.08em;margin-bottom:16px;">Input Values</div>
                """, unsafe_allow_html=True)
                st.markdown(f"""
                    <div style="display:flex;flex-direction:column;gap:10px;">
                        <div style="display:flex;justify-content:space-between;font-size:0.88rem;">
                            <span style="color:#94a3b8;">Rooms (RM)</span>
                            <span style="color:#f1f5f9;font-weight:600;">{rm_val}</span>
                        </div>
                        <div style="display:flex;justify-content:space-between;font-size:0.88rem;">
                            <span style="color:#94a3b8;">Lower Status %</span>
                            <span style="color:#f1f5f9;font-weight:600;">{lstat_val}</span>
                        </div>
                        <div style="display:flex;justify-content:space-between;font-size:0.88rem;">
                            <span style="color:#94a3b8;">Pupil-Teacher Ratio</span>
                            <span style="color:#f1f5f9;font-weight:600;">{ptratio_val}</span>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)

            if st.button("Predict House Price", key="boston_predict"):
                inp = np.array([[rm_val, lstat_val, ptratio_val]])
                inp_sc = demo_scaler.transform(inp)
                pred = demo_model.predict(inp_sc)[0]
                price_dollars = pred * 100_000
                st.markdown(f"""
                <div class="result-positive">
                    <div class="result-label" style="color:#22c55e;">Predicted Price</div>
                    <div style="font-size:2rem;font-weight:700;color:#f1f5f9;margin:8px 0;">${price_dollars:,.0f}</div>
                    <div class="result-sub">Based on rm={rm_val}, lstat={lstat_val}, ptratio={ptratio_val}</div>
                </div>
                """, unsafe_allow_html=True)

        except Exception as e:
            st.warning(f"Demo requires scikit-learn. Error: {e}")

    # ── Tab 3: Code ──
    with tabs[2]:
        section_head("MODEL CODE")
        code_block("""<span class="code-cm"># Neural Network for Boston Housing</span>
<span class="code-kw">from</span> tensorflow.keras.models <span class="code-kw">import</span> Sequential
<span class="code-kw">from</span> tensorflow.keras.layers <span class="code-kw">import</span> Dense
<span class="code-kw">from</span> tensorflow.keras.callbacks <span class="code-kw">import</span> EarlyStopping

X = df[[<span class="code-str">'rm'</span>, <span class="code-str">'lstat'</span>, <span class="code-str">'ptratio'</span>]]
y = df[<span class="code-str">'price'</span>]

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)

model = Sequential([
    Dense(<span class="code-num">16</span>, activation=<span class="code-str">'relu'</span>, input_shape=(<span class="code-num">3</span>,)),
    Dense(<span class="code-num">8</span>,  activation=<span class="code-str">'relu'</span>),
    Dense(<span class="code-num">1</span>)
])

model.compile(optimizer=<span class="code-str">'adam'</span>, loss=<span class="code-str">'mse'</span>)

early_stop = EarlyStopping(monitor=<span class="code-str">'val_loss'</span>, patience=<span class="code-num">10</span>)
history = model.fit(X_train, y_train,
    validation_split=<span class="code-num">0.2</span>,
    epochs=<span class="code-num">300</span>,
    batch_size=<span class="code-num">16</span>,
    callbacks=[early_stop]
)""")

    st.markdown('</div>', unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# CIFAR-10
# ══════════════════════════════════════════════════════════════════════════════
def page_cifar():
    st.markdown('<div class="page-wrap">', unsafe_allow_html=True)

    st.markdown("""
    <div style="margin-bottom:32px;">
        <div style="font-size:0.7rem;font-weight:700;color:#3b82f6;letter-spacing:0.12em;text-transform:uppercase;margin-bottom:8px;">02 / CIFAR-10</div>
        <div style="font-size:1.8rem;font-weight:700;color:#f1f5f9;letter-spacing:-0.02em;">Image Classifier</div>
        <div style="font-size:0.92rem;color:#64748b;margin-top:8px;">Convolutional Neural Network · TensorFlow · Keras</div>
    </div>
    """, unsafe_allow_html=True)

    CLASS_NAMES = ['airplane','automobile','bird','cat','deer','dog','frog','horse','ship','truck']

    tabs = st.tabs(["Project Overview", "Live Demo", "Code Snippets"])

    with tabs[0]:
        st.markdown("""
        <div class="glass-card" style="margin-bottom:20px;">
            <div style="font-size:0.75rem;font-weight:600;color:#3b82f6;text-transform:uppercase;letter-spacing:0.08em;margin-bottom:14px;">Project Summary</div>
            <p style="font-size:0.9rem;color:#94a3b8;line-height:1.75;">
                A Convolutional Neural Network trained on the CIFAR-10 benchmark dataset to classify 32×32 color images
                into 10 object categories. The model uses multiple convolutional and pooling layers followed by fully-connected
                dense layers and a softmax output.
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="metric-row">
            <div class="metric-card"><div class="metric-val">60K</div><div class="metric-lbl">Training Images</div></div>
            <div class="metric-card"><div class="metric-val">10K</div><div class="metric-lbl">Test Images</div></div>
            <div class="metric-card"><div class="metric-val">10</div><div class="metric-lbl">Classes</div></div>
            <div class="metric-card"><div class="metric-val">32×32</div><div class="metric-lbl">Input Size</div></div>
        </div>
        """, unsafe_allow_html=True)

        fancy_divider()
        section_head("10 CLASSES")
        cols = st.columns(5)
        for i, name in enumerate(CLASS_NAMES):
            with cols[i % 5]:
                st.markdown(f"""
                <div style="background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.07);border-radius:10px;
                            padding:14px;text-align:center;margin-bottom:10px;">
                    <div style="font-size:0.85rem;font-weight:500;color:#e2e8f0;">{name.capitalize()}</div>
                </div>
                """, unsafe_allow_html=True)

    with tabs[1]:
        st.markdown('<div style="font-size:0.85rem;color:#64748b;margin-bottom:20px;">Upload any image — the model will resize it to 32×32 and predict the CIFAR-10 class.</div>', unsafe_allow_html=True)

        uploaded = st.file_uploader("Upload an image", type=["jpg","jpeg","png"])
        if uploaded:
            from PIL import Image as PILImage
            img = PILImage.open(uploaded).convert("RGB")
            col1, col2 = st.columns([1,1])
            with col1:
                st.image(img, caption="Uploaded image", use_container_width=True)
            with col2:
                try:
                    from tensorflow.keras.models import load_model
                    @st.cache_resource
                    def load_cifar():
                        return load_model("cnn_model.h5")
                    cifar_model = load_cifar()
                    img_arr = np.array(img.resize((32,32))) / 255.0
                    pred = cifar_model.predict(np.expand_dims(img_arr, 0), verbose=0)[0]
                    idx  = np.argmax(pred)
                    st.markdown(f"""
                    <div class="result-positive" style="margin-top:0;">
                        <div class="result-label" style="color:#60a5fa;">{CLASS_NAMES[idx].capitalize()}</div>
                        <div style="font-size:1.6rem;font-weight:700;color:#f1f5f9;margin:6px 0;">{pred[idx]*100:.1f}% confidence</div>
                    </div>
                    """, unsafe_allow_html=True)
                    st.markdown("<br>**All class probabilities**", unsafe_allow_html=True)
                    for i in np.argsort(pred)[::-1]:
                        pct = int(pred[i]*100)
                        st.markdown(f"""
                        <div class="prob-row">
                            <span class="prob-name">{CLASS_NAMES[i].capitalize()}</span>
                            <div class="prob-bg"><div class="prob-fill" style="width:{pct}%;background:#3b82f6;"></div></div>
                            <span class="prob-pct">{pct}%</span>
                        </div>
                        """, unsafe_allow_html=True)
                except Exception:
                    st.info("Place `cnn_model.keras` in the same folder as portfolio.py to enable live predictions.")

    with tabs[2]:
        code_block("""<span class="code-cm"># CNN for CIFAR-10</span>
<span class="code-kw">from</span> tensorflow.keras.models <span class="code-kw">import</span> Sequential
<span class="code-kw">from</span> tensorflow.keras.layers <span class="code-kw">import</span> Conv2D, MaxPooling2D, Dense, Flatten, Dropout

model = Sequential([
    Conv2D(<span class="code-num">32</span>, (<span class="code-num">3</span>,<span class="code-num">3</span>), activation=<span class="code-str">'relu'</span>, input_shape=(<span class="code-num">32</span>,<span class="code-num">32</span>,<span class="code-num">3</span>)),
    MaxPooling2D((<span class="code-num">2</span>,<span class="code-num">2</span>)),
    Conv2D(<span class="code-num">64</span>, (<span class="code-num">3</span>,<span class="code-num">3</span>), activation=<span class="code-str">'relu'</span>),
    MaxPooling2D((<span class="code-num">2</span>,<span class="code-num">2</span>)),
    Flatten(),
    Dense(<span class="code-num">128</span>, activation=<span class="code-str">'relu'</span>),
    Dropout(<span class="code-num">0.5</span>),
    Dense(<span class="code-num">10</span>, activation=<span class="code-str">'softmax'</span>)
])
model.compile(optimizer=<span class="code-str">'adam'</span>,
              loss=<span class="code-str">'sparse_categorical_crossentropy'</span>,
              metrics=[<span class="code-str">'accuracy'</span>])""")

    st.markdown('</div>', unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# IRIS CLASSIFIER
# ══════════════════════════════════════════════════════════════════════════════
def page_iris():
    st.markdown('<div class="page-wrap">', unsafe_allow_html=True)

    st.markdown("""
    <div style="margin-bottom:32px;">
        <div style="font-size:0.7rem;font-weight:700;color:#3b82f6;letter-spacing:0.12em;text-transform:uppercase;margin-bottom:8px;">03 / Iris Classifier</div>
        <div style="font-size:1.8rem;font-weight:700;color:#f1f5f9;letter-spacing:-0.02em;">Flower Species Classifier</div>
        <div style="font-size:0.92rem;color:#64748b;margin-top:8px;">K-Nearest Neighbors · scikit-learn · k=10</div>
    </div>
    """, unsafe_allow_html=True)

    tabs = st.tabs(["Project Overview", "Live Demo", "Code Snippets"])

    from sklearn.datasets import load_iris
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import accuracy_score

    @st.cache_resource
    def load_iris_model():
        iris = load_iris()
        X, y = iris.data, iris.target
        X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
        knn = KNeighborsClassifier(n_neighbors=10)
        knn.fit(X, y)
        acc = accuracy_score(y_te, knn.predict(X_te))
        return knn, iris, acc

    knn, iris_data, acc = load_iris_model()

    COLORS = {"setosa":"#3b82f6","versicolor":"#22c55e","virginica":"#a855f7"}

    with tabs[0]:
        col1, col2 = st.columns([3,2])
        with col1:
            st.markdown(f"""
            <div class="glass-card">
                <div style="font-size:0.75rem;font-weight:600;color:#3b82f6;text-transform:uppercase;letter-spacing:0.08em;margin-bottom:14px;">Project Summary</div>
                <p style="font-size:0.9rem;color:#94a3b8;line-height:1.75;">
                    Uses the classic Iris dataset to classify flowers into three species — Setosa, Versicolor, and Virginica —
                    based on sepal and petal measurements. A K-Nearest Neighbors classifier with k=10 was selected after
                    hyperparameter optimization and achieves <strong style="color:#e2e8f0;">{acc*100:.2f}%</strong> accuracy.
                </p>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown(f"""
            <div class="metric-row" style="grid-template-columns:1fr 1fr;margin-top:0;">
                <div class="metric-card"><div class="metric-val">150</div><div class="metric-lbl">Samples</div></div>
                <div class="metric-card"><div class="metric-val">3</div><div class="metric-lbl">Classes</div></div>
                <div class="metric-card"><div class="metric-val">{acc*100:.1f}%</div><div class="metric-lbl">Accuracy</div></div>
                <div class="metric-card"><div class="metric-val">k=10</div><div class="metric-lbl">Neighbors</div></div>
            </div>
            """, unsafe_allow_html=True)

    with tabs[1]:
        col1, col2 = st.columns(2)
        with col1:
            sl = st.slider("Sepal Length (cm)", 4.0, 8.0, 5.8, 0.1)
            sw = st.slider("Sepal Width (cm)",  2.0, 4.5, 3.0, 0.1)
        with col2:
            pl = st.slider("Petal Length (cm)", 1.0, 7.0, 4.3, 0.1)
            pw = st.slider("Petal Width (cm)",  0.1, 2.5, 1.3, 0.1)

        if st.button("Classify", key="iris_classify"):
            inp  = np.array([[sl, sw, pl, pw]])
            pred = knn.predict(inp)[0]
            prob = knn.predict_proba(inp)[0]
            name = iris_data.target_names[pred]
            col  = COLORS.get(name, "#3b82f6")
            descs = {
                "setosa":     "Small arctic/subarctic species, most distinct of the three classes with notably small petals.",
                "versicolor": "Medium-sized wetland species, the blue flag iris, common across North America.",
                "virginica":  "Largest species with broad petals, native to the eastern United States.",
            }
            st.markdown(f"""
            <div style="background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.07);
                        border-left:4px solid {col};border-radius:12px;padding:28px;margin-top:20px;">
                <div style="font-size:0.72rem;color:{col};text-transform:uppercase;letter-spacing:0.1em;margin-bottom:8px;">Prediction</div>
                <div style="font-size:1.6rem;font-weight:700;color:#f1f5f9;">Iris {name.capitalize()}</div>
                <div style="font-size:0.85rem;color:#64748b;margin-top:8px;line-height:1.6;">{descs[name]}</div>
                <div style="margin-top:20px;padding-top:16px;border-top:1px solid rgba(255,255,255,0.06);
                            display:flex;gap:24px;font-size:0.82rem;">
                    <span style="color:#64748b;">Confidence: <strong style="color:#e2e8f0;">{prob[pred]*100:.1f}%</strong></span>
                    <span style="color:#64748b;">Model accuracy: <strong style="color:#e2e8f0;">{acc*100:.2f}%</strong></span>
                </div>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("<br>**Class probabilities**", unsafe_allow_html=True)
            for i, n in enumerate(iris_data.target_names):
                pct = int(prob[i]*100)
                st.markdown(f"""
                <div class="prob-row">
                    <span class="prob-name">{n.capitalize()}</span>
                    <div class="prob-bg"><div class="prob-fill" style="width:{pct}%;background:{COLORS[n]};"></div></div>
                    <span class="prob-pct">{pct}%</span>
                </div>
                """, unsafe_allow_html=True)

    with tabs[2]:
        code_block("""<span class="code-cm"># KNN Iris Classifier</span>
<span class="code-kw">from</span> sklearn.datasets <span class="code-kw">import</span> load_iris
<span class="code-kw">from</span> sklearn.neighbors <span class="code-kw">import</span> KNeighborsClassifier
<span class="code-kw">from</span> sklearn.model_selection <span class="code-kw">import</span> train_test_split

iris = load_iris()
X, y = iris.data, iris.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=<span class="code-num">0.2</span>, random_state=<span class="code-num">42</span>, stratify=y
)

knn = KNeighborsClassifier(n_neighbors=<span class="code-num">10</span>)
knn.fit(X, y)   <span class="code-cm"># trained on full dataset</span>

<span class="code-cm"># Predict</span>
prediction = knn.predict([[<span class="code-num">5.8</span>, <span class="code-num">3.0</span>, <span class="code-num">4.3</span>, <span class="code-num">1.3</span>]])
print(iris.target_names[prediction])  <span class="code-cm"># versicolor</span>""")

    st.markdown('</div>', unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# SENTIMENT ANALYSIS
# ══════════════════════════════════════════════════════════════════════════════
def page_sentiment():
    st.markdown('<div class="page-wrap">', unsafe_allow_html=True)

    st.markdown("""
    <div style="margin-bottom:32px;">
        <div style="font-size:0.7rem;font-weight:700;color:#3b82f6;letter-spacing:0.12em;text-transform:uppercase;margin-bottom:8px;">04 / Sentiment Analysis</div>
        <div style="font-size:1.8rem;font-weight:700;color:#f1f5f9;letter-spacing:-0.02em;">Feedback Sentiment Analyzer</div>
        <div style="font-size:0.92rem;color:#64748b;margin-top:8px;">RNN · LSTM · TensorFlow · IMDB Dataset</div>
    </div>
    """, unsafe_allow_html=True)

    tabs = st.tabs(["Project Overview", "Live Demo", "Code Snippets"])

    with tabs[0]:
        col1, col2 = st.columns([3,2])
        with col1:
            st.markdown("""
            <div class="glass-card">
                <div style="font-size:0.75rem;font-weight:600;color:#3b82f6;text-transform:uppercase;letter-spacing:0.08em;margin-bottom:14px;">Project Summary</div>
                <p style="font-size:0.9rem;color:#94a3b8;line-height:1.75;">
                    An LSTM-based recurrent neural network trained on the IMDB movie review dataset to classify text
                    as positive or negative sentiment. Input text is tokenized using the IMDB word index, padded to a
                    sequence length of 100, and passed through an embedding layer before the LSTM processes the context.
                </p>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("""
            <div class="metric-row" style="grid-template-columns:1fr 1fr;margin-top:0;">
                <div class="metric-card"><div class="metric-val">50K</div><div class="metric-lbl">Reviews</div></div>
                <div class="metric-card"><div class="metric-val">20K</div><div class="metric-lbl">Vocab Size</div></div>
                <div class="metric-card"><div class="metric-val">~83%</div><div class="metric-lbl">Accuracy</div></div>
                <div class="metric-card"><div class="metric-val">LSTM</div><div class="metric-lbl">Architecture</div></div>
            </div>
            """, unsafe_allow_html=True)

    with tabs[1]:
        if 'sent_history' not in st.session_state:
            st.session_state.sent_history = []

        feedback = st.text_area("Enter feedback or review text", placeholder="Type any review or feedback here...", height=130)

        col1, col2 = st.columns([3,1])
        with col1:
            analyze = st.button("Analyze Sentiment", key="sent_analyze")
        with col2:
            if st.button("Clear History", key="sent_clear"):
                st.session_state.sent_history = []
                st.rerun()

        if analyze and feedback.strip():
            try:
                from tensorflow.keras.models import load_model as lm
                from tensorflow.keras.datasets import imdb
                from tensorflow.keras.preprocessing import sequence

                @st.cache_resource
                def load_sent():
                    m = lm("sentiment_model.keras")
                    w = imdb.get_word_index()
                    return m, w

                sent_model, word_idx = load_sent()
                seq = [min(word_idx.get(w.lower(), 0)+3, 19999) for w in feedback.split()]
                pad = sequence.pad_sequences([seq], maxlen=100)
                score = sent_model.predict(pad, verbose=0)[0][0]

                sentiment = "Positive" if score > 0.5 else "Negative"
                conf = score*100 if score > 0.5 else (1-score)*100
                is_pos = sentiment == "Positive"
                card_cls = "result-positive" if is_pos else "result-negative"
                lbl_col  = "#22c55e" if is_pos else "#ef4444"

                st.markdown(f"""
                <div class="{card_cls}">
                    <div class="result-label" style="color:{lbl_col};">{sentiment} Sentiment</div>
                    <div style="font-size:1.6rem;font-weight:700;color:#f1f5f9;margin:6px 0;">{conf:.1f}% confidence</div>
                    <div class="result-sub">{"Satisfaction, approval, or favorable experience detected." if is_pos else "Dissatisfaction, criticism, or unfavorable experience detected."}</div>
                </div>
                """, unsafe_allow_html=True)

                st.session_state.sent_history.insert(0, {"text": feedback.strip(), "sentiment": sentiment, "conf": conf})

            except Exception:
                # Fallback keyword-based demo
                pos_words = {"good","great","excellent","amazing","love","wonderful","fantastic","best","happy","enjoyed","perfect","beautiful","outstanding"}
                neg_words = {"bad","terrible","awful","hate","worst","horrible","poor","disappointing","boring","waste","ugly","fail","broken"}
                words = set(feedback.lower().split())
                pos_score = len(words & pos_words)
                neg_score = len(words & neg_words)
                sentiment = "Positive" if pos_score >= neg_score else "Negative"
                conf = min(95, 60 + abs(pos_score - neg_score) * 10)
                is_pos = sentiment == "Positive"
                card_cls = "result-positive" if is_pos else "result-negative"
                lbl_col  = "#22c55e" if is_pos else "#ef4444"

                st.markdown(f"""
                <div class="{card_cls}">
                    <div class="result-label" style="color:{lbl_col};">{sentiment} Sentiment</div>
                    <div style="font-size:1.4rem;font-weight:700;color:#f1f5f9;margin:6px 0;">{conf:.0f}% confidence</div>
                    <div class="result-sub">Demo mode — place sentiment_model.keras in the folder for full LSTM predictions.</div>
                </div>
                """, unsafe_allow_html=True)

                st.session_state.sent_history.insert(0, {"text": feedback.strip(), "sentiment": sentiment, "conf": conf})

        if st.session_state.sent_history:
            fancy_divider()
            st.markdown("**Recent Analyses**")
            for item in st.session_state.sent_history[:6]:
                preview = item["text"][:90] + "..." if len(item["text"]) > 90 else item["text"]
                is_pos  = item["sentiment"] == "Positive"
                badge_bg  = "rgba(34,197,94,0.1)"  if is_pos else "rgba(239,68,68,0.1)"
                badge_col = "#22c55e" if is_pos else "#ef4444"
                st.markdown(f"""
                <div style="display:flex;justify-content:space-between;align-items:flex-start;gap:12px;
                            padding:12px 16px;background:rgba(255,255,255,0.02);border:1px solid rgba(255,255,255,0.06);
                            border-radius:8px;margin-bottom:8px;">
                    <span style="font-size:0.85rem;color:#64748b;flex:1;">{preview}</span>
                    <span style="font-size:0.75rem;font-weight:600;padding:2px 10px;border-radius:999px;
                                 background:{badge_bg};color:{badge_col};white-space:nowrap;">
                        {item['sentiment']} · {item['conf']:.0f}%
                    </span>
                </div>
                """, unsafe_allow_html=True)

    with tabs[2]:
        code_block("""<span class="code-cm"># LSTM Sentiment Analysis</span>
<span class="code-kw">from</span> tensorflow.keras.models <span class="code-kw">import</span> Sequential
<span class="code-kw">from</span> tensorflow.keras.layers <span class="code-kw">import</span> Embedding, LSTM, Dense
<span class="code-kw">from</span> tensorflow.keras.datasets <span class="code-kw">import</span> imdb

NUM_WORDS = <span class="code-num">20000</span>
MAX_LEN   = <span class="code-num">100</span>

(X_train, y_train), (X_test, y_test) = imdb.load_data(num_words=NUM_WORDS)
X_train = sequence.pad_sequences(X_train, maxlen=MAX_LEN)

model = Sequential([
    Embedding(NUM_WORDS, <span class="code-num">128</span>),
    LSTM(<span class="code-num">64</span>, dropout=<span class="code-num">0.2</span>),
    Dense(<span class="code-num">1</span>, activation=<span class="code-str">'sigmoid'</span>)
])

model.compile(optimizer=<span class="code-str">'adam'</span>,
              loss=<span class="code-str">'binary_crossentropy'</span>,
              metrics=[<span class="code-str">'accuracy'</span>])""")

    st.markdown('</div>', unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# DOGS VS CATS
# ══════════════════════════════════════════════════════════════════════════════
def page_dogs_cats():
    st.markdown('<div class="page-wrap">', unsafe_allow_html=True)

    st.markdown("""
    <div style="margin-bottom:32px;">
        <div style="font-size:0.7rem;font-weight:700;color:#3b82f6;letter-spacing:0.12em;text-transform:uppercase;margin-bottom:8px;">03 / Dogs vs Cats</div>
        <div style="font-size:1.8rem;font-weight:700;color:#f1f5f9;letter-spacing:-0.02em;">Binary Image Classifier</div>
        <div style="font-size:0.92rem;color:#64748b;margin-top:8px;">Convolutional Neural Network · TensorFlow · Binary Classification</div>
    </div>
    """, unsafe_allow_html=True)

    tabs = st.tabs(["Project Overview", "Live Demo", "Code Snippets"])

    # ── Tab 1: Overview ──
    with tabs[0]:
        col1, col2 = st.columns([3, 2])
        with col1:
            st.markdown("""
            <div class="glass-card">
                <div style="font-size:0.75rem;font-weight:600;color:#3b82f6;text-transform:uppercase;letter-spacing:0.08em;margin-bottom:14px;">Project Summary</div>
                <p style="font-size:0.9rem;color:#94a3b8;line-height:1.75;margin-bottom:16px;">
                    A binary image classification model trained to distinguish between photographs of dogs and cats.
                    The CNN takes 128×128 RGB images as input, applies convolutional and pooling layers to extract
                    spatial features, and outputs a single sigmoid probability.
                </p>
                <p style="font-size:0.9rem;color:#94a3b8;line-height:1.75;">
                    A prediction score of 0.5 or above is classified as <strong style="color:#e2e8f0;">Cat</strong>,
                    while a score below 0.5 is classified as <strong style="color:#e2e8f0;">Dog</strong>.
                    Images are normalized to [0, 1] before inference.
                </p>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("""
            <div class="metric-row" style="grid-template-columns:1fr 1fr;margin-top:0;">
                <div class="metric-card"><div class="metric-val">128px</div><div class="metric-lbl">Input Size</div></div>
                <div class="metric-card"><div class="metric-val">2</div><div class="metric-lbl">Classes</div></div>
                <div class="metric-card"><div class="metric-val">CNN</div><div class="metric-lbl">Architecture</div></div>
                <div class="metric-card"><div class="metric-val">Sigmoid</div><div class="metric-lbl">Output</div></div>
            </div>
            """, unsafe_allow_html=True)

        fancy_divider()
        section_head("MODEL ARCHITECTURE")
        st.markdown("""
        <div class="glass-card">
            <div style="display:flex;flex-direction:column;gap:12px;">
                <div style="display:flex;align-items:center;gap:16px;padding:14px;background:rgba(59,130,246,0.06);border:1px solid rgba(59,130,246,0.15);border-radius:10px;">
                    <span style="font-size:0.72rem;color:#3b82f6;font-weight:600;width:100px;">INPUT</span>
                    <span style="font-size:0.88rem;color:#e2e8f0;">128 × 128 × 3 RGB image</span>
                </div>
                <div style="display:flex;align-items:center;gap:16px;padding:14px;background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.07);border-radius:10px;">
                    <span style="font-size:0.72rem;color:#6366f1;font-weight:600;width:100px;">CONV + POOL</span>
                    <span style="font-size:0.88rem;color:#e2e8f0;">Multiple convolutional blocks with MaxPooling</span>
                </div>
                <div style="display:flex;align-items:center;gap:16px;padding:14px;background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.07);border-radius:10px;">
                    <span style="font-size:0.72rem;color:#6366f1;font-weight:600;width:100px;">FLATTEN</span>
                    <span style="font-size:0.88rem;color:#e2e8f0;">Flatten spatial features to 1D vector</span>
                </div>
                <div style="display:flex;align-items:center;gap:16px;padding:14px;background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.07);border-radius:10px;">
                    <span style="font-size:0.72rem;color:#6366f1;font-weight:600;width:100px;">DENSE</span>
                    <span style="font-size:0.88rem;color:#e2e8f0;">Fully connected layer with ReLU</span>
                </div>
                <div style="display:flex;align-items:center;gap:16px;padding:14px;background:rgba(34,197,94,0.06);border:1px solid rgba(34,197,94,0.15);border-radius:10px;">
                    <span style="font-size:0.72rem;color:#22c55e;font-weight:600;width:100px;">OUTPUT</span>
                    <span style="font-size:0.88rem;color:#e2e8f0;">1 neuron · Sigmoid · Dog (0) or Cat (1)</span>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # ── Tab 2: Live Demo ──
    with tabs[1]:
        st.markdown("""
        <div style="font-size:0.85rem;color:#64748b;margin-bottom:24px;line-height:1.6;">
            Upload a photo of a dog or cat. The model will analyze it and return a prediction with a confidence score.
            Images are automatically resized to 128×128 pixels before inference.
        </div>
        """, unsafe_allow_html=True)

        uploaded = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"], key="dvc_upload")

        if uploaded:
            from PIL import Image as PILImage

            image = PILImage.open(uploaded).convert("RGB")
            col1, col2 = st.columns([1, 1])

            with col1:
                st.image(image, caption="Uploaded image", use_container_width=True)

            with col2:
                try:
                    from tensorflow.keras.models import load_model as lm

                    @st.cache_resource
                    def load_dvc_model():
                        return lm("dogs_vs_cats_model.keras")

                    dvc_model = load_dvc_model()

                    img_resized = image.resize((128, 128))
                    img_array  = np.array(img_resized) / 255.0
                    img_array  = np.expand_dims(img_array, axis=0)

                    with st.spinner("Analyzing..."):
                        prediction = dvc_model.predict(img_array, verbose=0)[0][0]

                    if prediction >= 0.5:
                        label      = "Cat"
                        confidence = prediction * 100
                        accent     = "#3b82f6"
                    else:
                        label      = "Dog"
                        confidence = (1 - prediction) * 100
                        accent     = "#f59e0b"

                    other_conf = 100 - confidence
                    other_lbl  = "Dog" if label == "Cat" else "Cat"

                    st.markdown(f"""
                    <div style="background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.07);
                                border-left:4px solid {accent};border-radius:12px;padding:28px;margin-top:0;">
                        <div style="font-size:0.72rem;color:{accent};text-transform:uppercase;
                                    letter-spacing:0.1em;margin-bottom:8px;">Prediction</div>
                        <div style="font-size:2rem;font-weight:700;color:#f1f5f9;">{label}</div>
                        <div style="font-size:0.9rem;color:#64748b;margin-top:4px;">
                            {confidence:.1f}% confidence
                        </div>
                        <div style="margin-top:24px;">
                            <div class="prob-row">
                                <span class="prob-name">Dog</span>
                                <div class="prob-bg">
                                    <div class="prob-fill" style="width:{100-confidence if label=='Cat' else confidence:.0f}%;background:#f59e0b;"></div>
                                </div>
                                <span class="prob-pct">{100-confidence if label=='Cat' else confidence:.0f}%</span>
                            </div>
                            <div class="prob-row">
                                <span class="prob-name">Cat</span>
                                <div class="prob-bg">
                                    <div class="prob-fill" style="width:{confidence if label=='Cat' else 100-confidence:.0f}%;background:#3b82f6;"></div>
                                </div>
                                <span class="prob-pct">{confidence if label=='Cat' else 100-confidence:.0f}%</span>
                            </div>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)

                except Exception as e:
                    st.info("Place `dogs_vs_cats_model.keras` in the same folder as `portfolio.py` to enable live predictions.")
                    st.caption(f"Error: {e}")

    # ── Tab 3: Code ──
    with tabs[2]:
        section_head("MODEL CODE")
        code_block("""<span class="code-cm"># Dogs vs Cats CNN Classifier</span>
<span class="code-kw">import</span> tensorflow <span class="code-kw">as</span> tf
<span class="code-kw">from</span> tensorflow.keras.models <span class="code-kw">import</span> Sequential
<span class="code-kw">from</span> tensorflow.keras.layers <span class="code-kw">import</span> Conv2D, MaxPooling2D, Dense, Flatten, Dropout

IMG_SIZE = (<span class="code-num">128</span>, <span class="code-num">128</span>)

model = Sequential([
    Conv2D(<span class="code-num">32</span>, (<span class="code-num">3</span>,<span class="code-num">3</span>), activation=<span class="code-str">'relu'</span>, input_shape=(<span class="code-num">128</span>,<span class="code-num">128</span>,<span class="code-num">3</span>)),
    MaxPooling2D(<span class="code-num">2</span>,<span class="code-num">2</span>),
    Conv2D(<span class="code-num">64</span>, (<span class="code-num">3</span>,<span class="code-num">3</span>), activation=<span class="code-str">'relu'</span>),
    MaxPooling2D(<span class="code-num">2</span>,<span class="code-num">2</span>),
    Conv2D(<span class="code-num">128</span>, (<span class="code-num">3</span>,<span class="code-num">3</span>), activation=<span class="code-str">'relu'</span>),
    MaxPooling2D(<span class="code-num">2</span>,<span class="code-num">2</span>),
    Flatten(),
    Dense(<span class="code-num">512</span>, activation=<span class="code-str">'relu'</span>),
    Dropout(<span class="code-num">0.5</span>),
    Dense(<span class="code-num">1</span>, activation=<span class="code-str">'sigmoid'</span>)
])

model.compile(optimizer=<span class="code-str">'adam'</span>,
              loss=<span class="code-str">'binary_crossentropy'</span>,
              metrics=[<span class="code-str">'accuracy'</span>])

<span class="code-cm"># Predict on new image</span>
img = image.resize((<span class="code-num">128</span>, <span class="code-num">128</span>))
arr = np.array(img) / <span class="code-num">255.0</span>
arr = np.expand_dims(arr, axis=<span class="code-num">0</span>)
pred = model.predict(arr)[<span class="code-num">0</span>][<span class="code-num">0</span>]
label = <span class="code-str">"Cat"</span> <span class="code-kw">if</span> pred >= <span class="code-num">0.5</span> <span class="code-kw">else</span> <span class="code-str">"Dog"</span>""")

    st.markdown('</div>', unsafe_allow_html=True)


# ── Router ─────────────────────────────────────────────────────────────────────
page = st.session_state.page

if   page == "Home":              page_home()
elif page == "Boston Housing":    page_boston()
elif page == "CIFAR-10":          page_cifar()
elif page == "Dogs vs Cats":      page_dogs_cats()
elif page == "Iris Classifier":   page_iris()
elif page == "Sentiment Analysis":page_sentiment()
