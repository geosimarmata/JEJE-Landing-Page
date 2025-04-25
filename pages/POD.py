import streamlit as st
import os  # Import the os module

# Set page configuration
st.set_page_config(page_title="POD – Auto Rename ZIP", layout="wide")

# Custom CSS styles
st.markdown("""
    <style>
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

        /* Download Section Styling */
        .download-section {
            text-align: center;
            margin-top: 2rem;
        }
        .download-section h3 {
            color: #F97316;
            font-size: 1.8rem;
            margin-bottom: 1rem;
        }
        .download-section p {
            color: #555555;
            font-size: 1rem;
            margin-bottom: 1rem;
        }
        .download-section .stDownloadButton {
            display: inline-block;
            background: linear-gradient(to bottom, #CF3331, #A82828); /* Red gradient background */
            color: white;
            padding: 0.5rem 1.5rem;
            border: none;
            border-radius: 8px;
            font-size: 1rem;
            font-weight: bold;
            text-align: center;
            cursor: pointer;
        }
        .download-section .stDownloadButton:hover {
            background: linear-gradient(to bottom, #A82828, #CF3331); /* Reverse gradient on hover */
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

# Add a centered download button
# Use a relative path to locate the file
file_path = os.path.join(os.path.dirname(__file__), "rename_file_pod.bat")
try:
    with open(file_path, "rb") as file:
        st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
        st.download_button(
            label="Download Auto Rename ZIP Tool",
            data=file,
            file_name="rename_file_pod.bat",
            mime="application/octet-stream"
        )
        st.markdown("</div>", unsafe_allow_html=True)
except FileNotFoundError:
    st.error("The file 'rename_file_pod.bat' was not found. Please ensure it exists in the same directory as this script.")
