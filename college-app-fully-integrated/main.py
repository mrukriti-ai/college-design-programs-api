"""
Root-level main file for Streamlit Cloud deployment
This file imports and runs the actual Streamlit app from the streamlit_app directory
"""

import sys
import os

# Add the project root directory to the Python path
project_root = os.path.dirname(os.path.abspath(__file__))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# Import and run the main app
from streamlit_app.main import main

if __name__ == "__main__":
    main()
