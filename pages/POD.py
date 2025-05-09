import streamlit as st
import os

# Page settings
st.set_page_config(page_title="POD – Auto Rename ZIP", layout="centered")

# Custom CSS
st.markdown("""
    <style>
        .download-card {
            border-radius: 12px;
            padding: 2rem;
            background: linear-gradient(to bottom, #F97316, #FB923C);
            box-shadow: 2px 2px 8px rgba(0,0,0,0.1);
            margin: 2rem auto;
            text-align: center;
            width: 100%;
            max-width: 500px;
        }

        .download-card h3 {
            color: #fff;
            font-size: 1.5rem;
            margin-bottom: 0.5rem;
        }

        .download-card p {
            color: #fff;
            font-size: 1rem;
            margin-bottom: 1.2rem;
        }

        .download-card .stDownloadButton > div:first-child {
            background-color: white;
            color: #F97316 !important;
            font-weight: 600;
            border-radius: 8px;
            padding: 0.6rem 1.2rem;
            font-size: 1rem;
            box-shadow: 1px 1px 6px rgba(0,0,0,0.1);
        }

        .download-card .stDownloadButton:hover > div:first-child {
            background-color: #F97316;
            color: white !important;
        }
    </style>
""", unsafe_allow_html=True)

# Title section
st.markdown("""
<div style="text-align:center;">
    <h1 style="color:#F97316;">📁 POD – Auto Rename ZIP</h1>
    <p style="font-size:1.1rem; color:#444;">Download the Auto Rename ZIP tool to automate renaming based on delivery orders.</p>
</div>
""", unsafe_allow_html=True)

# File path
file_path = os.path.join(os.path.dirname(__file__), "rename_file_pod (1).bat")

# Download card with embedded button
try:
    with open(file_path, "rb") as file:
        with st.container():
            st.markdown('<div class="download-card">', unsafe_allow_html=True)
            st.markdown('<h3>Download Auto Rename ZIP Tool</h3>', unsafe_allow_html=True)
            st.markdown('<p>Click the button below to download the tool.</p>', unsafe_allow_html=True)
            st.download_button(
                label="Download Tool",
                data=file,
                file_name="Auto_Rename_ZIP_Tool.bat",
                mime="application/octet-stream"
            )
            st.markdown('</div>', unsafe_allow_html=True)
except FileNotFoundError:
    st.error("The download file was not found. Please check the path.")
