import streamlit as st
import os

# Set page configuration
st.set_page_config(page_title="POD – Auto Rename ZIP", layout="wide")

# Custom CSS styles
st.markdown("""
    <style>
        /* Sidebar Styling */
        [data-testid="stSidebar"] {
            background: linear-gradient(to bottom, #F97316, #FB923C);
            color: white;
        }

        /* Title Section Styling */
        .title-container {
            text-align: center;
            margin-bottom: 2rem;
        }
        .title-container h1 {
            color: #F27F30;
            font-size: 2.5rem;
            margin-bottom: 0.5rem;
        }
        .title-container p {
            color: #555555;
            font-size: 1.2rem;
        }

        /* Download Card Styling */
        .download-card {
            border: 1px solid #e0e0e0;
            border-radius: 12px;
            padding: 2rem;
            text-align: center;
            background: linear-gradient(to bottom, #F97316, #FB923C);
            box-shadow: 2px 2px 8px rgba(0,0,0,0.05);
            margin: 2rem auto;
            width: 50%;
        }

        .download-card h3 {
            color: #FFFFFF;
            font-size: 1.5rem;
            margin-bottom: 1rem;
        }

        .download-card p {
            color: #FFFFFF;
            font-size: 1rem;
            margin-bottom: 1.5rem;
        }

        .stDownloadButton > div:first-child {
            background-color: white;
            color: #CF3331 !important;
            padding: 0.75rem 1.5rem;
            border-radius: 8px;
            font-size: 1rem;
            font-weight: bold;
            box-shadow: 2px 2px 8px rgba(0, 0, 0, 0.1);
            border: none !important;
        }

        .stDownloadButton:hover > div:first-child {
            background-color: #CF3331;
            color: white !important;
            box-shadow: 4px 4px 12px rgba(0, 0, 0, 0.2);
        }

        .stDownloadButton:active > div:first-child {
            background-color: #A82828;
            color: white !important;
        }
    </style>
""", unsafe_allow_html=True)

# Title Section
st.markdown("""
    <div class="title-container">
        <h1>🗂 POD – Auto Rename ZIP</h1>
        <p>Download the Auto Rename ZIP tool to automate renaming based on delivery orders.</p>
    </div>
""", unsafe_allow_html=True)

# File path for download
file_path = os.path.join(os.path.dirname(__file__), "rename_file_pod (1).bat")

# Try to load and show download card with embedded button
try:
    with open(file_path, "rb") as file:
        st.markdown('<div class="download-card">', unsafe_allow_html=True)
        st.markdown("<h3>Download Auto Rename ZIP Tool</h3>", unsafe_allow_html=True)
        st.markdown("<p>Click the button below to download the tool.</p>", unsafe_allow_html=True)
        st.download_button(
            label="Download",
            data=file,
            file_name="Auto_Rename_ZIP_Tool.bat",
            mime="application/octet-stream"
        )
        st.markdown('</div>', unsafe_allow_html=True)
except FileNotFoundError:
    st.error("The file 'rename_file_pod (1).bat' was not found. Please ensure it exists in the correct folder.")
