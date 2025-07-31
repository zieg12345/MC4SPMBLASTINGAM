import streamlit as st

def live_inbound_monitoring_section():
    st.subheader("LIVE INBOUND MONITORING")
    st.markdown(
        """
        <iframe src="https://spmadridlaw.sg.larksuite.com/share/base/dashboard/shrlgmGDFf4zcgqMR1vVl9044Nh" 
        class="dashboard-iframe" 
        width="100%" 
        height="600px" 
        frameborder="0" 
        allow="fullscreen">
        </iframe>
        """,
        unsafe_allow_html=True
    )