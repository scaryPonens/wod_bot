import os

import streamlit as st
from dotenv import load_dotenv

from langchain_community.llms import Ollama

from crossfit_utils import build_coach, fetch_wod, summarize_and_format_wod, response_generator

load_dotenv()

st.title("WOD Bot")

if "llama_model" not in st.session_state:
    st.session_state["llama_model"] = os.getenv("LLAMA_MODEL")

if "random_wod" not in st.session_state:
    st.session_state["random_wod"] = fetch_wod()

if "llm" not in st.session_state:
    st.session_state["llm"] = Ollama(model=st.session_state['llama_model'])

if "coach" not in st.session_state:
    st.session_state["coach"] = build_coach()

if "summary" not in st.session_state:
    st.session_state["summary"] = summarize_and_format_wod(st.session_state["llm"], st.session_state["random_wod"])

st.markdown(st.session_state["summary"])

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("assistant"):
        response = st.write_stream(response_generator(st.session_state["llm"], st.session_state["coach"],
                                                      st.session_state["random_wod"], prompt))
    # Add user message to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})

