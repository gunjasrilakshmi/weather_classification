import streamlit as st
import pandas as pd
import pickle
with open('classifier.pkl','rb')as f:
    model=pickle.load(f)
st.title("Weather classification")
temperature=st.number_input(label="Temperature")
humidity=st.number_input(label="Humidity")
windspeed=st.number_input(label="Wind Speed")
precipitation=st.number_input(label="Precipitation (%)")
cloudCover=st.selectbox(label="Cloud Cover",options=["Overcast", "Partly Cloudy","Clear ","Cloudy"])
AtmosphericPresssure=st.number_input(label='AtmosphericPressure')
UVindex=st.number_input(label='UVindex')
season=st.selectbox(label='Season',options=['Winter','Spring','Autumn','Summer'])
Visiblity=st.number_input(label='Visibility')
Location=st.selectbox(label='location',options=['inland','mountain','coastal'])
cloud_cover_map= {"Overcast": 0, "Partly Cloudy": 1, "Clear": 2, "Cloudy": 3}

season_map = {"Winter": 0, "Spring": 1, "Summer": 2, "Autumn": 3}


location_map = {"inland": 0, "mountain": 1, "coastal": 2}


#Create feature array
features = [[
    temperature, 
    humidity, 
    windspeed, 
    precipitation, 
    cloud_cover_map[cloudCover], 
    AtmosphericPresssure, 
    UVindex, 
    season_map[season],
    Visiblity, 
    location_map[Location]
]]
#predict button
if st.button('predit Wheather'):
    prediction=model.predict(features)
    if prediction[0]==0:
        st.success(f'Weather classification is rainy')
    elif prediction[0]==1:
        st.success(f'Weather classification is cloudy')
    elif prediction[0]==2:
        st.success(f'Weather classification is sunny')
    else:
        st.success(f'Weather classification is snowy')