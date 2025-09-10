"""
Home page for the College Design Programs app.
Displays welcome message, value proposition, and call-to-action.
"""

import streamlit as st
from utils.config import PROGRAM_TYPES

def show():
    """Display the home page"""
    
    # Main header
    st.markdown('<h1 class="main-header">🎨 Find Your Perfect Design Program</h1>', unsafe_allow_html=True)
    
    # Value proposition
    st.markdown("""
    <div class="card">
        <h2>Discover Top Design Schools Worldwide</h2>
        <p>Find the perfect college for your design career with our comprehensive database of 
        design programs from around the world. Whether you're interested in Graphic Design, 
        UX/UI, Fashion, Product Design, Architecture, or Animation, we'll help you find 
        programs that match your interests, budget, and location preferences.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Features section
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="card">
            <h3>🔍 Smart Search</h3>
            <p>Filter by program type, budget range, and location to find your perfect match.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="card">
            <h3>🌍 Global Coverage</h3>
            <p>Explore design programs from top schools across North America, Europe, Asia, and Australia.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="card">
            <h3>⭐ Save Favorites</h3>
            <p>Save your favorite programs and compare them side by side.</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Supported programs
    st.markdown('<h2 class="sub-header">Supported Design Programs</h2>', unsafe_allow_html=True)
    
    program_cols = st.columns(3)
    for i, program in enumerate(PROGRAM_TYPES):
        with program_cols[i % 3]:
            st.markdown(f"• **{program}**")
    
    # Call to action
    st.markdown("---")
    st.markdown('<h2 class="sub-header">Ready to Find Your Perfect Program?</h2>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🚀 Start Your Search", type="primary", use_container_width=True):
            st.success("Navigate to '🔍 Find Colleges' to begin your search!")
    
    # Quick stats (placeholder for now)
    st.markdown("---")
    st.markdown('<h3>📊 Quick Stats</h3>', unsafe_allow_html=True)
    
    stats_col1, stats_col2, stats_col3, stats_col4 = st.columns(4)
    
    with stats_col1:
        st.metric("Design Programs", "100+")
    
    with stats_col2:
        st.metric("Countries", "25+")
    
    with stats_col3:
        st.metric("Program Types", "6")
    
    with stats_col4:
        st.metric("Budget Ranges", "4")
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: #666;'>
        <p>🎨 College Design Programs - Your gateway to design education worldwide</p>
    </div>
    """, unsafe_allow_html=True) 