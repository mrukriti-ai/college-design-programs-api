"""
Simplified College Design Programs App
Root-level file for easy Streamlit Cloud deployment
"""

import streamlit as st
import pandas as pd

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
    
    # Navigation
    st.markdown("### 🧭 Navigation")
    page = st.selectbox(
        "Choose a page:",
        ["🏠 Home", "🔍 Search Colleges", "📋 Results", "⭐ Favorites", "ℹ️ About"]
    )
    
    if page == "🏠 Home":
        show_home()
    elif page == "🔍 Search Colleges":
        show_search()
    elif page == "📋 Results":
        show_results()
    elif page == "⭐ Favorites":
        show_favorites()
    elif page == "ℹ️ About":
        show_about()

def show_home():
    """Show home page content"""
    st.markdown("### 🏠 Home")
    st.markdown("Welcome to the College Design Programs finder!")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("#### 🎨 Program Types")
        st.markdown("- Graphic Design")
        st.markdown("- UX/UI Design")
        st.markdown("- Fashion Design")
        st.markdown("- Product Design")
        st.markdown("- Architecture")
        st.markdown("- Animation")
    
    with col2:
        st.markdown("#### 🌍 Locations")
        st.markdown("- North America")
        st.markdown("- Europe")
        st.markdown("- Asia")
        st.markdown("- Australia")
    
    with col3:
        st.markdown("#### 💰 Budget Ranges")
        st.markdown("- Under $20k")
        st.markdown("- $20k - $40k")
        st.markdown("- $40k - $60k")
        st.markdown("- Over $60k")

def show_search():
    """Show search form"""
    st.markdown("### 🔍 Search Colleges")
    
    with st.form("search_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            program_type = st.selectbox(
                "Program Type",
                ["Graphic Design", "UX/UI", "Fashion", "Product Design", "Architecture", "Animation"]
            )
            
            budget = st.selectbox(
                "Budget Range",
                ["Under 20k", "20k-40k", "40k-60k", "Over 60k"]
            )
        
        with col2:
            location = st.selectbox(
                "Location",
                ["North America", "Europe", "Asia", "Australia", "Any"]
            )
            
            degree_level = st.selectbox(
                "Degree Level",
                ["Bachelor", "Master", "Certificate", "Any"]
            )
        
        submitted = st.form_submit_button("🔍 Search Colleges")
        
        if submitted:
            st.success(f"Searching for {program_type} programs in {location} with budget {budget}")
            st.session_state.search_results = True

def show_results():
    """Show search results"""
    st.markdown("### 📋 Search Results")
    
    # Sample data
    sample_colleges = [
        {
            "name": "Art Institute of Chicago",
            "program": "Graphic Design",
            "location": "Chicago, IL",
            "country": "USA",
            "tuition": "$45,000",
            "duration": "4 years",
            "rating": 4.5
        },
        {
            "name": "Parsons School of Design",
            "program": "Fashion Design",
            "location": "New York, NY",
            "country": "USA",
            "tuition": "$52,000",
            "duration": "4 years",
            "rating": 4.8
        },
        {
            "name": "Rhode Island School of Design",
            "program": "Product Design",
            "location": "Providence, RI",
            "country": "USA",
            "tuition": "$48,000",
            "duration": "4 years",
            "rating": 4.7
        },
        {
            "name": "Central Saint Martins",
            "program": "Fashion Design",
            "location": "London",
            "country": "UK",
            "tuition": "£25,000",
            "duration": "3 years",
            "rating": 4.9
        },
        {
            "name": "Design Academy Eindhoven",
            "program": "Product Design",
            "location": "Eindhoven",
            "country": "Netherlands",
            "tuition": "€15,000",
            "duration": "4 years",
            "rating": 4.6
        }
    ]
    
    # Display results
    for i, college in enumerate(sample_colleges):
        with st.container():
            col1, col2, col3 = st.columns([3, 1, 1])
            
            with col1:
                st.markdown(f"**{college['name']}**")
                st.markdown(f"📍 {college['location']}, {college['country']}")
                st.markdown(f"🎨 {college['program']}")
                st.markdown(f"💰 {college['tuition']} | ⏱️ {college['duration']}")
            
            with col2:
                st.markdown(f"⭐ {college['rating']}/5")
            
            with col3:
                if st.button("⭐", key=f"fav_{i}"):
                    st.success("Added to favorites!")
            
            st.markdown("---")

def show_favorites():
    """Show favorites page"""
    st.markdown("### ⭐ Your Favorites")
    st.info("Favorites feature coming soon! Use the search to find colleges you like.")

def show_about():
    """Show about page"""
    st.markdown("### ℹ️ About College Design Programs")
    st.markdown("""
    This app helps you find the perfect design program for your future career.
    
    **Features:**
    - 🔍 Search by program type, location, and budget
    - 📋 View detailed college information
    - ⭐ Save your favorite colleges
    - 🌍 International program options
    
    **Supported Program Types:**
    - Graphic Design
    - UX/UI Design
    - Fashion Design
    - Product Design
    - Architecture
    - Animation
    
    **Locations:**
    - North America (USA, Canada, Mexico)
    - Europe (UK, Germany, France, Netherlands, etc.)
    - Asia (India, China, Japan, Singapore, etc.)
    - Australia & New Zealand
    """)

if __name__ == "__main__":
    main()
