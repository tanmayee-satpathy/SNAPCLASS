import streamlit as st
from src.database.db import enroll_student_to_subject
from src.database.config import supabase
from PIL import Image
import time


@st.dialog("Capture or upload photos")
def add_photos_dialog():

    if 'attendance_images' not in st.session_state:
        st.session_state.attendance_images = []

    if 'captured_images' not in st.session_state:
        st.session_state.captured_images = []

    st.write('Add classroom photos to scan for attendance')

    if 'photo_tab' not in st.session_state:
        st.session_state.photo_tab = 'camera'

    t1, t2 = st.columns(2)

    with t1:
        type_camera = "primary" if st.session_state.photo_tab == 'camera' else 'tertiary'
        if st.button('Camera', type=type_camera, width='stretch'):
            st.session_state.photo_tab = 'camera'



    with t2:
        type_upload = "primary" if st.session_state.photo_tab == 'upload' else 'tertiary'
        if st.button('Upload photos', type=type_upload, width='stretch'):
            st.session_state.photo_tab = 'upload'

    if st.session_state.photo_tab == 'camera':

        if 'camera_key' not in st.session_state:
            st.session_state.camera_key = 0

        cam_photo = st.camera_input(
            'Take Snapshot',
            key=f"dialog_cam_{st.session_state.camera_key}"
        )

        if cam_photo is not None:

            image = Image.open(cam_photo).convert("RGB")

            st.session_state.attendance_images.append(image)

            st.success("Photo Captured Successfully")

            st.session_state.camera_key += 1

            st.rerun()
                

    if st.session_state.photo_tab == 'upload':
        uploaded_files = st.file_uploader( 'choose image files', type=['jpg', 'png', 'jpeg' ], accept_multiple_files=True, key='dialog_upload')

        if uploaded_files:
            for f in uploaded_files:
                image = Image.open(f)
                st.session_state.attendance_images.append(image)
            st.success('Photos Uploaded Successfully')

    st.divider()
    if st.button('Done', type='primary', width='stretch'):

        st.session_state.show_photo_dialog = False

        st.rerun()