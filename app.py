import streamlit as st
import tensorflow as tf
import numpy as np

# Load the model
model = tf.keras.models.load_model('Calorie_Predictor (1).h5',compile = False)
# model.summary()

st.title("🧮 Calorie Burn Predictor")
st.write("Enter the required details to predict calories burned:")

# Input fields
gender = st.selectbox("Gender", ["Male", "Female"])
age = st.number_input("Age", min_value=1, max_value=100, value=25)
height = st.number_input("Height (in cm)", min_value=50, max_value=250, value=170)
weight = st.number_input("Weight (in kg)", min_value=20, max_value=200, value=70)
duration = st.number_input("Workout Duration (in minutes)", min_value=1, max_value=300, value=60)
heart_rate = st.number_input("Heart Rate (bpm)", min_value=40, max_value=200, value=120)
body_temp = st.number_input("Body Temperature (°C)", min_value=30.0, max_value=45.0, value=37.0)

gender_val = 1 if gender == "Male" else 0

# Predict button
if st.button("Predict"):
    input_data = np.array([[gender_val, age, height, weight, duration, heart_rate, body_temp]], dtype=np.float32)
    # st.write(f"Input shape: {input_data.shape}")  # Should be (1, 7)
    prediction = model.predict(input_data)
    st.success(f"Estimated Calories Burned: 🔥 **{prediction[0][0]:.2f} kcal**")
