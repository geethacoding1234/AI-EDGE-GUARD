import plotly.graph_objects as go
import plotly.express as px
import pandas as pd


# --------------------------------------------------
# Vehicle Health Gauge
# --------------------------------------------------
def health_gauge(health):

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=health,
        title={"text": "Vehicle Health Score"},
        gauge={
            "axis": {"range": [0, 100]},
            "bar": {"color": "darkblue"},
            "steps": [
                {"range": [0, 40], "color": "#ff4d4d"},
                {"range": [40, 70], "color": "#ffd633"},
                {"range": [70, 100], "color": "#66ff66"},
            ],
        },
    ))

    fig.update_layout(height=350)

    return fig


# --------------------------------------------------
# Engine Temperature Gauge
# --------------------------------------------------
def engine_temp_gauge(temp):

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=temp,
        title={"text": "Engine Temperature (°C)"},
        gauge={
            "axis": {"range": [0, 150]},
            "bar": {"color": "red"},
        },
    ))

    fig.update_layout(height=300)

    return fig


# --------------------------------------------------
# RPM Gauge
# --------------------------------------------------
def rpm_gauge(rpm):

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=rpm,
        title={"text": "Engine RPM"},
        gauge={
            "axis": {"range": [0, 7000]},
            "bar": {"color": "green"},
        },
    ))

    fig.update_layout(height=300)

    return fig


# --------------------------------------------------
# Battery Gauge
# --------------------------------------------------
def battery_gauge(voltage):

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=voltage,
        title={"text": "Battery Voltage"},
        gauge={
            "axis": {"range": [0, 15]},
            "bar": {"color": "orange"},
        },
    ))

    fig.update_layout(height=300)

    return fig


# --------------------------------------------------
# Sensor Bar Chart
# --------------------------------------------------
def sensor_chart(engine, battery, rpm, speed,
                 vibration, oil, coolant,
                 current, tire, ambient):

    df = pd.DataFrame({

        "Sensor": [
            "Engine Temp",
            "Battery",
            "RPM",
            "Speed",
            "Vibration",
            "Oil",
            "Coolant",
            "Current",
            "Tire",
            "Ambient"
        ],

        "Value": [
            engine,
            battery,
            rpm,
            speed,
            vibration,
            oil,
            coolant,
            current,
            tire,
            ambient
        ]
    })

    fig = px.bar(
        df,
        x="Sensor",
        y="Value",
        title="Sensor Readings",
        text="Value"
    )

    fig.update_layout(height=450)

    return fig
