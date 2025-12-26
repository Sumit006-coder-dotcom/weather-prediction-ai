import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import streamlit as st

def _has_required_weather(data):
    required = ["temperature", "humidity", "pressure", "wind_speed"]
    return all(data.get(k) is not None for k in required)

# -----------------------------
# Bar Chart
# -----------------------------
def weather_bar_chart(data):
    if not _has_required_weather(data):
        st.warning("⚠ Insufficient data for charts")
        return

    df = pd.DataFrame({
        "Parameter": ["Temperature (°C)", "Humidity (%)", "Pressure (hPa)", "Wind Speed (m/s)"],
        "Value": [
            data.get("temperature"),
            data.get("humidity"),
            data.get("pressure"),
            data.get("wind_speed")
        ]
    })

    fig = px.bar(
        df,
        x="Parameter",
        y="Value",
        text="Value",
        title="🌦 Weather Parameters Overview"
    )
    fig.update_traces(textposition="outside")
    fig.update_layout(title_x=0.5)

    st.plotly_chart(fig, use_container_width=True)

# -----------------------------
# Radar Chart
# -----------------------------
def weather_radar_chart(data):
    if not _has_required_weather(data):
        return

    categories = ["Temperature", "Humidity", "Pressure", "Wind Speed"]
    values = [
        data.get("temperature"),
        data.get("humidity"),
        data.get("pressure") / 10,
        data.get("wind_speed") * 10
    ]

    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r=values,
        theta=categories,
        fill="toself",
        name="Weather Pattern"
    ))

    fig.update_layout(
        polar=dict(radialaxis=dict(visible=True)),
        title="🕸 Weather Radar Analysis",
        title_x=0.5
    )

    st.plotly_chart(fig, use_container_width=True)

# -----------------------------
# Donut Chart
# -----------------------------
def humidity_donut(data):
    if data.get("humidity") is None:
        return

    fig = go.Figure(data=[go.Pie(
        labels=["Humidity", "Remaining"],
        values=[data.get("humidity"), 100 - data.get("humidity")],
        hole=0.5
    )])

    fig.update_layout(title="💧 Humidity Contribution", title_x=0.5)
    st.plotly_chart(fig, use_container_width=True)
    
def show_map(data):
    if data.get("latitude") is None or data.get("longitude") is None:
        return

    df = pd.DataFrame({
        "lat": [data.get("latitude")],
        "lon": [data.get("longitude")]
    })

    st.map(df)