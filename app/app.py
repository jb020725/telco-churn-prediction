import streamlit as st
import joblib
from preprocessing import preprocess_input
import components

model = joblib.load('models/gradient_boosting.joblib')

st.title("Telco Customer Churn Prediction")

# Input widgets for numeric
SeniorCitizen = components.selectbox("Senior Citizen", options=[False, True], help_text="Check if customer is a senior citizen")
tenure = components.numeric_input("Tenure (months)", 0, 100, 12)
MonthlyCharges = components.numeric_input("Monthly Charges", 0.0, 1000.0, 70.0)
TotalCharges = components.numeric_input("Total Charges", 0.0, 50000.0, 1000.0)

# Input widgets for categorical
Contract = components.selectbox("Contract", options=["month-to-month", "one year", "two year"])
InternetService = components.selectbox("Internet Service", options=["DSL", "Fiber optic", "No"])
PaymentMethod = components.selectbox("Payment Method", options=["electronic check", "mailed check", "credit card (automatic)"])

# Boolean features
OnlineSecurity = components.checkbox("Online Security")
TechSupport = components.checkbox("Tech Support")
PaperlessBilling = components.checkbox("Paperless Billing")
StreamingMovies = components.checkbox("Streaming Movies")
DeviceProtection = components.checkbox("Device Protection")
StreamingTV = components.checkbox("Streaming TV")

if st.button("Predict Churn"):
    input_data = {
        "SeniorCitizen": 1 if SeniorCitizen else 0,
        "tenure": tenure,
        "MonthlyCharges": MonthlyCharges,
        "TotalCharges": TotalCharges,
        "Contract": Contract,
        "InternetService": InternetService,
        "PaymentMethod": PaymentMethod,
        "OnlineSecurity": OnlineSecurity,
        "TechSupport": TechSupport,
        "PaperlessBilling": PaperlessBilling,
        "StreamingMovies": StreamingMovies,
        "DeviceProtection": DeviceProtection,
        "StreamingTV": StreamingTV,
    }

    df = preprocess_input(input_data)
    prediction = model.predict(df)[0]
    prob = model.predict_proba(df)[0][1]

    st.write(f"Prediction: {'Churn' if prediction == 1 else 'No Churn'}")
    st.write(f"Churn Probability: {prob:.2f}")
