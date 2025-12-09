"""
Profile page for user input and search preferences.
Collects user information and search criteria for college recommendations.
"""

import streamlit as st
from streamlit_app.utils.config import PROGRAM_TYPES, BUDGET_RANGES, LOCATIONS, EDUCATION_LEVELS
from streamlit_app.utils.session_state import update_user_profile, update_search_filters
from streamlit_app.utils.api_service import save_user_profile
from streamlit_app.components.forms import create_user_profile_form

def show():
    """Display the profile and search form page"""
    
    st.markdown('<h1 class="main-header">🔍 Find Your Perfect Design Program</h1>', unsafe_allow_html=True)
    
    # Instructions
    st.markdown("""
    <div class="card">
        <h3>Tell us about your preferences</h3>
        <p>Fill out the form below to help us find design programs that match your interests, 
        budget, and location preferences. We'll search through our database of top design schools 
        to find the perfect match for you.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # User profile form
    with st.form("user_profile_form"):
        st.markdown('<h2 class="sub-header">Your Profile</h2>', unsafe_allow_html=True)
        
        # Personal information
        col1, col2 = st.columns(2)
        
        with col1:
            name = st.text_input("Full Name", placeholder="Enter your full name")
            email = st.text_input("Email Address", placeholder="your.email@example.com")
        
        with col2:
            education_level = st.selectbox(
                "Current Education Level",
                EDUCATION_LEVELS,
                index=0
            )
        
        st.markdown('<h2 class="sub-header">Program Preferences</h2>', unsafe_allow_html=True)
        
        # Program preferences
        col1, col2 = st.columns(2)
        
        with col1:
            program_interest = st.selectbox(
                "Design Program Interest",
                PROGRAM_TYPES,
                index=0
            )
            
            budget_range = st.selectbox(
                "Budget Range (per year)",
                BUDGET_RANGES,
                index=1
            )
        
        with col2:
            location_preference = st.selectbox(
                "Location Preference",
                LOCATIONS,
                index=0
            )
        
        # Additional preferences (optional)
        st.markdown('<h3>Additional Preferences (Optional)</h3>', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            degree_level = st.multiselect(
                "Degree Level",
                ["Bachelor", "Master", "Certificate"],
                default=["Bachelor", "Master"]
            )
        
        with col2:
            include_international = st.checkbox("Include International Programs", value=True)
        
        # Form submission
        submitted = st.form_submit_button("🔍 Find Matching Programs", type="primary")
        
        if submitted:
            # Validate required fields
            if not name or not email:
                st.error("Please fill in your name and email address.")
                return
            
            # Create user profile
            user_profile = {
                'name': name,
                'email': email,
                'education_level': education_level,
                'program_interest': program_interest,
                'budget_range': budget_range,
                'location_preference': location_preference,
                'degree_level': degree_level if degree_level else None,
                'include_international': include_international
            }
            
            # Create search filters
            search_filters = {
                'program_type': program_interest,
                'budget_range': budget_range,
                'location': location_preference
            }
            
            # Save to database via API
            with st.spinner("Saving your profile..."):
                saved_profile = save_user_profile(user_profile)
            
            if saved_profile:
                # Update session state
                update_user_profile(user_profile)
                update_search_filters(search_filters)
                
                # Show success message
                st.success("✅ Profile saved to database! Navigate to '📋 Results' to see your matching programs.")
            else:
                # Still update session state even if API fails (fallback)
                update_user_profile(user_profile)
                update_search_filters(search_filters)
                st.warning("⚠️ Profile saved locally. Could not connect to database. You can still use the app.")
            
            # Display summary
            st.markdown("### Your Search Criteria")
            st.json({
                "Program Type": program_interest,
                "Budget Range": budget_range,
                "Location": location_preference,
                "Degree Levels": degree_level if degree_level else "All"
            })
    
    # Help section
    with st.expander("ℹ️ How to use this form"):
        st.markdown("""
        **Step 1:** Fill in your personal information (name and email are required)
        
        **Step 2:** Select your design program interest from the available options
        
        **Step 3:** Choose your budget range for annual tuition
        
        **Step 4:** Select your preferred location (or 'Any' for worldwide search)
        
        **Step 5:** Optionally specify degree levels and other preferences
        
        **Step 6:** Click 'Find Matching Programs' to search our database
        
        Your preferences will be saved and you can view matching programs in the Results section.
        """)
    
    # Tips section
    with st.expander("💡 Search Tips"):
        st.markdown("""
        - **Budget Range:** Choose a range that includes your maximum budget
        - **Location:** Select 'Any' to see programs from all regions
        - **Program Type:** Choose the design field that best matches your interests
        - **Degree Level:** Select multiple levels to see both undergraduate and graduate options
        
        You can always modify your preferences and search again!
        """) 