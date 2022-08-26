from datetime import datetime
from requests import get
import streamlit as st
import pandas as pd
import numpy as np

st.markdown('''
# Looking for taxifare predictions 🔮 and ballons 🎈?
## You are in the right place!

1. Select your ride date and time
''')

col1, col2 = st.columns(2)
date_pick = col1.date_input("Pickup day", datetime(2018, 10, 27))
time_pick = col2.time_input("Pickup time", datetime.now())

st.markdown('''
2. Select your pickup and dropoff location

💡 You can check in the map if they are correct
''')

col1, col2 = st.columns(2)
pickup_lat = col1.number_input('Pickup latitude', value=40.75, step=0.001)
pickup_lon = col2.number_input('Pickup longitude', value=-73.99, step=0.001)
dropoff_lat = col1.number_input('Dropoff latitude', value=40.65, step=0.001)
dropoff_lon = col2.number_input('Dropoff longitude', value=-73.96, step=0.001)
st.map(
    pd.DataFrame([[pickup_lon, pickup_lat], [dropoff_lon, dropoff_lat]],
                 columns=['lon', 'lat']))

st.markdown('''
3. Select the number of passengers
''')
slider = st.slider('Number of passengers', 1, 8, 1)

url = 'https://api-2jt2jxjmya-ew.a.run.app/predict'

if st.button('Make magic 🪄'):
    params = {
        'pickup_datetime': f'{date_pick} {time_pick}',
        'pickup_latitude': pickup_lat,
        'pickup_longitude': pickup_lon,
        'dropoff_latitude': dropoff_lat,
        'dropoff_longitude': dropoff_lon,
        'passenger_count': slider
    }

    res = get(url, params=params).json()
    st.metric('Fare amount', f"{res['fare_amount']} $")
    st.balloons()

else:
    st.markdown('Press the button above')
