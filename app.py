import streamlit as st
from styles import get_css, motivational_quotes
from viber_blast import viber_blast_section
from email_blast_bucket2 import email_blast_bucket2_section
from email_blast_bucket4 import email_blast_bucket4_section
from email_blast_level1 import email_blast_level1_section
from email_blast_level6 import email_blast_level6_section
from email_blast_sbf_salad import email_blast_sbf_salad_section
from email_blast_sbf_pl import email_blast_sbf_pl_section
from live_inbound_monitoring import live_inbound_monitoring_section
from auto_statistics import auto_statistics_section
import random

# Initialize session state
if 'button1_clicked' not in st.session_state:
    st.session_state.button1_clicked = False
if 'button2_clicked' not in st.session_state:
    st.session_state.button2_clicked = False
if 'button3_clicked' not in st.session_state:
    st.session_state.button3_clicked = False
if 'button4_clicked' not in st.session_state:
    st.session_state.button4_clicked = False
if 'uploaded_file' not in st.session_state:
    st.session_state.uploaded_file = None
if 'collector_file' not in st.session_state:
    st.session_state.collector_file = None
if 'menu_open' not in st.session_state:
    st.session_state.menu_open = False
if 'email_bucket_option' not in st.session_state:
    st.session_state.email_bucket_option = "Bucket 2 with sequence template"
if 'auto_stats_option' not in st.session_state:
    st.session_state.auto_stats_option = "SBF NEGATIVE AUTOSTATS"
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'login_error' not in st.session_state:
    st.session_state.login_error = False

# Define credentials
USERNAME = "zmjepollo"
PASSWORD = "Hepollo_021"

# Login function
def check_login():
    st.markdown('<div class="main-content">', unsafe_allow_html=True)
    st.title("Login to WORKLOADS-AUTOMATED")
    username = st.text_input("Username", key="username_input")
    password = st.text_input("Password", type="password", key="password_input")
    if st.button("Login"):
        if username == USERNAME and password == PASSWORD:
            st.session_state.logged_in = True
            st.session_state.login_error = False
            st.rerun()
        else:
            st.session_state.login_error = True
    if st.session_state.login_error:
        st.error("Invalid username or password. Please try again.")
    st.markdown('</div>', unsafe_allow_html=True)

# Main app logic
if not st.session_state.logged_in:
    check_login()
else:
    # Set page configuration
    st.set_page_config(page_title="WORKLOADS-AUTOMATED", page_icon="📊", layout="wide")

    # Apply custom CSS
    st.markdown(get_css(), unsafe_allow_html=True)

    # Select a random quote
    random_quote = random.choice(motivational_quotes)

    # Header section
    col1, col2, col3 = st.columns([1, 3, 1])
    with col2:
        st.title(random_quote)

    # Sidebar with burger menu
    with st.sidebar:
        if st.session_state.menu_open:
            if st.button("✕ Close", key="close_menu", help="Close the menu"):
                st.session_state.menu_open = False
        else:
            if st.button("☰", key="burger_menu", help="Open the menu"):
                st.session_state.menu_open = True

        if st.session_state.menu_open:
            st.markdown('<div class="sidebar-content active">', unsafe_allow_html=True)
            if st.button("VIBER BLAST", help="Access Viber Blast CSV Uploader"):
                st.session_state.button1_clicked = True
                st.session_state.button2_clicked = False
                st.session_state.button3_clicked = False
                st.session_state.button4_clicked = False
                st.session_state.uploaded_file = None
                st.session_state.collector_file = None
            if st.button("EMAIL BLAST", help="Access Email Blast File Uploader"):
                st.session_state.button1_clicked = False
                st.session_state.button2_clicked = True
                st.session_state.button3_clicked = False
                st.session_state.button4_clicked = False
                st.session_state.uploaded_file = None
                st.session_state.collector_file = None
            if st.button("LIVE INBOUND MONITORING", help="Access MC4 Blasting Monitoring Dashboard"):
                st.session_state.button1_clicked = False
                st.session_state.button2_clicked = False
                st.session_state.button3_clicked = True
                st.session_state.button4_clicked = False
                st.session_state.uploaded_file = None
                st.session_state.collector_file = None
            if st.button("AUTO STATISTICS", help="Access Auto Statistics Dashboard"):
                st.session_state.button1_clicked = False
                st.session_state.button2_clicked = False
                st.session_state.button3_clicked = False
                st.session_state.button4_clicked = True
                st.session_state.uploaded_file = None
                st.session_state.collector_file = None
            if st.button("Logout", help="Log out of the application"):
                st.session_state.logged_in = False
                st.session_state.login_error = False
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="sidebar-content">', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

    # Main content
    with st.container():
        st.markdown('<div class="main-content">', unsafe_allow_html=True)
        
        if not (st.session_state.button1_clicked or st.session_state.button2_clicked or 
                st.session_state.button3_clicked or st.session_state.button4_clicked):
            st.subheader("Welcome")
            st.write("Click the ☰ menu in the sidebar and select a feature to begin.")
        elif st.session_state.button1_clicked:
            viber_blast_section()
        elif st.session_state.button2_clicked:
            bucket_option = st.selectbox(
                "Select Campaign",
                ["Bucket 2 with sequence template", "Bucket 4 Generic Template", "LEVEL 1 NEGATIVE ACCOUNTS", 
                 "LEVEL 6 NEGATIVE ACCOUNTS", "SBF SALAD NEGATIVE ACCOUNT", "SBF PL NEGATIVE ACCOUNTS"],
                help="Choose the bucket for email blast processing",
                key="email_bucket_select",
                index=["Bucket 2 with sequence template", "Bucket 4 Generic Template", "LEVEL 1 NEGATIVE ACCOUNTS", 
                       "LEVEL 6 NEGATIVE ACCOUNTS", "SBF SALAD NEGATIVE ACCOUNT", "SBF PL NEGATIVE ACCOUNTS"].index(st.session_state.email_bucket_option)
            )
            st.session_state.email_bucket_option = bucket_option
            if bucket_option == "Bucket 2 with sequence template":
                email_blast_bucket2_section()
            elif bucket_option == "Bucket 4 Generic Template":
                email_blast_bucket4_section()
            elif bucket_option == "LEVEL 1 NEGATIVE ACCOUNTS":
                email_blast_level1_section()
            elif bucket_option == "LEVEL 6 NEGATIVE ACCOUNTS":
                email_blast_level6_section()
            elif bucket_option == "SBF SALAD NEGATIVE ACCOUNT":
                email_blast_sbf_salad_section()
            elif bucket_option == "SBF PL NEGATIVE ACCOUNTS":
                email_blast_sbf_pl_section()
        elif st.session_state.button3_clicked:
            live_inbound_monitoring_section()
        elif st.session_state.button4_clicked:
            auto_statistics_section()

        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="footer">Viber Blast Uploader v1.3 | Aug 07, 2025 07:55 AM PHT</div>', unsafe_allow_html=True)