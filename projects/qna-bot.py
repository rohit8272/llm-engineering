import os

from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI
llm = ChatOpenAI(
    model="qwen3.8-27b",
    api_key=os.environ["EXPLABS_API_KEY"],
    base_url="https://api.experientiallabs.ai/v1",
)


import streamlit as st

st.title("QNA BOT")
st.markdown("This is a simple QNA bot using LangChain and EXPLABS API")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    role = message["role"]
    content = message["content"]
    st.chat_message(role).markdown(content)


query = st.chat_input("Ask anything (type 'exit' to quit): ")

if query:
    st.session_state.messages.append({"role": "user", "content": query})
    st.chat_message("user").markdown(query)
    res = llm.invoke(query)
    st.chat_message("ai").markdown(res.content)
    st.session_state.messages.append({"role": "ai", "content": res.content})
