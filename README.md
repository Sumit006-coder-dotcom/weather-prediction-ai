# 🌦 Weather Prediction Using Data Mining and AI

A web-based **Weather Prediction System** that uses **real-time weather data** from the **OpenWeather API** and applies **Machine Learning algorithms** to predict weather conditions such as **Sunny, Cloudy, Rainy, and Snowy**. The application includes **interactive visualizations**, **map-based city location display**, and is deployed on **Streamlit Cloud**.

This project fetches live weather data, performs preprocessing and feature scaling, and passes the data to trained ML models to generate accurate predictions. The results are displayed through a clean and user-friendly web interface with charts and a world map.

The system uses multiple machine learning algorithms including **Logistic Regression**, **Decision Tree Classifier**, and **Random Forest Classifier**, where **Random Forest** achieved the best performance and is used for deployment.

### 🎯 Key Objectives
- Collect real-time weather data using OpenWeather API  
- Perform data preprocessing and feature scaling  
- Train, compare, and evaluate ML models  
- Select the best-performing model  
- Visualize weather parameters using interactive charts  
- Display city location using latitude & longitude on a world map  
- Deploy the application using Streamlit Cloud  

### 🧰 Tech Stack
**Python**, Pandas, NumPy, Scikit-learn, Plotly, Matplotlib, Streamlit, OpenWeather API, Joblib, Git & GitHub

### 📁 Project Structure
    '''bash
    Weather/
    ├── app/ (main.py, api_fetch.py, prediction.py, visualization.py)
    ├── data/ (raw_weather_data.csv, processed_weather_data.csv)
    ├── models/ (trained ML models, scaler, label encoder)
    ├── notebooks/ (preprocessing, training, evaluation)
    ├── requirements.txt
    └── README.md


### ✨ Features
- 🌍 Works for cities worldwide (City or City, CountryCode)
- Real-time weather data fetching
- AI-based weather prediction
- Interactive charts (Bar, Radar, Donut)
- 🗺 World map visualization using latitude & longitude
- Fully web-based and cloud deployed

### ▶ How to Run Locally
    ```bash
    git clone https://github.com/your-username/weather-prediction-ai.git
    cd weather-prediction-ai
    python -m venv venv
    venv\Scripts\activate
    pip install -r requirements.txt
    set OPENWEATHER_API_KEY=your_api_key_here
    streamlit run app/main.py

### 🚀 Deployment

The application is deployed using Streamlit Cloud, and the OpenWeather API key is securely managed using Streamlit Secrets.

### 📈 Results

- Random Forest achieved the highest accuracy
- Interactive visualizations improved data interpretation
- Accurate weather predictions using live data

## 👨‍💻 Author

**Sumit Kumar Karn**
BCA (Hons. with Research)
Passionate about AI, ML & Data Science

