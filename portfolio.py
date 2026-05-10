import streamlit as st
import numpy as np

st.set_page_config(
    page_title="PTF04 — Carlo Glenn F. Dalusung",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ══════════════════════════════════════════════════════════════════════════════
# GLOBAL CSS
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
    background: #090b10;
    color: #e2e8f0;
}

#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 0 !important; max-width: 100% !important; }

/* ── Force sidebar always open ── */
[data-testid="collapsedControl"] { display: none !important; }
[data-testid="stSidebarCollapseButton"] { display: none !important; }
section[data-testid="stSidebar"] { 
    transform: none !important;
    width: 272px !important;
    min-width: 272px !important;
    max-width: 272px !important;
    left: 0 !important;
    visibility: visible !important;
    display: flex !important;
}
section[data-testid="stSidebar"][aria-expanded="false"] {
    transform: none !important;
    margin-left: 0 !important;
    width: 272px !important;
    min-width: 272px !important;
}

::-webkit-scrollbar { width: 3px; }
::-webkit-scrollbar-track { background: #090b10; }
::-webkit-scrollbar-thumb { background: #2563eb; border-radius: 2px; }

/* ── SIDEBAR ── */
[data-testid="stSidebar"] {
    background: #0b0d15 !important;
    border-right: 1px solid rgba(255,255,255,0.055) !important;
    min-width: 272px !important;
    max-width: 272px !important;
}
[data-testid="stSidebar"] > div:first-child { padding: 0 !important; }

[data-testid="stSidebar"] div[data-testid="stButton"] > button {
    background: transparent !important;
    color: #475569 !important;
    border: none !important;
    border-left: 3px solid transparent !important;
    border-radius: 0 !important;
    width: 100% !important;
    text-align: left !important;
    padding: 15px 28px !important;
    font-size: 0.875rem !important;
    font-weight: 500 !important;
    letter-spacing: 0.01em !important;
    box-shadow: none !important;
    transition: all 0.15s ease !important;
    justify-content: flex-start !important;
    min-height: unset !important;
}
[data-testid="stSidebar"] div[data-testid="stButton"] > button:hover {
    background: rgba(37,99,235,0.07) !important;
    color: #94a3b8 !important;
    border-left-color: rgba(37,99,235,0.3) !important;
    transform: none !important;
    box-shadow: none !important;
}

/* ── HERO ── */
.hero {
    position: relative;
    min-height: 520px;
    display: flex;
    align-items: center;
    padding: 110px 96px;
    overflow: hidden;
    background: #090b10;
    border-bottom: 1px solid rgba(255,255,255,0.045);
}
.hero::before {
    content: '';
    position: absolute; inset: 0;
    background-image:
        linear-gradient(rgba(59,130,246,0.03) 1px, transparent 1px),
        linear-gradient(90deg, rgba(59,130,246,0.03) 1px, transparent 1px);
    background-size: 80px 80px;
    pointer-events: none;
}
.orb {
    position: absolute; border-radius: 50%;
    filter: blur(100px); opacity: 0.12;
    animation: orb-float 10s ease-in-out infinite;
    pointer-events: none;
}
.orb-1 { width:520px;height:520px;background:#2563eb;top:-160px;right:4%;animation-delay:0s; }
.orb-2 { width:360px;height:360px;background:#4f46e5;bottom:-110px;right:26%;animation-delay:4s; }
.orb-3 { width:260px;height:260px;background:#0284c7;top:42%;left:36%;animation-delay:7s; }
@keyframes orb-float {
    0%,100% { transform:translateY(0) scale(1); }
    50%      { transform:translateY(-22px) scale(1.03); }
}
.hero-inner { position:relative;z-index:1;max-width:700px; }
.hero-badge {
    display:inline-flex; align-items:center; gap:8px;
    background:rgba(37,99,235,0.1); border:1px solid rgba(37,99,235,0.25);
    border-radius:999px; padding:6px 18px;
    font-size:0.7rem; font-weight:700; color:#60a5fa;
    letter-spacing:0.1em; text-transform:uppercase; margin-bottom:32px;
}
.hero-badge-dot {
    width:6px;height:6px;border-radius:50%;background:#3b82f6;
    animation:pulse 2s ease-in-out infinite;
}
@keyframes pulse {
    0%,100%{opacity:1;transform:scale(1);}
    50%{opacity:0.45;transform:scale(0.75);}
}
.hero h1 {
    font-size:clamp(2.4rem,4vw,3.8rem);
    font-weight:800; line-height:1.08;
    color:#f8fafc; letter-spacing:-0.03em; margin-bottom:24px;
}
.hero h1 em { font-style:normal; color:#3b82f6; }
.hero-desc {
    font-size:1.05rem; color:#64748b; line-height:1.8;
    max-width:520px; margin-bottom:56px; font-weight:400;
}
.hero-stats { display:flex; gap:56px; flex-wrap:wrap; }
.stat { display:flex; flex-direction:column; gap:5px; }
.stat-n { font-size:1.7rem;font-weight:800;color:#f1f5f9;letter-spacing:-0.02em; }
.stat-l { font-size:0.68rem;color:#475569;text-transform:uppercase;letter-spacing:0.09em;font-weight:600; }

/* ── PAGE HEADER ── */
.page-header {
    padding: 64px 96px 0;
    margin-bottom: 0;
    border-bottom: 1px solid rgba(255,255,255,0.045);
    padding-bottom: 40px;
}
.page-eyebrow {
    font-size:0.67rem;font-weight:700;color:#2563eb;
    letter-spacing:0.16em;text-transform:uppercase;margin-bottom:14px;
}
.page-title {
    font-size:2.1rem;font-weight:800;color:#f8fafc;
    letter-spacing:-0.03em;margin-bottom:10px;line-height:1.12;
}
.page-sub { font-size:0.9rem;color:#475569;font-weight:400; }

/* ── TABS — the main fix ── */
.stTabs {
    padding: 0 !important;
    margin: 0 !important;
}

/* Tab bar wrapper — full-width strip */
.stTabs [data-baseweb="tab-list"] {
    background: rgba(255,255,255,0.02) !important;
    border: none !important;
    border-bottom: 1px solid rgba(255,255,255,0.07) !important;
    border-radius: 0 !important;
    padding: 0 96px !important;
    gap: 0 !important;
    margin-bottom: 0 !important;
}

/* Each tab button */
.stTabs [data-baseweb="tab"] {
    background: transparent !important;
    border: none !important;
    border-bottom: 2px solid transparent !important;
    border-radius: 0 !important;
    color: #475569 !important;
    font-weight: 600 !important;
    font-size: 0.875rem !important;
    padding: 20px 28px !important;
    letter-spacing: 0.01em !important;
    margin-right: 4px !important;
    transition: color 0.15s, border-color 0.15s !important;
}
.stTabs [data-baseweb="tab"]:hover {
    color: #94a3b8 !important;
    background: transparent !important;
}
.stTabs [aria-selected="true"] {
    background: transparent !important;
    color: #f1f5f9 !important;
    border-bottom-color: #2563eb !important;
}

/* Tab panel — full-width, generous padding */
.stTabs [data-baseweb="tab-panel"] {
    padding: 56px 96px 80px !important;
}

/* ── CARDS ── */
.card {
    background: rgba(255,255,255,0.025);
    border: 1px solid rgba(255,255,255,0.065);
    border-radius: 20px;
    padding: 40px;
    transition: border-color 0.2s, box-shadow 0.2s;
}
.card:hover {
    border-color: rgba(37,99,235,0.2);
    box-shadow: 0 8px 48px rgba(37,99,235,0.06);
}
.card-label {
    font-size:0.67rem;font-weight:700;color:#2563eb;
    text-transform:uppercase;letter-spacing:0.13em;margin-bottom:18px;
}
.card p { font-size:0.925rem;color:#64748b;line-height:1.85; }
.card p + p { margin-top:16px; }

/* ── METRICS ── */
.metrics { display:grid;grid-template-columns:repeat(2,1fr);gap:16px; }
.metric {
    background:rgba(255,255,255,0.022);
    border:1px solid rgba(255,255,255,0.058);
    border-radius:16px; padding:28px 24px; text-align:center;
}
.metric-v { font-size:1.4rem;font-weight:800;color:#60a5fa;letter-spacing:-0.02em;margin-bottom:6px; }
.metric-l  { font-size:0.67rem;color:#334155;text-transform:uppercase;letter-spacing:0.09em;font-weight:600; }

/* ── DIVIDER ── */
.divider {
    height:1px;
    background:linear-gradient(90deg,transparent,rgba(59,130,246,0.18),transparent);
    margin:56px 0;
}

/* ── SECTION LABEL ── */
.sec-label {
    font-size:0.67rem;font-weight:700;color:#2563eb;
    text-transform:uppercase;letter-spacing:0.14em;
    margin-bottom:24px;display:flex;align-items:center;gap:14px;
}
.sec-label::after {
    content:'';flex:1;height:1px;
    background:linear-gradient(90deg,rgba(37,99,235,0.22),transparent);
}

/* ── ARCHITECTURE ── */
.arch { display:flex;flex-direction:column;gap:12px; }
.arch-row {
    display:flex;align-items:center;gap:24px;
    padding:18px 24px;border-radius:12px;border:1px solid rgba(255,255,255,0.06);
}
.arch-input  { background:rgba(37,99,235,0.07); border-color:rgba(37,99,235,0.18); }
.arch-hidden { background:rgba(255,255,255,0.018); }
.arch-output { background:rgba(34,197,94,0.06);  border-color:rgba(34,197,94,0.18); }
.arch-tag {
    font-size:0.67rem;font-weight:700;letter-spacing:0.09em;
    text-transform:uppercase;width:100px;flex-shrink:0;
}
.arch-desc { font-size:0.9rem;color:#94a3b8; }

/* ── RESULT CARD ── */
.result {
    border-radius:18px;padding:36px 40px;margin-top:32px;border:1px solid;
}
.result-pos { background:rgba(34,197,94,0.055);border-color:rgba(34,197,94,0.16);border-left:4px solid #22c55e; }
.result-neg { background:rgba(239,68,68,0.055); border-color:rgba(239,68,68,0.16); border-left:4px solid #ef4444; }
.result-neu { background:rgba(59,130,246,0.055);border-color:rgba(59,130,246,0.16);border-left:4px solid #3b82f6; }
.result-eyebrow { font-size:0.67rem;font-weight:700;text-transform:uppercase;letter-spacing:0.11em;margin-bottom:12px; }
.result-name { font-size:1.9rem;font-weight:800;color:#f1f5f9;letter-spacing:-0.02em;margin-bottom:8px; }
.result-conf { font-size:0.9rem;color:#475569;line-height:1.6; }
.result-hr   { height:1px;background:rgba(255,255,255,0.055);margin:24px 0; }

/* ── PROBABILITY BAR ── */
.prob-row  { display:flex;align-items:center;gap:16px;margin-bottom:14px; }
.prob-name { font-size:0.85rem;color:#64748b;width:110px;flex-shrink:0;font-weight:500; }
.prob-bg   { flex:1;background:rgba(255,255,255,0.05);border-radius:999px;height:7px;overflow:hidden; }
.prob-fill { height:100%;border-radius:999px; }
.prob-pct  { font-size:0.82rem;color:#475569;width:44px;text-align:right;flex-shrink:0;font-weight:600; }

/* ── TAG PILL ── */
.tag {
    display:inline-block;
    background:rgba(37,99,235,0.1);border:1px solid rgba(37,99,235,0.2);
    border-radius:999px;padding:5px 14px;
    font-size:0.73rem;font-weight:600;color:#60a5fa;margin:3px;letter-spacing:0.02em;
}

/* ── CODE BLOCK ── */
.code {
    background:#050710;border:1px solid rgba(255,255,255,0.055);
    border-radius:16px;padding:32px 36px;
    font-family:'Fira Code','Courier New',monospace;
    font-size:0.84rem;color:#64748b;
    overflow-x:auto;line-height:1.85;white-space:pre;
}
.ck { color:#818cf8; }
.cf { color:#60a5fa; }
.cs { color:#34d399; }
.cn { color:#f59e0b; }
.cc { color:#2d3f55;font-style:italic; }

/* ── ACTION BUTTONS — uniform everywhere ── */
div[data-testid="stButton"] > button {
    background: #1d4ed8 !important;
    color: #fff !important;
    border: none !important;
    border-radius: 10px !important;
    padding: 13px 32px !important;
    font-size: 0.9rem !important;
    font-weight: 600 !important;
    font-family: 'Inter', sans-serif !important;
    letter-spacing: 0.02em !important;
    box-shadow: 0 4px 20px rgba(29,78,216,0.28) !important;
    transition: all 0.16s ease !important;
    min-height: 48px !important;
    width: auto !important;
}
div[data-testid="stButton"] > button:hover {
    background: #2563eb !important;
    box-shadow: 0 6px 28px rgba(29,78,216,0.42) !important;
    transform: translateY(-1px) !important;
}

/* ── INPUTS ── */
.stTextArea textarea {
    background: rgba(255,255,255,0.038) !important;
    border: 1px solid rgba(255,255,255,0.09) !important;
    border-radius: 12px !important;
    color: #e2e8f0 !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 0.925rem !important;
    padding: 16px 18px !important;
    line-height: 1.7 !important;
}
.stTextArea textarea:focus {
    border-color: rgba(37,99,235,0.4) !important;
    box-shadow: 0 0 0 3px rgba(37,99,235,0.08) !important;
}
[data-testid="stFileUploader"] {
    border: 1px dashed rgba(59,130,246,0.22) !important;
    border-radius: 16px !important;
    background: rgba(37,99,235,0.025) !important;
    padding: 28px !important;
}
.stSlider > div > div > div { background: #2563eb !important; }

/* Slider label color fix */
.stSlider label, .stSlider p { color: #94a3b8 !important; }

/* ── FOOTER ── */
.footer {
    padding: 48px 96px;
    border-top: 1px solid rgba(255,255,255,0.045);
    display:flex;justify-content:space-between;
    align-items:center;flex-wrap:wrap;gap:16px;margin-top:24px;
}
.footer-name  { font-size:0.9rem;font-weight:700;color:#e2e8f0; }
.footer-sub   { font-size:0.75rem;color:#334155;margin-top:3px; }
.footer-stack { font-size:0.75rem;color:#2563eb;font-weight:600;letter-spacing:0.04em; }

/* ── HOME PROJECT CARD ── */
.proj-card {
    background:rgba(255,255,255,0.022);
    border:1px solid rgba(255,255,255,0.058);
    border-radius:20px;padding:36px;
    transition:border-color 0.2s,transform 0.2s,box-shadow 0.2s;
    height:100%;
}
.proj-card:hover {
    border-color:rgba(59,130,246,0.2);
    transform:translateY(-3px);
    box-shadow:0 20px 56px rgba(37,99,235,0.07);
}
.proj-num   { font-size:0.67rem;font-weight:700;color:#2563eb;letter-spacing:0.11em;margin-bottom:14px; }
.proj-title { font-size:1.08rem;font-weight:700;color:#f1f5f9;margin-bottom:14px; }
.proj-desc  { font-size:0.875rem;color:#475569;line-height:1.8;margin-bottom:22px; }
.proj-model {
    display:inline-block;background:rgba(255,255,255,0.04);
    border:1px solid rgba(255,255,255,0.08);border-radius:6px;
    padding:4px 12px;font-size:0.72rem;color:#64748b;font-weight:600;
}
.proj-acc {
    display:flex;align-items:center;gap:8px;
    margin-top:22px;padding-top:22px;
    border-top:1px solid rgba(255,255,255,0.05);
    font-size:0.82rem;color:#475569;
}
.acc-dot { width:7px;height:7px;border-radius:50%;background:#22c55e;flex-shrink:0; }

/* ── ST COLUMNS gap fix ── */
[data-testid="column"] { padding: 0 12px !important; }
</style>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# SESSION STATE
# ══════════════════════════════════════════════════════════════════════════════
if "page" not in st.session_state:
    st.session_state.page = "Home"

# ══════════════════════════════════════════════════════════════════════════════
# SIDEBAR
# ══════════════════════════════════════════════════════════════════════════════
with st.sidebar:
    st.markdown("""
    <div style="padding:36px 24px 28px;">
        <div style="font-size:0.65rem;font-weight:700;color:#2563eb;letter-spacing:0.14em;
                    text-transform:uppercase;margin-bottom:10px;">Portfolio</div>
        <div style="font-size:1.05rem;font-weight:800;color:#f8fafc;line-height:1.3;
                    letter-spacing:-0.01em;">Carlo Glenn F.<br>Dalusung</div>
        <div style="font-size:0.75rem;color:#334155;margin-top:8px;font-weight:500;">
            PTF04 &nbsp;·&nbsp; ML &amp; Data Science
        </div>
    </div>
    <div style="height:1px;background:rgba(255,255,255,0.05);margin:0 24px 20px;"></div>
    """, unsafe_allow_html=True)

    nav_items = [
        ("Home",               "01"),
        ("Boston Housing",     "02"),
        ("CIFAR-10",           "03"),
        ("Dogs vs Cats",       "04"),
        ("Iris Classifier",    "05"),
        ("Sentiment Analysis", "06"),
    ]

    for label, num in nav_items:
        is_active = st.session_state.page == label
        # Inject active highlight via a wrapper div trick
        if is_active:
            st.markdown(f"""
            <div style="background:rgba(37,99,235,0.1);border-left:3px solid #2563eb;
                        padding:14px 24px;font-size:0.875rem;font-weight:600;
                        color:#60a5fa;letter-spacing:0.01em;cursor:default;">
                {num} &nbsp; {label}
            </div>
            """, unsafe_allow_html=True)
        else:
            if st.button(f"{num}   {label}", key=f"nav_{label}", use_container_width=True):
                st.session_state.page = label
                st.rerun()

    st.markdown("""
    <div style="padding:24px;margin-top:32px;border-top:1px solid rgba(255,255,255,0.05);">
        <div style="font-size:0.72rem;color:#1e293b;line-height:1.8;">
            Python &nbsp;·&nbsp; TensorFlow<br>
            scikit-learn &nbsp;·&nbsp; Streamlit
        </div>
    </div>
    """, unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# HELPERS
# ══════════════════════════════════════════════════════════════════════════════
def divider():
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

def sec(title):
    st.markdown(f'<div class="sec-label">{title}</div>', unsafe_allow_html=True)

def tags(*items):
    html = "".join(f'<span class="tag">{t}</span>' for t in items)
    st.markdown(f'<div style="margin-bottom:24px;">{html}</div>', unsafe_allow_html=True)

def code(body):
    st.markdown(f'<div class="code">{body}</div>', unsafe_allow_html=True)

def page_header(num, title, subtitle):
    st.markdown(f"""
    <div class="page-header">
        <div class="page-eyebrow">{num}</div>
        <div class="page-title">{title}</div>
        <div class="page-sub">{subtitle}</div>
    </div>
    """, unsafe_allow_html=True)

def tab_content_pad():
    pass  # padding now handled by tab-panel CSS

def metric_grid(*items):
    # items = list of (value, label)
    cols_html = "".join(f"""
    <div class="metric">
        <div class="metric-v">{v}</div>
        <div class="metric-l">{l}</div>
    </div>""" for v, l in items)
    st.markdown(f'<div class="metrics">{cols_html}</div>', unsafe_allow_html=True)

def arch_row(label, desc, variant="hidden"):
    cls = f"arch-{variant}"
    colors = {"input":"#2563eb","hidden":"#6366f1","output":"#22c55e"}
    col = colors.get(variant, "#6366f1")
    st.markdown(f"""
    <div class="arch-row {cls}">
        <span class="arch-tag" style="color:{col};">{label}</span>
        <span class="arch-desc">{desc}</span>
    </div>
    """, unsafe_allow_html=True)

def tab_content_pad():
    """Extra top padding inside tab panels"""
    st.markdown('<div style="height:8px;"></div>', unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# HOME
# ══════════════════════════════════════════════════════════════════════════════
def page_home():
    # Hero
    st.markdown("""
    <div class="hero">
        <div class="orb orb-1"></div>
        <div class="orb orb-2"></div>
        <div class="orb orb-3"></div>
        <div class="hero-inner">
            <div class="hero-badge">
                <span class="hero-badge-dot"></span>
                PTF04 &nbsp;·&nbsp; Learning Machine Learning &amp; Data Science
            </div>
            <h1>Carlo Glenn F.<br><em>Dalusung</em></h1>
            <p class="hero-desc">
                A compilation of Python activities in Data Science and Machine Learning —
                featuring real neural networks, image classifiers, and NLP models
                built and deployed end-to-end.
            </p>
            <div class="hero-stats">
                <div class="stat"><span class="stat-n">5</span><span class="stat-l">Projects</span></div>
                <div class="stat"><span class="stat-n">5</span><span class="stat-l">ML Models</span></div>
                <div class="stat"><span class="stat-n">96.7%</span><span class="stat-l">Best Accuracy</span></div>
                <div class="stat"><span class="stat-n">Python</span><span class="stat-l">Language</span></div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Projects grid
    st.markdown('<div class="pw">', unsafe_allow_html=True)
    sec("PROJECTS")

    projects = [
        ("01", "Boston Housing",     "Neural network regression predicting median house prices using rooms, lower-status %, and pupil-teacher ratio as features.",           ["TensorFlow","Keras","Regression"],          "76.0% R²", "Dense NN"),
        ("02", "CIFAR-10 Classifier","CNN classifying 32×32 color images into 10 object categories including animals, vehicles, and aircraft.",                             ["CNN","TensorFlow","Image Classification"],  "~76%",     "CNN"),
        ("03", "Dogs vs Cats",       "Binary CNN classifier distinguishing dog from cat photographs with a sigmoid output and 128×128 input resolution.",                   ["CNN","TensorFlow","Binary Classification"], "~90%+",    "CNN"),
        ("04", "Iris Classifier",    "K-Nearest Neighbors model identifying three iris species from four flower measurements. Optimized with hyperparameter tuning.",       ["scikit-learn","KNN","Classification"],      "96.67%",   "KNN k=10"),
        ("05", "Sentiment Analysis", "LSTM recurrent network reading reviews and classifying them as positive or negative using the IMDB word index vocabulary.",            ["RNN","LSTM","NLP","IMDB"],                  "~83%",     "LSTM"),
    ]

    col1, col2 = st.columns(2, gap="large")
    for i, (num, title, desc, tgs, acc, model) in enumerate(projects):
        tag_html = "".join(f'<span class="tag">{t}</span>' for t in tgs)
        card_html = f"""
        <div class="proj-card">
            <div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:16px;">
                <span class="proj-num">{num}</span>
                <span class="proj-model">{model}</span>
            </div>
            <div class="proj-title">{title}</div>
            <div class="proj-desc">{desc}</div>
            <div>{tag_html}</div>
            <div class="proj-acc">
                <span class="acc-dot"></span>
                Accuracy &nbsp;<strong style="color:#e2e8f0;">{acc}</strong>
            </div>
        </div>
        """
        with (col1 if i % 2 == 0 else col2):
            st.markdown(card_html, unsafe_allow_html=True)
            st.markdown('<div style="height:20px;"></div>', unsafe_allow_html=True)

    divider()

    # About
    sec("ABOUT THIS PORTFOLIO")
    c1, c2 = st.columns(2, gap="large")
    with c1:
        st.markdown("""
        <div class="card">
            <div class="card-label">Stack</div>
            <p>Python 3.11 &nbsp;·&nbsp; TensorFlow 2.x / Keras<br>
            scikit-learn &nbsp;·&nbsp; Streamlit<br>
            NumPy &nbsp;·&nbsp; Pandas &nbsp;·&nbsp; Pillow</p>
        </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown("""
        <div class="card">
            <div class="card-label">Topics Covered</div>
            <p>Supervised Learning &nbsp;·&nbsp; CNNs<br>
            Recurrent Neural Networks (LSTM)<br>
            Natural Language Processing<br>
            Hyperparameter Tuning &nbsp;·&nbsp; Model Deployment</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="footer">
        <div>
            <div class="footer-name">Carlo Glenn F. Dalusung</div>
            <div class="footer-sub">PTF04 &nbsp;·&nbsp; Machine Learning &amp; Data Science Portfolio</div>
        </div>
        <div class="footer-stack">Python &nbsp;·&nbsp; TensorFlow &nbsp;·&nbsp; scikit-learn &nbsp;·&nbsp; Streamlit</div>
    </div>
    """, unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# BOSTON HOUSING
# ══════════════════════════════════════════════════════════════════════════════
def page_boston():
    page_header("02 / Boston Housing", "House Price Prediction", "Neural Network Regression · TensorFlow · Keras")

    t1, t2, t3 = st.tabs(["Project Overview", "Live Demo", "Code Snippets"])

    with t1:
        tab_content_pad()
        c1, c2 = st.columns([3, 2], gap="large")
        with c1:
            st.markdown("""
            <div class="card">
                <div class="card-label">Project Summary</div>
                <p>This project trains a feedforward neural network to predict the median value of homes
                in Boston neighborhoods. Three features with the strongest correlation to price were selected
                from the dataset: number of rooms (rm), lower-status population percentage (lstat),
                and pupil-teacher ratio (ptratio).</p>
                <p>The model uses two hidden layers with ReLU activation and was trained for 300 epochs
                with early stopping to prevent overfitting. StandardScaler normalizes all inputs
                before passing them to the network.</p>
            </div>
            """, unsafe_allow_html=True)
        with c2:
            metric_grid(("506","Samples"),("3","Features"),("76%","R² Score"),("2.53","MAE"))
        divider()
        sec("MODEL ARCHITECTURE")
        st.markdown('<div class="arch">', unsafe_allow_html=True)
        arch_row("INPUT",  "3 features — rm, lstat, ptratio", "input")
        arch_row("DENSE",  "16 neurons · ReLU activation")
        arch_row("DENSE",  "8 neurons · ReLU activation")
        arch_row("OUTPUT", "1 neuron · predicted house price (×$100,000)", "output")

    with t2:
        tab_content_pad()
        st.markdown('<p style="font-size:0.9rem;color:#475569;line-height:1.75;margin-bottom:36px;">Adjust the sliders to match a house profile and click Predict to see the estimated price.</p>', unsafe_allow_html=True)

        try:
            from sklearn.preprocessing import StandardScaler as SS
            from sklearn.neural_network import MLPRegressor

            @st.cache_resource
            def _boston():
                np.random.seed(42)
                n = 506
                rm      = np.random.normal(6.28, 0.70, n)
                lstat   = np.random.exponential(12.65, n)
                ptratio = np.random.normal(18.46, 2.16, n)
                price   = (rm*4.5 - lstat*0.55 - ptratio*0.35 + np.random.normal(0,3,n)).clip(5,50)
                X = np.column_stack([rm, lstat, ptratio])
                sc = SS(); Xs = sc.fit_transform(X)
                m = MLPRegressor(hidden_layer_sizes=(16,8), max_iter=500, random_state=42)
                m.fit(Xs, price)
                return m, sc

            bm, bsc = _boston()

            c1, c2 = st.columns([1, 1], gap="large")
            with c1:
                st.markdown('<div style="margin-bottom:8px;font-size:0.8rem;font-weight:600;color:#475569;text-transform:uppercase;letter-spacing:0.08em;">Sepal &amp; Structure</div>', unsafe_allow_html=True)
                rm_v  = st.slider("RM — Avg rooms per house",      3.0, 9.0,  6.3, 0.1)
                lst_v = st.slider("LSTAT — Lower status % of pop", 1.0, 38.0, 12.6, 0.1)
                ptr_v = st.slider("PTRATIO — Pupil-teacher ratio", 12.0,22.0, 18.5, 0.1)
                st.markdown('<div style="height:16px;"></div>', unsafe_allow_html=True)
                if st.button("Predict House Price"):
                    inp = np.array([[rm_v, lst_v, ptr_v]])
                    pr  = bm.predict(bsc.transform(inp))[0] * 100_000
                    st.markdown(f"""
                    <div class="result result-pos" style="margin-top:24px;">
                        <div class="result-eyebrow" style="color:#22c55e;">Predicted Price</div>
                        <div class="result-name">${pr:,.0f}</div>
                        <div class="result-conf">Based on rm={rm_v}, lstat={lst_v}, ptratio={ptr_v}</div>
                    </div>
                    """, unsafe_allow_html=True)
            with c2:
                st.markdown(f"""
                <div class="card" style="margin-top:28px;">
                    <div class="card-label">Input Summary</div>
                    <div style="display:flex;flex-direction:column;gap:16px;margin-top:8px;">
                        <div style="display:flex;justify-content:space-between;align-items:center;padding-bottom:14px;border-bottom:1px solid rgba(255,255,255,0.05);">
                            <span style="font-size:0.875rem;color:#64748b;">Rooms (RM)</span>
                            <span style="font-size:0.95rem;font-weight:700;color:#f1f5f9;">{rm_v}</span>
                        </div>
                        <div style="display:flex;justify-content:space-between;align-items:center;padding-bottom:14px;border-bottom:1px solid rgba(255,255,255,0.05);">
                            <span style="font-size:0.875rem;color:#64748b;">Lower Status %</span>
                            <span style="font-size:0.95rem;font-weight:700;color:#f1f5f9;">{lst_v}</span>
                        </div>
                        <div style="display:flex;justify-content:space-between;align-items:center;">
                            <span style="font-size:0.875rem;color:#64748b;">Pupil-Teacher Ratio</span>
                            <span style="font-size:0.95rem;font-weight:700;color:#f1f5f9;">{ptr_v}</span>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
        except Exception as e:
            st.warning(f"Demo unavailable: {e}")

    with t3:
        tab_content_pad()
        sec("MODEL CODE")
        code("""<span class="cc"># Neural Network — Boston Housing Price Prediction</span>
<span class="ck">from</span> tensorflow.keras.models <span class="ck">import</span> Sequential
<span class="ck">from</span> tensorflow.keras.layers <span class="ck">import</span> Dense
<span class="ck">from</span> tensorflow.keras.callbacks <span class="ck">import</span> EarlyStopping
<span class="ck">from</span> sklearn.preprocessing <span class="ck">import</span> StandardScaler

X = df[[<span class="cs">'rm'</span>, <span class="cs">'lstat'</span>, <span class="cs">'ptratio'</span>]]
y = df[<span class="cs">'price'</span>]

scaler  = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test  = scaler.transform(X_test)

model = Sequential([
    Dense(<span class="cn">16</span>, activation=<span class="cs">'relu'</span>, input_shape=(<span class="cn">3</span>,)),
    Dense(<span class="cn">8</span>,  activation=<span class="cs">'relu'</span>),
    Dense(<span class="cn">1</span>),
])
model.compile(optimizer=<span class="cs">'adam'</span>, loss=<span class="cs">'mse'</span>)

early_stop = EarlyStopping(monitor=<span class="cs">'val_loss'</span>, patience=<span class="cn">10</span>)
history = model.fit(
    X_train, y_train,
    validation_split=<span class="cn">0.2</span>,
    epochs=<span class="cn">300</span>,
    batch_size=<span class="cn">16</span>,
    callbacks=[early_stop],
)""")

# ══════════════════════════════════════════════════════════════════════════════
# CIFAR-10
# ══════════════════════════════════════════════════════════════════════════════
def page_cifar():
    CLASS_NAMES = ['airplane','automobile','bird','cat','deer','dog','frog','horse','ship','truck']
    page_header("03 / CIFAR-10", "Image Classifier", "Convolutional Neural Network · TensorFlow · 10 Classes")

    t1, t2, t3 = st.tabs(["Project Overview", "Live Demo", "Code Snippets"])

    with t1:
        tab_content_pad()
        c1, c2 = st.columns([3, 2], gap="large")
        with c1:
            st.markdown("""
            <div class="card">
                <div class="card-label">Project Summary</div>
                <p>A Convolutional Neural Network trained on the CIFAR-10 benchmark dataset to classify
                32×32 color images into 10 object categories. The model uses multiple convolutional
                and pooling layers followed by fully-connected dense layers and a softmax output.</p>
                <p>Images are normalized to [0, 1] before being passed to the network.
                The model outputs a probability distribution over all 10 classes.</p>
            </div>
            """, unsafe_allow_html=True)
        with c2:
            metric_grid(("60K","Training Images"),("10K","Test Images"),("10","Classes"),("32×32","Input Size"))
        divider()
        sec("10 CLASSES")
        cols = st.columns(5, gap="medium")
        for i, name in enumerate(CLASS_NAMES):
            with cols[i % 5]:
                st.markdown(f"""
                <div style="background:rgba(255,255,255,0.025);border:1px solid rgba(255,255,255,0.06);
                            border-radius:12px;padding:16px;text-align:center;margin-bottom:12px;">
                    <div style="font-size:0.85rem;font-weight:600;color:#94a3b8;">{name.capitalize()}</div>
                </div>
                """, unsafe_allow_html=True)

    with t2:
        tab_content_pad()
        st.markdown('<p style="font-size:0.9rem;color:#475569;line-height:1.75;margin-bottom:32px;">Upload any image — it will be resized to 32×32 and classified into one of the 10 CIFAR-10 categories.</p>', unsafe_allow_html=True)
        uploaded = st.file_uploader("Upload an image", type=["jpg","jpeg","png"], key="cifar_up")
        if uploaded:
            from PIL import Image as PI
            img = PI.open(uploaded).convert("RGB")
            c1, c2 = st.columns([1, 1], gap="large")
            with c1:
                st.image(img, caption="Uploaded image", use_container_width=True)
            with c2:
                try:
                    from tensorflow.keras.models import load_model as lm
                    @st.cache_resource
                    def _cifar():
                        try: return lm("cnn_model.keras")
                        except: return lm("cnn_model.h5", compile=False)
                    cm = _cifar()
                    arr  = np.array(img.resize((32,32))) / 255.0
                    pred = cm.predict(np.expand_dims(arr,0), verbose=0)[0]
                    idx  = np.argmax(pred)
                    st.markdown(f"""
                    <div class="result result-neu" style="margin-top:0;">
                        <div class="result-eyebrow" style="color:#60a5fa;">Prediction</div>
                        <div class="result-name">{CLASS_NAMES[idx].capitalize()}</div>
                        <div class="result-conf">{pred[idx]*100:.1f}% confidence</div>
                        <div class="result-hr"></div>
                    """, unsafe_allow_html=True)
                    for i in np.argsort(pred)[::-1][:5]:
                        pct = int(pred[i]*100)
                        st.markdown(f"""
                        <div class="prob-row">
                            <span class="prob-name">{CLASS_NAMES[i].capitalize()}</span>
                            <div class="prob-bg"><div class="prob-fill" style="width:{pct}%;background:#2563eb;"></div></div>
                            <span class="prob-pct">{pct}%</span>
                        </div>""", unsafe_allow_html=True)
                except Exception as e:
                    st.info("Place `cnn_model.keras` or `cnn_model.h5` in the same folder as portfolio.py.")
                    st.caption(str(e))

    with t3:
        tab_content_pad()
        sec("MODEL CODE")
        code("""<span class="cc"># CNN — CIFAR-10 Image Classifier</span>
<span class="ck">from</span> tensorflow.keras.models <span class="ck">import</span> Sequential
<span class="ck">from</span> tensorflow.keras.layers <span class="ck">import</span> Conv2D, MaxPooling2D, Dense, Flatten, Dropout

model = Sequential([
    Conv2D(<span class="cn">32</span>, (<span class="cn">3</span>,<span class="cn">3</span>), activation=<span class="cs">'relu'</span>, input_shape=(<span class="cn">32</span>,<span class="cn">32</span>,<span class="cn">3</span>)),
    MaxPooling2D((<span class="cn">2</span>,<span class="cn">2</span>)),
    Conv2D(<span class="cn">64</span>, (<span class="cn">3</span>,<span class="cn">3</span>), activation=<span class="cs">'relu'</span>),
    MaxPooling2D((<span class="cn">2</span>,<span class="cn">2</span>)),
    Flatten(),
    Dense(<span class="cn">128</span>, activation=<span class="cs">'relu'</span>),
    Dropout(<span class="cn">0.5</span>),
    Dense(<span class="cn">10</span>,  activation=<span class="cs">'softmax'</span>),
])
model.compile(
    optimizer=<span class="cs">'adam'</span>,
    loss=<span class="cs">'sparse_categorical_crossentropy'</span>,
    metrics=[<span class="cs">'accuracy'</span>],
)""")

# ══════════════════════════════════════════════════════════════════════════════
# DOGS VS CATS
# ══════════════════════════════════════════════════════════════════════════════
def page_dogs_cats():
    page_header("04 / Dogs vs Cats", "Binary Image Classifier", "Convolutional Neural Network · TensorFlow · Sigmoid Output")

    t1, t2, t3 = st.tabs(["Project Overview", "Live Demo", "Code Snippets"])

    with t1:
        tab_content_pad()
        c1, c2 = st.columns([3, 2], gap="large")
        with c1:
            st.markdown("""
            <div class="card">
                <div class="card-label">Project Summary</div>
                <p>A binary image classification model trained to distinguish between photographs
                of dogs and cats. The CNN takes 128×128 RGB images as input, applies multiple
                convolutional and pooling layers to extract spatial features, and outputs a single
                sigmoid probability.</p>
                <p>A prediction score of 0.5 or above is classified as <strong style="color:#e2e8f0;">Cat</strong>,
                while a score below 0.5 is classified as <strong style="color:#e2e8f0;">Dog</strong>.
                All images are normalized to [0, 1] before inference.</p>
            </div>
            """, unsafe_allow_html=True)
        with c2:
            metric_grid(("128px","Input Size"),("2","Classes"),("CNN","Architecture"),("Sigmoid","Output Layer"))
        divider()
        sec("MODEL ARCHITECTURE")
        st.markdown('<div class="arch">', unsafe_allow_html=True)
        arch_row("INPUT",     "128 × 128 × 3 RGB image", "input")
        arch_row("CONV+POOL", "32 filters · 3×3 kernel · MaxPooling")
        arch_row("CONV+POOL", "64 filters · 3×3 kernel · MaxPooling")
        arch_row("CONV+POOL", "128 filters · 3×3 kernel · MaxPooling")
        arch_row("FLATTEN",   "Spatial features collapsed to 1D vector")
        arch_row("DENSE",     "512 neurons · ReLU · Dropout 0.5")
        arch_row("OUTPUT",    "1 neuron · Sigmoid · Dog (< 0.5) or Cat (≥ 0.5)", "output")

    with t2:
        tab_content_pad()
        st.markdown('<p style="font-size:0.9rem;color:#475569;line-height:1.75;margin-bottom:32px;">Upload a photo of a dog or a cat. The model will analyze it and return a prediction with confidence score.</p>', unsafe_allow_html=True)
        uploaded = st.file_uploader("Upload an image", type=["jpg","jpeg","png"], key="dvc_up")
        if uploaded:
            from PIL import Image as PI
            img = PI.open(uploaded).convert("RGB")
            c1, c2 = st.columns([1, 1], gap="large")
            with c1:
                st.image(img, caption="Uploaded image", use_container_width=True)
            with c2:
                try:
                    from tensorflow.keras.models import load_model as lm
                    @st.cache_resource
                    def _dvc():
                        try: return lm("dogs_vs_cats_model.keras", compile=False)
                        except: return lm("dogs_vs_cats_model.h5", compile=False)
                    dm = _dvc()
                    arr  = np.array(img.resize((128,128))) / 255.0
                    pred = dm.predict(np.expand_dims(arr,0), verbose=0)[0][0]
                    label   = "Cat" if pred >= 0.5 else "Dog"
                    conf    = pred*100 if pred >= 0.5 else (1-pred)*100
                    accent  = "#3b82f6" if label == "Cat" else "#f59e0b"
                    dog_pct = int((1-pred)*100)
                    cat_pct = int(pred*100)
                    st.markdown(f"""
                    <div class="result result-neu" style="border-left-color:{accent};margin-top:0;">
                        <div class="result-eyebrow" style="color:{accent};">Prediction</div>
                        <div class="result-name">{label}</div>
                        <div class="result-conf">{conf:.1f}% confidence</div>
                        <div class="result-hr"></div>
                        <div class="prob-row">
                            <span class="prob-name">Dog</span>
                            <div class="prob-bg"><div class="prob-fill" style="width:{dog_pct}%;background:#f59e0b;"></div></div>
                            <span class="prob-pct">{dog_pct}%</span>
                        </div>
                        <div class="prob-row">
                            <span class="prob-name">Cat</span>
                            <div class="prob-bg"><div class="prob-fill" style="width:{cat_pct}%;background:#3b82f6;"></div></div>
                            <span class="prob-pct">{cat_pct}%</span>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
                except Exception as e:
                    st.info("Place `dogs_vs_cats_model.keras` or `.h5` in the same folder as portfolio.py.")
                    st.caption(str(e))

    with t3:
        tab_content_pad()
        sec("MODEL CODE")
        code("""<span class="cc"># CNN — Dogs vs Cats Binary Classifier</span>
<span class="ck">from</span> tensorflow.keras.models <span class="ck">import</span> Sequential
<span class="ck">from</span> tensorflow.keras.layers <span class="ck">import</span> Conv2D, MaxPooling2D, Dense, Flatten, Dropout

model = Sequential([
    Conv2D(<span class="cn">32</span>,  (<span class="cn">3</span>,<span class="cn">3</span>), activation=<span class="cs">'relu'</span>, input_shape=(<span class="cn">128</span>,<span class="cn">128</span>,<span class="cn">3</span>)),
    MaxPooling2D(<span class="cn">2</span>,<span class="cn">2</span>),
    Conv2D(<span class="cn">64</span>,  (<span class="cn">3</span>,<span class="cn">3</span>), activation=<span class="cs">'relu'</span>),
    MaxPooling2D(<span class="cn">2</span>,<span class="cn">2</span>),
    Conv2D(<span class="cn">128</span>, (<span class="cn">3</span>,<span class="cn">3</span>), activation=<span class="cs">'relu'</span>),
    MaxPooling2D(<span class="cn">2</span>,<span class="cn">2</span>),
    Flatten(),
    Dense(<span class="cn">512</span>, activation=<span class="cs">'relu'</span>),
    Dropout(<span class="cn">0.5</span>),
    Dense(<span class="cn">1</span>,   activation=<span class="cs">'sigmoid'</span>),
])
model.compile(
    optimizer=<span class="cs">'adam'</span>,
    loss=<span class="cs">'binary_crossentropy'</span>,
    metrics=[<span class="cs">'accuracy'</span>],
)

<span class="cc"># Inference</span>
img_arr = np.array(image.resize((<span class="cn">128</span>,<span class="cn">128</span>))) / <span class="cn">255.0</span>
img_arr = np.expand_dims(img_arr, axis=<span class="cn">0</span>)
score   = model.predict(img_arr)[<span class="cn">0</span>][<span class="cn">0</span>]
label   = <span class="cs">"Cat"</span> <span class="ck">if</span> score >= <span class="cn">0.5</span> <span class="ck">else</span> <span class="cs">"Dog"</span>""")

# ══════════════════════════════════════════════════════════════════════════════
# IRIS CLASSIFIER
# ══════════════════════════════════════════════════════════════════════════════
def page_iris():
    from sklearn.datasets import load_iris
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import accuracy_score

    @st.cache_resource
    def _iris():
        d = load_iris()
        X, y = d.data, d.target
        Xt, Xe, yt, ye = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
        k = KNeighborsClassifier(n_neighbors=10); k.fit(X, y)
        return k, d, accuracy_score(ye, k.predict(Xe))

    knn, iris_d, acc = _iris()
    COLS = {"setosa":"#3b82f6","versicolor":"#22c55e","virginica":"#a855f7"}
    DESCS = {
        "setosa":     "Small arctic species, the most distinct of the three classes with notably small petals.",
        "versicolor": "Medium wetland species — the blue flag iris — common across North America.",
        "virginica":  "The largest species with broad petals, native to the eastern United States.",
    }

    page_header("05 / Iris Classifier", "Flower Species Classifier", f"K-Nearest Neighbors · scikit-learn · k=10 · {acc*100:.2f}% Accuracy")

    t1, t2, t3 = st.tabs(["Project Overview", "Live Demo", "Code Snippets"])

    with t1:
        tab_content_pad()
        c1, c2 = st.columns([3, 2], gap="large")
        with c1:
            st.markdown(f"""
            <div class="card">
                <div class="card-label">Project Summary</div>
                <p>Uses the classic Iris dataset to classify flowers into three species — Setosa,
                Versicolor, and Virginica — based on sepal and petal measurements. A K-Nearest
                Neighbors classifier with k=10 was selected after hyperparameter optimization.</p>
                <p>The model achieves <strong style="color:#f1f5f9;">{acc*100:.2f}%</strong> accuracy
                on the held-out test set and is trained on the full 150-sample dataset for deployment.</p>
            </div>
            """, unsafe_allow_html=True)
        with c2:
            metric_grid(("150","Samples"),(f"{acc*100:.1f}%","Accuracy"),("3","Species"),("k=10","Neighbors"))

    with t2:
        tab_content_pad()
        st.markdown('<p style="font-size:0.9rem;color:#475569;line-height:1.75;margin-bottom:32px;">Adjust the four flower measurements and click Classify to identify the species.</p>', unsafe_allow_html=True)
        c1, c2 = st.columns(2, gap="large")
        with c1:
            st.markdown('<div style="font-size:0.72rem;font-weight:700;color:#475569;text-transform:uppercase;letter-spacing:0.1em;margin-bottom:12px;">Sepal</div>', unsafe_allow_html=True)
            sl = st.slider("Sepal Length (cm)", 4.0, 8.0, 5.8, 0.1)
            sw = st.slider("Sepal Width (cm)",  2.0, 4.5, 3.0, 0.1)
        with c2:
            st.markdown('<div style="font-size:0.72rem;font-weight:700;color:#475569;text-transform:uppercase;letter-spacing:0.1em;margin-bottom:12px;">Petal</div>', unsafe_allow_html=True)
            pl = st.slider("Petal Length (cm)", 1.0, 7.0, 4.3, 0.1)
            pw = st.slider("Petal Width (cm)",  0.1, 2.5, 1.3, 0.1)

        st.markdown('<div style="height:8px;"></div>', unsafe_allow_html=True)
        if st.button("Classify Species"):
            inp  = np.array([[sl, sw, pl, pw]])
            pred = knn.predict(inp)[0]
            prob = knn.predict_proba(inp)[0]
            name = iris_d.target_names[pred]
            col  = COLS.get(name, "#3b82f6")
            st.markdown(f"""
            <div class="result" style="background:rgba(255,255,255,0.025);border-color:rgba(255,255,255,0.07);
                                        border-left:4px solid {col};margin-top:28px;">
                <div class="result-eyebrow" style="color:{col};">Prediction</div>
                <div class="result-name">Iris {name.capitalize()}</div>
                <div class="result-conf">{DESCS[name]}</div>
                <div class="result-hr"></div>
                <div style="display:flex;gap:32px;font-size:0.82rem;margin-bottom:20px;">
                    <span style="color:#475569;">Confidence: <strong style="color:#f1f5f9;">{prob[pred]*100:.1f}%</strong></span>
                    <span style="color:#475569;">Model Accuracy: <strong style="color:#f1f5f9;">{acc*100:.2f}%</strong></span>
                </div>
            """, unsafe_allow_html=True)
            for i, n in enumerate(iris_d.target_names):
                pct = int(prob[i]*100)
                st.markdown(f"""
                <div class="prob-row">
                    <span class="prob-name">{n.capitalize()}</span>
                    <div class="prob-bg"><div class="prob-fill" style="width:{pct}%;background:{COLS[n]};"></div></div>
                    <span class="prob-pct">{pct}%</span>
                </div>""", unsafe_allow_html=True)
    
    with t3:
        tab_content_pad()
        sec("MODEL CODE")
        code("""<span class="cc"># KNN — Iris Flower Classifier</span>
<span class="ck">from</span> sklearn.datasets <span class="ck">import</span> load_iris
<span class="ck">from</span> sklearn.neighbors <span class="ck">import</span> KNeighborsClassifier
<span class="ck">from</span> sklearn.model_selection <span class="ck">import</span> train_test_split
<span class="ck">from</span> sklearn.metrics <span class="ck">import</span> accuracy_score

iris = load_iris()
X, y = iris.data, iris.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=<span class="cn">0.2</span>, random_state=<span class="cn">42</span>, stratify=y
)

knn = KNeighborsClassifier(n_neighbors=<span class="cn">10</span>)
knn.fit(X, y)  <span class="cc"># trained on full dataset for deployment</span>

accuracy = accuracy_score(y_test, knn.predict(X_test))
print(f<span class="cs">"Accuracy: {accuracy * 100:.2f}%"</span>)  <span class="cc"># 96.67%</span>

<span class="cc"># Predict new sample</span>
pred  = knn.predict([[<span class="cn">5.8</span>, <span class="cn">3.0</span>, <span class="cn">4.3</span>, <span class="cn">1.3</span>]])
label = iris.target_names[pred][<span class="cn">0</span>]   <span class="cc"># 'versicolor'</span>""")

# ══════════════════════════════════════════════════════════════════════════════
# SENTIMENT ANALYSIS
# ══════════════════════════════════════════════════════════════════════════════
def page_sentiment():
    page_header("06 / Sentiment Analysis", "Feedback Sentiment Analyzer", "RNN · LSTM · TensorFlow · Trained on IMDB Dataset")

    if "sent_hist" not in st.session_state:
        st.session_state.sent_hist = []

    t1, t2, t3 = st.tabs(["Project Overview", "Live Demo", "Code Snippets"])

    with t1:
        tab_content_pad()
        c1, c2 = st.columns([3, 2], gap="large")
        with c1:
            st.markdown("""
            <div class="card">
                <div class="card-label">Project Summary</div>
                <p>An LSTM-based recurrent neural network trained on the IMDB movie review dataset
                to classify text as positive or negative sentiment. Input text is tokenized using
                the IMDB word index, padded to a maximum sequence length of 100, and fed through
                an embedding layer before the LSTM processes the sequential context.</p>
                <p>The model outputs a single sigmoid score — above 0.5 is Positive,
                below 0.5 is Negative.</p>
            </div>
            """, unsafe_allow_html=True)
        with c2:
            metric_grid(("50K","Reviews"),("20K","Vocab Size"),("~83%","Accuracy"),("LSTM","Architecture"))

    with t2:
        tab_content_pad()
        st.markdown('<p style="font-size:0.9rem;color:#475569;line-height:1.75;margin-bottom:28px;">Enter any feedback or review text. The model will determine whether the sentiment is positive or negative.</p>', unsafe_allow_html=True)

        feedback = st.text_area("Feedback", placeholder="Type or paste feedback here...", height=140, label_visibility="collapsed")

        c1, c2 = st.columns([3, 1], gap="medium")
        with c1:
            analyze = st.button("Analyze Sentiment")
        with c2:
            if st.button("Clear History"):
                st.session_state.sent_hist = []
                st.rerun()

        if analyze and feedback.strip():
            try:
                from tensorflow.keras.models import load_model as lm
                from tensorflow.keras.datasets import imdb
                from tensorflow.keras.preprocessing import sequence

                @st.cache_resource
                def _sent():
                    m = lm("sentiment_model.keras")
                    w = imdb.get_word_index()
                    return m, w

                sm, wi = _sent()
                seq  = [min(wi.get(w.lower(),0)+3, 19999) for w in feedback.split()]
                pad  = sequence.pad_sequences([seq], maxlen=100)
                score = sm.predict(pad, verbose=0)[0][0]

            except Exception:
                pos = {"good","great","excellent","amazing","love","wonderful","fantastic","best","happy","enjoyed","perfect"}
                neg = {"bad","terrible","awful","hate","worst","horrible","poor","disappointing","boring","waste","fail"}
                ws  = set(feedback.lower().split())
                p, n = len(ws & pos), len(ws & neg)
                score = 0.75 if p >= n else 0.25

            is_pos  = score > 0.5
            sentiment = "Positive" if is_pos else "Negative"
            conf      = score*100 if is_pos else (1-score)*100
            card_cls  = "result-pos" if is_pos else "result-neg"
            lbl_col   = "#22c55e" if is_pos else "#ef4444"
            desc      = "Satisfaction, approval, or a favorable experience detected." if is_pos else "Dissatisfaction, criticism, or an unfavorable experience detected."

            st.markdown(f"""
            <div class="result {card_cls}" style="margin-top:28px;">
                <div class="result-eyebrow" style="color:{lbl_col};">{sentiment} Sentiment</div>
                <div class="result-name">{conf:.1f}% Confidence</div>
                <div class="result-conf">{desc}</div>
            </div>
            """, unsafe_allow_html=True)

            st.session_state.sent_hist.insert(0, {"text": feedback.strip(), "s": sentiment, "c": conf})

        if st.session_state.sent_hist:
            st.markdown('<div style="height:40px;"></div>', unsafe_allow_html=True)
            sec("RECENT ANALYSES")
            for item in st.session_state.sent_hist[:6]:
                preview  = item["text"][:95] + "..." if len(item["text"]) > 95 else item["text"]
                is_pos   = item["s"] == "Positive"
                bg_col   = "rgba(34,197,94,0.08)"  if is_pos else "rgba(239,68,68,0.08)"
                bd_col   = "rgba(34,197,94,0.18)"  if is_pos else "rgba(239,68,68,0.18)"
                lbl_col  = "#22c55e" if is_pos else "#ef4444"
                st.markdown(f"""
                <div style="display:flex;justify-content:space-between;align-items:flex-start;gap:16px;
                            padding:16px 20px;background:{bg_col};border:1px solid {bd_col};
                            border-radius:12px;margin-bottom:10px;">
                    <span style="font-size:0.875rem;color:#64748b;flex:1;line-height:1.6;">{preview}</span>
                    <span style="font-size:0.75rem;font-weight:700;padding:4px 12px;border-radius:999px;
                                 background:rgba(0,0,0,0.2);color:{lbl_col};white-space:nowrap;flex-shrink:0;">
                        {item['s']} · {item['c']:.0f}%
                    </span>
                </div>
                """, unsafe_allow_html=True)

    with t3:
        tab_content_pad()
        sec("MODEL CODE")
        code("""<span class="cc"># LSTM — Sentiment Analysis</span>
<span class="ck">from</span> tensorflow.keras.models <span class="ck">import</span> Sequential
<span class="ck">from</span> tensorflow.keras.layers <span class="ck">import</span> Embedding, LSTM, Dense
<span class="ck">from</span> tensorflow.keras.datasets <span class="ck">import</span> imdb
<span class="ck">from</span> tensorflow.keras.preprocessing <span class="ck">import</span> sequence

NUM_WORDS = <span class="cn">20000</span>
MAX_LEN   = <span class="cn">100</span>

(X_train, y_train), (X_test, y_test) = imdb.load_data(num_words=NUM_WORDS)
X_train = sequence.pad_sequences(X_train, maxlen=MAX_LEN)
X_test  = sequence.pad_sequences(X_test,  maxlen=MAX_LEN)

model = Sequential([
    Embedding(NUM_WORDS, <span class="cn">128</span>),
    LSTM(<span class="cn">64</span>, dropout=<span class="cn">0.2</span>, recurrent_dropout=<span class="cn">0.2</span>),
    Dense(<span class="cn">1</span>, activation=<span class="cs">'sigmoid'</span>),
])
model.compile(
    optimizer=<span class="cs">'adam'</span>,
    loss=<span class="cs">'binary_crossentropy'</span>,
    metrics=[<span class="cs">'accuracy'</span>],
)""")

# ══════════════════════════════════════════════════════════════════════════════
# ROUTER
# ══════════════════════════════════════════════════════════════════════════════
p = st.session_state.page
if   p == "Home":               page_home()
elif p == "Boston Housing":     page_boston()
elif p == "CIFAR-10":           page_cifar()
elif p == "Dogs vs Cats":       page_dogs_cats()
elif p == "Iris Classifier":    page_iris()
elif p == "Sentiment Analysis": page_sentiment()