"""
Simplified College Design Programs App for Testing
"""

import streamlit as st

def main():
    """Main application function"""
    
    # Page configuration
    st.set_page_config(
        page_title="College Design Programs",
        page_icon="🎨",
        layout="wide"
    )
    
    # Main header
    st.markdown("# 🎨 College Design Programs")
    st.markdown("---")
    
    # Welcome message
    st.markdown("## Welcome to College Design Programs!")
    st.markdown("Find the perfect design program for your future.")
    
    # Basic functionality
    st.markdown("### 🔍 Search Colleges")
    
    # Simple search form
    with st.form("search_form"):
        program_type = st.selectbox(
            "Program Type",
            ["Graphic Design", "UX/UI", "Fashion", "Product Design", "Architecture", "Animation"]
        )
        
        budget = st.selectbox(
            "Budget Range",
            ["Under 20k", "20k-40k", "40k-60k", "Over 60k"]
        )
        
        location = st.selectbox(
            "Location",
            ["North America", "Europe", "Asia", "Australia", "Any"]
        )
        
        submitted = st.form_submit_button("Search Colleges")
        
        if submitted:
            st.success(f"Searching for {program_type} programs in {location} with budget {budget}")
    
    # Sample results
    st.markdown("### 📋 Sample Results")
    
    sample_colleges = [
        {"name": "Art Institute of Chicago", "program": "Graphic Design", "location": "Chicago, IL", "tuition": "$45,000"},
        {"name": "Parsons School of Design", "program": "Fashion Design", "location": "New York, NY", "tuition": "$52,000"},
        {"name": "Rhode Island School of Design", "program": "Product Design", "location": "Providence, RI", "tuition": "$48,000"}
    ]
    
    for college in sample_colleges:
        with st.container():
            st.markdown(f"**{college['name']}**")
            st.markdown(f"📍 {college['location']} | 🎨 {college['program']} | 💰 {college['tuition']}")
            st.markdown("---")

if __name__ == "__main__":
    main()
