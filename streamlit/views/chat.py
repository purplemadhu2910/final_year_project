import streamlit as st
from datetime import datetime

def show():
    st.title("Legal Assistant")
    
    # --- Context Sidebar for Chat ---
    with st.expander("📚 Active Context: NDA_Alpha_Corp.pdf", expanded=False):
        st.markdown("""
        **Summary**: Non-disclosure agreement between Alpha Corp and Beta Ltd.
        **Key Risks**: Indefinite survival clause, Delhi jurisdiction.
        """)

    # --- Chat Interface ---
    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "Good morning. I have reviewed the active documents. Ready to assist with drafting, analysis, or citations."}
        ]

    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"], avatar="⚖️" if message["role"] == "assistant" else "👤"):
            st.markdown(message["content"])

    # Chat Input
    if prompt := st.chat_input("Ask a legal question or request a draft..."):
        # Display user message
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user", avatar="👤"):
            st.markdown(prompt)

        # Mock AI Response Logic
        response_content = ""
        
        if "draft" in prompt.lower():
            response_content = """
            **Drafting Clause: Non-Compete (Standard)**
            
            > "During the Term of this Agreement and for a period of twelve (12) months thereafter, the Receiving Party shall not, directly or indirectly, engage in any business that is competitive with the Disclosing Party's business within the Territory."
            
            *Citation: Standard Commercial Practice, Delhi High Court Bar Association Templates.*
            """
        elif "explain" in prompt.lower() or "simple" in prompt.lower():
            response_content = """
            **Simplified Explanation:**
            The clause means that if the contract ends, the receiving party cannot start a similar business or work for a competitor in the same area for one year.
            """
        else:
            response_content = f"""
            Regarding **"{prompt}"**:
            
            Based on the current document set, this appears to be a standard inquiry. Please verify specific state laws as they may vary.
            
            *Reference: Indian Contract Act, 1872 § 27 (Agreement in restraint of trade)*
            """

        # Display assistant response
        with st.chat_message("assistant", avatar="⚖️"):
            st.markdown(response_content)
            
            # Action Buttons for the response
            c1, c2 = st.columns([1, 4])
            with c1:
                st.button("📜 Show Source", key=f"src_{len(st.session_state.messages)}")
            
        st.session_state.messages.append({"role": "assistant", "content": response_content})

    # --- Mode Toggles ---
    st.markdown("---")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.checkbox("Enforce Legal Tone", value=True)
    with c2:
        st.checkbox("Cite Precedents", value=True)
    with c3:
        st.button("🗑️ Clear Thread")

