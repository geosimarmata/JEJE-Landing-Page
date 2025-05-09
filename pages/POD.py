import streamlit as st
import os

# Set page configuration
st.set_page_config(page_title="POD – Auto Rename ZIP", layout="wide")

# Custom CSS styles for consistent design
st.markdown("""
    <style>
        /* Sidebar Styling */
        [data-testid="stSidebar"] {
            background: linear-gradient(to bottom, #F97316, #FB923C);
            color: white;
        }
        [data-testid="stSidebar"] .css-1d391kg {
            color: white;
        }

        /* General Page Styling */
        body {
            font-family: 'Arial', sans-serif;
            background-color: #FFFFFF;
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
        .download-card:hover {
            box-shadow: 4px 4px 12px rgba(0,0,0,0.15);
            transform: scale(1.02);
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

        /* Natural Download Button Styling */
        .stDownloadButton > button {
            background-color: #FFFFFF !important;
            color: #F97316 !important;
            border: 2px solid #FFFFFF !important;
            border-radius: 8px !important;
            padding: 0.75rem 1.5rem !important;
            font-weight: bold !important;
            transition: all 0.3s ease !important;
        }
        
        .stDownloadButton > button:hover {
            background-color: transparent !important;
            color: #FFFFFF !important;
            border: 2px solid #FFFFFF !important;
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

# Add a styled download card with a button
file_path = os.path.join(os.path.dirname(__file__), "rename_file_pod (1).bat")
try:
    with open(file_path, "rb") as file:
        st.markdown("""
            <div class="download-card">
                <h3>Download Auto Rename ZIP Tool</h3>
                <p>Click the button below to download the tool.</p>
                <div style="margin-top: 1.5rem;">
        """, unsafe_allow_html=True)
        
        # This will create a more natural-looking download button
        st.download_button(
            label="Download",
            data=file,
            file_name="Auto_Rename_ZIP_Tool.bat",
            mime="application/octet-stream"
        )
        
        st.markdown("</div>", unsafe_allow_html=True)
except FileNotFoundError:
    st.error("The file 'rename_file_pod (1).bat' was not found. Please ensure it exists in the 'pages' folder.")
