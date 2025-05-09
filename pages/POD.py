import streamlit as st
import os

# Set page configuration
st.set_page_config(page_title="POD – Auto Rename ZIP", layout="wide")

# Custom CSS styles for consistent design
st.markdown("""
    <style>
        /* ... (keep existing styles the same) ... */

        /* Download Button Styling */
        .stDownloadButton > div:first-child { /* The actual button element */
            background-color: white !important;
            color: #CF3331 !important;
            padding: 0.75rem 1.5rem !important;
            border-radius: 8px !important;
            font-size: 1rem !important;
            font-weight: bold !important;
            text-align: center !important;
            box-shadow: 2px 2px 8px rgba(0, 0, 0, 0.1) !important;
            border: none !important;
        }

        .stDownloadButton:hover > div:first-child {
            background-color: #CF3331 !important;
            color: white !important;
        }
    </style>
""", unsafe_allow_html=True)

# Title Section (unchanged)
st.markdown("""
    <div class="title-container">
        <h1>🗂 POD – Auto Rename ZIP</h1>
        <p>Download the Auto Rename ZIP tool to automate renaming based on delivery orders.</p>
    </div>
""", unsafe_allow_html=True)

# Add styled download card and button
file_path = os.path.join(os.path.dirname(__file__), "rename_file_pod (1).bat")
try:
    with open(file_path, "rb") as file:
        # Render the orange card
        st.markdown("""
            <div class="download-card">
                <h3>Download Auto Rename ZIP Tool</h3>
                <p>Click the button below to download the tool.</p>
            </div>
        """, unsafe_allow_html=True)
        
        # Center the button using Streamlit columns
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.download_button(
                label="Download",
                data=file,
                file_name="Auto_Rename_ZIP_Tool.bat",
                mime="application/octet-stream"
            )
except FileNotFoundError:
    st.error("File not found. Ensure 'rename_file_pod (1).bat' exists in the 'pages' folder.")
