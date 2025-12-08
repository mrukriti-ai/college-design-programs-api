"""
Root-level main file for Streamlit Cloud deployment
This file imports and runs the actual Streamlit app from the streamlit_app directory
"""

import sys
import os

# Add the project root and streamlit_app directories to the Python path
project_root = os.path.dirname(os.path.abspath(__file__))
streamlit_dir = os.path.join(project_root, "streamlit_app")

for path in (project_root, streamlit_dir):
    if os.path.isdir(path) and path not in sys.path:
        sys.path.insert(0, path)

# Import and run the main app
from streamlit_app.main import main

if __name__ == "__main__":
    main()
