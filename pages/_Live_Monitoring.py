import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from utils.graphs import (
    engine_temp_gauge,
    rpm_gauge,
    battery_gauge,
)

st.set_page_config(
    page_title="Live Monitoring",
    page_icon="📡",
    layout="wide"
)

st.title("📡 Live Vehicle Monitoring")
st.markdown("### Real-Time Sensor Monitoring Dashboard")

st.divider()

# -------------------------------------------------
# Sidebar Inputs
# -------------------------------------------------

st.sidebar.header("📥 Live Sensor Inputs")

engine = st.sidebar.slider("🌡 Engine Temperature (°C)", 50.0, 150.0, 85.0)

battery = st.sidebar.slider("🔋 Battery Voltage (V)", 8.0, 15.0, 12.5)

rpm = st.sidebar.slider("⚙ Engine RPM", 500, 7000, 2500)

speed = st.sidebar.slider("🚗 Vehicle Speed", 0, 180, 60)

vibration = st.sidebar.slider("📳 Engine Vibration", 0.0, 10.0, 1.5)

oil = st.sidebar.slider("🛢 Oil Pressure", 10.0, 100.0, 55.0)

coolant = st.sidebar.slider("💧 Coolant Temperature", 40.0, 130.0, 90.0)

current = st.sidebar.slider("🔌 Battery Current", 0.0, 60.0, 15.0)

tire = st.sidebar.slider("🛞 Tire Pressure", 10.0, 50.0, 32.0)

ambient = st.sidebar.slider("🌤 Ambient Temperature", -10.0, 50.0, 30.0)

st.divider()

# -------------------------------------------------
# Live Sensor Cards
# -------------------------------------------------

c1, c2, c3, c4, c5 = st.columns(5)

c1.metric("🌡 Engine", f"{engine:.1f}°C")

c2.metric("🔋 Battery", f"{battery:.1f}V")

c3.metric("⚙ RPM", rpm)

c4.metric("🚗 Speed", f"{speed} km/h")

c5.metric("🛞 Tire", f"{tire} PSI")

st.divider()

# -------------------------------------------------
# Gauges
# -------------------------------------------------

g1, g2, g3 = st.columns(3)

with g1:
    st.plotly_chart(
        engine_temp_gauge(engine),
        use_container_width=True
    )

with g2:
    st.plotly_chart(
        rpm_gauge(rpm),
        use_container_width=True
    )

with g3:
    st.plotly_chart(
        battery_gauge(battery),
        use_container_width=True
    )

st.divider()

# -------------------------------------------------
# Live Sensor Trend
# -------------------------------------------------

st.subheader("📈 Current Sensor Values")

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=[
        "Engine",
        "Battery",
        "RPM",
        "Speed",
        "Oil",
        "Coolant",
        "Current",
        "Tire",
        "Ambient",
    ],
    y=[
        engine,
        battery,
        rpm,
        speed,
        oil,
        coolant,
        current,
        tire,
        ambient,
    ],
    mode="lines+markers",
    line=dict(width=3)
))

fig.update_layout(
    height=450,
    xaxis_title="Sensors",
    yaxis_title="Values"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

# -------------------------------------------------
# Sensor Summary
# -------------------------------------------------

st.subheader("📋 Live Sensor Summary")

df = pd.DataFrame({

    "Sensor":[

        "Engine Temperature",

        "Battery Voltage",

        "RPM",

        "Vehicle Speed",

        "Engine Vibration",

        "Oil Pressure",

        "Coolant Temperature",

        "Battery Current",

        "Tire Pressure",

        "Ambient Temperature"

    ],

    "Current Value":[

        f"{engine:.1f} °C",

        f"{battery:.1f} V",

        rpm,

        f"{speed} km/h",

        vibration,

        oil,

        coolant,

        current,

        tire,

        ambient

    ]

})

st.dataframe(
    df,
    hide_index=True,
    use_container_width=True
)

st.divider()

# -------------------------------------------------
# Sensor Health
# -------------------------------------------------

st.subheader("🟢 Sensor Status")

status = []

status.append(("Engine Temperature", "🟢 Normal" if engine < 100 else "🔴 High"))

status.append(("Battery Voltage", "🟢 Good" if battery >= 12 else "🟡 Low"))

status.append(("RPM", "🟢 Normal" if rpm < 4500 else "🔴 High"))

status.append(("Oil Pressure", "🟢 Good" if oil > 35 else "🔴 Low"))

status.append(("Coolant", "🟢 Normal" if coolant < 100 else "🔴 High"))

status.append(("Tire Pressure", "🟢 Good" if tire >= 30 else "🟡 Low"))

status_df = pd.DataFrame(
    status,
    columns=["Sensor", "Status"]
)

st.table(status_df)

st.success("✅ Live Monitoring Running Successfully")
