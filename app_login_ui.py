import streamlit as st
import json 
from pathlib import Path 
import datetime
import uuid
import time

st.set_page_config(page_title="Course Manager", 
                   page_icon="",
                   layout="centered",
                   initial_sidebar_state="collapsed"
                   )

st.title("Course Manager")

next_user_id_number = 2

users = [{
        "id": "1",
        "email": "admin@school.edu",
        "full_name": "System Admin",
        "password": "123ssag@43AE",
        "role": "Admin",
        "registered_at": "..." 
        }]

json_file = Path("users.json")
if json_file.exists():
    with json_file.open("r", encoding="utf-8") as f:
        users = json.load(f)

tab1, tab2 = st.tabs(["Login", "Register"])

with tab2:
    st.markdown("## New Instructor Account")
    email_address = st.text_input("Email Address", placeholder = "Enter your email address")
    full_name = st.text_input("Full Name", placeholder = "Enter your full name name")
    password = st.text_input("Password", placeholder = "Enter your password", type="password")
    role = st.selectbox("Role", ["Instructor"])

    btn_save = st.button("Create Account", width="stretch", disabled=False)

    if btn_save:
        if not email_address and full_name and password:
            st.warning("Please enter all credientals to create an account!")
        else:
            with st.spinner("Creating your account..."):
                time.sleep(5)

                new_user_id = str(next_user_id_number)
                next_user_id_number += 1

                users.append(
                    {
                        "id":new_user_id,
                        "email":email_address,
                        "full_name":full_name,
                        "password":password,
                        "role":role,
                        "registered_at":"..."
                    }
                )
                
                with json_file.open("w", encoding="utf-8") as f:
                    json.dump(users, f)

                st.success("Account created successfully!")
                st.dataframe(users) 

with tab1:
    login_email_address = st.text_input("Login Email Address", placeholder = "Enter your email address")
    login_password = st.text_input("Login Password", placeholder = "Enter your password", type="password")
    login_btn_save = st.button("Log In", type="primary", use_container_width=True)

    if login_btn_save:
        with st.spinner("Verifying credentials..."):
            time.sleep(5)
            
            found_user = None
            for user in users:
                if user["email"] == login_email_address and user['password'] == login_password:
                    found_user = user
                    break

            if found_user:
                st.success("Welcome Back!")
            else:
                st.error("Invalid email or password")

    st.subheader("User Database")
    st.dataframe(users)

