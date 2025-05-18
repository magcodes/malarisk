

import streamlit as st
import joblib
import numpy as np
import streamlit.components.v1 as components

# Load model
model = joblib.load('./models/malaria_predictor.pkl')

with open('./data/cleaned/malaria_map.html', 'r') as f:
    map_html = f.read()

st.title("Malaria Cases Predictor for Nigeria")

# Input fields
state = st.selectbox("Select State", ['Lagos', 'Kano', 'Kaduna', 'Rivers', 
'Oyo', 'Enugu', 'Abuja', 'Borno', 'Sokoto', 'Ondo', 'Benue', 'Delta'])
year = st.slider("Select Year", 2015, 2020, 2018)

s2_ndvi = st.number_input("Enter Sentinel-2 NDVI", min_value=-1.0, 
max_value=1.0, value=0.2)
s3_ndvi = st.number_input("Enter Sentinel-3 NDVI", min_value=-1.0, 
max_value=1.0, value=0.1)
s3_temp = st.number_input("Enter Sentinel-3 Temperature (Kelvin)", 
min_value=250.0, max_value=320.0, value=290.0)

if st.button("Predict Malaria Cases"):
    # Prepare features array
    features = np.array([[s2_ndvi, s3_ndvi, s3_temp, year]])
    prediction = model.predict(features)[0]
    st.success(f"Predicted Malaria Cases: {int(prediction)}")

st.markdown("---")
st.markdown("### Malaria Cases Map")
components.html(map_html, height=600)
