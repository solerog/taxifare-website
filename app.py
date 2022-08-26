from datetime import datetime
from requests import get
import streamlit as st
import pandas as pd
import numpy as np
'''
# TaxiFareModel front
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')
'''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

1. Let's ask for:
- date and time
- pickup longitude
- pickup latitude
- dropoff longitude
- dropoff latitude
- passenger count
'''
col1, col2 = st.columns(2)
date_pick = col1.date_input("Pickup day", datetime(2018, 10, 27))
time_pick = col2.time_input("Pickup time", datetime.now())
pickup_lat = col1.number_input('Pickup latitude', value=40.75, step=0.001)
pickup_lon = col2.number_input('Pickup longitude', value=-73.99, step=0.001)
dropoff_lat = col1.number_input('Dropoff latitude', value=40.65, step=0.001)
dropoff_lon = col2.number_input('Dropoff longitude', value=-73.96, step=0.001)
slider = st.slider('Number of passengers', 1, 8, 1)
st.map(
    pd.DataFrame([[pickup_lon, pickup_lat], [dropoff_lon, dropoff_lat]],
                 columns=['lon', 'lat']))
'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡

2. Let's build a dictionary containing the parameters for our API...

3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
'''
url = 'https://api-2jt2jxjmya-ew.a.run.app/predict'

if st.button('Make prediction'):
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
    st.write('No prediction yet')
