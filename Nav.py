import streamlit as st

import time
import json
from selenium import webdriver

def get_nav_and_date(stock):
    options = webdriver.chrome.options.Options()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    #options.add_argument("--headless")  # Run in headless mode
    res = {'date': None, 'nav': None, 'previous close':None}
    driver = webdriver.Chrome(options=options)
    try:
        driver.get("https://digital.fidelity.com/prgw/digital/research/quote/dashboard/summary?symbol={}".format(stock))
        time.sleep(4)
        html = driver.page_source
        if len(html.split("Nav<")) > 1:
            date = html.split("Nav<")[1].split("As of")[1][0:7]
            val = html.split("Nav<")[1].split("right ng-star-inserted")[1][2:].split("<")[0]
            res['date'] = date
            res['nav'] = val
            print("Nav, date:{}, value:{}".format(date, val))

        if res['nav'] in ['--', None]:
            date = html.split("Previous close")[1].split("As of")[1][0:7]
            val = html.split("Previous close")[1].split("right ng-star-inserted")[1][2:].split("<")[0]
            res['date'] = date
            res['previous close'] = val
            print("Previous close, date:{}, value:{}".format(date, val))

    except Exception as e:
        st.error(body='Selenium Exception occured!', icon='🔥')
        st.error(body=str(e), icon='🔥')
    driver.quit()
    return res


st.title(":rainbow[Hello 👋, this is our nav generator app]")
# st.markdown(
#     """
#
#     ** :rainbow[SHOW ME THE MONEY]**
#
#     """
# )

#if st.button("Send balloons!"):
#    st.balloons()

res = get_nav_and_date('TQQQ')
st.write('TQQQ nav:')
st.write(res['nav'], res['date'])
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
    res = get_nav_and_date(prompt)
    st.write(res['nav'], res['date'])