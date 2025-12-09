"""
Results page for displaying college search results.
Shows matching colleges with filtering options and college cards.
"""

import streamlit as st
from typing import List, Dict, Any
from utils.session_state import (
    get_search_results, get_search_filters, set_selected_college,
    add_to_favorites, remove_from_favorites, is_favorite
)
from components.cards import create_college_card
from components.filters import create_results_filter

def show():
    """Display the search results page"""
    
    st.markdown('<h1 class="main-header">📋 Search Results</h1>', unsafe_allow_html=True)
    
    # Get current search results and filters
    results = get_search_results()
    filters = get_search_filters()
    
    # Check if user has searched
    if not filters:
        st.warning("Please complete your profile and search preferences first.")
        st.info("Navigate to '🔍 Find Colleges' to set up your search criteria.")
        return
    
    # Display current search criteria
    st.markdown('<h2 class="sub-header">Your Search Criteria</h2>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Program Type", filters.get('program_type', 'N/A'))
    with col2:
        st.metric("Budget Range", filters.get('budget_range', 'N/A'))
    with col3:
        st.metric("Location", filters.get('location', 'N/A'))
    
    # Results filter section
    st.markdown('<h2 class="sub-header">Filter Results</h2>', unsafe_allow_html=True)
    
    # Mock results for now (replace with API call later)
    if not results:
        # Generate mock results for demonstration
        results = generate_mock_results(filters)
    
    # Apply additional filters
    filtered_results = apply_filters(results)
    
    # Display results count
    st.markdown(f"### Found {len(filtered_results)} matching programs")
    
    # Results display
    if filtered_results:
        display_results(filtered_results)
    else:
        st.info("No programs match your current criteria. Try adjusting your filters.")
        
        # Suggestions
        st.markdown("### 💡 Suggestions:")
        st.markdown("""
        - Try broadening your location preference
        - Consider a wider budget range
        - Check different program types
        - Remove some filters to see more options
        """)
    
    # Export options
    if filtered_results:
        st.markdown("---")
        st.markdown('<h3>📤 Export Results</h3>', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("📄 Export to PDF", use_container_width=True):
                st.info("PDF export functionality will be implemented later.")
        
        with col2:
            if st.button("📧 Email Results", use_container_width=True):
                st.info("Email functionality will be implemented later.")

def show_favorites():
    """Display favorites page"""
    
    st.markdown('<h1 class="main-header">⭐ Your Favorites</h1>', unsafe_allow_html=True)
    
    favorites = st.session_state.get('favorites', [])
    
    if not favorites:
        st.info("You haven't saved any favorites yet. Search for programs and add them to your favorites!")
        return
    
    st.markdown(f"### You have {len(favorites)} favorite programs")
    
    # Display favorites
    for i, college in enumerate(favorites):
        with st.container():
            create_college_card(college, show_favorite_button=False)
            
            # Remove from favorites button
            if st.button(f"🗑️ Remove from Favorites", key=f"remove_fav_{i}"):
                remove_from_favorites(college.get('id'))
                st.rerun()

def display_results(results: List[Dict[str, Any]]):
    """Display search results as cards"""
    
    # Sort options
    col1, col2 = st.columns([3, 1])
    
    with col1:
        sort_by = st.selectbox(
            "Sort by",
            ["Name (A-Z)", "Name (Z-A)", "Tuition (Low to High)", "Tuition (High to Low)"],
            index=0
        )
    
    with col2:
        results_per_page = st.selectbox("Results per page", [10, 20, 50], index=1)
    
    # Sort results
    sorted_results = sort_results(results, sort_by)
    
    # Pagination
    total_results = len(sorted_results)
    total_pages = (total_results + results_per_page - 1) // results_per_page
    
    if total_pages > 1:
        page = st.selectbox(f"Page (1-{total_pages})", range(1, total_pages + 1), index=0)
        start_idx = (page - 1) * results_per_page
        end_idx = min(start_idx + results_per_page, total_results)
        page_results = sorted_results[start_idx:end_idx]
    else:
        page_results = sorted_results
    
    # Display results
    for i, college in enumerate(page_results):
        with st.container():
            create_college_card(college)
            st.markdown("---")

def apply_filters(results: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Apply additional filters to results"""
    
    # Additional filter options
    st.markdown("### Additional Filters")
    
    col1, col2 = st.columns(2)
    
    with col1:
        degree_filter = st.multiselect(
            "Degree Level",
            ["Bachelor", "Master", "Certificate"],
            default=["Bachelor", "Master", "Certificate"]
        )
    
    with col2:
        tuition_filter = st.slider(
            "Max Tuition (per year)",
            min_value=0,
            max_value=100000,
            value=100000,
            step=5000
        )
    
    # Apply filters
    filtered = results.copy()
    
    if degree_filter:
        filtered = [r for r in filtered if r.get('degree_level') in degree_filter]
    
    filtered = [r for r in filtered if r.get('tuition_max', 0) <= tuition_filter]
    
    return filtered

def sort_results(results: List[Dict[str, Any]], sort_by: str) -> List[Dict[str, Any]]:
    """Sort results based on criteria"""
    
    if sort_by == "Name (A-Z)":
        return sorted(results, key=lambda x: x.get('name', ''))
    elif sort_by == "Name (Z-A)":
        return sorted(results, key=lambda x: x.get('name', ''), reverse=True)
    elif sort_by == "Tuition (Low to High)":
        return sorted(results, key=lambda x: x.get('tuition_min', 0))
    elif sort_by == "Tuition (High to Low)":
        return sorted(results, key=lambda x: x.get('tuition_min', 0), reverse=True)
    
    return results

def generate_mock_results(filters: Dict[str, Any]) -> List[Dict[str, Any]]:
    """Generate mock results for demonstration (replace with API call later)"""
    
    mock_colleges = [
        {
            'id': 1,
            'name': 'Parsons School of Design',
            'location_city': 'New York',
            'location_country': 'USA',
            'program_name': 'BFA Graphic Design',
            'program_type': 'Graphic Design',
            'degree_level': 'Bachelor',
            'tuition_min': 45000,
            'tuition_max': 50000,
            'application_deadline': '2024-01-15',
            'program_description': 'Comprehensive graphic design program with focus on digital and print media.',
            'contact_email': 'admissions@parsons.edu',
            'website_url': 'https://www.newschool.edu/parsons/'
        },
        {
            'id': 2,
            'name': 'Royal College of Art',
            'location_city': 'London',
            'location_country': 'UK',
            'program_name': 'MA Product Design',
            'program_type': 'Product Design',
            'degree_level': 'Master',
            'tuition_min': 35000,
            'tuition_max': 40000,
            'application_deadline': '2024-02-01',
            'program_description': 'Advanced product design program with industry collaboration.',
            'contact_email': 'admissions@rca.ac.uk',
            'website_url': 'https://www.rca.ac.uk/'
        },
        {
            'id': 3,
            'name': 'ArtCenter College of Design',
            'location_city': 'Pasadena',
            'location_country': 'USA',
            'program_name': 'BFA UX/UI Design',
            'program_type': 'UX/UI',
            'degree_level': 'Bachelor',
            'tuition_min': 40000,
            'tuition_max': 45000,
            'application_deadline': '2024-01-20',
            'program_description': 'User experience and interface design program with technology focus.',
            'contact_email': 'admissions@artcenter.edu',
            'website_url': 'https://www.artcenter.edu/'
        }
    ]
    
    # Filter mock results based on user preferences
    filtered = []
    for college in mock_colleges:
        if filters.get('program_type') and college['program_type'] != filters['program_type']:
            continue
        if filters.get('location') and filters['location'] != 'Any':
            # Simple location matching (can be improved)
            if filters['location'] == 'North America' and college['location_country'] not in ['USA', 'Canada']:
                continue
            elif filters['location'] == 'Europe' and college['location_country'] not in ['UK', 'Germany', 'France']:
                continue
        
        filtered.append(college)
    
    return filtered 