import streamlit as st
import pandas as pd
import io

# === Inject Custom CSS to Match Homepage ===
st.markdown("""
    <style>
        .main {
            background-color: #f0f2f6;
        }
        .stButton>button {
            color: white !important;
            background-color: #FF6F00 !important;
            border: none;
            border-radius: 6px;
            padding: 0.5em 1em;
        }
        h1, h2, h3 {
            color: #FF6F00;
        }
        .stDownloadButton>button {
            background-color: #FF6F00 !important;
            color: white !important;
        }
    </style>
""", unsafe_allow_html=True)

# === Page Config and Title ===
st.set_page_config(page_title="Vendor Analyst Generator", layout="wide")
st.title("📊 Vendor Analyst Generator")

# Initialize session state for the dataframe if it doesn't exist
if 'final_df' not in st.session_state:
    st.session_state.final_df = None

# Function to convert DataFrame to CSV bytes
@st.cache_data
def to_csv_bytes(df):
    output = io.BytesIO()
    df.to_csv(output, index=False, encoding='utf-8-sig')
    output.seek(0)
    return output

# === FILE UPLOADS ===
metabase_file = st.file_uploader("Upload Metabase CSV", type=["csv"])
spx_file = st.file_uploader("Upload SPX Excel File", type=["xlsx"])

# === PROCESSING AFTER FILE UPLOAD ===
if metabase_file and spx_file:
    if st.button("🚀 Generate Vendor Analyst"):
        try:
            # Read files
            metabase = pd.read_csv(metabase_file)
            raw_spx = pd.read_excel(spx_file, sheet_name='RAW SPX WEEKLY LEADTIME', header=1, usecols="A:BK")
            data_dedicated = pd.read_excel(spx_file, sheet_name='DATA Dedicated', header=3)
            raw_spx_manual = pd.read_excel(spx_file, sheet_name='RAW SPX WEEKLY LEADTIME', header=1, usecols=["LT Number", "Data Nopol", "VENDOR MANUAL / NOT FOUND"])
        except Exception as e:
            st.error(f"Error reading files: {e}")
            st.session_state.final_df = None
            st.stop()

        try:
            # Strip column names
            metabase.columns = metabase.columns.str.strip()
            raw_spx.columns = raw_spx.columns.str.strip()
            data_dedicated.columns = data_dedicated.columns.str.strip()
            raw_spx_manual.columns = raw_spx_manual.columns.str.strip()

            # Merge raw_spx and data_dedicated
            merged_df_lt = pd.merge(
                raw_spx,
                data_dedicated,
                left_on='Origin + Destination',
                right_on='uniq',
                how='left'
            )
            raw_spx['vendor_by_LTNumber'] = merged_df_lt['Vendor_y']

            # Clean license plates
            metabase['Cleaned Nopol'] = metabase['trip_transporter_vehicle_license_plate'].astype(str).str.replace(" ", "").str.lower()
            raw_spx['Cleaned Data Nopol'] = raw_spx['Data Nopol'].astype(str).str.replace(" ", "").str.lower()

            # Merge with metabase to get Vendor by Nopol
            result_df = raw_spx.merge(
                metabase[['Cleaned Nopol', 'trip_transporter_name']],
                left_on='Cleaned Data Nopol',
                right_on='Cleaned Nopol',
                how='left'
            )
            result_df = result_df.rename(columns={'trip_transporter_name': 'Vendor by Nopol'})

            # Fill missing and clean
            result_df['Vendor by Nopol'] = result_df['Vendor by Nopol'].fillna('').astype(str).str.strip()
            result_df['vendor_by_LTNumber'] = result_df['vendor_by_LTNumber'].fillna('').astype(str).str.strip()
            result_df = result_df.drop(columns=['Cleaned Data Nopol', 'Cleaned Nopol'])

            # Vendor Analyst Column
            result_df['Vendor_Analyst_Pre_Manual'] = result_df['vendor_by_LTNumber']
            result_df.loc[result_df['Vendor_Analyst_Pre_Manual'] == '', 'Vendor_Analyst_Pre_Manual'] = result_df['Vendor by Nopol']

            # Manual merge
            if 'LT Number' in result_df.columns and 'Data Nopol' in result_df.columns:
                result_df = pd.merge(result_df, raw_spx_manual, on=['LT Number', 'Data Nopol'], how='left')
            else:
                st.warning("Could not merge Vendor Manual data. Missing columns.")
                result_df['VENDOR MANUAL / NOT FOUND'] = ''

            result_df = result_df.rename(columns={'VENDOR MANUAL / NOT FOUND': 'Vendor Manual'})
            result_df['Vendor Manual'] = result_df['Vendor Manual'].fillna('').astype(str).str.strip()

            # Final Vendor Analyst logic
            result_df['Vendor Analyst'] = result_df['Vendor_Analyst_Pre_Manual']
            result_df.loc[result_df['Vendor Analyst'] == '', 'Vendor Analyst'] = result_df['Vendor Manual']

            check_condition = (
                (result_df['Vendor Manual'] != '') &
                (result_df['Vendor_Analyst_Pre_Manual'] != '') &
                (result_df['Vendor_Analyst_Pre_Manual'] != result_df['Vendor Manual'])
            )
            result_df.loc[check_condition, 'Vendor Analyst'] = "[CHECK] " + result_df['Vendor Analyst']
            result_df = result_df.drop(columns=['Vendor_Analyst_Pre_Manual'])

            # Reorder vendor columns to the end
            cols = list(result_df.columns)
            target_cols = ['vendor_by_LTNumber', 'Vendor by Nopol', 'Vendor Manual', 'Vendor Analyst']
            for col in target_cols:
                if col in cols:
                    cols.remove(col)
            result_df = result_df[cols + target_cols]

            # Store in session state
            st.session_state.final_df = result_df.drop_duplicates()
            st.success("✅ Vendor Analyst generated successfully!")

        except Exception as e:
            st.error(f"An error occurred during data processing: {e}")
            st.session_state.final_df = None

# === RESULT DISPLAY AND DOWNLOAD ===
if st.session_state.final_df is not None:
    st.subheader("📋 Vendor Analyst Preview")
    st.dataframe(st.session_state.final_df.head(100), use_container_width=True)

    if len(st.session_state.final_df) > 50000:
        st.warning("⚠️ Output is large. Download may take longer.")

    csv_bytes = to_csv_bytes(st.session_state.final_df)

    st.download_button(
        label="📥 Download Full Result CSV",
        data=csv_bytes,
        file_name="vendor_analyst_result.csv",
        mime="text/csv"
    )

elif not metabase_file or not spx_file:
    st.info("📁 Please upload both Metabase and SPX Excel files to continue.")
