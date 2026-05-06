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

#Service Layer
def build_prompt():
    return "You are an AI Assistant in a online shopping website." \
    "This is a test. So create some example dataset, use it to respond to the user." \
    "If the user is asking about the prior conversation, try to reference your answer to the prior conversation."

def get_ai_response(client:OpenAI, chat_history:list):
    #Steps:
    #Build the prompt 
    prompt = build_prompt()

    #Build prompt message
    prompt_message = [
        {
            'role':'system',
            'content': prompt
        }
    ]

    #Build the final message
    messages = chat_history + prompt_message

    #Call OpenAI
    get_ai_response = client.chat.completions.create(
        model="gpt-5-mini",
        messages = messages,
        temperature=1
    )

    #Return the response
    return get_ai_response.choices[0].message.content


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
    
orders = load_orders("ai-assistant/orders.json")
logs = load_logs("ai-assistant/ai_logs.json")

if "messages" not in st.session_state:
    st.session_state['messages'] = []
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
                "role":'assistant',
                "content": "Hi, how can I help you?"
            }
        )

with st.container(border=True, height=400):
    for message in st.session_state['messages']:
        with st.chat_message(message['role']):
            st.markdown(message['content'])

user_input = st.chat_input("Type your question...")
if user_input:
    st.session_state['messages'].append(
        {
            "role":'user',
            "content":user_input
        }
    )
    with st.chat_message('user'):
        st.markdown(user_input)
    with st.chat_message('assistant'):
        with st.spinner("Thinking..."):
            ai_response = get_ai_response(client=client, chat_history= st.session_state['messages'], context_hint="healthcare")

            st.makrdown(ai_response)

            st.session_state['messages'].append(
                {
                    'role':'assistant',
                    "content":ai_response
                }
            )
    
    logs = load_logs("ai-assistant/ai_logs.json")
    logs.append(
        {
            "user_message":user_input,
            "assistant_message":ai_response
        }
    )

    save_logs("ai-assistant/ai_logs.json", logs=logs)