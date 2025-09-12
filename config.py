"""
Configuration management for the Streamlit app.
Handles API settings, constants, and environment variables.
"""

import os
from typing import Dict, Any

# App constants
PROGRAM_TYPES = [
    "Graphic Design",
    "UX/UI", 
    "Fashion",
    "Product Design",
    "Architecture",
    "Animation"
]

BUDGET_RANGES = [
    "Under 20k",
    "20k-40k",
    "40k-60k",
    "Over 60k"
]

LOCATIONS = [
    "North America",
    "Europe", 
    "Asia",
    "Australia",
    "Any"
]

EDUCATION_LEVELS = [
    "High School",
    "Undergraduate",
    "Graduate"
]

def load_config() -> Dict[str, Any]:
    """Load application configuration"""
    
    config = {
        # API Configuration
        'api_base_url': os.getenv('API_BASE_URL', 'https://college-design-programs-api.onrender.com'),
        'api_timeout': int(os.getenv('API_TIMEOUT', '30')),
        
        # App Settings
        'max_results_per_page': int(os.getenv('MAX_RESULTS_PER_PAGE', '20')),
        'enable_debug': os.getenv('ENABLE_DEBUG', 'false').lower() == 'true',
        
        # Constants
        'program_types': PROGRAM_TYPES,
        'budget_ranges': BUDGET_RANGES,
        'locations': LOCATIONS,
        'education_levels': EDUCATION_LEVELS,
        
        # UI Settings
        'page_title': "College Design Programs",
        'page_icon': "🎨",
        'layout': "wide"
    }
    
    return config

def get_api_url(endpoint: str) -> str:
    """Get full API URL for an endpoint"""
    base_url = os.getenv('API_BASE_URL', 'https://college-design-programs-api.onrender.com')
    return f"{base_url.rstrip('/')}/{endpoint.lstrip('/')}"

def get_api_headers() -> Dict[str, str]:
    """Get default API headers"""
    return {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

def get_admin_headers() -> Dict[str, str]:
    """Get admin API headers with token"""
    headers = get_api_headers()
    admin_token = os.getenv('ADMIN_TOKEN', 'dev')
    headers['X-Admin-Token'] = admin_token
    return headers 