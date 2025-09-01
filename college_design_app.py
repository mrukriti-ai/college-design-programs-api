"""
College Design Programs - Streamlit App
A simple and functional app for discovering design programs.
"""

import streamlit as st
import pandas as pd
import plotly.express as px
from typing import List, Dict, Any

# Page configuration
st.set_page_config(
    page_title="College Design Programs",
    page_icon="🎨",
    layout="wide"
)

# Initialize session state
if 'favorites' not in st.session_state:
    st.session_state.favorites = []
if 'search_results' not in st.session_state:
    st.session_state.search_results = []
if 'show_search_results' not in st.session_state:
    st.session_state.show_search_results = False

def get_mock_data():
    """Return mock data for demonstration"""
    return [
        {
            "id": 1,
            "name": "Parsons School of Design",
            "location_city": "New York",
            "location_country": "USA",
            "program_name": "BFA in Communication Design",
            "program_type": "Graphic Design",
            "degree_level": "Bachelor",
            "tuition_min": 45000,
            "tuition_max": 50000,
            "application_deadline": "2024-01-15",
            "program_description": "Comprehensive program in visual communication and design principles.",
            "website_url": "https://www.newschool.edu/parsons/"
        },
        {
            "id": 2,
            "name": "Royal College of Art",
            "location_city": "London",
            "location_country": "UK",
            "program_name": "MA in Graphic Design",
            "program_type": "Graphic Design",
            "degree_level": "Master",
            "tuition_min": 35000,
            "tuition_max": 40000,
            "application_deadline": "2024-02-01",
            "program_description": "Advanced studies in contemporary graphic design and visual communication.",
            "website_url": "https://www.rca.ac.uk/"
        },
        {
            "id": 3,
            "name": "Central Saint Martins",
            "location_city": "London",
            "location_country": "UK",
            "program_name": "BA Fashion Design",
            "program_type": "Fashion",
            "degree_level": "Bachelor",
            "tuition_min": 25000,
            "tuition_max": 30000,
            "application_deadline": "2024-01-31",
            "program_description": "Innovative fashion design program with industry connections.",
            "website_url": "https://www.arts.ac.uk/colleges/central-saint-martins/"
        },
        {
            "id": 4,
            "name": "RISD (Rhode Island School of Design)",
            "location_city": "Providence",
            "location_country": "USA",
            "program_name": "BFA in Industrial Design",
            "program_type": "Product Design",
            "degree_level": "Bachelor",
            "tuition_min": 55000,
            "tuition_max": 60000,
            "application_deadline": "2024-01-10",
            "program_description": "Premier industrial design program with focus on innovation and sustainability.",
            "website_url": "https://www.risd.edu/"
        },
        {
            "id": 5,
            "name": "MIT Architecture",
            "location_city": "Cambridge",
            "location_country": "USA",
            "program_name": "MArch in Architecture",
            "program_type": "Architecture",
            "degree_level": "Master",
            "tuition_min": 50000,
            "tuition_max": 55000,
            "application_deadline": "2024-01-05",
            "program_description": "Cutting-edge architecture program with technology integration.",
            "website_url": "https://architecture.mit.edu/"
        },
        {
            "id": 6,
            "name": "CalArts",
            "location_city": "Valencia",
            "location_country": "USA",
            "program_name": "BFA in Character Animation",
            "program_type": "Animation",
            "degree_level": "Bachelor",
            "tuition_min": 48000,
            "tuition_max": 52000,
            "application_deadline": "2024-01-20",
            "program_description": "World-renowned animation program with industry connections.",
            "website_url": "https://calarts.edu/"
        },
        {
            "id": 7,
            "name": "Central Academy of Fine Arts",
            "location_city": "Beijing",
            "location_country": "China",
            "program_name": "BA in Digital Media Art",
            "program_type": "UX/UI",
            "degree_level": "Bachelor",
            "tuition_min": 15000,
            "tuition_max": 20000,
            "application_deadline": "2024-03-01",
            "program_description": "Leading digital media and UX design program in Asia.",
            "website_url": "https://www.cafa.edu.cn/"
        },
        {
            "id": 8,
            "name": "RMIT University",
            "location_city": "Melbourne",
            "location_country": "Australia",
            "program_name": "Bachelor of Design (Digital Media)",
            "program_type": "UX/UI",
            "degree_level": "Bachelor",
            "tuition_min": 30000,
            "tuition_max": 35000,
            "application_deadline": "2024-02-15",
            "program_description": "Innovative digital media design program with industry focus.",
            "website_url": "https://www.rmit.edu.au/"
        }
    ]

def filter_colleges(colleges: List[Dict[str, Any]], filters: Dict[str, Any]) -> List[Dict[str, Any]]:
    """Filter colleges based on criteria"""
    filtered_colleges = colleges.copy()
    
    for key, value in filters.items():
        if key == 'program_type' and value != "All":
            filtered_colleges = [c for c in filtered_colleges if c.get('program_type', '').lower() == value.lower()]
        elif key == 'location_country' and value != "Any":
            # Handle location mapping
            location_mapping = {
                "North America": "USA",
                "Europe": "UK",
                "Asia": "China",
                "Australia": "Australia"
            }
            mapped_location = location_mapping.get(value, value)
            filtered_colleges = [c for c in filtered_colleges if c.get('location_country', '').lower() == mapped_location.lower()]
        elif key == 'degree_level' and value != "Any":
            filtered_colleges = [c for c in filtered_colleges if c.get('degree_level', '').lower() == value.lower()]
    
    return filtered_colleges

def create_college_card(college: Dict[str, Any]):
    """Create a styled college card"""
    st.markdown(f"""
    <div style="background: white; padding: 1.5rem; border-radius: 12px; border: 1px solid #e9ecef; margin-bottom: 1rem; box-shadow: 0 4px 16px rgba(0,0,0,0.1);">
        <h3 style="margin: 0; color: #2c3e50;">{college['name']}</h3>
        <p><strong>Program:</strong> {college['program_name']}</p>
        <p><strong>Type:</strong> {college['program_type']}</p>
        <p><strong>Degree:</strong> {college['degree_level']}</p>
        <p><strong>Location:</strong> {college['location_city']}, {college['location_country']}</p>
        <p><strong>Tuition:</strong> ${college['tuition_min']:,} - ${college['tuition_max']:,}</p>
        <p><strong>Deadline:</strong> {college['application_deadline']}</p>
        <p style="color: #666; font-size: 0.9rem;">{college['program_description']}</p>
        <a href="{college['website_url']}" target="_blank">
            <button style="background: #667eea; color: white; border: none; padding: 0.5rem 1rem; border-radius: 8px; cursor: pointer;">
                Visit Website
            </button>
        </a>
    </div>
    """, unsafe_allow_html=True)

def display_colleges(colleges: List[Dict[str, Any]], section_name: str):
    """Display colleges with favorite buttons"""
    if colleges:
        st.markdown(f"### {section_name}")
        for college in colleges:
            create_college_card(college)
            
            # Add to favorites button
            col1, col2 = st.columns([3, 1])
            with col2:
                if college['id'] in [f['id'] for f in st.session_state.favorites]:
                    if st.button(f"❤️ Remove from Favorites", key=f"remove_{college['id']}_{section_name}"):
                        st.session_state.favorites = [f for f in st.session_state.favorites if f['id'] != college['id']]
                        st.rerun()
                else:
                    if st.button(f"🤍 Add to Favorites", key=f"add_{college['id']}_{section_name}"):
                        st.session_state.favorites.append(college)
                        st.rerun()
    else:
        st.warning(f"No programs found for {section_name}")

def main():
    st.title("🎨 College Design Programs")
    st.markdown("Discover Your Perfect Design Education Worldwide")
    
    # Demo mode message
    st.info("🎨 **Demo Mode**: Currently using sample data. All features work perfectly!")
    
    # Get all colleges
    all_colleges = get_mock_data()
    
    # Quick stats
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Programs", len(all_colleges))
    with col2:
        countries = len(set(c['location_country'] for c in all_colleges))
        st.metric("Countries", countries)
    with col3:
        program_types = len(set(c['program_type'] for c in all_colleges))
        st.metric("Program Types", program_types)
    with col4:
        st.metric("Your Favorites", len(st.session_state.favorites))
    
    # Search form
    st.markdown("### 🔍 Find Your Perfect Program")
    
    with st.form("search_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            program_type = st.selectbox(
                "Program Type",
                ["All", "Graphic Design", "UX/UI", "Fashion", "Product Design", "Architecture", "Animation"]
            )
        
        with col2:
            location = st.selectbox(
                "Location",
                ["Any", "North America", "Europe", "Asia", "Australia"]
            )
        
        degree_level = st.selectbox(
            "Degree Level",
            ["Any", "Bachelor", "Master", "Certificate"]
        )
        
        search_submitted = st.form_submit_button("🔍 Search Programs", type="primary")
        
        if search_submitted:
            # Build filters
            filters = {
                'program_type': program_type,
                'location_country': location,
                'degree_level': degree_level
            }
            
            # Filter colleges
            filtered_results = filter_colleges(all_colleges, filters)
            st.session_state.search_results = filtered_results
            st.session_state.show_search_results = True
            
            # Show results count
            st.success(f"Found {len(filtered_results)} matching programs!")
    
    # Display search results if available
    if st.session_state.show_search_results and st.session_state.search_results:
        display_colleges(st.session_state.search_results, "📋 Search Results")
    
    # Show all programs by default (if no search was performed)
    if not st.session_state.show_search_results:
        display_colleges(all_colleges, "📋 All Available Programs")
    
    # Favorites section
    if st.session_state.favorites:
        st.markdown("### ⭐ Your Favorite Programs")
        for college in st.session_state.favorites:
            create_college_card(college)
            
            if st.button(f"🗑️ Remove from Favorites", key=f"fav_remove_{college['id']}"):
                st.session_state.favorites = [f for f in st.session_state.favorites if f['id'] != college['id']]
                st.rerun()
    
    # Analytics
    st.markdown("### 📈 Analytics")
    df = pd.DataFrame(all_colleges)
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Program types distribution
        program_counts = df['program_type'].value_counts()
        fig_programs = px.pie(
            values=program_counts.values,
            names=program_counts.index,
            title='Program Types Distribution'
        )
        st.plotly_chart(fig_programs, use_container_width=True)
    
    with col2:
        # Location distribution
        location_counts = df['location_country'].value_counts()
        fig_location = px.bar(
            x=location_counts.index,
            y=location_counts.values,
            title='Programs by Country',
            labels={'x': 'Country', 'y': 'Number of Programs'}
        )
        st.plotly_chart(fig_location, use_container_width=True)

if __name__ == "__main__":
    main()
