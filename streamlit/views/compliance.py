import streamlit as st
from datetime import datetime

if "compliance_tasks" not in st.session_state:
    st.session_state.compliance_tasks = []

def check_deadlines():
    warnings = []
    today = datetime.now().date()
    for task in st.session_state.compliance_tasks:
        days_left = (task["deadline"] - today).days
        if days_left <= 3 and days_left >= 0:
            warnings.append(f"⚠️ '{task['name']}' deadline in {days_left} days!")
        elif days_left < 0:
            warnings.append(f"🚨 '{task['name']}' overdue by {abs(days_left)} days!")
    return warnings

def show():
    st.title("Compliance & Risk Center")
    
    # Show deadline warnings
    warnings = check_deadlines()
    if warnings:
        for warning in warnings:
            st.warning(warning)
    
    # Add new compliance task
    st.subheader("📅 Add Compliance Task")
    col_a, col_b = st.columns(2)
    with col_a:
        task_name = st.text_input("Task Name")
    with col_b:
        task_deadline = st.date_input("Deadline", min_value=datetime.now().date())
    
    if st.button("Add Task") and task_name:
        st.session_state.compliance_tasks.append({
            "name": task_name,
            "deadline": task_deadline,
            "added_at": datetime.now()
        })
        st.success(f"✅ Task added: {task_name}")
        st.rerun()
    
    st.markdown("---")
    
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
    
    # Show user-added tasks with deadlines
    if st.session_state.compliance_tasks:
        st.markdown("---")
        st.subheader("Your Compliance Tasks")
        for task in st.session_state.compliance_tasks:
            days_left = (task["deadline"] - datetime.now().date()).days
            status = "🟢" if days_left > 3 else "🟡" if days_left >= 0 else "🔴"
            st.write(f"{status} **{task['name']}** - Deadline: {task['deadline']} ({days_left} days)")

