import streamlit as st

def show():
    st.title("Compliance & Risk Center")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("Regulatory Tracking")
        st.markdown("""
        <div class="legal-card">
            <div style="display: flex; justify-content: space-between;">
                <h3>DPDP Readiness</h3>
                <span class="status-indicator status-safe">Compliant</span>
            </div>
            <div style="color: #b0b0b0; font-size: 0.9rem; margin-bottom: 10px;">Last Audit: Jan 10, 2024</div>
            <progress value="100" max="100" style="width: 100%; height: 8px;"></progress>
        </div>
        
        <div class="legal-card">
            <div style="display: flex; justify-content: space-between;">
                <h3>IT Act (SPDI) Rules</h3>
                <span class="status-indicator status-medium">Review Needed</span>
            </div>
            <div style="color: #b0b0b0; font-size: 0.9rem; margin-bottom: 10px;">New amendment passed. Update privacy policy.</div>
            <progress value="75" max="100" style="width: 100%; height: 8px;"></progress>
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.subheader("Pending Tasks")
        tasks = [
            {"Task": "Sign DPA with Vendor X", "Due": "Today", "Priority": "High"},
            {"Task": "Q1 Compliance Training", "Due": "Feb 5", "Priority": "Medium"},
            {"Task": "Update Cookie Policy", "Due": "Feb 10", "Priority": "Low"},
        ]
        
        for t in tasks:
            p_color = "#D32F2F" if t['Priority'] == "High" else "#FFA000" if t['Priority'] == "Medium" else "#2E7D32"
            st.markdown(f"""
            <div class="legal-card" style="padding: 10px; border-left: 3px solid {p_color};">
                <div style="font-weight: 600;">{t['Task']}</div>
                <div style="font-size: 0.8rem; color: #b0b0b0;">Due: {t['Due']}</div>
            </div>
            """, unsafe_allow_html=True)

