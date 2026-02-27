#How to run the Streamlit app: 
    #streamlit run (name of file)
    #Example: streamlit run app_day2.py for this file

import streamlit as st

st.title("Course Management")
st.header("Assignment Management")
st.subheader("Dashboard")

next_assignment_id_number = 3

st.divider()
st.markdown("--------") #Makes space

#Load data
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

#Input
#st.markdown("# Add New Assignment")
st.markdown("## Add New Assignment")
#st.markdown("### Add New Assignment")

title = st.text_input("Title")
description = st.text_area("Description", placeholder="Normalization is covered here", 
                           help="Here you are entering the assignment details")
points = st.number_input("Points")

#assignment_type = st.text_input("Assignment Type")
assignment_type = st.radio("Type", ["Homework","Lab"], horizontal=True)
st.caption("Homework type")

assignment_type2 = st.selectbox("Type", ["Select an option","Homework", "Lab", "Other"])
if assignment_type2 == "Other":
    assignment_type2 = st.text_input("Type", placeholder = "Enter the assignment type")

due_date = st.date_input("Due Date")

btn_save = st.button("Save", width="stretch", disabled=False)

import time

if btn_save:
    if not title:
        st.warning("Title needs to be provided!")
    else:
        with st.spinner("Assignment is being recorded..."):
            time.sleep(5)

            new_assignment_id = "HW" + str(next_assignment_id_number)
            next_assignment_id_number += 1

            assignments.append(
                {
                    "id":new_assignment_id,
                    "title":title,
                    "description":description,
                    "points":points,
                    "type":assignment_type
                }
            )

            st.success("New assignment is recorded!")
            st.info("This is a new assignment")
            st.dataframe(assignments)
    