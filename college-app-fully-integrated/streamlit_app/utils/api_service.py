"""
API Service utilities for making HTTP requests to the backend
"""

import requests
from typing import Dict, Any, Optional
from streamlit_app.utils.config import get_api_url, get_api_headers


def save_user_profile(profile_data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    """
    Save user profile to the database via API
    
    Args:
        profile_data: Dictionary containing user profile information
        
    Returns:
        Response data if successful, None if error
    """
    import streamlit as st
    
    try:
        url = get_api_url("api/user-profiles/")
        headers = get_api_headers()
        
        # Debug: Show API URL being called (only in debug mode)
        if st.session_state.get('enable_debug', False):
            st.write(f"🔍 API URL: {url}")
            st.write(f"🔍 Profile Data: {profile_data}")
        
        response = requests.post(
            url,
            json=profile_data,
            headers=headers,
            timeout=10
        )
        
        if response.status_code in [200, 201]:
            return response.json()
        else:
            error_msg = f"API Error {response.status_code}: {response.text}"
            st.error(f"❌ {error_msg}")
            print(f"Error saving profile: {error_msg}")
            return None
            
    except requests.exceptions.ConnectionError as e:
        error_msg = f"Cannot connect to API at {get_api_url('api/user-profiles/')}. Is the backend running?"
        st.error(f"❌ Connection Error: {error_msg}")
        print(f"Connection error: {e}")
        return None
    except requests.exceptions.Timeout as e:
        error_msg = "API request timed out. Please try again."
        st.error(f"❌ Timeout: {error_msg}")
        print(f"Timeout error: {e}")
        return None
    except requests.exceptions.RequestException as e:
        error_msg = f"Request failed: {str(e)}"
        st.error(f"❌ {error_msg}")
        print(f"Request error: {e}")
        return None
    except Exception as e:
        error_msg = f"Unexpected error: {str(e)}"
        st.error(f"❌ {error_msg}")
        print(f"Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        return None


def get_user_profile(email: str) -> Optional[Dict[str, Any]]:
    """
    Get user profile by email from the database
    
    Args:
        email: User email address
        
    Returns:
        User profile data if found, None otherwise
    """
    try:
        url = get_api_url(f"api/user-profiles/{email}")
        headers = get_api_headers()
        
        response = requests.get(
            url,
            headers=headers,
            timeout=10
        )
        
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            return None
        else:
            print(f"Error getting profile: {response.status_code}")
            return None
            
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

