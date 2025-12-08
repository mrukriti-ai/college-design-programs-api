"""
Root-level main file for Streamlit Cloud deployment
This file imports and runs the actual Streamlit app from the streamlit_app directory
"""

import sys
from pathlib import Path

# Add the project root and streamlit_app directories to the Python path
project_root = Path(__file__).resolve().parent
streamlit_dir = project_root / "streamlit_app"

for path in (streamlit_dir, project_root):
    if path.is_dir():
        sys.path.insert(0, str(path))

# Import and run the main app (with fallback if package import fails)
try:
    from streamlit_app.main import main
except ModuleNotFoundError:
    import main as streamlit_main  # when run inside streamlit_app folder
    main = streamlit_main.main

if __name__ == "__main__":
    main()
