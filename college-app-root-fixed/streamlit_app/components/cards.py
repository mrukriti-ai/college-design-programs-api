"""
College card components for displaying college information.
"""

import streamlit as st
from typing import Dict, Any, Optional

def create_college_card(college: Dict[str, Any], show_favorite_button: bool = True) -> bool:
    """
    Create a college information card.
    
    Args:
        college: Dictionary containing college information
        show_favorite_button: Whether to show the favorite button
        
    Returns:
        bool: True if college was added to favorites, False otherwise
    """
    with st.container():
        st.markdown("---")
        
        # College header
        col1, col2 = st.columns([3, 1])
        
        with col1:
            st.markdown(f"### {college.get('name', 'Unknown College')}")
            st.markdown(f"**Location:** {college.get('location', 'N/A')}")
            st.markdown(f"**Program:** {college.get('program_type', 'N/A')}")
        
        with col2:
            if show_favorite_button:
                if st.button("⭐", key=f"fav_{college.get('id', 'unknown')}"):
                    return True
        
        # College details
        st.markdown(f"**Tuition:** ${college.get('tuition', 'N/A')}")
        st.markdown(f"**Duration:** {college.get('duration', 'N/A')}")
        st.markdown(f"**Description:** {college.get('description', 'No description available')}")
        
        # Rating
        if college.get('rating'):
            st.markdown(f"**Rating:** {college.get('rating')}/5 ⭐")
        
        st.markdown("---")
    
    return False

def create_college_summary_card(college: Dict[str, Any]) -> None:
    """
    Create a summary card for college information.
    
    Args:
        college: Dictionary containing college information
    """
    with st.container():
        st.markdown(f"**{college.get('name', 'Unknown College')}**")
        st.markdown(f"📍 {college.get('location', 'N/A')}")
        st.markdown(f"🎨 {college.get('program_type', 'N/A')}")
        st.markdown(f"💰 ${college.get('tuition', 'N/A')}")

def create_favorite_card(college: Dict[str, Any]) -> bool:
    """
    Create a favorite college card with remove option.
    
    Args:
        college: Dictionary containing college information
        
    Returns:
        bool: True if college was removed from favorites
    """
    with st.container():
        col1, col2 = st.columns([4, 1])
        
        with col1:
            st.markdown(f"**{college.get('name', 'Unknown College')}**")
            st.markdown(f"📍 {college.get('location', 'N/A')}")
            st.markdown(f"🎨 {college.get('program_type', 'N/A')}")
        
        with col2:
            if st.button("❌", key=f"remove_{college.get('id', 'unknown')}"):
                return True
        
        st.markdown("---")
    
    return False