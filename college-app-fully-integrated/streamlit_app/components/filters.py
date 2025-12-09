"""
Filter components for search and results filtering.
Provides consistent filtering functionality across the application.
"""

import streamlit as st
from typing import List, Dict, Any
from streamlit_app.utils.config import PROGRAM_TYPES, BUDGET_RANGES, LOCATIONS

def create_results_filter():
    """Create a results filter component"""
    
    st.markdown("### 🔍 Filter Results")
    
    col1, col2 = st.columns(2)
    
    with col1:
        program_filter = st.multiselect(
            "Program Types",
            PROGRAM_TYPES,
            default=PROGRAM_TYPES,
            help="Select program types to include"
        )
        
        budget_filter = st.multiselect(
            "Budget Ranges",
            BUDGET_RANGES,
            default=BUDGET_RANGES,
            help="Select budget ranges to include"
        )
    
    with col2:
        location_filter = st.multiselect(
            "Locations",
            LOCATIONS,
            default=LOCATIONS,
            help="Select locations to include"
        )
        
        degree_filter = st.multiselect(
            "Degree Levels",
            ["Bachelor", "Master", "Certificate"],
            default=["Bachelor", "Master", "Certificate"],
            help="Select degree levels to include"
        )
    
    # Additional filters
    max_tuition = st.slider(
        "Maximum Tuition (per year)",
        min_value=0,
        max_value=100000,
        value=100000,
        step=5000,
        help="Filter by maximum annual tuition"
    )
    
    return {
        'program_filter': program_filter,
        'budget_filter': budget_filter,
        'location_filter': location_filter,
        'degree_filter': degree_filter,
        'max_tuition': max_tuition
    }

def apply_filters_to_results(results: List[Dict[str, Any]], filters: Dict[str, Any]) -> List[Dict[str, Any]]:
    """Apply filters to search results"""
    
    filtered_results = results.copy()
    
    # Program type filter
    if filters.get('program_filter') and filters['program_filter'] != PROGRAM_TYPES:
        filtered_results = [
            r for r in filtered_results 
            if r.get('program_type') in filters['program_filter']
        ]
    
    # Budget filter
    if filters.get('budget_filter') and filters['budget_filter'] != BUDGET_RANGES:
        filtered_results = [
            r for r in filtered_results 
            if any(budget_range_matches(r, budget) for budget in filters['budget_filter'])
        ]
    
    # Location filter
    if filters.get('location_filter') and filters['location_filter'] != LOCATIONS:
        filtered_results = [
            r for r in filtered_results 
            if any(location_matches(r, location) for location in filters['location_filter'])
        ]
    
    # Degree level filter
    if filters.get('degree_filter'):
        filtered_results = [
            r for r in filtered_results 
            if r.get('degree_level') in filters['degree_filter']
        ]
    
    # Tuition filter
    if filters.get('max_tuition'):
        filtered_results = [
            r for r in filtered_results 
            if r.get('tuition_max', 0) <= filters['max_tuition']
        ]
    
    return filtered_results

def budget_range_matches(college: Dict[str, Any], budget_range: str) -> bool:
    """Check if college matches budget range"""
    
    tuition_min = college.get('tuition_min', 0)
    tuition_max = college.get('tuition_max', 0)
    
    if budget_range == "Under 20k":
        return tuition_min <= 20000
    elif budget_range == "20k-40k":
        return tuition_min <= 40000 and (tuition_max == 0 or tuition_max >= 20000)
    elif budget_range == "40k-60k":
        return tuition_min <= 60000 and (tuition_max == 0 or tuition_max >= 40000)
    elif budget_range == "Over 60k":
        return tuition_max == 0 or tuition_max >= 60000
    
    return True

def location_matches(college: Dict[str, Any], location: str) -> bool:
    """Check if college matches location"""
    
    country = college.get('location_country', '')
    
    if location == "North America":
        return country in ["USA", "United States", "Canada", "Mexico"]
    elif location == "Europe":
        return country in ["UK", "United Kingdom", "Germany", "France", "Italy", "Spain", "Netherlands", "Sweden", "Denmark", "Finland", "Norway", "Belgium", "Portugal", "Switzerland", "Austria", "Poland", "Ireland"]
    elif location == "Asia":
        return country in ["India", "China", "Japan", "South Korea", "Singapore", "Hong Kong", "Taiwan", "Thailand", "Malaysia", "Indonesia", "Philippines", "Vietnam"]
    elif location == "Australia":
        return country in ["Australia", "New Zealand"]
    elif location == "Any":
        return True
    
    return True

def create_sort_options():
    """Create sorting options for results"""
    
    sort_by = st.selectbox(
        "Sort by",
        [
            "Name (A-Z)",
            "Name (Z-A)", 
            "Tuition (Low to High)",
            "Tuition (High to Low)",
            "Location (A-Z)",
            "Program Type (A-Z)"
        ],
        index=0
    )
    
    return sort_by

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
    elif sort_by == "Location (A-Z)":
        return sorted(results, key=lambda x: f"{x.get('location_city', '')}, {x.get('location_country', '')}")
    elif sort_by == "Program Type (A-Z)":
        return sorted(results, key=lambda x: x.get('program_type', ''))
    
    return results 