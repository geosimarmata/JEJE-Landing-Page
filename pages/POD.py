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

        /* Button Container Styling */
        .button-container {
            display: flex;
            flex-direction: column;
            gap: 1rem;
            align-items: center;
            margin-top: 1.5rem;
        }

        /* Custom Button Styling */
        .stDownloadButton > button,
        .gdrive-button {
            background-color: #CF3331 !important;
            color: white !important;
            border: none !important;
            border-radius: 8px !important;
            padding: 0.5rem 1.2rem !important;
            font-weight: 600 !important;
            transition: background-color 0.2s ease-in-out !important;
            width: auto !important;
            margin: 0 auto !important;
            display: flex !important;
            align-items: center !important;
            justify-content: center !important;
            gap: 0.5rem !important;
            text-decoration: none !important;
            cursor: pointer !important;
        }
        
        .stDownloadButton > button:hover,
        .gdrive-button:hover {
            background-color: #A82828 !important;
        }
        
        .gdrive-icon {
            width: 20px;
            height: 20px;
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

# Add a styled download card with buttons
file_path = os.path.join(os.path.dirname(__file__), "rename_file_pod (1).bat")
try:
    with open(file_path, "rb") as file:
        st.markdown("""
            <div class="download-card">
                <h3>Download Auto Rename ZIP Tool</h3>
                <p>Click the button below to download the tool or view additional documentation.</p>
                <div class="button-container">
        """, unsafe_allow_html=True)
        
        # Download button
        st.download_button(
            label="Download Tool",
            data=file,
            file_name="Auto_Rename_ZIP_Tool.bat",
            mime="application/octet-stream"
        )
        
        # Google Drive button with logo
        st.markdown("""
            <a href="https://drive.google.com/drive/folders/YOUR_FOLDER_ID" 
               target="_blank" 
               class="gdrive-button">
                <img src="https://www.gstatic.com/images/branding/product/1x/drive_2020q4_48dp.png" 
                     alt="Google Drive" 
                     class="gdrive-icon">
                View Documentation
            </a>
        """, unsafe_allow_html=True)
        
        st.markdown("""
                </div>
            </div>
        """, unsafe_allow_html=True)
except FileNotFoundError:
    st.error("The file 'rename_file_pod (1).bat' was not found. Please ensure it exists in the 'pages' folder.")
