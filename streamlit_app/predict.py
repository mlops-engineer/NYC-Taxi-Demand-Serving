import streamlit as st
import requests
import time
import subprocess
import session_state

current_session = session_state.get(load=False)

st.title('NYC Taxi Demand Prediction')

st.sidebar.subheader("Predict Option")

month = st.sidebar.number_input('Month', min_value=1, max_value=12, value=1)
day = st.sidebar.number_input('Day', min_value=1, max_value=31, value=14)
weekday = st.sidebar.number_input('weekday', min_value=0, max_value=6, value=2)
hour = st.sidebar.number_input('Hour', min_value=0, max_value=23, value=17)
is_weekend = st.sidebar.number_input('Is Weekend', min_value=0, max_value=1, value=0)
lag_1h_cnt = st.sidebar.number_input('lag_1h_cnt', min_value=0, value=1103)
lag_1d_cnt = st.sidebar.number_input('lag_1d_cnt', min_value=0, value=1189)
lag_7d_cnt = st.sidebar.number_input('lag_7d_cnt', min_value=0, value=1730)
lag_14d_cnt = st.sidebar.number_input('lag_14d_cnt', min_value=0, value=1800)
avg_14d_cnt = st.sidebar.number_input('avg_14d_cnt', min_value=0.0, value=969.17)
avg_21d_cnt = st.sidebar.number_input('avg_21d_cnt', min_value=0.0, value=879.14)
std_14d_cnt = st.sidebar.number_input('std_14d_cnt', min_value=0, value=507)
std_21d_cnt = st.sidebar.number_input('std_21d_cnt', min_value=0, value=477)
zip_code_le = st.sidebar.number_input('zip_code_le', min_value=0, value=13)

commands = ["bentoml", "serve", "NycTaxiPredictionRFService:latest"]

if current_session.load == False:
    subprocess.Popen(
        commands
    )
    current_session.load = True
    time.sleep(10)

if st.sidebar.button("Predict"):
    response = requests.post("http://127.0.0.1:5000/predict",
                             json=[[month, day, weekday, hour, is_weekend, lag_1h_cnt, lag_1d_cnt, lag_7d_cnt,
                                    lag_14d_cnt, avg_14d_cnt, avg_21d_cnt, std_14d_cnt, std_21d_cnt, zip_code_le]])

    print(response.text)

    st.text(f'Predict Result : {response.text}')
