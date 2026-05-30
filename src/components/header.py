import streamlit as st
import base64
    
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()
def header_home():

    logo_path = "assets/logo.png"

    st.markdown(f"""
    <div style="
        display:flex;
        justify-content:center;
        width:100%;
        margin-top:10px;
        margin-bottom:10px;
    ">
        <img src="data:image/png;base64,{get_base64_image(logo_path)}"
            width="130">
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style='
        text-align:center;
        font-family:Poppins,sans-serif;
        font-size:72px;
        font-weight:700;
        letter-spacing:-4px;
        margin-top:-10px;
        margin-bottom:0px;
        background: linear-gradient(135deg,#FFFFFF,#C4B5FD,#8B5CF6);
        -webkit-background-clip:text;
        -webkit-text-fill-color:transparent;
    '>
        SNAPCLASS
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <p style='
        text-align:center;
        color:#9CA3AF;
        font-size:18px;
        margin-top:8px;
        margin-bottom:28px;
        letter-spacing:0.5px;
    '>
        AI-Powered Smart Attendance Platform
    </p>
    """, unsafe_allow_html=True)

def header_dashboard():

    st.markdown("""
    <h1 style='
        font-size:2.2rem;
        font-weight:700;
        color:#A78BFA;
        margin-bottom:0.2rem;
        white-space:nowrap;
    '>
        Teacher Dashboard
    </h1>
    """, unsafe_allow_html=True)

    