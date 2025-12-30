import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import plotly.graph_objects as go


# 1️.Bar Chart
def weather_bar_chart(forecast):
    if not forecast:
        st.warning("No forecast data available for chart")
        return

    df = pd.DataFrame(forecast)

    if "date" not in df.columns or "temp" not in df.columns:
        st.error(f"Invalid forecast structure: {df.columns.tolist()}")
        return

    fig = px.bar(
        df,
        x="date",
        y="temp",
        text="temp",
        title="🌦 Temperature Forecast (Next Days)",
        labels={"temp": "Temperature (°C)"}
    )

    fig.update_traces(textposition="outside")
    fig.update_layout(title_x=0.5)

    st.plotly_chart(fig, use_container_width=True)


# 2️. Radar(Spider) Chart
def weather_radar_chart(forecast):
    if not forecast:
        st.warning("No forecast data available for radar chart")
        return

    day = forecast[0]

    categories = ["Temperature", "Humidity", "Pressure", "Wind Speed"]
    values = [
        day.get("temp", 0),
        day.get("humidity", 0),
        day.get("pressure", 0) / 10,
        day.get("wind_speed", 0) * 10
    ]

    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
        r=values,
        theta=categories,
        fill='toself',
        name="Weather Pattern"
    ))

    fig.update_layout(
        polar=dict(radialaxis=dict(visible=True)),
        title="🕸 Weather Radar Analysis",
        title_x=0.5
    )

    st.plotly_chart(fig, use_container_width=True)
    

# 3️. Donut Chart (Humidity Focus)
def humidity_donut(forecast):
    day = forecast[0]

    humidity = day.get("humidity", 0)

    labels = ["Humidity", "Remaining"]
    values = [humidity, 100 - humidity]

    fig = go.Figure(data=[go.Pie(
        labels=labels,
        values=values,
        hole=0.5
    )])

    fig.update_layout(
        title="💧 Humidity Level",
        title_x=0.5
    )

    st.plotly_chart(fig, use_container_width=True)
    
#4. World Map Visualization
def show_map(forecast):
    if not forecast:
        st.warning("📍 Location data not available")
        return

    lat = forecast[0]["latitude"]
    lon = forecast[0]["longitude"]

    df = pd.DataFrame({
        "lat": [lat],
        "lon": [lon]
    })

    
    st.map(df)