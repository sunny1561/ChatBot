import openai
import streamlit as st
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()


import os
# Set your OpenAI API key
openai.api_key = os.getenv('open_api_key')

def chat_with_gpt4(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response['choices'][0]['message']['content']

# Streamlit app
st.title("GPT-4 Chatbot")

if "history" not in st.session_state:
    st.session_state.history = []

user_input = st.text_input("Ask Questions:", key="input")

if st.button("Send"):
    if user_input:
        st.session_state.history.append({"role": "user", "content": user_input})
        response = chat_with_gpt4(user_input)
        st.session_state.history.append({"role": "assistant", "content": response})

# Display conversation history
for message in st.session_state.history:
    if message["role"] == "user":
        st.write(f"You: {message['content']}")
    else:
        st.write(f"Chatbot: {message['content']}")

# Automatically scroll to the bottom of the chat history
st.experimental_rerun()
