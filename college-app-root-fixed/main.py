"""
Root-level main file for Streamlit Cloud deployment
This file imports and runs the actual Streamlit app from the streamlit_app directory
"""

import sys
import os

# Add the streamlit_app directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'streamlit_app'))

# Import and run the main app
from streamlit_app.main import main

if __name__ == "__main__":
    main()
