import streamlit as st
import joblib
import numpy as np

# Load the model
best_rf_model = joblib.load('./model/best_xgb_model.pkl')

# Streamlit UI for user input
st.title("Insurance Charge Prediction")

age = st.number_input("Age", min_value=18, max_value=100, value=30)
bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, value=25.0)
children = st.number_input("Children", min_value=0, max_value=5, value=0)
smoker = st.selectbox("Smoker", ["No", "Yes"])
region = st.selectbox("Region", ["northeast", "northwest", "southeast", "southwest"])
sex = st.selectbox("Sex", ["female", "male"])

# Preprocessing for inputs (one-hot encoding, etc.)
smoker = 1 if smoker == "Yes" else 0
sex = 1 if sex == "male" else 0
region_northeast, region_northwest, region_southeast, region_southwest = 0, 0, 0, 0
if region == "northeast":
    region_northeast = 1
elif region == "northwest":
    region_northwest = 1
elif region == "southeast":
    region_southeast = 1
else:
    region_southwest = 1

# Prepare the data for prediction
new_data = np.array([[age, bmi, children, smoker, sex, region_northeast, region_northwest, region_southeast]])

# Make prediction
if st.button("Predict"):
    predicted_charge = best_rf_model.predict(new_data)
    st.write(f"Predicted Insurance Charge: {np.exp(predicted_charge[0]):.2f}")
