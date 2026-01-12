## 🌦 Weather Prediction System using Machine Learning & Data Mining

A complete end-to-end **Weather Prediction System** that collects **real-time weather data** using the **OpenWeather API**, performs **preprocessing**, applies multiple **Machine Learning models**, evaluates performance, and visualizes insights.
The system also includes clustering analysis for discovering weather patterns.

## Project Highlights
- Real-time weather data collection
- Data preprocessing and feature scaling
- Multiple ML models comparison
- Clustering analysis using K-Means
- Model evaluation with multiple metrics
- Interactive visualizations
- Modular notebook pipeline
- Ready for deployment and research

## Objectives
- Collect live weather data from OpenWeather API
- Clean and preprocess the dataset
- Train multiple ML models
- Evaluate accuracy, precision, recall, F1-score
- Perform clustering analysis
- Visualize model performance and insights
- Save trained models for reuse

## Machine Learning Models Used
- Model
- Purpose
- Logistic Regression
- Baseline classifier
- Decision Tree Classifier
- Non-linear modeling
- Random Forest Classifier
- Ensemble model (Best Accuracy)
- K-Means Clustering
- Pattern discovery

## Evaluation Metrics
The following metrics are used for evaluation:
- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix
- Classification Report
- MAE
- RMSE
- Model Comparison Graph

## Tech Stack
- Language: Python
- Data Handling: Pandas, NumPy
- Machine Learning: Scikit-learn
- Visualization: Matplotlib, Seaborn
- API: OpenWeather API
- Model Persistence: Joblib
- Environment: Jupyter Notebook, VS Code
- Version Control: Git & GitHub

# Project Structure

WEATHER/
│
├── data/
│   ├── raw_weather_data.csv
│   ├── processed_weather_data.csv
│   └── weather_clustered.csv
│
├── models/
│   ├── logistic_model.pkl
│   ├── decision_tree_model.pkl
│   ├── random_forest_model.pkl
│   ├── scaler.pkl
│   └── label_encoder.pkl
│
├── notebooks/
│   ├── 1_data_collection.ipynb
│   ├── 2_preprocessing.ipynb
│   ├── 3_model_training.ipynb
│   ├── 4_Clustering.ipynb
│   └── 5_evaluation.ipynb
│
├── venv/
├── .gitignore
├── LICENSE.md
├── README.md
└── requirements.txt

## Workflow Pipeline
- Data Collection
- Fetch live weather data using OpenWeather API
- Save into raw_weather_data.csv
- Preprocessing
- Handle missing values
- Feature scaling
- Label encoding
- Save into processed_weather_data.csv
- Model Training
- Train Logistic Regression
- Train Decision Tree
- Train Random Forest
- Save trained models
- Clustering
- Apply K-Means clustering
- Save clustered data
- Evaluation
- Generate metrics
- Plot accuracy comparison
- Confusion matrix and classification report

## How to Run the Project
- Step 1: Clone Repository:
Bash
git clone https://github.com/your-username/weather-prediction.git
cd weather-prediction
- Step 2: Create Virtual Environment:
Bash
python -m venv venv
venv\Scripts\activate
- Step 3: Install Dependencies:
Bash
pip install -r requirements.txt
- Step 4: Run Notebooks in Sequence

**Open Jupyter Notebook or VS Code and execute**:
- 1️. 1_data_collection.ipynb
- 2️. 2_preprocessing.ipynb
- 3️. 3_model_training.ipynb
- 4️. 4_Clustering.ipynb
- 5️. 5_evaluation.ipynb

## Sample Results
- Model
- Accuracy
- Logistic Regression
- ~0.57
- Decision Tree
- ~0.72
- Random Forest
- ~0.81

**Random Forest achieved the highest accuracy.**

## Future Enhancements
- Integrate deep learning (LSTM) for time-series forecasting
- Deploy using Streamlit or Flask
- Add real-time dashboard
- Expand dataset with historical records
- Improve clustering visualization
- Mobile-friendly UI

## Author
Sumit Kumar Karn
BCA (Hons. with Research)
Passionate about AI, Machine Learning & Data Science

## Acknowledgements
OpenWeather API
Scikit-learn Community
Pandas & NumPy
Matplotlib