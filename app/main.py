import streamlit as st
from api_fetch import fetch_5day_forecast
from prediction import predict_weather
from visualization import weather_bar_chart, weather_radar_chart, humidity_donut, show_map

# Weather emoji mapping
weather_emoji = {
    "Clear": "☀",
    "Clouds": "☁",
    "Rain": "🌧",
    "Snow": "❄",
    "Thunderstorm": "⛈",
    "Drizzle": "🌦",
    "Mist": "🌫",
    "Fog": "🌫"
}

st.title("🌍 Weather Forecast App")

city = st.text_input("Enter City Name")
forecast = fetch_5day_forecast(city)

if forecast is None:
    st.error("City not found or API error")
    
elif isinstance(forecast, str):
    st.error(f"⚠ Network Error: {forecast}")
else:
    st.success("Forecast Generated Successfully")

    for day in forecast:
        emoji = weather_emoji.get(day["weather"], "🌤")
        st.write(
    f"📅 {day['date']} → {emoji} {day['weather']} | 🌡 {day['temp']}°C"
)
    weather_bar_chart(forecast)

    st.subheader("🌀 Weather Distribution")
    weather_radar_chart(forecast)

    st.subheader("💧 Humidity Overview")
    humidity_donut(forecast)

    st.subheader("🗺 Location Map")
    show_map(forecast)

