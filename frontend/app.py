import streamlit as st
import requests
import json
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="LexAssist - AI Legal & Tax Assistant",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Backend API URL
API_URL = "http://localhost:8000"

# Initialize session state
if 'query_history' not in st.session_state:
    st.session_state.query_history = []

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #666;
        text-align: center;
        margin-bottom: 2rem;
    }
    .disclaimer-box {
        background-color: #fff3cd;
        border-left: 5px solid #ffc107;
        padding: 1rem;
        margin: 1rem 0;
        border-radius: 5px;
        color: #000000;
    }
    .response-box {
        background-color: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        border: 1px solid #dee2e6;
        margin: 1rem 0;
    }
    .suggestion-box {
        background-color: #e7f3ff;
        padding: 0.8rem;
        border-radius: 5px;
        margin: 0.5rem 0;
        cursor: pointer;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/000000/law.png", width=80)
    st.title("⚖️ LexAssist")
    st.markdown("---")
    
    page = st.radio(
        "Navigation",
        ["🏠 Home", "⚖️ Ask Legal Question", "💰 Tax Assistant", "📄 Document Explanation", "📜 Query History", "ℹ️ About"]
    )
    
    st.markdown("---")
    st.markdown("### Quick Stats")
    st.metric("Queries Processed", len(st.session_state.query_history))
    
    st.markdown("---")
    st.markdown("### ⚠️ Important Notice")
    st.info("This is an AI assistant and does NOT provide legal advice. Always consult a qualified professional.")

# Main content
if page == "🏠 Home":
    st.markdown('<div class="main-header">⚖️ Welcome to LexAssist</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Your AI-Powered Legal & Tax Assistant</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("### ⚖️ Legal Assistance")
        st.write("Get simplified explanations of legal concepts, statutes, and your rights.")
        
    with col2:
        st.markdown("### 💰 Tax Guidance")
        st.write("Understand tax laws, deductions, and filing requirements in simple terms.")
        
    with col3:
        st.markdown("### 📄 Document Analysis")
        st.write("Upload legal documents and get easy-to-understand explanations.")
    
    st.markdown("---")
    st.markdown("### 🚀 Getting Started")
    st.write("1. Choose a service from the sidebar")
    st.write("2. Ask your question or upload a document")
    st.write("3. Get instant AI-powered insights")
    
    st.markdown('<div class="disclaimer-box">⚠️ <strong>Disclaimer:</strong> LexAssist provides general information only and is not a substitute for professional legal or tax advice.</div>', unsafe_allow_html=True)

elif page == "⚖️ Ask Legal Question":
    st.markdown('<div class="main-header">⚖️ Legal Question Assistant</div>', unsafe_allow_html=True)
    
    st.write("Ask any legal question and get a simplified explanation.")
    
    # Query input with form for Enter key submission
    with st.form(key="legal_question_form", clear_on_submit=False):
        query = st.text_area(
            "Enter your legal question:", 
            height=100, 
            placeholder="Example: What is GST in India?",
            key="legal_query_input"
        )
        
        col1, col2 = st.columns([1, 5])
        with col1:
            submit_button = st.form_submit_button("🔍 Ask", type="primary", use_container_width=True)
    
    # Process form submission
    if submit_button:
        if query and query.strip():
            with st.spinner("Processing your question..."):
                try:
                    # Send request to backend
                    response = requests.post(
                        f"{API_URL}/ask",
                        json={"query": query, "category": "legal"},
                        timeout=30
                    )
                    
                    if response.status_code == 200:
                        data = response.json()
                        
                        # Display response
                        st.markdown('<div class="response-box">', unsafe_allow_html=True)
                        st.markdown("### 📝 Response")
                        st.write(data['response'])
                        
                        # Copy button
                        if st.button("📋 Copy Response", key="copy_legal"):
                            st.code(data['response'], language=None)
                            st.success("✅ Response ready to copy! Select the text above.")
                        
                        st.markdown('</div>', unsafe_allow_html=True)
                        
                        # Suggested questions
                        if data.get('suggested_questions'):
                            st.markdown("### 💡 Suggested Follow-up Questions")
                            for suggestion in data['suggested_questions']:
                                st.markdown(f'<div class="suggestion-box">• {suggestion}</div>', unsafe_allow_html=True)
                        
                        # Add to history
                        st.session_state.query_history.append({
                            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                            "query": query,
                            "category": "legal"
                        })
                        
                        st.success("✅ Query processed successfully!")
                    else:
                        st.error(f"Error: {response.json().get('detail', 'Unknown error')}")
                
                except requests.exceptions.ConnectionError:
                    st.error("❌ Cannot connect to backend. Make sure the FastAPI server is running on http://localhost:8000")
                except Exception as e:
                    st.error(f"❌ Error: {str(e)}")
        else:
            st.warning("⚠️ Please enter a question before submitting.")

elif page == "💰 Tax Assistant":
    st.markdown('<div class="main-header">💰 Tax Assistant</div>', unsafe_allow_html=True)
    
    st.write("Get help with tax-related questions and understand tax concepts.")
    
    # Query input with form for Enter key submission
    with st.form(key="tax_question_form", clear_on_submit=False):
        query = st.text_area(
            "Enter your tax question:", 
            height=100, 
            placeholder="Example: What is GST in India?",
            key="tax_query_input"
        )
        
        col1, col2 = st.columns([1, 5])
        with col1:
            submit_button = st.form_submit_button("🔍 Ask", type="primary", use_container_width=True)
    
    # Process form submission
    if submit_button:
        if query and query.strip():
            with st.spinner("Processing your question..."):
                try:
                    response = requests.post(
                        f"{API_URL}/ask",
                        json={"query": query, "category": "tax"},
                        timeout=30
                    )
                    
                    if response.status_code == 200:
                        data = response.json()
                        
                        st.markdown('<div class="response-box">', unsafe_allow_html=True)
                        st.markdown("### 📝 Response")
                        st.write(data['response'])
                        
                        # Copy button
                        if st.button("📋 Copy Response", key="copy_tax"):
                            st.code(data['response'], language=None)
                            st.success("✅ Response ready to copy! Select the text above.")
                        
                        st.markdown('</div>', unsafe_allow_html=True)
                        
                        if data.get('suggested_questions'):
                            st.markdown("### 💡 Suggested Follow-up Questions")
                            for suggestion in data['suggested_questions']:
                                st.markdown(f'<div class="suggestion-box">• {suggestion}</div>', unsafe_allow_html=True)
                        
                        st.session_state.query_history.append({
                            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                            "query": query,
                            "category": "tax"
                        })
                        
                        st.success("✅ Query processed successfully!")
                    else:
                        st.error(f"Error: {response.json().get('detail', 'Unknown error')}")
                
                except requests.exceptions.ConnectionError:
                    st.error("❌ Cannot connect to backend. Make sure the FastAPI server is running on http://localhost:8000")
                except Exception as e:
                    st.error(f"❌ Error: {str(e)}")
        else:
            st.warning("⚠️ Please enter a question before submitting.")

elif page == "📄 Document Explanation":
    st.markdown('<div class="main-header">📄 Document Explanation</div>', unsafe_allow_html=True)
    
    st.write("Upload a legal or tax document (PDF or TXT) and get a simplified explanation.")
    
    uploaded_file = st.file_uploader("Choose a document", type=['pdf', 'txt'])
    
    if uploaded_file:
        st.info(f"📎 File uploaded: {uploaded_file.name} ({uploaded_file.size} bytes)")
        
        if st.button("🔍 Explain Document", type="primary"):
            with st.spinner("Analyzing document..."):
                try:
                    files = {"file": (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)}
                    
                    response = requests.post(
                        f"{API_URL}/explain-document",
                        files=files,
                        timeout=60
                    )
                    
                    if response.status_code == 200:
                        data = response.json()
                        
                        st.markdown("### 📊 Document Information")
                        col1, col2 = st.columns(2)
                        with col1:
                            st.metric("Filename", data['filename'])
                        with col2:
                            st.metric("Text Length", f"{data['text_length']} characters")
                        
                        st.markdown("---")
                        
                        with st.expander("📄 Extracted Text (Preview)"):
                            st.text(data['extracted_text'])
                        
                        st.markdown('<div class="response-box">', unsafe_allow_html=True)
                        st.markdown("### 📝 AI Explanation")
                        st.write(data['explanation'])
                        
                        # Copy button
                        if st.button("📋 Copy Explanation", key="copy_doc"):
                            st.code(data['explanation'], language=None)
                            st.success("✅ Explanation ready to copy! Select the text above.")
                        
                        st.markdown('</div>', unsafe_allow_html=True)
                        
                        st.success("✅ Document analyzed successfully!")
                    else:
                        st.error(f"Error: {response.json().get('detail', 'Unknown error')}")
                
                except requests.exceptions.ConnectionError:
                    st.error("❌ Cannot connect to backend. Make sure the FastAPI server is running on http://localhost:8000")
                except Exception as e:
                    st.error(f"❌ Error: {str(e)}")

elif page == "📜 Query History":
    st.markdown('<div class="main-header">📜 Query History</div>', unsafe_allow_html=True)
    
    st.write("View your previous queries and responses.")
    
    try:
        response = requests.get(f"{API_URL}/history", timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            history = data['history']
            
            if history:
                st.info(f"📊 Total queries: {data['count']}")
                
                # Filter options
                col1, col2 = st.columns([1, 3])
                with col1:
                    filter_category = st.selectbox(
                        "Filter by category:",
                        ["All", "legal", "tax"]
                    )
                
                # Display history
                for item in history:
                    if filter_category == "All" or item['category'] == filter_category:
                        with st.expander(f"🕒 {item['timestamp']} - {item['category'].upper()}"):
                            st.markdown(f"**Query:** {item['query']}")
                            st.markdown("---")
                            st.markdown(f"**Response:**")
                            st.write(item['response'])
                            
                            if st.button("📋 Copy", key=f"copy_{item['id']}"):
                                st.code(item['response'], language=None)
                                st.success("✅ Ready to copy!")
            else:
                st.info("No queries yet. Start asking questions!")
        else:
            st.error("Failed to load history")
    
    except requests.exceptions.ConnectionError:
        st.error("❌ Cannot connect to backend. Make sure the server is running.")
    except Exception as e:
        st.error(f"❌ Error: {str(e)}")

elif page == "ℹ️ About":
    st.markdown('<div class="main-header">ℹ️ About LexAssist</div>', unsafe_allow_html=True)
    
    st.markdown("""
    ### What is LexAssist?
    
    LexAssist is an AI-powered legal and tax assistant designed to help users understand complex legal and tax concepts in simple, easy-to-understand language.
    
    ### Features
    
    - **Legal Question Assistant**: Ask any legal question and get simplified explanations
    - **Tax Assistant**: Get help with tax-related queries and understand tax laws
    - **Document Explanation**: Upload legal/tax documents and receive plain-language explanations
    - **Query History**: Track your previous questions
    - **Suggested Questions**: Get relevant follow-up question suggestions
    
    ### Technology Stack
    
    **Frontend:**
    - Streamlit (Python)
    - Clean, intuitive UI
    
    **Backend:**
    - FastAPI
    - RESTful API architecture
    
    **AI Integration:**
    - OpenAI API
    - Natural language processing
    
    ### Important Disclaimer
    
    ⚠️ **LexAssist is an informational tool only.** The responses provided are AI-generated and should not be considered professional legal or tax advice. Always consult with a qualified attorney or tax professional for specific legal or tax matters.
    
    ### Version
    
    Current Version: 1.0.0
    
    ### Support
    
    For issues or questions, please refer to the README.md file in the project repository.
    """)
    
    st.markdown("---")
    st.markdown("### 📊 Query History")
    
    if st.session_state.query_history:
        for i, item in enumerate(reversed(st.session_state.query_history[-10:])):
            with st.expander(f"Query {len(st.session_state.query_history) - i}: {item['query'][:50]}..."):
                st.write(f"**Time:** {item['timestamp']}")
                st.write(f"**Category:** {item['category']}")
                st.write(f"**Query:** {item['query']}")
    else:
        st.info("No queries yet. Start asking questions!")
