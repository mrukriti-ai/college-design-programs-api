"""
Session state management utilities for the Streamlit app.
Handles user data, search results, and favorites persistence.
"""

import streamlit as st
from typing import Dict, List, Any

def init_session_state():
    """Initialize session state variables"""
    
    # User profile and preferences
    if 'user_profile' not in st.session_state:
        st.session_state.user_profile = {}
    
    # Search results
    if 'search_results' not in st.session_state:
        st.session_state.search_results = []
    
    # Selected college for details view
    if 'selected_college' not in st.session_state:
        st.session_state.selected_college = None
    
    # Favorites list
    if 'favorites' not in st.session_state:
        st.session_state.favorites = []
    
    # Search filters
    if 'search_filters' not in st.session_state:
        st.session_state.search_filters = {}
    
    # Current page state
    if 'current_page' not in st.session_state:
        st.session_state.current_page = 'home'
    
    # API configuration
    if 'api_base_url' not in st.session_state:
        st.session_state.api_base_url = "http://localhost:8000"  # Default for local development

def update_user_profile(profile_data: Dict[str, Any]):
    """Update user profile in session state"""
    st.session_state.user_profile.update(profile_data)

def add_to_favorites(college: Dict[str, Any]):
    """Add a college to favorites"""
    if college not in st.session_state.favorites:
        st.session_state.favorites.append(college)

def remove_from_favorites(college_id: int):
    """Remove a college from favorites by ID"""
    st.session_state.favorites = [
        college for college in st.session_state.favorites 
        if college.get('id') != college_id
    ]

def is_favorite(college_id: int) -> bool:
    """Check if a college is in favorites"""
    return any(college.get('id') == college_id for college in st.session_state.favorites)

def clear_search_results():
    """Clear search results"""
    st.session_state.search_results = []

def set_search_results(results: List[Dict[str, Any]]):
    """Set search results"""
    st.session_state.search_results = results

def get_search_results() -> List[Dict[str, Any]]:
    """Get current search results"""
    return st.session_state.search_results

def set_selected_college(college: Dict[str, Any]):
    """Set selected college for details view"""
    st.session_state.selected_college = college

def get_selected_college() -> Dict[str, Any]:
    """Get selected college"""
    return st.session_state.selected_college

def update_search_filters(filters: Dict[str, Any]):
    """Update search filters"""
    st.session_state.search_filters.update(filters)

def get_search_filters() -> Dict[str, Any]:
    """Get current search filters"""
    return st.session_state.search_filters

def clear_session():
    """Clear all session state (for logout/reset)"""
    keys_to_clear = [
        'user_profile', 'search_results', 'selected_college', 
        'search_filters', 'current_page'
    ]
    for key in keys_to_clear:
        if key in st.session_state:
            del st.session_state[key]
    
    # Reinitialize
    init_session_state() 