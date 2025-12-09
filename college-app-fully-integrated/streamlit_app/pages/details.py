"""
Details page for displaying comprehensive college information.
Shows detailed information about a selected college program.
"""

import streamlit as st
from streamlit_app.utils.session_state import get_selected_college, add_to_favorites, remove_from_favorites, is_favorite

def show():
    """Display the college details page"""
    
    college = get_selected_college()
    
    if not college:
        st.warning("No college selected. Please go back to results and select a college.")
        st.info("Navigate to '📋 Results' to view and select colleges.")
        return
    
    # Header with college name
    st.markdown(f'<h1 class="main-header">🎓 {college.get("name", "College Details")}</h1>', unsafe_allow_html=True)
    
    # Back button
    if st.button("← Back to Results"):
        st.rerun()
    
    # College overview card
    st.markdown('<h2 class="sub-header">Program Overview</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Main program information
        st.markdown(f"""
        <div class="card">
            <h3>{college.get('program_name', 'Program Name')}</h3>
            <p><strong>Program Type:</strong> {college.get('program_type', 'N/A')}</p>
            <p><strong>Degree Level:</strong> {college.get('degree_level', 'N/A')}</p>
            <p><strong>Location:</strong> {college.get('location_city', 'N/A')}, {college.get('location_country', 'N/A')}</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        # Quick actions
        st.markdown("### Quick Actions")
        
        # Favorite button
        college_id = college.get('id')
        if college_id:
            if is_favorite(college_id):
                if st.button("💔 Remove from Favorites", use_container_width=True):
                    remove_from_favorites(college_id)
                    st.success("Removed from favorites!")
                    st.rerun()
            else:
                if st.button("❤️ Add to Favorites", use_container_width=True):
                    add_to_favorites(college)
                    st.success("Added to favorites!")
                    st.rerun()
        
        # Contact button
        if college.get('contact_email'):
            st.markdown(f"[📧 Contact Admissions](mailto:{college['contact_email']})")
        
        # Website button
        if college.get('website_url'):
            st.markdown(f"[🌐 Visit Website]({college['website_url']})")
    
    # Detailed information sections
    col1, col2 = st.columns(2)
    
    with col1:
        # Tuition information
        st.markdown('<h3>💰 Tuition & Costs</h3>', unsafe_allow_html=True)
        
        tuition_min = college.get('tuition_min')
        tuition_max = college.get('tuition_max')
        
        if tuition_min and tuition_max:
            if tuition_min == tuition_max:
                st.metric("Annual Tuition", f"${tuition_min:,}")
            else:
                st.metric("Annual Tuition Range", f"${tuition_min:,} - ${tuition_max:,}")
        elif tuition_min:
            st.metric("Annual Tuition (Min)", f"${tuition_min:,}")
        else:
            st.info("Tuition information not available")
        
        # Application deadline
        deadline = college.get('application_deadline')
        if deadline:
            st.metric("Application Deadline", deadline)
        else:
            st.info("Application deadline not available")
    
    with col2:
        # Location information
        st.markdown('<h3>📍 Location</h3>', unsafe_allow_html=True)
        
        city = college.get('location_city', 'N/A')
        country = college.get('location_country', 'N/A')
        
        st.markdown(f"""
        <div class="card">
            <p><strong>City:</strong> {city}</p>
            <p><strong>Country:</strong> {country}</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Program description
    if college.get('program_description'):
        st.markdown('<h3>📚 Program Description</h3>', unsafe_allow_html=True)
        st.markdown(f"""
        <div class="card">
            <p>{college['program_description']}</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Admission requirements
    if college.get('admission_requirements'):
        st.markdown('<h3>📋 Admission Requirements</h3>', unsafe_allow_html=True)
        st.markdown(f"""
        <div class="card">
            <p>{college['admission_requirements']}</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Contact information
    st.markdown('<h3>📞 Contact Information</h3>', unsafe_allow_html=True)
    
    contact_col1, contact_col2 = st.columns(2)
    
    with contact_col1:
        if college.get('contact_email'):
            st.markdown(f"**Email:** {college['contact_email']}")
        else:
            st.info("Email not available")
    
    with contact_col2:
        if college.get('website_url'):
            st.markdown(f"**Website:** [{college['website_url']}]({college['website_url']})")
        else:
            st.info("Website not available")
    
    # Action buttons
    st.markdown("---")
    st.markdown('<h3>🎯 Next Steps</h3>', unsafe_allow_html=True)
    
    action_col1, action_col2, action_col3 = st.columns(3)
    
    with action_col1:
        if st.button("📧 Contact Admissions", use_container_width=True):
            if college.get('contact_email'):
                st.info(f"Email: {college['contact_email']}")
            else:
                st.warning("Contact email not available")
    
    with action_col2:
        if st.button("🌐 Visit Website", use_container_width=True):
            if college.get('website_url'):
                st.markdown(f"[Open website]({college['website_url']})")
            else:
                st.warning("Website not available")
    
    with action_col3:
        if st.button("📄 Download Info", use_container_width=True):
            st.info("Download functionality will be implemented later.")
    
    # Similar programs suggestion (placeholder)
    st.markdown("---")
    st.markdown('<h3>🔍 Similar Programs</h3>', unsafe_allow_html=True)
    st.info("Similar programs feature will be implemented later.")
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: #666;'>
        <p>💡 Tip: Add this program to your favorites to compare with others later!</p>
    </div>
    """, unsafe_allow_html=True) 