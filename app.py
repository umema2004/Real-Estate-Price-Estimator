import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Load model
model = joblib.load("real_estate_price_model.pkl")

# App title
st.title("🏠 Real Estate Price Estimator")
st.markdown("Predict property prices based on location, size, and features.")

# Input form
with st.form("prediction_form"):
    city = st.selectbox("City", ["Islamabad", "Lahore", "Karachi", "Rawalpindi"])  # add more if needed
    location = st.text_input("Location (e.g., DHA Phase 2)")
    property_type = st.selectbox("Property Type", ["House", "Flat", "Upper Portion", "Lower Portion", "Plot"])
    bedrooms = st.slider("Bedrooms", 1, 10, 3)
    baths = st.slider("Bathrooms", 1, 10, 2)
    area_size = st.number_input("Area Size (in Marla or Sqft)", min_value=1.0, step=0.5)

    submitted = st.form_submit_button("Predict Price")

if submitted:
    # Create input dataframe
    input_df = pd.DataFrame({
        "city": [city],
        "location": [location],
        "property_type": [property_type],
        "bedrooms": [bedrooms],
        "baths": [baths],
        "Area Size": [area_size]
    })

    # Predict
    try:
        prediction = model.predict(input_df)[0]
        st.success(f"Estimated Property Price: Rs {int(prediction):,}")
    except Exception as e:
        st.error("Prediction failed. Make sure the location is similar to training data.")
