# 🌦 Weather Prediction Using Data Mining and AI
A web-based Weather Prediction System that uses real-time weather data from the OpenWeather API and applies multiple Machine Learning algorithms to predict weather conditions. The application includes interactive visualizations, map-based location display, and is deployed on Streamlit Cloud.

# Project Overview
This project aims to predict weather conditions such as Sunny, Rainy, and Cloudy using data mining techniques and machine learning models. Real-time weather data is fetched from the OpenWeather API, processed, and passed to trained ML models for prediction. The results are displayed through an interactive web interface.

# Objectives
Collect real-time weather data using OpenWeather API
Perform data preprocessing and feature scaling
Train and compare multiple ML algorithms
Select the best-performing model
Visualize weather parameters using interactive charts
Display city location on a world map
Deploy the application on the web

# Machine Learning Algorithms Used
Logistic Regression – Baseline model
Decision Tree Classifier – Non-linear model
Random Forest Classifier – Ensemble model (best accuracy, used for deployment)

# Tech Stack
Programming Language: Python
Data Mining & ML: Pandas, NumPy, Scikit-learn
Visualization: Plotly, Matplotlib
Web Framework: Streamlit
API: OpenWeather API
Model Persistence: Joblib
Deployment: Streamlit Cloud
Version Control: Git & GitHub

# Project Structure
Weather/
│
├── app/
│   ├── main.py            
│   ├── api_fetch.py         
│   ├── prediction.py        
│   ├── visualization.py     
│
├── data/
│   ├── raw_weather_data.csv
│   ├── processed_weather_data.csv
│
├── models/
│   ├── logistic_model.pkl
│   ├── decision_tree_model.pkl
│   ├── random_forest_model.pkl
│   ├── scaler.pkl
│   ├── label_encoder.pkl
│
├── notebooks/
│   ├── data_collection.ipynb
│   ├── preprocessing.ipynb
│   ├── model_training.ipynb
│   ├── evaluation.ipynb
│
├── requirements.txt
└── README.md

# Features
Works for cities worldwide (City or City,CountryCode)
Real-time weather data fetching
AI-based weather prediction
Interactive graphs (Bar, Radar, Donut charts)
World map visualization using latitude & longitude
Deployed and accessible via web browser

# How to Run Locally
1. Clone the repository
git clone https://github.com/your-username/weather-prediction-ai.git
cd weather-prediction-ai
2. Create and activate virtual environment
python -m venv venv
venv\Scripts\activate  
3. Install dependencies
pip install -r requirements.txt
4. Set OpenWeather API key
Create an environment variable:
set OPENWEATHER_API_KEY=your_api_key_here
5. Run the Streamlit app
streamlit run app/main.py

# Deployment
The application is deployed using Streamlit Cloud.
The OpenWeather API key is securely managed using Streamlit Secrets.
# Results
> Random Forest achieved the highest accuracy among all models
> Interactive visualizations improved data interpretation
> The system successfully predicts weather conditions using live data

# Future Enhancements
> Use LSTM for time-series weather forecasting
> Add weather forecast (next 5–7 days)
> Integrate mobile-friendly UI
> Store historical data automatically (daily collection)

# Sample Inputs
Delhi
Delhi,IN
London
London,UK
New York,US
Tokyo,JP

# Author
> Sumit Kumar Karn
> BCA (Hons. with Research)
> Passionate about AI, ML & Data Science
# Acknowledgements
>OpenWeather API
> Streamlit
> Scikit-learn community
