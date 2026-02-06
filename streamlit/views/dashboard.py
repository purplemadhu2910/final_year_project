import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

def show():
    # --- Top Bar Controls ---
    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown(f"## Dashboard <span style='color:#b0b0b0; font-size:1rem; font-weight:400'>| {datetime.now().strftime('%B %d, %Y')}</span>", unsafe_allow_html=True)
    with col2:
        st.selectbox("Legal Jurisdiction", ["India (Corporate)", "India (Litigation)", "India (Tax)"], key="region_select")

    # --- High Level Metrics ---
    # Custom CSS for cards is effectively used here by st.metric limitation workarounds or custom html if needed.
    # We'll use columns for layout.
    
    m1, m2, m3, m4 = st.columns(4)
    
    with m1:
        st.metric(label="Active Documents", value="24", delta="3 New")
        
    with m2:
        st.metric(label="High Risk Alerts", value="5", delta="-2", delta_color="inverse")
        
    with m3:
        st.metric(label="Compliance Score", value="92%", delta="+1.5%")
        
    with m4:
        st.metric(label="System Health", value="Online", delta="Stable")

    st.markdown("---")

    # --- Main Content Split ---
    c1, c2 = st.columns([2, 1])

    with c1:
        st.subheader("Recent Activity")
        
        # Mock Activity Data
        activity_data = [
            {"Time": "10:23 AM", "Event": "Contract Analysis Completed", "File": "NDA_Alpha_Corp.pdf", "Status": "Review Ready"},
            {"Time": "09:45 AM", "Event": "Risk Flag Detected", "File": "Tax_Filing_FY24.docx", "Status": "High Risk"},
            {"Time": "09:12 AM", "Event": "User Login", "File": "-", "Status": "Auth Success"},
            {"Time": "Yesterday", "Event": "Document Uploaded", "File": "Merger_Agreement_v2.pdf", "Status": "Processing"},
        ]
        
        # Render as a clean table or custom list
        for item in activity_data:
            icon = "🟢" if item['Status'] == 'Auth Success' or item['Status'] == 'Review Ready' else "🔴" if item['Status'] == 'High Risk' else "🔵"
            
            st.markdown(f"""
            <div class="legal-card" style="padding: 1rem; margin-bottom: 0.5rem; display: flex; justify-content: space-between; align-items: center;">
                <div>
                    <div style="font-weight: 600; font-size: 0.95rem;">{icon} {item['Event']}</div>
                    <div style="color: #b0b0b0; font-size: 0.85rem;">{item['File']}</div>
                </div>
                <div style="text-align: right;">
                    <div style="font-size: 0.85rem; color: #b0b0b0;">{item['Time']}</div>
                    <div style="font-size: 0.8rem; text-transform: uppercase; letter-spacing: 0.5px;">{item['Status']}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
    with c2:
        st.subheader("System Status")
        st.markdown("""
        <div class="legal-card">
            <h3>AI Engine</h3>
            <div><span class="status-indicator status-safe"></span>NLP Core: <strong>Active</strong></div>
            <div style="margin-top: 5px;"><span class="status-indicator status-safe"></span>OCR Module: <strong>Active</strong></div>
            <div style="margin-top: 5px;"><span class="status-indicator status-medium"></span>Risk Classifier: <strong>Loaded (v2.1)</strong></div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="legal-card">
            <h3>Storage Quota</h3>
            <div style="margin-bottom: 5px; display: flex; justify-content: space-between;">
                <span>Used</span>
                <span>45%</span>
            </div>
            <div style="background-color: #30363d; height: 6px; border-radius: 3px; overflow: hidden;">
                <div style="background-color: #2C74B3; width: 45%; height: 100%;"></div>
            </div>
            <div style="margin-top: 10px; font-size: 0.8rem; color: #b0b0b0;">12.4 GB of 50 GB Used</div>
        </div>
        """, unsafe_allow_html=True)

