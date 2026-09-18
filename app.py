import streamlit as st
import pandas as pd
import joblib

model = joblib.load("car_price_model.pkl")

st.title("Used Car Price Prediction")

car_name = st.text_input("Car Name")

year = st.number_input(
    "Year",
    min_value=2000,
    max_value=2025,
    value=2020
)

present_price = st.number_input(
    "Present Price (Lakhs)",
    min_value=0.0,
    value=5.0
)

kms_driven = st.number_input(
    "Kilometers Driven",
    min_value=0,
    value=10000
)

fuel_type = st.selectbox(
    "Fuel Type",
    ["Petrol", "Diesel", "CNG"]
)

seller_type = st.selectbox(
    "Seller Type",
    ["Dealer", "Individual"]
)

transmission = st.selectbox(
    "Transmission",
    ["Manual", "Automatic"]
)

owner = st.number_input(
    "Owner",
    min_value=0,
    max_value=5,
    value=0
)

if st.button("Predict Price"):

    data = pd.DataFrame({
        "Car_Name": [car_name],
        "Year": [year],
        "Present_Price": [present_price],
        "Kms_Driven": [kms_driven],
        "Fuel_Type": [fuel_type],
        "Seller_Type": [seller_type],
        "Transmission": [transmission],
        "Owner": [owner]
    })

    prediction = model.predict(data)

    st.success(
        f"Predicted Selling Price: ₹ {prediction[0]:.2f} Lakhs"
    )