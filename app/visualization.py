import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import streamlit as st

# -----------------------------
# 1️⃣ Attractive Bar Chart
# -----------------------------
def weather_bar_chart(data):
    df = pd.DataFrame({
        "Parameter": ["Temperature (°C)", "Humidity (%)", "Pressure (hPa)", "Wind Speed (m/s)"],
        "Value": [
            data["temperature"],
            data["humidity"],
            data["pressure"],
            data["wind_speed"]
        ]
    })

    fig = px.bar(
        df,
        x="Parameter",
        y="Value",
        text="Value",
        title="🌦 Weather Parameters Overview",
    )

    fig.update_traces(textposition="outside")
    fig.update_layout(title_x=0.5)

    st.plotly_chart(fig, use_container_width=True)


# -----------------------------
# 2️⃣ Radar (Spider) Chart
# -----------------------------
def weather_radar_chart(data):
    categories = ["Temperature", "Humidity", "Pressure", "Wind Speed"]
    values = [
        data["temperature"],
        data["humidity"],
        data["pressure"] / 10,   # scaled for visibility
        data["wind_speed"] * 10  # scaled for visibility
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


# -----------------------------
# 3️⃣ Donut Chart (Humidity Focus)
# -----------------------------
def humidity_donut(data):
    labels = ["Humidity", "Remaining Factors"]
    values = [data["humidity"], 100 - data["humidity"]]

    fig = go.Figure(data=[go.Pie(
        labels=labels,
        values=values,
        hole=0.5
    )])

    fig.update_layout(
        title="💧 Humidity Contribution",
        title_x=0.5
    )

    st.plotly_chart(fig, use_container_width=True)
def show_map(data):
    df = pd.DataFrame({
        "lat": [data["latitude"]],
        "lon": [data["longitude"]],
        "city": [f'{data["city"]}, {data["country"]}']
    })

    st.subheader("🌍 City Location on World Map")
    st.map(df)