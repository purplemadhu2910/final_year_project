import streamlit as st

def show():
    st.title("Tax Intelligence Module")
    
    # Summary Cards
    c1, c2, c3 = st.columns(3)
    with c1:
        st.metric("Est. Tax Liability", "₹12,450", "+2.4%")
    with c2:
        st.metric("Deductibles Found", "14 Items", "₹3,200 Value")
    with c3:
        st.metric("Audit Risk Score", "Low", "Safe")
        
    st.markdown("---")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("Transaction Analysis")
        st.dataframe({
            "Transaction ID": ["TX-992", "TX-993", "TX-994", "TX-995"],
            "Description": ["Legal Consultation", "Office Lease", "Software Lic.", "Client Dinner"],
            "Category": ["Professional Svc", "Rent", "Technology", "Meals/Ent."],
            "Tax Treatment": ["Deductible (100%)", "Deductible (100%)", "Amortizable", "Deductible (50%)"],
            "Amount": ["₹4,500", "₹2,000", "₹1,200", "₹350"]
        }, use_container_width=True)
        
    with col2:
        st.subheader("Jurisdiction Logic")
        st.info("Applying tax rules for: \n\n**🇮🇳 India (GST & IT Act)**\n**🏢 State GST**")
        
        with st.expander("Tax Law Reference"):
            st.markdown("""
            **Income Tax Act, 1961 (Section 37)**
            > Any expenditure (not being capital nature) laid out... wholly and exclusively for the purposes of the business.
            """)
