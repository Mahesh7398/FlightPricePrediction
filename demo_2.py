# Import necessary libraries
import streamlit as st
import joblib
import numpy as np
import pandas as pd
from datetime import datetime
import pickle

def main():
    # Set up Streamlit app
    st.title("Flight Price Prediction App")
    st.write("Predict flight prices based on user inputs.")

    # Define input fields for the features required by the model
    st.sidebar.header("Enter Flight Details:")

    # Airline
    airline = st.sidebar.selectbox("Airline", ["Air India", "AirAsia", "GO FIRST", "Indigo","SpiceJet","StarAir","Trujet","Vistara"])
    airline_mapping = {"Air India": 0, "AirAsia": 1, "GO FIRST": 2, "Indigo": 3, "SpiceJet": 4, "StarAir": 5, "Trujet": 6, "Vistara": 7}
    airline_encoded = airline_mapping[airline]

    # Class
    flight_class = st.sidebar.selectbox("Class", ["Economy", "Business", "First Class"])
    class_mapping = {"Economy": 0, "Business": 1, "First Class": 2}
    class_encoded = class_mapping[flight_class]

    # Departure city
    from_city = st.sidebar.selectbox("From City", ["Bangalore", "Chennai", "Delhi", "Hyderabad", "Kolkata", "Mumbai"])
    from_city_mapping = {"Bangalore": 0, "Chennai": 1, "Delhi": 2, "Hyderabad": 3, "Kolkata": 4, "Mumbai": 5}
    from_city_encoded = from_city_mapping[from_city]

    # Destination city
    to_city = st.sidebar.selectbox("To City", ["Bangalore", "Chennai", "Delhi", "Hyderabad", "Kolkata", "Mumbai"])
    to_city_mapping = {"Bangalore": 0, "Chennai": 1, "Delhi": 2, "Hyderabad": 3, "Kolkata": 4, "Mumbai": 5}
    to_city_encoded = to_city_mapping[to_city]

    # Duration
    duration = st.sidebar.number_input("Duration (minutes)", min_value=30, max_value=1440, step=30)

    # Stops
    stops = st.sidebar.selectbox("Stops", ["Non-stop", "1 Stop", "2+ Stops"])
    stops_mapping = {"Non-stop": 0, "1 Stop": 1, "2+ Stops": 2}
    stops_encoded = stops_mapping[stops]

    # Date of the flight
    flight_date = st.sidebar.date_input("Flight Date")
    day = flight_date.day
    month = flight_date.month
    year = flight_date.year

    # Time of day (inferred from departure hour)
    departure_hour = st.sidebar.slider("Departure Hour", 0, 23, 12)
    time_of_day = 0

    # Collect inputs for prediction
    input_data = np.array([
        [airline_encoded, from_city_encoded, to_city_encoded, duration, stops_encoded,
         day, month, year, departure_hour, time_of_day, class_encoded]
    ])
    
    with open('random_forest_model.pkl', 'rb') as file:
        loaded_model = pickle.load(file)

    # Prediction Button
    if st.button("Predict Price"):
        # Make prediction
        predicted_price = loaded_model.predict(input_data)[0]
        st.write(f"### Predicted Price: {predicted_price:.2f}")

main()

