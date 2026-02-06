import streamlit as st
import time

def show_login():
    # Center the login form
    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        st.markdown("<br><br><br>", unsafe_allow_html=True)
        
        with st.container():
            st.markdown("""
            <div style="text-align: center; margin-bottom: 2rem;">
                <h1>Lex-Assist</h1>
                <p>Secure Legal Operating System</p>
            </div>
            """, unsafe_allow_html=True)
            
            with st.form("login_form"):
                username = st.text_input("Username", placeholder="Enter username")
                password = st.text_input("Password", type="password", placeholder="Enter password")
                
                submitted = st.form_submit_button("Login", use_container_width=True, type="primary")
                
                if submitted:
                    if username == "admin" and password == "password":
                        with st.spinner("Authenticating..."):
                            time.sleep(1) # Fake delay for UX
                            st.session_state["authenticated"] = True
                            st.rerun()
                    else:
                        st.error("Invalid credentials. Please try again.")

        st.markdown("""
        <div style="text-align: center; margin-top: 5rem; color: #666; font-size: 0.8rem;">
            &copy; 2026 Lex-Assist Systems. Authorized Personnel Only.
        </div>
        """, unsafe_allow_html=True)
