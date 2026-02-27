import streamlit as st
import time
import json
from pathlib import Path 

st.title("Course Management App")
st.divider()

next_assignment_id_number = 3

#load data
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

tab1, tab2, tab3 = st.tabs(["View Assignments", "Add New Assignment", "Update An Assignment"])

with tab1:
    tab_option = st.radio("View/Search", ["View", "Search"], horizontal=True)
    if tab_option == "View":
        st.dataframe(assignments)

with tab2:
    st.info("Coming soon...")
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
                
                #record into json file
                with json_path.open("w", encoding="utf-8") as f:
                    json.dump(assignments, f)

                st.success("New assignment is recorded!")
                st.info("This is a new assignment")
                st.dataframe(assignments) 

with tab3:
    st.info("Maybe coming soon...")

