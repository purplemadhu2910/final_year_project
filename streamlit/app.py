import streamlit as st
import os

# Page Config - Must be the first Streamlit command
st.set_page_config(
    page_title="Lex-Assist | Legal OS",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Load Custom CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

try:
    local_css("styles/main.css")
except FileNotFoundError:
    st.warning("CSS file not found. Styles may not load correctly.")

# --- Session State for Navigation ---
if "page" not in st.session_state:
    st.session_state.page = "Dashboard"

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

def set_page(page_name):
    st.session_state.page = page_name

def logout():
    st.session_state.authenticated = False
    st.rerun()

# --- Authentication Check ---
if not st.session_state.authenticated:
    from views import login
    login.show_login()

else:
    # --- Top Navigation Header ---
    # Using columns to create a specific header bar for feature quick-access
    _, t1, t2, t3, _ = st.columns([1, 2, 2, 2, 1])

    with t1:
        if st.button("AI Analysis", use_container_width=True, type="primary" if st.session_state.page == "AI Analysis" else "secondary"):
            set_page("AI Analysis")
    with t2:
        if st.button("Tax Intelligence", use_container_width=True, type="primary" if st.session_state.page == "Tax Intelligence" else "secondary"):
            set_page("Tax Intelligence")
    with t3:
        if st.button("Legal Assistant", use_container_width=True, type="primary" if st.session_state.page == "Legal Assistant" else "secondary"):
            set_page("Legal Assistant")

    # --- Sidebar ---
    with st.sidebar:
        st.markdown('<div class="legal-card"><h3>Lex-Assist</h3><small>System Status: <span style="color:#2E7D32">● Online</span></small></div>', unsafe_allow_html=True)
        
        st.title("Navigation")
        
        # We use the session state 'page' to drive the radio button
        # but we also capture changes to it via the key argument automatically
        selected_page = st.radio(
            "Go to",
            ["Dashboard", "Documents", "AI Analysis", "Legal Assistant", "Compliance Center", "Tax Intelligence", "Settings"],
            label_visibility="collapsed",
            key="page"
        )
        
        st.markdown("---")
        st.caption("Active Case: **State v. Kumar**")
        st.caption("User: **Senior Advocate**")
        
        st.markdown("---")
        if st.button("Logout"):
            logout()

    # --- Main Page Routing ---
    if st.session_state.page == "Dashboard":
        from views import dashboard
        dashboard.show()

    elif st.session_state.page == "Documents":
        from views import documents
        documents.show()
        
    elif st.session_state.page == "AI Analysis":
        from views import analysis
        analysis.show()

    elif st.session_state.page == "Legal Assistant":
        from views import chat
        chat.show()

    elif st.session_state.page == "Compliance Center":
        from views import compliance
        compliance.show()

    elif st.session_state.page == "Tax Intelligence":
        from views import tax
        tax.show()

    elif st.session_state.page == "Settings":
        from views import settings
        settings.show()
