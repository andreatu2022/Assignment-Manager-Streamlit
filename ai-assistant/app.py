import os
import streamlit as st

#Make sure you install the packages if it shows an error!
#pip install dotenv
#pip install openai
from dotenv import load_dotenv 
from openai import OpenAI 
import json
from pathlib import Path

load_dotenv()

st.set_page_config("AI Assistant - Open AI")
st.title("AI Assistant - Open AI")

api_key = os.getenv("OPEN_AI_KEY")

if not api_key:
    st.error("Open AI key was not found!")
    st.stop()

client = OpenAI(api_key=api_key) #Creating an object from the Open AI class and initializing it with my Open AI key

#Data Layer
def load_orders(filepath: str):
    json_path = Path(filepath)
    if json_path.exists():
        with open(json_path, "r") as f:
            return json.load(f)
    else:
        return []

#Load Logs
def load_logs(filepath:str):
    json_path = Path(filepath)
    if json_path.exists():
        with open(json_path, "r") as f:
            return json.load(f)
    else:
        return []

#Save Logs
def save_logs(filepath: str, logs:list):
    json_path = Path(filepath)
    with open(json_path, "w") as f:
        json.dump(logs, f)
    
if "messages" not in st.session_state:
    st.session_state['messages'] = []

orders = load_orders("ai-assistant/orders.json")
logs = load_logs("ai-assistant/ai_logs.json")

for log in logs:
    st.session_state['messsages'].append(
        {
            "role":log['role'],
            "content":log["content"]
        }
    )

if len(logs) == 0:
    st.session_state['messages'].append(
        {
            "role":'ai-assistant',
            "content": "Hi, how can I help you?"
        }
    )

with st.container(border=True, height=400):
    for message in st.session_state['messages']:
        with st.container(border=True):
            with st.chat_message(message['role']):
                st.markdown(message['content'])