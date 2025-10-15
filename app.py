import streamlit as st
from datetime import datetime
import styles
import viber_blast
import email_blast_bucket2
import email_blast_bucket4
import email_blast_level1
import email_blast_level6
import email_blast_sbf_salad
import email_blast_sbf_pl
import mc4_ptp
import auto_statistics
import live_inbound_monitoring
import random
import email_blast_sbf_new_endo

# Hardcoded credentials
USERNAME = "zmjepollo"
PASSWORD = "Hepollo_021"

# Set page configuration
st.set_page_config(
    page_title="WORKLOADS-AUTOMATED",
    page_icon="📊",
    layout="wide"
)

# Apply custom CSS
st.markdown(styles.custom_css, unsafe_allow_html=True)

# Initialize session state for login
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# Login section
if not st.session_state.logged_in:
    st.header("Login to WORKLOADS-AUTOMATED")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Login"):
        if username == USERNAME and password == PASSWORD:
            st.session_state.logged_in = True
            st.success("Logged in successfully!")
            st.rerun()
        else:
            st.error("Invalid username or password")
else:
    # Display motivational quote
    st.markdown(f"<div class='quote-box'>{random.choice(styles.motivational_quotes)}</div>", unsafe_allow_html=True)

    # Sidebar with burger menu
    with st.sidebar:
        st.markdown(
            """
            <style>
            .sidebar .sidebar-content {
                background-color: #f0f2f6;
            }
            .burger-menu {
                font-size: 24px;
                cursor: pointer;
                padding: 10px;
                background-color: #007bff;
                color: white;
                text-align: center;
                border-radius: 5px;
            }
            .burger-menu:hover {
                background-color: #0056b3;
            }
            </style>
            <div class="burger-menu">☰ Menu</div>
            """,
            unsafe_allow_html=True
        )

        # Dropdown menu for selecting options
        option = st.selectbox(
            "Select an option:",
            [
                "VIBER BLAST",
                "EMAIL BLAST",
                "LIVE INBOUND MONITORING",
                "AUTO STATISTICS"
            ],
            key="main_option"
        )

    # Conditional rendering based on selected option
    if option == "VIBER BLAST":
        viber_blast.viber_blast_section()
    elif option == "EMAIL BLAST":
        email_option = st.selectbox(
            "Select Email Blast Type:",
            [
                "BUCKET 2",
                "BUCKET 4",
                "LEVEL 1 NEGATIVE ACCOUNT",
                "LEVEL 6 NEGATIVE ACCOUNT",
                "SBF SALAD NEGATIVE ACCOUNT",
                "SBF PL NEGATIVE ACCOUNT",
                "MC4 PTP",
                "SBF NEW ENDO"
            ],
            key="email_blast_option"
        )
        if email_option == "BUCKET 2":
            email_blast_bucket2.email_blast_bucket2_section()
        elif email_option == "BUCKET 4":
            email_blast_bucket4.email_blast_bucket4_section()
        elif email_option == "LEVEL 1 NEGATIVE ACCOUNT":
            email_blast_level1.email_blast_level1_section()
        elif email_option == "LEVEL 6 NEGATIVE ACCOUNT":
            email_blast_level6.email_blast_level6_section()
        elif email_option == "SBF SALAD NEGATIVE ACCOUNT":
            email_blast_sbf_salad.email_blast_sbf_salad_section()
        elif email_option == "SBF PL NEGATIVE ACCOUNT":
            email_blast_sbf_pl.email_blast_sbf_pl_section()
        elif email_option == "MC4 PTP":
            mc4_ptp.mc4_ptp_section()
        elif email_option == "SBF NEW ENDO":
            email_blast_sbf_new_endo.email_blast_sbf_new_endo_section()
    elif option == "LIVE INBOUND MONITORING":
        live_inbound_monitoring.live_inbound_monitoring_section()
    elif option == "AUTO STATISTICS":
        auto_option = st.selectbox(
            "Select Auto Statistics Type:",
            [
                "SBF NEGATIVE AUTOSTATS",
                "L1-L6 NEGATIVE AUTOSTATS",
                "SBF NEW ENDO"
            ],
            key="auto_statistics_option"
        )
        if auto_option == "SBF NEGATIVE AUTOSTATS":
            auto_statistics.auto_statistics_section()
        elif auto_option == "L1-L6 NEGATIVE AUTOSTATS":
            auto_statistics.auto_statistics_section()
        elif auto_option == "SBF NEW ENDO":
            auto_statistics.auto_statistics_sbf_new_endo_section()
    # Footer
    st.markdown(
        f"""
        <div class='footer'>
            <p>WORKLOADS-AUTOMATED v1.0 | Last updated: {datetime.now().strftime('%B %d, %Y %I:%M %p PST')}</p>
        </div>
        """,
        unsafe_allow_html=True
    )