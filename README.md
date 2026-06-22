# 🎓 Student Performance Predictor

## Overview

Student Performance Predictor is a Machine Learning web application built using Python, Scikit-Learn, and Streamlit.

The application predicts whether a student is likely to PASS or FAIL based on:

* Study Time
* Number of Absences
* First Period Grade (G1)

The model uses a Random Forest Classifier trained on the Student Performance Dataset.

---

## Features

Interactive Streamlit Web Application

Student Pass/Fail Prediction

Random Forest Machine Learning Model

Clean and User-Friendly Interface

---

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* Streamlit
* Joblib

---

## Dataset

Student Performance Dataset

Features Used:

* studytime
* absences
* G1

Target:

* PASS (G3 ≥ 10)
* FAIL (G3 < 10)

---

## Model Performance

Model: Random Forest Classifier

Accuracy: 84%

---

## Project Structure

student-performance-predictor/

├── app.py

├── train.py

├── student-mat.csv

├── model.pkl

├── requirements.txt

└── README.md

---

## Installation

Install dependencies:

pip install -r requirements.txt

Train model:

python train.py

Run application:

streamlit run app.py

---

## Screenshot

See the application screenshot below.

---

## Author

Adan Kaleem

Machine Learning & Artificial Intelligence Student
