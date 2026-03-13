import streamlit as st
import json
from pathlib import Path
from datetime import datetime
import uuid
import time

st.set_page_config(page_title="Course Manager", layout="centered")

#st.session_state remembers the past!
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False #initial value, no one is logged in

if "user" not in st.session_state:
    st.session_state["user"] = None

if "role" not in st.session_state:
    st.session_state["role"] = None

if "page" not in st.session_state:
    st.session_state["page"] = "login"

users = [
    {
        "id": "1",
        "email": "admin@school.edu",
        "full_name": "System Admin",
        "password": "123ssag@43AE",
        "role": "Admin",
        "registered_at": "..." 
    }
]

json_path = Path("users.json")
if json_path.exists():
    with open(json.path, "r") as f:
        users = json.load


assignments = [
    {
        "id":"HW1",
        "title":"Intro to Database",
        "description":"Basics of Database Design",
        "points":100,
        "type":"Homework"
    },
    {
        "id":"HW2",
        "title":"Normalization",
        "description":"Normalizing",
        "points":100,
        "type":"Homework"
    }
]

json_path = Path("assignments.json")
#Load the data from a json file
if json_path.exists():
    with json_path.open("r", encoding="utf-8") as f:
        assignments = json.load(f)


json_path = Path("users.json")
if json_path.exists():
    with open(json.path, "r") as f:
        users = json.load


if st.session_state["role"] == "Instructor":
    if st.session_state["page"] == "home":
        st.markdown("Welcome! This is the Instructor Dashboard")
        if st.button("Go To Dashboard", key="dashboard_view_btn", type="primary", use_container_width=True):
            st.session_state["page"] = "dashboard"
            st.rerun()
    elif st.session_state["page"] == "dashboard":
        st.markdown("Dashboard")

    


elif st.session_state["role"] == "Admin":
    st.markdown("Welcome! This is the Admin Dashboard")

    if st.button("Log Out", type="primary", use_container_width=True):
        with st.spinner("Logging out..."):
            st.session_state["logged_in"] = False
            st.session_state["user"] = None
            st.session_state["role"] = None
            st.session_state["page"] = "login"
            time.sleep(4)

            #After every important action, you need to rerun the page!
            st.rerun()

else:
    # --- LOGIN ---
    st.subheader("Log In")
    with st.container(border=True):
        email_input = st.text_input("Email", key="login_email")
        password_input = st.text_input("Password", type="password", key="login_password")
        
        if st.button("Log In"):
            with st.spinner("Logging in..."):
                time.sleep(2) # Fake backend delay
                
                # Find user
                found_user = None
                for user in users:
                    if user["email"].strip().lower() == email_input.strip().lower() and user["password"] == password_input:
                        found_user = user
                        break
                
                if found_user:
                    st.success(f"Welcome back, {found_user['email']}!")
                    st.session_state["logged_in"] = True
                    st.session_state["user"] = found_user
                    st.session_state["role"] = found_user["role"]
                    st.session_state["page"] = "home"

                    st.sucess("Login sucessful!")
                    time.sleep(2)
                    st.rerun()
                else:
                    st.error("Invalid credentials")

    # --- REGISTRATION ---
    st.subheader("New Instructor Account")
    with st.container(border=True):
        new_email = st.text_input("Email Address", key="reg_email")
        new_password = st.text_input("Password", type="password", key="reg_password")
        
        if st.button("Create Account"):
            with st.spinner("Creating account..."):
                time.sleep(2) # Fake backend delay
                # ... (Assume validation logic here) ...
                users.append({
                    "id": str(uuid.uuid4()),
                    "email": new_email,
                    "password": new_password,
                    "role": "Instructor"
                })

                with open(json_path, "w") as f:
                    json.dump(users, f)

                st.success("Account created!")
                st.rerun()

    st.write("---")
    st.dataframe(users)

with st.sidebar:
    st.markdown("Course Manager Sidebar")
    if st.session_state["logged_in"] == True:
        user = st.session_state["user"]
        st.markdown(f"Logged User Email: {user["email"]}")