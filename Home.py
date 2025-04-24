import streamlit as st

# Set page configuration
st.set_page_config(page_title="JHT/SJL Data Portal", layout="wide")

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

        /* Project Card Styling */
        .project-card {
            border: 1px solid #e0e0e0;
            border-radius: 12px;
            padding: 1.5rem;
            text-align: center;
            transition: all 0.2s ease-in-out;
            background: linear-gradient(to bottom, #F97316, #FB923C); /* Gradient background */
            box-shadow: 2px 2px 8px rgba(0,0,0,0.05);
        }
        .project-card:hover {
            box-shadow: 4px 4px 12px rgba(0,0,0,0.15);
            transform: scale(1.02);
        }
        .project-card h3 {
            color: #FFFFFF; /* White text for titles */
            font-size: 1.5rem;
            margin-bottom: 0.5rem;
        }
        .project-card p {
            color: #FFFFFF; /* White text for descriptions */
            font-size: 1rem;
            margin-bottom: 1rem;
        }
        .project-card a {
            display: inline-block;
            margin-top: 0.75rem;
            background-color: #CF3331; /* Red button */
            color: white;
            padding: 0.5rem 1.2rem;
            border-radius: 8px;
            text-decoration: none;
            font-weight: 600;
            transition: background-color 0.2s ease-in-out;
        }
        .project-card a:hover {
            background-color: #A82828; /* Darker red on hover */
        }

        /* Metabase Section Styling */
        .metabase-section {
            text-align: center;
            margin-top: 2rem;
        }
        .metabase-section h3 {
            color: #F97316;
            font-size: 1.8rem;
            margin-bottom: 1rem;
        }
        .metabase-section p {
            color: #555555;
            font-size: 1rem;
            margin-bottom: 1rem;
        }
        .metabase-section a img {
            transition: transform 0.2s ease-in-out;
        }
        .metabase-section a img:hover {
            transform: scale(1.1);
        }
    </style>
""", unsafe_allow_html=True)

# Title Section
st.markdown("""
    <div class="title-container">
        <h1>📊 JHT/SJL Data Portal</h1>
        <p>Analyze, automate, and monitor logistics data in one neat place.</p>
    </div>
""", unsafe_allow_html=True)

# Project Dashboard Grid with more space between columns
col1, spacer, col2 = st.columns([1, 0.5, 1])  # Increase the spacer column width to 0.5 for more space

with col1:
    st.markdown("""
        <div class="project-card">
            <h3>📦 Vendor Tiering</h3>
            <p>View rankings of vendors based on specific criteria.</p>
            <a href="/Vendor_Tiering">Open</a>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)  # Add vertical spacing between cards

    st.markdown("""
        <div class="project-card">
            <h3>💬 Data Blasting Krani</h3>
            <p>Convert raw data into chat-ready messages.</p>
            <a href="/Data_Blasting_Krani">Open</a>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)  # Add vertical spacing between cards

    st.markdown("""
        <div class="project-card">
            <h3>📍 Report Posisi Armada</h3>
            <p>Track the current positions of all operational vehicles.</p>
            <a href="/Report_Posisi_Armada">Open</a>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="project-card">
            <h3>🗂 POD – Auto Rename ZIP</h3>
            <p>Upload ZIP files for automated renaming based on delivery orders.</p>
            <a href="/POD_Auto_Rename_ZIP">Open</a>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)  # Add vertical spacing between cards

    st.markdown("""
        <div class="project-card">
            <h3>🛠 Maintenance Schedule</h3>
            <p>Manage and review maintenance schedules for fleet vehicles.</p>
            <a href="/Maintenance_Schedule">Open</a>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)  # Add vertical spacing between cards

    st.markdown("""
        <div class="project-card">
            <h3>🗓 KIR Schedule</h3>
            <p>Monitor inspection schedules and KIR documentation.</p>
            <a href="/KIR_Schedule">Open</a>
        </div>
    """, unsafe_allow_html=True)

# Order Analysis Section
st.markdown("---")
st.markdown("""
    <div class="metabase-section">
        <h3>🧠 Order Analysis via Metabase</h3>
        <p>To analyze order data from JHT or SJL using Metabase, click the icon below:</p>
        <a href="https://metabase.example.com" target="_blank">
            <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/8d/Metabase_logo.png/320px-Metabase_logo.png" width="180"/>
        </a>
    </div>
""", unsafe_allow_html=True)