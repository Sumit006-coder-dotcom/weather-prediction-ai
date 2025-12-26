import streamlit as st
from api_fetch import fetch_weather
from prediction import predict_weather
from visualization import weather_bar_chart, weather_radar_chart,humidity_donut,show_map

st.set_page_config(page_title="Weather Prediction App", layout="centered")

st.markdown(
    "<h1 style='text-align:center;'>🌍 AI Weather Prediction System</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align:center;'>Enter any city in the world "
    "(e.g., Delhi,IN | London,UK | New York,US)</p>",
    unsafe_allow_html=True
)

city = st.text_input("🌐 City Name", placeholder="City or City,CountryCode")

if st.button("🔍 Predict Weather"):
    data = fetch_weather(city)

    if data["error"]:
        st.error(data["message"])
    else:
        prediction = predict_weather(data)

        # Weather Card
        st.markdown(
    f"""
    <div style="padding:15px;border-radius:10px;background:#f0f2f6;">
    <h3>{data.get('city', 'N/A')}, {data.get('country', 'N/A')}</h3>
    🌡 Temperature: {data.get('temperature', 'N/A')} °C <br>
    💧 Humidity: {data.get('humidity', 'N/A')} % <br>
    🌬 Wind Speed: {data.get('wind_speed', 'N/A')} m/s <br>
    📊 Pressure: {data.get('pressure', 'N/A')} hPa
    </div>
    """,
    unsafe_allow_html=True
)

        st.success(f"🤖 Predicted Weather: *{prediction}*")

        # Graphs
        weather_bar_chart(data)
        weather_radar_chart(data)
        humidity_donut(data)
        show_map(data)