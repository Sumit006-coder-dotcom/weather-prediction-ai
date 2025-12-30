1. 🌦 Weather Prediction Using Data Mining and AI
A web-based Weather Prediction System that uses real-time weather data from the OpenWeather API and applies Machine Learning algorithms to predict weather conditions.
The application features interactive visualizations, map-based location display, and is deployed using Streamlit Cloud.

2. Project Overview
> This project predicts weather conditions such as Sunny, Cloudy, Rainy, and Snowy using data mining techniques and machine learning models.
> Live weather data is fetched from the OpenWeather API, processed, and passed to trained ML models to generate predictions.
> The results are displayed through an interactive and user-friendly web interface.

3. Objectives
> Collect real-time weather data using OpenWeather API
> Perform data preprocessing and feature scaling
> Train and compare multiple machine learning algorithms
> Select the best-performing model
> Visualize weather parameters using interactive charts
> Display city location on a world map
> Deploy the application on the web using Streamlit Cloud

4. Machine Learning Algorithms Used
> Logistic Regression – Baseline classification model
> Decision Tree Classifier – Non-linear decision-based model
> Random Forest Classifier – Ensemble model
> Best-performing model and used for deployment

5. Tech Stack
> Programming Language: Python
> Data Mining & Machine Learning: Pandas, NumPy, Scikit-learn
> Visualization: Plotly, Matplotlib
> Web Framework: Streamlit
> API: OpenWeather API
> Model Persistence: Joblib
> Deployment: Streamlit Cloud
> Version Control: Git & GitHub

6. Project Structure

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
│   ├── preprocessing.ipynb
│   ├── model_training.ipynb
│   ├── evaluation.ipynb
│
├── requirements.txt
└── README.md

7. Features
> 🌍 Works for cities worldwide (City or City, CountryCode)
> Real-time weather data fetching
> AI-based weather prediction
> Interactive visualizations:
   > Bar Chart
   > Radar Chart
   > Donut Chart
> 🗺 World map visualization using latitude & longitude
> Deployed and accessible via web browser

8. ▶ How to Run Locally
1️. Clone the Repository:
Bash
git clone https://github.com/your-username/weather-prediction-ai.git
cd weather-prediction-ai
2️. Create & Activate Virtual Environment:
Bash
python -m venv venv
venv\Scripts\activate
3️. Install Dependencies:
Bash
pip install -r requirements.txt
4️. Set OpenWeather API Key
Create an environment variable:
Bash
set OPENWEATHER_API_KEY=your_api_key_here
5️. Run the Streamlit App:
Bash
streamlit run app/main.py

9. Deployment
> The application is deployed using Streamlit Cloud.
> The OpenWeather API key is securely managed using Streamlit Secrets.

10. 📈 Results
> Random Forest achieved the highest accuracy among all models
> Interactive visualizations improved data interpretation
> The system successfully predicts weather conditions using live data.

11. Future Enhancements
> Implement LSTM for time-series weather forecasting
> Add 5–7 days weather forecast
> Improve mobile-friendly UI
> Automatically store historical weather data
12. Sample Inputs:
Delhi
Delhi,IN
London
London,UK
New York,US
Tokyo,JP

13. Author
Sumit Kumar Karn
BCA (Hons. with Research)
Passionate about AI, ML & Data Science

14. Acknowledgements
> OpenWeather API
> Streamlit
> Scikit-learn Community