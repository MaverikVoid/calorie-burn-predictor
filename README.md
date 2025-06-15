# 🔥 Calorie Burn Predictor 

This is a simple Streamlit web application that predicts the number of calories burned during a workout session based on personal metrics like age, weight, duration, heart rate, etc.

## 🚀 Live Demo
👉 [Click here to try it out](https://your-username.streamlit.app)  
_(Replace with your actual deployment link)_

---

## 📦 Features

- Predicts calorie burn using a trained neural network model.
- User-friendly UI built with Streamlit.
- Takes into account gender, age, height, weight, workout duration, heart rate, and body temperature.

---

## 🧠 Tech Stack

- **Frontend**: Streamlit
- **Backend**: TensorFlow/Keras
- **Language**: Python
- **Model Format**: `.keras` (saved Keras Sequential model)

---

## 📊 Input Features

| Feature           | Description                        |
|-------------------|------------------------------------|
| Gender            | Male / Female                      |
| Age               | In years (1-100)                   |
| Height            | In cm (50-250)                     |
| Weight            | In kg (20-200)                     |
| Workout Duration  | In minutes (1-300)                 |
| Heart Rate        | In bpm (40-200)                    |
| Body Temperature  | In Celsius (30.0 - 45.0°C)         |

---

## 🧪 How to Run Locally

1. Clone the repo:
   git clone https://github.com/your-username/calorie-burn-predictor.git
   cd calorie-burn-predictor
2. Install dependencies:
    pip install -r requirements.txt
3.Run the app:
    streamlit run app.py
