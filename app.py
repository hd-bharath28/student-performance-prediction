import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load("student_model.pkl")

st.title("Student Performance Prediction System")

st.write("Enter student details to predict final marks:")

studytime = st.slider("Study Time (1-4)", 1, 4)
failures = st.slider("Number of Past Failures", 0, 4)
famrel = st.slider("Family Relationship (1-5)", 1, 5)
freetime = st.slider("Free Time (1-5)", 1, 5)
goout = st.slider("Going Out (1-5)", 1, 5)
Dalc = st.slider("Workday Alcohol Consumption (1-5)", 1, 5)
Walc = st.slider("Weekend Alcohol Consumption (1-5)", 1, 5)
health = st.slider("Health (1-5)", 1, 5)
absences = st.slider("Number of Absences", 0, 50)
G1 = st.slider("First Internal Marks (0-20)", 0, 20)
G2 = st.slider("Second Internal Marks (0-20)", 0, 20)

if st.button("Predict Final Marks"):
    input_data = np.array([[studytime, failures, famrel, freetime, goout,
                             Dalc, Walc, health, absences, G1, G2]])
    
    prediction = model.predict(input_data)
    st.success(f"Predicted Final Marks: {prediction[0]:.2f}")