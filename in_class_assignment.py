import streamlit as st
import json
from pathlib import Path
from datetime import datetime
import uuid
import time

st.set_page_config(page_title="Excused Absence App", layout="wide", initial_sidebar_state='expanded')

if "page" not in st.session_state:
    st.session_state['page'] = 'home'

requests = [
    {

        "request_id" : "0111212",
        "status": "Pending",
        "course_id": "011101",
        "student_email": "jsmith@university.edu",
        "absence_date": "2026-03-25",
        "submitted_timestamp": "2026-03-19 08:30:00",
        "excuse_type": "Medical",
        "explanation": "I have a scheduled doctor's appointment that I cannot reschedule.",
        "instructor_note": ""
    }
]

with st.sidebar:
    st.sidebar.title("Navigation")
    if st.button("Excused Absence", key="excused_absense_btn", type='primary', use_container_width=True):
        st.session_state['page'] = 'home'
        st.rerun()
    if st.button("Excused Absence Request Form", key="form_btn", type='primary', use_container_width=True):
        st.session_state['page'] = 'orders'
        st.rerun()

json_path_requests = Path('requests.json')

if json_path_requests.exists():
    with open(json_path_requests, "r") as f:
        requests = json.load(f)
else:
    requests = []

if st.session_state['page'] == 'home':
    st.markdown("# Excused Absence Homepage")
    st.divider()

    st.subheader("Excused Absenses")
    total_count = len(requests)
    pending_count = 0

    for request in requests:
        if request["status"] == "Pending":
            pending_count = pending_count + 1

    col1, col2, col3 = st.columns([4,2,2])
    with col2:
        st.metric("Count", total_count)
    with col3:
        st.metric("Pending", pending_count)
        

    col4, col5 = st.columns([2,1])
    with col4:
        st.text_input("Search By Student Email")
    with col5: 
        st.selectbox(
            "Status",
            ["All", "Pending", "Approved", "Cancelled"],
            key="dashboard_status_filter_select"
        )
