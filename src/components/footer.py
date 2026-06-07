import streamlit as st

# follows DRY principle  - Don't Repeat Yourself
def footer_home():
    st.markdown(
        (
            "<div style='text-align:center;color:rgba(245,243,255,0.98);margin-top:32px;"
            "margin-bottom:6px;font-size:0.98rem;letter-spacing:0.2px;"
            "text-shadow:0 1px 10px rgba(0,0,0,0.40);'>"
            "Created with &#10084; by <b>Tanmayee</b></div>"
        ),
        unsafe_allow_html=True,
    )


def footer_dashboard():
    st.markdown(
        (
            "<div style='text-align:center;color:rgba(237,233,255,0.98);margin-top:28px;"
            "margin-bottom:14px;font-size:0.98rem;letter-spacing:0.25px;"
            "text-shadow:0 1px 10px rgba(0,0,0,0.45);'>"
            "Created with &#10084; by <b>Tanmayee</b></div>"
        ),
        unsafe_allow_html=True,
    )


#  2 footer func instead of 1 as diff screens require diff spacing and styling