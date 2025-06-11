import streamlit as st
import yfinance as yf

import time

st.title(":rainbow[Hello 👋, this is our nav generator app]")
st.markdown(
    """

    ** :rainbow[SHOW ME THE MONEY]**

    """
)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Let's start chatting! 👇"}]

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("Provide SYMBOL:"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    print(prompt)
    ticker = yf.Ticker(prompt)
    st.write(ticker.info['navPrice']
)