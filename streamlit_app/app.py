import streamlit as st
import os
from confirm_button_hack import cache_on_button_press

root = os.path.join(os.path.dirname(__file__))

dashboards = {
    "NYC Taxi Demand Prediction": os.path.join(root, "predict.py"),
    "Temp": os.path.join(root, "temp.py"),
}


@cache_on_button_press('Authenticate')
def authenticate(username, password):
    return username == "user" and password == "fsdl"


st.sidebar.subheader("Login")

username = st.sidebar.text_input('username')
password = st.sidebar.text_input('password', type='password')

if authenticate(username, password):
    st.sidebar.success('You are authenticated!')
else:
    st.sidebar.error('The username or password you have entered is invalid.')

choice = st.sidebar.radio("Mode", list(dashboards.keys()))

path = dashboards[choice]
with open(path, encoding="utf-8") as code:
    exec(code.read(), globals())

