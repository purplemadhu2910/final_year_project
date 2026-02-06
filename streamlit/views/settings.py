import streamlit as st

def show():
    st.title("System Settings")
    
    tab1, tab2, tab3 = st.tabs(["User Profile", "System Configuration", "Audit Logs"])
    
    with tab1:
        c1, c2 = st.columns([1, 2])
        with c1:
            st.image("https://www.w3schools.com/howto/img_avatar.png", width=150)
        with c2:
            st.text_input("Full Name", "Senior Partner", disabled=True)
            st.text_input("Role", "Admin / Partner", disabled=True)
            st.text_input("Email", "partner@firm.legal")
            st.button("Update Profile")

    with tab2:
        st.toggle("Dark Mode Enforcement", value=True)
        st.toggle("Enable Two-Factor Authentication (2FA)", value=True)
        st.selectbox("Data Residency", ["India (Mumbai - AWS)", "India (Hyderabad - Azure)", "India (Delhi - GCP)"])
        st.number_input("Session Timeout (Minutes)", value=30)
        
    with tab3:
        st.subheader("Security Audit Trail")
        st.dataframe([
            {"Timestamp": "2024-01-31 10:45:01", "User": "Partner", "Action": "Viewed Document", "Resource": "NDA_Alpha.pdf"},
            {"Timestamp": "2024-01-31 10:42:12", "User": "Partner", "Action": "Exported Report", "Resource": "Risk_Analysis_vFinal.pdf"},
            {"Timestamp": "2024-01-31 09:15:00", "User": "System", "Action": "Backup Created", "Resource": "Daily_Backup_0131.zip"},
        ], use_container_width=True)

