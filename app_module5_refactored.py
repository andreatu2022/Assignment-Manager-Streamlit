#Update when you watch the lecture you missed

import streamlit as st
import time
import json
from pathlib import Path
import uuid

#Data Layer
def load_data():
    if json_path.exists(json_path):
        with open(json_path, "r") as f:
            assignemnts = json.load(f)
    else:
        assignments = []
    
    return assignments

def save_data(assignments, json_path):
    with open(json_path, "w") as f:
        


#Service Layer
def add_new_assignment(assignments, title, description, points, type):
    assignments.append(
        {
            "id": str(uuid.uuid4()),
            "title": title,
            "description": description, 
            "points": points,
            "type": type
        }
    )

    return assignments 

#UI Layer
def render_dashboard():
    pass

def render_add_new_assignment():
    pass

def main():
    pass
