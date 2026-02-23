import streamlit as st

def show():
    # --- Toolbar ---
    c1, c2, c3 = st.columns([2, 1, 1])
    with c1:
        st.markdown("### 📄 Contract_NDA_Alpha_vFinal.pdf")
    with c2:
        st.caption("AI Analysis Status")
        st.markdown("**Completed (98% Confidence)**")
    with c3:
        st.button("📥 Export Report", use_container_width=True)

    st.markdown("---")

    # --- 3-Panel Layout ---
    # Streamlit columns: Left (Viewer), Center (AI), Right (References)
    col_viewer, col_ai, col_refs = st.columns([1.5, 1.5, 1])

    # --- Panel 1: Document Viewer (Simulated) ---
    with col_viewer:
        st.subheader("Document Viewer")
        st.markdown("""
        <div style="background-color: #1e212b; padding: 20px; height: 600px; overflow-y: scroll; border: 1px solid #30363d; font-family: 'Georgia', serif; font-size: 0.95rem; line-height: 1.8; color: #d0d0d0;">
            <p><strong>NON-DISCLOSURE AGREEMENT</strong></p>
            <p>This NON-DISCLOSURE AGREEMENT (the "Agreement") is entered into as of January 15, 2024, by and between Alpha Pvt Ltd ("Disclosing Party") and Beta Solutions LLP ("Receiving Party").</p>
            <p><strong>1. CONFIDENTIAL INFORMATION</strong><br>
            For purposes of this Agreement, "Confidential Information" shall mean any and all information, whether written, oral, or visual, that is disclosed by the Disclosing Party to the Receiving Party...</p>
            <p style="background-color: rgba(211, 47, 47, 0.2); border-left: 3px solid #D32F2F; padding-left: 5px;">
            <strong>2. TERM AND TERMINATION</strong><br>
            This Agreement shall remain in effect for a period of ten (10) years from the Effective Date. The obligations of confidentiality shall survive the termination of this Agreement indefinitely.
            </p>
            <p><strong>3. EXCLUSIONS</strong><br>
            Confidential Information shall not include information that: (a) is or becomes generally available to the public other than as a result of a disclosure by the Receiving Party...</p>
            <p><strong>4. GOVERNING LAW</strong><br>
            This Agreement shall be governed by and construed in accordance with the laws of the Republic of India, and courts at New Delhi shall have exclusive jurisdiction.</p>
            <br><br><br><br><br>
            <p><em>(Scroll to view more...)</em></p>
        </div>
        """, unsafe_allow_html=True)

    # --- Panel 2: AI Analysis Layer ---
    with col_ai:
        st.subheader("AI Intelligence Layer")
        
        # Executive Summary
        with st.expander("📌 Executive Summary", expanded=True):
            st.info("Standard NDA with unusually long duration (10 years) and indefinite survival clause. Jurisdiction is New Delhi.")
        
        # Risk Analysis
        confidence_threshold = st.slider("Minimum Confidence Threshold (%)", min_value=0, max_value=100, value=85, help="Filter risks based on AI confidence score.")
        
        with st.expander("⚠️ Risk Assessment", expanded=True):
            # Define Risks
            risk1 = """
            <div class="legal-card" style="padding: 10px; border-left: 4px solid #D32F2F;">
                <strong>High Risk: Clause 2 (Term)</strong>
                <p style="font-size: 0.9rem; margin-bottom: 5px;">"Indefinite survival of confidentiality" may be deemed unreasonable in certain jurisdictions.</p>
                <code style="font-size: 0.8rem;">Confidence: 92%</code>
            </div>
            """
            
            risk2 = """
            <div class="legal-card" style="padding: 10px; border-left: 4px solid #FFA000;">
                <strong>Medium Risk: Clause 4 (Governing Law)</strong>
                <p style="font-size: 0.9rem; margin-bottom: 5px;">Ensure compliance with Indian Contract Act regarding exclusive jurisdiction clauses.</p>
                <code style="font-size: 0.8rem;">Confidence: 88%</code>
            </div>
            """
            
            visible_risks = []
            if 92 >= confidence_threshold:
                visible_risks.append(risk1)
            if 88 >= confidence_threshold:
                visible_risks.append(risk2)
                
            if visible_risks:
                st.markdown("".join(visible_risks), unsafe_allow_html=True)
            else:
                st.info(f"No risks found with confidence >= {confidence_threshold}%")

        # Clause Breakdown
        with st.expander("🔍 Clause Breakdown"):
            st.markdown("**1. Confidentiality Scope** - Broad (Standard)")
            st.markdown("**2. Non-Solicitation** - <span style='color:green'>Absent</span>", unsafe_allow_html=True)
            st.markdown("**3. Dispute Resolution** - Arbitration (AAA Rules)")

    # --- Panel 3: References & Citations ---
    with col_refs:
        st.subheader("Legal References")
        
        st.markdown("""
        <div class="legal-card" style="font-size: 0.85rem;">
            <strong>Indian Contract Act, 1872</strong>
            <p style="margin-top: 5px; color: #b0b0b0;">§ 27. Agreement in restraint of trade, void.</p>
            <a href="#" style="color: #2C74B3; text-decoration: none;">View Statute ↗</a>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="legal-card" style="font-size: 0.85rem;">
            <strong>Case Precedent</strong>
            <p><em>Percept D'Mark v. Zaheer Khan (2006)</em></p>
            <p style="margin-top: 5px; color: #b0b0b0;">Supreme Court ruling on post-term covenants.</p>
            <a href="#" style="color: #2C74B3; text-decoration: none;">Read Opinion ↗</a>
        </div>
        """, unsafe_allow_html=True)

        st.info("💡 **AI Suggestion**\nConsider negotiating the survival term to 3-5 years post-termination.")
        
        st.markdown("---")
        st.subheader("Export Report")
        with st.form("export_form"):
            st.markdown("Select format for **Legal Opinion Letter**:")
            fmt = st.radio("Format", ["PDF (Court)", "DOCX (Editable)", "JSON (Integrations)"], label_visibility="collapsed")
            st.checkbox("Include Case Citations", value=True)
            st.checkbox("Redact Confidential Info", value=False)
            
            if st.form_submit_button("Generate & Download"):
                st.success(f"Report generated in {fmt} format. Downloading...")


