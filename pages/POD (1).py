import streamlit as st
import os

# Set page configuration
st.set_page_config(page_title="POD – Auto Rename ZIP", layout="wide")

# Custom CSS styles for consistent design
st.markdown("""
    <style>
        /* Sidebar Styling */
        [data-testid="stSidebar"] {
            background: linear-gradient(to bottom, #F97316, #FB923C); /* Gradient background */
            color: white;
        }
        [data-testid="stSidebar"] .css-1d391kg {
            color: white; /* Text color for dropdown */
        }

        /* General Page Styling */
        body {
            font-family: 'Arial', sans-serif;
            background-color: #FFFFFF; /* White background */
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
            text-align: center; /* Keep text centered within the card */
            background: linear-gradient(to bottom, #F97316, #FB923C); /* Gradient background */
            box-shadow: 2px 2px 8px rgba(0,0,0,0.05);
            margin: 2rem auto;
            width: 50%; /* Center the card and limit its width */
        }
        .download-card:hover {
            box-shadow: 4px 4px 12px rgba(0,0,0,0.15);
            transform: scale(1.02);
        }
        .download-card h3 {
            color: #FFFFFF; /* White text for titles */
            font-size: 1.5rem;
            margin-bottom: 1rem;
        }
        .download-card p {
            color: #FFFFFF; /* White text for descriptions */
            font-size: 1rem;
            margin-bottom: 1.5rem;
        }

        /* Download Button Styling */
        .download-button-wrapper { /* Wrapper to center the button */
            display: flex;
            justify-content: center; /* Center the button horizontally */
            margin-top: 1rem; /* Add some space between the card and the button */
        }

        .stDownloadButton {
            /* Remove default Streamlit button styling to customize */
            padding: 0 !important;
        }

        .stDownloadButton > div:first-child { /* The actual button element */
            background-color: white;
            color: #CF3331 !important;
            padding: 0.75rem 1.5rem;
            border-radius: 8px;
            font-size: 1rem;
            font-weight: bold;
            text-align: center; /* Ensure text inside the button is centered */
            box-shadow: 2px 2px 8px rgba(0, 0, 0, 0.1);
            border: none !important; /* Remove any default borders */
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

# Add a styled download card with a button
file_path = os.path.join(os.path.dirname(__file__), "rename_file_pod (1) (6).bat")
try:
    with open(file_path, "rb") as file:
        st.markdown("""
            <div class="download-card">
                <h3>Download Auto Rename ZIP Tool</h3>
                <p>Click the button below to download the tool.</p>
            </div>
        """, unsafe_allow_html=True)
        st.markdown('<div class="download-button-wrapper">', unsafe_allow_html=True)
        st.download_button(
            label="Download",
            data=file,
            file_name="Auto_Rename_ZIP_Tool.bat",
            mime="application/octet-stream"
        )
        st.markdown('</div>', unsafe_allow_html=True)
except FileNotFoundError:
    st.error("The file 'rename_file_pod (1).bat' was not found. Please ensure it exists in the 'pages' folder.")
