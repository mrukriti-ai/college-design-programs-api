"""
Reusable form components for the Streamlit app.
Provides consistent form elements across different pages.
"""

import streamlit as st
from utils.config import PROGRAM_TYPES, BUDGET_RANGES, LOCATIONS, EDUCATION_LEVELS

def create_user_profile_form():
    """Create a user profile form component"""
    
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
        
        # Additional preferences
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
        
        return {
            'submitted': submitted,
            'name': name,
            'email': email,
            'education_level': education_level,
            'program_interest': program_interest,
            'budget_range': budget_range,
            'location_preference': location_preference,
            'degree_level': degree_level,
            'include_international': include_international
        }

def create_search_filter_form():
    """Create a search filter form component"""
    
    with st.form("search_filter_form"):
        st.markdown('<h3>Refine Your Search</h3>', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            program_filter = st.multiselect(
                "Program Types",
                PROGRAM_TYPES,
                default=PROGRAM_TYPES
            )
            
            budget_filter = st.multiselect(
                "Budget Ranges",
                BUDGET_RANGES,
                default=BUDGET_RANGES
            )
        
        with col2:
            location_filter = st.multiselect(
                "Locations",
                LOCATIONS,
                default=LOCATIONS
            )
            
            degree_filter = st.multiselect(
                "Degree Levels",
                ["Bachelor", "Master", "Certificate"],
                default=["Bachelor", "Master", "Certificate"]
            )
        
        # Additional filters
        max_tuition = st.slider(
            "Maximum Tuition (per year)",
            min_value=0,
            max_value=100000,
            value=100000,
            step=5000
        )
        
        submitted = st.form_submit_button("🔍 Apply Filters", type="primary")
        
        return {
            'submitted': submitted,
            'program_filter': program_filter,
            'budget_filter': budget_filter,
            'location_filter': location_filter,
            'degree_filter': degree_filter,
            'max_tuition': max_tuition
        }

def create_contact_form():
    """Create a contact form component"""
    
    with st.form("contact_form"):
        st.markdown('<h3>Contact Us</h3>', unsafe_allow_html=True)
        
        name = st.text_input("Your Name", placeholder="Enter your name")
        email = st.text_input("Your Email", placeholder="your.email@example.com")
        subject = st.selectbox(
            "Subject",
            ["General Inquiry", "Technical Support", "Feature Request", "Bug Report", "Other"]
        )
        message = st.text_area("Message", placeholder="Enter your message here...", height=150)
        
        submitted = st.form_submit_button("📧 Send Message", type="primary")
        
        return {
            'submitted': submitted,
            'name': name,
            'email': email,
            'subject': subject,
            'message': message
        } 