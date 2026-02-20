import streamlit as st

#1. Step 1: Header first (text elements)
st.title("Course Manager")
st.header("Course Assignments Manager")
st.subheader("Course Assignment Manager")

st.divider()
#2. Step 2: Define assignments list (data continunity)

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

#3. Step 3: Add new assignment section 
#col1, col2 = st.columns(2) -> this will give you 50%-50%
st.subheader("Add New Assignment")

with st.container(border = True):


    col1, col2 = st.columns([2,1])
    #col1, col2 = st.columns([1,6,1])

    with col1:
        with st.container(border=True):
            st.markdown("### Assignment Details")
            title = st.text_input("Assignment Title", placeholder = "Homework1", help = "Enter a short name")
            description = st.text_area("Assignment Description", placeholder = "Ex. Details...")

    with col2:
        st.markdown("**Due Date Selection**")
        due_date = st.date_input("Due Date")