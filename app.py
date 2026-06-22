import streamlit as st
import numpy as np
import joblib

# Load model
model = joblib.load("model.pkl")

st.set_page_config(
    page_title="Student Performance Predictor",
    page_icon="🎓"
)

st.title("🎓 Student Performance Predictor")

st.write(
    "Enter student information and predict whether the student will pass or fail."
)

# Inputs
study_time = st.selectbox(
    "Study Time",
    [1, 2, 3, 4],
    help="""
    1 = < 2 hours/week
    2 = 2-5 hours/week
    3 = 5-10 hours/week
    4 = > 10 hours/week
    """
)

absences = st.number_input(
    "Number of Absences",
    min_value=0,
    max_value=100,
    value=5
)

g1 = st.number_input(
    "First Period Grade (G1)",
    min_value=0,
    max_value=20,
    value=10
)

if st.button("Predict"):

    input_data = np.array([
        [study_time, absences, g1]
    ])

    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.success("✅ Student is likely to PASS")
    else:
        st.error("❌ Student is likely to FAIL")