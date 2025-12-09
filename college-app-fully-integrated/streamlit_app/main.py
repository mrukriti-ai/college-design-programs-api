"""
College Design Programs - Streamlit Frontend
Main application entry point with navigation and session state management.
"""

import streamlit as st
from streamlit_app.pages import home, profile, results, details, admin
from streamlit_app.utils.session_state import init_session_state
from streamlit_app.utils.config import load_config

def main():
    """Main application function"""
    
    # Page configuration
    st.set_page_config(
        page_title="College Design Programs",
        page_icon="🎨",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Initialize session state
    init_session_state()
    
    # Load configuration
    config = load_config()
    
    # Custom CSS for better styling
    st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #2c3e50;
        margin-bottom: 1rem;
    }
    .card {
        background-color: #f8f9fa;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #1f77b4;
        margin-bottom: 1rem;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Sidebar navigation
    with st.sidebar:
        st.markdown("## 🎨 College Design Programs")
        st.markdown("---")
        
        # Navigation menu
        page = st.selectbox(
            "Navigation",
            ["🏠 Home", "🔍 Find Colleges", "📋 Results", "⭐ Favorites", "⚙️ Admin"],
            index=0
        )
        
        st.markdown("---")
        
        # Display current user info if available
        if st.session_state.get('user_profile'):
            st.markdown("### Current Profile")
            user_profile_data = st.session_state.user_profile
            st.markdown(f"**Name:** {user_profile_data.get('name', 'N/A')}")
            st.markdown(f"**Program:** {user_profile_data.get('program_interest', 'N/A')}")
            st.markdown(f"**Budget:** {user_profile_data.get('budget_range', 'N/A')}")
        
        # Display favorites count
        if st.session_state.get('favorites'):
            st.markdown(f"### Favorites ({len(st.session_state.favorites)})")
    
    # Main content area
    if page == "🏠 Home":
        home.show()
    elif page == "🔍 Find Colleges":
        profile.show()
    elif page == "📋 Results":
        results.show()
    elif page == "⭐ Favorites":
        results.show_favorites()
    elif page == "⚙️ Admin":
        admin.show()

if __name__ == "__main__":
    main() 