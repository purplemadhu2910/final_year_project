import streamlit as st
import pandas as pd
from datetime import datetime

def show():
    st.title("Document Workspace")
    
    # --- Upload Section ---
    with st.expander("📄 Upload New Document", expanded=True):
        st.file_uploader("Drag and drop legal documents here (PDF, DOCX, TXT)", accept_multiple_files=True)
        c1, c2 = st.columns([1, 1])
        with c1:
            st.selectbox("Document Classification", ["Agreement", "Vakalatnama", "ITR/GST", "Financials", "Legal Notice"], key="doc_class")
        with c2:
            st.text_input("Client Reference / Case ID", placeholder="e.g., CASE-2024-001")
        
        if st.button("Process & Auto-Tag"):
            st.toast("Document uploaded and sent to OCR engine.", icon="⏳")

    st.markdown("---")

    # --- Document List Filter ---
    col1, col2, col3 = st.columns([2, 1, 1])
    with col1:
        st.text_input("🔍 Search Documents", placeholder="Search by name, tag, or content...")
    with col2:
        st.selectbox("Filter by Type", ["All", "Contracts", "Filings", "Tax"], key="filter_type")
    with col3:
        st.selectbox("Sort by", ["Date Modified", "Name", "Status"], key="sort_doc")

    # --- Document List (Mock Data) ---
    st.subheader("Active Files")

    # Mock Data
    data = [
        {"Name": "NDA_Alpha_Pvt_Ltd.pdf", "Type": "Agreement", "Status": "Review Ready", "Modified": "2024-05-21", "Confidence": "98%"},
        {"Name": "ITR_Filing_AY24-25.docx", "Type": "ITR", "Status": "High Risk", "Modified": "2024-05-20", "Confidence": "85%"},
        {"Name": "Shareholders_Agreement.pdf", "Type": "Agreement", "Status": "Processing", "Modified": "2024-05-19", "Confidence": "Pending"},
        {"Name": "State_v_Kumar_Brief.pdf", "Type": "Bail Application", "Status": "Finalized", "Modified": "2024-05-15", "Confidence": "99%"},
    ]
    
    # Custom List View
    for i, doc in enumerate(data):
        status_color = "#2E7D32" if doc['Status'] == "Finalized" or doc['Status'] == "Review Ready" else "#D32F2F" if doc['Status'] == "High Risk" else "#2C74B3"
        
        with st.container():
            # Apply card styling using a markdown wrapper for the background if possible, or just use columns
            # Using columns for layout
            c1, c2, c3 = st.columns([2, 1, 1])
            
            with c1:
                st.markdown(f"**{doc['Name']}**")
                st.caption(f"{doc['Type']} • Modified: {doc['Modified']}")
            
            with c2:
                st.markdown(f"<p style='text-align: center; color: #b0b0b0; font-size: 0.8rem; margin-bottom: 0;'>AI Confidence</p><p style='text-align: center; font-weight: 600; margin-top: 0;'>{doc['Confidence']}</p>", unsafe_allow_html=True)
                
            with c3:
                st.markdown(f"<div style='text-align: right; margin-bottom: 5px;'><span style='background-color: {status_color}22; color: {status_color}; padding: 4px 8px; border-radius: 4px; font-size: 0.8rem; font-weight: 600; border: 1px solid {status_color}44;'>{doc['Status']}</span></div>", unsafe_allow_html=True)
                if st.button("Open Action Menu", key=f"btn_{i}", use_container_width=True):
                    st.toast(f"Menu actions for {doc['Name']} are currently disabled in this demo.", icon="🚧")
            
            st.markdown("---")

