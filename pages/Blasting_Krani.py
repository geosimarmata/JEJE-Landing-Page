import streamlit as st
import pandas as pd
import re
from datetime import datetime, timedelta

# Page config
st.set_page_config(page_title="Data Blasting Krani", layout="wide")

# Custom styles
st.markdown("""
    <style>
    [data-testid="stSidebar"] {
        background: linear-gradient(to bottom, #F97316, #FB923C);
        color: black;
    }
    .blasting-title h1 {
        color: #F27F30;
        font-size: 2.2rem;
    }
    .blast-box {
        background: #FFF3E0;
        border-left: 6px solid #FB923C;
        padding: 1rem;
        border-radius: 8px;
        white-space: pre-wrap;
        font-family: 'Courier New', monospace;
        font-size: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("""
    <div class="blasting-title">
        <h1>💬 Data Blasting Krani</h1>
    </div>
""", unsafe_allow_html=True)

# Upload CSV
uploaded_file = st.file_uploader("Upload your trip data CSV", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # Convert datetime fields
    df['tanggal_muat'] = pd.to_datetime(df['tanggal_muat'], errors='coerce')
    df['trip_waktu_muat'] = pd.to_datetime(df['trip_waktu_muat'], format="%I:%M %p", errors='coerce').dt.time

    # Combine datetime for sorting
    df['sort_datetime'] = df.apply(
        lambda row: datetime.combine(row['tanggal_muat'].date(), row['trip_waktu_muat'])
        if pd.notnull(row['tanggal_muat']) and pd.notnull(row['trip_waktu_muat'])
        else pd.NaT,
        axis=1
    )

    # Sidebar Filters
    st.sidebar.header("Filter Data")

    selected_date_range = st.sidebar.date_input(
        "Select Date Range",
        value=(datetime.now().date() - timedelta(days=7), datetime.now().date()),
        help="Pilih rentang tanggal"
    )

    if isinstance(selected_date_range, tuple) and len(selected_date_range) == 2:
        start_date, end_date = selected_date_range
    else:
        start_date = end_date = selected_date_range

    # Origin city options with "All"
    origin_options = ["All"] + sorted(df['origin_city_name'].dropna().unique())
    selected_origin = st.sidebar.selectbox("Select Origin City", origin_options)

    # Shipper name options with "All"
    shipper_options = ["All"] + sorted(df['nama_shipper'].dropna().unique())
    selected_shipper = st.sidebar.selectbox("Select Shipper", shipper_options)

    # NEW: Select box to show all or only not supplied
    show_option = st.sidebar.selectbox(
        "Show Data",
        options=["All", "Not Supplied Yet"],
        index=0,
        help="Pilih untuk menampilkan semua data atau hanya data yang belum lengkap"
    )

    # Generate button in sidebar
    generate = st.sidebar.button("Generate 🚀")

    if generate:
        # Filter dataframe by date and origin
        filtered_df = df[
            (df['tanggal_muat'].dt.date >= start_date) &
            (df['tanggal_muat'].dt.date <= end_date) &
            ((selected_origin == "All") | (df['origin_city_name'] == selected_origin)) &
            ((selected_shipper == "All") | (df['nama_shipper'] == selected_shipper))
        ].copy()

        if filtered_df.empty:
            st.warning("No data found.")
        else:
            filtered_df.sort_values(by='sort_datetime', inplace=True)

            supplied_data_messages = []
            not_supply_messages = []

            for _, row in filtered_df.iterrows():
                tanggal = row['tanggal_muat'].strftime('%d %b %y') if pd.notnull(row['tanggal_muat']) else "Tanggal?"
                waktu = row['trip_waktu_muat'].strftime('%H:%M:%S') if pd.notnull(row['trip_waktu_muat']) else "Waktu?"
                truck_type = row.get('tipe_truk', '-')

                origin = row.get('origin_location_name', '-')
                dest = row.get('destination_location_name', '-')
                multi_drop = row.get('multi_drop', '')

                multi_drop_location = ''
                if pd.notna(multi_drop) and str(multi_drop).strip():
                    match = re.search(r'\[(.*?)\]', multi_drop)
                    if match:
                        multi_drop_location = match.group(1)

                route = f"{origin} - {dest}"
                if multi_drop_location:
                    route += f" - {multi_drop_location}"

                driver = row.get('nama_driver', '')
                nopol = row.get('nopol', '')
                phone = row.get('telp_driver', '')

                if all(pd.notna(x) and str(x).strip() for x in [driver, nopol, phone]):
                    message = f"""{tanggal} - {waktu}
{truck_type}
{route}
{driver}
{nopol}
Contact Driver
{phone}"""
                    supplied_data_messages.append(message.strip())
                else:
                    message = f"""{tanggal} - {waktu}
{truck_type}
{route}
*DATA MENYUSUL*"""
                    not_supply_messages.append(message.strip())

            # Decide which messages to show based on the select box
            if show_option == "All":
                final_messages = supplied_data_messages + not_supply_messages
            else:  # Only Not Supplied
                final_messages = not_supply_messages

            # Add LOADING PLAN title inside orange box
            title_html = "<b>*LOADING PLAN*</b><br><br>"
            result_output = title_html + "<br><br>".join(final_messages)
            st.markdown(f"<div class='blast-box'>{result_output}</div>", unsafe_allow_html=True)

else:
    st.info("Please upload a CSV file.")
