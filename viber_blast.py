import streamlit as st
import pandas as pd
from datetime import datetime
from openpyxl import Workbook
from io import BytesIO

def viber_blast_section():
    st.subheader("Viber Blast CSV Uploader")
    
    # Dropdown for selecting bucket
    bucket_option = st.selectbox(
        "Select Campaign",
        ["Bucket 2", "Bucket 4"],
        help="Choose the bucket for Viber blast processing"
    )

    # File uploader
    uploaded_file = st.file_uploader(
        "📤 Choose a CSV file",
        type=["csv"],
        key=f"viber_blast_uploader_{bucket_option.lower().replace(' ', '_')}",
        help="Upload a CSV with columns: Client, Account No., Debtor Name, Contact No."
    )
    if uploaded_file is not None:
        st.session_state.uploaded_file = uploaded_file
        st.success("File uploaded successfully!")

    # Reset button
    if st.session_state.uploaded_file is not None:
        if st.button("🔄 Reset", help="Clear the uploaded file and reset"):
            st.session_state.uploaded_file = None
            st.session_state.button1_clicked = False
            st.rerun()

    # Sample data based on bucket
    if bucket_option == "Bucket 2":
        sample_data = {
            "Campaign": ["SAMPLE", "SAMPLE", "SAMPLE", "SAMPLE"],
            "CH Code": ["12345", "123456", "1234567", "12345678"],
            "First Name": ["", "", "", ""],
            "Full Name": ["Richard Arenas", "Jinnggoy Dela Cruz", "Roman Dalisay", "Edwin Paras"],
            "Last Name": ["", "", "", ""],
            "Mobile Number": ["09274186327", "09760368821", "09088925110", "09175791122"],
            "OB": ["", "", "", ""]
        }
    else:  # Bucket 4
        sample_data = {
            "Campaign": ["SAMPLE"],
            "CH Code": ["123456789"],
            "First Name": [""],
            "Full Name": ["Janica d Benbinuto"],
            "Last Name": [""],
            "Mobile Number": ["09655669672"],
            "OB": [""]
        }
    sample_df = pd.DataFrame(sample_data)

    # Dynamic filename
    current_date = datetime.now().strftime(f"VIBER BLAST {bucket_option.upper()} %b %d %Y %I:%M %p PST").upper()

    if st.session_state.uploaded_file is not None:
        try:
            # Read CSV without converting dtypes
            df = pd.read_csv(st.session_state.uploaded_file, encoding='utf-8-sig', skipinitialspace=True, dtype=str)
            df = df.fillna("")  # Replace NaN with empty string
            df.columns = df.columns.str.strip()
            required_columns = ["Client", "Account No.", "Debtor Name", "Contact No."]
            missing_columns = [col for col in required_columns if col not in df.columns]
            
            if missing_columns:
                st.error(f"The following required columns are missing: {', '.join(missing_columns)}")
            else:
                # Validate Contact No. length without type conversion
                invalid_contact_no = df[df["Contact No."].str.len() != 11]
                if not invalid_contact_no.empty:
                    st.warning(f"Found {len(invalid_contact_no)} rows where Contact No. is not 11 digits. These rows are still included but may need review.")
                initial_row_count_bel = len(df)
                df = df[~df["Account No."].str.contains("BEL", case=False, na=False)]
                if initial_row_count_bel != len(df):
                    st.info(f"Removed {initial_row_count_bel - len(df)} rows where Account No. contains 'BEL'.")
                initial_row_count = len(df)
                df = df.drop_duplicates(subset=["Account No."], keep="first")
                if initial_row_count != len(df):
                    st.info(f"Removed {initial_row_count - len(df)} duplicate rows based on 'Account No.'.")
                if len(df) == 0:
                    st.warning("No rows remain after filtering. Showing sample data only.")
                summary_df = pd.DataFrame({
                    "Campaign": df["Client"],
                    "CH Code": df["Account No."],
                    "First Name": [""] * len(df),
                    "Full Name": df["Debtor Name"],
                    "Last Name": [""] * len(df),
                    "Mobile Number": df["Contact No."],
                    "OB": [""] * len(df)
                })
                # Combine with sample data
                summary_df = pd.concat([summary_df, sample_df], ignore_index=True)
                st.subheader("Summary Table")
                st.dataframe(summary_df, use_container_width=True)
                output = BytesIO()
                wb = Workbook()
                ws = wb.active
                ws.title = "Viber Blast"
                headers = list(summary_df.columns)
                for col_num, header in enumerate(headers, 1):
                    ws.cell(row=1, column=col_num).value = header
                for row_num, row in enumerate(summary_df.values, 2):
                    for col_num, value in enumerate(row, 1):
                        ws.cell(row=row_num, column=col_num).value = str(value)
                        ws.cell(row=row_num, column=col_num).number_format = '@'
                wb.save(output)
                output.seek(0)
                st.download_button(
                    label="📥 Download Summary Table as Excel",
                    data=output,
                    file_name=f"{current_date}.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                    key="download_summary"
                )
        except Exception as e:
            st.error(f"An error occurred while processing the file: {str(e)}")
    else:
        st.subheader("Sample Summary Table")
        st.dataframe(sample_df, use_container_width=True)
        output = BytesIO()
        wb = Workbook()
        ws = wb.active
        ws.title = "Viber Blast"
        headers = list(sample_df.columns)
        for col_num, header in enumerate(headers, 1):
            ws.cell(row=1, column=col_num).value = header
        for row_num, row in enumerate(sample_df.values, 2):
            for col_num, value in enumerate(row, 1):
                ws.cell(row=row_num, column=col_num).value = str(value)
                ws.cell(row=row_num, column=col_num).number_format = '@'
        wb.save(output)
        output.seek(0)
        st.download_button(
            label="📥 Download",
            data=output,
            file_name=f"{current_date}.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            key="download_sample"
        )
        st.info("Please upload a CSV file to generate the summary table with your data.")