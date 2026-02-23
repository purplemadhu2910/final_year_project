import streamlit as st
from auth import register_user, login_user

# ──────────────────────────────────────────────────────
# Page Config
# ──────────────────────────────────────────────────────
st.set_page_config(
    page_title="LexAssist",
    page_icon="⚖️",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ──────────────────────────────────────────────────────
# Session State Defaults
# ──────────────────────────────────────────────────────
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
if "user" not in st.session_state:
    st.session_state.user = None
if "page" not in st.session_state:
    st.session_state.page = "login"
if "theme" not in st.session_state:
    st.session_state.theme = "dark"

# ──────────────────────────────────────────────────────
# Theme Toggle Callback
# ──────────────────────────────────────────────────────
def toggle_theme():
    st.session_state.theme = "light" if st.session_state.theme == "dark" else "dark"

# ──────────────────────────────────────────────────────
# Determine current theme
# ──────────────────────────────────────────────────────
is_dark = st.session_state.theme == "dark"

# ──────────────────────────────────────────────────────
# Custom CSS — Dual Theme with CSS Variables
# ──────────────────────────────────────────────────────
if is_dark:
    theme_vars = """
    :root {
        --bg-primary: #0a0e1a;
        --bg-secondary: #0f1629;
        --bg-card: rgba(17, 24, 39, 0.72);
        --bg-input: rgba(15, 23, 42, 0.8);
        --bg-input-focus: rgba(15, 23, 42, 1);
        --bg-info-card: rgba(15, 23, 42, 0.5);
        --bg-welcome: linear-gradient(135deg, rgba(99,102,241,0.1), rgba(139,92,246,0.05));
        --border-card: rgba(99, 102, 241, 0.15);
        --border-input: rgba(148, 163, 184, 0.12);
        --border-info: rgba(148, 163, 184, 0.1);
        --border-welcome: rgba(99,102,241,0.15);
        --text-primary: #f1f5f9;
        --text-secondary: #94a3b8;
        --text-label: #94a3b8;
        --text-info-label: #64748b;
        --text-link: #a5b4fc;
        --text-link-hover: #818cf8;
        --accent-gradient: linear-gradient(135deg, #6366f1, #8b5cf6, #a78bfa);
        --brand-title-gradient: linear-gradient(135deg, #f1f5f9, #a5b4fc);
        --shadow-card: 0 25px 60px -12px rgba(0,0,0,0.5), 0 0 40px rgba(99,102,241,0.06);
        --shadow-btn: 0 4px 20px rgba(99, 102, 241, 0.3);
        --shadow-btn-hover: 0 8px 30px rgba(99, 102, 241, 0.45);
        --shadow-icon: 0 8px 24px rgba(99,102,241,0.28);
        --shadow-icon-pulse: 0 8px 34px rgba(99,102,241,0.45);
        --orb1-bg: rgba(99, 102, 241, 0.18);
        --orb2-bg: rgba(139, 92, 246, 0.14);
        --orb3-bg: rgba(167, 139, 250, 0.1);
        --orb-opacity: 0.35;
        --toggle-bg: rgba(99, 102, 241, 0.15);
        --toggle-border: rgba(99, 102, 241, 0.25);
        --toggle-hover: rgba(99, 102, 241, 0.25);
        --toggle-text: #a5b4fc;
    }
    """
else:
    theme_vars = """
    :root {
        --bg-primary: #f0f2f5;
        --bg-secondary: #e8eaef;
        --bg-card: rgba(255, 255, 255, 0.85);
        --bg-input: rgba(241, 245, 249, 0.9);
        --bg-input-focus: rgba(255, 255, 255, 1);
        --bg-info-card: rgba(241, 245, 249, 0.7);
        --bg-welcome: linear-gradient(135deg, rgba(99,102,241,0.06), rgba(139,92,246,0.03));
        --border-card: rgba(99, 102, 241, 0.18);
        --border-input: rgba(100, 116, 139, 0.2);
        --border-info: rgba(100, 116, 139, 0.12);
        --border-welcome: rgba(99,102,241,0.12);
        --text-primary: #1e293b;
        --text-secondary: #475569;
        --text-label: #475569;
        --text-info-label: #64748b;
        --text-link: #6366f1;
        --text-link-hover: #4f46e5;
        --accent-gradient: linear-gradient(135deg, #6366f1, #8b5cf6, #a78bfa);
        --brand-title-gradient: linear-gradient(135deg, #1e293b, #6366f1);
        --shadow-card: 0 25px 60px -12px rgba(0,0,0,0.08), 0 0 40px rgba(99,102,241,0.04);
        --shadow-btn: 0 4px 20px rgba(99, 102, 241, 0.2);
        --shadow-btn-hover: 0 8px 30px rgba(99, 102, 241, 0.35);
        --shadow-icon: 0 8px 24px rgba(99,102,241,0.2);
        --shadow-icon-pulse: 0 8px 34px rgba(99,102,241,0.35);
        --orb1-bg: rgba(99, 102, 241, 0.08);
        --orb2-bg: rgba(139, 92, 246, 0.06);
        --orb3-bg: rgba(167, 139, 250, 0.05);
        --orb-opacity: 0.5;
        --toggle-bg: rgba(99, 102, 241, 0.08);
        --toggle-border: rgba(99, 102, 241, 0.18);
        --toggle-hover: rgba(99, 102, 241, 0.15);
        --toggle-text: #6366f1;
    }
    """

st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

{theme_vars}

/* ── Global ── */
html, body, [data-testid="stAppViewContainer"] {{
    font-family: 'Inter', sans-serif !important;
}}

[data-testid="stAppViewContainer"] {{
    background: linear-gradient(180deg, var(--bg-primary) 0%, var(--bg-secondary) 50%, var(--bg-primary) 100%);
}}

[data-testid="stHeader"] {{
    background: transparent !important;
}}

[data-testid="collapsedControl"] {{
    display: none !important;
}}

/* ── Hide Streamlit Branding ── */
#MainMenu, footer, header {{visibility: hidden;}}

/* ── Theme Toggle Button ── */
.theme-toggle {{
    position: fixed;
    top: 16px;
    right: 20px;
    z-index: 9999;
    display: flex;
    align-items: center;
    gap: 8px;
    background: var(--toggle-bg);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    border: 1px solid var(--toggle-border);
    border-radius: 40px;
    padding: 8px 18px;
    cursor: pointer;
    transition: all 0.35s cubic-bezier(0.4, 0, 0.2, 1);
    font-family: 'Inter', sans-serif;
    font-size: 0.82rem;
    font-weight: 600;
    color: var(--toggle-text);
    letter-spacing: 0.3px;
}}
.theme-toggle:hover {{
    background: var(--toggle-hover);
    transform: scale(1.04);
}}
.theme-toggle .toggle-icon {{
    font-size: 1.1rem;
    transition: transform 0.4s ease;
}}
.theme-toggle:hover .toggle-icon {{
    transform: rotate(30deg);
}}

/* ── Animated Background Orbs ── */
.orb-container {{
    position: fixed;
    top: 0; left: 0; right: 0; bottom: 0;
    pointer-events: none;
    z-index: 0;
    overflow: hidden;
}}
.orb {{
    position: absolute;
    border-radius: 50%;
    filter: blur(80px);
    opacity: var(--orb-opacity);
}}
.orb-1 {{
    width: 400px; height: 400px;
    background: var(--orb1-bg);
    top: -8%; right: -5%;
    animation: float1 15s ease-in-out infinite;
}}
.orb-2 {{
    width: 300px; height: 300px;
    background: var(--orb2-bg);
    bottom: -8%; left: -5%;
    animation: float2 18s ease-in-out infinite;
}}
.orb-3 {{
    width: 200px; height: 200px;
    background: var(--orb3-bg);
    top: 45%; left: 45%;
    animation: pulse 10s ease-in-out infinite;
}}
@keyframes float1 {{
    0%, 100% {{ transform: translate(0, 0); }}
    33% {{ transform: translate(20px, -30px); }}
    66% {{ transform: translate(-10px, 20px); }}
}}
@keyframes float2 {{
    0%, 100% {{ transform: translate(0, 0); }}
    33% {{ transform: translate(-15px, 25px); }}
    66% {{ transform: translate(15px, -10px); }}
}}
@keyframes pulse {{
    0%, 100% {{ transform: scale(1); opacity: var(--orb-opacity); }}
    50% {{ transform: scale(1.2); opacity: 0.18; }}
}}

/* ── Card Container ── */
.auth-card {{
    background: var(--bg-card);
    backdrop-filter: blur(30px) saturate(1.5);
    -webkit-backdrop-filter: blur(30px) saturate(1.5);
    border: 1px solid var(--border-card);
    border-radius: 18px;
    padding: 44px 36px 36px;
    max-width: 440px;
    margin: 0 auto;
    box-shadow: var(--shadow-card);
    position: relative;
    overflow: hidden;
    animation: slideUp 0.55s cubic-bezier(0.16,1,0.3,1);
}}
.auth-card::before {{
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 3px;
    background: var(--accent-gradient);
    border-radius: 18px 18px 0 0;
}}
@keyframes slideUp {{
    0% {{ opacity: 0; transform: translateY(28px) scale(0.97); }}
    100% {{ opacity: 1; transform: translateY(0) scale(1); }}
}}

/* ── Brand ── */
.brand-section {{
    text-align: center;
    margin-bottom: 30px;
}}
.brand-icon {{
    width: 56px; height: 56px;
    background: var(--accent-gradient);
    border-radius: 14px;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 14px;
    box-shadow: var(--shadow-icon);
    font-size: 26px;
    animation: iconPulse 3s ease-in-out infinite;
}}
@keyframes iconPulse {{
    0%, 100% {{ box-shadow: var(--shadow-icon); }}
    50% {{ box-shadow: var(--shadow-icon-pulse); }}
}}
.brand-title {{
    font-size: 1.75rem;
    font-weight: 700;
    letter-spacing: -0.5px;
    background: var(--brand-title-gradient);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin: 0;
}}
.brand-sub {{
    color: var(--text-secondary);
    font-size: 0.9rem;
    margin-top: 4px;
}}

/* ── Streamlit Input Overrides ── */
[data-testid="stTextInput"] > div > div > input,
[data-testid="stNumberInput"] input {{
    background: var(--bg-input) !important;
    border: 1.5px solid var(--border-input) !important;
    border-radius: 10px !important;
    color: var(--text-primary) !important;
    font-family: 'Inter', sans-serif !important;
    padding: 12px 16px !important;
    font-size: 0.95rem !important;
    transition: all 0.3s cubic-bezier(0.4,0,0.2,1) !important;
}}
[data-testid="stTextInput"] > div > div > input:focus {{
    border-color: rgba(99, 102, 241, 0.5) !important;
    box-shadow: 0 0 0 4px rgba(99, 102, 241, 0.18) !important;
    background: var(--bg-input-focus) !important;
}}

[data-testid="stTextInput"] label,
.stTextInput label {{
    color: var(--text-label) !important;
    font-size: 0.8rem !important;
    font-weight: 600 !important;
    text-transform: uppercase !important;
    letter-spacing: 0.8px !important;
    font-family: 'Inter', sans-serif !important;
}}

/* ── Primary Button ── */
.stButton > button {{
    width: 100%;
    padding: 14px 24px !important;
    background: var(--accent-gradient) !important;
    color: #fff !important;
    border: none !important;
    border-radius: 10px !important;
    font-size: 0.95rem !important;
    font-weight: 600 !important;
    font-family: 'Inter', sans-serif !important;
    letter-spacing: 0.3px;
    cursor: pointer;
    transition: all 0.3s cubic-bezier(0.4,0,0.2,1) !important;
    box-shadow: var(--shadow-btn) !important;
    margin-top: 8px;
}}
.stButton > button:hover {{
    transform: translateY(-2px);
    box-shadow: var(--shadow-btn-hover) !important;
}}
.stButton > button:active {{
    transform: translateY(0);
}}

/* ── Logout Button ── */
.logout-btn button {{
    background: rgba(248, 113, 113, 0.1) !important;
    border: 1px solid rgba(248, 113, 113, 0.2) !important;
    color: #f87171 !important;
    box-shadow: none !important;
    padding: 10px 28px !important;
}}
.logout-btn button:hover {{
    background: rgba(248, 113, 113, 0.2) !important;
    box-shadow: none !important;
}}

/* ── Link-style Button ── */
.link-btn button {{
    background: transparent !important;
    color: var(--text-link) !important;
    box-shadow: none !important;
    font-weight: 600 !important;
    padding: 8px 4px !important;
    text-decoration: none;
}}
.link-btn button:hover {{
    color: var(--text-link-hover) !important;
    background: transparent !important;
    box-shadow: none !important;
    text-decoration: underline;
    transform: none !important;
}}

/* ── Footer Text ── */
.auth-footer {{
    text-align: center;
    margin-top: 22px;
    font-size: 0.88rem;
    color: var(--text-secondary);
}}

/* ── Dashboard Info Cards ── */
.info-grid {{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
    gap: 16px;
    margin: 24px 0;
}}
.info-card {{
    background: var(--bg-info-card);
    border: 1px solid var(--border-info);
    border-radius: 12px;
    padding: 22px;
    transition: all 0.3s ease;
}}
.info-card:hover {{
    border-color: rgba(99, 102, 241, 0.2);
    transform: translateY(-2px);
}}
.info-label {{
    font-size: 0.72rem;
    font-weight: 600;
    color: var(--text-info-label);
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-bottom: 6px;
}}
.info-value {{
    font-size: 1.05rem;
    font-weight: 600;
    color: var(--text-primary);
    word-break: break-all;
}}

/* ── Welcome Banner ── */
.welcome-banner {{
    background: var(--bg-welcome);
    border: 1px solid var(--border-welcome);
    border-radius: 12px;
    padding: 28px;
    text-align: center;
    margin-top: 8px;
}}
.welcome-emoji {{ font-size: 2.5rem; margin-bottom: 10px; }}
.welcome-text {{ color: var(--text-secondary); font-size: 0.9rem; line-height: 1.7; }}

/* ── Dashboard Card ── */
.dash-card {{
    background: var(--bg-card);
    backdrop-filter: blur(30px) saturate(1.5);
    -webkit-backdrop-filter: blur(30px) saturate(1.5);
    border: 1px solid var(--border-card);
    border-radius: 18px;
    padding: 44px 36px 36px;
    max-width: 700px;
    margin: 0 auto;
    box-shadow: var(--shadow-card);
    position: relative;
    overflow: hidden;
    animation: slideUp 0.55s cubic-bezier(0.16,1,0.3,1);
}}
.dash-card::before {{
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 3px;
    background: var(--accent-gradient);
    border-radius: 18px 18px 0 0;
}}

/* ── Dashboard Header ── */
.dash-header {{
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 28px;
    flex-wrap: wrap;
    gap: 12px;
}}
.dash-title {{
    font-size: 1.4rem;
    font-weight: 700;
    background: var(--brand-title-gradient);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin: 0;
}}

/* ── Alert Styles ── */
.custom-error {{
    background: rgba(248, 113, 113, 0.1);
    border: 1px solid rgba(248, 113, 113, 0.22);
    color: #f87171;
    padding: 12px 18px;
    border-radius: 10px;
    font-size: 0.88rem;
    font-weight: 500;
    margin-bottom: 16px;
    animation: shakeIn 0.4s ease;
}}
.custom-success {{
    background: rgba(52, 211, 153, 0.1);
    border: 1px solid rgba(52, 211, 153, 0.22);
    color: #34d399;
    padding: 12px 18px;
    border-radius: 10px;
    font-size: 0.88rem;
    font-weight: 500;
    margin-bottom: 16px;
    animation: shakeIn 0.4s ease;
}}
@keyframes shakeIn {{
    0% {{ transform: translateX(-8px); opacity: 0; }}
    50% {{ transform: translateX(4px); }}
    100% {{ transform: translateX(0); opacity: 1; }}
}}

/* ── Theme Toggle Streamlit Button Override ── */
.theme-toggle-btn button {{
    width: auto !important;
    background: var(--toggle-bg) !important;
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    border: 1px solid var(--toggle-border) !important;
    border-radius: 40px !important;
    padding: 8px 20px !important;
    font-size: 0.82rem !important;
    font-weight: 600 !important;
    color: var(--toggle-text) !important;
    letter-spacing: 0.3px;
    box-shadow: none !important;
    transition: all 0.35s cubic-bezier(0.4, 0, 0.2, 1) !important;
    margin-top: 0 !important;
}}
.theme-toggle-btn button:hover {{
    background: var(--toggle-hover) !important;
    transform: scale(1.04) !important;
    box-shadow: none !important;
}}

/* ── Responsive ── */
@media (max-width: 540px) {{
    .auth-card, .dash-card {{ padding: 28px 20px 24px; }}
    .brand-title {{ font-size: 1.45rem; }}
    .dash-title {{ font-size: 1.2rem; }}
    .info-grid {{ grid-template-columns: 1fr; }}
}}
</style>

<!-- Animated Background Orbs -->
<div class="orb-container">
    <div class="orb orb-1"></div>
    <div class="orb orb-2"></div>
    <div class="orb orb-3"></div>
</div>
""", unsafe_allow_html=True)


# ──────────────────────────────────────────────────────
# Theme Toggle (top-right corner)
# ──────────────────────────────────────────────────────
toggle_col1, toggle_col2 = st.columns([5, 1])
with toggle_col2:
    theme_icon = "☀️ Light" if is_dark else "🌙 Dark"
    st.markdown('<div class="theme-toggle-btn">', unsafe_allow_html=True)
    st.button(theme_icon, key="theme_toggle", on_click=toggle_theme)
    st.markdown('</div>', unsafe_allow_html=True)


# ──────────────────────────────────────────────────────
# Helper: Navigation
# ──────────────────────────────────────────────────────
def go_to(page: str):
    st.session_state.page = page

def logout():
    st.session_state.authenticated = False
    st.session_state.user = None
    st.session_state.page = "login"


# ──────────────────────────────────────────────────────
# PAGE: Login
# ──────────────────────────────────────────────────────
def render_login():
    st.markdown("""
    <div class="auth-card">
        <div class="brand-section">
            <div class="brand-icon">🔒</div>
            <p class="brand-title">LexAssist</p>
            <p class="brand-sub">Sign in to your account</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Form
    with st.form("login_form", clear_on_submit=False):
        email = st.text_input("Email", placeholder="you@example.com")
        password = st.text_input("Password", type="password", placeholder="••••••••")
        submitted = st.form_submit_button("Sign In")

    if submitted:
        result = login_user(email, password)
        if result["success"]:
            st.session_state.authenticated = True
            st.session_state.user = result["user"]
            st.session_state.page = "dashboard"
            st.rerun()
        else:
            st.markdown(f'<div class="custom-error">❌ {result["message"]}</div>', unsafe_allow_html=True)

    # Footer
    st.markdown('<div class="auth-footer">Don\'t have an account?</div>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        st.markdown('<div class="link-btn">', unsafe_allow_html=True)
        if st.button("Create one", key="go_register"):
            go_to("register")
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)


# ──────────────────────────────────────────────────────
# PAGE: Register
# ──────────────────────────────────────────────────────
def render_register():
    st.markdown("""
    <div class="auth-card">
        <div class="brand-section">
            <div class="brand-icon">👤</div>
            <p class="brand-title">LexAssist</p>
            <p class="brand-sub">Create your account</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    with st.form("register_form", clear_on_submit=False):
        name = st.text_input("Full Name", placeholder="John Doe")
        email = st.text_input("Email", placeholder="you@example.com")
        password = st.text_input("Password", type="password", placeholder="Min. 6 characters")
        confirm_password = st.text_input("Confirm Password", type="password", placeholder="Re-enter password")
        submitted = st.form_submit_button("Create Account")

    if submitted:
        if not name or not email or not password or not confirm_password:
            st.markdown('<div class="custom-error">❌ Please fill in all fields.</div>', unsafe_allow_html=True)
        elif password != confirm_password:
            st.markdown('<div class="custom-error">❌ Passwords do not match.</div>', unsafe_allow_html=True)
        else:
            result = register_user(name, email, password)
            if result["success"]:
                st.session_state.authenticated = True
                st.session_state.user = result["user"]
                st.session_state.page = "dashboard"
                st.rerun()
            else:
                st.markdown(f'<div class="custom-error">❌ {result["message"]}</div>', unsafe_allow_html=True)

    st.markdown('<div class="auth-footer">Already have an account?</div>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        st.markdown('<div class="link-btn">', unsafe_allow_html=True)
        if st.button("Sign in", key="go_login"):
            go_to("login")
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)


# ──────────────────────────────────────────────────────
# PAGE: Dashboard
# ──────────────────────────────────────────────────────
def render_dashboard():
    if not st.session_state.authenticated:
        st.session_state.page = "login"
        st.rerun()
        return

    user = st.session_state.user
    created = user.get("createdAt", None)
    if created:
        from datetime import datetime
        if isinstance(created, datetime):
            date_str = created.strftime("%B %d, %Y")
        else:
            date_str = str(created)
    else:
        date_str = "N/A"

    # Dashboard header with logout
    hcol1, hcol2 = st.columns([3, 1])
    with hcol1:
        st.markdown('<p class="dash-title">⚖️ LexAssist Dashboard</p>', unsafe_allow_html=True)
    with hcol2:
        st.markdown('<div class="logout-btn">', unsafe_allow_html=True)
        if st.button("🚪 Logout", key="logout_btn"):
            logout()
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    # User info cards
    st.markdown(f"""
    <div class="info-grid">
        <div class="info-card">
            <div class="info-label">Full Name</div>
            <div class="info-value">{user.get("name", "—")}</div>
        </div>
        <div class="info-card">
            <div class="info-label">Email</div>
            <div class="info-value">{user.get("email", "—")}</div>
        </div>
        <div class="info-card">
            <div class="info-label">Member Since</div>
            <div class="info-value">{date_str}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Welcome banner
    st.markdown("""
    <div class="welcome-banner">
        <div class="welcome-emoji">🎉</div>
        <p class="welcome-text">
            Welcome to <strong>LexAssist</strong>! Your account is secured with
            industry-standard bcrypt encryption. You're all set to explore your
            legal assistant dashboard.
        </p>
    </div>
    """, unsafe_allow_html=True)


# ──────────────────────────────────────────────────────
# Router
# ──────────────────────────────────────────────────────
page = st.session_state.page

if page == "dashboard":
    render_dashboard()
elif page == "register":
    render_register()
else:
    render_login()
