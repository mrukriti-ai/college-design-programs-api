#!/usr/bin/env python3
"""
Test script to verify user profile API is working
"""

import requests
import json
import os

# Get API base URL from environment or use default
API_BASE_URL = os.getenv('API_BASE_URL', 'https://college-design-programs-api.onrender.com')

def test_user_profile_api():
    """Test the user profile API endpoints"""
    
    print("=" * 70)
    print("🧪 Testing User Profile API")
    print("=" * 70)
    print(f"\n📍 API Base URL: {API_BASE_URL}\n")
    
    # Test data
    test_profile = {
        "name": "Test User",
        "email": f"test_{os.urandom(4).hex()}@example.com",  # Unique email
        "education_level": "Undergraduate",
        "program_interest": "Graphic Design",
        "budget_range": "20k-40k",
        "location_preference": "North America",
        "degree_level": ["Bachelor", "Master"],
        "include_international": True
    }
    
    # Test 1: Create user profile
    print("Test 1: Creating user profile...")
    print(f"   Data: {json.dumps(test_profile, indent=2)}")
    
    try:
        url = f"{API_BASE_URL}/api/user-profiles/"
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        
        response = requests.post(url, json=test_profile, headers=headers, timeout=10)
        
        print(f"   Status Code: {response.status_code}")
        print(f"   Response: {response.text[:200]}")
        
        if response.status_code in [200, 201]:
            print("   ✅ Profile created successfully!")
            created_profile = response.json()
            test_email = created_profile.get('email')
            
            # Test 2: Get user profile
            print(f"\nTest 2: Retrieving user profile by email ({test_email})...")
            get_url = f"{API_BASE_URL}/api/user-profiles/{test_email}"
            get_response = requests.get(get_url, headers=headers, timeout=10)
            
            print(f"   Status Code: {get_response.status_code}")
            if get_response.status_code == 200:
                print("   ✅ Profile retrieved successfully!")
                print(f"   Profile: {json.dumps(get_response.json(), indent=2, default=str)}")
            else:
                print(f"   ❌ Failed to retrieve profile: {get_response.text}")
            
            # Test 3: List all profiles
            print(f"\nTest 3: Listing all user profiles...")
            list_url = f"{API_BASE_URL}/api/user-profiles/"
            list_response = requests.get(list_url, headers=headers, timeout=10)
            
            print(f"   Status Code: {list_response.status_code}")
            if list_response.status_code == 200:
                profiles = list_response.json()
                print(f"   ✅ Found {len(profiles)} profiles")
                if profiles:
                    print(f"   Sample profile: {json.dumps(profiles[0], indent=2, default=str)}")
            else:
                print(f"   ❌ Failed to list profiles: {list_response.text}")
                
        else:
            print(f"   ❌ Failed to create profile")
            print(f"   Error: {response.text}")
            
    except requests.exceptions.ConnectionError:
        print(f"   ❌ Connection Error: Cannot connect to {API_BASE_URL}")
        print("   💡 Make sure:")
        print("      - Backend is running")
        print("      - API URL is correct")
        print("      - Network connection is working")
    except requests.exceptions.Timeout:
        print(f"   ❌ Timeout: API request took too long")
    except Exception as e:
        print(f"   ❌ Unexpected error: {e}")
        import traceback
        traceback.print_exc()
    
    print("\n" + "=" * 70)
    print("✅ Testing complete!")
    print("=" * 70)

if __name__ == "__main__":
    test_user_profile_api()

