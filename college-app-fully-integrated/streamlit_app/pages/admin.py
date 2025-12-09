"""
Admin page for data management and Excel file upload.
Allows administrators to upload college data and view system status.
"""

import streamlit as st
import pandas as pd
from io import BytesIO
from streamlit_app.utils.config import get_admin_headers

def show():
    """Display the admin page"""
    
    st.markdown('<h1 class="main-header">⚙️ Admin Panel</h1>', unsafe_allow_html=True)
    
    # Admin authentication (simple for MVP)
    st.markdown("""
    <div class="card">
        <h3>Data Management</h3>
        <p>Upload Excel files to update the college database. Only authorized administrators 
        can access this section.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Excel upload section
    st.markdown('<h2 class="sub-header">📊 Upload College Data</h2>', unsafe_allow_html=True)
    
    # File upload
    uploaded_file = st.file_uploader(
        "Choose an Excel file",
        type=['xlsx', 'xls'],
        help="Upload an Excel file with college data. Required columns: name, location_city, location_country, program_name, program_type, degree_level, tuition_min, tuition_max"
    )
    
    if uploaded_file is not None:
        # Display file info
        st.success(f"File uploaded: {uploaded_file.name}")
        
        # Preview data
        try:
            df = pd.read_excel(uploaded_file)
            st.markdown("### 📋 Data Preview")
            st.dataframe(df.head(), use_container_width=True)
            
            # Validate required columns
            required_columns = [
                'name', 'location_city', 'location_country', 'program_name',
                'program_type', 'degree_level', 'tuition_min', 'tuition_max'
            ]
            
            missing_columns = [col for col in required_columns if col not in df.columns]
            
            if missing_columns:
                st.error(f"Missing required columns: {', '.join(missing_columns)}")
                st.info("Please ensure your Excel file contains all required columns.")
            else:
                st.success("✅ All required columns are present!")
                
                # Upload button
                if st.button("🚀 Upload to Database", type="primary"):
                    upload_to_database(uploaded_file)
        
        except Exception as e:
            st.error(f"Error reading file: {str(e)}")
            st.info("Please ensure the file is a valid Excel file.")
    
    # System status section
    st.markdown("---")
    st.markdown('<h2 class="sub-header">📈 System Status</h2>', unsafe_allow_html=True)
    
    # Mock status for now (replace with API calls later)
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Total Colleges", "100+")
    
    with col2:
        st.metric("Last Update", "2024-01-15")
    
    with col3:
        st.metric("System Status", "🟢 Online")
    
    # Data statistics
    st.markdown('<h3>📊 Data Statistics</h3>', unsafe_allow_html=True)
    
    stats_col1, stats_col2 = st.columns(2)
    
    with stats_col1:
        st.markdown("### Program Types")
        program_stats = {
            "Graphic Design": 25,
            "UX/UI": 20,
            "Fashion": 15,
            "Product Design": 18,
            "Architecture": 12,
            "Animation": 10
        }
        
        for program, count in program_stats.items():
            st.markdown(f"• **{program}:** {count} programs")
    
    with stats_col2:
        st.markdown("### Locations")
        location_stats = {
            "North America": 45,
            "Europe": 35,
            "Asia": 15,
            "Australia": 5
        }
        
        for location, count in location_stats.items():
            st.markdown(f"• **{location}:** {count} programs")
    
    # Help section
    with st.expander("ℹ️ Excel File Format"):
        st.markdown("""
        ### Required Excel Format
        
        Your Excel file must contain the following columns:
        
        | Column | Description | Required | Example |
        |--------|-------------|----------|---------|
        | name | College/University name | Yes | "Parsons School of Design" |
        | location_city | City name | Yes | "New York" |
        | location_country | Country name | Yes | "USA" |
        | program_name | Program name | Yes | "BFA Graphic Design" |
        | program_type | Program category | Yes | "Graphic Design" |
        | degree_level | Degree type | Yes | "Bachelor" |
        | tuition_min | Minimum annual tuition | Yes | 45000 |
        | tuition_max | Maximum annual tuition | Yes | 50000 |
        
        ### Optional Columns
        
        | Column | Description | Example |
        |--------|-------------|---------|
        | application_deadline | Application deadline | "2024-01-15" |
        | program_description | Program description | "Comprehensive design program..." |
        | admission_requirements | Admission requirements | "Portfolio, transcripts..." |
        | contact_email | Contact email | "admissions@college.edu" |
        | website_url | College website | "https://www.college.edu" |
        
        ### Tips
        - Use consistent formatting for dates (YYYY-MM-DD)
        - Ensure tuition values are numeric
        - Program types must match: Graphic Design, UX/UI, Fashion, Product Design, Architecture, Animation
        - Degree levels must match: Bachelor, Master, Certificate
        """)
    
    # Troubleshooting
    with st.expander("🔧 Troubleshooting"):
        st.markdown("""
        ### Common Issues
        
        **File upload fails:**
        - Check file format (must be .xlsx or .xls)
        - Ensure file is not corrupted
        - Verify file size (max 10MB)
        
        **Missing columns error:**
        - Check column names match exactly (case-sensitive)
        - Ensure no extra spaces in column names
        - Verify all required columns are present
        
        **Data validation errors:**
        - Check program_type values match allowed options
        - Verify degree_level values are correct
        - Ensure tuition values are numeric
        
        **Upload fails:**
        - Check internet connection
        - Verify admin token is valid
        - Contact system administrator
        """)

def upload_to_database(file):
    """Upload file to database (placeholder for API integration)"""
    
    with st.spinner("Uploading data to database..."):
        # Simulate upload process
        import time
        time.sleep(2)
        
        # Mock response (replace with actual API call)
        st.success("✅ Data uploaded successfully!")
        st.info("Uploaded 100 new college programs to the database.")
        
        # Show upload summary
        st.markdown("### 📊 Upload Summary")
        
        summary_col1, summary_col2 = st.columns(2)
        
        with summary_col1:
            st.metric("New Programs", "100")
            st.metric("Updated Programs", "0")
        
        with summary_col2:
            st.metric("Skipped", "0")
            st.metric("Errors", "0") 