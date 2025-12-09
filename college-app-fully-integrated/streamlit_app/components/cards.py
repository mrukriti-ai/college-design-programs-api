"""
Card components for displaying college information.
Provides reusable card UI elements for college listings.
"""

import streamlit as st
from typing import Dict, Any, Optional

def create_college_card(college: Dict[str, Any], show_favorite_button: bool = True):
    """
    Create a college information card component.
    
    Args:
        college: Dictionary containing college information
        show_favorite_button: Whether to show the favorite button
    """
    with st.container():
        st.markdown("---")
        
        # College name and location
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown(f"### {college.get('name', 'Unknown College')}")
            location = f"{college.get('location_city', '')}, {college.get('location_country', '')}"
            st.markdown(f"📍 {location}")
        
        with col2:
            if show_favorite_button:
                from streamlit_app.utils.session_state import add_to_favorites, is_favorite
                favorite_status = is_favorite(college.get('id'))
                button_text = "❤️ Remove" if favorite_status else "🤍 Add"
                if st.button(button_text, key=f"fav_{college.get('id')}"):
                    if favorite_status:
                        from streamlit_app.utils.session_state import remove_from_favorites
                        remove_from_favorites(college.get('id'))
                    else:
                        add_to_favorites(college)
                    st.rerun()
        
        # Program information
        st.markdown(f"**Program:** {college.get('program_name', 'N/A')}")
        st.markdown(f"**Type:** {college.get('program_type', 'N/A')}")
        st.markdown(f"**Degree Level:** {college.get('degree_level', 'N/A')}")
        
        # Tuition information
        tuition_min = college.get('tuition_min')
        tuition_max = college.get('tuition_max')
        if tuition_min and tuition_max:
            st.markdown(f"**Tuition:** ${tuition_min:,} - ${tuition_max:,}")
        elif tuition_min:
            st.markdown(f"**Tuition:** ${tuition_min:,}+")
        
        # Description
        description = college.get('program_description', '')
        if description:
            with st.expander("📝 Program Description"):
                st.write(description)
        
        # Website link
        website_url = college.get('website_url')
        if website_url:
            st.markdown(f"[🌐 Visit Website]({website_url})")
        
        # Application deadline
        deadline = college.get('application_deadline')
        if deadline:
            st.markdown(f"**Application Deadline:** {deadline}")
