import joblib
import numpy as np
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

model = joblib.load(os.path.join(BASE_DIR, "models", "random_forest_model.pkl"))
scaler = joblib.load(os.path.join(BASE_DIR, "models", "scaler.pkl"))
le = joblib.load(os.path.join(BASE_DIR, "models", "label_encoder.pkl"))

def predict_weather(data):

    required_keys = ["temperature", "humidity", "pressure", "wind_speed"]
    for key in required_keys:
        if key not in data:
            return "Prediction unavailable"

    features = np.array([[
        data["temperature"],
        data["humidity"],
        data["pressure"],
        data["wind_speed"]
    ]])

    features_scaled = scaler.transform(features)
    prediction = model.predict(features_scaled)

    return le.inverse_transform(prediction)[0]