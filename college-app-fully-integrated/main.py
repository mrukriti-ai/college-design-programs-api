"""
Root-level main file for Streamlit Cloud deployment
This file imports and runs the actual Streamlit app from the streamlit_app directory
"""

import sys
from pathlib import Path

# Add the project root and streamlit_app directories to the Python path
project_root = Path(__file__).resolve().parent
streamlit_dir = project_root / "streamlit_app"

# Add paths to sys.path
for path in (streamlit_dir, project_root):
    if path.is_dir() and str(path) not in sys.path:
        sys.path.insert(0, str(path))

# Import and run the main app
from streamlit_app.main import main

if __name__ == "__main__":
    main()
